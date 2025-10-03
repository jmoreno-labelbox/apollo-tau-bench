# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "069",
        "instruction": "As a Triage Engineer, address the asset validation crash identified as 'crash_007'. Locate the owner of the 'assets/textures/character_models/' directory and their team lead. Initiate a bug in the 'Game Build Pipeline Modernization' project, titled 'Crash on Asset Validation: Oversized Texture', and assign it to the team lead. Link this bug to the 'Create automated game build pipeline' epic as a blocker. Include 'Issue Signature: Asset validation failed' in the new bug as a comment. Additionally, update the crash event's status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_007"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "assets/textures/character_models/"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_002"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_002"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_002"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Crash on Asset Validation: Oversized Texture",
                    "assignee_id": "user_002"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Issue Signature: Asset validation failed"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_007",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "085",
        "instruction": "As a Triage Engineer, address the reported access violation crash, 'crash_001'. Determine the complete path for 'renderer.cpp' to identify the owner and their team lead. Create a new bug in the 'Game Build Pipeline Modernization' project with the title 'Access Violation in Renderer' and assign it to the lead. Connect this bug to the 'Create automated game build pipeline' epic as a related issue. Add 'Access violation in GameEngine.dll' as a comment for the new bug. Furthermore, change the crash event's status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_001"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Access Violation in Renderer",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Access violation in GameEngine.dll"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_001",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "098",
        "instruction": "As a Triage Engineer, a Kubernetes memory crash, 'crash_006', has been reported. Since it's an infrastructure issue, locate the owner of 'multiplayer.cpp' to determine the responsible team and their lead. Establish a new incident in the 'Multi-Platform Game Infrastructure' project titled 'K8s Memory Allocation Failure' and delegate it to the team lead. This incident acts as a blocker for the main cross-platform epic with the title 'Implement cross-platform game infrastructure', so make sure to link them. Include 'Kubernetes resource allocation failed: insufficient memory' as a comment in the newly created incident. To wrap up, change the crash event's status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_006"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "incident",
                    "title": "K8s Memory Allocation Failure",
                    "assignee_id": "user_003",
                    "priority": "critical",
                    "state": "open"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Kubernetes resource allocation failed: insufficient memory"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_006",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "048",
        "instruction": "As a Dev Ops Engineer, the build run 'run_001' has failed. Retrieve the bisect result to pinpoint the cause. Following the bisect, generate a new bug in the 'Game Engine Core Migration' project with the title 'Build Failure due to Missing Declaration in Renderer'. Assign this bug to the owner of the suspect file 'src/game/engine/renderer.cpp'. After that, draft a fix proposal of type 'compilation_issue' titled 'Add Missing TextureManager Declaration' with the description 'A function declaration is missing'. Finally, revise the build run's triage status to 'fix_proposed'.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_001"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Build Failure due to Missing Declaration in Renderer",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_001",
                    "bisect_result_id": "bisect_001",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "compilation_issue",
                    "title": "Add Missing TextureManager Declaration",
                    "description": "A function declaration is missing"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_001",
                    "triage_status": "fix_proposed"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "117",
        "instruction": "As a Triage Engineer, handle the reported Kubernetes crash, identified as 'crash_006'. Identify the owner of 'multiplayer.cpp' and their team lead. Coordinate the creation of a new bug titled 'K8s Crash' within the 'Multi-Platform Game Infrastructure' project specifically for the team lead. Dispatch an email to the team lead with the subject 'New Bug Notification' and the message 'New Kubernetes Crash'. Associate this with the 'Implement cross-platform game infrastructure' epic as a dependency. Include the issue signature from the crash as a comment, and subsequently update the crash event's status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_006"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "K8s Crash",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_003",
                    "recipient_id": "user_003",
                    "title": "New Bug Notification",
                    "message": "New Kubernetes Crash",
                    "channel": "email",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Kubernetes resource allocation failed: insufficient memory"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_006",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "120",
        "instruction": "As a Triage Engineer, manage the access violation crash named 'crash_001'. Initiate a new bug entry in the 'Multi-Platform Game Infrastructure' project titled 'Access Violation on Renderer' for the owner of 'renderer.cpp'. Send an email to the team lead with the title 'Bug Assignment Notification' and the message 'New Access Violation Bug Assigned to your team'. This should be linked as a dependency to the 'Implement cross-platform game infrastructure' epic. Add the crash's issue signature as a comment, and update the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_001"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "Access Violation on Renderer",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_003",
                    "recipient_id": "user_001",
                    "title": "Bug Assignment Notification",
                    "message": "New Access Violation Bug Assigned to your team",
                    "channel": "email"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Access violation in GameEngine.dll at 0x00007FF6A1B2C456"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_001",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "124",
        "instruction": "As a Triage Engineer, you must handle a new compilation crash, 'crash_005'. Start by creating a bug report in the 'Game Build Pipeline Modernization' project, titled 'Renderer Compilation Issue in Build Pipeline', for the owner responsible for 'renderer.cpp'. An email needs to be sent to the team lead with the message 'New Compilation Bug in Build Pipeline' and titled 'Bug Assignment'. This bug should be linked as a blocker to the 'Create automated game build pipeline' epic, include the stack trace from the crash in the comments, and update the crash status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_005"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Renderer Compilation Issue in Build Pipeline",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_002",
                    "recipient_id": "user_001",
                    "title": "Bug Assignment",
                    "message": "New Compilation Bug in Build Pipeline",
                    "channel": "email"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "renderer.cpp:245: issue: 'TextureManager::loadTexture' was not declared in this scope"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_005",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "125",
        "instruction": "As part of your role as a Triage Engineer, handle the recent access violation crash, 'crash_001'. You should create a new entry in the 'Multi-Platform Game Infrastructure' project titled 'Access Violation on Multiple Platforms', for the team lead overseeing 'renderer.cpp'. A Slack notification must be sent to the lead with the message 'New Cross-Platform Bug' and the title 'Bug Assignment'. Ensure this is linked as a related issue to the 'Implement cross-platform game infrastructure' epic, add the issue signature from the crash as a comment, and set the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_001"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "Access Violation on Multiple Platforms",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_003",
                    "recipient_id": "user_001",
                    "title": "Bug Assignment",
                    "message": "New Cross-Platform Bug",
                    "channel": "slack"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Access violation in GameEngine.dll at 0x00007FF6A1B2C456"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_001",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "126",
        "instruction": "As a Triage Engineer, you need to handle a network timeout crash, 'crash_003'. It's essential to document a new bug in the 'Game Security & Anti-Cheat Framework' project with the title 'Network Timeout Vulnerability' directed to the team lead of 'multiplayer.cpp'. You must also send an email to the lead with the subject 'Bug Assignment' and message 'New Network Vulnerability'. Ensure that this is linked as a blocker to the 'Implement anti-cheat system integration' story. Include the stack trace from the crash as a comment, and set the crash status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_003"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Network Timeout Vulnerability",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_004",
                    "recipient_id": "user_003",
                    "title": "Bug Assignment",
                    "message": "New Network Vulnerability",
                    "channel": "email"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "NetworkManager.dll!NetworkManager::checkConnection() + 0x123\nNetworkManager.dll!NetworkManager::update() + 0x456\nGameEngine.dll!GameLoop::update() + 0x789"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_003",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "128",
        "instruction": "As a Triage Engineer, a crash related to asset validation, 'crash_007', requires attention. Document this issue as a new bug in the 'Game Engine Core Migration' project titled 'Asset Crash: Environment Model' directed to the owner of 'assets/models/environment/'. Send an email to the team lead with the message 'New Asset Bug Assigned to Your Team' and subject 'Bug Assignment'. Link this as a related issue to the 'Implement game engine rendering pipeline' story, attach the issue signature from the crash as a comment, and modify the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_007"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "assets/models/environment/"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_007"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_002"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_002"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Asset Crash: Environment Model",
                    "assignee_id": "user_007"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_001",
                    "recipient_id": "user_002",
                    "title": "Bug Assignment",
                    "message": "New Asset Bug Assigned to Your Team",
                    "channel": "email"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement game engine rendering pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_001",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Asset validation failed: Texture size 4096x4096 exceeds maximum 2048x2048"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_007",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "130",
        "instruction": "As a Triage Engineer, 'crash_001', an access violation crash, has been logged and you need to handle it. Coordinate the creation of a bug in the 'Multi-Platform Game Infrastructure' project with the title 'Renderer Access Violation on Multiple Platforms' for the team lead of the 'renderer.cpp' file. Dispatch an email to the lead with the message 'New Cross-Platform Bug' and the title 'Bug Assignment'. This should be associated as a dependency to the 'Implement cross-platform game infrastructure' epic, insert the issue signature from the crash as a comment, and update the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_001"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "Renderer Access Violation on Multiple Platforms",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_003",
                    "recipient_id": "user_001",
                    "title": "Bug Assignment",
                    "message": "New Cross-Platform Bug",
                    "channel": "email"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Access violation in GameEngine.dll at 0x00007FF6A1B2C456"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_001",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "131",
        "instruction": "As a Triage Engineer, 'crash_003', a network timeout crash, has been reported. Proceed to create a new bug in the 'Game Security & Anti-Cheat Framework' project titled 'Network Vulnerability' for the team lead responsible for 'multiplayer.cpp'. Send a Slack notification to the lead with the message 'New Network Security Issue' and the title 'Bug Assignment'. This should be connected as a blocker for the 'Implement anti-cheat system integration' story, add the stack trace from the crash as a comment, and update the crash status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_003"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Network Vulnerability",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_004",
                    "recipient_id": "user_003",
                    "title": "Bug Assignment",
                    "message": "New Network Security Issue",
                    "channel": "slack"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "NetworkManager.dll!NetworkManager::checkConnection() + 0x123\nNetworkManager.dll!NetworkManager::update() + 0x456\nGameEngine.dll!GameLoop::update() + 0x789"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_003",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "132",
        "instruction": "As a Triage Engineer, a report of a Kubernetes crash, 'crash_006', has reached you. It is necessary to open a new bug in the 'Game Analytics & Telemetry Platform' project, titled 'K8s Crash', for the 'multiplayer.cpp' team lead. An email with the subject 'Bug Assignment' and the message 'New K8s Crash' must be dispatched to the lead. Ensure this is linked as a related issue to the 'Implement multi-cloud application architecture' epic, add the issue signature from the crash as a comment, and change the crash event's status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_006"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Analytics & Telemetry Platform"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_005",
                    "type": "bug",
                    "title": "K8s Crash",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_005",
                    "recipient_id": "user_003",
                    "title": "Bug Assignment",
                    "message": "New K8s Crash",
                    "channel": "email"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement multi-cloud application architecture"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_006",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Kubernetes resource allocation failed: insufficient memory"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_006",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "075",
        "instruction": "As a Triage Engineer, a report for 'crash_001' regarding an access violation has come in. Proceed to generate a bug in the 'Game Build Pipeline Modernization' project with the title 'Access Violation in Renderer', assigning it to the 'renderer.cpp' file lead. Since it appears to relate to the main build pipeline epic titled 'Create automated game build pipeline', ensure they are linked. Insert 'Access violation in GameEngine.dll' into the bug report's comments for context, followed by marking the crash as 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_001"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Access Violation in Renderer",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Access violation in GameEngine.dll"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_001",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "133",
        "instruction": "As a Triage Engineer, handle an asset validation crash, 'crash_007'. Initiate a new bug in the 'Game Engine Core Migration' project titled 'Asset Crash' for the individual responsible for the 'assets/models/environment/' file. Coordinate a notification to the slack channel for the file's team lead with the message 'New Asset Bug' and the title 'Bug Assignment'. Additionally, link this as a dependency to the 'Implement game engine rendering pipeline' story, incorporate the issue signature from the crash as a comment, and update the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_007"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "assets/models/environment/"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_002"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Asset Crash",
                    "assignee_id": "user_007"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_001",
                    "recipient_id": "user_002",
                    "title": "Bug Assignment",
                    "message": "New Asset Bug",
                    "channel": "slack"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement game engine rendering pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_001",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Asset validation failed: Texture size 4096x4096 exceeds maximum 2048x2048"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_007",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "121",
        "instruction": "As a Triage Engineer, address a network timeout crash, 'crash_003'. Develop a new bug in the 'Game Security & Anti-Cheat Framework' project with the title 'Network Timeout Security Concern' for the team lead of 'multiplayer.cpp'. Relay a notification to slack to the lead with the message 'New network security bug filed' and the title 'Bug Assignment'. Connect this bug as related to the 'Implement anti-cheat system integration' story, append the stack trace from the crash as a comment, and revise the crash status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_003"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Network Timeout Security Concern",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_004",
                    "recipient_id": "user_003",
                    "title": "Bug Assignment",
                    "message": "New network security bug filed",
                    "channel": "slack"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "NetworkManager.dll!NetworkManager::checkConnection() + 0x123\nNetworkManager.dll!NetworkManager::update() + 0x456\nGameEngine.dll!GameLoop::update() + 0x789"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_003",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "118",
        "instruction": "Act as a Triage Engineer. There has been an asset validation crash, 'crash_007'. Identify the owner of the 'assets/textures/character_models/' directory and ascertain their team lead. Initiate a new bug entry within the 'Game Security & Anti-Cheat Framework' project, with the title 'Asset Validation Security Issue', designated for the team lead. Additionally, dispatch a notification via slack containing the message 'New Asset Security Bug' and the title 'New Bug Notification'. Connect this as a blocker to the 'Implement anti-cheat system integration' story. Include the crash issue signature as a comment, and subsequently change the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_007"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "assets/textures/character_models/"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_002"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_002"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_002"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Asset Validation Security Issue",
                    "assignee_id": "user_002"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_004",
                    "recipient_id": "user_002",
                    "title": "New Bug Notification",
                    "message": "New Asset Security Bug",
                    "channel": "slack",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Asset validation failed: Texture size 4096x4096 exceeds maximum 2048x2048"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_007",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "119",
        "instruction": "Function as a Triage Engineer. A compilation crash, 'crash_005', has been documented. Within the 'Game Build Pipeline Modernization' project, formulate a new bug titled 'Build Pipeline Blocked by Compilation Crash' for the 'renderer.cpp' team lead. Furthermore, send a Slack notification to the team lead with the message 'New build-blocking bug assigned' and the title 'New Build Blocker'. Ensure this bug is associated as a blocker to the 'Create automated game build pipeline' epic. Add a comment with the first line from the crash's stack trace and update the crash event status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_005"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Build Pipeline Blocked by Compilation Crash",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_002",
                    "recipient_id": "user_001",
                    "title": "New Build Blocker",
                    "message": "New build-blocking bug assigned",
                    "channel": "slack"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "renderer.cpp:245: issue: 'TextureManager::loadTexture' was not declared in this scope"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_005",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "095",
        "instruction": "As a Triage Engineer, a severe access violation, 'crash_001', has been reported to you. Determine the owner of the 'renderer.cpp' file and identify their team lead. Proceed to create a critical incident ticket within the 'Game Analytics & Telemetry Platform' project, considering this crash could affect our data collection. Name it 'Critical Access Violation in Renderer'. Assign this incident to the team lead you have identified. This incident pertains to the main analytics epic, so make sure to link it to the 'Implement multi-cloud application architecture' story. Additionally, include the crash fingerprint as a comment for tracking and change the crash event's status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_001"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Analytics & Telemetry Platform"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_005",
                    "type": "incident",
                    "title": "Critical Access Violation in Renderer",
                    "assignee_id": "user_001",
                    "priority": "critical"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement multi-cloud application architecture"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_006",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "renderer_character_load_access_violation_xyz"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_001",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "089",
        "instruction": "As a Triage Engineer, you have been notified about the recurrent compilation crash 'crash_005'. Identify the owner of the 'renderer.cpp' file. Subsequently, find the team lead for that owner. Construct a bug within the 'Game Build Pipeline Modernization' project titled 'Recurring Compilation Crash' and allocate it to the team lead. Locate the 'Create automated game build pipeline' epic and link this bug as a dependency. Add the crash event's stack trace as a comment. Furthermore, set the crash's status to 'reopened'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_005"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Recurring Compilation Crash",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: renderer.cpp:245: issue: 'TextureManager::loadTexture' was not declared in this scope\nrenderer.cpp:245: note: suggested alternative: 'TextureManager::loadTextureAsync'"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_005",
                    "status": "reopened"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "107",
        "instruction": "As a Triage Engineer, a Kubernetes crash, 'crash_006', has been flagged. Identify the owner of 'multiplayer.cpp' and their team lead. Generate a new bug entry in the 'Game Security & Anti-Cheat Framework' project with the title 'K8s Deployment Failure' for the team lead. Dispatch an email to the team lead with the content 'New K8s Bug' and subject 'New Bug Notification'. This bug is obstructing the 'Implement anti-cheat system integration' story, therefore, connect them. Insert the issue signature from the crash as a comment. Lastly, adjust the crash's status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_006"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "K8s Deployment Failure",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_004",
                    "recipient_id": "user_003",
                    "title": "New Bug Notification",
                    "message": "New K8s Bug",
                    "channel": "email",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Kubernetes resource allocation failed: insufficient memory"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_006",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "101",
        "instruction": "As a Triage Engineer, you have a report of a new crash, 'crash_003', concerning network timeouts. Locate the owner of the 'multiplayer.cpp' file and their team lead. Formulate a new bug report in the 'Multi-Platform Game Infrastructure' project titled 'Network Timeout Crash' and allocate it to the file's owner. Subsequently, send an email notification to the team lead to notify them of the new bug assigned to their team member, using the message 'New Bug Assigned to Your Team'. Relate this bug as a dependency to the 'Implement cross-platform game infrastructure' epic. Finally, append 'Stack Trace: NetworkManager.dll' as a comment to the bug and classify the crash incident as 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_003"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "Network Timeout Crash",
                    "assignee_id": "user_008"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_003",
                    "recipient_id": "user_003",
                    "title": "New Bug Assigned to Your Team",
                    "message": "New Bug Assigned to Your Team",
                    "channel": "email",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: NetworkManager.dll"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_003",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "102",
        "instruction": "As a Release Manager, handle a situation where deployment 'deploy_004' failed, resulting in a rollback. Initiate a new critical incident within the appropriate project, titled 'Deployment Failure and Rollback Initiated for deploy_004'. Delegate the incident to the team lead of the 'Game Server Operations Team'. A Slack notification about the incident alert should be sent to the team lead, containing the title 'Critical Incident: Deployment Failure' and mirror the same message as the incident title. Additionally, append a comment to the newly created incident stating 'Rolling back to version v1.0.4 as per rollback plan.'.",
        "actions": [
            {
                "name": "GetDeploymentById",
                "arguments": {
                    "id": "deploy_004"
                },
            },
            {
                "name": "GetPipelineById",
                "arguments": {
                    "id": "pipe_005"
                },
            },
            {
                "name": "GetProjectById",
                "arguments": {
                    "id": "proj_003"
                },
            },
            {
                "name": "GetTeamByName",
                "arguments": {
                    "name": "Game Server Operations Team"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_005"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "incident",
                    "title": "Deployment Failure and Rollback Initiated for deploy_004",
                    "assignee_id": "user_005",
                    "priority": "critical"
                },
            },
            {
                "name": "GetRollbackByDeploymentId",
                "arguments": {
                    "deployment_id": "deploy_004"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_003",
                    "recipient_id": "user_005",
                    "title": "Critical Incident: Deployment Failure",
                    "message": "Deployment Failure and Rollback Initiated for deploy_004",
                    "channel": "slack",
                    "notification_type": "incident_alert"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Rolling back to version v1.0.4 as per rollback plan."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "103",
        "instruction": "In your role as a Triage Engineer, manage the compilation crash identified as 'crash_005'. Locate the owner of 'renderer.cpp' along with their team lead. Formulate a bug in the 'Game Security & Anti-Cheat Framework' project, titled 'Compilation Failure Blocking Security Analysis', and allocate it to the owner. Furthermore, dispatch a bug_assignment Slack notification to the team lead, titled 'High-Priority Bug Assigned to Your Team' with the message 'Compilation Failure Blocking Security Analysis'. As this issue obstructs the primary anti-cheat story titled 'Implement anti-cheat system integration', ensure they are linked appropriately. Update the crash event's status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_005"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Compilation Failure Blocking Security Analysis",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_004",
                    "recipient_id": "user_001",
                    "title": "High-Priority Bug Assigned to Your Team",
                    "message": "Compilation Failure Blocking Security Analysis",
                    "channel": "slack",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_005",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "104",
        "instruction": "You are a Dev Ops Engineer. A performance regression was detected in build 'run_007'. Handle the creation of a high-priority bug in the 'Game Engine Core Migration' project titled 'Performance Regression in Renderer' for the owner of the bisect result. Send a bug_assignment email to the owner with the title 'Action Required: Performance Regression' and a message 'Performance Regression in Renderer'. Coordinate the creation of a fix proposal of type 'performance_regression' titled 'Optimize Texture Loading Performance' with the description 'Address frame rate drop caused by recent renderer changes'. Additionally, update the build's triage status to 'fix_proposed'.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_007"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_007"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_004"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Performance Regression in Renderer",
                    "assignee_id": "user_001",
                    "priority": "high"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_001",
                    "recipient_id": "user_001",
                    "title": "Action Required: Performance Regression",
                    "message": "Performance Regression in Renderer",
                    "channel": "email",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_007",
                    "bisect_result_id": "bisect_004",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "performance_regression",
                    "title": "Optimize Texture Loading Performance",
                    "description": "Address frame rate drop caused by recent renderer changes"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_007",
                    "triage_status": "fix_proposed"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "106",
        "instruction": "You are a Triage Engineer. An access violation crash, 'crash_001', has occurred. Coordinate the creation of a new bug in the 'Game Build Pipeline Modernization' project titled 'Access Violation in Renderer' for the file owner of 'renderer.cpp'. Send a notification about the bug assignment to slack to the team lead with the message 'New Access Violation Bug' and title 'New Bug Notification'. This bug should be linked as related to the 'Create automated game build pipeline' epic. Include the crash's issue signature as a comment, and subsequently, update the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_001"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Access Violation in Renderer",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_002",
                    "recipient_id": "user_001",
                    "title": "New Bug Notification",
                    "message": "New Access Violation Bug",
                    "channel": "slack",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Access violation in GameEngine.dll at 0x00007FF6A1B2C456"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_001",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "109",
        "instruction": "As a Triage Engineer, handle a compilation crash, 'crash_005', that has resurfaced. Identify the owner of 'renderer.cpp' and their team lead. Proceed to create a new bug in the 'Game Security & Anti-Cheat Framework' project with the title 'Recurring Compilation Failure' and assign it to the team lead. Dispatch an email notification to the team lead with the message 'Recurring Compilation Bug' and title 'New Bug Notification'. Since this is a dependency for the 'Implement anti-cheat system integration' story, ensure they are linked. Incorporate the stack trace from the crash as a comment and subsequently update the crash's status to 'reopened'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_005"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Recurring Compilation Failure",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_004",
                    "recipient_id": "user_001",
                    "title": "New Bug Notification",
                    "message": "Recurring Compilation Bug",
                    "channel": "email",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "renderer.cpp:245: issue: 'TextureManager::loadTexture' was not declared in this scope"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_005",
                    "status": "reopened"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "110",
        "instruction": "As a Triage Engineer, manage a newly logged access violation crash, 'crash_001'. Create a bug in the 'Game Analytics & Telemetry Platform' project titled 'Renderer Access Violation' for the team lead of ''renderer.cpp'' file. Transmit a bug assignment notification to slack with the message 'New Renderer Crash' and title 'New Bug Notification'. Make sure to link this bug as a blocker to the 'Implement multi-cloud application architecture' epic. Additionally, add the crash's issue signature as a comment and change the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_001"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Analytics & Telemetry Platform"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_005",
                    "type": "bug",
                    "title": "Renderer Access Violation",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_005",
                    "recipient_id": "user_001",
                    "title": "New Bug Notification",
                    "message": "New Renderer Crash",
                    "channel": "slack",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement multi-cloud application architecture"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_006",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Access violation in GameEngine.dll at 0x00007FF6A1B2C456"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_001",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "111",
        "instruction": "As a Triage Engineer, handle the network crash 'crash_003' that has been reported. Initiate a new bug entry within the 'Game Engine Core Migration' project, titled 'Network Crash in Multiplayer', and allocate it to the team lead responsible for the 'multiplayer.cpp' file. Dispatch an email notification with the subject 'New Bug Notification' and the message 'New Network Crash'. Ensure this bug is established as a dependency of the 'Implement game engine rendering pipeline' story. Additionally, append the stack trace from the crash as a comment, and subsequently revise the crash status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_003"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Network Crash in Multiplayer",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_001",
                    "recipient_id": "user_003",
                    "title": "New Bug Notification",
                    "message": "New Network Crash",
                    "channel": "email",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement game engine rendering pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_001",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "NetworkManager.dll!NetworkManager::checkConnection() + 0x123\nNetworkManager.dll!NetworkManager::update() + 0x456\nGameEngine.dll!GameLoop::update() + 0x789"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_003",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "112",
        "instruction": "Handle the triaging of a Kubernetes crash 'crash_006'. Initiate a new bug in the 'Game Build Pipeline Modernization' project titled 'K8s Crash' for the team lead of the 'multiplayer.cpp' file. Additionally, send a notification to Slack with the subject 'New Bug Notification' and the message 'New K8s Crash'. Correlate this as a related issue to the 'Create automated game build pipeline' epic. Furthermore, incorporate the crash's issue signature as a comment, and subsequently modify the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_006"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "K8s Crash",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_002",
                    "recipient_id": "user_003",
                    "title": "New Bug Notification",
                    "message": "New K8s Crash",
                    "channel": "slack",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Kubernetes resource allocation failed: insufficient memory"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_006",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "113",
        "instruction": "There is an asset validation crash (ID: crash_007) that requires triaging. You should create a new bug in the 'Multi-Platform Game Infrastructure' project with the title 'Asset Validation Failure' and assign it to the team lead responsible for the 'assets/textures/character_models/' directory. An email needs to be sent to the team lead with the subject 'New Bug Notification' and the message 'New Asset Bug' regarding this issue. As this is impeding the 'Implement cross-platform game infrastructure' epic, ensure they are linked properly. Additionally, incorporate the crash's issue signature as a comment on the bug and update the crash event status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_007"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "assets/textures/character_models/"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_002"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_002"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_002"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "Asset Validation Failure",
                    "assignee_id": "user_002"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_003",
                    "recipient_id": "user_002",
                    "title": "New Bug Notification",
                    "message": "New Asset Bug",
                    "channel": "email",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Asset validation failed: Texture size 4096x4096 exceeds maximum 2048x2048"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_007",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "114",
        "instruction": "Attention is required for a compilation crash (ID: crash_005) that has just been reported. Proceed to create a new bug in the 'Game Analytics & Telemetry Platform' project titled 'Renderer Compilation Issue' for the team lead associated with 'renderer.cpp'. Deliver a bug assignment notification to the slack channel with the subject 'New Bug Notification' and the message 'New Compilation Issue'. This bug forms a dependency for the 'Implement multi-cloud application architecture' epic, so ensure they are linked appropriately. Furthermore, add the first line of the stack trace from the crash as a comment on the bug and change the crash status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_005"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Analytics & Telemetry Platform"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_005",
                    "type": "bug",
                    "title": "Renderer Compilation Issue",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_005",
                    "recipient_id": "user_001",
                    "title": "New Bug Notification",
                    "message": "New Compilation Issue",
                    "channel": "slack",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement multi-cloud application architecture"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_006",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "renderer.cpp:245: issue: 'TextureManager::loadTexture' was not declared in this scope"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_005",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "116",
        "instruction": "You are a Triage Engineer. A network timeout crash, 'crash_003', has been reported and needs your attention. Generate a new bug in the 'Game Build Pipeline Modernization' project titled 'Network Timeout in Build Pipeline' for the team lead of 'multiplayer.cpp' file. Notify slack with the message 'New Network Timeout Bug' and title 'New Bug Notification'. Connect this bug as a blocker to the 'Create automated game build pipeline' epic. Additionally, include the stack trace from the crash as a comment, and subsequently update the crash status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_003"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Network Timeout in Build Pipeline",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_002",
                    "recipient_id": "user_003",
                    "title": "New Bug Notification",
                    "message": "New Network Timeout Bug",
                    "channel": "slack",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "NetworkManager.dll!NetworkManager::checkConnection() + 0x123\nNetworkManager.dll!NetworkManager::update() + 0x456\nGameEngine.dll!GameLoop::update() + 0x789"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_003",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "051",
        "instruction": "You are a Triage Engineer. Crash report 'crash_005' has been filed for a compilation issue. A new bug must be generated in the 'Game Engine Core Migration' project with the title 'Compilation Crash in Renderer' and assigned to the team lead of the suspect file 'renderer.cpp'. Locate the original 'Implement game engine rendering pipeline' story and associate this new bug as being blocked by it. A comment needs to be added to the new bug with the stack trace from the crash event with 'Stack Trace: renderer.cpp'. Also, the status of the crash event should be updated to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_005"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Compilation Crash in Renderer",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement game engine rendering pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_001",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: renderer.cpp"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_005",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "053",
        "instruction": "As a Dev Ops Engineer, a performance regression has been detected in build 'run_007'. Determine the bisect outcome and identify the responsible owner. In the 'Game Engine Core Migration' project, create a new bug titled 'Performance Regression in Texture System' and assign it to the relevant owner. Next, coordinate a fix proposal categorized as 'performance_regression' with the title 'Optimize Texture Loading' and include a description saying 'Implement texture caching to fix frame rate drop'. Finally, ensure the build's triage status is updated to 'fix_proposed'.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_007"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_007"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_004"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Performance Regression in Texture System",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_007",
                    "bisect_result_id": "bisect_004",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "performance_regression",
                    "title": "Optimize Texture Loading",
                    "description": "Implement texture caching to fix frame rate drop"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_007",
                    "triage_status": "fix_proposed"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "054",
        "instruction": "Serving as a Triage Engineer, an issue with 'AIPathfindingTest::NavigationMeshTest' has been raised due to a test failure. Generate a fingerprint for this test failure. If no existing bugs match this fingerprint, locate the owner of the 'src/game/ai/pathfinding.h' file. Proceed to create a new bug in the 'Game Engine Core Migration' project titled 'AI Test Failure: Navmesh Generation Timeout'. Assign this bug, with the comment 'Test timed out', to the file's owner.",
        "actions": [
            {
                "name": "GetTestResultById",
                "arguments": {
                    "id": "test_result_002"
                },
            },
            {
                "name": "GenerateFingerprintForTestResult",
                "arguments": {
                    "test_result_id": "test_result_002"
                },
            },
            {
                "name": "FindBugByCrashFingerprint",
                "arguments": {
                    "crash_fingerprint": "ai_navmesh_generation_timeout_abc"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/ai/pathfinding.h"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "AI Test Failure: Navmesh Generation Timeout",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Test timed out"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "055",
        "instruction": "Handle the role of a Triage Engineer. Crash report 'crash_005' suggests a compilation issue. Identify the full path for the module 'renderer.cpp' from the crash's stack trace to determine the owner and their team. Coordinate the creation of a new critical bug in the 'Game Engine Core Migration' project with the title 'Critical Compilation Crash in Renderer' and delegate it to the team lead of the respective team. Insert a comment stating 'Associated crash fingerprint: build_compilation_missing_declaration_xyz' into the bug. This bug must be connected to the primary 'Implement game engine rendering pipeline' story as a blocker and have the crash event's status updated to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_005"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Critical Compilation Crash in Renderer",
                    "assignee_id": "user_001",
                    "priority": "critical"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Associated crash fingerprint: build_compilation_missing_declaration_xyz"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement game engine rendering pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_001",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_005",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "058",
        "instruction": "Coordinate the responsibilities of a Dev Ops Engineer. The 'run_005' build has failed due to an integration issue. Discover the bisect result, and use this to identify the owner of the first suspect file. Initiate a new bug in the 'Game Engine Core Migration' project titled 'Integration Failure in Connection Manager' and allocate it to this owner. Additionally, establish a fix proposal for the 'integration_failure' with the title 'Fix Connection Timeout Logic' and provide a description of 'The connection manager is timing out during integration tests'. Lastly, you should append the new bug to the main 'Multiplayer' epic (work_004) and revise the build's triage status to 'fix_proposed'.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_005"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_005"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Integration Failure in Connection Manager",
                    "assignee_id": "user_008"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_005",
                    "bisect_result_id": "bisect_003",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "integration_failure",
                    "title": "Fix Connection Timeout Logic",
                    "description": "The connection manager is timing out during integration tests"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "epic"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_005",
                    "triage_status": "fix_proposed"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "061",
        "instruction": "As a Triage Engineer, a new crash, 'crash_001', has been reported for an access violation. Please create a new bug report in the 'Game Build Pipeline Modernization' project with the title 'Access Violation in Renderer' and assign it to the team lead of the 'renderer.cpp' file implicated in the crash. Locate the 'Create automated game build pipeline' epic and link this new bug to it as a related issue. Add a comment 'Issue Signature: Access violation' to the bug. Finally, update the crash event's status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_001"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Access Violation in Renderer",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Issue Signature: Access violation"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_001",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "062",
        "instruction": "As a Triage Engineer, a network timeout crash, 'crash_003', has occurred. Determine the owner of 'multiplayer.cpp' and their team lead. Register a new bug in the 'Multi-Platform Game Infrastructure' project titled 'Network Timeout During Gameplay' and assign it to the team lead. Connect this bug as a dependency to the 'Implement cross-platform game infrastructure' epic. Include 'Stack Trace: NetworkManager.dll' as a comment to the bug. Lastly, update the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_003"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "Network Timeout During Gameplay",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: NetworkManager.dll"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_003",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "063",
        "instruction": "As a Triage Engineer, handle the crash 'crash_006', which points to a Kubernetes problem. Considering it's an infrastructure concern, identify the owner of 'multiplayer.cpp' to pinpoint the responsible team and their leader. Coordinate the creation of a new bug in the 'Game Security & Anti-Cheat Framework' project, titled 'Kubernetes Deployment Crash,' and assign it to the team lead. This newly created bug must be linked as being blocked by the 'Implement anti-cheat system integration' story. Include a comment stating 'Kubernetes resource allocation failed: insufficient memory' in the new bug. Finally, update the crash event status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_006"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Kubernetes Deployment Crash",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Kubernetes resource allocation failed: insufficient memory"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_006",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "064",
        "instruction": "In your role as a Triage Engineer, address the asset validation crash 'crash_007'. Initiate the creation of a new bug in the 'Game Engine Core Migration' project, named 'Asset Validation Failure: Texture Size', and allocate it to the team lead of the 'assets/textures/character_models/' asset folder. Link this bug to the 'Implement game engine rendering pipeline' story, marking it as a related issue. Add a comment, 'Issue Signature: Asset validation failed', to the bug. Additionally, you should adjust the crash event status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_007"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "assets/textures/character_models/"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_002"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_002"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_002"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Asset Validation Failure: Texture Size",
                    "assignee_id": "user_002"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement game engine rendering pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_001",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Issue Signature: Asset validation failed"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_007",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "065",
        "instruction": "As a Triage Engineer, the compilation crash 'crash_005' has once more been recorded. Locate the owner of the 'renderer.cpp' file. Subsequently, identify the team lead of this owner. Organize a bug entry in the 'Game Build Pipeline Modernization' project with the title 'Recurring Compilation Crash' and designate it to the team lead. Search for the 'Create automated game build pipeline' epic and link this bug as its dependency. Include 'Stack Trace: renderer.cpp' in the comments on the bug. Lastly, modify the status of the crash to 'reopened'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_005"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Recurring Compilation Crash",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: renderer.cpp"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_005",
                    "status": "reopened"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "066",
        "instruction": "As part of your duties as a Triage Engineer, a new access violation crash named 'crash_001' has been documented. Determine the owner of the 'renderer.cpp' file along with their team lead. Arrange for a bug entry in the 'Multi-Platform Game Infrastructure' project with the heading 'Access Violation on Character Load' and allocate it to the team lead. Connect this bug to the 'Implement cross-platform game infrastructure' epic, marking it as a blocker. Insert 'Issue Signature: Access violation in GameEngine.dll' as a comment under the bug. Conclude by updating the crash event's status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_001"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "Access Violation on Character Load",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Issue Signature: Access violation in GameEngine.dll"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_001",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "001",
        "instruction": "As a Dev Ops Engineer, handle a failed critical build 'run_001'. Develop a bug report titled 'Build failure in renderer on feature/new-renderer', ensuring the bug owner is the owner of the bisect linked to the critical bug. Additionally, draft a fix proposal titled 'Fix missing TextureManager::loadTexture declaration', with the description 'Add missing function declaration in texture_manager.h header file.' and classify it as 'compilation_issue'. Lastly, update the build run status to resolved.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_001"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_001"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Build failure in renderer on feature/new-renderer",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_001",
                    "bisect_result_id": "bisect_001",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "compilation_issue",
                    "title": "Fix missing TextureManager::loadTexture declaration",
                    "description": "Add missing function declaration in texture_manager.h header file."
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_001",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "002",
        "instruction": "In your role as a Security Engineer, manage a critical vulnerability detected in the 'game-engine' repository's dependencies for CVE-2024-2345. Formulate a critical bug report for this vulnerability with the title 'Critical Security Vulnerability: CVE-2024-2345 in Docker', delegate it to the appropriate team lead, and categorize it as a security issue. Subsequently, set the vulnerability status to 'triaged'.",
        "actions": [
            {
                "name": "SearchVulnerabilitiesByCve",
                "arguments": {
                    "cve": "CVE-2024-2345"
                },
            },
            {
                "name": "GetRepositoryByName",
                "arguments": {
                    "name": "game-engine"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "FindProjectOwnerTeam",
                "arguments": {
                    "project_id": "proj_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Critical Security Vulnerability: CVE-2024-2345 in Docker",
                    "assignee_id": "user_001",
                    "priority": "critical"
                },
            },
            {
                "name": "GetLabelByName",
                "arguments": {
                    "name": "security"
                },
            },
            {
                "name": "AddLabelToWorkItem",
                "arguments": {
                    "work_item_id": "work_028",
                    "label_id": "label_004"
                },
            },
            {
                "name": "UpdateVulnerabilityStatus",
                "arguments": {
                    "id": "vuln_006",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "004",
        "instruction": "As a Triage Engineer, you have received a crash report, 'crash_004', which seems to be a repeat of a known issue. Please generate a new bug report under the title '[Duplicate] Multiplayer Connection Timeout' in the 'Game Engine Core Migration' project for this recent crash. Then, close the bug and leave the comment 'Closing as a duplicate.' Additionally, remember to update the status of the crash report to duplicate.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_004"
                },
            },
            {
                "name": "FindCrashesByCrashFingerprint",
                "arguments": {
                    "crash_fingerprint": "network_connection_timeout_30s_xyz"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "[Duplicate] Multiplayer Connection Timeout"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Closing as a duplicate."
                },
            },
            {
                "name": "UpdateWorkItemState",
                "arguments": {
                    "id": "work_028",
                    "new_state": "closed"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_004",
                    "status": "duplicate"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "006",
        "instruction": "In your role as a Release Manager, a failure has occurred with the deployment 'deploy_004' to production. An immediate rollback is required. Locate the plan for rolling back this deployment and carry it out. After initiating the rollback process, open a critical incident ticket entitled 'Critical Rollback: Deployment deploy_004 failed' and assign it to the team lead of 'Game Server Operations Team' within the 'Game Analytics & Telemetry Platform' project for thorough investigation.",
        "actions": [
            {
                "name": "GetDeploymentById",
                "arguments": {
                    "id": "deploy_004"
                },
            },
            {
                "name": "GetRollbackByDeploymentId",
                "arguments": {
                    "deployment_id": "deploy_004"
                },
            },
            {
                "name": "CreateDeployment",
                "arguments": {
                    "pipeline_id": "pipe_005",
                    "environment_id": "env_010",
                    "deployed_by": "user_004",
                    "version": "v1.0.4",
                    "status": "in_progress"
                },
            },
            {
                "name": "GetTeamByName",
                "arguments": {
                    "name": "Game Server Operations Team"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_005"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Analytics & Telemetry Platform"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_005",
                    "type": "incident",
                    "title": "Critical Rollback: Deployment deploy_004 failed",
                    "assignee_id": "user_005",
                    "priority": "critical",
                    "state": "open"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "012",
        "instruction": "You are a Triage Engineer. Crash report 'crash_002' has been received. It seems to be a duplicate of an existing crash. Generate a new bug for this specific instance with the title '[Duplicate Crash] Character Load Access Violation on RTX 3070', assigning it to the same individual as the original, or to None if there is no assignee on the original bug. Connect the new bug to the original as a duplicate. Additionally, you should close the new bug and change the crash event's status to 'duplicate'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_002"
                },
            },
            {
                "name": "FindBugByCrashFingerprint",
                "arguments": {
                    "crash_fingerprint": "renderer_character_load_access_violation_xyz"
                },
            },
            {
                "name": "GetWorkItemAssignee",
                "arguments": {
                    "id": "work_026"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "[Duplicate Crash] Character Load Access Violation on RTX 3070",
                    "assignee_id": null
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_026",
                    "child_id": "work_028",
                    "link_type": "duplicate"
                },
            },
            {
                "name": "UpdateWorkItemState",
                "arguments": {
                    "id": "work_028",
                    "new_state": "closed"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_002",
                    "status": "duplicate"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "014",
        "instruction": "You are a Dev Ops Engineer. The build 'run_003' failed because of a test failure. Your task is to initiate a new bug report with the title 'Unit test failure in renderer on feature/new-renderer'. Assign this bug to the owner identified by the bisect operation. Then, prepare a fix proposal titled 'Fix texture format validation' with the description 'Update texture format validation to handle new character texture format' and type 'test_failure'. Finally, set the build run's triage status to 'resolved'.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_003"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_003"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_002"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Unit test failure in renderer on feature/new-renderer",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_003",
                    "bisect_result_id": "bisect_002",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "test_failure",
                    "title": "Fix texture format validation",
                    "description": "Update texture format validation to handle new character texture format"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_003",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "016",
        "instruction": "As a Dev Ops Engineer, a performance regression has been identified in build 'run_007'. Please initiate a new bug titled 'Performance regression in renderer' and assign it to the owner found via the bisect. Next, propose a fix with the title 'Optimize texture loading performance' and include a description saying 'Address frame rate drop caused by recent renderer changes', categorizing it as 'performance_regression'. At the end, mark the build run's triage status as 'resolved'.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_007"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_007"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_004"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Performance regression in renderer",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_007",
                    "bisect_result_id": "bisect_004",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "performance_regression",
                    "title": "Optimize texture loading performance",
                    "description": "Address frame rate drop caused by recent renderer changes"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_007",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "017",
        "instruction": "Being a Release Manager, deployment 'deploy_007' has shown instability in production. Execute a rollback process. Subsequently, an incident ticket must be created in the 'Mobile App Infrastructure' project with the title 'Critical Rollback: Deployment deploy_007 is not stable'. Ensure to allocate the ticket to the lead of the 'Game Server Operations Team'.",
        "actions": [
            {
                "name": "GetDeploymentById",
                "arguments": {
                    "id": "deploy_007"
                },
            },
            {
                "name": "GetRollbackByDeploymentId",
                "arguments": {
                    "deployment_id": "deploy_007"
                },
            },
            {
                "name": "CreateDeployment",
                "arguments": {
                    "pipeline_id": "pipe_009",
                    "environment_id": "env_019",
                    "deployed_by": "user_006",
                    "version": "v2.2.1",
                    "status": "in_progress"
                },
            },
            {
                "name": "GetTeamByName",
                "arguments": {
                    "name": "Game Server Operations Team"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_005"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Mobile App Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_017",
                    "type": "incident",
                    "title": "Critical Rollback: Deployment deploy_007 is not stable",
                    "assignee_id": "user_005",
                    "priority": "critical",
                    "state": "open"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "018",
        "instruction": "As a Release Manager, there is an issue with the production deployment 'deploy_009' being unstable in production. Initiate the rollback process. Subsequently, open an incident ticket with the title 'Production Rollback: Deployment deploy_009 is not stable' under the 'Infrastructure as Code Migration' project and assign it to the lead of the 'Infrastructure Automation' team.",
        "actions": [
            {
                "name": "GetDeploymentById",
                "arguments": {
                    "id": "deploy_009"
                },
            },
            {
                "name": "GetRollbackByDeploymentId",
                "arguments": {
                    "deployment_id": "deploy_009"
                },
            },
            {
                "name": "CreateDeployment",
                "arguments": {
                    "pipeline_id": "pipe_011",
                    "environment_id": "env_024",
                    "deployed_by": "user_008",
                    "version": "v1.4.2",
                    "status": "in_progress"
                },
            },
            {
                "name": "GetTeamByName",
                "arguments": {
                    "name": "Infrastructure Automation"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_010"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Infrastructure as Code Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_010",
                    "type": "incident",
                    "title": "Production Rollback: Deployment deploy_009 is not stable",
                    "assignee_id": "user_003",
                    "priority": "critical",
                    "state": "open"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "019",
        "instruction": "As a Release Manager, you must address the failure of deployment 'deploy_010' by performing a rollback. Retrieve the necessary rollback details and initiate the process. Afterward, create an incident titled 'Rollback Triggered: Deployment deploy_010 failed' in the 'API Gateway Implementation' project and ensure that this ticket is assigned to the lead of the 'Developer Experience' team.",
        "actions": [
            {
                "name": "GetDeploymentById",
                "arguments": {
                    "id": "deploy_010"
                },
            },
            {
                "name": "GetRollbackByDeploymentId",
                "arguments": {
                    "deployment_id": "deploy_010"
                },
            },
            {
                "name": "CreateDeployment",
                "arguments": {
                    "pipeline_id": "pipe_013",
                    "environment_id": "env_029",
                    "deployed_by": "user_009",
                    "version": "v2.0.2",
                    "status": "in_progress"
                },
            },
            {
                "name": "GetTeamByName",
                "arguments": {
                    "name": "Developer Experience"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_006"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "API Gateway Implementation"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_013",
                    "type": "incident",
                    "title": "Rollback Triggered: Deployment deploy_010 failed",
                    "assignee_id": "user_016",
                    "priority": "critical",
                    "state": "open"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "020",
        "instruction": "You are a Triage Engineer. A new crash, 'crash_001', has been reported. Locate the original bug relating to the crash's fingerprint. Subsequently, create a new bug titled '[Duplicate Crash] Character Load Access Violation on RTX 4080', and assign it to Anna Kowalski. Make sure to link this new bug as a duplicate of the original one. Also, close the newly created bug and update the crash event's status to 'duplicate'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_001"
                },
            },
            {
                "name": "FindBugByCrashFingerprint",
                "arguments": {
                    "crash_fingerprint": "renderer_character_load_access_violation_xyz"
                },
            },
            {
                "name": "GetUserByName",
                "arguments": {
                    "name": "Anna Kowalski"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "[Duplicate Crash] Character Load Access Violation on RTX 4080",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_026",
                    "child_id": "work_028",
                    "link_type": "duplicate"
                },
            },
            {
                "name": "UpdateWorkItemState",
                "arguments": {
                    "id": "work_028",
                    "new_state": "closed"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_001",
                    "status": "duplicate"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "021",
        "instruction": "You are a Triage Engineer. We have obtained crash report 'crash_003', which you need to manage. This appears to be a novel issue. Develop a bug report under the 'Game Security & Anti-Cheat Framework' project with the title 'Network Connection Timeout in Multiplayer'. Assign it to the owner of the 'src/game/network/multiplayer.cpp' file. Add a comment stating 'New crash report, needs investigation.' to the newly created bug and modify the crash event's status to 'analyzed'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_003"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Network Connection Timeout in Multiplayer",
                    "assignee_id": "user_008"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "New crash report, needs investigation."
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_003",
                    "status": "analyzed"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "022",
        "instruction": "As a Triage Engineer, note that the bug 'Texture compression artifact on character model' seems to be a duplicate of the 'Game crashes when loading character model' issue. Link them as duplicates, add a comment saying 'Closing as a duplicate.' to the duplicate bug, and proceed to close the bug.",
        "actions": [
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Texture compression artifact on character model"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Game crashes when loading character model"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_026",
                    "child_id": "work_027",
                    "link_type": "duplicate"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_027",
                    "comment": "Closing as a duplicate."
                },
            },
            {
                "name": "UpdateWorkItemState",
                "arguments": {
                    "id": "work_027",
                    "new_state": "closed"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "023",
        "instruction": "As a Dev Ops Engineer, address the test failure in build 'run_003' by creating a bug report titled 'Renderer test failure on feature/new-renderer' and assigning it to the owner found via the bisect operation. Next, draft a fix proposal titled 'Fix texture validation in renderer tests' with the description 'Update test case to handle new texture formats' and categorize it as 'test_failure'. Lastly, set the build's triage status to 'resolved'.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_003"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_003"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_002"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Renderer test failure on feature/new-renderer",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_003",
                    "bisect_result_id": "bisect_002",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "test_failure",
                    "title": "Fix texture validation in renderer tests",
                    "description": "Update test case to handle new texture formats"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_003",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "024",
        "instruction": "As a Dev Ops Engineer, an integration test did not succeed in build 'run_005'. Please log a bug with the title 'Multiplayer connection test failing' and assign it to the bisect owner. Formulate a fix proposal titled 'Resolve multiplayer connection timeout' and provide the description 'Increase timeout to prevent integration test failures', categorized as 'integration_failure'. Lastly, ensure the build 'run_005' is marked as triaged by updating its status to 'resolved'.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_005"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_005"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_003"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Multiplayer connection test failing",
                    "assignee_id": "user_008"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_005",
                    "bisect_result_id": "bisect_003",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "integration_failure",
                    "title": "Resolve multiplayer connection timeout",
                    "description": "Increase timeout to prevent integration test failures"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_005",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "025",
        "instruction": "Serving as a Dev Ops Engineer, the build 'run_006' encountered a failure due to an issue with asset validation. Kindly file a bug with the heading 'Asset validation failure for oversized texture' and allocate it to the owner indicated in the bisect report. Afterward, generate a fix proposal named 'Resize oversized hero texture' with the description 'Resize hero_character_diffuse.png to meet engine requirements', classified as 'asset_validation_issue'. Finally, amend the build's triage status to 'resolved'.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_006"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_006"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_006"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-assets"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Asset validation failure for oversized texture",
                    "assignee_id": "user_008"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_006",
                    "bisect_result_id": "bisect_006",
                    "repo": "game-assets",
                    "branch": "feature/new-assets",
                    "fix_type": "asset_validation_issue",
                    "title": "Resize oversized hero texture",
                    "description": "Resize hero_character_diffuse.png to meet engine requirements"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_006",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "026",
        "instruction": "As a Dev Ops Engineer, address the localization issue identified in build 'run_008'. Generate a bug with the title 'Localization text overflows UI' and assign it to the appropriate owner identified from the bisect. Next, draft a fix proposal titled 'Fix German UI text overflow', detailing 'Shorten German translation for ui.main_menu.start_game to fit constraints' and categorize it as 'localization_issue'. Ultimately, update build 'run_008' to resolved status.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_008"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_008"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_007"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-localization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "Localization text overflows UI",
                    "assignee_id": "user_008"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_008",
                    "bisect_result_id": "bisect_007",
                    "repo": "game-localization",
                    "branch": "feature/localization-update",
                    "fix_type": "localization_issue",
                    "title": "Fix German UI text overflow",
                    "description": "Shorten German translation for ui.main_menu.start_game to fit constraints"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_008",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "027",
        "instruction": "As a Dev Ops Engineer, manage the compilation failure for build 'run_001'. Create a bug entitled 'Compilation failed on feature/new-renderer' for the bisect owner. Subsequently, draft a fix proposal titled 'Fix compilation issue in TextureManager', including the description 'A declaration is missing for loadTexture in the header file', and classify it as 'compilation_issue'. Conclude by resolving the build run.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_001"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_001"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Compilation failed on feature/new-renderer",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_001",
                    "bisect_result_id": "bisect_001",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "compilation_issue",
                    "title": "Fix compilation issue in TextureManager",
                    "description": "A declaration is missing for loadTexture in the header file."
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_001",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "028",
        "instruction": "You are a Dev Ops Engineer. Handle the test failure from build 'run_003'. A bug should be created with the title 'Failing unit test in renderer module' for the person identified by the bisect. Additionally, create a fix proposal for a 'test_failure' with the title 'Correct texture validation logic' and description 'The unit test is failing due to incorrect texture format validation logic'. Lastly, ensure the build run is resolved.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_003"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_003"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_002"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Failing unit test in renderer module",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_003",
                    "bisect_result_id": "bisect_002",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "test_failure",
                    "title": "Correct texture validation logic",
                    "description": "The unit test is failing due to incorrect texture format validation logic"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_003",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "029",
        "instruction": "You are a Dev Ops Engineer. Resolve the integration failure in build 'run_005'. Create a bug with the title 'Multiplayer integration test failing' for the bisect owner. Construct a fix proposal for an 'integration_failure' with the title 'Fix connection timeout in multiplayer tests' and description 'The integration test is failing due to a connection timeout in the multiplayer module'. Finally, ensure the build run is resolved.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_005"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_005"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_003"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Multiplayer integration test failing",
                    "assignee_id": "user_008"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_005",
                    "bisect_result_id": "bisect_003",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "integration_failure",
                    "title": "Fix connection timeout in multiplayer tests",
                    "description": "The integration test is failing due to a connection timeout in the multiplayer module"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_005",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "030",
        "instruction": "You are a Dev Ops Engineer. Address the asset validation failure in build 'run_006'. Report a bug to the bisect owner with the title 'Invalid asset: oversized texture'. Next, propose a solution for an 'asset_validation_issue' titled 'Resize hero texture to pass validation' with the description 'The hero_character_diffuse.png texture is too large and needs to be resized'. Conclude by resolving the build.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_006"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_006"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_006"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-assets"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Invalid asset: oversized texture",
                    "assignee_id": "user_008"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_006",
                    "bisect_result_id": "bisect_006",
                    "repo": "game-assets",
                    "branch": "feature/new-assets",
                    "fix_type": "asset_validation_issue",
                    "title": "Resize hero texture to pass validation",
                    "description": "The hero_character_diffuse.png texture is too large and needs to be resized"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_006",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "031",
        "instruction": "You are a Dev Ops Engineer. Handle the localization issue in build 'run_008'. Report a bug for the bisect owner with the title 'UI text overflow in German localization'. Next, propose a fix for a 'localization_issue' titled 'Correct overflowing German UI text' with the description 'The German translation for ui.main_menu.start_game is too long and causes a UI overflow'. Finally, update the build run's triage status to 'resolved'.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_008"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_008"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_007"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-localization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "UI text overflow in German localization",
                    "assignee_id": "user_008"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_008",
                    "bisect_result_id": "bisect_007",
                    "repo": "game-localization",
                    "branch": "feature/localization-update",
                    "fix_type": "localization_issue",
                    "title": "Correct overflowing German UI text",
                    "description": "The German translation for ui.main_menu.start_game is too long and causes a UI overflow"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_008",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "032",
        "instruction": "You are a Dev Ops Engineer. Address the compilation failure in build 'run_001'. Open a bug with the title 'Build error in renderer module' for the bisect owner. Following that, draft a fix proposal for a 'compilation_issue' titled 'Fix undeclared function in renderer' with the description 'The function loadTexture is not declared in the TextureManager header, causing a compilation failure'. In conclusion, resolve the build.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_001"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_001"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Build error in renderer module",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_001",
                    "bisect_result_id": "bisect_001",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "compilation_issue",
                    "title": "Fix undeclared function in renderer",
                    "description": "The function loadTexture is not declared in the TextureManager header, causing a compilation failure"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_001",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "033",
        "instruction": "You are a Dev Ops Engineer. Assess the test failure in build 'run_003'. Report a bug titled 'Unit test for texture loading failing' for the bisect owner. Subsequently, create a fix proposal for a 'test_failure' with the title 'Update texture validation in unit tests' and a description of 'The texture format validation in the renderer unit test needs to be updated for new formats'. Finally, mark the build as resolved.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_003"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_003"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_002"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Unit test for texture loading failing",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_003",
                    "bisect_result_id": "bisect_002",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "test_failure",
                    "title": "Update texture validation in unit tests",
                    "description": "The texture format validation in the renderer unit test needs to be updated for new formats"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_003",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "034",
        "instruction": "You are a Dev Ops Engineer. Handle the integration failure from build 'run_005'. Create a bug for the person identified by the bisect with the title 'Multiplayer connection is timing out in integration tests'. Draft a fix proposal for an 'integration_failure' with the title 'Fix multiplayer test timeout' and a description of 'The multiplayer integration test is failing due to a timeout. The threshold should be increased'. Finally, resolve the build run.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_005"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_005"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_003"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Multiplayer connection is timing out in integration tests",
                    "assignee_id": "user_008"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_005",
                    "bisect_result_id": "bisect_003",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "integration_failure",
                    "title": "Fix multiplayer test timeout",
                    "description": "The multiplayer integration test is failing due to a timeout. The threshold should be increased"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_005",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "035",
        "instruction": "You are a Dev Ops Engineer. Manage the asset validation failure in build 'run_006'. Submit a bug with the title 'Asset validation error: texture size' for the bisect owner. Prepare a fix proposal for an 'asset_validation_issue' with the title 'Fix oversized texture in game assets' and description 'The hero_character_diffuse.png texture is larger than the maximum allowed size and needs to be resized'. Conclude by resolving the build.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_006"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_006"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_006"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-assets"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Asset validation error: texture size",
                    "assignee_id": "user_008"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_006",
                    "bisect_result_id": "bisect_006",
                    "repo": "game-assets",
                    "branch": "feature/new-assets",
                    "fix_type": "asset_validation_issue",
                    "title": "Fix oversized texture in game assets",
                    "description": "The hero_character_diffuse.png texture is larger than the maximum allowed size and needs to be resized"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_006",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "036",
        "instruction": "As a Dev Ops Engineer, handle the issue of a localization failure in build 'run_008'. Generate a bug report titled 'German translation causing UI overflow' for the individual identified by the bisect. Next, prepare a fix proposal under 'localization_issue' with the title 'Shorten German UI string to fix overflow' and provide the description 'The German translation for 'ui.main_menu.start_game' is too long and needs to be shortened to prevent UI overflow'. Finally, update the build status to resolved.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_008"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_008"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_007"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-localization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "German translation causing UI overflow",
                    "assignee_id": "user_008"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_008",
                    "bisect_result_id": "bisect_007",
                    "repo": "game-localization",
                    "branch": "feature/localization-update",
                    "fix_type": "localization_issue",
                    "title": "Shorten German UI string to fix overflow",
                    "description": "The German translation for 'ui.main_menu.start_game' is too long and needs to be shortened to prevent UI overflow"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_008",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "037",
        "instruction": "As a Dev Ops Engineer, take care of the performance regression detected in build 'run_007'. Draft a bug for the individual identified by the bisect, titled 'Renderer performance has degraded'. Next, create a fix proposal for a 'performance_regression' with the title 'Fix performance drop in texture loading' and explain with the description 'Recent changes to the renderer have caused a significant drop in frame rate. This needs to be optimized'. Conclude by resolving the build run.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_007"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_007"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_004"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Renderer performance has degraded",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_007",
                    "bisect_result_id": "bisect_004",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "performance_regression",
                    "title": "Fix performance drop in texture loading",
                    "description": "Recent changes to the renderer have caused a significant drop in frame rate. This needs to be optimized"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_007",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "038",
        "instruction": "As a Dev Ops Engineer, you need to handle an integration failure that occurred in build 'run_005'. Initiate the creation of a bug report titled 'Integration test failure in multiplayer connection' and assign it to the owner identified in the bisect report. Following that, coordinate a fix proposal with the title 'Fix multiplayer connection timeout' and provide the description 'Increase connection timeout threshold to fix integration test failure', with the type set as 'integration_failure'. Finally, update the triage status of the build run to 'resolved'.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_005"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_005"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_003"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Integration test failure in multiplayer connection",
                    "assignee_id": "user_008"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_005",
                    "bisect_result_id": "bisect_003",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "integration_failure",
                    "title": "Fix multiplayer connection timeout",
                    "description": "Increase connection timeout threshold to fix integration test failure"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_005",
                    "triage_status": "resolved"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "046",
        "instruction": "Being a Dev Ops Engineer, manage the situation where deployment 'deploy_004' failed. Locate the last successful deployment on the same pipeline to identify the rollback version. Then, search for the work item related to the 'Implement multi-cloud application architecture' feature, included in the failed deployment. Comment on this work item to note that the deployment failed and a rollback is in progress, specifying the version to which you are reverting. Subsequently, proceed to initiate the rollback. Ultimately, report a critical incident in the 'Multi-Platform Game Infrastructure' project with the title 'Deployment Failure and Rollback of Multi-Cloud App' and delegate it to the 'Game Server Operations Team' lead.",
        "actions": [
            {
                "name": "GetDeploymentById",
                "arguments": {
                    "id": "deploy_004"
                },
            },
            {
                "name": "FindPreviousSuccessfulDeployment",
                "arguments": {
                    "pipeline_id": "pipe_005",
                    "before_timestamp": "2025-01-26T08:20:00Z"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement multi-cloud application architecture"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_006",
                    "comment": "Deployment failed. Rolling back to version v1.0.4 from deployment deploy_005."
                },
            },
            {
                "name": "CreateDeployment",
                "arguments": {
                    "pipeline_id": "pipe_005",
                    "environment_id": "env_011",
                    "deployed_by": "user_004",
                    "version": "v1.0.4",
                    "status": "in_progress"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "GetTeamByName",
                "arguments": {
                    "name": "Game Server Operations Team"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_005"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "incident",
                    "title": "Deployment Failure and Rollback of Multi-Cloud App",
                    "assignee_id": "user_005",
                    "priority": "critical"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "050",
        "instruction": "As a Dev Ops Engineer, a build failure in 'run_001' is obstructing deployments and requires a hotfix. Locate the bisect result to pinpoint the suspect files and determine the responsible owner. Retrieve the repository and project specifics for 'game-engine'. Initiate a new branch from 'main' called 'hotfix/build-run-001'. Create a new urgent bug titled 'Hotfix for Build run_001 Failure' and allocate it to the owner. Include a comment saying 'Please commit the fix for this build failure' on the bug. Moreover, ensure the build triage run's status is changed to 'in_progress'.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_001"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_001"
                },
            },
            {
                "name": "GetRepositoryByName",
                "arguments": {
                    "name": "game-engine"
                },
            },
            {
                "name": "GetProjectIdForRepositoryName",
                "arguments": {
                    "repository_name": "game-engine"
                },
            },
            {
                "name": "GetBranchByName",
                "arguments": {
                    "repository_id": "repo_031",
                    "branch_name": "main"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repository_id": "repo_031",
                    "branch_name": "hotfix/build-run-001",
                    "source_branch_id": "branch_051"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Hotfix for Build run_001 Failure",
                    "assignee_id": "user_001",
                    "priority": "high"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Please commit the fix for this build failure"
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_001",
                    "triage_status": "in_progress"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "067",
        "instruction": "As a Triage Engineer, a network crash, 'crash_003', has been detected. Identify the owner of the 'multiplayer.cpp' file and their team lead. Generate a bug in the 'Game Security & Anti-Cheat Framework' project titled 'Crash on Network Timeout' for the team lead. Associate this new bug with the 'Implement anti-cheat system integration' story as related. Add 'Stack Trace: NetworkManager.dll' as a comment to the bug. Lastly, modify the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_003"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Crash on Network Timeout",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: NetworkManager.dll"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_003",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "068",
        "instruction": "As a Triage Engineer, handle the crash report 'crash_006' concerning a Kubernetes problem for triage. Locate the owner of 'multiplayer.cpp' and identify their team lead for responsibility. Set up a new bug within the 'Game Engine Core Migration' project under the title 'K8s Memory Allocation Crash'. Designate the bug to the team lead. Connect it to the 'Implement game engine rendering pipeline' story as a dependency. Append 'Issue Signature: Kubernetes resource allocation failed' as a comment to the bug. Lastly, change the crash's status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_006"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "K8s Memory Allocation Crash",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement game engine rendering pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_001",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Issue Signature: Kubernetes resource allocation failed"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_006",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "070",
        "instruction": "As a Triage Engineer, address the compilation crash 'crash_005' that has been recorded. Determine the owner of 'renderer.cpp' and their team lead. Coordinate the creation of a bug within the 'Multi-Platform Game Infrastructure' project titled 'Renderer Compilation Failure' and allocate it to the lead. Ensure the newly created bug is linked to the 'Implement cross-platform game infrastructure' epic as a related issue. Insert 'Stack Trace: renderer.cpp' as a comment to the bug. Additionally, adjust the crash's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_005"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "Renderer Compilation Failure",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: renderer.cpp"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_005",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "071",
        "instruction": "As a Triage Engineer, handle crash 'crash_001' for triage. Identify the owner of 'renderer.cpp' and their team lead. In the 'Game Security & Anti-Cheat Framework' project, generate a new bug titled 'Access Violation Crash in Rendering' for the team lead. Ensure this bug is connected to the 'Implement anti-cheat system integration' story as a dependency. Include 'Access violation in GameEngine.dll' as a comment in the newly created bug. Ultimately, modify the crash event's status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_001"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Access Violation Crash in Rendering",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Access violation in GameEngine.dll"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_001",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "072",
        "instruction": "As a Triage Engineer, handle the reported network timeout crash, 'crash_003'. Determine the owner of 'multiplayer.cpp' and their team lead. In the 'Game Engine Core Migration' project, generate a bug titled 'Network Instability Crash', assigning it to the team lead. Connect this bug to the 'Implement game engine rendering pipeline' story as a blocker. Insert 'Stack Trace: NetworkManager.dll' as a comment on the new bug. To conclude, update the crash event's status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_003"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Network Instability Crash",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement game engine rendering pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_001",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: NetworkManager.dll"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_003",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "073",
        "instruction": "Handle your role as a Triage Engineer. Attention is required for crash report 'crash_006' related to a Kubernetes issue. Locate the owner of 'multiplayer.cpp' and their team leader. It is necessary to create a bug within the 'Game Build Pipeline Modernization' project titled 'K8s Crash During Deployment' and assign it to the team lead. Ensure this bug is related to the 'Create automated game build pipeline' epic. Add the comment 'Kubernetes resource allocation failed: insufficient memory' to the bug report. Conclude by updating the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_006"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "K8s Crash During Deployment",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Kubernetes resource allocation failed: insufficient memory"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_006",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "076",
        "instruction": "Coordinate your duties as a Triage Engineer regarding a network timeout issue noted in crash report 'crash_003'. Identify who is responsible for the 'multiplayer.cpp' file and their team head. Create a bug in the 'Game Security & Anti-Cheat Framework' project with the title 'Network Timeout During Gameplay', and allocate it to the team lead. Since this is likely a prerequisite for our anti-cheat integration, associate it with the story titled 'Implement anti-cheat system integration'. Include the comment 'Stack Trace: NetworkManager.dll' in the bug details and adjust the crash status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_003"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Network Timeout During Gameplay",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: NetworkManager.dll"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_003",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "077",
        "instruction": "As a Triage Engineer, the compilation crash 'crash_005' requires your focus. Determine the owner of 'renderer.cpp' and identify their team leader. Initiate a bug entry in the 'Multi-Platform Game Infrastructure' project titled 'Critical Renderer Compilation Failure', assigning it to the team lead. Given that this is a significant obstacle for our cross-platform epic titled 'Implement cross-platform game infrastructure', ensure you link it appropriately. Include 'Stack Trace: renderer.cpp' in a bug comment, and subsequently mark the crash status as 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_005"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "Critical Renderer Compilation Failure",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: renderer.cpp"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_005",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "078",
        "instruction": "Acting as a Triage Engineer, address the Kubernetes-related crash identified as 'crash_006'. This appears to be an infrastructure problem, so ascertain who is responsible for 'multiplayer.cpp' to uncover the accountable team and its leader. Create a bug in the 'Game Engine Core Migration' project named 'K8s Infrastructure Crash' and delegate it to the lead. Since this issue seems to connect to the primary rendering pipeline called 'Implement game engine rendering pipeline', ensure you link the corresponding work items. Insert a comment in the bug stating 'Kubernetes resource allocation failed: insufficient memory' for context, and lastly, change the crash status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_006"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "K8s Infrastructure Crash",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement game engine rendering pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_001",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Kubernetes resource allocation failed: insufficient memory"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_006",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "079",
        "instruction": "As a Triage Engineer, you need to address an asset validation crash 'crash_007' that has occurred. Identify the owner of the 'assets/models/environment/' directory and ascertain their team lead. Ensure a bug is filed in the 'Game Build Pipeline Modernization' project with the heading 'Asset Validation Crash: Environment Model' directed to the team lead. This issue must be linked as a prerequisite for the main build pipeline epic titled 'Create automated game build pipeline'. Add 'Asset validation failed' as a comment on the bug report, and then proceed to update the crash event status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_007"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "assets/models/environment/"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_007"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_002"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_002"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Asset Validation Crash: Environment Model",
                    "assignee_id": "user_002"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Asset validation failed"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_007",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "080",
        "instruction": "As a Triage Engineer, you must handle another access violation, 'crash_001', that has been reported. Create a bug for the leader of the 'renderer.cpp' file. The bug should be associated with the 'Game Security & Anti-Cheat Framework' project and titled 'Security Concern: Access Violation in Renderer'. This may impede our anti-cheat efforts, so connect it to the story titled 'Implement anti-cheat system integration'. Add 'Access violation in GameEngine.dll' in a comment on the bug, and mark the crash under the status 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_001"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Security Concern: Access Violation in Renderer",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Access violation in GameEngine.dll"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_001",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "081",
        "instruction": "Handle the responsibilities of a Triage Engineer. We have encountered a network timeout crash ('crash_003'). Determine the owner of 'multiplayer.cpp' and identify their manager. Register a bug for the manager within the 'Game Build Pipeline Modernization' project with the designation 'Network Instability in Builds'. Connect this as a related issue to the primary build pipeline epic titled 'Create automated game build pipeline'. For additional context, incorporate 'Stack Trace: NetworkManager.dll' as a comment on the bug. Lastly, revise the crash status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_003"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Network Instability in Builds",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: NetworkManager.dll"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_003",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "082",
        "instruction": "Coordinate under the capacity of a Triage Engineer. A compilation crash, known as 'crash_005', has occurred. Locate the owner of 'renderer.cpp' and their team leader. Initiate a new bug in the 'Game Security & Anti-Cheat Framework' project for the team leader, with the title 'Build Failure: Renderer Compilation'. This bug must be linked as a dependency for the anti-cheat story titled 'Implement anti-cheat system integration'. Add 'Stack Trace: renderer.cpp' as a comment to the bug. Finally, adjust the crash's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_005"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Build Failure: Renderer Compilation",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: renderer.cpp"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_005",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "083",
        "instruction": "You are a Triage Engineer. Address the Kubernetes crash 'crash_006'. Determine the owner of 'multiplayer.cpp' and their team lead. File a bug in the 'Game Build Pipeline Modernization' project for the team lead with the title 'Deployment Failure: K8s Memory'. Connect this bug as a blocker to the 'Create automated game build pipeline' epic. Insert 'Kubernetes resource allocation failed: insufficient memory' as a comment for the bug, and subsequently change the crash status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_006"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "Deployment Failure: K8s Memory",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Kubernetes resource allocation failed: insufficient memory"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_006",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "084",
        "instruction": "You are a Triage Engineer. An asset validation crash, 'crash_007', has occurred. Locate the owner of the 'assets/textures/character_models/' directory and their team lead. Initiate a bug in the 'Multi-Platform Game Infrastructure' project titled 'Asset Crash: Invalid Texture' for the team lead. This bug pertains to the cross-platform epic with the title 'Implement cross-platform game infrastructure', so ensure they are linked with type 'related'. Append a comment to the new bug with 'Asset validation failed: Texture size'. Finally, set the crash event's status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_007"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "assets/textures/character_models/"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_002"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_002"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_002"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "Asset Crash: Invalid Texture",
                    "assignee_id": "user_002"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Asset validation failed: Texture size"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_007",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "086",
        "instruction": "As a Triage Engineer, a network timeout crash, 'crash_003', has been encountered. Determine the full path for 'multiplayer.cpp' to pinpoint the owner and their team lead. Create a new bug in the 'Multi-Platform Game Infrastructure' project with the title 'Network Timeout During Gameplay' and delegate it to the team lead. Connect this bug as a dependency to the 'Implement cross-platform game infrastructure' epic. Include 'Stack Trace: NetworkManager.dll' as a comment within the new bug. In closing, change the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_003"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "Network Timeout During Gameplay",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: NetworkManager.dll"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_003",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "087",
        "instruction": "As a Triage Engineer, crash 'crash_006' suggests a Kubernetes problem. Determine who owns 'multiplayer.cpp' to locate the responsible team and their lead. Register a new bug in the 'Game Security & Anti-Cheat Framework' project titled 'Kubernetes Deployment Crash' and assign it to the team lead. Since this bug is hindering the 'Implement anti-cheat system integration' story, link the two. Add 'Kubernetes resource allocation failed: insufficient memory' as a comment to the newly created bug. To finish, adjust the crash event's status to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_006"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Kubernetes Deployment Crash",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Kubernetes resource allocation failed: insufficient memory"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_006",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "088",
        "instruction": "As a Triage Engineer, promptly address the asset validation crash identified as 'crash_007'. Locate the owner of the asset folder 'assets/textures/character_models/' and their respective team lead. Coordinate the creation of a new bug in the 'Game Engine Core Migration' project with the title 'Asset Validation Failure: Texture Size', assigning it to the team lead. Since this issue pertains to the main rendering pipeline, ensure it is linked to the story with the title 'Implement game engine rendering pipeline'. Include a comment on the bug stating 'Texture size 4096x4096 exceeds maximum 2048x2048'. Finally, update the crash event status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_007"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "assets/textures/character_models/"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_002"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_002"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_002"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Asset Validation Failure: Texture Size",
                    "assignee_id": "user_002"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement game engine rendering pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_001",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Texture size 4096x4096 exceeds maximum 2048x2048"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_007",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "090",
        "instruction": "As a Triage Engineer, handle the new access violation crash labeled 'crash_001'. Identify the owner of the 'renderer.cpp' file and find out who their team lead is. Coordinate the creation of a bug in the 'Multi-Platform Game Infrastructure' project with the title 'Access Violation on Character Load', assigning it to the team lead for resolution. Link this as it is a blocker to our cross-platform epic named 'Implement cross-platform game infrastructure'. Add a comment to the bug stating 'Access violation in GameEngine.dll'. Conclude by updating the status of the crash event to 'investigating'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_001"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "Access Violation on Character Load",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "blocks"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Access violation in GameEngine.dll"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_001",
                    "status": "investigating"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "092",
        "instruction": "As a Triage Engineer, the crash report 'crash_006' related to a Kubernetes problem requires your attention. Identify both the owner of 'multiplayer.cpp' and their team leader. Generate a bug in the 'Game Build Pipeline Modernization' project with the title 'K8s Crash During Deployment' and delegate it to the team leader. Ensure this bug is linked as related to the 'Create automated game build pipeline' epic. It is essential to add a comment stating 'Kubernetes resource allocation failed' to the bug. To complete the task, modify the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_006"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Build Pipeline Modernization"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_002",
                    "type": "bug",
                    "title": "K8s Crash During Deployment",
                    "assignee_id": "user_003"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Create automated game build pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_003",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Kubernetes resource allocation failed"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_006",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "093",
        "instruction": "As part of your responsibilities as a Triage Engineer, you need to address the asset validation crash, 'crash_007'. Locate both the owner of the 'assets/textures/character_models/' directory and their team leader. Initiate a bug in the 'Multi-Platform Game Infrastructure' project with the title 'Asset Crash: Invalid Texture' directed towards the team leader. Because this bug relates to the cross-platform epic 'Implement cross-platform game infrastructure', please ensure they are linked. Include a comment in the new bug that says 'Texture size 4096x4096 exceeds maximum 2048x2048'. In conclusion, change the crash event's status to 'triaged'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_007"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "assets/textures/character_models/"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_002"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_002"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_002"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Multi-Platform Game Infrastructure"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_003",
                    "type": "bug",
                    "title": "Asset Crash: Invalid Texture",
                    "assignee_id": "user_002"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement cross-platform game infrastructure"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_004",
                    "child_id": "work_028",
                    "link_type": "related"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Texture size 4096x4096 exceeds maximum 2048x2048"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_007",
                    "status": "triaged"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "094",
        "instruction": "As a Triage Engineer, a compilation crash, 'crash_005', has been logged that needs your attention. Identify the owner of 'renderer.cpp' and their team lead. Establish a bug in the 'Game Security & Anti-Cheat Framework' project titled 'Renderer Compilation Failure' and delegate it to the lead. This is crucial for the anti-cheat story titled 'Implement anti-cheat system integration', so ensure they are linked. Append 'Stack Trace: renderer.cpp' as a comment to the newly generated bug. Finally, change the crash's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_005"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Renderer Compilation Failure",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: renderer.cpp"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_005",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "096",
        "instruction": "As a Triage Engineer, a network timeout crash, 'crash_003', requires your expertise. Locate the owner of 'multiplayer.cpp' and their team lead. Formulate a new high-priority bug in the 'Game Engine Core Migration' project titled 'Network Timeout Crash'. Assign this bug to the team lead. This problem is integral to the main rendering pipeline titled 'Implement game engine rendering pipeline', so be sure to link them. Add 'Stack Trace: NetworkManager.dll' as a comment on the newly created bug. Thereafter, modify the crash event's status to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_003"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "multiplayer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/network/multiplayer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_008"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_003"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_003"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Network Timeout Crash",
                    "assignee_id": "user_003",
                    "priority": "high"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement game engine rendering pipeline"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_001",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "Stack Trace: NetworkManager.dll"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_003",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "099",
        "instruction": "As a Triage Engineer, you are handling the compilation crash 'crash_005' that has occurred. A bug needs to be created in the 'Game Security & Anti-Cheat Framework' project with the title 'Compilation Failure Blocking Security Scans' directed to the team lead handling the 'renderer.cpp' file. This bug is a prerequisite for the main anti-cheat story titled 'Implement anti-cheat system integration'; ensure they are linked. Incorporate the crash fingerprint as a comment for reference. Additionally, the crash event's status must be set to 'assigned'.",
        "actions": [
            {
                "name": "GetCrashEventById",
                "arguments": {
                    "id": "crash_005"
                },
            },
            {
                "name": "FindFullPathForFileName",
                "arguments": {
                    "file_name": "renderer.cpp"
                },
            },
            {
                "name": "FindFileOwner",
                "arguments": {
                    "file_path": "src/game/engine/renderer.cpp"
                },
            },
            {
                "name": "GetUserById",
                "arguments": {
                    "id": "user_001"
                },
            },
            {
                "name": "GetTeamById",
                "arguments": {
                    "id": "team_001"
                },
            },
            {
                "name": "GetTeamLead",
                "arguments": {
                    "team_id": "team_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Security & Anti-Cheat Framework"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_004",
                    "type": "bug",
                    "title": "Compilation Failure Blocking Security Scans",
                    "assignee_id": "user_001"
                },
            },
            {
                "name": "FindWorkItemByTitle",
                "arguments": {
                    "title": "Implement anti-cheat system integration"
                },
            },
            {
                "name": "LinkWorkItems",
                "arguments": {
                    "parent_id": "work_005",
                    "child_id": "work_028",
                    "link_type": "dependency"
                },
            },
            {
                "name": "AddCommentToWorkItem",
                "arguments": {
                    "id": "work_028",
                    "comment": "build_compilation_missing_declaration_xyz"
                },
            },
            {
                "name": "UpdateCrashEventStatus",
                "arguments": {
                    "id": "crash_005",
                    "status": "assigned"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "100",
        "instruction": "As a Dev Ops Engineer, you need to address the critical build 'run_001' that has failed, obstructing development. Identify the cause through the bisect result and find the responsible owner. In the 'Game Engine Core Migration' project, initiate a new high priority bug titled 'Critical Build Failure: Renderer Compilation' and allocate it to the owner. Ensure that a bug_assignment Slack notification is sent with the title 'New Critical Bug Assigned' and the message 'You have been assigned a critical build failure' to make the owner aware of the situation. Moreover, generate a fix proposal for the 'compilation_issue' with the title 'Fix Missing TextureManager Declaration' and a description stating 'A function declaration is missing.', marking the build as 'in_progress'.",
        "actions": [
            {
                "name": "GetBuildRunById",
                "arguments": {
                    "id": "run_001"
                },
            },
            {
                "name": "GetBisectResultForBuildRun",
                "arguments": {
                    "build_run_id": "run_001"
                },
            },
            {
                "name": "GetOwnerForBisect",
                "arguments": {
                    "bisect_id": "bisect_001"
                },
            },
            {
                "name": "GetProjectByName",
                "arguments": {
                    "name": "Game Engine Core Migration"
                },
            },
            {
                "name": "CreateWorkItem",
                "arguments": {
                    "project_id": "proj_001",
                    "type": "bug",
                    "title": "Critical Build Failure: Renderer Compilation",
                    "assignee_id": "user_001",
                    "priority": "high"
                },
            },
            {
                "name": "SendNotification",
                "arguments": {
                    "project_id": "proj_001",
                    "recipient_id": "user_001",
                    "title": "New Critical Bug Assigned",
                    "message": "You have been assigned a critical build failure",
                    "channel": "slack",
                    "notification_type": "bug_assignment"
                },
            },
            {
                "name": "CreateFixProposal",
                "arguments": {
                    "build_run_id": "run_001",
                    "bisect_result_id": "bisect_001",
                    "repo": "game-engine",
                    "branch": "feature/new-renderer",
                    "fix_type": "compilation_issue",
                    "title": "Fix Missing TextureManager Declaration",
                    "description": "A function declaration is missing."
                },
            },
            {
                "name": "UpdateBuildRunTriageStatus",
                "arguments": {
                    "id": "run_001",
                    "triage_status": "in_progress"
                }
            }
        ],
        "outputs": []
    }
]
