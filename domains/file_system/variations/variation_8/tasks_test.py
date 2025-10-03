from tau_bench.types import Action, Task

TASKS = [
   Task(
    annotator="0",
    user_id="USER_001",
    instruction=(
        "Ensure NERC-CIP compliance for Task ID SCAN_016 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_002",
    instruction=(
        "Process the first incomplete task from the `file_check_db` to ensure FedRAMP compliance for Task ID SCAN_017. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and notifying the '#File Check' channel of the successful completion and cleanup."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
                "parallel_processes": 6,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(
            name="AddHeaderToFileLog",
            kwargs={"task_id": "fc_task_001", "log_name": "file_check_log.json"},
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
                "session_to_kill": "none",
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="SendSlackNotification",
            kwargs={
                "channel": "#File Check",
                "message": "Task fc_task_001 (Weekly Log Analysis) is complete. The log of discovered files has been successfully generated and verified.",
            },
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
                "notes": "Completed scan of /var/log/applications on server-prod-01.company.com.",
            },
        ),
    ],
    outputs=[
        '"status": "success"',
        '"filtered_count": 0',
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
    Task(
    annotator="0",
    user_id="USER_003",
    instruction=(
        "Perform audited archival process meeting incident response requirements for Task ID ARCH_002. Archive '/app/logs/server.log' and '/app/logs/database.log' as 'app_logs_backup.tar.gz' to 'storage.server.com:/backup/logs'. The incident response policy mandates pre-flight validation of source files. When files are missing, the audit protocol requires documenting the workflow termination in central task log and notifying the archive status channel about the task failure with source file unavailability details. Ensure the archival outcome is properly recorded for audit compliance."
    ),
    actions=[
        Action(
            name="ParseArchiveInstructions",
            kwargs={
                "archive_name": "app_logs_backup.tar.gz",
                "destination_directory": "/backup/logs",
                "remote_address": "storage.server.com",
                "files_to_archive": [
                    "/app/logs/server.log",
                    "/app/logs/database.log",
                ],
            },
        ),
        Action(
            name="ValidateFilesExist",
            kwargs={
                "file_paths": ["/app/logs/server.log", "/app/logs/database.log"]
            },
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "ARCH_002",
                "task_name": "File Archival",
                "result": "Failure",
                "notes": "Workflow terminated due to missing source files.",
            },
        ),
        Action(
            name="SendSlackNotification",
            kwargs={
                "channel": "#archive-status",
                "message": "Task ARCH_002 failed: Source files not found.",
            },
        ),
    ],
    outputs=[
        '"status": "failed"',
        '"missing_files": ["/app/logs/server.log", "/app/logs/database.log"]',
    ],
),
    Task(
    annotator="0",
    user_id="USER_004",
    instruction=(
        "Update central task database by reorganizing files from '/var/log' to '/archived/logs' for Task ID F_ADJ_004. Sort '.txt' files to 'text' and '.old' to 'legacy'. To pass the audit, ensure the database is updated with a final log stating 'Reorganized 3 files from /var/log to /archived/logs after successful pre-flight checks.' and a notification is sent to '#system-alerts' with the message 'Task F_ADJ_004 (File Tree Adjustment) complete. All files from /var/log have been moved to /archived/logs and sorted.'."
    ),
    actions=[
        Action(
            name="ParseDirectoryRestructureInstructions",
            kwargs={
                "target_directory": "/var/log",
                "destination_directory": "/archived/logs",
                "sort_rules": {"txt": "text", "old": "legacy"},
            },
        ),
        Action(
            name="CreateFileListForMove",
            kwargs={"target_directory": "/var/log"},
        ),
        Action(name="PopulateChecksumsInFileList", kwargs={}),
        Action(
            name="ComputeAndResolveDestinationPaths",
            kwargs={
                "destination_directory": "/archived/logs",
                "sort_rules": {"txt": "text", "old": "legacy"},
            },
        ),
        Action(name="CopyAndVerifyFiles", kwargs={}),
        Action(
            name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "F_ADJ_004",
                "task_name": "File Tree Adjustment",
                "result": "Success",
                "notes": "Reorganized 3 files from /var/log to /archived/logs after successful pre-flight checks.",
            },
        ),
        Action(
            name="SendSlackNotification",
            kwargs={
                "channel": "#system-alerts",
                "message": "Task F_ADJ_004 (File Tree Adjustment) complete. All files from /var/log have been moved to /archived/logs and sorted.",
            },
        ),
    ],
    outputs=[
        '"status": "success"',
        '"verified_and_copied": 3',
        '"cleaned_files_count": 3',
    ],
),
    Task(
        annotator="0",
        user_id="USER_005",
        instruction=(
            "Conduct audited reorganization of '/var/log' directory for Task ID F_ADJ_005 following company audit policy requiring complete and precise audit trail. Sort directory contents into '/backup/logs' with specific rules for 'kern.log' and 'dpkg.log'. For audit approval, the trail must contain two database logs: initial registration with note 'Plan registration for F_ADJ_005: Reorganize /var/log for audit.' and final completion log with exact note 'Organized audit-relevant log files from /var/log.'. Policy additionally requires final notification to '#compliance-reports' channel with precise message: 'Task F_ADJ_005 (File Tree Adjustment) complete. Log files in /var/log have been successfully organized for audit.' Execute reorganization while ensuring audit trail meets these strict content requirements."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/backup/logs",
                    "sort_rules": {
                        "kern.log": "kernel_events",
                        "dpkg.log": "package_events",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_005",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Plan registration for F_ADJ_005: Reorganize /var/log for audit.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/backup/logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/backup/logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/backup/logs",
                    "sort_rules": {
                        "kern.log": "kernel_events",
                        "dpkg.log": "package_events",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_005",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Organized audit-relevant log files from /var/log.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#compliance-reports",
                    "message": "Task F_ADJ_005 (File Tree Adjustment) complete. Log files in /var/log have been successfully organized for audit.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
        ],
    ),
    Task(
    annotator="0",
    user_id="USER_006",
    instruction=(
        "Attempt audited archival of user and transaction data from '/data/exports/' for Task ID ARCH_003. Send the archive, named 'data_exports_backup.tar.gz', to 'backup.server.net:/archives/exports'. When source files ('users.csv', 'transactions.csv') are missing, log the failure with ERROR severity and notify the '#backup-status' channel, mentioning '@oncall-team'."
    ),
    actions=[
        Action(
            name="ParseArchiveInstructions",
            kwargs={
                "archive_name": "data_exports_backup.tar.gz",
                "destination_directory": "/archives/exports",
                "remote_address": "backup.server.net",
                "files_to_archive": [
                    "/data/exports/users.csv",
                    "/data/exports/transactions.csv",
                ],
            },
        ),
        Action(
            name="ValidateFilesExist",
            kwargs={
                "file_paths": [
                    "/data/exports/users.csv",
                    "/data/exports/transactions.csv",
                ],
            },
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "ARCH_003",
                "notes": "Workflow terminated due to missing source files.",
                "severity": "ERROR",
            },
        ),
        Action(
            name="SendSlackNotification",
            kwargs={
                "channel": "#backup-status",
                "message": "Task ARCH_003 failed: Source files not found.",
                "mention_users": ["@oncall-team"],
            },
        ),
    ],
    outputs=[
        '"status": "failed"',
        '"missing_files": ["/data/exports/users.csv", "/data/exports/transactions.csv"]',
    ],
),
    Task(
        annotator="0",
        user_id="USER_007",
        instruction=(
            "Perform file reorganization of '/var/log' for Task ID F_ADJ_006 to pass strict compliance audit requirements. Target location is '/storage/logs' with sorting rules for '.conf' (to 'config') and '.pid' (to 'process'). Automated compliance check requires specific, machine-readable audit trail entries. For approval, audit system must find initial database log with note 'Registering plan: Move /var/log to /storage/logs.' and final completion log with note 'Reorganized 3 files from /var/log to /storage/logs after successful pre-flight checks.'. User notification sent to '#infra-alerts' must exactly match 'Task F_ADJ_006 (File Tree Adjustment) complete. All files from /var/log have been moved to /storage/logs and sorted.' for compliance system parsing. Execute reorganization while ensuring these specific audit requirements are met."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/storage/logs",
                    "sort_rules": {"conf": "config", "pid": "process"},
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_006",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /storage/logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/storage/logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/storage/logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/storage/logs",
                    "sort_rules": {"conf": "config", "pid": "process"},
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_006",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /storage/logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#infra-alerts",
                    "message": "Task F_ADJ_006 (File Tree Adjustment) complete. All files from /var/log have been moved to /storage/logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_008",
        instruction=(
            "Conduct audited reorganization of '/var/log' directory for Task ID F_ADJ_007 following company audit policy requiring complete and precise audit trail. Sort directory contents into '/secure/audit_logs' with files named 'messages' going to 'system_messages' subdirectory and files named 'secure' going to 'security_logs' subdirectory. For audit approval, trail must contain two database logs: initial registration with note 'Plan registration for F_ADJ_007: Reorganize /var/log for audit.' and final completion log with exact note 'Organized audit-relevant message files from /var/log.'. Policy additionally requires final notification to '#audit-tracking' channel with precise message: 'Task F_ADJ_007 (File Tree Adjustment) complete. Message logs in /var/log have been successfully organized for audit.' Execute reorganization while ensuring audit trail meets these strict content requirements."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/secure/audit_logs",
                    "sort_rules": {
                        "messages": "system_messages",
                        "secure": "security_logs",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_007",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Plan registration for F_ADJ_007: Reorganize /var/log for audit.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/secure/audit_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/secure/audit_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/secure/audit_logs",
                    "sort_rules": {
                        "messages": "system_messages",
                        "secure": "security_logs",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_007",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Organized audit-relevant message files from /var/log.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#audit-tracking",
                    "message": "Task F_ADJ_007 (File Tree Adjustment) complete. Message logs in /var/log have been successfully organized for audit.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_009",
        instruction=(
            "Perform archival process for application configuration files meeting incident response audit requirements for Task ID ARCH_004. Archive '/app/data/config.yaml' and '/app/data/settings.json' into an archive named 'app_config_backup.tar.gz' for delivery to 'archive.corp.com:/backups/configs'.\n\nThis task is governed by the following company policies:\n\n1.  **Configuration Archival Policy**: For long-term storage, all configuration archives must use maximum Gzip compression (level 9), be encrypted with the current 'CONFIG_KEY_2024', and be retained for 730 days.\n\n2.  **Pre-flight Validation Policy**: Before archival, you must validate that the source files exist and that you have the necessary read permissions.\n\n3.  **Failure Notification Policy**: If the workflow fails due to missing source files, you must log the failure in the database with a 'WARNING' severity. A medium-priority alert must also be sent to the '#config-archives' channel with the message 'Task ARCH_004 failed: Source files not found.'."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "app_config_backup.tar.gz",
                    "destination_directory": "/backups/configs",
                    "remote_address": "archive.corp.com",
                    "files_to_archive": [
                        "/app/data/config.yaml",
                        "/app/data/settings.json",
                    ],
                    "compression_level": 9,
                    "encryption_key_id": "CONFIG_KEY_2024",
                    "retention_days": 730,
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": ["/app/data/config.yaml", "/app/data/settings.json"],
                    "check_permissions": "enabled",
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_004",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "WARNING",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#config-archives",
                    "message": "Task ARCH_004 failed: Source files not found.",
                    "priority": "medium",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/app/data/config.yaml", "/app/data/settings.json"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_010",
        instruction=(
            "Perform file reorganization of '/var/log' for Task ID F_ADJ_008 to pass strict compliance audit requirements. Target location is '/retained/logs' with sorting rules for '.err' (to 'errors') and '.warn' (to 'warnings'). Automated compliance check requires specific, machine-readable audit trail entries. For approval, audit system must find initial database log with note 'Registering plan: Move /var/log to /retained/logs.' and final completion log with note 'Reorganized 3 files from /var/log to /retained/logs after successful pre-flight checks.'. User notification sent to '#log-management' must exactly match 'Task F_ADJ_008 (File Tree Adjustment) complete. All files from /var/log have been moved to /retained/logs and sorted.' for compliance system parsing. Execute reorganization while ensuring these specific audit requirements are met."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/retained/logs",
                    "sort_rules": {"err": "errors", "warn": "warnings"},
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_008",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /retained/logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/retained/logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/retained/logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/retained/logs",
                    "sort_rules": {"err": "errors", "warn": "warnings"},
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_008",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /retained/logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#log-management",
                    "message": "Task F_ADJ_008 (File Tree Adjustment) complete. All files from /var/log have been moved to /retained/logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_011",
        instruction=(
            "Execute GDPR-compliant reorganization of '/var/log' for legal department's quarterly review through Task ID F_ADJ_009. Destination is '/compliance/gdpr_logs' with '.access' files categorized as 'user_activity' and '.fail' files as 'system_faults'. Legal compliance framework requires database documentation showing 'Registering plan: Move /var/log to /compliance/gdpr_logs.' initially and 'Reorganized 3 files from /var/log to /compliance/gdpr_logs after successful pre-flight checks.' upon completion. Automated scanner also requires '#legal-compliance' notification stating 'Task F_ADJ_009 (File Tree Adjustment) complete. All files from /var/log have been moved to /compliance/gdpr_logs and sorted.' Meet these GDPR documentation requirements."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/compliance/gdpr_logs",
                    "sort_rules": {"access": "user_activity", "fail": "system_faults"},
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_009",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /compliance/gdpr_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/compliance/gdpr_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/compliance/gdpr_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/compliance/gdpr_logs",
                    "sort_rules": {"access": "user_activity", "fail": "system_faults"},
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_009",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /compliance/gdpr_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#legal-compliance",
                    "message": "Task F_ADJ_009 (File Tree Adjustment) complete. All files from /var/log have been moved to /compliance/gdpr_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_012",
        instruction=(
            "Execute emergency backup archival meeting disaster recovery audit standards for Task ID ARCH_005. Archive '/db/production/customers.sql' and '/db/production/orders.sql' as 'emergency_db_snapshot.tar.gz' to 'dr-site.internal:/disaster_recovery/databases'. Apply DR configuration using compression level 9 with DR_MASTER_KEY encryption, 90-day retention in hot tier archive. Validation requires 1000-byte minimum size. When workflows fail due to missing source files, update database with 'Workflow terminated due to missing source files.' using CRITICAL severity in RFC3339 timestamp format, and notify '#dr-operations' with 'Task ARCH_005 failed: Source files not found.' at urgent priority. The DR monitoring system queries database for these entries to trigger failover procedures."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "emergency_db_snapshot.tar.gz",
                    "destination_directory": "/disaster_recovery/databases",
                    "remote_address": "dr-site.internal",
                    "files_to_archive": [
                        "/db/production/customers.sql",
                        "/db/production/orders.sql",
                    ],
                    "compression_level": 9,
                    "encryption_key_id": "DR_MASTER_KEY",
                    "retention_days": 90,
                    "archive_tier": "hot",
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/db/production/customers.sql",
                        "/db/production/orders.sql",
                    ],
                    "minimum_size_bytes": 1000,
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_005",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "CRITICAL",
                    "timestamp_format": "RFC3339",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#dr-operations",
                    "message": "Task ARCH_005 failed: Source files not found.",
                    "priority": "urgent",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/db/production/customers.sql", "/db/production/orders.sql"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_013",
        instruction=(
            "Perform SOC2-compliant reorganization of '/var/log' for security team's annual audit through Task ID F_ADJ_010. Auditor requires relocation to '/audit/soc2_logs' with classification where '.audit' files route to 'access_control' and '.cron' files to 'scheduled_tasks'. SOC2 compliance system requires specific database entries for validation: task database must contain initial log with 'Registering plan: Move /var/log to /audit/soc2_logs.' and final entry with 'Reorganized 3 files from /var/log to /audit/soc2_logs after successful pre-flight checks.' Additionally, '#soc2-compliance' must receive: 'Task F_ADJ_010 (File Tree Adjustment) complete. All files from /var/log have been moved to /audit/soc2_logs and sorted.' Complete this reorganization while ensuring audit trail meets these certification requirements."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/audit/soc2_logs",
                    "sort_rules": {
                        "audit": "access_control",
                        "cron": "scheduled_tasks",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_010",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /audit/soc2_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/audit/soc2_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/audit/soc2_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/audit/soc2_logs",
                    "sort_rules": {
                        "audit": "access_control",
                        "cron": "scheduled_tasks",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_010",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /audit/soc2_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#soc2-compliance",
                    "message": "Task F_ADJ_010 (File Tree Adjustment) complete. All files from /var/log have been moved to /audit/soc2_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_014",
        instruction=(
            "Perform file reorganization of '/var/log' to meet PCI-DSS compliance requirements for Task ID F_ADJ_011. Target location is '/pci/secure_logs' with sorting rules for '.payment' (to 'transactions') and '.card' (to 'sensitive'). Compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#pci-compliance' channel that task is complete. Execute reorganization ensuring these PCI-DSS audit standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/pci/secure_logs",
                    "sort_rules": {"payment": "transactions", "card": "sensitive"},
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_011",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /pci/secure_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/pci/secure_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/pci/secure_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/pci/secure_logs",
                    "sort_rules": {"payment": "transactions", "card": "sensitive"},
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_011",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /pci/secure_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#pci-compliance",
                    "message": "Task F_ADJ_011 (File Tree Adjustment) complete. All files from /var/log have been moved to /pci/secure_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_015",
        instruction=(
            "Perform archival process meeting financial audit requirements for Task ID ARCH_006. Archive '/finance/reports/quarterly.xlsx' and '/finance/reports/annual.pdf' into an archive named 'financial_reports_backup.tar.gz' for delivery to 'audit-storage.finance:/fiscal/archives'.\n\nThis task is governed by the following compliance policies:\n\n1.  **Financial Records Archival Policy**: For long-term compliance, all financial records must be archived with balanced compression (level 6), encrypted with the 'FINANCE_AUDIT_KEY', and retained for 2555 days (7 years).\n\n2.  **Data Integrity Clause**: Validate that the financial reports are not empty, with a minimum size of 1024 bytes required for a valid report.\n\n3.  **Standard Notification Protocol**: If the workflow fails due to missing source files, log this as an informational event ('INFO' severity) in the database. A normal-priority alert must also be sent to the '#finance-audit' channel with the message 'Task ARCH_006 failed: Source files not found.'."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "financial_reports_backup.tar.gz",
                    "destination_directory": "/fiscal/archives",
                    "remote_address": "audit-storage.finance",
                    "files_to_archive": [
                        "/finance/reports/quarterly.xlsx",
                        "/finance/reports/annual.pdf",
                    ],
                    "compression_level": 6,
                    "encryption_key_id": "FINANCE_AUDIT_KEY",
                    "retention_days": 2555,
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/finance/reports/quarterly.xlsx",
                        "/finance/reports/annual.pdf",
                    ],
                    "minimum_size_bytes": 1024,
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_006",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "INFO",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#finance-audit",
                    "message": "Task ARCH_006 failed: Source files not found.",
                    "priority": "normal",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/finance/reports/quarterly.xlsx", "/finance/reports/annual.pdf"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_016",
        instruction=(
            "Perform file reorganization of '/var/log' to meet HIPAA compliance requirements for Task ID F_ADJ_012. Target location is '/hipaa/protected_logs' with 'patient.log' files routed to 'phi_data' and 'admin.log' files to 'administrative'. HIPAA compliance validation system requires central task database to contain evidence showing 'Plan registration for F_ADJ_012: Reorganize /var/log for audit.' initially and 'Organized audit-relevant health records from /var/log.' upon completion, with '#hipaa-compliance' notification 'Task F_ADJ_012 (File Tree Adjustment) complete. Health information logs in /var/log have been successfully organized for audit.' Execute reorganization ensuring these HIPAA standards are satisfied."
        ),
        actions=[
            # Actions remain unchanged
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/hipaa/protected_logs",
                    "sort_rules": {
                        "patient.log": "phi_data",
                        "admin.log": "administrative",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_012",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Plan registration for F_ADJ_012: Reorganize /var/log for audit.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/hipaa/protected_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/hipaa/protected_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/hipaa/protected_logs",
                    "sort_rules": {
                        "patient.log": "phi_data",
                        "admin.log": "administrative",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_012",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Organized audit-relevant health records from /var/log.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#hipaa-compliance",
                    "message": "Task F_ADJ_012 (File Tree Adjustment) complete. Health information logs in /var/log have been successfully organized for audit.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_017",
        instruction=(
            "Perform archival process meeting ISO27001 security audit requirements for Task ID ARCH_007. Archive '/security/incidents/breach.log' and '/security/incidents/vulnerability.csv' into an archive named 'security_incidents_backup.tar.gz' for delivery to 'iso-compliant.storage:/security/archives'.\n\nThis task is governed by the ISO27001 Compliance Framework, which mandates the following:\n\n1.  **Secure Archival Standard**: Security incident data must be archived with strong compression (level 7), encrypted with the 'ISO_SECURITY_2024' key, and retained in the 'secure' storage tier for 1095 days (3 years).\n\n2.  **Data Integrity Check**: Validate that incident files contain data, with a minimum size of 512 bytes required.\n\n3.  **Incident Reporting Protocol**: If the workflow fails due to missing source files, you must log the failure with 'ERROR' severity and an ISO8601 timestamp in the database. A high-priority alert must also be sent to the '#iso27001-alerts' channel with the message 'Task ARCH_007 failed: Source files not found.'."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "security_incidents_backup.tar.gz",
                    "destination_directory": "/security/archives",
                    "remote_address": "iso-compliant.storage",
                    "files_to_archive": [
                        "/security/incidents/breach.log",
                        "/security/incidents/vulnerability.csv",
                    ],
                    "compression_level": 7,
                    "encryption_key_id": "ISO_SECURITY_2024",
                    "retention_days": 1095,
                    "archive_tier": "secure",
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/security/incidents/breach.log",
                        "/security/incidents/vulnerability.csv",
                    ],
                    "minimum_size_bytes": 512,
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_007",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "ERROR",
                    "timestamp_format": "ISO8601",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#iso27001-alerts",
                    "message": "Task ARCH_007 failed: Source files not found.",
                    "priority": "high",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/security/incidents/breach.log", "/security/incidents/vulnerability.csv"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_018",
        instruction=(
            "Reorganize '/var/log' files to meet FERPA compliance requirements for Task ID F_ADJ_013. Target location is '/education/secure_logs' with sorting rules for '.student' (to 'records') and '.grade' (to 'academic'). FERPA compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#ferpa-compliance' channel that the task is complete. Execute reorganization ensuring these FERPA audit standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/education/secure_logs",
                    "sort_rules": {"student": "records", "grade": "academic"},
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_013",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /education/secure_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/education/secure_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/education/secure_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/education/secure_logs",
                    "sort_rules": {"student": "records", "grade": "academic"},
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_013",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /education/secure_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#ferpa-compliance",
                    "message": "Task F_ADJ_013 (File Tree Adjustment) complete. All files from /var/log have been moved to /education/secure_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_019",
        instruction=(
            "Perform archival process meeting CCPA compliance audit requirements for Task ID ARCH_008. Archive '/privacy/requests/deletion.json' and '/privacy/requests/access.json' into an archive named 'privacy_requests_backup.tar.gz' for delivery to 'ccpa-archive.legal:/compliance/privacy'.\n\nThis task is governed by the following CCPA-specific data handling policies:\n\n1.  **Data Portability Policy**: To ensure data is easily transferable, archives must use standard Gzip compression (level 5) and be encrypted with the 'CCPA_COMPLIANCE_KEY'. Data must be retained for 365 days.\n\n2.  **Data Integrity Check**: Validate that the source files exist and that you have the necessary read permissions before processing.\n\n3.  **Failure Notification Protocol**: If the workflow fails due to missing source files, you must log the failure in the database with 'ERROR' severity. A high-priority alert must also be sent to the '#ccpa-compliance' channel with the message 'Task ARCH_008 failed: Source files not found.'."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "privacy_requests_backup.tar.gz",
                    "destination_directory": "/compliance/privacy",
                    "remote_address": "ccpa-archive.legal",
                    "files_to_archive": [
                        "/privacy/requests/deletion.json",
                        "/privacy/requests/access.json",
                    ],
                    "compression_level": 5,
                    "encryption_key_id": "CCPA_COMPLIANCE_KEY",
                    "retention_days": 365,
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/privacy/requests/deletion.json",
                        "/privacy/requests/access.json",
                    ],
                    "check_permissions": "enabled",
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_008",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "ERROR",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#ccpa-compliance",
                    "message": "Task ARCH_008 failed: Source files not found.",
                    "priority": "high",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/privacy/requests/deletion.json", "/privacy/requests/access.json"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_020",
        instruction=(
            "Conduct audited reorganization of '/var/log' directory for Task ID F_ADJ_014 following company NIST compliance policy requiring complete and precise audit trail in central database. Sort directory contents into '/nist/framework_logs' with files named 'incident' going to 'respond_phase' and files named 'monitor' going to 'detect_phase'. For audit approval, database trail must contain two entries: initial registration with note 'Plan registration for F_ADJ_014: Reorganize /var/log for audit.' and final completion log with exact note 'Organized audit-relevant security framework files from /var/log.'. Policy additionally requires final notification to '#nist-framework' channel with precise message: 'Task F_ADJ_014 (File Tree Adjustment) complete. Security framework logs in /var/log have been successfully organized for audit.' Execute reorganization while ensuring database audit trail meets these strict content requirements."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/nist/framework_logs",
                    "sort_rules": {
                        "incident": "respond_phase",
                        "monitor": "detect_phase",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_014",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Plan registration for F_ADJ_014: Reorganize /var/log for audit.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/nist/framework_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/nist/framework_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/nist/framework_logs",
                    "sort_rules": {
                        "incident": "respond_phase",
                        "monitor": "detect_phase",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_014",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Organized audit-relevant security framework files from /var/log.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#nist-framework",
                    "message": "Task F_ADJ_014 (File Tree Adjustment) complete. Security framework logs in /var/log have been successfully organized for audit.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_021",
        instruction=(
            "Perform archival process meeting GLBA compliance audit requirements for Task ID ARCH_009. Archive '/financial/customer/accounts.db' and '/financial/customer/transactions.log' into an archive named 'glba_financial_backup.tar.gz' for delivery to 'glba-secure.finance:/protected/archives'.\n\nThis task is governed by the GLBA Safeguards Rule, which mandates the following:\n\n1.  **Secure Financial Archival**: All customer financial information must be archived with strong Gzip compression (level 7), encrypted using the 'GLBA_PROTECTION_KEY', and retained for 2555 days (7 years).\n\n2.  **Pre-Archive Validation**: Confirm that the source files exist and are accessible before initiating the backup.\n\n3.  **Compliance Failure Reporting**: If the workflow fails due to missing source files, you must log the failure in the database with 'CRITICAL' severity. An urgent-priority alert must also be sent to the '#glba-protection' channel with the message 'Task ARCH_009 failed: Source files not found.'."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "glba_financial_backup.tar.gz",
                    "destination_directory": "/protected/archives",
                    "remote_address": "glba-secure.finance",
                    "files_to_archive": [
                        "/financial/customer/accounts.db",
                        "/financial/customer/transactions.log",
                    ],
                    "compression_level": 7,
                    "encryption_key_id": "GLBA_PROTECTION_KEY",
                    "retention_days": 2555,
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/financial/customer/accounts.db",
                        "/financial/customer/transactions.log",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_009",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "CRITICAL",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#glba-protection",
                    "message": "Task ARCH_009 failed: Source files not found.",
                    "priority": "urgent",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/financial/customer/accounts.db", "/financial/customer/transactions.log"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_022",
        instruction=(
            "Reorganize '/var/log' files to meet CIS compliance requirements for Task ID F_ADJ_015. Target location is '/cis/benchmark_logs' with sorting rules for '.baseline' (to 'controls') and '.scan' (to 'assessments'). CIS compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#cis-benchmarks' channel that the task is complete. Execute reorganization ensuring these CIS security standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/cis/benchmark_logs",
                    "sort_rules": {"baseline": "controls", "scan": "assessments"},
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_015",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /cis/benchmark_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/cis/benchmark_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/cis/benchmark_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/cis/benchmark_logs",
                    "sort_rules": {"baseline": "controls", "scan": "assessments"},
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_015",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /cis/benchmark_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#cis-benchmarks",
                    "message": "Task F_ADJ_015 (File Tree Adjustment) complete. All files from /var/log have been moved to /cis/benchmark_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_023",
        instruction=(
            "Perform archival process meeting COBIT governance audit requirements for Task ID ARCH_010. Archive '/governance/policies/it_policy.doc' and '/governance/policies/risk_matrix.xls' as 'governance_docs_backup.tar.gz' to 'cobit-archive.governance:/compliance/policies'. The COBIT configuration uses compression level 6 with COBIT_GOVERNANCE_KEY encryption and 0-day retention. Failed workflows due to missing source files must update the database with 'Workflow terminated due to missing source files.' using WARNING severity, and notify '#cobit-governance' with 'Task ARCH_010 failed: Source files not found.' at normal priority. Ensure governance compliance requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "governance_docs_backup.tar.gz",
                    "destination_directory": "/compliance/policies",
                    "remote_address": "cobit-archive.governance",
                    "files_to_archive": [
                        "/governance/policies/it_policy.doc",
                        "/governance/policies/risk_matrix.xls",
                    ],
                    "compression_level": 6,
                    "encryption_key_id": "COBIT_GOVERNANCE_KEY",
                    "retention_days": 0,
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/governance/policies/it_policy.doc",
                        "/governance/policies/risk_matrix.xls",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_010",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "WARNING",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#cobit-governance",
                    "message": "Task ARCH_010 failed: Source files not found.",
                    "priority": "normal",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/governance/policies/it_policy.doc", "/governance/policies/risk_matrix.xls"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_024",
        instruction=(
            "Reorganize '/var/log' files to meet FISMA compliance requirements for Task ID F_ADJ_016. Target location is '/fisma/federal_logs' with files containing 'agency' in their names categorized to 'government_data' and files containing 'citizen' to 'public_records'. FISMA compliance validation system requires central task database to contain 'Plan registration for F_ADJ_016: Reorganize /var/log for audit.' initially and 'Organized audit-relevant federal records from /var/log.' upon completion, with '#fisma-compliance' notification 'Task F_ADJ_016 (File Tree Adjustment) complete. Federal information logs in /var/log have been successfully organized for audit.' Execute reorganization ensuring these federal information standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/fisma/federal_logs",
                    "sort_rules": {
                        "agency": "government_data",
                        "citizen": "public_records",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_016",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Plan registration for F_ADJ_016: Reorganize /var/log for audit.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/fisma/federal_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/fisma/federal_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/fisma/federal_logs",
                    "sort_rules": {
                        "agency": "government_data",
                        "citizen": "public_records",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_016",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Organized audit-relevant federal records from /var/log.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#fisma-compliance",
                    "message": "Task F_ADJ_016 (File Tree Adjustment) complete. Federal information logs in /var/log have been successfully organized for audit.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_025",
        instruction=(
            "Perform archival process meeting ITIL service management audit requirements for Task ID ARCH_011. Archive '/service/incidents/P1_incidents.csv' and '/service/incidents/P2_incidents.csv' into an archive named 'service_incidents_backup.tar.gz' for delivery to 'itil-storage.ops:/service/archives'.\n\nThis task is governed by the ITIL Framework for service management, which specifies:\n\n1.  **Incident Record Archival**: All incident records must be archived with high Gzip compression (level 8), encrypted with the 'ITIL_SERVICE_KEY', and retained for 1825 days (5 years).\n\n2.  **Pre-flight Check**: Before archival, you must validate that the source incident files exist.\n\n3.  **Failure Reporting**: If the workflow fails due to missing source files, you must log the failure in the database with 'ERROR' severity. A high-priority alert must also be sent to the '#itil-service' channel with the message 'Task ARCH_011 failed: Source files not found.'."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "service_incidents_backup.tar.gz",
                    "destination_directory": "/service/archives",
                    "remote_address": "itil-storage.ops",
                    "files_to_archive": [
                        "/service/incidents/P1_incidents.csv",
                        "/service/incidents/P2_incidents.csv",
                    ],
                    "compression_level": 8,
                    "encryption_key_id": "ITIL_SERVICE_KEY",
                    "retention_days": 1825,
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/service/incidents/P1_incidents.csv",
                        "/service/incidents/P2_incidents.csv",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_011",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "ERROR",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#itil-service",
                    "message": "Task ARCH_011 failed: Source files not found.",
                    "priority": "high",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/service/incidents/P1_incidents.csv", "/service/incidents/P2_incidents.csv"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_026",
        instruction=(
            "Perform archival process meeting ITAR export control audit requirements for Task ID ARCH_012. Archive '/export/controlled/technical_data.pdf' and '/export/controlled/defense_article.doc' as 'itar_controlled_backup.tar.gz' to 'itar-secure.defense:/restricted/archives' using compression level 9 with ITAR_SECURE_KEY encryption and 0-day retention in restricted tier. Missing source files require database updates with 'Workflow terminated due to missing source files.' at CRITICAL severity and '#itar-compliance' notification 'Task ARCH_012 failed: Source files not found.' at urgent priority. Ensure ITAR compliance adherence."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "itar_controlled_backup.tar.gz",
                    "destination_directory": "/restricted/archives",
                    "remote_address": "itar-secure.defense",
                    "files_to_archive": [
                        "/export/controlled/technical_data.pdf",
                        "/export/controlled/defense_article.doc",
                    ],
                    "compression_level": 9,
                    "encryption_key_id": "ITAR_SECURE_KEY",
                    "retention_days": 0,
                    "archive_tier": "restricted",
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/export/controlled/technical_data.pdf",
                        "/export/controlled/defense_article.doc",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_012",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "CRITICAL",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#itar-compliance",
                    "message": "Task ARCH_012 failed: Source files not found.",
                    "priority": "urgent",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/export/controlled/technical_data.pdf", "/export/controlled/defense_article.doc"]',
        ],
    ),
    Task(
    annotator="0",
    user_id="USER_027",
    instruction=(
        "Update central task database by reorganizing '/var/log' to '/basel/risk_logs' for Basel III compliance through Task ID F_ADJ_017. Sort files named 'liquidity' to 'lcr_reports' and 'capital' to 'car_reports'. For audit approval, ensure the database is modified with a final completion log containing the exact note 'Organized audit-relevant risk management files from /var/log.'. The final notification to '#basel-compliance' must also exactly match 'Task F_ADJ_017 (File Tree Adjustment) complete. Risk management logs in /var/log have been successfully organized for audit.'."
    ),
    actions=[
        Action(
            name="ParseDirectoryRestructureInstructions",
            kwargs={
                "target_directory": "/var/log",
                "destination_directory": "/basel/risk_logs",
                "sort_rules": {
                    "liquidity": "lcr_reports",
                    "capital": "car_reports",
                },
            },
        ),
        Action(
            name="CreateFileListForMove",
            kwargs={"target_directory": "/var/log"},
        ),
        Action(name="PopulateChecksumsInFileList", kwargs={}),
        Action(
            name="ComputeAndResolveDestinationPaths",
            kwargs={
                "destination_directory": "/basel/risk_logs",
                "sort_rules": {
                    "liquidity": "lcr_reports",
                    "capital": "car_reports",
                },
            },
        ),
        Action(name="CopyAndVerifyFiles", kwargs={}),
        Action(
            name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "F_ADJ_017",
                "task_name": "File Tree Adjustment",
                "result": "Success",
                "notes": "Organized audit-relevant risk management files from /var/log.",
            },
        ),
        Action(
            name="SendSlackNotification",
            kwargs={
                "channel": "#basel-compliance",
                "message": "Task F_ADJ_017 (File Tree Adjustment) complete. Risk management logs in /var/log have been successfully organized for audit.",
            },
        ),
    ],
    outputs=[
        '"status": "success"',
        '"verified_and_copied": 3',
    ],
),
    Task(
        annotator="0",
        user_id="USER_028",
        instruction=(
            "Perform archival process meeting MiFID II compliance audit requirements for Task ID ARCH_013. Archive '/trading/records/transactions.csv' and '/trading/records/orders.json' as 'mifid_trading_backup.tar.gz' to 'mifid-archive.eu:/regulatory/trading'. The MiFID II configuration requires compression level 8, MIFID_COMPLIANCE_KEY encryption, and 1825-day retention. Failed workflows due to missing source files must update the database with 'Workflow terminated due to missing source files.' using CRITICAL severity, and notify '#mifid-compliance' with 'Task ARCH_013 failed: Source files not found.' at urgent priority. Ensure MiFID II regulatory requirements are satisfied."
        ),
        actions=[
            # Actions remain unchanged
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "mifid_trading_backup.tar.gz",
                    "destination_directory": "/regulatory/trading",
                    "remote_address": "mifid-archive.eu",
                    "files_to_archive": [
                        "/trading/records/transactions.csv",
                        "/trading/records/orders.json",
                    ],
                    "compression_level": 8,
                    "encryption_key_id": "MIFID_COMPLIANCE_KEY",
                    "retention_days": 1825,
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/trading/records/transactions.csv",
                        "/trading/records/orders.json",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_013",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "CRITICAL",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#mifid-compliance",
                    "message": "Task ARCH_013 failed: Source files not found.",
                    "priority": "urgent",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/trading/records/transactions.csv", "/trading/records/orders.json"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_029",
        instruction=(
            "Reorganize '/var/log' files to meet CMMC compliance requirements for Task ID F_ADJ_018. Target location is '/cmmc/defense_logs' with sorting rules for '.contractor' (to 'cui_data') and '.supplier' (to 'supply_chain'). CMMC validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#cmmc-certification' channel that the task is complete. Execute reorganization ensuring these defense industry standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/cmmc/defense_logs",
                    "sort_rules": {
                        "contractor": "cui_data",
                        "supplier": "supply_chain",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_018",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /cmmc/defense_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/cmmc/defense_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/cmmc/defense_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/cmmc/defense_logs",
                    "sort_rules": {
                        "contractor": "cui_data",
                        "supplier": "supply_chain",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_018",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /cmmc/defense_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#cmmc-certification",
                    "message": "Task F_ADJ_018 (File Tree Adjustment) complete. All files from /var/log have been moved to /cmmc/defense_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_030",
        instruction=(
            "Perform archival process meeting FedRAMP authorization requirements for Task ID ARCH_014. Archive '/cloud/assessment/ssp.docx' and '/cloud/assessment/sar.pdf' into an archive named 'fedramp_assessment_backup.tar.gz' for delivery to 'fedramp-secure.gov:/authorization/packages'.\n\nThis task is governed by the FedRAMP framework, which requires the following for handling sensitive government data:\n\n1.  **Secure Government Data Archival**: All assessment documents must be archived with the highest Gzip compression (level 9), encrypted with the 'FEDRAMP_AUTH_KEY', and retained indefinitely (0 days) in the 'gov-secure' tier.\n\n2.  **Pre-flight Validation**: Validate that the source SSP and SAR files exist and that you have read permissions before proceeding.\n\n3.  **Failure Notification Protocol**: If the workflow fails due to missing source files, you must log the failure in the database with 'ERROR' severity. A high-priority alert must also be sent to the '#fedramp-auth' channel with the message 'Task ARCH_014 failed: Source files not found.'."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "fedramp_assessment_backup.tar.gz",
                    "destination_directory": "/authorization/packages",
                    "remote_address": "fedramp-secure.gov",
                    "files_to_archive": [
                        "/cloud/assessment/ssp.docx",
                        "/cloud/assessment/sar.pdf",
                    ],
                    "compression_level": 9,
                    "encryption_key_id": "FEDRAMP_AUTH_KEY",
                    "retention_days": 0,
                    "archive_tier": "gov-secure",
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/cloud/assessment/ssp.docx",
                        "/cloud/assessment/sar.pdf",
                    ],
                    "check_permissions": "enabled",
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_014",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "ERROR",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#fedramp-auth",
                    "message": "Task ARCH_014 failed: Source files not found.",
                    "priority": "high",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/cloud/assessment/ssp.docx", "/cloud/assessment/sar.pdf"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_031",
        instruction=(
            "Reorganize '/var/log' files to meet NERC CIP compliance requirements for Task ID F_ADJ_019. Target location is '/nerc/critical_logs' with sorting rules for '.scada' (to 'operational') and '.ics' (to 'industrial'). NERC compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#nerc-cip' channel that the task is complete. Execute reorganization ensuring these critical infrastructure protection standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/nerc/critical_logs",
                    "sort_rules": {"scada": "operational", "ics": "industrial"},
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_019",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /nerc/critical_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/nerc/critical_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/nerc/critical_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/nerc/critical_logs",
                    "sort_rules": {"scada": "operational", "ics": "industrial"},
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_019",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /nerc/critical_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#nerc-cip",
                    "message": "Task F_ADJ_019 (File Tree Adjustment) complete. All files from /var/log have been moved to /nerc/critical_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
    annotator="0",
    user_id="USER_032",
    instruction=(
        "Attempt SWIFT CSP-compliant archival of SWIFT messages from '/banking/swift/' for Task ID ARCH_015. Deliver the archive, named 'swift_messages_backup.tar.gz', to 'swift-secure.bank:/compliance/archives'. When source files ('mt103.txt', 'mt202.txt') are missing, log the failure with CRITICAL severity and send an urgent-priority alert to the '#swift-csp' channel."
    ),
    actions=[
        Action(
            name="ParseArchiveInstructions",
            kwargs={
                "archive_name": "swift_messages_backup.tar.gz",
                "destination_directory": "/compliance/archives",
                "remote_address": "swift-secure.bank",
                "files_to_archive": [
                    "/banking/swift/mt103.txt",
                    "/banking/swift/mt202.txt",
                ],
            },
        ),
        Action(
            name="ValidateFilesExist",
            kwargs={
                "file_paths": [
                    "/banking/swift/mt103.txt",
                    "/banking/swift/mt202.txt",
                ],
            },
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "ARCH_015",
                "notes": "Workflow terminated due to missing source files.",
                "severity": "CRITICAL",
            },
        ),
        Action(
            name="SendSlackNotification",
            kwargs={
                "channel": "#swift-csp",
                "message": "Task ARCH_015 failed: Source files not found.",
                "priority": "urgent",
            },
        ),
    ],
    outputs=[
        '"status": "failed"',
        '"missing_files": ["/banking/swift/mt103.txt", "/banking/swift/mt202.txt"]',
    ],
),
    Task(
        annotator="0",
        user_id="USER_033",
        instruction=(
            "Reorganize '/var/log' files to meet OWASP compliance requirements for Task ID F_ADJ_020. Target location is '/owasp/security_logs' with 'injection' files routed to 'sqli_attempts' and 'xss' files to 'script_attacks'. OWASP compliance validation system requires central task database to contain 'Plan registration for F_ADJ_020: Reorganize /var/log for audit.' initially and 'Organized audit-relevant security testing files from /var/log.' upon completion. Send notification to '#owasp-security' channel: 'Task F_ADJ_020 (File Tree Adjustment) complete. Security testing logs in /var/log have been successfully organized for audit.' Execute reorganization ensuring these security testing standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/owasp/security_logs",
                    "sort_rules": {
                        "injection": "sqli_attempts",
                        "xss": "script_attacks",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_020",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Plan registration for F_ADJ_020: Reorganize /var/log for audit.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/owasp/security_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/owasp/security_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/owasp/security_logs",
                    "sort_rules": {
                        "injection": "sqli_attempts",
                        "xss": "script_attacks",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_020",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Organized audit-relevant security testing files from /var/log.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#owasp-security",
                    "message": "Task F_ADJ_020 (File Tree Adjustment) complete. Security testing logs in /var/log have been successfully organized for audit.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_034",
        instruction=(
            "Perform archival process meeting GDPR Article 30 compliance audit requirements for Task ID ARCH_016. Archive '/privacy/processing/activities.json' and '/privacy/processing/records.csv' as 'gdpr_records_backup.tar.gz' to 'gdpr-compliant.eu:/article30/archives' using compression level 6 with GDPR_COMPLIANCE_KEY encryption and 2555-day retention. Validation requires permission checks enabled. Missing source files require database updates with 'Workflow terminated due to missing source files.' at ERROR severity and '#gdpr-article30' notification 'Task ARCH_016 failed: Source files not found.' at high priority. Ensure Article 30 compliance adherence."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "gdpr_records_backup.tar.gz",
                    "destination_directory": "/article30/archives",
                    "remote_address": "gdpr-compliant.eu",
                    "files_to_archive": [
                        "/privacy/processing/activities.json",
                        "/privacy/processing/records.csv",
                    ],
                    "compression_level": 6,
                    "encryption_key_id": "GDPR_COMPLIANCE_KEY",
                    "retention_days": 2555,
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/privacy/processing/activities.json",
                        "/privacy/processing/records.csv",
                    ],
                    "check_permissions": "enabled",
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_016",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "ERROR",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#gdpr-article30",
                    "message": "Task ARCH_016 failed: Source files not found.",
                    "priority": "high",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/privacy/processing/activities.json", "/privacy/processing/records.csv"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_035",
        instruction=(
            "Reorganize '/var/log' files to meet RBI compliance requirements for Task ID F_ADJ_021. Target location is '/rbi/banking_logs' with sorting rules for '.neft' (to 'domestic_transfers') and '.rtgs' (to 'settlements'). RBI compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#rbi-compliance' channel that the task is complete. Execute reorganization ensuring these Reserve Bank of India standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/rbi/banking_logs",
                    "sort_rules": {"neft": "domestic_transfers", "rtgs": "settlements"},
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_021",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /rbi/banking_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/rbi/banking_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/rbi/banking_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/rbi/banking_logs",
                    "sort_rules": {"neft": "domestic_transfers", "rtgs": "settlements"},
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_021",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /rbi/banking_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#rbi-compliance",
                    "message": "Task F_ADJ_021 (File Tree Adjustment) complete. All files from /var/log have been moved to /rbi/banking_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_036",
        instruction=(
            "Perform archival process meeting COSO framework audit requirements for Task ID ARCH_017. Archive '/controls/internal/sox_controls.xlsx' and '/controls/internal/risk_assessment.pdf' into an archive named 'coso_controls_backup.tar.gz' for delivery to 'coso-compliant.audit:/framework/archives'.\n\nThis task is governed by the COSO framework for internal controls, which specifies:\n\n1.  **Internal Controls Archival Policy**: All internal control documents must be archived with strong Gzip compression (level 7) and encrypted with the 'COSO_FRAMEWORK_KEY'. These archives must be retained for 2555 days (7 years).\n\n2.  **Pre-Archive Validation**: Validate that the source control and risk assessment files exist before proceeding.\n\n3.  **Failure Reporting Protocol**: If the workflow fails due to missing source files, you must log the failure in the database with 'WARNING' severity. A medium-priority alert must also be sent to the '#coso-framework' channel with the message 'Task ARCH_017 failed: Source files not found.'."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "coso_controls_backup.tar.gz",
                    "destination_directory": "/framework/archives",
                    "remote_address": "coso-compliant.audit",
                    "files_to_archive": [
                        "/controls/internal/sox_controls.xlsx",
                        "/controls/internal/risk_assessment.pdf",
                    ],
                    "compression_level": 7,
                    "encryption_key_id": "COSO_FRAMEWORK_KEY",
                    "retention_days": 2555,
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/controls/internal/sox_controls.xlsx",
                        "/controls/internal/risk_assessment.pdf",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_017",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "WARNING",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#coso-framework",
                    "message": "Task ARCH_017 failed: Source files not found.",
                    "priority": "medium",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/controls/internal/sox_controls.xlsx", "/controls/internal/risk_assessment.pdf"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_037",
        instruction=(
            "Reorganize '/var/log' files to meet IOSCO compliance requirements for Task ID F_ADJ_022. Target location is '/iosco/market_logs' with sorting rules for '.trading' (to 'market_integrity') and '.clearing' (to 'settlement_finality'). IOSCO compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#iosco-principles' channel that the task is complete. Execute reorganization ensuring these securities regulation standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/iosco/market_logs",
                    "sort_rules": {
                        "trading": "market_integrity",
                        "clearing": "settlement_finality",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_022",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /iosco/market_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/iosco/market_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/iosco/market_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/iosco/market_logs",
                    "sort_rules": {
                        "trading": "market_integrity",
                        "clearing": "settlement_finality",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_022",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /iosco/market_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#iosco-principles",
                    "message": "Task F_ADJ_022 (File Tree Adjustment) complete. All files from /var/log have been moved to /iosco/market_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_038",
        instruction=(
            "Perform archival process meeting EBA stress testing audit requirements for Task ID ARCH_018. Archive '/banking/stress/adverse_scenario.csv' and '/banking/stress/baseline_scenario.csv' into an archive named 'eba_stress_backup.tar.gz' for delivery to 'eba-compliant.eu:/stress_testing/archives'.\n\nThis task is governed by the EBA regulatory framework for stress testing, which requires:\n\n1.  **Stress Test Data Archival**: All scenario data must be archived with high Gzip compression (level 8), encrypted with the 'EBA_STRESS_KEY', and retained for 1825 days (5 years).\n\n2.  **Data Integrity Check**: Validate that the source scenario files exist and are not empty (1-byte minimum).\n\n3.  **Regulatory Failure Notification**: If the workflow fails due to missing source files, you must log the failure in the database with 'ERROR' severity. A high-priority alert must also be sent to the '#eba-stress' channel with the message 'Task ARCH_018 failed: Source files not found.'."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "eba_stress_backup.tar.gz",
                    "destination_directory": "/stress_testing/archives",
                    "remote_address": "eba-compliant.eu",
                    "files_to_archive": [
                        "/banking/stress/adverse_scenario.csv",
                        "/banking/stress/baseline_scenario.csv",
                    ],
                    "compression_level": 8,
                    "encryption_key_id": "EBA_STRESS_KEY",
                    "retention_days": 1825,
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/banking/stress/adverse_scenario.csv",
                        "/banking/stress/baseline_scenario.csv",
                    ],
                    "minimum_size_bytes": 1,
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_018",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "ERROR",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#eba-stress",
                    "message": "Task ARCH_018 failed: Source files not found.",
                    "priority": "high",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/banking/stress/adverse_scenario.csv", "/banking/stress/baseline_scenario.csv"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_039",
        instruction=(
            "Reorganize '/var/log' files to meet APRA prudential requirements for Task ID F_ADJ_023. Target location is '/apra/prudential_logs' with sorting rules for '.capital' (to 'cps_standards') and '.liquidity' (to 'aps_standards'). APRA compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#apra-prudential' channel that the task is complete. Execute reorganization ensuring these Australian regulatory standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/apra/prudential_logs",
                    "sort_rules": {
                        "capital": "cps_standards",
                        "liquidity": "aps_standards",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_023",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /apra/prudential_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/apra/prudential_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/apra/prudential_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/apra/prudential_logs",
                    "sort_rules": {
                        "capital": "cps_standards",
                        "liquidity": "aps_standards",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_023",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /apra/prudential_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#apra-prudential",
                    "message": "Task F_ADJ_023 (File Tree Adjustment) complete. All files from /var/log have been moved to /apra/prudential_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_040",
        instruction=(
            "Perform archival process meeting CPRA consumer privacy audit requirements for Task ID ARCH_019. Archive '/california/privacy/opt_out.json' and '/california/privacy/data_requests.csv' as 'cpra_privacy_backup.tar.gz' to 'cpra-secure.ca:/consumer_privacy/archives' using compression level 6 with CPRA_PRIVACY_KEY encryption and 1095-day retention. Missing source files require database updates with 'Workflow terminated due to missing source files.' at ERROR severity and '#cpra-privacy' notification 'Task ARCH_019 failed: Source files not found.' at high priority. Ensure CPRA compliance adherence."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "cpra_privacy_backup.tar.gz",
                    "destination_directory": "/consumer_privacy/archives",
                    "remote_address": "cpra-secure.ca",
                    "files_to_archive": [
                        "/california/privacy/opt_out.json",
                        "/california/privacy/data_requests.csv",
                    ],
                    "compression_level": 6,
                    "encryption_key_id": "CPRA_PRIVACY_KEY",
                    "retention_days": 1095,
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/california/privacy/opt_out.json",
                        "/california/privacy/data_requests.csv",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_019",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "ERROR",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#cpra-privacy",
                    "message": "Task ARCH_019 failed: Source files not found.",
                    "priority": "high",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/california/privacy/opt_out.json", "/california/privacy/data_requests.csv"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_041",
        instruction=(
            "Perform file reorganization of '/var/log' to pass strict DORA compliance audit for Task ID F_ADJ_024. Target location is '/dora/resilience_logs' with sorting rules for '.incident' (to 'disruptions') and '.recovery' (to 'continuity'). Automated compliance check requires specific, machine-readable entries in central task database. For approval, audit system must find initial database log with note 'Registering plan: Move /var/log to /dora/resilience_logs.' and final completion database log with note 'Reorganized 3 files from /var/log to /dora/resilience_logs after successful pre-flight checks.'. User notification sent to '#dora-operational' must exactly match 'Task F_ADJ_024 (File Tree Adjustment) complete. All files from /var/log have been moved to /dora/resilience_logs and sorted.' for compliance system parsing. Execute reorganization while ensuring these specific database audit requirements are met."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/dora/resilience_logs",
                    "sort_rules": {"incident": "disruptions", "recovery": "continuity"},
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_024",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /dora/resilience_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/dora/resilience_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/dora/resilience_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/dora/resilience_logs",
                    "sort_rules": {"incident": "disruptions", "recovery": "continuity"},
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_024",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /dora/resilience_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#dora-operational",
                    "message": "Task F_ADJ_024 (File Tree Adjustment) complete. All files from /var/log have been moved to /dora/resilience_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_042",
        instruction=(
            "Perform archival process meeting Solvency II regulatory audit requirements for Task ID ARCH_020. Archive '/insurance/scr/market_risk.xlsx' and '/insurance/scr/operational_risk.xlsx' as 'solvency_scr_backup.tar.gz' to 'solvency-compliant.eu:/regulatory/capital'. The Solvency II configuration requires compression level 8, SOLVENCY_II_KEY encryption, and 3650-day retention. Failed workflows due to missing source files must update the database with 'Workflow terminated due to missing source files.' using CRITICAL severity, and notify '#solvency-capital' with 'Task ARCH_020 failed: Source files not found.' at urgent priority. Ensure Solvency II capital requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "solvency_scr_backup.tar.gz",
                    "destination_directory": "/regulatory/capital",
                    "remote_address": "solvency-compliant.eu",
                    "files_to_archive": [
                        "/insurance/scr/market_risk.xlsx",
                        "/insurance/scr/operational_risk.xlsx",
                    ],
                    "compression_level": 8,
                    "encryption_key_id": "SOLVENCY_II_KEY",
                    "retention_days": 3650,
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/insurance/scr/market_risk.xlsx",
                        "/insurance/scr/operational_risk.xlsx",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_020",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "CRITICAL",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#solvency-capital",
                    "message": "Task ARCH_020 failed: Source files not found.",
                    "priority": "urgent",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/insurance/scr/market_risk.xlsx", "/insurance/scr/operational_risk.xlsx"]',
        ],
    ),
    Task(
    annotator="0",
    user_id="USER_043",
    instruction=(
        "Update central task database by reorganizing files from '/var/log' to '/ifrs17/insurance_logs' for Task ID F_ADJ_025. Sort 'premium' files to 'insurance_revenue' and 'claims' files to 'insurance_expense'. To meet IFRS 17 compliance, ensure the database is updated with a final log stating 'Organized audit-relevant insurance contract files from /var/log.' and the '#ifrs17-reporting' channel receives a notification with the exact message 'Task F_ADJ_025 (File Tree Adjustment) complete. Insurance contract logs in /var/log have been successfully organized for audit.'."
    ),
    actions=[
        Action(
            name="ParseDirectoryRestructureInstructions",
            kwargs={
                "target_directory": "/var/log",
                "destination_directory": "/ifrs17/insurance_logs",
                "sort_rules": {
                    "premium": "insurance_revenue",
                    "claims": "insurance_expense",
                },
            },
        ),
        Action(
            name="CreateFileListForMove",
            kwargs={"target_directory": "/var/log"},
        ),
        Action(name="PopulateChecksumsInFileList", kwargs={}),
        Action(
            name="ComputeAndResolveDestinationPaths",
            kwargs={
                "destination_directory": "/ifrs17/insurance_logs",
                "sort_rules": {
                    "premium": "insurance_revenue",
                    "claims": "insurance_expense",
                },
            },
        ),
        Action(name="CopyAndVerifyFiles", kwargs={}),
        Action(
            name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "F_ADJ_025",
                "task_name": "File Tree Adjustment",
                "result": "Success",
                "notes": "Organized audit-relevant insurance contract files from /var/log.",
            },
        ),
        Action(
            name="SendSlackNotification",
            kwargs={
                "channel": "#ifrs17-reporting",
                "message": "Task F_ADJ_025 (File Tree Adjustment) complete. Insurance contract logs in /var/log have been successfully organized for audit.",
            },
        ),
    ],
    outputs=[
        '"status": "success"',
        '"verified_and_copied": 3',
    ],
),
    Task(
        annotator="0",
        user_id="USER_044",
        instruction=(
            "Perform archival process meeting TCFD climate disclosure audit requirements for Task ID ARCH_021. Archive '/climate/risks/physical_risks.json' and '/climate/risks/transition_risks.json' into an archive named 'tcfd_climate_backup.tar.gz' for delivery to 'tcfd-compliant.esg:/disclosures/climate'.\n\nThis task is governed by the TCFD Framework for climate-related financial disclosures, which requires:\n\n1.  **Climate Risk Data Archival**: All climate risk data must be archived with balanced Gzip compression (level 6), encrypted using the 'TCFD_CLIMATE_KEY', and retained for 1825 days (5 years).\n\n2.  **Pre-Archive Validation**: Confirm that the source physical and transition risk files exist before initiating the backup.\n\n3.  **Disclosure Failure Reporting**: If the workflow fails due to missing source files, you must log the failure in the database with 'ERROR' severity. A high-priority alert must also be sent to the '#tcfd-climate' channel with the message 'Task ARCH_021 failed: Source files not found.'."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "tcfd_climate_backup.tar.gz",
                    "destination_directory": "/disclosures/climate",
                    "remote_address": "tcfd-compliant.esg",
                    "files_to_archive": [
                        "/climate/risks/physical_risks.json",
                        "/climate/risks/transition_risks.json",
                    ],
                    "compression_level": 6,
                    "encryption_key_id": "TCFD_CLIMATE_KEY",
                    "retention_days": 1825,
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/climate/risks/physical_risks.json",
                        "/climate/risks/transition_risks.json",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_021",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "ERROR",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#tcfd-climate",
                    "message": "Task ARCH_021 failed: Source files not found.",
                    "priority": "high",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/climate/risks/physical_risks.json", "/climate/risks/transition_risks.json"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_045",
        instruction=(
            "Reorganize '/var/log' files to meet SASB sustainability reporting requirements for Task ID F_ADJ_026. Target location is '/sasb/sustainability_logs' with sorting rules for '.emissions' (to 'environmental') and '.workforce' (to 'social'). SASB compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#sasb-reporting' channel that the task is complete. Execute reorganization ensuring these sustainability disclosure standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/sasb/sustainability_logs",
                    "sort_rules": {"emissions": "environmental", "workforce": "social"},
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_026",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /sasb/sustainability_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/sasb/sustainability_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/sasb/sustainability_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/sasb/sustainability_logs",
                    "sort_rules": {"emissions": "environmental", "workforce": "social"},
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_026",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /sasb/sustainability_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#sasb-reporting",
                    "message": "Task F_ADJ_026 (File Tree Adjustment) complete. All files from /var/log have been moved to /sasb/sustainability_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_046",
        instruction=(
            "Perform archival process meeting SEC Rule 17a-4 compliance audit requirements for Task ID ARCH_022. Archive '/trading/communications/emails.pst' and '/trading/communications/chats.json' into an archive named 'sec_communications_backup.tar.gz' for delivery to 'sec-compliant.finance:/rule17a4/archives'.\n\nThis task is governed by SEC Rule 17a-4, which mandates the following for electronic records:\n\n1.  **WORM Storage Archival**: All broker-dealer communications must be archived with high Gzip compression (level 7), encrypted using the 'SEC_17A4_KEY', and retained for 2190 days (6 years) in a WORM-compliant (Write-Once, Read-Many) tier.\n\n2.  **Pre-Archive Validation**: Confirm that the source email and chat records exist before initiating the backup.\n\n3.  **Regulatory Reporting for Failures**: If the workflow fails due to missing source files, you must log the failure in the database with 'CRITICAL' severity. An urgent-priority alert must also be sent to the '#sec-rule17a4' channel with the message 'Task ARCH_022 failed: Source files not found.'."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "sec_communications_backup.tar.gz",
                    "destination_directory": "/rule17a4/archives",
                    "remote_address": "sec-compliant.finance",
                    "files_to_archive": [
                        "/trading/communications/emails.pst",
                        "/trading/communications/chats.json",
                    ],
                    "compression_level": 7,
                    "encryption_key_id": "SEC_17A4_KEY",
                    "retention_days": 2190,
                    "archive_tier": "WORM",
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/trading/communications/emails.pst",
                        "/trading/communications/chats.json",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_022",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                    "severity": "CRITICAL",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#sec-rule17a4",
                    "message": "Task ARCH_022 failed: Source files not found.",
                    "priority": "urgent",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/trading/communications/emails.pst", "/trading/communications/chats.json"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_047",
        instruction=(
            "Reorganize '/var/log' files to meet FATF compliance requirements for Task ID F_ADJ_027. Target location is '/fatf/aml_logs' with sorting rules for '.kyc' (to 'customer_due_diligence') and '.sar' (to 'suspicious_activity'). FATF compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#fatf-compliance' channel that the task is complete. Execute reorganization ensuring these anti-money laundering standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/fatf/aml_logs",
                    "sort_rules": {
                        "kyc": "customer_due_diligence",
                        "sar": "suspicious_activity",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_027",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /fatf/aml_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/fatf/aml_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/fatf/aml_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/fatf/aml_logs",
                    "sort_rules": {
                        "kyc": "customer_due_diligence",
                        "sar": "suspicious_activity",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_027",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /fatf/aml_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#fatf-compliance",
                    "message": "Task F_ADJ_027 (File Tree Adjustment) complete. All files from /var/log have been moved to /fatf/aml_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_048",
        instruction=(
            "Perform archival process meeting ESMA MiFIR transaction reporting audit requirements for Task ID ARCH_023. Archive '/reporting/mifir/transaction_reports.xml' and '/reporting/mifir/reference_data.csv' into 'esma_mifir_backup.tar.gz' for destination 'esma-compliant.eu:/mifir/transaction_reporting'. The ESMA regulatory framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#esma-mifir' reading 'Task ARCH_023 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "esma_mifir_backup.tar.gz",
                    "destination_directory": "/mifir/transaction_reporting",
                    "remote_address": "esma-compliant.eu",
                    "files_to_archive": [
                        "/reporting/mifir/transaction_reports.xml",
                        "/reporting/mifir/reference_data.csv",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/reporting/mifir/transaction_reports.xml",
                        "/reporting/mifir/reference_data.csv",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_023",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#esma-mifir",
                    "message": "Task ARCH_023 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/reporting/mifir/transaction_reports.xml", "/reporting/mifir/reference_data.csv"]',
        ],
    ),
    Task(
    annotator="0",
    user_id="USER_049",
    instruction=(
        "Modify central task database by reorganizing '/var/log' to '/fsb/tlac_logs' for Task ID F_ADJ_028. Sort '.subordinated' files to 'tier2_capital' and '.senior' files to 'tier1_capital'. For FSB TLAC compliance, update the database with a log stating 'Reorganized 3 files from /var/log to /fsb/tlac_logs after successful pre-flight checks.' and send a notification to '#fsb-tlac' with the message 'Task F_ADJ_028 (File Tree Adjustment) complete. All files from /var/log have been moved to /fsb/tlac_logs and sorted.'."
    ),
    actions=[
        Action(
            name="ParseDirectoryRestructureInstructions",
            kwargs={
                "target_directory": "/var/log",
                "destination_directory": "/fsb/tlac_logs",
                "sort_rules": {
                    "subordinated": "tier2_capital",
                    "senior": "tier1_capital",
                },
            },
        ),
        Action(
            name="CreateFileListForMove",
            kwargs={"target_directory": "/var/log"},
        ),
        Action(name="PopulateChecksumsInFileList", kwargs={}),
        Action(
            name="ComputeAndResolveDestinationPaths",
            kwargs={
                "destination_directory": "/fsb/tlac_logs",
                "sort_rules": {
                    "subordinated": "tier2_capital",
                    "senior": "tier1_capital",
                },
            },
        ),
        Action(name="CopyAndVerifyFiles", kwargs={}),
        Action(
            name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "F_ADJ_028",
                "task_name": "File Tree Adjustment",
                "result": "Success",
                "notes": "Reorganized 3 files from /var/log to /fsb/tlac_logs after successful pre-flight checks.",
            },
        ),
        Action(
            name="SendSlackNotification",
            kwargs={
                "channel": "#fsb-tlac",
                "message": "Task F_ADJ_028 (File Tree Adjustment) complete. All files from /var/log have been moved to /fsb/tlac_logs and sorted.",
            },
        ),
    ],
    outputs=[
        '"status": "success"',
        '"verified_and_copied": 3',
        '"cleaned_files_count": 3',
    ],
),
    Task(
        annotator="0",
        user_id="USER_050",
        instruction=(
            "Perform archival process meeting CFTC swap data reporting audit requirements for Task ID ARCH_024. Archive '/derivatives/swaps/interest_rate.json' and '/derivatives/swaps/credit_default.json' into 'cftc_swaps_backup.tar.gz' for destination 'cftc-compliant.gov:/swap_data/repository'. The CFTC regulatory framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#cftc-swaps' reading 'Task ARCH_024 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "cftc_swaps_backup.tar.gz",
                    "destination_directory": "/swap_data/repository",
                    "remote_address": "cftc-compliant.gov",
                    "files_to_archive": [
                        "/derivatives/swaps/interest_rate.json",
                        "/derivatives/swaps/credit_default.json",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/derivatives/swaps/interest_rate.json",
                        "/derivatives/swaps/credit_default.json",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_024",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#cftc-swaps",
                    "message": "Task ARCH_024 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/derivatives/swaps/interest_rate.json", "/derivatives/swaps/credit_default.json"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_051",
        instruction=(
            "Perform archival process meeting BCBS 239 risk data aggregation audit requirements for Task ID ARCH_025. Archive '/risk/data/credit_exposures.csv' and '/risk/data/market_positions.csv' into 'bcbs239_risk_backup.tar.gz' for destination 'bcbs-compliant.bank:/riskdata/aggregation'. The BCBS framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#bcbs239-risk' reading 'Task ARCH_025 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "bcbs239_risk_backup.tar.gz",
                    "destination_directory": "/riskdata/aggregation",
                    "remote_address": "bcbs-compliant.bank",
                    "files_to_archive": [
                        "/risk/data/credit_exposures.csv",
                        "/risk/data/market_positions.csv",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/risk/data/credit_exposures.csv",
                        "/risk/data/market_positions.csv",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_025",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#bcbs239-risk",
                    "message": "Task ARCH_025 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/risk/data/credit_exposures.csv", "/risk/data/market_positions.csv"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_052",
        instruction=(
            "Reorganize '/var/log' files to meet EMIR compliance requirements for Task ID F_ADJ_029. Target location is '/emir/derivative_logs' with sorting rules for '.otc' (to 'over_the_counter') and '.etd' (to 'exchange_traded'). EMIR compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#emir-reporting' channel that the task is complete. Execute reorganization ensuring these European derivatives standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/emir/derivative_logs",
                    "sort_rules": {"otc": "over_the_counter", "etd": "exchange_traded"},
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_029",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /emir/derivative_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/emir/derivative_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/emir/derivative_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/emir/derivative_logs",
                    "sort_rules": {"otc": "over_the_counter", "etd": "exchange_traded"},
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_029",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /emir/derivative_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#emir-reporting",
                    "message": "Task F_ADJ_029 (File Tree Adjustment) complete. All files from /var/log have been moved to /emir/derivative_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_053",
        instruction=(
            "Perform archival process meeting PIPEDA privacy audit requirements for Task ID ARCH_026. Archive '/canada/privacy/consent_records.json' and '/canada/privacy/breach_notifications.csv' into 'pipeda_privacy_backup.tar.gz' for destination 'pipeda-compliant.ca:/privacy/protection'. The PIPEDA compliance framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#pipeda-privacy' reading 'Task ARCH_026 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "pipeda_privacy_backup.tar.gz",
                    "destination_directory": "/privacy/protection",
                    "remote_address": "pipeda-compliant.ca",
                    "files_to_archive": [
                        "/canada/privacy/consent_records.json",
                        "/canada/privacy/breach_notifications.csv",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/canada/privacy/consent_records.json",
                        "/canada/privacy/breach_notifications.csv",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_026",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#pipeda-privacy",
                    "message": "Task ARCH_026 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/canada/privacy/consent_records.json", "/canada/privacy/breach_notifications.csv"]',
        ],
    ),
    Task(
    annotator="0",
    user_id="USER_054",
    instruction=(
        "Update central task database by reorganizing files from '/var/log' to '/lgpd/brazilian_logs' to meet LGPD compliance for Task ID F_ADJ_030. Sort '.personal' files to 'dados_pessoais' and '.sensitive' files to 'dados_sensiveis'. To pass the audit, ensure the database is updated with a log stating 'Reorganized 3 files from /var/log to /lgpd/brazilian_logs after successful pre-flight checks.' and a notification is sent to '#lgpd-compliance' with the message 'Task F_ADJ_030 (File Tree Adjustment) complete. All files from /var/log have been moved to /lgpd/brazilian_logs and sorted.'."
    ),
    actions=[
        Action(
            name="ParseDirectoryRestructureInstructions",
            kwargs={
                "target_directory": "/var/log",
                "destination_directory": "/lgpd/brazilian_logs",
                "sort_rules": {
                    "personal": "dados_pessoais",
                    "sensitive": "dados_sensiveis",
                },
            },
        ),
        Action(
            name="CreateFileListForMove",
            kwargs={"target_directory": "/var/log"},
        ),
        Action(name="PopulateChecksumsInFileList", kwargs={}),
        Action(
            name="ComputeAndResolveDestinationPaths",
            kwargs={
                "destination_directory": "/lgpd/brazilian_logs",
                "sort_rules": {
                    "personal": "dados_pessoais",
                    "sensitive": "dados_sensiveis",
                },
            },
        ),
        Action(name="CopyAndVerifyFiles", kwargs={}),
        Action(
            name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "F_ADJ_030",
                "task_name": "File Tree Adjustment",
                "result": "Success",
                "notes": "Reorganized 3 files from /var/log to /lgpd/brazilian_logs after successful pre-flight checks.",
            },
        ),
        Action(
            name="SendSlackNotification",
            kwargs={
                "channel": "#lgpd-compliance",
                "message": "Task F_ADJ_030 (File Tree Adjustment) complete. All files from /var/log have been moved to /lgpd/brazilian_logs and sorted.",
            },
        ),
    ],
    outputs=[
        '"status": "success"',
        '"verified_and_copied": 3',
        '"cleaned_files_count": 3',
    ],
),
    Task(
        annotator="0",
        user_id="USER_055",
        instruction=(
            "Perform archival process meeting SAMA cybersecurity framework audit requirements for Task ID ARCH_027. Archive '/saudi/cyber/threat_intel.json' and '/saudi/cyber/incident_response.log' into 'sama_cyber_backup.tar.gz' for destination 'sama-compliant.sa:/cybersecurity/framework'. The SAMA regulatory framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#sama-cyber' reading 'Task ARCH_027 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "sama_cyber_backup.tar.gz",
                    "destination_directory": "/cybersecurity/framework",
                    "remote_address": "sama-compliant.sa",
                    "files_to_archive": [
                        "/saudi/cyber/threat_intel.json",
                        "/saudi/cyber/incident_response.log",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/saudi/cyber/threat_intel.json",
                        "/saudi/cyber/incident_response.log",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_027",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#sama-cyber",
                    "message": "Task ARCH_027 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/saudi/cyber/threat_intel.json", "/saudi/cyber/incident_response.log"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_056",
        instruction=(
            "Reorganize '/var/log' files to meet PDPA compliance requirements for Task ID F_ADJ_031. Target location is '/pdpa/singapore_logs' with sorting rules for '.personal' (to 'individual_data') and '.consent' (to 'permission_records'). PDPA compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#pdpa-singapore' channel that the task is complete. Execute reorganization ensuring these Singapore data protection standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/pdpa/singapore_logs",
                    "sort_rules": {
                        "personal": "individual_data",
                        "consent": "permission_records",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_031",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /pdpa/singapore_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/pdpa/singapore_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/pdpa/singapore_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/pdpa/singapore_logs",
                    "sort_rules": {
                        "personal": "individual_data",
                        "consent": "permission_records",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_031",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /pdpa/singapore_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#pdpa-singapore",
                    "message": "Task F_ADJ_031 (File Tree Adjustment) complete. All files from /var/log have been moved to /pdpa/singapore_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_057",
        instruction=(
            "Perform archival process meeting DIFC data protection audit requirements for Task ID ARCH_028. Archive '/dubai/difc/employee_data.xlsx' and '/dubai/difc/customer_records.csv' into 'difc_data_backup.tar.gz' for destination 'difc-compliant.ae:/data_protection/archives'. The DIFC regulatory framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#difc-data' reading 'Task ARCH_028 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "difc_data_backup.tar.gz",
                    "destination_directory": "/data_protection/archives",
                    "remote_address": "difc-compliant.ae",
                    "files_to_archive": [
                        "/dubai/difc/employee_data.xlsx",
                        "/dubai/difc/customer_records.csv",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/dubai/difc/employee_data.xlsx",
                        "/dubai/difc/customer_records.csv",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_028",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#difc-data",
                    "message": "Task ARCH_028 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/dubai/difc/employee_data.xlsx", "/dubai/difc/customer_records.csv"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_058",
        instruction=(
            "Reorganize '/var/log' files to meet OECD compliance requirements for Task ID F_ADJ_032. Target location is '/oecd/privacy_logs' with sorting rules for '.collection' (to 'data_gathering') and '.usage' (to 'data_processing'). OECD compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#oecd-privacy' channel that the task is complete. Execute reorganization ensuring these privacy guideline standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/oecd/privacy_logs",
                    "sort_rules": {
                        "collection": "data_gathering",
                        "usage": "data_processing",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_032",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /oecd/privacy_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/oecd/privacy_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/oecd/privacy_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/oecd/privacy_logs",
                    "sort_rules": {
                        "collection": "data_gathering",
                        "usage": "data_processing",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_032",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /oecd/privacy_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#oecd-privacy",
                    "message": "Task F_ADJ_032 (File Tree Adjustment) complete. All files from /var/log have been moved to /oecd/privacy_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_059",
        instruction=(
            "Perform archival process meeting APEC CBPR certification audit requirements for Task ID ARCH_029. Archive '/apec/privacy/accountability.json' and '/apec/privacy/cross_border.csv' into 'apec_cbpr_backup.tar.gz' for destination 'apec-certified.org:/cbpr/privacy'. The APEC CBPR framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#apec-cbpr' reading 'Task ARCH_029 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "apec_cbpr_backup.tar.gz",
                    "destination_directory": "/cbpr/privacy",
                    "remote_address": "apec-certified.org",
                    "files_to_archive": [
                        "/apec/privacy/accountability.json",
                        "/apec/privacy/cross_border.csv",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/apec/privacy/accountability.json",
                        "/apec/privacy/cross_border.csv",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_029",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#apec-cbpr",
                    "message": "Task ARCH_029 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/apec/privacy/accountability.json", "/apec/privacy/cross_border.csv"]',
        ],
    ),
    Task(
    annotator="0",
    user_id="USER_060",
    instruction=(
        "Update central task database by reorganizing files from '/var/log' to '/lgpd/brazilian_logs' to meet LGPD compliance for Task ID F_ADJ_030. Sort '.personal' files to 'dados_pessoais' and '.sensitive' files to 'dados_sensiveis'. To pass the audit, ensure the database is updated with a log stating 'Reorganized 3 files from /var/log to /lgpd/brazilian_logs after successful pre-flight checks.' and a notification is sent to '#lgpd-compliance' with the message 'Task F_ADJ_030 (File Tree Adjustment) complete. All files from /var/log have been moved to /lgpd/brazilian_logs and sorted.'."
    ),
    actions=[
        Action(
            name="ParseDirectoryRestructureInstructions",
            kwargs={
                "target_directory": "/var/log",
                "destination_directory": "/lgpd/brazilian_logs",
                "sort_rules": {
                    "personal": "dados_pessoais",
                    "sensitive": "dados_sensiveis",
                },
            },
        ),
        Action(
            name="CreateFileListForMove",
            kwargs={"target_directory": "/var/log"},
        ),
        Action(name="PopulateChecksumsInFileList", kwargs={}),
        Action(
            name="ComputeAndResolveDestinationPaths",
            kwargs={
                "destination_directory": "/lgpd/brazilian_logs",
                "sort_rules": {
                    "personal": "dados_pessoais",
                    "sensitive": "dados_sensiveis",
                },
            },
        ),
        Action(name="CopyAndVerifyFiles", kwargs={}),
        Action(
            name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "F_ADJ_030",
                "task_name": "File Tree Adjustment",
                "result": "Success",
                "notes": "Reorganized 3 files from /var/log to /lgpd/brazilian_logs after successful pre-flight checks.",
            },
        ),
        Action(
            name="SendSlackNotification",
            kwargs={
                "channel": "#lgpd-compliance",
                "message": "Task F_ADJ_030 (File Tree Adjustment) complete. All files from /var/log have been moved to /lgpd/brazilian_logs and sorted.",
            },
        ),
    ],
    outputs=[
        '"status": "success"',
        '"verified_and_copied": 3',
        '"cleaned_files_count": 3',
    ],
),
    Task(
        annotator="0",
        user_id="USER_061",
        instruction=(
            "Perform archival process meeting FINRA Rule 4511 audit requirements for Task ID ARCH_030. Archive '/broker/records/customer_accounts.csv' and '/broker/records/order_tickets.json' into 'finra_records_backup.tar.gz' for destination 'finra-compliant.us:/rule4511/books'. The FINRA regulatory framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#finra-4511' reading 'Task ARCH_030 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "finra_records_backup.tar.gz",
                    "destination_directory": "/rule4511/books",
                    "remote_address": "finra-compliant.us",
                    "files_to_archive": [
                        "/broker/records/customer_accounts.csv",
                        "/broker/records/order_tickets.json",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/broker/records/customer_accounts.csv",
                        "/broker/records/order_tickets.json",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_030",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#finra-4511",
                    "message": "Task ARCH_030 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/broker/records/customer_accounts.csv", "/broker/records/order_tickets.json"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_062",
        instruction=(
            "Reorganize '/var/log' files to meet MAS compliance requirements for Task ID F_ADJ_034. Target location is '/mas/singapore_financial' with sorting rules for '.remittance' (to 'cross_border') and '.digital' (to 'fintech_services'). MAS compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#mas-compliance' channel that the task is complete. Execute reorganization ensuring these Monetary Authority of Singapore standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/mas/singapore_financial",
                    "sort_rules": {
                        "remittance": "cross_border",
                        "digital": "fintech_services",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_034",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /mas/singapore_financial.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/mas/singapore_financial"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/mas/singapore_financial"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/mas/singapore_financial",
                    "sort_rules": {
                        "remittance": "cross_border",
                        "digital": "fintech_services",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_034",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /mas/singapore_financial after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#mas-compliance",
                    "message": "Task F_ADJ_034 (File Tree Adjustment) complete. All files from /var/log have been moved to /mas/singapore_financial and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_063",
        instruction=(
            "Perform archival process meeting BIS Basel Committee audit requirements for Task ID ARCH_031. Archive '/basel/committee/leverage_ratio.xlsx' and '/basel/committee/nsfr_calculation.csv' into 'bis_basel_backup.tar.gz' for destination 'bis-compliant.ch:/basel/standards'. The BIS regulatory framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#bis-basel' reading 'Task ARCH_031 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "bis_basel_backup.tar.gz",
                    "destination_directory": "/basel/standards",
                    "remote_address": "bis-compliant.ch",
                    "files_to_archive": [
                        "/basel/committee/leverage_ratio.xlsx",
                        "/basel/committee/nsfr_calculation.csv",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/basel/committee/leverage_ratio.xlsx",
                        "/basel/committee/nsfr_calculation.csv",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_031",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#bis-basel",
                    "message": "Task ARCH_031 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/basel/committee/leverage_ratio.xlsx", "/basel/committee/nsfr_calculation.csv"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_064",
        instruction=(
            "Reorganize '/var/log' files to meet CSRC compliance requirements for Task ID F_ADJ_035. Target location is '/csrc/china_securities' with sorting rules for files named 'disclosure' (to 'information_disclosure') and files named 'trading' (to 'market_supervision'). CSRC compliance validation system requires central task database to contain evidence of plan registration and successful completion. Send notification to '#csrc-compliance' channel that the task is complete. Execute reorganization ensuring these Chinese securities regulatory standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/csrc/china_securities",
                    "sort_rules": {
                        "disclosure": "information_disclosure",
                        "trading": "market_supervision",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_035",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /csrc/china_securities.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/csrc/china_securities"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/csrc/china_securities"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/csrc/china_securities",
                    "sort_rules": {
                        "disclosure": "information_disclosure",
                        "trading": "market_supervision",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_035",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /csrc/china_securities after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#csrc-compliance",
                    "message": "Task F_ADJ_035 (File Tree Adjustment) complete. All files from /var/log have been moved to /csrc/china_securities and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_065",
        instruction=(
            "Perform archival process meeting FCA SMCR regime audit requirements for Task ID ARCH_032. Archive '/uk/smcr/senior_managers.json' and '/uk/smcr/certification_regime.csv' into 'fca_smcr_backup.tar.gz' for destination 'fca-compliant.uk:/smcr/accountability'. The FCA regulatory framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#fca-smcr' reading 'Task ARCH_032 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "fca_smcr_backup.tar.gz",
                    "destination_directory": "/smcr/accountability",
                    "remote_address": "fca-compliant.uk",
                    "files_to_archive": [
                        "/uk/smcr/senior_managers.json",
                        "/uk/smcr/certification_regime.csv",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/uk/smcr/senior_managers.json",
                        "/uk/smcr/certification_regime.csv",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_032",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#fca-smcr",
                    "message": "Task ARCH_032 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/uk/smcr/senior_managers.json", "/uk/smcr/certification_regime.csv"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_066",
        instruction=(
            "Reorganize '/var/log' files to meet HKMA compliance requirements for Task ID F_ADJ_036. Target location is '/hkma/hong_kong_logs' with sorting rules for '.virtual' (to 'virtual_banking') and '.stable' (to 'stablecoin_regulation'). HKMA compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#hkma-compliance' channel that the task is complete. Execute reorganization ensuring these Hong Kong monetary authority standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/hkma/hong_kong_logs",
                    "sort_rules": {
                        "virtual": "virtual_banking",
                        "stable": "stablecoin_regulation",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_036",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /hkma/hong_kong_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/hkma/hong_kong_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/hkma/hong_kong_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/hkma/hong_kong_logs",
                    "sort_rules": {
                        "virtual": "virtual_banking",
                        "stable": "stablecoin_regulation",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_036",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /hkma/hong_kong_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#hkma-compliance",
                    "message": "Task F_ADJ_036 (File Tree Adjustment) complete. All files from /var/log have been moved to /hkma/hong_kong_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_067",
        instruction=(
            "Perform archival process meeting SEBI compliance audit requirements for Task ID ARCH_033. Archive '/india/sebi/insider_trading.log' and '/india/sebi/market_manipulation.csv' into 'sebi_compliance_backup.tar.gz' for destination 'sebi-compliant.in:/regulatory/surveillance'. The SEBI regulatory framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#sebi-surveillance' reading 'Task ARCH_033 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "sebi_compliance_backup.tar.gz",
                    "destination_directory": "/regulatory/surveillance",
                    "remote_address": "sebi-compliant.in",
                    "files_to_archive": [
                        "/india/sebi/insider_trading.log",
                        "/india/sebi/market_manipulation.csv",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/india/sebi/insider_trading.log",
                        "/india/sebi/market_manipulation.csv",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_033",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#sebi-surveillance",
                    "message": "Task ARCH_033 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/india/sebi/insider_trading.log", "/india/sebi/market_manipulation.csv"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_068",
        instruction=(
            "Reorganize '/var/log' files to meet JFSA compliance requirements for Task ID F_ADJ_037. Target location is '/jfsa/japan_financial' with sorting rules for '.zaibatsu' (to 'conglomerate_oversight') and '.crypto' (to 'digital_assets'). JFSA compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#jfsa-compliance' channel that the task is complete. Execute reorganization ensuring these Japanese financial regulatory standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/jfsa/japan_financial",
                    "sort_rules": {
                        "zaibatsu": "conglomerate_oversight",
                        "crypto": "digital_assets",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_037",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /jfsa/japan_financial.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/jfsa/japan_financial"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/jfsa/japan_financial"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/jfsa/japan_financial",
                    "sort_rules": {
                        "zaibatsu": "conglomerate_oversight",
                        "crypto": "digital_assets",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_037",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /jfsa/japan_financial after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#jfsa-compliance",
                    "message": "Task F_ADJ_037 (File Tree Adjustment) complete. All files from /var/log have been moved to /jfsa/japan_financial and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_069",
        instruction=(
            "Perform archival process meeting ASIC market integrity audit requirements for Task ID ARCH_034. Archive '/australia/asic/market_conduct.json' and '/australia/asic/product_intervention.csv' into 'asic_integrity_backup.tar.gz' for destination 'asic-compliant.au:/market/integrity'. The ASIC regulatory framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#asic-market' reading 'Task ARCH_034 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "asic_integrity_backup.tar.gz",
                    "destination_directory": "/market/integrity",
                    "remote_address": "asic-compliant.au",
                    "files_to_archive": [
                        "/australia/asic/market_conduct.json",
                        "/australia/asic/product_intervention.csv",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/australia/asic/market_conduct.json",
                        "/australia/asic/product_intervention.csv",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_034",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#asic-market",
                    "message": "Task ARCH_034 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/australia/asic/market_conduct.json", "/australia/asic/product_intervention.csv"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_070",
        instruction=(
            "Reorganize '/var/log' files to meet ACPR compliance requirements for Task ID F_ADJ_038. Target location is '/acpr/french_prudential' with sorting rules for '.solvabilite' (to 'solvency_requirements') and '.liquidite' (to 'liquidity_coverage'). ACPR compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#acpr-compliance' channel that the task is complete. Execute reorganization ensuring these French prudential supervisory standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/acpr/french_prudential",
                    "sort_rules": {
                        "solvabilite": "solvency_requirements",
                        "liquidite": "liquidity_coverage",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_038",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /acpr/french_prudential.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/acpr/french_prudential"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/acpr/french_prudential"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/acpr/french_prudential",
                    "sort_rules": {
                        "solvabilite": "solvency_requirements",
                        "liquidite": "liquidity_coverage",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_038",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /acpr/french_prudential after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#acpr-compliance",
                    "message": "Task F_ADJ_038 (File Tree Adjustment) complete. All files from /var/log have been moved to /acpr/french_prudential and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_071",
        instruction=(
            "Perform archival process meeting AMF compliance audit requirements for Task ID ARCH_035. Archive '/france/amf/market_abuse.json' and '/france/amf/insider_dealing.csv' into 'amf_surveillance_backup.tar.gz' for destination 'amf-compliant.fr:/surveillance/archives'. The AMF regulatory framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#amf-surveillance' reading 'Task ARCH_035 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "amf_surveillance_backup.tar.gz",
                    "destination_directory": "/surveillance/archives",
                    "remote_address": "amf-compliant.fr",
                    "files_to_archive": [
                        "/france/amf/market_abuse.json",
                        "/france/amf/insider_dealing.csv",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/france/amf/market_abuse.json",
                        "/france/amf/insider_dealing.csv",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_035",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#amf-surveillance",
                    "message": "Task ARCH_035 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/france/amf/market_abuse.json", "/france/amf/insider_dealing.csv"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_072",
        instruction=(
            "Reorganize '/var/log' files to meet BAFIN compliance requirements for Task ID F_ADJ_039. Target location is '/bafin/german_logs' with sorting rules for '.kredit' (to 'credit_institutions') and '.versicherung' (to 'insurance_undertakings'). BAFIN compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#bafin-compliance' channel that the task is complete. Execute reorganization ensuring these German financial supervisory standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/bafin/german_logs",
                    "sort_rules": {
                        "kredit": "credit_institutions",
                        "versicherung": "insurance_undertakings",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_039",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /bafin/german_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/bafin/german_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/bafin/german_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/bafin/german_logs",
                    "sort_rules": {
                        "kredit": "credit_institutions",
                        "versicherung": "insurance_undertakings",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_039",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /bafin/german_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#bafin-compliance",
                    "message": "Task F_ADJ_039 (File Tree Adjustment) complete. All files from /var/log have been moved to /bafin/german_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_073",
        instruction=(
            "Perform archival process meeting CNBV compliance audit requirements for Task ID ARCH_036. Archive '/mexico/cnbv/banking_supervision.xlsx' and '/mexico/cnbv/securities_oversight.json' into 'cnbv_regulatory_backup.tar.gz' for destination 'cnbv-compliant.mx:/supervision/archives'. The CNBV regulatory framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#cnbv-supervision' reading 'Task ARCH_036 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "cnbv_regulatory_backup.tar.gz",
                    "destination_directory": "/supervision/archives",
                    "remote_address": "cnbv-compliant.mx",
                    "files_to_archive": [
                        "/mexico/cnbv/banking_supervision.xlsx",
                        "/mexico/cnbv/securities_oversight.json",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/mexico/cnbv/banking_supervision.xlsx",
                        "/mexico/cnbv/securities_oversight.json",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_036",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#cnbv-supervision",
                    "message": "Task ARCH_036 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/mexico/cnbv/banking_supervision.xlsx", "/mexico/cnbv/securities_oversight.json"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_074",
        instruction=(
            "Reorganize '/var/log' files to meet CONSOB compliance requirements for Task ID F_ADJ_040. Target location is '/consob/italian_markets' with sorting rules for '.borsa' (to 'stock_exchange') and '.obbligazioni' (to 'bond_markets'). CONSOB compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#consob-markets' channel that the task is complete. Execute reorganization ensuring these Italian market supervisory standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/consob/italian_markets",
                    "sort_rules": {
                        "borsa": "stock_exchange",
                        "obbligazioni": "bond_markets",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_040",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /consob/italian_markets.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/consob/italian_markets"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/consob/italian_markets"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/consob/italian_markets",
                    "sort_rules": {
                        "borsa": "stock_exchange",
                        "obbligazioni": "bond_markets",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_040",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /consob/italian_markets after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#consob-markets",
                    "message": "Task F_ADJ_040 (File Tree Adjustment) complete. All files from /var/log have been moved to /consob/italian_markets and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_075",
        instruction=(
            "Perform archival process meeting CSSF Luxembourg audit requirements for Task ID ARCH_037. Archive '/luxembourg/cssf/ucits_funds.csv' and '/luxembourg/cssf/aifmd_reports.json' into 'cssf_funds_backup.tar.gz' for destination 'cssf-compliant.lu:/funds/archives'. The CSSF regulatory framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#cssf-funds' reading 'Task ARCH_037 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "cssf_funds_backup.tar.gz",
                    "destination_directory": "/funds/archives",
                    "remote_address": "cssf-compliant.lu",
                    "files_to_archive": [
                        "/luxembourg/cssf/ucits_funds.csv",
                        "/luxembourg/cssf/aifmd_reports.json",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/luxembourg/cssf/ucits_funds.csv",
                        "/luxembourg/cssf/aifmd_reports.json",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_037",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#cssf-funds",
                    "message": "Task ARCH_037 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/luxembourg/cssf/ucits_funds.csv", "/luxembourg/cssf/aifmd_reports.json"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_076",
        instruction=(
            "Reorganize '/var/log' files to meet OSC compliance requirements for Task ID F_ADJ_041. Target location is '/osc/ontario_securities' with sorting rules for '.prospectus' (to 'disclosure_documents') and '.takeover' (to 'bid_circulars'). OSC compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#osc-compliance' channel that the task is complete. Execute reorganization ensuring these Ontario securities commission standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/osc/ontario_securities",
                    "sort_rules": {
                        "prospectus": "disclosure_documents",
                        "takeover": "bid_circulars",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_041",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /osc/ontario_securities.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/osc/ontario_securities"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/osc/ontario_securities"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/osc/ontario_securities",
                    "sort_rules": {
                        "prospectus": "disclosure_documents",
                        "takeover": "bid_circulars",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_041",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /osc/ontario_securities after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#osc-compliance",
                    "message": "Task F_ADJ_041 (File Tree Adjustment) complete. All files from /var/log have been moved to /osc/ontario_securities and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_077",
        instruction=(
            "Perform archival process meeting DNB Netherlands audit requirements for Task ID ARCH_038. Archive '/netherlands/dnb/banking_license.json' and '/netherlands/dnb/prudential_data.csv' into 'dnb_supervision_backup.tar.gz' for destination 'dnb-compliant.nl:/supervision/archives'. The DNB regulatory framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#dnb-supervision' reading 'Task ARCH_038 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "dnb_supervision_backup.tar.gz",
                    "destination_directory": "/supervision/archives",
                    "remote_address": "dnb-compliant.nl",
                    "files_to_archive": [
                        "/netherlands/dnb/banking_license.json",
                        "/netherlands/dnb/prudential_data.csv",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/netherlands/dnb/banking_license.json",
                        "/netherlands/dnb/prudential_data.csv",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_038",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#dnb-supervision",
                    "message": "Task ARCH_038 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/netherlands/dnb/banking_license.json", "/netherlands/dnb/prudential_data.csv"]',
        ],
    ),
    Task(
    annotator="0",
    user_id="USER_078",
    instruction=(
        "Modify central task database by reorganizing '/var/log' to '/cbi/irish_logs' for CBI compliance audit through Task ID F_ADJ_042. Sort '.prism' files to 'regulatory_reporting' and '.mortgage' files to 'lending_measures'. To pass, update the database with a log stating 'Reorganized 3 files from /var/log to /cbi/irish_logs after successful pre-flight checks.'. The notification to '#cbi-compliance' must also be exactly 'Task F_ADJ_042 (File Tree Adjustment) complete. All files from /var/log have been moved to /cbi/irish_logs and sorted.'."
    ),
    actions=[
        Action(
            name="ParseDirectoryRestructureInstructions",
            kwargs={
                "target_directory": "/var/log",
                "destination_directory": "/cbi/irish_logs",
                "sort_rules": {
                    "prism": "regulatory_reporting",
                    "mortgage": "lending_measures",
                },
            },
        ),
        Action(
            name="CreateFileListForMove",
            kwargs={"target_directory": "/var/log"},
        ),
        Action(name="PopulateChecksumsInFileList", kwargs={}),
        Action(
            name="ComputeAndResolveDestinationPaths",
            kwargs={
                "destination_directory": "/cbi/irish_logs",
                "sort_rules": {
                    "prism": "regulatory_reporting",
                    "mortgage": "lending_measures",
                },
            },
        ),
        Action(name="CopyAndVerifyFiles", kwargs={}),
        Action(
            name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "F_ADJ_042",
                "task_name": "File Tree Adjustment",
                "result": "Success",
                "notes": "Reorganized 3 files from /var/log to /cbi/irish_logs after successful pre-flight checks.",
            },
        ),
        Action(
            name="SendSlackNotification",
            kwargs={
                "channel": "#cbi-compliance",
                "message": "Task F_ADJ_042 (File Tree Adjustment) complete. All files from /var/log have been moved to /cbi/irish_logs and sorted.",
            },
        ),
    ],
    outputs=[
        '"status": "success"',
        '"verified_and_copied": 3',
        '"cleaned_files_count": 3',
    ],
),
    Task(
        annotator="0",
        user_id="USER_079",
        instruction=(
            "Perform archival process meeting FINMA Swiss regulatory audit requirements for Task ID ARCH_039. Archive '/switzerland/finma/banking_ordinance.pdf' and '/switzerland/finma/insurance_supervision.json' into 'finma_regulatory_backup.tar.gz' for destination 'finma-compliant.ch:/regulatory/archives'. The FINMA regulatory framework requires that any workflow failure due to missing source files must be properly documented in central task database. Specifically, the audit system expects to find a database log entry with note 'Workflow terminated due to missing source files.' and a notification to '#finma-regulatory' reading 'Task ARCH_039 failed: Source files not found.' when files cannot be located. Execute the archival while ensuring these database audit requirements are satisfied."
        ),
        actions=[
            Action(
                name="ParseArchiveInstructions",
                kwargs={
                    "archive_name": "finma_regulatory_backup.tar.gz",
                    "destination_directory": "/regulatory/archives",
                    "remote_address": "finma-compliant.ch",
                    "files_to_archive": [
                        "/switzerland/finma/banking_ordinance.pdf",
                        "/switzerland/finma/insurance_supervision.json",
                    ],
                },
            ),
            Action(
                name="ValidateFilesExist",
                kwargs={
                    "file_paths": [
                        "/switzerland/finma/banking_ordinance.pdf",
                        "/switzerland/finma/insurance_supervision.json",
                    ]
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "ARCH_039",
                    "task_name": "File Archival",
                    "result": "Failure",
                    "notes": "Workflow terminated due to missing source files.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#finma-regulatory",
                    "message": "Task ARCH_039 failed: Source files not found.",
                },
            ),
        ],
        outputs=[
            '"status": "failed"',
            '"missing_files": ["/switzerland/finma/banking_ordinance.pdf", "/switzerland/finma/insurance_supervision.json"]',
        ],
    ),
    Task(
        annotator="0",
        user_id="USER_080",
        instruction=(
            "Reorganize '/var/log' files to meet RBA compliance requirements for Task ID F_ADJ_043. Target location is '/rba/austrian_logs' with sorting rules for '.wien' (to 'vienna_branch') and '.salzburg' (to 'regional_offices'). RBA compliance validation system requires central task database to contain evidence of plan registration and successful completion showing 3 files were processed. Send notification to '#rba-compliance' channel that the task is complete. Execute reorganization ensuring these Austrian banking regulatory standards are satisfied."
        ),
        actions=[
            Action(
                name="ParseDirectoryRestructureInstructions",
                kwargs={
                    "target_directory": "/var/log",
                    "destination_directory": "/rba/austrian_logs",
                    "sort_rules": {
                        "wien": "vienna_branch",
                        "salzburg": "regional_offices",
                    },
                },
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_043",
                    "task_name": "File Tree Adjustment",
                    "result": "Plan Registered",
                    "notes": "Registering plan: Move /var/log to /rba/austrian_logs.",
                },
            ),
            Action(
                name="CreateFileListForMove",
                kwargs={"target_directory": "/var/log"},
            ),
            Action(name="GetDiskSpace", kwargs={"path": "/rba/austrian_logs"}),
            Action(name="CalculateTotalSize", kwargs={}),
            Action(
                name="VerifySpaceRequirements",
                kwargs={"destination_path": "/rba/austrian_logs"},
            ),
            Action(name="PopulateChecksumsInFileList", kwargs={}),
            Action(
                name="ComputeAndResolveDestinationPaths",
                kwargs={
                    "destination_directory": "/rba/austrian_logs",
                    "sort_rules": {
                        "wien": "vienna_branch",
                        "salzburg": "regional_offices",
                    },
                },
            ),
            Action(name="CopyAndVerifyFiles", kwargs={}),
            Action(
                name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
            ),
            Action(
                name="LogTaskCompletion",
                kwargs={
                    "task_id": "F_ADJ_043",
                    "task_name": "File Tree Adjustment",
                    "result": "Success",
                    "notes": "Reorganized 3 files from /var/log to /rba/austrian_logs after successful pre-flight checks.",
                },
            ),
            Action(
                name="SendSlackNotification",
                kwargs={
                    "channel": "#rba-compliance",
                    "message": "Task F_ADJ_043 (File Tree Adjustment) complete. All files from /var/log have been moved to /rba/austrian_logs and sorted.",
                },
            ),
        ],
        outputs=[
            '"status": "success"',
            '"verified_and_copied": 3',
            '"cleaned_files_count": 3',
        ],
    ),
    Task(
    annotator="0",
    user_id="USER_081",
    instruction=(
        "Ensure SEC compliance for Task ID SCAN_001 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_082",
    instruction=(
        "Ensure GDPR compliance for Task ID SCAN_002 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_083",
    instruction=(
        "Ensure HIPAA compliance for Task ID SCAN_003 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_084",
    instruction=(
        "Ensure SOX compliance for Task ID SCAN_004 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_085",
    instruction=(
        "Ensure PCI-DSS compliance for Task ID SCAN_005 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_086",
    instruction=(
        "Ensure ISO27001 compliance for Task ID SCAN_006 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_087",
    instruction=(
        "Ensure FERPA compliance for Task ID SCAN_007 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_088",
    instruction=(
        "Ensure CCPA compliance for Task ID SCAN_008 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_089",
    instruction=(
        "Ensure NIST compliance for Task ID SCAN_009 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_090",
    instruction=(
        "Ensure HIPAA compliance for Task ID SCAN_010 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
    Task(
    annotator="0",
    user_id="USER_091",
    instruction=(
        "Ensure PCI-DSS compliance for Task ID SCAN_010 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_092",
    instruction=(
        "Ensure SOX compliance for Task ID SCAN_011 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_093",
    instruction=(
        "Ensure GDPR compliance for Task ID SCAN_012 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_094",
    instruction=(
        "Ensure FISMA compliance for Task ID SCAN_013 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_095",
    instruction=(
        "Ensure GLBA compliance for Task ID SCAN_014 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_096",
    instruction=(
        "Ensure COPPA compliance for Task ID SCAN_015 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
    Task(
    annotator="0",
    user_id="USER_097",
    instruction=(
        "Update central task log database by performing a file reorganization of '/var/log' to '/processed/logs' for Task ID F_ADJ_002. Sort files with a '.log' extension into a 'system' subdirectory and '.gz' files into 'archived'. For compliance audit approval, ensure the database is modified with a final completion log containing the exact note 'Reorganized 3 files from /var/log to /processed/logs after successful pre-flight checks.'. The final notification to '#ops-alerts' must also exactly match 'Task F_ADJ_002 (File Tree Adjustment) complete. All files from /var/log have been moved to /processed/logs and sorted.'."
    ),
    actions=[
        Action(
            name="ParseDirectoryRestructureInstructions",
            kwargs={
                "target_directory": "/var/log",
                "destination_directory": "/processed/logs",
                "sort_rules": {"log": "system", "gz": "archived"},
            },
        ),
        Action(
            name="CreateFileListForMove",
            kwargs={"target_directory": "/var/log"},
        ),
        Action(name="PopulateChecksumsInFileList", kwargs={}),
        Action(
            name="ComputeAndResolveDestinationPaths",
            kwargs={
                "destination_directory": "/processed/logs",
                "sort_rules": {"log": "system", "gz": "archived"},
            },
        ),
        Action(name="CopyAndVerifyFiles", kwargs={}),
        Action(
            name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "F_ADJ_002",
                "task_name": "File Tree Adjustment",
                "result": "Success",
                "notes": "Reorganized 3 files from /var/log to /processed/logs after successful pre-flight checks.",
            },
        ),
        Action(
            name="SendSlackNotification",
            kwargs={
                "channel": "#ops-alerts",
                "message": "Task F_ADJ_002 (File Tree Adjustment) complete. All files from /var/log have been moved to /processed/logs and sorted.",
            },
        ),
    ],
    outputs=[
        '"status": "success"',
        '"verified_and_copied": 3',
        '"cleaned_files_count": 3',
    ],
),
Task(
    annotator="0",
    user_id="USER_098",
    instruction=(
        "Modify central audit database by conducting a reorganization of '/var/log' to '/data/audited_logs' for Task ID F_ADJ_003. Sorting rules are to place 'syslog' files into 'system_events' and 'auth.log' files into 'security_events'. For audit approval, update the database with a final completion log containing the exact note 'Organized audit-relevant log files from /var/log.'. The policy additionally requires a final notification to the '#security-audits' channel with the precise message: 'Task F_ADJ_003 (File Tree Adjustment) complete. System log files in /var/log have been successfully organized for audit.'."
    ),
    actions=[
        Action(
            name="ParseDirectoryRestructureInstructions",
            kwargs={
                "target_directory": "/var/log",
                "destination_directory": "/data/audited_logs",
                "sort_rules": {
                    "syslog": "system_events",
                    "auth.log": "security_events",
                },
            },
        ),
        Action(
            name="CreateFileListForMove",
            kwargs={"target_directory": "/var/log"},
        ),
        Action(name="PopulateChecksumsInFileList", kwargs={}),
        Action(
            name="ComputeAndResolveDestinationPaths",
            kwargs={
                "destination_directory": "/data/audited_logs",
                "sort_rules": {
                    "syslog": "system_events",
                    "auth.log": "security_events",
                },
            },
        ),
        Action(name="CopyAndVerifyFiles", kwargs={}),
        Action(
            name="CleanOriginalDirectory", kwargs={"target_directory": "/var/log"}
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "F_ADJ_003",
                "task_name": "File Tree Adjustment",
                "result": "Success",
                "notes": "Organized audit-relevant log files from /var/log.",
            },
        ),
        Action(
            name="SendSlackNotification",
            kwargs={
                "channel": "#security-audits",
                "message": "Task F_ADJ_003 (File Tree Adjustment) complete. System log files in /var/log have been successfully organized for audit.",
            },
        ),
    ],
    outputs=[
        '"status": "success"',
        '"verified_and_copied": 3',
    ],
),
   Task(
    annotator="0",
    user_id="USER_099",
    instruction=(
        "Ensure ISO 27001 compliance for Task ID SCAN_025 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
),
Task(
    annotator="0",
    user_id="USER_100",
    instruction=(
        "Ensure HIPAA compliance for Task ID SCAN_027 by processing the first incomplete task from the `file_check_db`. Connect to the designated server, execute a file scan based on all specified criteria, and verify the integrity of the resulting log file. Conclude by updating the task's status in the database and cleaning up remote artifacts."
    ),
    actions=[
        Action(name="ScanIncompleteTasks", kwargs={}),
        Action(
            name="CheckSshConnection",
            kwargs={"remote_address": "server-prod-01.company.com"},
        ),
        Action(
            name="FindAndStatFiles",
            kwargs={
                "target_directory": "/var/log/applications",
                "last_access_days": 7,
            },
        ),
        Action(
            name="FilterFileLog",
            kwargs={
                "log_name": "file_check_log.json",
                "max_size": 52428800,
                "users": ["web_service"],
            },
        ),
        Action(name="ComputeChecksum", kwargs={"log_name": "file_check_log.json"}),
        Action(
            name="CopyFileToHost", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="VerifyLocalChecksum", kwargs={"log_name": "file_check_log.json"}
        ),
        Action(
            name="RemoteCleanup",
            kwargs={
                "files_to_delete": [
                    "file_check_log.json",
                    "file_check_log.json.sha256",
                ],
            },
        ),
        Action(
            name="UpdateTaskStatus",
            kwargs={"task_id": "fc_task_001", "completed": True},
        ),
        Action(
            name="LogTaskCompletion",
            kwargs={
                "task_id": "fc_task_001",
                "task_name": "Weekly Log Analysis",
                "result": "Success",
            },
        ),
    ],
    outputs=[
        '"copied_files": ["local_file_check_log.json", "local_file_check_log.json.sha256"]',
    ],
)
]