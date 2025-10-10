from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="069",
        instruction=(
            "You are a Triage Engineer. Handle the asset validation crash 'crash_007'. "
            "You should find the owner of the 'assets/textures/character_models/' directory and their team lead. "
            "Create a bug in the 'Game Build Pipeline Modernization' project titled 'Crash on Asset Validation: Oversized Texture', assigned to the team lead. "
            "Link this bug to the 'Create automated game build pipeline' epic as a blocker. "
            "Add 'Issue Signature: Asset validation failed' as a comment to the new bug. "
            "Also, set the crash event's status to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_007"}),
            Action(name="find_file_owner", kwargs={"file_path": "assets/textures/character_models/"}),
            Action(name="get_user_by_id", kwargs={"id": "user_002"}),
            Action(name="get_team_by_id", kwargs={"id": "team_002"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_002"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Crash on Asset Validation: Oversized Texture", "assignee_id": "user_002"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Issue Signature: Asset validation failed"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_007", "status": "investigating"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="085",
        instruction=(
            "You are a Triage Engineer. An access violation crash, 'crash_001', has been reported. "
            "You should find the full path for 'renderer.cpp' to determine the owner and their team lead. "
            "A new bug should be created in the 'Game Build Pipeline Modernization' project with the title 'Access Violation in Renderer' and assigned to the lead. "
            "Link this bug to the 'Create automated game build pipeline' epic as a related issue. "
            "Add 'Access violation in GameEngine.dll' as a comment for the new bug. "
            "Also, update the crash event's status to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_001"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Access Violation in Renderer", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Access violation in GameEngine.dll"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_001", "status": "triaged"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="098",
        instruction=(
            "You are a Triage Engineer. A Kubernetes memory crash, 'crash_006', has been reported. "
            "Since this is an infrastructure problem, find the owner of 'multiplayer.cpp' to identify the responsible team and their lead. "
            "Create a new incident in the 'Multi-Platform Game Infrastructure' project titled 'K8s Memory Allocation Failure' and assign it to the team lead. "
            "This incident is a blocker for the main cross-platform epic with title 'Implement cross-platform game infrastructure', so link them. "
            "Add 'Kubernetes resource allocation failed: insufficient memory' as a comment to the new created incident. "
            "To conclude, update the crash event's status to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_006"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "incident", "title": "K8s Memory Allocation Failure", "assignee_id": "user_003", 'priority': 'critical', 'state': 'open'}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Kubernetes resource allocation failed: insufficient memory"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_006", "status": "investigating"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="048",
        instruction=(
            "You are a Dev Ops Engineer. The build run 'run_001' failed. "
            "Find the bisect result to identify the cause. "
            "Based on the bisect, create a new bug in the 'Game Engine Core Migration' "
            "project titled 'Build Failure due to Missing Declaration in Renderer'. "
            "Assign this bug to the owner of the suspect file 'src/game/engine/renderer.cpp'. "
            "Then, create a fix proposal of type 'compilation_issue' "
            "titled 'Add Missing TextureManager Declaration' with "
            "description 'A function declaration is missing'. "
            "Finally, update the build run's triage status to 'fix_proposed'."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_001"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_001"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Build Failure due to Missing Declaration in Renderer", "assignee_id": "user_001"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_001", "bisect_result_id": "bisect_001", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "compilation_issue", "title": "Add Missing TextureManager Declaration", "description": "A function declaration is missing"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_001", "triage_status": "fix_proposed"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="117",
        instruction=(
            "You are a Triage Engineer. A Kubernetes crash, 'crash_006', has been reported. "
            "Find the owner of 'multiplayer.cpp' and their team lead. "
            "Create a new bug in the 'Multi-Platform Game Infrastructure' project titled 'K8s Crash' for the team lead. "
            "Send an email to the team lead with the message 'New Kubernetes Crash' and title 'New Bug Notification'. "
            "Link this as a dependency to the 'Implement cross-platform game infrastructure' epic. "
            "Add the issue signature from the crash as a comment, and then update the crash event's status to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_006"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "K8s Crash", "assignee_id": "user_003"}),
            Action(name="send_notification", kwargs={"project_id": "proj_003", "recipient_id": "user_003", "title": "New Bug Notification", "message": "New Kubernetes Crash", "channel": "email", "notification_type": "bug_assignment"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Kubernetes resource allocation failed: insufficient memory"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_006", "status": "triaged"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="120",
        instruction=(
            "You are a Triage Engineer. An access violation crash, 'crash_001', has occurred. "
            "A new bug should be created in the 'Multi-Platform Game Infrastructure' project titled 'Access Violation on Renderer' for the owner of 'renderer.cpp'. "
            "An email should be sent to the team lead with message 'New Access Violation Bug Assigned to your team' and title 'Bug Assignment Notification'. "
            "This should be linked as a dependency to the 'Implement cross-platform game infrastructure' epic, "
            "the crash's issue signature should be added as a comment, and the crash event's status should be updated to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_001"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "Access Violation on Renderer", "assignee_id": "user_001"}),
            Action(name="send_notification", kwargs={"project_id": "proj_003", "recipient_id": "user_001", "title": "Bug Assignment Notification", "message": "New Access Violation Bug Assigned to your team", "channel": "email"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Access violation in GameEngine.dll at 0x00007FF6A1B2C456"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_001", "status": "assigned"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="124",
        instruction=(
            "You are a Triage Engineer. There is a new compilation crash, 'crash_005', that you should handle. "
            "A new bug should be created in the 'Game Build Pipeline Modernization' project titled 'Renderer Compilation Issue in Build Pipeline' for the owner of 'renderer.cpp'. "
            "An email should be sent to the team lead with message 'New Compilation Bug in Build Pipeline' and title 'Bug Assignment'. "
            "This bug should be linked as a blocker to the 'Create automated game build pipeline' epic, "
            "the stack trace from the crash should be added as a comment, and the crash status should be updated to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_005"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Renderer Compilation Issue in Build Pipeline", "assignee_id": "user_001"}),
            Action(name="send_notification", kwargs={"project_id": "proj_002", "recipient_id": "user_001", "title": "Bug Assignment", "message": "New Compilation Bug in Build Pipeline", "channel": "email"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "renderer.cpp:245: issue: 'TextureManager::loadTexture' was not declared in this scope"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_005", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="125",
        instruction=(
            "You are a Triage Engineer. An access violation crash, 'crash_001', has occurred. "
            "You should create a new in the 'Multi-Platform Game Infrastructure' project titled 'Access Violation on Multiple Platforms' for the team lead of 'renderer.cpp'. "
            "A Slack notification should be sent to the lead with message 'New Cross-Platform Bug' and title 'Bug Assignment'. "
            "This should be linked as a related issue to the 'Implement cross-platform game infrastructure' epic, "
            "the issue signature from the crash should be added as a comment, and the crash event's status should be updated to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_001"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "Access Violation on Multiple Platforms", "assignee_id": "user_001"}),
            Action(name="send_notification", kwargs={"project_id": "proj_003", "recipient_id": "user_001", "title": "Bug Assignment", "message": "New Cross-Platform Bug", "channel": "slack"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Access violation in GameEngine.dll at 0x00007FF6A1B2C456"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_001", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="126",
        instruction=(
            "You are a Triage Engineer. A network timeout crash, 'crash_003', needs to be addressed. "
            "You should create a new bug in the 'Game Security & Anti-Cheat Framework' project titled 'Network Timeout Vulnerability' for the team lead of 'multiplayer.cpp'. "
            "An email should be sent to the lead with message 'New Network Vulnerability' and title 'Bug Assignment'. "
            "This should be linked as a blocker for the 'Implement anti-cheat system integration' story, "
            "the stack trace from the crash should be added as a comment, and the crash status should be updated to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_003"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Network Timeout Vulnerability", "assignee_id": "user_003"}),
            Action(name="send_notification", kwargs={"project_id": "proj_004", "recipient_id": "user_003", "title": "Bug Assignment", "message": "New Network Vulnerability", "channel": "email"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "NetworkManager.dll!NetworkManager::checkConnection() + 0x123\nNetworkManager.dll!NetworkManager::update() + 0x456\nGameEngine.dll!GameLoop::update() + 0x789"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_003", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="128",
        instruction=(
            "You are a Triage Engineer. An asset validation crash, 'crash_007', has occurred. "
            "You should create a new bug in the 'Game Engine Core Migration' project titled 'Asset Crash: Environment Model' for the owner of 'assets/models/environment/'. "
            "An email should be sent to the team lead with message 'New Asset Bug Assigned to Your Team' and title 'Bug Assignment'. "
            "This should be linked as a related issue to the 'Implement game engine rendering pipeline' story, "
            "the issue signature from the crash should be added as a comment, and the crash event's status should be updated to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_007"}),
            Action(name="find_file_owner", kwargs={"file_path": "assets/models/environment/"}),
            Action(name="get_user_by_id", kwargs={"id": "user_007"}),
            Action(name="get_team_by_id", kwargs={"id": "team_002"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_002"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Asset Crash: Environment Model", "assignee_id": "user_007"}),
            Action(name="send_notification", kwargs={"project_id": "proj_001", "recipient_id": "user_002", "title": "Bug Assignment", "message": "New Asset Bug Assigned to Your Team", "channel": "email"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement game engine rendering pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_001", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Asset validation failed: Texture size 4096x4096 exceeds maximum 2048x2048"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_007", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="130",
        instruction=(
            "You are a Triage Engineer. An access violation crash, 'crash_001', has been logged and you should handle it. "
            "A bug should be created in the 'Multi-Platform Game Infrastructure' project titled 'Renderer Access Violation on Multiple Platforms' for the team lead of 'renderer.cpp' file. "
            "You should send an email to the lead with message 'New Cross-Platform Bug' and title 'Bug Assignment'. "
            "This should be linked as a dependency to the 'Implement cross-platform game infrastructure' epic, "
            "the issue signature from the crash should be added as a comment, and the crash event's status should be updated to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_001"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "Renderer Access Violation on Multiple Platforms", "assignee_id": "user_001"}),
            Action(name="send_notification", kwargs={"project_id": "proj_003", "recipient_id": "user_001", "title": "Bug Assignment", "message": "New Cross-Platform Bug", "channel": "email"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Access violation in GameEngine.dll at 0x00007FF6A1B2C456"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_001", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="131",
        instruction=(
            "You are a Triage Engineer. A network timeout crash, 'crash_003', has been reported. "
            "A new bug should be created in the 'Game Security & Anti-Cheat Framework' project titled 'Network Vulnerability' for the team lead of 'multiplayer.cpp'. "
            "A Slack notification should be sent to the lead with message 'New Network Security Issue' and title 'Bug Assignment'. "
            "This should be linked as a blocker for the 'Implement anti-cheat system integration' story, "
            "the stack trace from the crash should be added as a comment, and the crash status should be updated to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_003"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Network Vulnerability", "assignee_id": "user_003"}),
            Action(name="send_notification", kwargs={"project_id": "proj_004", "recipient_id": "user_003", "title": "Bug Assignment", "message": "New Network Security Issue", "channel": "slack"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "NetworkManager.dll!NetworkManager::checkConnection() + 0x123\nNetworkManager.dll!NetworkManager::update() + 0x456\nGameEngine.dll!GameLoop::update() + 0x789"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_003", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="132",
        instruction=(
            "You are a Triage Engineer. A Kubernetes crash, 'crash_006', has been reported. "
            "A new bug should be created in the 'Game Analytics & Telemetry Platform' project titled 'K8s Crash' for the team lead of 'multiplayer.cpp'. "
            "An email should be sent to the lead with message 'New K8s Crash' and title 'Bug Assignment'. "
            "This should be linked as a related issue to the 'Implement multi-cloud application architecture' epic, "
            "the issue signature from the crash should be added as a comment, and the crash event's status should be updated to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_006"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Analytics & Telemetry Platform"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_005", "type": "bug", "title": "K8s Crash", "assignee_id": "user_003"}),
            Action(name="send_notification", kwargs={"project_id": "proj_005", "recipient_id": "user_003", "title": "Bug Assignment", "message": "New K8s Crash", "channel": "email"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement multi-cloud application architecture"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_006", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Kubernetes resource allocation failed: insufficient memory"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_006", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="075",
        instruction=(
            "You are a Triage Engineer. Crash report 'crash_001' just came in for an access violation. "
            "You should create a bug for this in the 'Game Build Pipeline Modernization' project with title 'Access Violation in Renderer' and assign it to the lead of 'renderer.cpp' file. "
            "It seems related to the main build pipeline epic with title 'Create automated game build pipeline', so please link them. "
            "Make sure to add 'Access violation in GameEngine.dll' to the bug report as a comment for context and then mark the crash as 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_001"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Access Violation in Renderer", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Access violation in GameEngine.dll"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_001", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="133",
        instruction=(
            "You are a Triage Engineer. An asset validation crash, 'crash_007', has occurred. "
            "A new bug should be created in the 'Game Engine Core Migration' project titled 'Asset Crash' for the owner of 'assets/models/environment/' file. "
            "A notification to slack channel should be sent to the team lead of that file with message 'New Asset Bug' and title 'Bug Assignment'. "
            "Also, you should link this as a dependency to the 'Implement game engine rendering pipeline' story, "
            "add the issue signature from the crash as a comment, and then update the crash event's status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_007"}),
            Action(name="find_file_owner", kwargs={"file_path": "assets/models/environment/"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_002"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Asset Crash", "assignee_id": "user_007"}),
            Action(name="send_notification", kwargs={"project_id": "proj_001", "recipient_id": "user_002", "title": "Bug Assignment", "message": "New Asset Bug", "channel": "slack"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement game engine rendering pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_001", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Asset validation failed: Texture size 4096x4096 exceeds maximum 2048x2048"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_007", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="121",
        instruction=(
            "You are a Triage Engineer. A network timeout crash, 'crash_003', has been reported. "
            "A new bug should be created in the 'Game Security & Anti-Cheat Framework' project titled 'Network Timeout Security Concern' for the team lead of 'multiplayer.cpp'. "
            "You should send a notification to slack to the lead with message 'New network security bug filed' and title 'Bug Assignment'. "
            "This bug should be linked as related to the 'Implement anti-cheat system integration' story, "
            "the stack trace from the crash should be added as a comment, and the crash status should be updated to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_003"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Network Timeout Security Concern", "assignee_id": "user_003"}),
            Action(name="send_notification", kwargs={"project_id": "proj_004", "recipient_id": "user_003", "title": "Bug Assignment", "message": "New network security bug filed", "channel": "slack"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "NetworkManager.dll!NetworkManager::checkConnection() + 0x123\nNetworkManager.dll!NetworkManager::update() + 0x456\nGameEngine.dll!GameLoop::update() + 0x789"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_003", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="118",
        instruction=(
            "You are a Triage Engineer. An asset validation crash, 'crash_007', has occurred. "
            "Find the owner of the 'assets/textures/character_models/' directory and their team lead. "
            "Create a new bug in the 'Game Security & Anti-Cheat Framework' project titled 'Asset Validation Security Issue' for the team lead. "
            "Also, send a notification to slack with the message 'New Asset Security Bug' and title 'New Bug Notification'. "
            "Link this as a blocker to the 'Implement anti-cheat system integration' story. "
            "Add the issue signature from the crash as a comment, and then update the crash event's status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_007"}),
            Action(name="find_file_owner", kwargs={"file_path": "assets/textures/character_models/"}),
            Action(name="get_user_by_id", kwargs={"id": "user_002"}),
            Action(name="get_team_by_id", kwargs={"id": "team_002"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_002"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Asset Validation Security Issue", "assignee_id": "user_002"}),
            Action(name="send_notification", kwargs={"project_id": "proj_004", "recipient_id": "user_002", "title": "New Bug Notification", "message": "New Asset Security Bug", "channel": "slack", "notification_type": "bug_assignment"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Asset validation failed: Texture size 4096x4096 exceeds maximum 2048x2048"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_007", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="119",
        instruction=(
            "You are a Triage Engineer. A compilation crash, 'crash_005', has been reported. "
            "A new bug should be created in the 'Game Build Pipeline Modernization' project titled 'Build Pipeline Blocked by Compilation Crash' for the team lead of 'renderer.cpp'. "
            "Also, you should send a notification to slack to the team lead with message 'New build-blocking bug assigned' and title 'New Build Blocker'. "
            "This bug should be linked as a blocker to the 'Create automated game build pipeline' epic, "
            "a comment should be added with the first line from crash's stack trace, and the crash event should be marked as 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_005"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Build Pipeline Blocked by Compilation Crash", "assignee_id": "user_001"}),
            Action(name="send_notification", kwargs={"project_id": "proj_002", "recipient_id": "user_001", "title": "New Build Blocker", "message": "New build-blocking bug assigned", "channel": "slack"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "renderer.cpp:245: issue: 'TextureManager::loadTexture' was not declared in this scope"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_005", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="095",
        instruction=(
            "You are a Triage Engineer. A critical access violation, 'crash_001', has been reported. "
            "Identify the owner of the 'renderer.cpp' file and their team lead. "
            "You should create a critical incident ticket in the 'Game Analytics & Telemetry Platform' project, as this crash may be impacting our data collection. Title it 'Critical Access Violation in Renderer'. "
            "Assign the incident to the team lead you found. "
            "This incident is related to the main analytics epic, so link it to the 'Implement multi-cloud application architecture' story. "
            "Also, you should add the crash fingerprint as a comment for tracking and update the crash event's status to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_001"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Analytics & Telemetry Platform"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_005", "type": "incident", "title": "Critical Access Violation in Renderer", "assignee_id": "user_001", "priority": "critical"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement multi-cloud application architecture"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_006", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "renderer_character_load_access_violation_xyz"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_001", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="089",
        instruction=(
            "You are a Triage Engineer. The compilation crash 'crash_005' has been reported again. "
            "Find the owner for the file 'renderer.cpp'. Then find the lead of that owner's team. "
            "Create a bug in the 'Game Build Pipeline Modernization' project with the title 'Recurring Compilation Crash' and assign it to the team lead. "
            "Find the 'Create automated game build pipeline' epic and link this bug as a dependency. "
            "Add the stack trace from the crash event as a comment. "
            "Also, update the crash's status to 'reopened'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_005"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Recurring Compilation Crash", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: renderer.cpp:245: issue: 'TextureManager::loadTexture' was not declared in this scope\nrenderer.cpp:245: note: suggested alternative: 'TextureManager::loadTextureAsync'"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_005", "status": "reopened"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="107",
        instruction=(
            "You are a Triage Engineer. A Kubernetes crash, 'crash_006', has been reported. "
            "Find the owner of 'multiplayer.cpp' and their team lead. "
            "Create a new bug in the 'Game Security & Anti-Cheat Framework' project titled 'K8s Deployment Failure' for the team lead. "
            "Send an email to the team lead with the message 'New K8s Bug' and title 'New Bug Notification'. "
            "This bug is blocking the 'Implement anti-cheat system integration' story, so link them. "
            "Add the issue signature from the crash as a comment. "
            "Finally, update the crash's status to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_006"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "K8s Deployment Failure", "assignee_id": "user_003"}),
            Action(name="send_notification", kwargs={"project_id": "proj_004", "recipient_id": "user_003", "title": "New Bug Notification", "message": "New K8s Bug", "channel": "email", "notification_type": "bug_assignment"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Kubernetes resource allocation failed: insufficient memory"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_006", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="101",
        instruction=(
            "You are a Triage Engineer. A new crash, 'crash_003', related to network timeouts has been reported. "
            "Find the owner of the 'multiplayer.cpp' file and their team lead. "
            "Create a new bug in the 'Multi-Platform Game Infrastructure' project titled 'Network Timeout Crash' and assign it to the file's owner. "
            "Then, send an email notification to the team lead to inform them of the new bug assigned to their team member, "
            "for message use 'New Bug Assigned to Your Team'. "
            "Link this bug as a dependency to the 'Implement cross-platform game infrastructure' epic. "
            "Finally, add 'Stack Trace: NetworkManager.dll' as a comment to the bug and mark the crash event as 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_003"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "Network Timeout Crash", "assignee_id": "user_008"}),
            Action(name="send_notification", kwargs={"project_id": "proj_003", "recipient_id": "user_003", "title": "New Bug Assigned to Your Team", "message": "New Bug Assigned to Your Team", "channel": "email", "notification_type": "bug_assignment"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: NetworkManager.dll"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_003", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="102",
        instruction=(
            "You are a Release Manager. Deployment 'deploy_004' failed, triggering a rollback. "
            "Create a new critical incident in the correct project titled 'Deployment Failure and Rollback Initiated for deploy_004'. "
            "Assign the incident to the team lead of 'Game Server Operations Team'. "
            "You should send a incident alert Slack notification to the team lead with the title 'Critical Incident: Deployment Failure' and message the same as the incident title. "
            "Also, add a comment to the new incident with 'Rolling back to version v1.0.4 as per rollback plan.'."
        ),
        actions=[
            Action(name="get_deployment_by_id", kwargs={"id": "deploy_004"}),
            Action(name="get_pipeline_by_id", kwargs={"id": "pipe_005"}),
            Action(name="get_project_by_id", kwargs={"id": "proj_003"}),
            Action(name="get_team_by_name", kwargs={"name": "Game Server Operations Team"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_005"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "incident", "title": "Deployment Failure and Rollback Initiated for deploy_004", "assignee_id": "user_005", "priority": "critical"}),
            Action(name="get_rollback_by_deployment_id", kwargs={"deployment_id": "deploy_004"}),
            Action(name="send_notification", kwargs={"project_id": "proj_003", "recipient_id": "user_005", "title": "Critical Incident: Deployment Failure", "message": "Deployment Failure and Rollback Initiated for deploy_004", "channel": "slack", "notification_type": "incident_alert"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Rolling back to version v1.0.4 as per rollback plan."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="103",
        instruction=(
            "You are a Triage Engineer. A compilation crash, 'crash_005', needs to be handled. "
            "You should find the owner of 'renderer.cpp' and their team lead. "
            "A bug should be created in the 'Game Security & Anti-Cheat Framework' project titled 'Compilation Failure Blocking Security Analysis' and assigned to the owner. "
            "Also, you should send a bug_assignment Slack notification to the team lead, with title 'High-Priority Bug Assigned to Your Team' and message 'Compilation Failure Blocking Security Analysis'. "
            "This issue blocks the main anti-cheat story with title 'Implement anti-cheat system integration', so link them accordingly. "
            "The crash event's status should be set to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_005"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Compilation Failure Blocking Security Analysis", "assignee_id": "user_001"}),
            Action(name="send_notification", kwargs={"project_id": "proj_004", "recipient_id": "user_001", "title": "High-Priority Bug Assigned to Your Team", "message": "Compilation Failure Blocking Security Analysis", "channel": "slack", "notification_type": "bug_assignment"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_005", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="104",
        instruction=(
            "You are a Dev Ops Engineer. A performance regression was detected in build 'run_007'. "
            "A high-priority bug should be created in the 'Game Engine Core Migration' project titled 'Performance Regression in Renderer' for the owner of the bisect result. "
            "A bug_assignment email should be sent to the owner with the title 'Action Required: Performance Regression' and a message 'Performance Regression in Renderer'. "
            "You should create a fix proposal of type 'performance_regression' with the title 'Optimize Texture Loading Performance' and description 'Address frame rate drop caused by recent renderer changes'. "
            "Also, you should update the build's triage status to 'fix_proposed'."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_007"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_007"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_004"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Performance Regression in Renderer", "assignee_id": "user_001", "priority": "high"}),
            Action(name="send_notification", kwargs={"project_id": "proj_001", "recipient_id": "user_001", "title": "Action Required: Performance Regression", "message": "Performance Regression in Renderer", "channel": "email", "notification_type": "bug_assignment"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_007", "bisect_result_id": "bisect_004", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "performance_regression", "title": "Optimize Texture Loading Performance", "description": "Address frame rate drop caused by recent renderer changes"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_007", "triage_status": "fix_proposed"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="106",
        instruction=(
            "You are a Triage Engineer. An access violation crash, 'crash_001', has occurred. "
            "A new bug should be created in the 'Game Build Pipeline Modernization' project titled 'Access Violation in Renderer' for the file owner of 'renderer.cpp'. "
            "You should send a bug assignment notification to slack to the team lead saying 'New Access Violation Bug' and title 'New Bug Notification'. "
            "This bug should be linked as related to the 'Create automated game build pipeline' epic. "
            "Also, add the crash's issue signature as a comment, and then update the crash event's status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_001"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Access Violation in Renderer", "assignee_id": "user_001"}),
            Action(name="send_notification", kwargs={"project_id": "proj_002", "recipient_id": "user_001", "title": "New Bug Notification", "message": "New Access Violation Bug", "channel": "slack", "notification_type": "bug_assignment"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Access violation in GameEngine.dll at 0x00007FF6A1B2C456"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_001", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="109",
        instruction=(
            "You are a Triage Engineer. A compilation crash, 'crash_005', has been reported again. "
            "Find the owner of 'renderer.cpp' and their team lead. "
            "Create a new bug in the 'Game Security & Anti-Cheat Framework' project titled 'Recurring Compilation Failure' and assign it to the team lead. "
            "Send an email notification to the team lead with the message 'Recurring Compilation Bug' and title 'New Bug Notification'. "
            "This is a dependency for the 'Implement anti-cheat system integration' story, so link them. "
            "Add the stack trace from the crash as a comment, and then update the crash's status to 'reopened'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_005"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Recurring Compilation Failure", "assignee_id": "user_001"}),
            Action(name="send_notification", kwargs={"project_id": "proj_004", "recipient_id": "user_001", "title": "New Bug Notification", "message": "Recurring Compilation Bug", "channel": "email", "notification_type": "bug_assignment"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "renderer.cpp:245: issue: 'TextureManager::loadTexture' was not declared in this scope"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_005", "status": "reopened"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="110",
        instruction=(
            "You are a Triage Engineer. A new access violation crash, 'crash_001', has been logged. "
            "A bug should be created in the 'Game Analytics & Telemetry Platform' project titled 'Renderer Access Violation' for the team lead of ''renderer.cpp'' file. "
            "Send a bug assignment notification to slack with the message 'New Renderer Crash' and title 'New Bug Notification'. "
            "You should link this bug as a blocker to the 'Implement multi-cloud application architecture' epic. "
            "Also, add the crash's issue signature as a comment, "
            "and update the crash event's status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_001"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Analytics & Telemetry Platform"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_005", "type": "bug", "title": "Renderer Access Violation", "assignee_id": "user_001"}),
            Action(name="send_notification", kwargs={"project_id": "proj_005", "recipient_id": "user_001", "title": "New Bug Notification", "message": "New Renderer Crash", "channel": "slack", "notification_type": "bug_assignment"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement multi-cloud application architecture"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_006", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Access violation in GameEngine.dll at 0x00007FF6A1B2C456"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_001", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="111",
        instruction=(
            "You are a Triage Engineer. A network crash, 'crash_003', has been reported. "
            "A new bug should be created in the 'Game Engine Core Migration' project titled 'Network Crash in Multiplayer' and assigned to the team lead of 'multiplayer.cpp' file. "
            "An email notification should be sent with the message 'New Network Crash' and title 'New Bug Notification'. "
            "You should link this bug as a dependency to the 'Implement game engine rendering pipeline' story. "
            "Also, add the stack trace from the crash as a comment, and then update the crash status to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_003"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Network Crash in Multiplayer", "assignee_id": "user_003"}),
            Action(name="send_notification", kwargs={"project_id": "proj_001", "recipient_id": "user_003", "title": "New Bug Notification", "message": "New Network Crash", "channel": "email", "notification_type": "bug_assignment"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement game engine rendering pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_001", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "NetworkManager.dll!NetworkManager::checkConnection() + 0x123\nNetworkManager.dll!NetworkManager::update() + 0x456\nGameEngine.dll!GameLoop::update() + 0x789"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_003", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="112",
        instruction=(
            "You are a Triage Engineer. A Kubernetes crash, 'crash_006', needs to be triaged. "
            "Create a new bug in the 'Game Build Pipeline Modernization' project titled 'K8s Crash' for the team lead of 'multiplayer.cpp' file. "
            "Also, you should send a notification to slack with the message 'New K8s Crash' and title 'New Bug Notification'. "
            "Link this as a related issue to the 'Create automated game build pipeline' epic. "
            "Also, add the crash's issue signature as a comment, and then update the crash event's status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_006"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "K8s Crash", "assignee_id": "user_003"}),
            Action(name="send_notification", kwargs={"project_id": "proj_002", "recipient_id": "user_003", "title": "New Bug Notification", "message": "New K8s Crash", "channel": "slack", "notification_type": "bug_assignment"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Kubernetes resource allocation failed: insufficient memory"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_006", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="113",
        instruction=(
            "We've got an asset validation crash (ID: crash_007) that needs triaging. "
            "A new bug should be created in the 'Multi-Platform Game Infrastructure' project titled 'Asset Validation Failure' and assigned to the team lead of 'assets/textures/character_models/' directory. "
            "An email should be sent to the team lead with the title 'New Bug Notification' and message 'New Asset Bug' about this. "
            "Since this is blocking the 'Implement cross-platform game infrastructure' epic, make sure to link them appropriately. "
            "Also, you should add the crash's issue signature as a comment to the bug, and finally mark the crash event status as 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_007"}),
            Action(name="find_file_owner", kwargs={"file_path": "assets/textures/character_models/"}),
            Action(name="get_user_by_id", kwargs={"id": "user_002"}),
            Action(name="get_team_by_id", kwargs={"id": "team_002"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_002"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "Asset Validation Failure", "assignee_id": "user_002"}),
            Action(name="send_notification", kwargs={"project_id": "proj_003", "recipient_id": "user_002", "title": "New Bug Notification", "message": "New Asset Bug", "channel": "email", "notification_type": "bug_assignment"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Asset validation failed: Texture size 4096x4096 exceeds maximum 2048x2048"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_007", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="114",
        instruction=(
            "A compilation crash (ID: crash_005) just came in and needs your attention. "
            "Then create a new bug in the 'Game Analytics & Telemetry Platform' project called 'Renderer Compilation Issue' for the team lead of 'renderer.cpp'. "
            "Send them a bug assignment notification to slack channel titled 'New Bug Notification' with the message 'New Compilation Issue'. "
            "This bug is a dependency for the 'Implement multi-cloud application architecture' epic, so please link them accordingly. "
            "Also, you should add the first line of the stack trace from the crash as a comment to the bug, and update the crash status to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_005"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Analytics & Telemetry Platform"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_005", "type": "bug", "title": "Renderer Compilation Issue", "assignee_id": "user_001"}),
            Action(name="send_notification", kwargs={"project_id": "proj_005", "recipient_id": "user_001", "title": "New Bug Notification", "message": "New Compilation Issue", "channel": "slack", "notification_type": "bug_assignment"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement multi-cloud application architecture"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_006", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "renderer.cpp:245: issue: 'TextureManager::loadTexture' was not declared in this scope"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_005", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="116",
        instruction=(
            "You are a Triage Engineer. A network timeout crash, 'crash_003', has been reported and you should handle it. "
            "Create a new bug in the 'Game Build Pipeline Modernization' project titled 'Network Timeout in Build Pipeline' for the team lead of 'multiplayer.cpp' file. "
            "You should send a notification to slack with the message 'New Network Timeout Bug' and title 'New Bug Notification'. "
            "Link this bug as a blocker to the 'Create automated game build pipeline' epic. "
            "Also, add the stack trace from the crash as a comment, and then update the crash status to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_003"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Network Timeout in Build Pipeline", "assignee_id": "user_003"}),
            Action(name="send_notification", kwargs={"project_id": "proj_002", "recipient_id": "user_003", "title": "New Bug Notification", "message": "New Network Timeout Bug", "channel": "slack", "notification_type": "bug_assignment"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "NetworkManager.dll!NetworkManager::checkConnection() + 0x123\nNetworkManager.dll!NetworkManager::update() + 0x456\nGameEngine.dll!GameLoop::update() + 0x789"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_003", "status": "investigating"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="051",
        instruction=(
            "You are a Triage Engineer. Crash report 'crash_005' has been filed for a compilation issue. "
            "A new bug should be created in the 'Game Engine Core Migration' project "
            "with the title 'Compilation Crash in Renderer' and assigned to the team lead of the suspect file 'renderer.cpp'. "
            "You should find the original 'Implement game engine rendering pipeline' story and link this new bug as being blocked by it. "
            "A comment should be added to the new bug with the stack trace from the crash event with 'Stack Trace: renderer.cpp'. "
            "Also, the crash event's status should be updated to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_005"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Compilation Crash in Renderer", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement game engine rendering pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_001", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: renderer.cpp"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_005", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="053",
        instruction=(
            "You are a Dev Ops Engineer. A performance regression was found in build 'run_007'. "
            "Find the bisect result and the responsible owner. "
            "Create a new bug in the 'Game Engine Core Migration' project titled 'Performance Regression in Texture System' and assign it to the owner. "
            "Then, create a fix proposal of type 'performance_regression' with the title 'Optimize Texture Loading' and a description of 'Implement texture caching to fix frame rate drop'. "
            "Finally, you should update the build's triage status to 'fix_proposed'."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_007"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_007"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_004"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Performance Regression in Texture System", "assignee_id": "user_001"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_007", "bisect_result_id": "bisect_004", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "performance_regression", "title": "Optimize Texture Loading", "description": "Implement texture caching to fix frame rate drop"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_007", "triage_status": "fix_proposed"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="054",
        instruction=(
            "You are a Triage Engineer. A test failure for 'AIPathfindingTest::NavigationMeshTest' has been reported. "
            "A fingerprint should be generated for this test failure. "
            "If there are no existing bugs with this fingerprint, "
            "you should find the owner of the 'src/game/ai/pathfinding.h' file. "
            "A new bug should be created in the 'Game Engine Core Migration' project, "
            "titled 'AI Test Failure: Navmesh Generation Timeout'. "
            "This bug with comment 'Test timed out' should be assigned to the file's owner. "
        ),
        actions=[
            Action(name="get_test_result_by_id", kwargs={"id": "test_result_002"}),
            Action(name="generate_fingerprint_for_test_result", kwargs={"test_result_id": "test_result_002"}),
            Action(name="find_bug_by_crash_fingerprint", kwargs={"crash_fingerprint": "ai_navmesh_generation_timeout_abc"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/ai/pathfinding.h"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "AI Test Failure: Navmesh Generation Timeout", "assignee_id": "user_003"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Test timed out"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="055",
        instruction=(
            "You are a Triage Engineer. Crash report 'crash_005' indicates a compilation issue. "
            "You should find the full path for the module 'renderer.cpp' from the crash's stack trace in order to get the owner and his team. "
            "A new critical bug should be created in the 'Game Engine Core Migration' project "
            "titled 'Critical Compilation Crash in Renderer' and assigned to the team lead of the team. "
            "A comment 'Associated crash fingerprint: build_compilation_missing_declaration_xyz' should be added to the bug. "
            "This bug should be linked to the main 'Implement game engine rendering pipeline' story "
            "as a blocker and have the crash event's status set to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_005"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Critical Compilation Crash in Renderer", "assignee_id": "user_001", "priority": "critical"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Associated crash fingerprint: build_compilation_missing_declaration_xyz"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement game engine rendering pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_001", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_005", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="058",
        instruction=(
            "You are a Dev Ops Engineer. The 'run_005' build failed with an integration issue. "
            "You should find the bisect result, and from that, find the owner of the first suspect file. "
            "A new bug should be created in the 'Game Engine Core Migration' project "
            "titled 'Integration Failure in Connection Manager' and assigned to this owner. "
            "ALso, a fix proposal for the 'integration_failure' should be created "
            "with the title 'Fix Connection Timeout Logic' and "
            "a description of 'The connection manager is timing out during integration tests'. "
            "Finally, you should link the new bug to the main 'Multiplayer' epic (work_004) and "
            "update the build's triage status to 'fix_proposed'."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_005"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_005"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Integration Failure in Connection Manager", "assignee_id": "user_008"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_005", "bisect_result_id": "bisect_003", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "integration_failure", "title": "Fix Connection Timeout Logic", "description": "The connection manager is timing out during integration tests"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "epic"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_005", "triage_status": "fix_proposed"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="061",
        instruction=(
            "You are a Triage Engineer. A new crash, 'crash_001', has been reported for an access violation. "
            "A new bug report should be created in the 'Game Build Pipeline Modernization' project with the title 'Access Violation in Renderer' and assigned to the team lead of the 'renderer.cpp' file implicated in the crash. "
            "You should find the 'Create automated game build pipeline' epic and link this new bug to it as a related issue. "
            "A comment 'Issue Signature: Access violation' should be added to the bug. "
            "Also, the crash event's status should be updated to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_001"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Access Violation in Renderer", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Issue Signature: Access violation"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_001", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="062",
        instruction=(
            "You are a Triage Engineer. A network timeout crash, 'crash_003', has occurred. "
            "Identify the owner of 'multiplayer.cpp' and their team lead. "
            "File a new bug in the 'Multi-Platform Game Infrastructure' project titled 'Network Timeout During Gameplay' and assign it to the team lead. "
            "Link this bug as a dependency to the 'Implement cross-platform game infrastructure' epic. "
            "Add 'Stack Trace: NetworkManager.dll' as a comment to the bug. "
            "To conclude, update the crash event's status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_003"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "Network Timeout During Gameplay", "assignee_id": "user_003"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: NetworkManager.dll"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_003", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="063",
        instruction=(
            "You are a Triage Engineer. Crash 'crash_006' indicates a Kubernetes issue. "
            "Since this is an infrastructure problem, you should find the owner of 'multiplayer.cpp' to identify the responsible team and their lead. "
            "A new bug should be created in the 'Game Security & Anti-Cheat Framework' project titled 'Kubernetes Deployment Crash' and assigned to the team lead. "
            "This new bug should be linked as being blocked by the 'Implement anti-cheat system integration' story. "
            "Add 'Kubernetes resource allocation failed: insufficient memory' to the new bug as a comment. "
            "Finally, change the crash event's status to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_006"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Kubernetes Deployment Crash", "assignee_id": "user_003"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Kubernetes resource allocation failed: insufficient memory"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_006", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="064",
        instruction=(
            "You are a Triage Engineer. An asset validation crash, 'crash_007', needs to be addressed. "
            "Create a new bug in the 'Game Engine Core Migration' project titled 'Asset Validation Failure: Texture Size' and assign it to the team lead of 'assets/textures/character_models/' asset folder. "
            "You should link this bug to the 'Implement game engine rendering pipeline' story as a related issue. "
            "Add 'Issue Signature: Asset validation failed' comment to the bug. "
            "Also, you should update the crash event status to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_007"}),
            Action(name="find_file_owner", kwargs={"file_path": "assets/textures/character_models/"}),
            Action(name="get_user_by_id", kwargs={"id": "user_002"}),
            Action(name="get_team_by_id", kwargs={"id": "team_002"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_002"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Asset Validation Failure: Texture Size", "assignee_id": "user_002"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement game engine rendering pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_001", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Issue Signature: Asset validation failed"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_007", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="065",
        instruction=(
            "You are a Triage Engineer. The compilation crash 'crash_005' has been reported again. "
            "Find the owner for the file 'renderer.cpp'. Then find the lead of that owner's team. "
            "You should create a bug in the 'Game Build Pipeline Modernization' project with the title 'Recurring Compilation Crash' and assign it to the team lead. "
            "Find the 'Create automated game build pipeline' epic and link this bug as a dependency. "
            "Add 'Stack Trace: renderer.cpp' as a comment to the created bug. "
            "Also, update the crash's status to 'reopened'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_005"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Recurring Compilation Crash", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: renderer.cpp"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_005", "status": "reopened"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="066",
        instruction=(
            "You are a Triage Engineer. A new access violation crash, 'crash_001', has been logged. "
            "Find the owner of the 'renderer.cpp' file and their team lead. "
            "Create a bug in the 'Multi-Platform Game Infrastructure' project titled 'Access Violation on Character Load' and assign it to the team lead. "
            "Link this bug to the 'Implement cross-platform game infrastructure' epic as a blocker. "
            "Add 'Issue Signature: Access violation in GameEngine.dll' as a comment for the bug. "
            "To finish, update the crash event's status to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_001"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "Access Violation on Character Load", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Issue Signature: Access violation in GameEngine.dll"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_001", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="001",
        instruction=(
            "You are a Dev Ops Engineer. A critical build 'run_001' has failed."
            "You should reate a bug report for the issue with title 'Build failure in renderer on feature/new-renderer', "
            "for the bug owner you should use the owner of the bisect that is connected to the critical bug. "
            "Also, create a fix proposal with title 'Fix missing TextureManager::loadTexture declaration', "
            "description 'Add missing function declaration in texture_manager.h header file.' and type 'compilation_issue'. "
            "Finally, mark the build run as resolved."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_001"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_001"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_001"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Build failure in renderer on feature/new-renderer", "assignee_id": "user_001"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_001", "bisect_result_id": "bisect_001", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "compilation_issue", "title": "Fix missing TextureManager::loadTexture declaration", "description": "Add missing function declaration in texture_manager.h header file."}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_001", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="002",
        instruction=(
            "You are a Security Engineer. A critical vulnerability has been found "
            "in the 'game-engine' repository's dependencies for CVE-2024-2345. "
            "Please create a critical bug report for the vulnerability with "
            "title 'Critical Security Vulnerability: CVE-2024-2345 in Docker', assign it to the correct team lead, "
            "and label it as a security issue. "
            "Also you should update the vulnerability status to 'triaged'. "
        ),
        actions=[
            Action(name="search_vulnerabilities_by_cve", kwargs={"cve": "CVE-2024-2345"}),
            Action(name="get_repository_by_name", kwargs={"name": "game-engine"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="find_project_owner_team", kwargs={"project_id": "proj_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Critical Security Vulnerability: CVE-2024-2345 in Docker", "assignee_id": "user_001", "priority": "critical"}),
            Action(name="get_label_by_name", kwargs={"name": "security"}),
            Action(name="add_label_to_work_item", kwargs={"work_item_id": "work_028", "label_id": "label_004"}),
            Action(name="update_vulnerability_status", kwargs={"id": "vuln_006", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="004",
        instruction=(
            "You are a Triage Engineer. A crash report, 'crash_004', just came in. "
            "It looks like a duplicate of a known issue. "
            "For this latest crash create a new bug report with title '[Duplicate] Multiplayer Connection Timeout' "
            "in project 'Game Engine Core Migration', "
            "and then close the bug and set comment 'Closing as a duplicate.' "
            "You should alsoset the status to duplicate for the crash report."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_004"}),
            Action(name="find_crashes_by_crash_fingerprint", kwargs={"crash_fingerprint": "network_connection_timeout_30s_xyz"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "[Duplicate] Multiplayer Connection Timeout"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Closing as a duplicate."}),
            Action(name="update_work_item_state", kwargs={"id": "work_028", "new_state": "closed"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_004", "status": "duplicate"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="006",
        instruction=(
            "You are a Release Manager. Deployment 'deploy_004' to production failed. We need to roll back immediately. "
            "Find the rollback plan for this deployment and execute it. "
            "Once the rollback is underway, open a critical incident ticket "
            "with title 'Critical Rollback: Deployment deploy_004 failed' and assign it to the "
            "'Game Server Operations Team' team lead in 'Game Analytics & Telemetry Platform' project "
            "for a full investigation."
        ),
        actions=[
            Action(name="get_deployment_by_id", kwargs={"id": "deploy_004"}),
            Action(name="get_rollback_by_deployment_id", kwargs={"deployment_id": "deploy_004"}),
            Action(name="create_deployment", kwargs={"pipeline_id": "pipe_005", "environment_id": "env_010", "deployed_by": "user_004", "version": "v1.0.4", "status": "in_progress"}),
            Action(name="get_team_by_name", kwargs={"name": "Game Server Operations Team"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_005"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Analytics & Telemetry Platform"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_005", "type": "incident", "title": "Critical Rollback: Deployment deploy_004 failed",  "assignee_id": "user_005", "priority": "critical", "state": "open"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="012",
        instruction=(
            "You are a Triage Engineer. Crash report 'crash_002' has come in. "
            "It appears to be a duplicate of an existing crash. "
            "Create a new bug for this specific instance with the title "
            "'[Duplicate Crash] Character Load Access Violation on RTX 3070', assigning it to the same person as the original, "
            "or to None if there is no assignee person on the original bug. "
            "Link the new bug to the original as a duplicate. "
            "You should also close the new bug and update the crash event's status to 'duplicate'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_002"}),
            Action(name="find_bug_by_crash_fingerprint", kwargs={"crash_fingerprint": "renderer_character_load_access_violation_xyz"}),
            Action(name="get_work_item_assignee", kwargs={"id": "work_026"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "[Duplicate Crash] Character Load Access Violation on RTX 3070", "assignee_id": None}),
            Action(name="link_work_items", kwargs={"parent_id": "work_026", "child_id": "work_028", "link_type": "duplicate"}),
            Action(name="update_work_item_state", kwargs={"id": "work_028", "new_state": "closed"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_002", "status": "duplicate"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="014",
        instruction=(
            "You are a Dev Ops Engineer. The build 'run_003' failed due to a test failure. "
            "Your task is to create a new bug report with the title 'Unit test failure in renderer on feature/new-renderer'. "
            "Assign this bug to the owner identified by the bisect operation. "
            "Then, draft a fix proposal titled 'Fix texture format validation' "
            "with the description 'Update texture format validation to handle new character texture format' "
            "and type 'test_failure'. "
            "Finally, update the build run's triage status to 'resolved'."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_003"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_003"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_002"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Unit test failure in renderer on feature/new-renderer", "assignee_id": "user_001"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_003", "bisect_result_id": "bisect_002", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "test_failure", "title": "Fix texture format validation", "description": "Update texture format validation to handle new character texture format"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_003", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="016",
        instruction=(
            "You are a Dev Ops Engineer. A performance regression was detected in build 'run_007'. "
            "Please create a new bug titled 'Performance regression in renderer' "
            "and assign it to the owner identified by the bisect. "
            "Then, create a fix proposal with the title 'Optimize texture loading performance' "
            "and a description of 'Address frame rate drop caused by recent renderer changes', "
            "and type 'performance_regression'. "
            "Finally, set the build run's triage status to 'resolved'."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_007"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_007"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_004"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Performance regression in renderer", "assignee_id": "user_001"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_007", "bisect_result_id": "bisect_004", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "performance_regression", "title": "Optimize texture loading performance", "description": "Address frame rate drop caused by recent renderer changes"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_007", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="017",
        instruction=(
            "You are a Release Manager. Deployment 'deploy_007' is not stable in production. "
            "A rollback is required to be initiated. "
            "Then, a incident ticket should be created in the 'Mobile App Infrastructure' project "
            "titled 'Critical Rollback: Deployment deploy_007 is not stable'. "
            "You should assign the ticket to the lead of the 'Game Server Operations Team' team."
        ),
        actions=[
            Action(name="get_deployment_by_id", kwargs={"id": "deploy_007"}),
            Action(name="get_rollback_by_deployment_id", kwargs={"deployment_id": "deploy_007"}),
            Action(name="create_deployment", kwargs={"pipeline_id": "pipe_009", "environment_id": "env_019", "deployed_by": "user_006", "version": "v2.2.1", "status": "in_progress"}),
            Action(name="get_team_by_name", kwargs={"name": "Game Server Operations Team"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_005"}),
            Action(name="get_project_by_name", kwargs={"name": "Mobile App Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_017", "type": "incident", "title": "Critical Rollback: Deployment deploy_007 is not stable", "assignee_id": "user_005", "priority": "critical", "state": "open"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="018",
        instruction=(
            "You are a Release Manager. The production deployment 'deploy_009' is not stable in production. "
            "The rollback process has to be initialised. "
            "After that, create an incident ticket with the title 'Production Rollback: Deployment deploy_009 is not stable' "
            "in the 'Infrastructure as Code Migration' project. "
            "The ticket should be assigned to the lead of the 'Infrastructure Automation' team."
        ),
        actions=[
            Action(name="get_deployment_by_id", kwargs={"id": "deploy_009"}),
            Action(name="get_rollback_by_deployment_id", kwargs={"deployment_id": "deploy_009"}),
            Action(name="create_deployment", kwargs={"pipeline_id": "pipe_011", "environment_id": "env_024", "deployed_by": "user_008", "version": "v1.4.2", "status": "in_progress"}),
            Action(name="get_team_by_name", kwargs={"name": "Infrastructure Automation"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_010"}),
            Action(name="get_project_by_name", kwargs={"name": "Infrastructure as Code Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_010", "type": "incident", "title": "Production Rollback: Deployment deploy_009 is not stable", "assignee_id": "user_003", "priority": "critical", "state": "open"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="019",
        instruction=(
            "You are a Release Manager. Deployment 'deploy_010' has failed and needs to be rolled back. "
            "Find the necessary rollback information and begin the process. "
            "Then, an incident should be created titled 'Rollback Triggered: Deployment deploy_010 failed' "
            "for the 'API Gateway Implementation' project. "
            "Assign this ticket to the lead of the 'Developer Experience' team."
        ),
        actions=[
            Action(name="get_deployment_by_id", kwargs={"id": "deploy_010"}),
            Action(name="get_rollback_by_deployment_id", kwargs={"deployment_id": "deploy_010"}),
            Action(name="create_deployment", kwargs={"pipeline_id": "pipe_013", "environment_id": "env_029", "deployed_by": "user_009", "version": "v2.0.2", "status": "in_progress"}),
            Action(name="get_team_by_name", kwargs={"name": "Developer Experience"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_006"}),
            Action(name="get_project_by_name", kwargs={"name": "API Gateway Implementation"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_013", "type": "incident", "title": "Rollback Triggered: Deployment deploy_010 failed", "assignee_id": "user_016", "priority": "critical", "state": "open"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="020",
        instruction=(
            "You are a Triage Engineer. Another crash, 'crash_001', has been reported. "
            "Find the original bug associated with this crash's fingerprint. "
            "Then, a new bug titled '[Duplicate Crash] Character Load Access Violation on RTX 4080', "
            "should be created and assigned to Alex Chen. "
            "This new bug should be linked as a duplicate of the original one. "
            "You should also close the new bug and update the crash event's status to 'duplicate'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_001"}),
            Action(name="find_bug_by_crash_fingerprint", kwargs={"crash_fingerprint": "renderer_character_load_access_violation_xyz"}),
            Action(name="get_user_by_name", kwargs={"name": "Alex Chen"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "[Duplicate Crash] Character Load Access Violation on RTX 4080", "assignee_id": "user_001"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_026", "child_id": "work_028", "link_type": "duplicate"}),
            Action(name="update_work_item_state", kwargs={"id": "work_028", "new_state": "closed"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_001", "status": "duplicate"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="021",
        instruction=(
            "You are a Triage Engineer. We've received crash report 'crash_003' that you should handle. "
            "This seems to be a new issue. A bug report should be created "
            "under 'Game Security & Anti-Cheat Framework' project "
            "with the title 'Network Connection Timeout in Multiplayer'. "
            "And assigned it to the owner of the 'src/game/network/multiplayer.cpp' file. "
            "A new comment 'New crash report, needs investigation.' should be added to the new created bug "
            "and the crash event marked as 'analyzed'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_003"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Network Connection Timeout in Multiplayer", "assignee_id": "user_008"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "New crash report, needs investigation."}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_003", "status": "analyzed"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="022",
        instruction=(
            "You are a Triage Engineer. The bug 'Texture compression artifact on character model' "
            "appears to be a duplicate of the 'Game crashes when loading character model' bug. "
            "They should be linked as duplicates, add a comment to the duplicate bug "
            "with 'Closing as a duplicate.' should be added, and then you should close the bug."
        ),
        actions=[
            Action(name="find_work_item_by_title", kwargs={"title": "Texture compression artifact on character model"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Game crashes when loading character model"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_026", "child_id": "work_027", "link_type": "duplicate"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_027", "comment": "Closing as a duplicate."}),
            Action(name="update_work_item_state", kwargs={"id": "work_027", "new_state": "closed"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="023",
        instruction=(
            "You are a Dev Ops Engineer. Build 'run_003' has a test failure. "
            "A bug report should be created with the title 'Renderer test failure on feature/new-renderer' "
            "and assigned to the owner identified by the bisect operation. "
            "Then, you should create a fix proposal titled 'Fix texture validation in renderer tests' "
            "with the description 'Update test case to handle new texture formats' "
            "and type 'test_failure'. "
            "Finally, the build's triage status should be set to 'resolved'."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_003"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_003"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_002"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Renderer test failure on feature/new-renderer", "assignee_id": "user_001"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_003", "bisect_result_id": "bisect_002", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "test_failure", "title": "Fix texture validation in renderer tests", "description": "Update test case to handle new texture formats"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_003", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="024",
        instruction=(
            "You are a Dev Ops Engineer. An integration test failed in build 'run_005'. "
            "Create a bug for this with the title 'Multiplayer connection test failing' and assign it to the bisect owner. "
            "Draft a fix proposal titled 'Resolve multiplayer connection timeout' and describe it as 'Increase timeout to prevent integration test failures', with type 'integration_failure'. "
            "Lastly, mark the build 'run_005' as triaged by setting its status to 'resolved'."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_005"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_005"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_003"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Multiplayer connection test failing", "assignee_id": 'user_008'}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_005", "bisect_result_id": "bisect_003", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "integration_failure", "title": "Resolve multiplayer connection timeout", "description": "Increase timeout to prevent integration test failures"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_005", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="025",
        instruction=(
            "You are a Dev Ops Engineer. Build 'run_006' failed due to an asset validation issue. "
            "Please open a bug titled 'Asset validation failure for oversized texture' and "
            "assign it to the owner from the bisect report. "
            "Then, a fix proposal should be created with title 'Resize oversized hero texture' and with "
            "the description 'Resize hero_character_diffuse.png to meet engine requirements' and type 'asset_validation_issue'. "
            "Finally, update the build's triage status to 'resolved'."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_006"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_006"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_006"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-assets"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Asset validation failure for oversized texture", "assignee_id": 'user_008'}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_006", "bisect_result_id": "bisect_006", "repo": "game-assets", "branch": "feature/new-assets", "fix_type": "asset_validation_issue", "title": "Resize oversized hero texture", "description": "Resize hero_character_diffuse.png to meet engine requirements"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_006", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="026",
        instruction=(
            "You are a Dev Ops Engineer. A localization issue was found in build 'run_008'. "
            "A bug should be created with the title 'Localization text overflows UI' and "
            "assigned to the responsible owner from the bisect. "
            "Then, create a fix proposal titled 'Fix German UI text overflow' "
            "with the description 'Shorten German translation for ui.main_menu.start_game to fit constraints' "
            "and type 'localization_issue'. "
            "To finish, mark build 'run_008' as resolved."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_008"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_008"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_007"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-localization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "Localization text overflows UI", "assignee_id": 'user_008'}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_008", "bisect_result_id": "bisect_007", "repo": "game-localization", "branch": "feature/localization-update", "fix_type": "localization_issue", "title": "Fix German UI text overflow", "description": "Shorten German translation for ui.main_menu.start_game to fit constraints"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_008", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="027",
        instruction=(
            "You are a Dev Ops Engineer. You have to triage the compilation failure in build 'run_001'. "
            "A bug titled 'Compilation failed on feature/new-renderer' should be created for the bisect owner. "
            "Then, a fix proposal should be created titled 'Fix compilation issue in TextureManager' "
            "with description 'A declaration is missing for loadTexture in the header file' and type 'compilation_issue'. "
            "Finally, the build run should be resolved."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_001"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_001"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_001"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Compilation failed on feature/new-renderer", "assignee_id": "user_001"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_001", "bisect_result_id": "bisect_001", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "compilation_issue", "title": "Fix compilation issue in TextureManager", "description": "A declaration is missing for loadTexture in the header file."}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_001", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="028",
        instruction=(
            "You are a Dev Ops Engineer. You have to handle the test failure from build 'run_003'. "
            "A bug should be created with the title 'Failing unit test in renderer module' for the person identified by the bisect. "
            "Also, fix proposal should be created for a 'test_failure' with the title "
            "'Correct texture validation logic' and description 'The unit test is failing due to incorrect texture format validation logic'. "
            "Finally, the build run should be resolved."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_003"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_003"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_002"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Failing unit test in renderer module", "assignee_id": "user_001"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_003", "bisect_result_id": "bisect_002", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "test_failure", "title": "Correct texture validation logic", "description": "The unit test is failing due to incorrect texture format validation logic"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_003", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="029",
        instruction=(
            "You are a Dev Ops Engineer. Address the integration failure in build 'run_005'. "
            "Create a bug titled 'Multiplayer integration test failing' for the bisect owner. "
            "Draft a fix proposal for an 'integration_failure' with the title 'Fix connection timeout in multiplayer tests' and description 'The integration test is failing due to a connection timeout in the multiplayer module'. "
            "Finally, the build run should be resolved."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_005"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_005"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_003"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Multiplayer integration test failing", "assignee_id": 'user_008'}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_005", "bisect_result_id": "bisect_003", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "integration_failure", "title": "Fix connection timeout in multiplayer tests", "description": "The integration test is failing due to a connection timeout in the multiplayer module"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_005", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="030",
        instruction=(
            "You are a Dev Ops Engineer. Triage the asset validation failure in build 'run_006'. "
            "Create a bug for the bisect owner with the title 'Invalid asset: oversized texture'. "
            "Then, create a fix proposal for an 'asset_validation_issue' titled 'Resize hero texture to pass validation' with the description 'The hero_character_diffuse.png texture is too large and needs to be resized'. "
            "Finally, resolve the build."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_006"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_006"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_006"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-assets"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Invalid asset: oversized texture", "assignee_id": 'user_008'}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_006", "bisect_result_id": "bisect_006", "repo": "game-assets", "branch": "feature/new-assets", "fix_type": "asset_validation_issue", "title": "Resize hero texture to pass validation", "description": "The hero_character_diffuse.png texture is too large and needs to be resized"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_006", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="031",
        instruction=(
            "You are a Dev Ops Engineer. Resolve the localization issue in build 'run_008'. "
            "File a bug for the bisect owner with the title 'UI text overflow in German localization'. "
            "Then, create a fix proposal for a 'localization_issue' titled 'Correct overflowing German UI text' with the description 'The German translation for ui.main_menu.start_game is too long and causes a UI overflow'. "
            "Finally, mark the build run's triage status as 'resolved'."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_008"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_008"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_007"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-localization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "UI text overflow in German localization", "assignee_id": 'user_008'}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_008", "bisect_result_id": "bisect_007", "repo": "game-localization", "branch": "feature/localization-update", "fix_type": "localization_issue", "title": "Correct overflowing German UI text", "description": "The German translation for ui.main_menu.start_game is too long and causes a UI overflow"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_008", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="032",
        instruction=(
            "You are a Dev Ops Engineer. Handle the compilation failure in build 'run_001'. "
            "Create a bug with the title 'Build error in renderer module' for the bisect owner. "
            "Then, create a fix proposal for a 'compilation_issue' titled 'Fix undeclared function in renderer' with the description 'The function loadTexture is not declared in the TextureManager header, causing a compilation failure'. "
            "Finally, resolve the build."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_001"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_001"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_001"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Build error in renderer module", "assignee_id": "user_001"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_001", "bisect_result_id": "bisect_001", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "compilation_issue", "title": "Fix undeclared function in renderer", "description": "The function loadTexture is not declared in the TextureManager header, causing a compilation failure"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_001", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="033",
        instruction=(
            "You are a Dev Ops Engineer. Triage the test failure in build 'run_003'. "
            "Create a bug titled 'Unit test for texture loading failing' for the bisect owner. "
            "Then, draft a fix proposal for a 'test_failure' with the title 'Update texture validation in unit tests' and a description of 'The texture format validation in the renderer unit test needs to be updated for new formats'. "
            "Finally, mark the build as resolved."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_003"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_003"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_002"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Unit test for texture loading failing", "assignee_id": "user_001"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_003", "bisect_result_id": "bisect_002", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "test_failure", "title": "Update texture validation in unit tests", "description": "The texture format validation in the renderer unit test needs to be updated for new formats"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_003", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="034",
        instruction=(
            "You are a Dev Ops Engineer. Address the integration failure from build 'run_005'. "
            "A bug should be created for the person identified by the bisect with the title "
            "'Multiplayer connection is timing out in integration tests'. "
            "A fix proposal should be drafted for an 'integration_failure' with "
            "the title 'Fix multiplayer test timeout' and "
            "a description of 'The multiplayer integration test is failing due to a timeout. The threshold should be increased'. "
            "Finally, you should resolve the build run."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_005"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_005"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_003"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Multiplayer connection is timing out in integration tests", "assignee_id": 'user_008'}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_005", "bisect_result_id": "bisect_003", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "integration_failure", "title": "Fix multiplayer test timeout", "description": "The multiplayer integration test is failing due to a timeout. The threshold should be increased"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_005", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="035",
        instruction=(
            "You are a Dev Ops Engineer. Handle the asset validation failure in build 'run_006'. "
            "File a bug with the title 'Asset validation error: texture size' for the bisect owner. "
            "Then, create a fix proposal for an 'asset_validation_issue' with the title 'Fix oversized texture in game assets' and description 'The hero_character_diffuse.png texture is larger than the maximum allowed size and needs to be resized'. "
            "Lastly, resolve the build."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_006"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_006"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_006"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-assets"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Asset validation error: texture size", "assignee_id": 'user_008'}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_006", "bisect_result_id": "bisect_006", "repo": "game-assets", "branch": "feature/new-assets", "fix_type": "asset_validation_issue", "title": "Fix oversized texture in game assets", "description": "The hero_character_diffuse.png texture is larger than the maximum allowed size and needs to be resized"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_006", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="036",
        instruction=(
            "You are a Dev Ops Engineer. Triage the localization failure in build 'run_008'. "
            "Create a bug titled 'German translation causing UI overflow' for the owner identified by the bisect. "
            "Then, draft a fix proposal for a 'localization_issue' titled 'Shorten German UI string to fix overflow' "
            "with the description 'The German translation for 'ui.main_menu.start_game' is too long and needs to be shortened to prevent UI overflow'. "
            "Finally, mark the build as resolved."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_008"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_008"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_007"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-localization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "German translation causing UI overflow", "assignee_id": 'user_008'}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_008", "bisect_result_id": "bisect_007", "repo": "game-localization", "branch": "feature/localization-update", "fix_type": "localization_issue", "title": "Shorten German UI string to fix overflow", "description": "The German translation for 'ui.main_menu.start_game' is too long and needs to be shortened to prevent UI overflow"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_008", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="037",
        instruction=(
            "You are a Dev Ops Engineer. Address the performance regression from build 'run_007'. "
            "Create a bug for the person identified by the bisect with the title 'Renderer performance has degraded'. "
            "Draft a fix proposal for a 'performance_regression' with the title 'Fix performance drop in texture loading' and a description of 'Recent changes to the renderer have caused a significant drop in frame rate. This needs to be optimized'. "
            "Finally, resolve the build run."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_007"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_007"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_004"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Renderer performance has degraded", "assignee_id": "user_001"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_007", "bisect_result_id": "bisect_004", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "performance_regression", "title": "Fix performance drop in texture loading", "description": "Recent changes to the renderer have caused a significant drop in frame rate. This needs to be optimized"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_007", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="038",
        instruction=(
            "You are a Dev Ops Engineer. An integration failure has occurred in build 'run_005'. "
            "A bug report titled 'Integration test failure in multiplayer connection' "
            "should be created and assigned to the owner from the bisect report. "
            "Next, a fix proposal should be created with the title 'Fix multiplayer connection timeout' "
            "and description 'Increase connection timeout threshold to fix integration test failure', "
            "and type 'integration_failure'. "
            "To conclude, you should change the triage status of the build run to 'resolved'."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_005"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_005"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_003"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Integration test failure in multiplayer connection", "assignee_id": "user_008"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_005", "bisect_result_id": "bisect_003", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "integration_failure", "title": "Fix multiplayer connection timeout", "description": "Increase connection timeout threshold to fix integration test failure"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_005", "triage_status": "resolved"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="046",
        instruction=(
            "You are a Dev Ops Engineer. Deployment 'deploy_004' failed. "
            "Find the last successful deployment on the same pipeline to determine the rollback version. "
            "Then, find the work item for the 'Implement multi-cloud application architecture' feature, which was part of the failed deployment. "
            "Add a comment to this work item explaining that the deployment failed and is being rolled back, mentioning the version you're rolling back to. "
            "After that, initiate the rollback. "
            "Finally, create a critical incident in the 'Multi-Platform Game Infrastructure' project titled 'Deployment Failure and Rollback of Multi-Cloud App' and assign it to the 'Game Server Operations Team' lead."
        ),
        actions=[
            Action(name="get_deployment_by_id", kwargs={"id": "deploy_004"}),
            Action(name="find_previous_successful_deployment", kwargs={"pipeline_id": "pipe_005", "before_timestamp": "2025-01-26T08:20:00Z"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement multi-cloud application architecture"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_006", "comment": "Deployment failed. Rolling back to version v1.0.4 from deployment deploy_005."}),
            Action(name="create_deployment", kwargs={"pipeline_id": "pipe_005", "environment_id": "env_011", "deployed_by": "user_004", "version": "v1.0.4", "status": "in_progress"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="get_team_by_name", kwargs={"name": "Game Server Operations Team"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_005"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "incident", "title": "Deployment Failure and Rollback of Multi-Cloud App", "assignee_id": "user_005", "priority": "critical"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="050",
        instruction=(
            "You are a Dev Ops Engineer. A build failure in 'run_001' is blocking deployments and needs a hotfix. "
            "Find the bisect result to identify the suspect files and responsible owner. "
            "Get the repository and project details for 'game-engine'. "
            "A new branch should be created from 'main' named 'hotfix/build-run-001'. "
            "A new high priority bug should be created titled 'Hotfix for Build run_001 Failure' and assigned to the owner. "
            "A comment 'Please commit the fix for this build failure' should be added to the bug. "
            "Also, the build triage run's status should be set to 'in_progress'."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_001"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_001"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_001"}),
            Action(name="get_repository_by_name", kwargs={"name": "game-engine"}),
            Action(name="get_project_id_for_repository_name", kwargs={"repository_name": "game-engine"}),
            Action(name="get_branch_by_name", kwargs={"repository_id": "repo_031", "branch_name": "main"}),
            Action(name="create_branch", kwargs={"repository_id": "repo_031", "branch_name": "hotfix/build-run-001", "source_branch_id": "branch_051"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Hotfix for Build run_001 Failure", "assignee_id": "user_001", "priority": "high"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Please commit the fix for this build failure"}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_001", "triage_status": "in_progress"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="067",
        instruction=(
            "You are a Triage Engineer. A network crash, 'crash_003', has been reported. "
            "Find the owner of the 'multiplayer.cpp' file and their team lead. "
            "Create a bug in the 'Game Security & Anti-Cheat Framework' project titled 'Crash on Network Timeout' for the team lead. "
            "Link this new bug as related to the 'Implement anti-cheat system integration' story. "
            "Add 'Stack Trace: NetworkManager.dll' as a comment to the bug. "
            "Finally, update the crash event's status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_003"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Crash on Network Timeout", "assignee_id": "user_003"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: NetworkManager.dll"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_003", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="068",
        instruction=(
            "You are a Triage Engineer. Crash report 'crash_006' for a Kubernetes issue needs to be triaged. "
            "Find the owner of 'multiplayer.cpp' and their team lead as the responsible party. "
            "Create a new bug in the 'Game Engine Core Migration' project titled 'K8s Memory Allocation Crash'. "
            "Assign the bug to the team lead. "
            "Link it to the 'Implement game engine rendering pipeline' story as a dependency. "
            "Add 'Issue Signature: Kubernetes resource allocation failed' as a comment to the bug. "
            "Finally, update the crash's status to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_006"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "K8s Memory Allocation Crash", "assignee_id": "user_003"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement game engine rendering pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_001", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Issue Signature: Kubernetes resource allocation failed"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_006", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="070",
        instruction=(
            "You are a Triage Engineer. A compilation crash, 'crash_005', has been logged. "
            "You should find the owner of 'renderer.cpp' and their team lead. "
            "A bug should be created for this in the 'Multi-Platform Game Infrastructure' project "
            "titled 'Renderer Compilation Failure' and assigned to the lead. "
            "The new created bug should be lineked to the 'Implement cross-platform game infrastructure' epic as a related issue. "
            "'Stack Trace: renderer.cpp' should be added as a comment to the created bug. "
            "Also, the crash's status should be set to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_005"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "Renderer Compilation Failure", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: renderer.cpp"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_005", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="071",
        instruction=(
            "You are a Triage Engineer. Crash 'crash_001' needs to be triaged. "
            "Find the owner of 'renderer.cpp' and their team lead. "
            "Create a new bug in the 'Game Security & Anti-Cheat Framework' project titled 'Access Violation Crash in Rendering' for the team lead. "
            "This bug should be linked to the 'Implement anti-cheat system integration' story as a dependency. "
            "Add 'Access violation in GameEngine.dll' as a comment to the new created bug. "
            "To conclude, the crash event's status should be updated to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_001"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Access Violation Crash in Rendering", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Access violation in GameEngine.dll"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_001", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="072",
        instruction=(
            "You are a Triage Engineer. A network timeout crash, 'crash_003', has been reported. "
            "Find the owner of 'multiplayer.cpp' and their team lead. "
            "Create a bug in the 'Game Engine Core Migration' project titled 'Network Instability Crash' and assign it to the team lead. "
            "Link this bug to the 'Implement game engine rendering pipeline' story as a blocker. "
            "Add 'Stack Trace: NetworkManager.dll' as a comment on the new bug. "
            "Finally, change the crash event's status to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_003"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Network Instability Crash", "assignee_id": "user_003"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement game engine rendering pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_001", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: NetworkManager.dll"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_003", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="073",
        instruction=(
            "You are a Triage Engineer. Crash report 'crash_006' for a Kubernetes issue needs attention. "
            "You should find the owner of 'multiplayer.cpp' and their team lead. "
            "A bug should be created in the 'Game Build Pipeline Modernization' project titled 'K8s Crash During Deployment' and assigned to the team lead. "
            "This bug should be linked as related to the 'Create automated game build pipeline' epic. "
            "You should add 'Kubernetes resource allocation failed: insufficient memory' as a comment to the bug. "
            "To finish, the crash event's status should be set to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_006"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "K8s Crash During Deployment", "assignee_id": "user_003"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Kubernetes resource allocation failed: insufficient memory"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_006", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="076",
        instruction=(
            "You are a Triage Engineer. We're seeing a network timeout issue in crash report 'crash_003'. "
            "Please identify the owner of the 'multiplayer.cpp' file and their team lead. "
            "Log a new bug for this in the 'Game Security & Anti-Cheat Framework' project with title 'Network Timeout During Gameplay', assigned to the lead. "
            "This seems to be a dependency for our anti-cheat integration, so please link it to that story with title 'Implement anti-cheat system integration'. "
            "Set 'Stack Trace: NetworkManager.dll' as a comment on the bug and update the crash status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_003"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Network Timeout During Gameplay", "assignee_id": "user_003"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: NetworkManager.dll"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_003", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="077",
        instruction=(
            "You are a Triage Engineer. The compilation crash 'crash_005' needs your attention. "
            "You should find who owns 'renderer.cpp' and who their team lead. "
            "A bug should be created in the 'Multi-Platform Game Infrastructure' project about this, titled 'Critical Renderer Compilation Failure', and assigned to the team lead. "
            "This is a major blocker for our cross-platform epic with title 'Implement cross-platform game infrastructure', so link it accordingly. "
            "Make sure to add 'Stack Trace: renderer.cpp' in a comment for the bug, and then mark the crash as 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_005"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "Critical Renderer Compilation Failure", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: renderer.cpp"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_005", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="078",
        instruction=(
            "You are a Triage Engineer. We have a Kubernetes-related crash in 'crash_006'. "
            "This is likely an infrastructure issue, so find out who owns 'multiplayer.cpp' to identify the responsible team and its lead. "
            "Log a bug in the 'Game Engine Core Migration' project called 'K8s Infrastructure Crash' and assign it to the lead. "
            "This seems related to the main rendering pipeline with title 'Implement game engine rendering pipeline', so link the two work items. "
            "Add 'Kubernetes resource allocation failed: insufficient memory' comment to the bug for context, and finally, update the crash status to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_006"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "K8s Infrastructure Crash", "assignee_id": "user_003"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement game engine rendering pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_001", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Kubernetes resource allocation failed: insufficient memory"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_006", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="079",
        instruction=(
            "You are a Triage Engineer. An asset validation crash 'crash_007' has occurred. "
            "Please determine the owner of the 'assets/models/environment/' directory and find their team lead. "
            "A bug should be createdin the 'Game Build Pipeline Modernization' project with the title 'Asset Validation Crash: Environment Model' for the team lead. "
            "This bug is a dependency for the main build pipeline epic with title 'Create automated game build pipeline', so link them. "
            "You should add 'Asset validation failed' as a comment to the bug report, and then update the crash event status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_007"}),
            Action(name="find_file_owner", kwargs={"file_path": "assets/models/environment/"}),
            Action(name="get_user_by_id", kwargs={"id": "user_007"}),
            Action(name="get_team_by_id", kwargs={"id": "team_002"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_002"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Asset Validation Crash: Environment Model", "assignee_id": "user_002"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Asset validation failed"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_007", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="080",
        instruction=(
            "You are a Triage Engineer. Another access violation, 'crash_001', has been reported. "
            "You should create a new bug for the lead of of 'renderer.cpp' file. "
            "The bug should be in the 'Game Security & Anti-Cheat Framework' project and titled 'Security Concern: Access Violation in Renderer'. "
            "This could block our anti-cheat work, so link it to that story with title 'Implement anti-cheat system integration'. "
            "Paste 'Access violation in GameEngine.dll' into a comment for the bug, and let's mark the crash as 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_001"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Security Concern: Access Violation in Renderer", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Access violation in GameEngine.dll"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_001", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="081",
        instruction=(
            "You are a Triage Engineer. We have a network timeout crash ('crash_003'). "
            "Figure out who owns 'multiplayer.cpp' and who their manager is. "
            "File a bug for the manager in the 'Game Build Pipeline Modernization' project named 'Network Instability in Builds'. "
            "Link this as a related issue to the main build pipeline epic with title 'Create automated game build pipeline'. "
            "For context, you should add 'Stack Trace: NetworkManager.dll' as a comment on the bug. "
            "Finally, update the crash status to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_003"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Network Instability in Builds", "assignee_id": "user_003"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: NetworkManager.dll"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_003", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="082",
        instruction=(
            "You are a Triage Engineer. A compilation crash, 'crash_005', has occurred. "
            "Find the owner of 'renderer.cpp' and their team lead. "
            "Create a new bug in the 'Game Security & Anti-Cheat Framework' project for the team lead, titled 'Build Failure: Renderer Compilation'. "
            "This bug is a dependency for the anti-cheat story with title 'Implement anti-cheat system integration', so please link them. "
            "Add 'Stack Trace: renderer.cpp' to a comment for the bug. "
            "To finish, update the crash's status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_005"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Build Failure: Renderer Compilation", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: renderer.cpp"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_005", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="083",
        instruction=(
            "You are a Triage Engineer. Triage the Kubernetes crash 'crash_006'. "
            "Identify the owner of 'multiplayer.cpp' and their team lead. "
            "Log a bug in the 'Game Build Pipeline Modernization' project for the team lead with the title 'Deployment Failure: K8s Memory'. "
            "Link this bug as a blocker to the 'Create automated game build pipeline' epic. "
            "Add 'Kubernetes resource allocation failed: insufficient memory' as a comment for the bug, and then update the crash status to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_006"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "Deployment Failure: K8s Memory", "assignee_id": "user_003"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Kubernetes resource allocation failed: insufficient memory"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_006", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="084",
        instruction=(
            "You are a Triage Engineer. An asset validation crash, 'crash_007', has occurred. "
            "You should find the owner of the 'assets/textures/character_models/' directory and their team lead. "
            "A bug should be created in the 'Multi-Platform Game Infrastructure' project titled 'Asset Crash: Invalid Texture' for the team lead. "
            "This bug is related to the cross-platform epic with title 'Implement cross-platform game infrastructure', so please link them with type 'related'. "
            "Add a comment to the new bug with 'Asset validation failed: Texture size'. "
            "Finally, update the crash event's status to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_007"}),
            Action(name="find_file_owner", kwargs={"file_path": "assets/textures/character_models/"}),
            Action(name="get_user_by_id", kwargs={"id": "user_002"}),
            Action(name="get_team_by_id", kwargs={"id": "team_002"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_002"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "Asset Crash: Invalid Texture", "assignee_id": "user_002"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Asset validation failed: Texture size"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_007", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="086",
        instruction=(
            "You are a Triage Engineer. A network timeout crash, 'crash_003', has occurred. "
            "Find the full path for 'multiplayer.cpp' to identify the owner and their team lead. "
            "File a new bug in the 'Multi-Platform Game Infrastructure' project titled 'Network Timeout During Gameplay' and assign it to the team lead. "
            "Link this bug as a dependency to the 'Implement cross-platform game infrastructure' epic. "
            "Add 'Stack Trace: NetworkManager.dll' as a comment to the new bug. "
            "To conclude, update the crash event's status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_003"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "Network Timeout During Gameplay", "assignee_id": "user_003"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: NetworkManager.dll"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_003", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="087",
        instruction=(
            "You are a Triage Engineer. Crash 'crash_006' indicates a Kubernetes issue. "
            "Find the owner of 'multiplayer.cpp' to identify the responsible team and their lead. "
            "Create a new bug in the 'Game Security & Anti-Cheat Framework' project titled 'Kubernetes Deployment Crash' and assign it to the team lead. "
            "This bug is blocking the 'Implement anti-cheat system integration' story, so link them. "
            "Add 'Kubernetes resource allocation failed: insufficient memory' to the new bug as a comment. "
            "Finally, change the crash event's status to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_006"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Kubernetes Deployment Crash", "assignee_id": "user_003"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Kubernetes resource allocation failed: insufficient memory"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_006", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="088",
        instruction=(
            "You are a Triage Engineer. An asset validation crash, 'crash_007', needs to be addressed. "
            "Find the owner of the asset folder 'assets/textures/character_models/' and their team lead. "
            "Create a new bug in the 'Game Engine Core Migration' project titled 'Asset Validation Failure: Texture Size' and assign it to the team lead. "
            "This is related to the main rendering pipeline, so link it to that story with title 'Implement game engine rendering pipeline'. "
            "Add 'Texture size 4096x4096 exceeds maximum 2048x2048' as a comment to the bug. "
            "Lastly, update the crash event status to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_007"}),
            Action(name="find_file_owner", kwargs={"file_path": "assets/textures/character_models/"}),
            Action(name="get_user_by_id", kwargs={"id": "user_002"}),
            Action(name="get_team_by_id", kwargs={"id": "team_002"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_002"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Asset Validation Failure: Texture Size", "assignee_id": "user_002"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement game engine rendering pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_001", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Texture size 4096x4096 exceeds maximum 2048x2048"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_007", "status": "triaged"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="090",
        instruction=(
            "You are a Triage Engineer. A new access violation crash, 'crash_001', has been logged. "
            "Find the owner of the 'renderer.cpp' file and their team lead. "
            "Create a bug in the 'Multi-Platform Game Infrastructure' project titled 'Access Violation on Character Load' and assign it to the team lead. "
            "This is a blocker for our cross-platform epic with title 'Implement cross-platform game infrastructure', so link them accordingly. "
            "Add 'Access violation in GameEngine.dll' as a comment for the new bug. "
            "To finish, update the crash event's status to 'investigating'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_001"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "Access Violation on Character Load", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "blocks"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Access violation in GameEngine.dll"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_001", "status": "investigating"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="092",
        instruction=(
            "You are a Triage Engineer. Crash report 'crash_006' for a Kubernetes issue needs attention. "
            "Find the owner of 'multiplayer.cpp' and their team lead. "
            "Create a bug in the 'Game Build Pipeline Modernization' project titled 'K8s Crash During Deployment' and assign it to the team lead. "
            "Link this bug as related to the 'Create automated game build pipeline' epic. "
            "You should add a comment with 'Kubernetes resource allocation failed' to the bug. "
            "To finish, update the crash event's status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_006"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Build Pipeline Modernization"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_002", "type": "bug", "title": "K8s Crash During Deployment", "assignee_id": "user_003"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Create automated game build pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_003", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Kubernetes resource allocation failed"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_006", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="093",
        instruction=(
            "You are a Triage Engineer. An asset validation crash, 'crash_007', has occurred. "
            "Find the owner of the 'assets/textures/character_models/' directory and their team lead. "
            "Create a bug in the 'Multi-Platform Game Infrastructure' project titled 'Asset Crash: Invalid Texture' for the team lead. "
            "This bug is related to the cross-platform epic with title 'Implement cross-platform game infrastructure', so please link them. "
            "Add a comment to the new bug with 'Texture size 4096x4096 exceeds maximum 2048x2048'. "
            "Finally, update the crash event's status to 'triaged'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_007"}),
            Action(name="find_file_owner", kwargs={"file_path": "assets/textures/character_models/"}),
            Action(name="get_user_by_id", kwargs={"id": "user_002"}),
            Action(name="get_team_by_id", kwargs={"id": "team_002"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_002"}),
            Action(name="get_project_by_name", kwargs={"name": "Multi-Platform Game Infrastructure"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_003", "type": "bug", "title": "Asset Crash: Invalid Texture", "assignee_id": "user_002"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement cross-platform game infrastructure"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_004", "child_id": "work_028", "link_type": "related"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Texture size 4096x4096 exceeds maximum 2048x2048"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_007", "status": "triaged"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="094",
        instruction=(
            "You are a Triage Engineer. A compilation crash, 'crash_005', has been logged. "
            "Find the owner of 'renderer.cpp' and their team lead. "
            "Create a bug for this in the 'Game Security & Anti-Cheat Framework' project titled 'Renderer Compilation Failure' and assign it to the lead. "
            "This is a dependency for the anti-cheat story with title 'Implement anti-cheat system integration', so please link them. "
            "Add 'Stack Trace: renderer.cpp' as a comment to the new created bug. "
            "Finally, update the crash's status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_005"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Renderer Compilation Failure", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: renderer.cpp"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_005", "status": "assigned"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="096",
        instruction=(
            "You are a Triage Engineer. A network timeout crash, 'crash_003', needs to be handled. "
            "Find the owner of 'multiplayer.cpp' and their team lead. "
            "Create a new high-priority bug in the 'Game Engine Core Migration' project titled 'Network Timeout Crash'. "
            "Assign this bug to the team lead. "
            "This issue is a dependency for the main rendering pipeline with title 'Implement game engine rendering pipeline', so link them. "
            "Add 'Stack Trace: NetworkManager.dll' as a comment on the new bug. "
            "Afterward, update the crash event's status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_003"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "multiplayer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/network/multiplayer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_008"}),
            Action(name="get_team_by_id", kwargs={"id": "team_003"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_003"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Network Timeout Crash", "assignee_id": "user_003", "priority": "high"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement game engine rendering pipeline"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_001", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "Stack Trace: NetworkManager.dll"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_003", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="099",
        instruction=(
            "You are a Triage Engineer. The compilation crash 'crash_005' has occurred. "
            "A bug should be created in the 'Game Security & Anti-Cheat Framework' project titled 'Compilation Failure Blocking Security Scans' for the team lead of 'renderer.cpp' file. "
            "This bug is a dependency for the main anti-cheat story with title 'Implement anti-cheat system integration'; they should be linked. "
            "The crash fingerprint should be added as a comment for their reference. "
            "Also, you should set the crash event's status to 'assigned'."
        ),
        actions=[
            Action(name="get_crash_event_by_id", kwargs={"id": "crash_005"}),
            Action(name="find_full_path_for_file_name", kwargs={"file_name": "renderer.cpp"}),
            Action(name="find_file_owner", kwargs={"file_path": "src/game/engine/renderer.cpp"}),
            Action(name="get_user_by_id", kwargs={"id": "user_001"}),
            Action(name="get_team_by_id", kwargs={"id": "team_001"}),
            Action(name="get_team_lead", kwargs={"team_id": "team_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Security & Anti-Cheat Framework"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_004", "type": "bug", "title": "Compilation Failure Blocking Security Scans", "assignee_id": "user_001"}),
            Action(name="find_work_item_by_title", kwargs={"title": "Implement anti-cheat system integration"}),
            Action(name="link_work_items", kwargs={"parent_id": "work_005", "child_id": "work_028", "link_type": "dependency"}),
            Action(name="add_comment_to_work_item", kwargs={"id": "work_028", "comment": "build_compilation_missing_declaration_xyz"}),
            Action(name="update_crash_event_status", kwargs={"id": "crash_005", "status": "assigned"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="100",
        instruction=(
            "You are a Dev Ops Engineer. A critical build 'run_001' has failed, blocking development. "
            "You should find the bisect result to identify the cause and the responsible owner. "
            "Create a new high priority bug in the 'Game Engine Core Migration' project titled 'Critical Build Failure: Renderer Compilation' and assign it to the owner. "
            "Also, a bug_assignment Slack notification should be sent with title 'New Critical Bug Assigned' "
            "and message 'You have been assigned a critical build failure' "
            "to the owner to alert them of the new critical bug. "
            "Also, a fix proposal should be created for the 'compilation_issue' with the title 'Fix Missing TextureManager Declaration' and description 'A function declaration is missing.', and the build marked as 'in_progress'."
        ),
        actions=[
            Action(name="get_build_run_by_id", kwargs={"id": "run_001"}),
            Action(name="get_bisect_result_for_build_run", kwargs={"build_run_id": "run_001"}),
            Action(name="get_owner_for_bisect", kwargs={"bisect_id": "bisect_001"}),
            Action(name="get_project_by_name", kwargs={"name": "Game Engine Core Migration"}),
            Action(name="create_work_item", kwargs={"project_id": "proj_001", "type": "bug", "title": "Critical Build Failure: Renderer Compilation", "assignee_id": "user_001", "priority": "high"}),
            Action(name="send_notification", kwargs={"project_id": "proj_001", "recipient_id": "user_001", "title": "New Critical Bug Assigned", "message": "You have been assigned a critical build failure", "channel": "slack", "notification_type": "bug_assignment"}),
            Action(name="create_fix_proposal", kwargs={"build_run_id": "run_001", "bisect_result_id": "bisect_001", "repo": "game-engine", "branch": "feature/new-renderer", "fix_type": "compilation_issue", "title": "Fix Missing TextureManager Declaration", "description": "A function declaration is missing."}),
            Action(name="update_build_run_triage_status", kwargs={"id": "run_001", "triage_status": "in_progress"}),
        ],
        outputs=[]
    ),


]
