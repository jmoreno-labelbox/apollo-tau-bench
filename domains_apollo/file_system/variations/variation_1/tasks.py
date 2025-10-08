# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "USER_106",
        "instruction": "As a Security Analyst working on assignment 'SEC-REVIEW-CONFIG-01', your goal is to segregate potentially sensitive configuration files from the ongoing file organization job 'dir_op_001' for security assessment purposes. You need to locate all '.dat' and '.json' files listed in the operation manifest on 'server-data-01.company.com'. Rather than permitting them to undergo standard sorting, you must quarantine these files by transferring them to a newly created secure directory at '/secure/quarantine/config_review_20240120/'. Your responsibilities encompass complete task execution, including database updates to reflect moved file statuses and documenting the successful quarantine process.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/secure/quarantine/config_review_20240120"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/secure/quarantine/config_review_20240120/inventory.dat"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/secure/quarantine/config_review_20240120/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "SEC-REVIEW-CONFIG-01",
                    "task_type": "security_quarantine",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"dir_op_001\"",
                "\"files_identified_for_quarantine\": 2",
                "\"quarantine_directory_created\": true",
                "\"files_moved_to_quarantine\": 2",
                "\"original_task_files_updated\": 2",
                "\"quarantine_task_logged\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_104",
        "instruction": "As a Data Analyst Support Specialist working on 'PRIORITY-REVIEW-001', urgent analysis work demands immediate access to all CSV files from the queued sorting operation 'dir_op_001'. Your task is to capture these specific files before processing. You must locate all CSV files within the operation's manifest on 'server-data-01.company.com'. Rather than allowing them to continue to their standard sorting location, you need to move all identified CSV files to a newly established priority review directory at '/data/priority_review/20240120/'. Your duties include complete task execution, database modifications to update moved file statuses within the original 'dir_op_001' workflow, and recording the successful staging operation.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/priority_review/20240120"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/priority_review/20240120/sales_data.csv"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/priority_review/20240120/customer_info.csv"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/priority_review/20240120/data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "PRIORITY-REVIEW-001",
                    "task_type": "data_staging",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"dir_op_001\"",
                "\"files_identified_for_staging\": 3",
                "\"staging_directory_created\": true",
                "\"files_moved_to_staging\": 3",
                "\"original_task_files_updated\": 3",
                "\"staging_task_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_099",
        "instruction": "As a Data Analyst Support Specialist working on 'PRIORITY-REVIEW-001', urgent analysis work demands immediate access to all CSV files from the queued sorting operation 'dir_op_001'. Your task is to capture these specific files before processing. You must locate all CSV files within the operation's manifest on 'server-data-01.company.com'. Rather than allowing them to continue to their standard sorting location, you need to move all identified CSV files to a newly established priority review directory at '/data/priority_review/20240120/'. Your duties include complete task execution, database modifications to update moved file statuses within the original 'dir_op_001' workflow, recording the successful staging operation, and sending a slack message to the 'Operations' channel.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/priority_review/20240120"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/priority_review/20240120/sales_data.csv"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/priority_review/20240120/customer_info.csv"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/priority_review/20240120/data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "PRIORITY-REVIEW-001",
                    "task_type": "data_staging",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"dir_op_001\"",
                "\"files_identified_for_staging\": 3",
                "\"staging_directory_created\": true",
                "\"files_moved_to_staging\": 3",
                "\"original_task_files_updated\": 3",
                "\"staging_task_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_079",
        "instruction": "As a Data Archival Specialist working on 'EOY-REPORTS-ARCHIVAL-01', you must handle the year-end procedure by transferring all recent financial reports to a permanent archive location. Prior to any file operations, conduct a comprehensive System Readiness Assessment. This involves executing Pre-Execution File Transfer Security Clearance protocols for the user linked to the audit task ('user_003') and confirming that the target server 'server-analytics.company.com' is operational with adequate disk space. Upon successful completion of all checks, identify all reports meeting the criteria specified in 'fc_task_003' and transfer them to a newly created permanent directory at '/analytics/final_reports/2023/'. Your responsibilities include complete task execution, database modifications to update the underlying audit task status, logging the successful archival operation, and sending a slack message to the 'Operations' channel.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_003"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "carol_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-analytics.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-analytics.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "directory": "/analytics/reports"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "directory_path": "/analytics/final_reports/2023"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "source_path": "/analytics/reports/daily_sales_report.csv",
                    "destination_path": "/analytics/final_reports/2023/daily_sales_report.csv"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "source_path": "/analytics/reports/monthly_trends.csv",
                    "destination_path": "/analytics/final_reports/2023/monthly_trends.csv"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_003",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "EOY-REPORTS-ARCHIVAL-01",
                    "task_type": "data_archival",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"fc_task_003\"",
                "\"security_clearance_status\": \"passed\"",
                "\"server_status\": \"online\"",
                "\"disk_space_ok\": true",
                "\"files_identified_for_archival\": 2",
                "\"archive_directory_created\": true",
                "\"files_moved_to_archive\": 2",
                "\"original_task_status_updated\": true",
                "\"archival_task_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_074",
        "instruction": "As an Incident Commander performing a comprehensive post-mortem analysis on the failed archive task 'arch_005', you must determine the technical root cause of the failure and execute a mandatory security review of the original operation based on the user's role. Document your findings for both the technical failure and any identified security violations using the original task ID. Complete the process by sending a detailed incident report to 'System Alerts', notifying the responsible user ('user_004') and all system administrators ('user_001', 'user_005') with the message: 'Post-mortem for arch_005 COMPLETE. Technical failure: Insufficient storage. Security review: Critical policy violation found. User: @dave.intern. See logs for details. cc @alice.admin @eve.manager'",
        "actions": [
            {
                "name": "GetErrorLogDetails",
                "arguments": {
                    "task_id": "arch_005"
                },
            },
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_005"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "dave_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_005",
                    "task_type": "post_mortem",
                    "user_id": "user_004",
                    "error_type": "insufficient_remote_storage",
                    "severity": "medium",
                    "details_json": {
                        "reason": "Insufficient storage space on remote server personal-backup.company.com."
                    }
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_005",
                    "task_type": "security_review",
                    "user_id": "user_004",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User 'user_004' (intern) attempted access to unauthorized server 'personal-backup.company.com'."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Post-mortem for arch_005 COMPLETE. Technical failure: Insufficient storage. Security review: Critical policy violation found. User: @dave.intern. See logs for details. cc @alice.admin @eve.manager"
                }
            }
        ],
        "outputs": [
                "\"incident_task_id\": \"arch_005\"",
                "\"technical_root_cause\": \"Insufficient storage space\"",
                "\"security_review_status\": \"failed\"",
                "\"policy_violation_confirmed\": true",
                "\"technical_error_logged\": true",
                "\"security_error_logged\": true",
                "\"user_contact\": \"@ethan.intern\"",
                "\"admin_1_contact\": \"@maya.admin\"",
                "\"admin_2_contact\": \"@aria.manager\"",
                "\"slack_report_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_021",
        "instruction": "Complete file audit 'fc_task_003' following Standard File Check practices while maintaining secure data handling throughout the entire workflow. Archive and transfer the audit scan findings from 'server-analytics.company.com' to '/storage/file_check_results/' on 'storage-01.company.com', ensuring transfer integrity validation. After the transfer, perform necessary cleanup, log the delivery against the original task ID, and send final confirmation to the 'Operations' channel upon full audit completion.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_003"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-analytics.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "directory": "/analytics/reports"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_003",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_003",
                    "task_type": "file_check",
                    "user_id": "user_003"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "File Check"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "storage-01.company.com"
                },
            },
            {
                "name": "CreateArchiveOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "archive_path": "/tmp/fc_task_003_results.tar.gz",
                    "files_to_include": [
                        "/analytics/reports/daily_sales_report.csv",
                        "/analytics/reports/monthly_trends.csv"
                    ]
                },
            },
            {
                "name": "TransferFileToRemote",
                "arguments": {
                    "source_path": "/tmp/fc_task_003_results.tar.gz",
                    "remote_address": "storage-01.company.com",
                    "destination_path": "/storage/file_check_results/fc_task_003_results.tar.gz",
                    "ssh_key": "carol_rsa_key"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "filepath": "/tmp/fc_task_003_results.tar.gz"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_003",
                    "task_type": "results_delivery",
                    "user_id": "user_003"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"file_check_complete\": true",
                "\"file_check_logged\": true",
                "\"file_check_notification_sent\": true",
                "\"results_archive_created\": true",
                "\"transfer_complete_and_verified\": true",
                "\"source_cleanup_complete\": true",
                "\"delivery_logged\": true",
                "\"final_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_049",
        "instruction": "Conduct post-mortem security review 'SEC-REV-005' for the failed archive task 'arch_005' initiated by 'user_004' targeting 'personal-backup.company.com'. Execute comprehensive Pre-Execution Security Clearance practices on the original task parameters to identify any security policy violations that occurred before the storage error. Upon confirming a violation, log a new, separate 'critical' 'permission_denied' security violation error using the review ID. Escalate the findings to system administrators ('user_001', 'user_005') through the 'System Alerts' channel with this exact message: 'CRITICAL SECURITY VIOLATION (SEC-REV-005): User @dave.intern (role: intern) attempted unauthorized archive operation to personal-backup.company.com. Key 'dave_rsa_key' is not authorized. cc @alice.admin @eve.manager'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_005"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "dave_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "SEC-REV-005",
                    "task_type": "security_review",
                    "user_id": "user_004",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User 'user_004' (intern) with key 'dave_rsa_key' attempted access to unauthorized server 'personal-backup.company.com'."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "CRITICAL SECURITY VIOLATION (SEC-REV-005): User @dave.intern (role: intern) attempted unauthorized archive operation to personal-backup.company.com. Key 'dave_rsa_key' is not authorized. cc @alice.admin @eve.manager"
                }
            }
        ],
        "outputs": [
                "\"review_id\": \"SEC-REV-005\"",
                "\"original_task_id\": \"arch_005\"",
                "\"policy_violation_confirmed\": true",
                "\"violating_user\": \"user_004\"",
                "\"unauthorized_server\": \"personal-backup.company.com\"",
                "\"security_error_logged\": true",
                "\"admin_1_contact\": \"@maya.admin\"",
                "\"admin_2_contact\": \"@aria.manager\"",
                "\"escalation_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_047",
        "instruction": "Execute the secure lifecycle for archive task 'arch_001' by ensuring all pre-flight security and readiness checks pass on target server 'backup-server.company.com' before initiating any archival activity. Once validated, you must oversee execution of the Secure Archive Creation practices so that a complete archive is generated and transferred. The transfer process must include integrity verification to guarantee that the archive arrives intact. After successful confirmation, the source system 'server-prod-01.company.com' must be left clean and free of temporary artifacts, the task formally marked as completed, and the operation recorded for audit purposes. A clear completion notice must be issued to the 'Operations' channel summarizing that the archive was secured, validated, cleaned up, and finalized according to policy. The expected outcome is that all validations are passed, the archive is created and transferred with integrity confirmed, the source is cleared, the task is updated and logged, and the Operations team is notified.",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "alice_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "backup-server.company.com"
                },
            },
            {
                "name": "CreateArchiveOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "archive_path": "/tmp/project_backup_2024.tar.gz",
                    "files_to_include": [
                        "/home/projects/webapp/src/main.js",
                        "/home/projects/webapp/src/utils.js",
                        "/home/projects/webapp/config/database.json",
                        "/home/projects/webapp/docs/readme.md",
                        "/home/projects/webapp/tests/unit_tests.py"
                    ]
                },
            },
            {
                "name": "TransferFileToRemote",
                "arguments": {
                    "source_path": "/tmp/project_backup_2024.tar.gz",
                    "remote_address": "backup-server.company.com",
                    "destination_path": "/tmp/archives/project_backup_2024.tar.gz",
                    "ssh_key": "alice_rsa_key"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/tmp/project_backup_2024.tar.gz"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_001",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "arch_001",
                    "task_type": "archive",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"archive_id\": \"arch_001\"",
                "\"security_clearance\": \"passed\"",
                "\"disk_space_ok\": true",
                "\"archive_created\": true",
                "\"transfer_complete\": true",
                "\"checksum_verified\": true",
                "\"source_cleanup_complete\": true",
                "\"task_status_updated\": \"completed\"",
                "\"completion_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_035",
        "instruction": "As an Automated Data Librarian, execute the file organization mandate 'dir_op_001' securely and completely. Begin by confirming that the requesting user ('user_002') has valid security clearance for the target server 'server-data-01.company.com'. After authorization is verified, perform the complete file organization process by relocating all files in the operation manifest to their correct destination subdirectories on the target server, creating necessary directory structures where they do not exist. Update each processed file's operation status to reflect successful completion. Conclude the operation by sending a success notification to the 'Operations' channel. The final outcome should demonstrate that security was verified, all directories were prepared, all files were moved, statuses were updated, and the final notification was sent.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/csv"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/dat"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/json"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/miscellaneous"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/sorted/csv/sales_data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/sorted/csv/customer_info.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/data/sorted/dat/inventory.dat"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/data/sorted/json/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/readme.txt",
                    "destination_path": "/data/sorted/miscellaneous/readme.txt"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/sorted/csv/data_0.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"operation_id\": \"dir_op_001\"",
                "\"security_clearance\": \"passed\"",
                "\"files_to_process\": 6",
                "\"directories_created\": 4",
                "\"files_moved\": 6",
                "\"all_statuses_updated\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_045",
        "instruction": "A critical, multi-server data synchronization operation for 'user_003' requires immediate pre-flight coordination. Conduct a comprehensive 'System Readiness Assessment' across all participating servers: 'server-data-01.company.com' and 'server-analytics.company.com', following standard operational protocols. For each server, validate that it is online, has at least 100GB of available disk space, and that the user's default SSH key is explicitly authorized for access. If all checks pass for all servers, you must log the successful assessment under the task ID 'readiness_check_user_003' and notify the 'Operations' channel with the message: 'System readiness assessment for user_003 sync operation passed. All target servers are online, have sufficient disk space, and user is authorized. Ready to proceed.'",
        "actions": [
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "carol_rsa_key"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-analytics.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-analytics.company.com"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "readiness_check_user_003",
                    "task_type": "readiness_check",
                    "user_id": "user_003"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "System readiness assessment for user_003 sync operation passed. All target servers are online, have sufficient disk space, and user is authorized. Ready to proceed."
                }
            }
        ],
        "outputs": [
                "\"user_key_id\": \"carol_rsa_key\"",
                "\"server_1_status\": \"online\"",
                "\"server_1_disk_ok\": true",
                "\"server_1_auth_ok\": true",
                "\"server_2_status\": \"online\"",
                "\"server_2_disk_ok\": true",
                "\"server_2_auth_ok\": true",
                "\"overall_readiness\": \"passed\"",
                "\"assessment_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_084",
        "instruction": "Respond to security incident 'INCIDENT-LOG-ISOLATION-01' by immediately isolating and containing recent application logs on 'server-prod-01.company.com'. Follow secure evidence collection protocols under Project Manager ('user_005') authority. Identify all target log files matching criteria from 'fc_task_001', then create a secure archive of these logs and transfer it to the central evidence locker at '/storage/incident_evidence/' on 'backup-server.company.com'. Purge the original source log files from the production server as a containment measure. Complete the task by updating the original file check task status in the database and logging the successful evidence isolation.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "eve_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "directory": "/var/log/applications"
                },
            },
            {
                "name": "CreateArchiveOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "archive_path": "/tmp/INCIDENT-LOG-ISOLATION-01.tar.gz",
                    "files_to_include": [
                        "/var/log/applications/webapp.log",
                        "/var/log/applications/api_requests.log",
                        "/var/log/applications/error.log"
                    ]
                },
            },
            {
                "name": "TransferFileToRemote",
                "arguments": {
                    "source_path": "/tmp/INCIDENT-LOG-ISOLATION-01.tar.gz",
                    "remote_address": "backup-server.company.com",
                    "destination_path": "/storage/incident_evidence/INCIDENT-LOG-ISOLATION-01.tar.gz",
                    "ssh_key": "eve_rsa_key"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/var/log/applications/webapp.log"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/var/log/applications/api_requests.log"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/var/log/applications/error.log"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_001",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "INCIDENT-LOG-ISOLATION-01",
                    "task_type": "forensics",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"fc_task_001\"",
                "\"security_clearance_status\": \"passed\"",
                "\"server_status\": \"online\"",
                "\"files_identified_for_isolation\": 3",
                "\"evidence_archive_created\": true",
                "\"evidence_transfer_successful\": true",
                "\"source_files_purged\": 3",
                "\"original_task_status_updated\": true",
                "\"forensics_task_logged\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_060",
        "instruction": "Execute file organization mandate 'dir_op_001' by first conducting a comprehensive System Readiness Assessment. Ensure the requesting user ('user_002') is fully authorized for the target server ('server-data-01.company.com') according to all security policies, and verify the server's resource health remains within the 80% utilization threshold. After all pre-flight checks pass, execute the complete file organization process. Conclude all operations by sending a final success notification to the 'Operations' channel.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/csv"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/dat"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/json"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/miscellaneous"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/sorted/csv/sales_data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/sorted/csv/customer_info.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/data/sorted/dat/inventory.dat"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/data/sorted/json/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/readme.txt",
                    "destination_path": "/data/sorted/miscellaneous/readme.txt"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/sorted/csv/data_0.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "dir_op_001",
                    "task_type": "file_organization",
                    "user_id": "user_002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"operation_id\": \"dir_op_001\"",
                "\"security_clearance_status\": \"passed\"",
                "\"server_health_status\": \"passed\"",
                "\"files_to_process\": 6",
                "\"directories_created\": 4",
                "\"files_moved\": 6",
                "\"all_statuses_updated\": true",
                "\"completion_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_078",
        "instruction": "Handle incident 'INCIDENT-LOG-ISOLATION-01' by immediately isolating recent application logs on 'server-prod-01.company.com' due to a potential security threat. Begin by performing Pre-Execution File Transfer Security Clearance practices for the project manager ('user_005') who authorized this action, if needed. Secure the logs for forensic analysis by identifying all target log files matching criteria from 'fc_task_001', then relocate all identified files to a newly created secure directory at '/var/forensics/incident_20240120/'. Complete the task by updating the original file check task status in the database and logging the successful isolation of the potentially compromised files.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "eve_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "directory": "/var/log/applications"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "directory_path": "/var/forensics/incident_20240120"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "source_path": "/var/log/applications/webapp.log",
                    "destination_path": "/var/forensics/incident_20240120/webapp.log"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "source_path": "/var/log/applications/api_requests.log",
                    "destination_path": "/var/forensics/incident_20240120/api_requests.log"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "source_path": "/var/log/applications/error.log",
                    "destination_path": "/var/forensics/incident_20240120/error.log"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_001",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "INCIDENT-LOG-ISOLATION-01",
                    "task_type": "forensics",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"fc_task_001\"",
                "\"security_clearance_status\": \"passed\"",
                "\"server_status\": \"online\"",
                "\"files_identified_for_isolation\": 3",
                "\"forensics_directory_created\": true",
                "\"files_moved_to_isolation\": 3",
                "\"original_task_status_updated\": true",
                "\"forensics_task_logged\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_072",
        "instruction": "Investigate root cause analysis 'RCA-STO-001' for the high disk usage alert on 'storage-01.company.com' to determine the underlying cause. Begin by confirming the server's live resource usage, then identify the most recently completed 'archive' task that targeted this server as the likely contributing factor. When your investigation confirms this correlation, log a new 'high' severity 'disk_space_warning' error using the RCA task ID, detailing the server, its usage percentage, and the contributing task ID. Complete the investigation by alerting administrators ('user_001', 'user_005') in 'System Alerts' with your findings using this message: 'RCA Complete (RCA-STO-001): High disk usage (82%) on storage-01.company.com correlated with task arch_002. @alice.admin @eve.manager please review.'",
        "actions": [
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "storage-01.company.com"
                },
            },
            {
                "name": "GetLastSuccessfulTaskRun",
                "arguments": {
                    "task_type": "archive"
                },
            },
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_002"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "RCA-STO-001",
                    "task_type": "forensics",
                    "user_id": "system_agent",
                    "error_type": "disk_space_warning",
                    "severity": "high",
                    "details_json": {
                        "server": "storage-01.company.com",
                        "usage_percent": 82,
                        "likely_cause_task": "arch_002"
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "RCA Complete (RCA-STO-001): High disk usage (82%) on storage-01.company.com correlated with task arch_002. @alice.admin @eve.manager please review."
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "RCA-STO-001",
                    "task_type": "investigation",
                    "user_id": "system_agent"
                }
            }
        ],
        "outputs": [
                "\"disk_usage_confirmed_percent\": 82",
                "\"last_archive_task\": \"arch_002\"",
                "\"correlation_confirmed\": true",
                "\"incident_log_created\": true",
                "\"admin_1_contact\": \"@maya.admin\"",
                "\"admin_2_contact\": \"@aria.manager\"",
                "\"slack_escalation_sent\": true",
                "\"investigation_complete_and_logged\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_024",
        "instruction": "Manage the data lifecycle for archival task 'arch_002', which has reached the cleanup stage. Use Archive Finalization Practices to retrieve the task record for 'arch_002' and identify the original source filepaths. Securely purge all of these original files from 'server-analytics.company.com'. After cleanup completion, update the archive record status to 'verified' in the system, confirming the entire lifecycle has been completed. Log this finalization for auditability. Close the process by notifying the Operations team through a confirmation message to the 'Operations' channel.",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_002"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "filepath": "/analytics/raw_data/user_events_2023.csv"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "filepath": "/analytics/raw_data/page_views_2023.csv"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "filepath": "/analytics/processed/monthly_reports_2023.json"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "filepath": "/analytics/processed/yearly_summary_2023.pdf"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_002",
                    "status": "verified"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "arch_002",
                    "task_type": "archive_cleanup",
                    "user_id": "user_003"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"archive_id\": \"arch_002\"",
                "\"source_files_deleted\": 4",
                "\"task_status_updated\": \"verified\"",
                "\"operation_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_030",
        "instruction": "The '/data/temp' directory on 'server-data-01.company.com' requires routine cleanup to manage disk space effectively. Apply Stale File Cleanup practices for maintenance task 'fc_task_002' by identifying and purging all files that violate the task's defined data retention and size policies. After completing the cleanup, formally mark the task as completed, log the operational success for auditing purposes, and report the results to the 'Operations' channel.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/temp_export_001.csv"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_002",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_002",
                    "task_type": "file_check",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"cleanup_task_id\": \"fc_task_002\"",
                "\"filters_applied\": [\"older_than_30_days\", \"max_size_100MB\"]",
                "\"files_identified_for_deletion\": 1",
                "\"file_deleted\": \"/data/temp/temp_export_001.csv\"",
                "\"cleanup_completed\": true",
                "\"task_status_updated\": true",
                "\"operation_logged\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_022",
        "instruction": "Execute the 'System Health Audit' identified as 'HEALTH-AUDIT-01' for primary data servers: 'server-data-01.company.com' and 'server-prod-01.company.com'. Verify that each server's disk usage remains below the operational threshold of 75%. Treat any threshold breach as a critical issue requiring immediate escalation to the 'System Alerts' channel and remediation through Stale File Cleanup practices defined in maintenance task 'fc_task_002'. After completing the audit and any corrective actions, ensure the entire process is properly logged under 'HEALTH-AUDIT-01' and provide the 'Operations' channel with a clear, comprehensive summary of the audit outcome, including any breaches detected and actions taken. The expected outcome is that all servers are audited, any issues are escalated and remediated according to policy, the audit is logged, and the final report is communicated.",
        "actions": [
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "HEALTH-AUDIT-01: Disk usage on server-data-01.company.com (78%) exceeds 75% threshold. Initiating cleanup."
                },
            },
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/temp_export_001.csv"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/cache_backup.dat"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_002",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "HEALTH-AUDIT-01",
                    "task_type": "system_health_audit",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "System Health Audit HEALTH-AUDIT-01 complete. server-data-01.company.com exceeded disk threshold and was remediated by purging 2 stale files. server-prod-01.company.com is healthy."
                }
            }
        ],
        "outputs": [
                "\"servers_checked\": 2",
                "\"threshold_breached_on\": \"server-data-01.company.com\"",
                "\"slack_alert_sent\": true",
                "\"cleanup_protocol_initiated\": true",
                "\"files_purged_count\": 2",
                "\"cleanup_task_status_updated\": true",
                "\"audit_operation_logged\": true",
                "\"slack_summary_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_012",
        "instruction": "Handle incident case 'INC-PERM-007' following the confirmation by security audit that user 'user_003' gained unauthorized access to 'server-data-01.company.com' using credential 'carol_rsa_key'. Respond to this incident by formally logging the violation and collecting forensic evidence from the compromised server's primary data directories: `/data/temp` and `/data/unsorted`. Preserve all collected evidence in an archive and securely transfer it under administrative account 'user_001' to '/storage/incident_evidence/' on 'backup-server.company.com'. Complete the incident response by notifying the Operations team through this structured message to the 'Operations' channel: 'Incident INC-PERM-007 remediated. Unauthorized access by user_003 on server-data-01.company.com has been logged. A full forensic archive of data directories has been created and stored for review.'",
        "actions": [
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "carol_rsa_key"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "INC-PERM-007",
                    "task_type": "incident_response",
                    "user_id": "user_003",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "user": "user_003",
                        "server": "server-data-01.company.com",
                        "reason": "Unauthorized key found during audit."
                    }
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/unsorted"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "CreateArchiveOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "archive_path": "/tmp/INC-PERM-007_evidence.tar.gz",
                    "files_to_include": [
                        "/data/temp/temp_export_001.csv",
                        "/data/temp/cache_backup.dat",
                        "/data/unsorted/sales_data.csv",
                        "/data/unsorted/customer_info.csv"
                    ]
                },
            },
            {
                "name": "TransferFileToRemote",
                "arguments": {
                    "source_path": "/tmp/INC-PERM-007_evidence.tar.gz",
                    "remote_address": "backup-server.company.com",
                    "destination_path": "/storage/incident_evidence/INC-PERM-007_evidence.tar.gz",
                    "ssh_key": "alice_rsa_key"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/tmp/INC-PERM-007_evidence.tar.gz"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "INC-PERM-007",
                    "task_type": "incident_response",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "Incident INC-PERM-007 remediated. Unauthorized access by user_003 on server-data-01.company.com has been logged. A full forensic archive of data directories has been created and stored for review."
                }
            }
        ],
        "outputs": [
                "\"incident_id\": \"INC-PERM-007\"",
                "\"violation_logged\": true",
                "\"directories_scanned\": 2",
                "\"files_inventoried\": 4",
                "\"admin_ssh_key_retrieved\": \"alice_rsa_key\"",
                "\"forensic_archive_created\": true",
                "\"evidence_transfer_complete\": true",
                "\"source_cleanup_complete\": true",
                "\"incident_response_logged\": true",
                "\"slack_summary_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_016",
        "instruction": "Conduct a pre-flight security audit for archive task 'arch_003' by enforcing all security protocols through the 'Pre-Execution File Transfer Security Clearance Protocol' for requesting user ('user_002') against target server 'log-storage.company.com'. When a security policy violation is discovered, follow standard practice for halting operations due to critical security failure, including updating all relevant database records and escalating the incident. Send this message to 'System Alerts' for escalation: 'Task arch_003 HALTED on security violation. User @bob.dev is not authorized for log-storage.company.com.'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_003"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_003",
                    "status": "failed"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_003",
                    "task_type": "security_audit",
                    "user_id": "user_002",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "Key 'bob_rsa_key' is not authorized for server 'log-storage.company.com' as per its authorized_servers list."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Task arch_003 HALTED on security violation. User @bob.dev is not authorized for log-storage.company.com."
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"arch_003\"",
                "\"user_role\": \"developer\"",
                "\"ssh_key_id\": \"bob_rsa_key\"",
                "\"authorization_check\": \"failed\"",
                "\"policy_violation_confirmed\": true",
                "\"task_status_updated\": \"failed\"",
                "\"security_error_logged\": true",
                "\"user_contact\": \"@ryan.dev\"",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_019",
        "instruction": "Ensure that source server ('server-prod-01.company.com') is in healthy state before proceeding with pending archive task 'arch_001' for user 'user_001'. Perform a required health check confirming that CPU, memory, and disk utilization are each below the 75% threshold. When the server meets these conditions, carry out the Secure Archive Creation protocol to completion. After the archive has been created and transferred successfully, finalize the task according to policy, including updating its status, logging completion, and sending a notification to the 'Operations' channel.",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "backup-server.company.com"
                },
            },
            {
                "name": "CreateArchiveOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "archive_path": "/tmp/project_backup_2024.tar.gz",
                    "files_to_include": [
                        "/home/projects/webapp/src/main.js",
                        "/home/projects/webapp/src/utils.js",
                        "/home/projects/webapp/config/database.json",
                        "/home/projects/webapp/docs/readme.md",
                        "/home/projects/webapp/tests/unit_tests.py"
                    ]
                },
            },
            {
                "name": "TransferFileToRemote",
                "arguments": {
                    "source_path": "/tmp/project_backup_2024.tar.gz",
                    "remote_address": "backup-server.company.com",
                    "destination_path": "/tmp/archives/project_backup_2024.tar.gz",
                    "ssh_key": "alice_rsa_key"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_001",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "arch_001",
                    "task_type": "archive",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"source_server_health_status\": \"healthy\"",
                "\"destination_disk_space_ok\": true",
                "\"archive_created\": true",
                "\"transfer_successful\": true",
                "\"task_status_updated\": true",
                "\"completion_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_020",
        "instruction": "You are an Incident Responder assigned to 'INC-ARCH-003'. The archive task 'arch_003' has been flagged due to a pre-execution failure. Your directive is to conduct a full 'Task Failure Diagnosis Protocol' to determine the root cause. If the failure is confirmed to be a security policy violation, you must perform a database write to log a new 'critical' 'permission_denied' error for this incident, update the original archive task's status to 'failed', and then escalate the finding. Your escalation must be sent to the 'System Alerts' channel, notifying the original user and all system administrators ('user_001', 'user_005') with the message: 'Incident INC-ARCH-003: Task arch_003 failed due to security policy violation. User @bob.dev (developer) is not authorized for log-storage.company.com. Task aborted. cc @alice.admin @eve.manager'",
        "actions": [
            {
                "name": "GetErrorLogDetails",
                "arguments": {
                    "task_id": "arch_003"
                },
            },
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_003"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "INC-ARCH-003",
                    "task_type": "incident_response",
                    "user_id": "user_002",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User 'user_002' with role 'developer' has no authorization for 'log-storage.company.com' per policy.",
                        "original_task": "arch_003"
                    }
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_003",
                    "status": "failed"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Incident INC-ARCH-003: Task arch_003 failed due to security policy violation. User @bob.dev (developer) is not authorized for log-storage.company.com. Task aborted. cc @alice.admin @eve.manager"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "INC-ARCH-003",
                    "task_type": "incident_response",
                    "user_id": "system_agent"
                }
            }
        ],
        "outputs": [
                "\"incident_id\": \"INC-ARCH-003\"",
                "\"root_cause_confirmed\": \"permission_denied\"",
                "\"policy_violation_found\": true",
                "\"error_log_created\": true",
                "\"original_task_status_updated\": \"failed\"",
                "\"user_notified\": \"@ryan.dev\"",
                "\"admins_notified\": true",
                "\"incident_response_logged\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_087",
        "instruction": "Conduct root cause analysis 'RCA-STO-001' for the high disk usage alert (82%) detected on 'storage-01.company.com'. Establish the current usage level on the server and determine whether a recently completed archive task contributed to this condition. Validate the most recent successful archive targeting this server, including retrieving its instructions to assess its contribution. When correlation is found, record the findings in the system by creating a 'disk_space_warning' entry under the RCA task ID with high severity. Include the affected server, its usage, the contributing task identifier, and the archive size in the error record. Communicate the RCA outcome to administrators ('user_001' and 'user_005') through the 'System Alerts' channel with an explicit message reporting the correlation and tagging @alice.admin and @eve.manager for review.",
        "actions": [
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "storage-01.company.com"
                },
            },
            {
                "name": "GetLastSuccessfulTaskRun",
                "arguments": {
                    "task_type": "archive"
                },
            },
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_002"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "RCA-STO-001",
                    "task_type": "forensics",
                    "user_id": "system_agent",
                    "error_type": "disk_space_warning",
                    "severity": "high",
                    "details_json": {
                        "server": "storage-01.company.com",
                        "usage_percent": 82,
                        "likely_cause_task": "arch_002",
                        "archive_size_display": "487.0MB"
                    }
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "RCA Complete (RCA-STO-001): High disk usage (82%) on storage-01.company.com correlated with task arch_002 (487.0MB). @alice.admin @eve.manager please review."
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "RCA-STO-001",
                    "task_type": "investigation",
                    "user_id": "system_agent"
                }
            }
        ],
        "outputs": [
                "\"disk_usage_confirmed_percent\": 82",
                "\"contributing_task_id\": \"arch_002\"",
                "\"correlation_confirmed\": true",
                "\"incident_log_created\": true",
                "\"admin_1_contact\": \"@maya.admin\"",
                "\"admin_2_contact\": \"@aria.manager\"",
                "\"slack_escalation_sent\": true",
                "\"investigation_complete_and_logged\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_089",
        "instruction": "Perform post-mortem security review 'SEC-REV-005' on the failed archive task 'arch_005' initiated by 'user_004' targeting 'personal-backup.company.com'. Execute the complete 'Pre-Execution Security Clearance Protocol' on the original task parameters to determine if a security policy was violated before the storage error occurred. Upon confirming a violation, log a new, separate 'critical' 'permission_denied' security violation error using the review ID. Escalate by notifying system administrators ('user_001', 'user_005') via the 'System Alerts' channel with this explicit message: 'CRITICAL SECURITY VIOLATION (SEC-REV-005): User @dave.intern (role: intern) attempted unauthorized archive operation to personal-backup.company.com. Key 'dave_rsa_key' is not authorized. cc @alice.admin @eve.manager'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_005"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "dave_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "SEC-REV-005",
                    "task_type": "security_review",
                    "user_id": "user_004",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User 'user_004' (intern) with key 'dave_rsa_key' attempted access to unauthorized server 'personal-backup.company.com'."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "CRITICAL SECURITY VIOLATION (SEC-REV-005): User @dave.intern (role: intern) attempted unauthorized archive operation to personal-backup.company.com. Key 'dave_rsa_key' is not authorized. cc @alice.admin @eve.manager"
                }
            }
        ],
        "outputs": [
                "\"review_id\": \"SEC-REV-005\"",
                "\"original_task_id\": \"arch_005\"",
                "\"policy_violation_confirmed\": true",
                "\"violating_user\": \"user_004\"",
                "\"unauthorized_server\": \"personal-backup.company.com\"",
                "\"security_error_logged\": true",
                "\"admin_1_contact\": \"@maya.admin\"",
                "\"admin_2_contact\": \"@aria.manager\"",
                "\"escalation_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_007",
        "instruction": "Handle security review assignment 'SEC-REVIEW-CONFIG-01' by isolating potentially sensitive configuration files from the pending file organization task 'dir_op_001'. Identify all '.dat' and '.json' files within the operation's manifest on 'server-data-01.company.com' and prevent them from being sorted. Quarantine these specific files by relocating them to a newly created secure directory at '/secure/quarantine/config_review_20240120/'. Execute the complete task, including database modifications to update moved file statuses and logging the successful quarantine operation.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/secure/quarantine/config_review_20240120"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/secure/quarantine/config_review_20240120/inventory.dat"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/secure/quarantine/config_review_20240120/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "SEC-REVIEW-CONFIG-01",
                    "task_type": "security_quarantine",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"dir_op_001\"",
                "\"files_identified_for_quarantine\": 2",
                "\"quarantine_directory_created\": true",
                "\"files_moved_to_quarantine\": 2",
                "\"original_task_files_updated\": 2",
                "\"quarantine_task_logged\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_063",
        "instruction": "Perform comprehensive Pre-Execution Security Clearance for pending archive task 'arch_004' as a Security Automation Engineer. Validate that the requesting user's role ('project_manager') has permitted access under the 'SSH Access Policy' and confirm the user's default SSH key is explicitly authorized for destination server 'document-vault.company.com'. When either validation fails, halt the operation by marking the archive task as 'failed', logging a 'critical' 'permission_denied' error with violation details, and sending a notification to the 'System Alerts' channel.",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_004"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "eve_rsa_key"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_004",
                    "status": "failed"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_004",
                    "task_type": "archive",
                    "user_id": "user_005",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "SSH key 'eve_rsa_key' is not authorized for destination server 'document-vault.company.com'."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"arch_004\"",
                "\"user_role_check\": \"passed\"",
                "\"ssh_key_check\": \"failed\"",
                "\"violating_key\": \"eve_rsa_key\"",
                "\"unauthorized_server\": \"document-vault.company.com\"",
                "\"task_status_updated\": \"failed\"",
                "\"security_error_logged\": true",
                "\"user_contact\": \"@aria.manager\"",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_036",
        "instruction": "Resolve maintenance task 'fc_task_002' by first performing comprehensive pre-flight readiness checks. Conduct Pre-Execution Security Clearance practices for designated user ('user_001') and verify the target server's operational status. When all checks pass, apply Stale File Cleanup Practices as needed, ensuring you purge only files that strictly match all policy filters defined within the task. Complete the process by notifying the 'File Check' channel with this message: 'Maintenance task fc_task_002 completed successfully. 1 stale file purged from /data/temp on server-data-01.company.com.'",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "alice_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/temp_export_001.csv"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_002",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_002",
                    "task_type": "file_check",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "File Check",
                    "message": "Maintenance task fc_task_002 completed successfully. 1 stale file purged from /data/temp on server-data-01.company.com."
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"fc_task_002\"",
                "\"security_clearance_status\": \"passed\"",
                "\"server_status\": \"online\"",
                "\"files_scanned\": 2",
                "\"files_matching_criteria\": 1",
                "\"files_deleted_count\": 1",
                "\"task_status_updated\": true",
                "\"completion_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_057",
        "instruction": "Isolate potentially sensitive configuration files from the pending file organization task 'dir_op_001' as part of security review 'SEC-REVIEW-CONFIG-01'. Identify all '.dat' and '.json' files within the operation's manifest on 'server-data-01.company.com' and prevent their standard sorting. Quarantine these specific files by relocating them to a newly established secure directory at '/secure/quarantine/config_review_20240120/'. Handle the complete task execution, including database modifications to update moved file statuses and logging the successful quarantine operation.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/secure/quarantine/config_review_20240120"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/secure/quarantine/config_review_20240120/inventory.dat"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/secure/quarantine/config_review_20240120/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "SEC-REVIEW-CONFIG-01",
                    "task_type": "security_quarantine",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"dir_op_001\"",
                "\"files_identified_for_quarantine\": 2",
                "\"quarantine_directory_created\": true",
                "\"files_moved_to_quarantine\": 2",
                "\"original_task_files_updated\": 2",
                "\"quarantine_task_logged\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_070",
        "instruction": "Execute file audit 'fc_task_003' and securely deliver the findings by first following the 'Standard File Check Protocol'. After completing the scan, archive the files found and securely transfer the resulting archive to '/storage/file_check_results/' on 'storage-01.company.com'. Confirm transfer integrity, perform cleanup of the temporary archive on the source server, log the delivery using the original task ID, and send final confirmation to 'Operations'.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_003"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-analytics.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "directory": "/analytics/reports"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_003",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_003",
                    "task_type": "file_check",
                    "user_id": "user_003"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "File Check"
                },
            },
            {
                "name": "CreateArchiveOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "archive_path": "/tmp/fc_task_003_results.tar.gz",
                    "files_to_include": [
                        "/analytics/reports/daily_sales_report.csv",
                        "/analytics/reports/monthly_trends.csv"
                    ]
                },
            },
            {
                "name": "TransferFileToRemote",
                "arguments": {
                    "source_path": "/tmp/fc_task_003_results.tar.gz",
                    "remote_address": "storage-01.company.com",
                    "destination_path": "/storage/file_check_results/fc_task_003_results.tar.gz",
                    "ssh_key": "carol_rsa_key"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "filepath": "/tmp/fc_task_003_results.tar.gz"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_003",
                    "task_type": "results_delivery",
                    "user_id": "user_003"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"file_check_complete\": true",
                "\"file_check_logged\": true",
                "\"file_check_notification_sent\": true",
                "\"results_archive_created\": true",
                "\"transfer_complete_and_verified\": true",
                "\"source_cleanup_complete\": true",
                "\"delivery_logged\": true",
                "\"final_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_038",
        "instruction": "Conduct 'Pre-Execution Security Clearance' for archive task 'arch_004' by validating both role-based and key-based authorization under the SSH Access Policy. Verify the requesting user's role ('project_manager') against the policy to ensure server access permission, and confirm the user's default SSH key is authorized for destination server ('document-vault.company.com'). When any violation is detected, record it as a critical permission error, reflect the failure in the task status, and escalate to the 'System Alerts' channel with this message: 'Task arch_004 HALTED on security violation. User @eve.manager's key 'eve_rsa_key' is not authorized for destination server 'document-vault.company.com'. Operation aborted.'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_004"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "eve_rsa_key"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_004",
                    "status": "failed"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_004",
                    "task_type": "archive",
                    "user_id": "user_005",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "SSH key 'eve_rsa_key' is not authorized for destination server 'document-vault.company.com'."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Task arch_004 HALTED on security violation. User @eve.manager's key 'eve_rsa_key' is not authorized for destination server 'document-vault.company.com'. Operation aborted."
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"arch_004\"",
                "\"user_role_check\": \"passed\"",
                "\"ssh_key_check\": \"failed\"",
                "\"violating_key\": \"eve_rsa_key\"",
                "\"unauthorized_server\": \"document-vault.company.com\"",
                "\"task_status_updated\": \"failed\"",
                "\"security_error_logged\": true",
                "\"user_contact\": \"@aria.manager\"",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_039",
        "instruction": "Oversee remediation of the failed archive task 'arch_005' by carrying out Task Failure Diagnosis practices to identify and record the root cause. During remediation planning, assess available storage capacity on alternative servers 'backup-server.company.com' and 'storage-01.company.com' to determine a viable destination. Log the chosen alternative and supporting diagnostic details as part of remediation analysis. Communicate a structured remediation plan to the 'Operations' channel with this message: 'Remediation Plan for arch_005: Retry task using 'backup-server.company.com' as the destination (4250GB available). cc @dave.intern', and finalize the incident with proper completion logging.",
        "actions": [
            {
                "name": "GetErrorLogDetails",
                "arguments": {
                    "task_id": "arch_005"
                },
            },
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_005"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "backup-server.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "storage-01.company.com"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_005",
                    "task_type": "remediation_analysis",
                    "user_id": "user_004",
                    "error_type": "remediation_analysis",
                    "severity": "medium",
                    "details_json": {
                        "root_cause": "Insufficient storage space on personal-backup.company.com",
                        "best_alternative_server": "backup-server.company.com",
                        "alternative_available_gb": 4250
                    }
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "Remediation Plan for arch_005: Retry task using 'backup-server.company.com' as the destination (4250GB available). cc @dave.intern"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "arch_005",
                    "task_type": "incident_response",
                    "user_id": "system_agent"
                }
            }
        ],
        "outputs": [
                "\"failed_task_id\": \"arch_005\"",
                "\"root_cause_identified\": \"Insufficient storage space on remote server\"",
                "\"user_contact\": \"@ethan.intern\"",
                "\"alternative_server_1_space\": 4250",
                "\"alternative_server_2_space\": 1800",
                "\"remediation_log_created\": true",
                "\"remediation_plan_sent\": true",
                "\"incident_fully_processed\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_009",
        "instruction": "Handle priority review assignment 'PRIORITY-REVIEW-001' requiring immediate access to all CSV files from pending sorting job 'dir_op_001'. Intercept these specific files by identifying all CSV files in the operation's manifest on 'server-data-01.company.com'. Prevent them from proceeding to the standard sorting destination by relocating all identified CSV files to a new priority review directory at '/data/priority_review/20240120/'. Execute the complete task, including database modifications to update moved file statuses within the original 'dir_op_001' mandate and logging the successful staging operation.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/priority_review/20240120"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/priority_review/20240120/sales_data.csv"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/priority_review/20240120/customer_info.csv"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/priority_review/20240120/data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "PRIORITY-REVIEW-001",
                    "task_type": "data_staging",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"dir_op_001\"",
                "\"files_identified_for_staging\": 3",
                "\"staging_directory_created\": true",
                "\"files_moved_to_staging\": 3",
                "\"original_task_files_updated\": 3",
                "\"staging_task_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_064",
        "instruction": "Conduct comprehensive post-mortem on failed archive task 'arch_005' through dual investigation following all appropriate protocols. Diagnose the technical root cause of the failure, then conduct mandatory security review of the original operation due to the user's role. Log findings for both the technical failure and any discovered security violations. Send comprehensive incident report to 'System Alerts', notifying responsible user ('user_004') and all system administrators ('user_001', 'user_005') with this message: 'Post-mortem for arch_005 COMPLETE. Technical failure: Insufficient storage. Security review: Critical policy violation found. User: @dave.intern. See logs for details. cc @alice.admin @eve.manager'",
        "actions": [
            {
                "name": "GetErrorLogDetails",
                "arguments": {
                    "task_id": "arch_005"
                },
            },
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_005"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "dave_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_005",
                    "task_type": "post_mortem",
                    "user_id": "user_004",
                    "error_type": "insufficient_remote_storage",
                    "severity": "medium",
                    "details_json": {
                        "reason": "Insufficient storage space on remote server personal-backup.company.com."
                    }
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_005",
                    "task_type": "security_review",
                    "user_id": "user_004",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User 'user_004' (intern) attempted access to unauthorized server 'personal-backup.company.com'."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Post-mortem for arch_005 COMPLETE. Technical failure: Insufficient storage. Security review: Critical policy violation found. User: @dave.intern. See logs for details. cc @alice.admin @eve.manager"
                }
            }
        ],
        "outputs": [
                "\"incident_task_id\": \"arch_005\"",
                "\"technical_root_cause\": \"Insufficient storage space\"",
                "\"security_review_status\": \"failed\"",
                "\"policy_violation_confirmed\": true",
                "\"technical_error_logged\": true",
                "\"security_error_logged\": true",
                "\"user_contact\": \"@ethan.intern\"",
                "\"admin_1_contact\": \"@maya.admin\"",
                "\"admin_2_contact\": \"@aria.manager\"",
                "\"slack_report_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_062",
        "instruction": "Secure all relevant recent reports for quarterly review process 'GOVERNANCE-REVIEW-Q1'. Identify all reports on 'server-analytics.company.com' matching criteria defined in standard file audit task 'fc_task_003'. Prevent modification during review by relocating all identified files to a newly created secure directory at '/analytics/reports/review_pending_q1/'. Complete the task by performing database modification to update audit task status reflecting quarterly completion, logging the successful governance action, and sending slack message to Operations.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_003"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-analytics.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "directory": "/analytics/reports"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "directory_path": "/analytics/reports/review_pending_q1"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "source_path": "/analytics/reports/daily_sales_report.csv",
                    "destination_path": "/analytics/reports/review_pending_q1/daily_sales_report.csv"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "source_path": "/analytics/reports/monthly_trends.csv",
                    "destination_path": "/analytics/reports/review_pending_q1/monthly_trends.csv"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_003",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "GOVERNANCE-REVIEW-Q1",
                    "task_type": "data_governance",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"fc_task_003\"",
                "\"files_identified_for_review\": 2",
                "\"review_directory_created\": true",
                "\"files_moved_to_review\": 2",
                "\"original_task_status_updated\": true",
                "\"governance_task_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_065",
        "instruction": "Execute file organization mandate 'dir_op_001' after conducting comprehensive System Readiness Assessment. Perform Pre-Execution Security Clearance practice for user ('user_002') on target server 'server-data-01.company.com' and Proactive Server Health Check practice using 80% utilization threshold. Log 'low_storage_warning' due to server's high current disk usage before proceeding. When all pre-flight checks pass despite the warning, execute File Organization practice completely. Conclude all operations with final success notification to the 'Operations' channel.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "dir_op_001",
                    "task_type": "pre_execution_check",
                    "user_id": "user_002",
                    "error_type": "low_storage_warning",
                    "severity": "warning",
                    "details_json": {
                        "disk_percent": 78,
                        "threshold_percent": 80
                    }
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/csv"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/dat"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/json"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/miscellaneous"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/sorted/csv/sales_data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/sorted/csv/customer_info.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/data/sorted/dat/inventory.dat"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/data/sorted/json/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/readme.txt",
                    "destination_path": "/data/sorted/miscellaneous/readme.txt"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/sorted/csv/data_0.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"operation_id\": \"dir_op_001\"",
                "\"security_clearance_status\": \"passed\"",
                "\"server_health_status\": \"passed\"",
                "\"low_storage_warning_logged\": true",
                "\"files_to_process\": 6",
                "\"directories_created\": 4",
                "\"files_moved\": 6",
                "\"all_statuses_updated\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_067",
        "instruction": "Handle incident 'INC-DIROP-RETRY-01' concerning deferred file organization task 'dir_op_001' by reassessing the operational environment. Determine whether current resource usage on 'server-data-01.company.com' is within acceptable limits, defined as below 60% CPU utilization. When the server remains above this threshold, prevent operation from proceeding. Apply deferral protocol by recording the cause of non-execution, updating all files in the task to failed state to prevent re-queueing, and providing visibility to stakeholders through the 'Operations' channel. Send notification explicitly stating that 'dir_op_001' remains deferred due to persistent high resource usage on the server, including actual CPU and memory percentages, and tag @bob.dev for awareness.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "dir_op_001",
                    "task_type": "pre_execution_check",
                    "user_id": "user_002",
                    "error_type": "high_resource_usage",
                    "severity": "warning",
                    "details_json": {
                        "cpu_percent": 62,
                        "memory_percent": 72,
                        "threshold_percent": 60,
                        "action_taken": "deferred"
                    }
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "failed"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "Task dir_op_001 remains deferred due to persistent high resource usage on server-data-01.company.com (CPU: 62%, MEM: 72%). cc @bob.dev"
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"dir_op_001\"",
                "\"server_cpu_usage\": 62",
                "\"health_check_status\": \"failed\"",
                "\"warning_log_created\": true",
                "\"files_in_operation\": 6",
                "\"file_statuses_updated_to_failed\": 6",
                "\"user_notified\": \"@ryan.dev\"",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_001",
        "instruction": "Carry out archive operation 'arch_003' with strict adherence to security and operational policies. Verify requesting user ('user_002') for authorization to access destination server ('log-storage.company.com') under the SSH Access Policy before any file operations proceed. When authorization is not confirmed, halt the archive operation and reflect failed state with reason clearly recorded. Capture policy violations as critical permission errors in task logs with full details for audit. Update task status accordingly and notify relevant parties, including system-wide alert to the 'System Alerts' channel stating: 'Archive task arch_003 failed pre-execution security clearance. User @bob.dev is not authorized for the destination server. See error logs for details.'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_003"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_003",
                    "task_type": "archive",
                    "user_id": "user_002",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User role 'developer' is not authorized for 'log-storage.company.com' per SSH Access Policy."
                    }
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_003",
                    "status": "failed"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Archive task arch_003 failed pre-execution security clearance. User @bob.dev is not authorized for the destination server. See error logs for details."
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"arch_003\"",
                "\"user_role\": \"developer\"",
                "\"ssh_key_id\": \"bob_rsa_key\"",
                "\"security_clearance_status\": \"failed\"",
                "\"policy_violation_detected\": true",
                "\"error_log_created\": true",
                "\"task_status_updated_to\": \"failed\"",
                "\"user_notified\": \"@ryan.dev\"",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_002",
        "instruction": "Handle high-priority failure of archive task 'arch_005' by applying Task Failure Diagnosis practices to investigate the incident and confirm whether the root cause is storage-related. When insufficient storage is confirmed on primary server ('personal-backup.company.com'), determine viable remediation path by evaluating available capacity on designated alternative servers, including 'backup-server.company.com' and 'storage-01.company.com'. Record analysis outcome in the system with remediation analysis entry documenting confirmed root cause, severity level, and best available alternative server with its capacity. Communicate remediation plan to stakeholders through the 'Operations' channel with explicit message describing recommended retry destination, available space, identified root cause, and tagging responsible user (@dave.intern) for visibility.",
        "actions": [
            {
                "name": "GetErrorLogDetails",
                "arguments": {
                    "task_id": "arch_005"
                },
            },
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_005"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "backup-server.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "storage-01.company.com"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_005",
                    "task_type": "remediation_analysis",
                    "user_id": "user_004",
                    "error_type": "remediation_analysis",
                    "severity": "medium",
                    "details_json": {
                        "root_cause": "Insufficient storage space on personal-backup.company.com",
                        "best_alternative_server": "backup-server.company.com",
                        "alternative_available_gb": 4250
                    }
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "Remediation Plan for arch_005: Retry task using backup-server.company.com as the destination (4250GB available). Root cause: insufficient space on personal-backup.company.com. cc @dave.intern"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "arch_005",
                    "task_type": "incident_response",
                    "user_id": "system_agent"
                }
            }
        ],
        "outputs": [
                "\"failed_task_id\": \"arch_005\"",
                "\"root_cause_identified\": \"Insufficient storage space on remote server. Available: 45MB, Required: 234MB\"",
                "\"alternative_server_1_space_gb\": 4250",
                "\"alternative_server_2_space_gb\": 1800",
                "\"remediation_log_created\": true",
                "\"user_contact\": \"@ethan.intern\"",
                "\"remediation_plan_sent_to_ops\": true",
                "\"incident_fully_processed\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_004",
        "instruction": "Respond to 'INCIDENT-LOG-ISOLATION-01' requiring immediate isolation of recent application logs on 'server-prod-01.company.com' due to potential security incident. Follow secure evidence collection practice by identifying all target log files using criteria from standard file check task 'fc_task_001'. Create secure archive of these files, transfer the archive to central evidence locker at '/storage/incident_evidence/' on 'backup-server.company.com' using administrative account ('user_001'), then purge source log files from production server to contain the incident. Complete the task by updating original file check task status and logging successful isolation of potentially compromised files.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_001"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "directory": "/var/log/applications"
                },
            },
            {
                "name": "CreateArchiveOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "archive_path": "/tmp/INCIDENT-LOG-ISOLATION-01.tar.gz",
                    "files_to_include": [
                        "/var/log/applications/webapp.log",
                        "/var/log/applications/api_requests.log",
                        "/var/log/applications/error.log"
                    ]
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "TransferFileToRemote",
                "arguments": {
                    "source_path": "/tmp/INCIDENT-LOG-ISOLATION-01.tar.gz",
                    "remote_address": "backup-server.company.com",
                    "destination_path": "/storage/incident_evidence/INCIDENT-LOG-ISOLATION-01.tar.gz",
                    "ssh_key": "alice_rsa_key"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/var/log/applications/webapp.log"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/var/log/applications/api_requests.log"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/var/log/applications/error.log"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_001",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "INCIDENT-LOG-ISOLATION-01",
                    "task_type": "forensics",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"fc_task_001\"",
                "\"files_identified_for_isolation\": 3",
                "\"evidence_archive_created\": true",
                "\"admin_key_retrieved\": \"alice_rsa_key\"",
                "\"evidence_transfer_successful\": true",
                "\"source_files_purged\": 3",
                "\"original_task_status_updated\": true",
                "\"forensics_task_logged\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_005",
        "instruction": "Handle incident 'INC-DIROP-PARTIAL-01' where file organization task 'dir_op_001' was deferred and user ('user_002') has requested partial execution. Verify server ('server-data-01.company.com') health is below 80% operational threshold, then proceed with modified 'File Organization Protocol'. Move only CSV files to their correct destination and all other file types to new '/data/deferred/' directory for later processing. Update status for every file in the manifest via database modification. Send slack message to Operations with this message: 'Incident INC-DIROP-PARTIAL-01: Partial completion for dir_op_001. CSV files moved to /data/sorted/csv. Non-CSV files moved to /data/deferred for later processing.'",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/csv"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/deferred"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/sorted/csv/sales_data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/sorted/csv/customer_info.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/sorted/csv/data_0.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/data/deferred/inventory.dat"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/data/deferred/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/readme.txt",
                    "destination_path": "/data/deferred/readme.txt"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "INC-DIROP-PARTIAL-01",
                    "task_type": "incident_response",
                    "user_id": "user_002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "Incident INC-DIROP-PARTIAL-01: Partial completion for dir_op_001. CSV files moved to /data/sorted/csv. Non-CSV files moved to /data/deferred for later processing."
                }
            }
        ],
        "outputs": [
                "\"server_health_ok\": true",
                "\"directories_created\": 2",
                "\"csv_files_moved\": 3",
                "\"other_files_deferred\": 3",
                "\"all_statuses_updated\": true",
                "\"partial_completion_logged\": true",
                "\"slack_summary_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_006",
        "instruction": "Handle task 'HYGIENE-PROD-LOGS-01' by ensuring proper archival and removal of outdated log files located in `/var/log/applications` on `server-prod-01.company.com`. Identify target files in compliance with Standard File Check practices defined in maintenance task 'fc_task_001'. Archive files under 'Secure File Archive Creation Protocol', including only files identified by the scan. Store the archive in `/backups/log_hygiene/` on `backup-server.company.com`, operating under authority of designated manager ('user_005'). Following data lifecycle policy, purge any successfully archived files from the source system. Reflect completion by updating original file check task, logging hygiene activity, and providing notification to stakeholders via 'Operations' channel.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_001"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "directory": "/var/log/applications"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "backup-server.company.com"
                },
            },
            {
                "name": "CreateArchiveOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "archive_path": "/tmp/HYGIENE-PROD-LOGS-01.tar.gz",
                    "files_to_include": [
                        "/var/log/applications/webapp.log",
                        "/var/log/applications/api_requests.log",
                        "/var/log/applications/error.log"
                    ]
                },
            },
            {
                "name": "TransferFileToRemote",
                "arguments": {
                    "source_path": "/tmp/HYGIENE-PROD-LOGS-01.tar.gz",
                    "remote_address": "backup-server.company.com",
                    "destination_path": "/backups/log_hygiene/HYGIENE-PROD-LOGS-01.tar.gz",
                    "ssh_key": "eve_rsa_key"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/var/log/applications/webapp.log"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/var/log/applications/api_requests.log"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/var/log/applications/error.log"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_001",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "HYGIENE-PROD-LOGS-01",
                    "task_type": "system_hygiene",
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"fc_task_001\"",
                "\"files_found_to_archive\": 3",
                "\"destination_disk_space_ok\": true",
                "\"archive_created\": true",
                "\"transfer_successful\": true",
                "\"source_files_purged\": 3",
                "\"original_task_status_updated\": true",
                "\"hygiene_task_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_008",
        "instruction": "Handle final data lifecycle stage of completed archive task 'arch_001' by purging all original source files from 'server-prod-01.company.com'. Perform 'Pre-Execution Security Clearance Protocol' before any deletions to ensure original user ('user_001') is authorized. After clearance, retrieve the archive's file manifest and systematically delete every source file. Update archive status to 'verified' via database write, signifying lifecycle completion. Conclude by logging cleanup operation ('CLEANUP-ARCH-001') and notifying 'Operations'.",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "alice_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/src/main.js"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/src/utils.js"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/config/database.json"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/docs/readme.md"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/tests/unit_tests.py"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_001",
                    "status": "verified"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "CLEANUP-ARCH-001",
                    "task_type": "archive_cleanup",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"archive_id\": \"arch_001\"",
                "\"security_clearance\": \"passed\"",
                "\"source_files_identified\": 5",
                "\"source_files_deleted\": 5",
                "\"task_status_updated\": \"verified\"",
                "\"cleanup_operation_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_010",
        "instruction": "Perform pre-flight integrity verification 'AUDIT-DIR-OP-001' of directory operation 'dir_op_001' by validating that every file in the operation's manifest exists on 'server-data-01.company.com' and each file's live checksum matches the reference checksum stored in the manifest. Reflect in audit outcome whether all files pass these validations. When any file fails due to absence or checksum mismatch, enforce failure protocol: mark audit unsuccessful, create critical error log entry identifying the file and violation type, update all files in the operation to 'failed' status, and notify administrators through 'System Alerts' channel.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetRemoteFileChecksum",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/sales_data.csv"
                },
            },
            {
                "name": "GetRemoteFileChecksum",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/customer_info.csv"
                },
            },
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/inventory.dat"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "AUDIT-DIR-OP-001",
                    "task_type": "pre_flight_audit",
                    "user_id": "user_002",
                    "error_type": "file_not_found",
                    "severity": "critical",
                    "details_json": {
                        "filepath": "/data/unsorted/inventory.dat",
                        "server": "server-data-01.company.com"
                    }
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "failed"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                }
            }
        ],
        "outputs": [
                "\"audit_id\": \"AUDIT-DIR-OP-001\"",
                "\"files_to_audit\": 6",
                "\"files_verified\": 2",
                "\"audit_failed\": true",
                "\"failing_file\": \"/data/unsorted/inventory.dat\"",
                "\"error_log_created\": true",
                "\"files_in_operation\": 6",
                "\"file_statuses_updated_to_failed\": 6",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_011",
        "instruction": "Execute file organization mandate 'dir_op_002' for task 'DEP-OP-002', but first remediate high disk usage issue on target server 'server-data-01.company.com'. Begin by following 'Stale File Cleanup Protocol' as defined in maintenance task 'fc_task_002', ensuring you purge only files that strictly match all defined policy filters (age and size). After cleanup practice is fully complete, proceed with complete 'File Organization Protocol' for 'dir_op_002' as requested by 'user_001'.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/temp_export_001.csv"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_002",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_002",
                    "task_type": "cleanup",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "File Check"
                },
            },
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_002"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_002"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/archive/projects/documents"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/archive/projects/source_code"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/archive/projects/data_files"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/archive/projects/miscellaneous"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/tmp/project_files/project_spec.pdf",
                    "destination_path": "/archive/projects/documents/project_spec.pdf"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_007",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/tmp/project_files/src/main.py",
                    "destination_path": "/archive/projects/source_code/main.py"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_008",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "DEP-OP-002",
                    "task_type": "file_organization",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"dependency_check_passed\": true",
                "\"cleanup_protocol_initiated\": true",
                "\"files_purged\": 1",
                "\"cleanup_task_logged\": true",
                "\"main_operation_files_found\": 2",
                "\"directories_created\": 4",
                "\"main_operation_files_moved\": 2",
                "\"all_statuses_updated\": true",
                "\"main_operation_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_013",
        "instruction": "You are a Forensic Investigator assigned to 'RCA-STO-001', a root cause analysis for a high disk usage alert (82%) on 'storage-01.company.com'. Your mission is to find the cause. We need to confirm the live disk usage. Also to find the most recently completed 'archive' task that targeted this server; you have intelligence suggesting 'arch_002' is the likely candidate. Validate this by retrieving the archive's instructions. If confirmed, perform a database write, logging a new 'high' severity 'disk_space_warning' error using the RCA task ID. The log's details must include the server, its usage, the contributing task ID, and that task's archive size. Alert for administrators is needed ('user_001', 'user_005') in 'System Alerts' with the message: 'RCA Complete (RCA-STO-001): High disk usage (82%) on storage-01.company.com correlated with task arch_002 (487.0MB). @alice.admin @eve.manager please review.'",
        "actions": [
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "storage-01.company.com"
                },
            },
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_002"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "RCA-STO-001",
                    "task_type": "forensics",
                    "user_id": "system_agent",
                    "error_type": "disk_space_warning",
                    "severity": "high",
                    "details_json": {
                        "server": "storage-01.company.com",
                        "usage_percent": 82,
                        "likely_cause_task": "arch_002",
                        "archive_size_bytes": 510654976
                    }
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "RCA Complete (RCA-STO-001): High disk usage (82%) on storage-01.company.com correlated with task arch_002 (487.0MB). @alice.admin @eve.manager please review."
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "RCA-STO-001",
                    "task_type": "investigation",
                    "user_id": "system_agent"
                }
            }
        ],
        "outputs": [
                "\"disk_usage_confirmed_percent\": 82",
                "\"contributing_task_id\": \"arch_002\"",
                "\"correlation_confirmed\": true",
                "\"incident_log_created\": true",
                "\"admin_1_contact\": \"@maya.admin\"",
                "\"admin_2_contact\": \"@aria.manager\"",
                "\"slack_escalation_sent\": true",
                "\"investigation_complete_and_logged\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_014",
        "instruction": "Execute pending archive operation 'arch_002' from initiation to final cleanup by following 'Secure File Archive Creation Protocol' to create and transfer the archive to its destination directory. After transfer completion, follow appropriate data lifecycle practice by purging all original source files from 'server-analytics.company.com'. Finalize by updating archive status to 'verified' via database modification to signify lifecycle completion.",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_002"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "storage-01.company.com"
                },
            },
            {
                "name": "CreateArchiveOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "archive_path": "/tmp/analytics_data_archive_20240116_103000.tar.gz",
                    "files_to_include": [
                        "/analytics/raw_data/user_events_2023.csv",
                        "/analytics/raw_data/page_views_2023.csv",
                        "/analytics/processed/monthly_reports_2023.json",
                        "/analytics/processed/yearly_summary_2023.pdf"
                    ]
                },
            },
            {
                "name": "TransferFileToRemote",
                "arguments": {
                    "source_path": "/tmp/analytics_data_archive_20240116_103000.tar.gz",
                    "remote_address": "storage-01.company.com",
                    "destination_path": "/var/backups/analytics_data_archive_20240116_103000.tar.gz",
                    "ssh_key": "carol_rsa_key"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_002",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "arch_002",
                    "task_type": "archive",
                    "user_id": "user_003"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "filepath": "/analytics/raw_data/user_events_2023.csv"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "filepath": "/analytics/raw_data/page_views_2023.csv"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "filepath": "/analytics/processed/monthly_reports_2023.json"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "filepath": "/analytics/processed/yearly_summary_2023.pdf"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_002",
                    "status": "verified"
                }
            }
        ],
        "outputs": [
                "\"archive_id\": \"arch_002\"",
                "\"disk_space_ok\": true",
                "\"archive_created\": true",
                "\"transfer_successful\": true",
                "\"initial_status_updated\": \"completed\"",
                "\"source_files_purged\": 4",
                "\"final_status_updated\": \"verified\""
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_015",
        "instruction": "Perform partial migration 'MIGRATE-DATA-ONLY-001' of data-related files from file organization mandate 'dir_op_001'. Ensure operation is fully authorized and target server 'server-data-01.company.com' is ready before proceeding. After all pre-flight checks pass, identify only data-specific files ('.dat' and '.json') from the operation's manifest and relocate them to new pre-migration staging directory at '/staging/data_migration_q1/'. Execute the complete task, including database modifications to update moved file statuses and logging successful staging.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/staging/data_migration_q1"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/staging/data_migration_q1/inventory.dat"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/staging/data_migration_q1/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "MIGRATE-DATA-ONLY-001",
                    "task_type": "data_staging",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"dir_op_001\"",
                "\"security_clearance_status\": \"passed\"",
                "\"disk_space_ok\": true",
                "\"files_identified_for_staging\": 2",
                "\"staging_directory_created\": true",
                "\"files_moved_to_staging\": 2",
                "\"original_task_files_updated\": 2",
                "\"staging_task_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_017",
        "instruction": "Handle priority review assignment 'PRIORITY-REVIEW-001' requiring immediate access to all CSV files from pending sorting job 'dir_op_001'. Intercept these specific files by identifying all CSV files in the operation's manifest on 'server-data-01.company.com'. Prevent them from proceeding to standard sorting destination by relocating all identified CSV files to new priority review directory at '/data/priority_review/20240120/'. Execute the complete task, including database modifications to update moved file statuses within original 'dir_op_001' mandate, logging successful staging operation, and sending message to 'Operations' channel.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/priority_review/20240120"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/priority_review/20240120/sales_data.csv"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/priority_review/20240120/customer_info.csv"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/priority_review/20240120/data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "PRIORITY-REVIEW-001",
                    "task_type": "data_staging",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"dir_op_001\"",
                "\"files_identified_for_staging\": 3",
                "\"staging_directory_created\": true",
                "\"files_moved_to_staging\": 3",
                "\"original_task_files_updated\": 3",
                "\"staging_task_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_018",
        "instruction": "Conduct pre-flight security audit for archive task 'arch_004' by enforcing all security protocols before execution. Perform complete 'Pre-Execution Security Clearance Protocol' for requesting user ('user_005') against target server 'document-vault.company.com'. When security policy violation is discovered, immediately halt the operation, update archive task status to 'failed' via database writes, log 'critical' 'permission_denied' error detailing exact violation, and escalate the incident by notifying 'System Alerts' channel.",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_004"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "eve_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_004",
                    "status": "failed"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_004",
                    "task_type": "security_audit",
                    "user_id": "user_005",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "Key 'eve_rsa_key' is not authorized for server 'document-vault.company.com' as per its authorized_servers list."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"arch_004\"",
                "\"user_role\": \"project_manager\"",
                "\"ssh_key_id\": \"eve_rsa_key\"",
                "\"authorization_check\": \"failed\"",
                "\"policy_violation_confirmed\": true",
                "\"task_status_updated\": \"failed\"",
                "\"security_error_logged\": true",
                "\"user_contact\": \"@aria.manager\"",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_023",
        "instruction": "Successfully complete pending archive operation 'arch_001', a critical task requiring full adherence to security and operational best practices. Ensure user is authorized to access destination server and server has adequate disk space before execution. After all pre-flight checks pass, create the archive on source server 'server-prod-01.company.com' and transfer it. Conclude by updating all relevant database records to reflect task completion and notifying 'Operations' channel with this message: 'Archive task arch_001 completed successfully. Archive transferred to backup-server.company.com:/tmp/archives/.'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "alice_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "backup-server.company.com"
                },
            },
            {
                "name": "CreateArchiveOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "archive_path": "/tmp/project_backup_2024.tar.gz",
                    "files_to_include": [
                        "/home/projects/webapp/src/main.js",
                        "/home/projects/webapp/src/utils.js",
                        "/home/projects/webapp/config/database.json",
                        "/home/projects/webapp/docs/readme.md",
                        "/home/projects/webapp/tests/unit_tests.py"
                    ]
                },
            },
            {
                "name": "TransferFileToRemote",
                "arguments": {
                    "source_path": "/tmp/project_backup_2024.tar.gz",
                    "remote_address": "backup-server.company.com",
                    "destination_path": "/tmp/archives/project_backup_2024.tar.gz",
                    "ssh_key": "alice_rsa_key"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_001",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "arch_001",
                    "task_type": "archive",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "Archive task arch_001 completed successfully. Archive transferred to backup-server.company.com:/tmp/archives/."
                }
            }
        ],
        "outputs": [
                "\"archive_id\": \"arch_001\"",
                "\"security_clearance_status\": \"passed\"",
                "\"sufficient_disk_space\": true",
                "\"archive_created\": true",
                "\"transfer_successful\": true",
                "\"task_status_updated\": \"completed\"",
                "\"completion_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_025",
        "instruction": "Execute file organization mandate 'dir_op_001' for task 'DEP-OP-001', dependent on target server 'server-data-01.company.com' health. Perform health check against 75% disk usage threshold first. When server is unhealthy, remediate the issue by following 'Stale File Cleanup Protocol' for designated cleanup task 'fc_task_002'. After remediation is fully complete, proceed with complete 'File Organization Protocol' for 'dir_op_001'.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/temp_export_001.csv"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/cache_backup.dat"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_002",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_002",
                    "task_type": "file_check",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "File Check"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/csv"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/dat"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/json"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/miscellaneous"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/sorted/csv/sales_data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/sorted/csv/customer_info.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/data/sorted/dat/inventory.dat"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/data/sorted/json/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/readme.txt",
                    "destination_path": "/data/sorted/miscellaneous/readme.txt"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/sorted/csv/data_0.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "DEP-OP-001",
                    "task_type": "file_organization",
                    "user_id": "user_002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"dependency_check_passed\": true",
                "\"cleanup_protocol_initiated\": true",
                "\"files_purged\": 2",
                "\"cleanup_task_logged\": true",
                "\"files_in_main_op\": 6",
                "\"main_operation_files_moved\": 6",
                "\"all_statuses_updated\": true",
                "\"main_operation_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_026",
        "instruction": "Prepare financial reports for compliance audit 'FIN-AUDIT-PREP-Q1' by identifying all relevant reports on 'server-analytics.company.com' using rules defined in standing audit task 'fc_task_003'. Prevent modification during review by securely isolating these files through relocation of all identified reports to new, centralized quarantine directory at '/secure/quarantine/financial_audit_q1/'. Execute the complete task, including database modification to update underlying audit task status and logging successful preparation for compliance review.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_003"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-analytics.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "directory": "/analytics/reports"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "directory_path": "/secure/quarantine/financial_audit_q1"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "source_path": "/analytics/reports/daily_sales_report.csv",
                    "destination_path": "/secure/quarantine/financial_audit_q1/daily_sales_report.csv"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "source_path": "/analytics/reports/monthly_trends.csv",
                    "destination_path": "/secure/quarantine/financial_audit_q1/monthly_trends.csv"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_003",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "FIN-AUDIT-PREP-Q1",
                    "task_type": "compliance_prep",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"fc_task_003\"",
                "\"files_identified_for_quarantine\": 2",
                "\"quarantine_directory_created\": true",
                "\"files_moved_to_quarantine\": 2",
                "\"original_task_status_updated\": true",
                "\"compliance_task_logged\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_027",
        "instruction": "Execute file organization mandate 'dir_op_001' for task 'DEP-OP-001', dependent on target server 'server-data-01.company.com' health. Perform health check against 75% disk usage threshold first. When server is unhealthy, remediate the issue by following 'Stale File Cleanup Protocol' for designated cleanup task 'fc_task_002'. After remediation, proceed with complete 'File Organization Protocol' for 'dir_op_001'.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/temp_export_001.csv"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/cache_backup.dat"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_002",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_002",
                    "task_type": "file_check",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "File Check"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/csv"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/dat"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/json"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/miscellaneous"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/sorted/csv/sales_data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/sorted/csv/customer_info.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/data/sorted/dat/inventory.dat"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/data/sorted/json/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/readme.txt",
                    "destination_path": "/data/sorted/miscellaneous/readme.txt"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/sorted/csv/data_0.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "DEP-OP-001",
                    "task_type": "file_organization",
                    "user_id": "user_002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"dependency_check_passed\": true",
                "\"cleanup_protocol_initiated\": true",
                "\"files_purged\": 2",
                "\"cleanup_task_logged\": true",
                "\"files_in_main_op\": 6",
                "\"main_operation_files_moved\": 6",
                "\"all_statuses_updated\": true",
                "\"main_operation_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_028",
        "instruction": "Perform mandatory pre-flight integrity audit on source files for archive operation 'arch_002', which reside on 'server-analytics.company.com'. Follow appropriate practice to verify every source file listed in the task's manifest. When any file is not found, immediately halt, update archive status to 'failed' in database, log 'critical' 'file_not_found' error, and alert 'System Alerts' with this message: 'Pre-flight audit for arch_002 FAILED: Source file /analytics/raw_data/page_views_2023.csv not found. Archival process halted.'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_002"
                },
            },
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "filepath": "/analytics/raw_data/user_events_2023.csv"
                },
            },
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "server-analytics.company.com",
                    "filepath": "/analytics/raw_data/page_views_2023.csv"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_002",
                    "status": "failed"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_002",
                    "task_type": "pre_flight_audit",
                    "user_id": "user_003",
                    "error_type": "file_not_found",
                    "severity": "critical",
                    "details_json": {
                        "filepath": "/analytics/raw_data/page_views_2023.csv"
                    }
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Pre-flight audit for arch_002 FAILED: Source file /analytics/raw_data/page_views_2023.csv not found. Archival process halted."
                }
            }
        ],
        "outputs": [
                "\"archive_id\": \"arch_002\"",
                "\"files_to_audit\": 4",
                "\"audit_failed\": true",
                "\"failing_file\": \"/analytics/raw_data/page_views_2023.csv\"",
                "\"task_status_updated\": \"failed\"",
                "\"error_log_created\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_029",
        "instruction": "Handle file check task 'fc_task_001' requested by user 'user_005' by performing full pre-execution security clearance before execution. Verify the user's default SSH key is authorized for target server and their role ('project_manager') complies with 'SSH Access Policy'. Only after confirming authorization and checking server is online may you proceed with file scan. Upon completion, update task status, log results, and notify 'File Check' channel.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_001"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "eve_rsa_key"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "directory": "/var/log/applications"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_001",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_001",
                    "task_type": "file_check",
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "File Check"
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"fc_task_001\"",
                "\"user_id\": \"user_005\"",
                "\"ssh_key_id\": \"eve_rsa_key\"",
                "\"authorization_status\": \"approved\"",
                "\"server_status\": \"online\"",
                "\"files_found_count\": 3",
                "\"task_completed_status\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_031",
        "instruction": "Audit pending archive task 'arch_004' against 'SSH Access Policy' following security compliance review flag. Determine if user's role and SSH key authorizations permit access to target server 'document-vault.company.com'. When policy violation is confirmed, immediately neutralize the threat by canceling the operation, logging critical 'permission_denied' security error, and alerting 'System Alerts' channel about enforcement action.",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_004"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "eve_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_004",
                    "status": "failed"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_004",
                    "task_type": "archive",
                    "user_id": "user_005",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "Key 'eve_rsa_key' not authorized for server 'document-vault.company.com'."
                    }
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"arch_004\"",
                "\"user_role\": \"project_manager\"",
                "\"ssh_key_id\": \"eve_rsa_key\"",
                "\"authorization_check\": \"failed\"",
                "\"policy_violation_confirmed\": true",
                "\"task_status_updated\": \"failed\"",
                "\"security_error_logged\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_032",
        "instruction": "Execute file organization mandate 'dir_op_001' by systematically processing the entire contents of '/data/unsorted' directory on 'server-data-01.company.com'. Create required subdirectory structure within '/data/sorted' first, then meticulously relocate every file to its designated new location, ensuring each individual move is tracked by updating the file's status to 'completed'. Send final confirmation to 'Operations' channel once all files are successfully organized.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/csv"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/dat"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/json"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/miscellaneous"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/sorted/csv/sales_data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/sorted/csv/customer_info.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/data/sorted/dat/inventory.dat"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/data/sorted/json/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/readme.txt",
                    "destination_path": "/data/sorted/miscellaneous/readme.txt"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/sorted/csv/data_0.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"operation_id\": \"dir_op_001\"",
                "\"files_to_process\": 6",
                "\"directories_created\": 4",
                "\"files_moved\": 6",
                "\"file_statuses_updated\": 6",
                "\"task_fully_completed\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_033",
        "instruction": "Conduct root cause analysis for failed file check task 'fc_task_004' by retrieving the technical error log. After confirming the root cause, create formal, user-facing incident record by logging new error message that summarizes the issue. Identify the user who initiated the task and notify them with detailed message in 'System Alerts' channel: 'Incident report for task fc_task_004: Connection timeout to server-config.company.com. User: @bob.dev. Server is in maintenance mode.'",
        "actions": [
            {
                "name": "GetErrorLogDetails",
                "arguments": {
                    "task_id": "fc_task_004"
                },
            },
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_004"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "fc_task_004",
                    "task_type": "file_check",
                    "user_id": "user_002",
                    "error_type": "connection_timeout",
                    "severity": "high",
                    "details_json": {
                        "server": "server-config.company.com",
                        "reason": "Server is in maintenance mode."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Incident report for task fc_task_004: Connection timeout to server-config.company.com. User: @bob.dev. Server is in maintenance mode."
                }
            }
        ],
        "outputs": [
                "\"failed_task_id\": \"fc_task_004\"",
                "\"root_cause\": \"Connection timeout to server-config.company.com - server may be in maintenance mode\"",
                "\"database_updated\": true",
                "\"new_error_msg_id\": \"err_msg_006\"",
                "\"user_contact\": \"@ryan.dev\"",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_034",
        "instruction": ["Handle critical storage alert 'storage_alert_S01' for 'storage-01.company.com' by confirming live disk usage. When usage_percent > 80, create low_storage_warning log with structured fields (server, usage_percent, threshold_percent), then notify admins 'user_001' and 'user_005' via 'System Alerts' with this message: 'CRITICAL: Server storage-01.company.com has reached 82 percent disk usage. Immediate action required. @alice.admin @eve.manager please investigate.'."],
        "actions": [
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "storage-01.company.com"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "storage_alert_S01",
                    "task_type": "system_monitoring",
                    "user_id": "system_agent",
                    "error_type": "low_storage_warning",
                    "severity": "warning",
                    "details_json": {
                        "server": "storage-01.company.com",
                        "usage_percent": 82,
                        "threshold_percent": 80
                    }
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "CRITICAL: Server storage-01.company.com has reached 82 percent disk usage. Immediate action required. @alice.admin @eve.manager please investigate."
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "storage_alert_S01",
                    "task_type": "system_monitoring",
                    "user_id": "system_agent"
                }
            }
        ],
        "outputs": [
                "\"disk_usage_percent\": 82",
                "\"threshold_exceeded\": true",
                "\"warning_log_created\": true",
                "\"admin_1_contact\": \"@maya.admin\"",
                "\"admin_2_contact\": \"@aria.manager\"",
                "\"escalation_complete\": true",
                "\"slack_notification_sent\": true",
                "\"completion_logged\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_037",
        "instruction": "Process incident 'INC-FC004-MAINT' concerning failure of task 'fc_task_004' by investigating the failure through retrieving original error log and confirming live status and current resource load of target server. After verifying root cause, perform database write by logging new, formal incident record with 'medium' severity under error type 'server_maintenance', using incident ID as task identifier. Conclude by composing and sending structured notification message to 'File Check' channel, including incident ID, affected user's slack handle, and server's confirmed status.",
        "actions": [
            {
                "name": "GetErrorLogDetails",
                "arguments": {
                    "task_id": "fc_task_004"
                },
            },
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_004"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-config.company.com"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-config.company.com"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "INC-FC004-MAINT",
                    "task_type": "incident_response",
                    "user_id": "user_002",
                    "error_type": "server_maintenance",
                    "severity": "medium",
                    "details_json": {
                        "original_task_id": "fc_task_004",
                        "server": "server-config.company.com",
                        "confirmed_status": "maintenance"
                    }
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "File Check",
                    "message": "Task Deferred: Task fc_task_004 for user @bob.dev is deferred. Reason: Target server server-config.company.com confirmed status is maintenance. Tracking ID: INC-FC004-MAINT."
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "INC-FC004-MAINT",
                    "task_type": "incident_response",
                    "user_id": "system_agent"
                }
            }
        ],
        "outputs": [
                "\"original_task_id\": \"fc_task_004\"",
                "\"root_cause\": \"Connection timeout to server-config.company.com - server may be in maintenance mode\"",
                "\"live_server_status\": \"maintenance\"",
                "\"root_cause_confirmed\": true",
                "\"incident_log_created\": true",
                "\"user_contact\": \"@ryan.dev\"",
                "\"user_notification_sent\": true",
                "\"incident_response_logged\": true",
                "\"incident_fully_processed\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_040",
        "instruction": "Handle incident 'HRA-SRVDATA-01' regarding high resource usage on 'server-data-01.company.com' by executing 'Proactive Server Health Check Protocol' with 70% utilization threshold. When breached, escalate with forensic analysis of '/data/temp' directory against policy defined in task 'fc_task_002'. Log 'warning' severity 'high_resource_usage' error using incident ID, detailing breached metrics and count of policy-violating files. Conclude by alerting 'System Alerts' with structured message including incident ID and server name.",
        "actions": [
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "HRA-SRVDATA-01",
                    "task_type": "system_monitoring",
                    "user_id": "system_agent",
                    "error_type": "high_resource_usage",
                    "severity": "warning",
                    "details_json": {
                        "server": "server-data-01.company.com",
                        "memory_percent": 72,
                        "disk_percent": 78,
                        "non_compliant_files_count": 1
                    }
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Health Alert (HRA-SRVDATA-01): server-data-01.company.com has breached resource thresholds. MEM: 72%, DSK: 78%."
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "HRA-SRVDATA-01",
                    "task_type": "system_monitoring",
                    "user_id": "system_agent"
                }
            }
        ],
        "outputs": [
                "\"incident_id\": \"HRA-SRVDATA-01\"",
                "\"threshold_exceeded\": true",
                "\"memory_usage\": 72",
                "\"disk_usage\": 78",
                "\"non_compliant_files_found\": 1",
                "\"warning_log_created\": true",
                "\"slack_alert_sent\": true",
                "\"investigation_complete\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_041",
        "instruction": "Handle full lifecycle of maintenance task 'fc_task_002' by resolving this task through purging stale files from target server according to defined policies. Ensure operation security by validating that requesting user ('user_001') has fully authorized access to target server before executing any file deletions. After successful execution and cleanup, finalize process by updating all relevant database records and sending comprehensive completion summary to 'Operations' channel with this message: 'Maintenance task fc_task_002 completed successfully. A total of 2 stale files were purged from /data/temp on server-data-01.company.com.'",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "alice_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/temp_export_001.csv"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/cache_backup.dat"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_002",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_002",
                    "task_type": "file_check",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "Maintenance task fc_task_002 completed successfully. A total of 2 stale files were purged from /data/temp on server-data-01.company.com."
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"fc_task_002\"",
                "\"security_clearance_status\": \"passed\"",
                "\"server_status\": \"online\"",
                "\"files_scanned\": 2",
                "\"non_compliant_files_found\": 2",
                "\"files_deleted\": 2",
                "\"task_status_updated\": true",
                "\"completion_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_042",
        "instruction": "Stage relevant input files for new data processing job deployment through assignment 'DEPLOY-PREP-001'. Isolate all CSV files from file organization mandate 'dir_op_001' on 'server-data-01.company.com' instead of moving them to final sorted location. Relocate all identified CSV files to new, temporary staging directory at '/staging/data_processing_job_v2/'. Execute the complete task, including database modifications to update moved file statuses within original mandate and logging successful staging operation.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/staging/data_processing_job_v2"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/staging/data_processing_job_v2/sales_data.csv"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/staging/data_processing_job_v2/customer_info.csv"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/staging/data_processing_job_v2/data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "DEPLOY-PREP-001",
                    "task_type": "data_staging",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"dir_op_001\"",
                "\"files_identified_for_staging\": 6",
                "\"staging_directory_created\": true",
                "\"csv_files_moved_to_staging\": 3",
                "\"original_task_files_updated\": 3",
                "\"staging_task_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_043",
        "instruction": "Prepare project files for pre-production review through assignment 'STAGE-PROJECT-FILES-002'. Identify all files associated with file organization mandate 'dir_op_002' and relocate them to new staging directory on 'server-data-01.company.com' at '/staging/review/dir_op_002/' instead of moving to final archive. Execute the complete task, including database modification to update status of all files within original mandate, logging successful staging operation, and sending slack message to Operations.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_002"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_002"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/staging/review/dir_op_002"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/tmp/project_files/project_spec.pdf",
                    "destination_path": "/staging/review/dir_op_002/project_spec.pdf"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/tmp/project_files/src/main.py",
                    "destination_path": "/staging/review/dir_op_002/main.py"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_007",
                    "status": "completed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_008",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "STAGE-PROJECT-FILES-002",
                    "task_type": "data_staging",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"dir_op_002\"",
                "\"files_identified_for_staging\": 2",
                "\"staging_directory_created\": true",
                "\"files_moved_to_staging\": 2",
                "\"original_task_files_updated\": 2",
                "\"staging_task_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_044",
        "instruction": "Handle file organization mandate 'dir_op_001' by following standard pre-flight operational practice before executing file moves. Conduct full readiness assessment of target server 'server-data-01.company.com', verifying both requesting user's ('user_002') security clearance and server's resource health. When detecting server under heavy load (memory or disk usage > 75%), follow standard procedure to log 'high_resource_usage' warning and alert 'System Alerts' before proceeding. After all pre-flight checks pass, execute file organization task completely, ensuring all files are moved and their statuses are updated.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "dir_op_001",
                    "task_type": "pre_execution_check",
                    "user_id": "user_002",
                    "error_type": "high_resource_usage",
                    "severity": "warning",
                    "details_json": {
                        "server": "server-data-01.company.com",
                        "disk_percent": 78,
                        "threshold_percent": 75
                    }
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/csv"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/dat"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/json"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/miscellaneous"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/sorted/csv/sales_data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/sorted/csv/customer_info.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/data/sorted/dat/inventory.dat"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/data/sorted/json/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/readme.txt",
                    "destination_path": "/data/sorted/miscellaneous/readme.txt"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/sorted/csv/data_0.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"operation_id\": \"dir_op_001\"",
                "\"security_clearance_status\": \"passed\"",
                "\"heavy_load_detected\": true",
                "\"warning_log_created\": true",
                "\"slack_alert_sent\": true",
                "\"files_to_process\": 6",
                "\"files_moved\": 6",
                "\"all_statuses_updated\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_046",
        "instruction": "Investigate alert 'HRA-SRVPROD-01' for 'server-prod-01.company.com' by following standard practice to confirm if server resource usage (memory or disk) has breached 50% operational threshold. When threshold is breached, perform forensic scan of '/var/log/applications' directory to identify oversized files (>20MB). Log findings and escalate by notifying appropriate channels and personnel following analysis. The project manager for this system is Aria Lead ('user_005'). Include confirmation to 'System Alerts' and remediation proposal to 'Operations' with this message: 'Remediation Plan for HRA-SRVPROD-01: Oversized files ['webapp.log', 'api_requests.log'] found in /var/log/applications. Recommend cleanup task. cc @eve.manager'",
        "actions": [
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "directory": "/var/log/applications"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "HRA-SRVPROD-01",
                    "task_type": "system_monitoring",
                    "user_id": "system_agent",
                    "error_type": "high_resource_usage",
                    "severity": "warning",
                    "details_json": {
                        "server": "server-prod-01.company.com",
                        "threshold_percent": 50,
                        "memory_percent": 58,
                        "disk_percent": 65,
                        "oversized_files_found": [
                            "webapp.log",
                            "api_requests.log"
                        ]
                    }
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "High Resource Usage Confirmed: HRA-SRVPROD-01 on server-prod-01.company.com. MEM: 58%, DSK: 65%."
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "Remediation Plan for HRA-SRVPROD-01: Oversized files ['webapp.log', 'api_requests.log'] found in /var/log/applications. Recommend cleanup task. cc @eve.manager"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "HRA-SRVPROD-01",
                    "task_type": "investigation",
                    "user_id": "system_agent"
                }
            }
        ],
        "outputs": [
                "\"alert_id\": \"HRA-SRVPROD-01\"",
                "\"threshold_exceeded\": true",
                "\"oversized_files_count\": 2",
                "\"warning_log_created\": true",
                "\"system_alert_sent\": true",
                "\"remediation_plan_sent\": true",
                "\"investigation_logged\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_048",
        "instruction": "Assess health of 'server-prod-01.company.com' and 'server-data-01.company.com' for audit 'HEALTH-AUDIT-02', enforcing 75% disk usage threshold. When server is found non-compliant, immediately escalate with alert then apply standard remediation procedure for stale files as defined by maintenance task 'fc_task_002'. Conclude audit by logging completion and reporting full summary of findings and actions taken to 'Operations' channel with this message: 'System Health Audit HEALTH-AUDIT-02 complete. Server server-data-01.company.com exceeded disk threshold (78%) and was remediated by purging 2 stale files. Server server-prod-01.company.com is healthy.'",
        "actions": [
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "HEALTH-AUDIT-02: Disk usage on server-data-01.company.com (78%) exceeds 75% threshold. Initiating cleanup."
                },
            },
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/temp_export_001.csv"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/cache_backup.dat"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_002",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_002",
                    "task_type": "file_check",
                    "user_id": "user_001"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "HEALTH-AUDIT-02",
                    "task_type": "system_health_audit",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "System Health Audit HEALTH-AUDIT-02 complete. Server server-data-01.company.com exceeded disk threshold (78%) and was remediated by purging 2 stale files. Server server-prod-01.company.com is healthy."
                }
            }
        ],
        "outputs": [
                "\"servers_checked\": 2",
                "\"threshold_breached_on\": \"server-data-01.company.com\"",
                "\"initial_alert_sent\": true",
                "\"cleanup_protocol_initiated\": true",
                "\"files_purged_count\": 2",
                "\"maintenance_task_status_updated\": true",
                "\"cleanup_task_logged\": true",
                "\"audit_operation_logged\": true",
                "\"slack_summary_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_050",
        "instruction": "Execute file organization mandate 'dir_op_001', delayed due to low disk space warning, by conducting full readiness assessment first. Perform 'Pre-Execution Security Clearance Protocol' for requesting user ('user_002') and re-validate target server 'server-data-01.company.com' health. When all pre-flight checks pass, proceed with complete 'File Organization Protocol' as originally specified. Conclude all operations with final success notification to 'Operations' channel.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/csv"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/dat"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/json"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/miscellaneous"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/sorted/csv/sales_data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/sorted/csv/customer_info.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/data/sorted/dat/inventory.dat"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/data/sorted/json/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/readme.txt",
                    "destination_path": "/data/sorted/miscellaneous/readme.txt"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/sorted/csv/data_0.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"operation_id\": \"dir_op_001\"",
                "\"security_clearance\": \"passed\"",
                "\"server_health_ok\": true",
                "\"disk_space_ok\": true",
                "\"files_to_process\": 6",
                "\"directories_created\": 4",
                "\"files_moved\": 6",
                "\"all_statuses_updated\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_051",
        "instruction": "Perform post-archive cleanup for 'arch_002' following protocol requiring full security clearance check before deleting any files. Validate that original user ('user_003') has authorized access to source server ('server-analytics.company.com') per 'SSH Access Policy'. When policy violation is discovered, halt cleanup, log critical 'permission_denied' error via database write, and escalate to 'System Alerts' channel with this message: 'HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted.'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_002"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "carol_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_002_cleanup",
                    "task_type": "security_check",
                    "user_id": "user_003",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User role 'data_analyst' is not authorized for server 'server-analytics.company.com' per SSH Access Policy."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted."
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"arch_002_cleanup\"",
                "\"user_role\": \"data_analyst\"",
                "\"ssh_key_id\": \"carol_rsa_key\"",
                "\"security_clearance_status\": \"failed\"",
                "\"policy_violation_detected\": true",
                "\"cleanup_aborted\": true",
                "\"error_log_created\": true",
                "\"user_notified\": \"@luna.analyst\"",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_052",
        "instruction": "Conduct post-mortem security review 'SEC-REV-005' on failed archive task 'arch_005' by performing 'Pre-Execution Security Clearance Protocol' on original task parameters. The task was initiated by 'user_004' targeting 'personal-backup.company.com'. When policy violation is confirmed, log new, separate 'critical' 'permission_denied' security violation error using review ID. Escalate by notifying system administrators ('user_001', 'user_005') via 'System Alerts' channel with this message: 'CRITICAL SECURITY VIOLATION (SEC-REV-005): User @dave.intern (role: intern) attempted unauthorized archive operation to personal-backup.company.com. Key 'dave_rsa_key' is not authorized. cc @alice.admin @eve.manager'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_005"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "dave_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "SEC-REV-005",
                    "task_type": "security_review",
                    "user_id": "user_004",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User 'user_004' (intern) with key 'dave_rsa_key' attempted access to unauthorized server 'personal-backup.company.com'."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "CRITICAL SECURITY VIOLATION (SEC-REV-005): User @dave.intern (role: intern) attempted unauthorized archive operation to personal-backup.company.com. Key 'dave_rsa_key' is not authorized. cc @alice.admin @eve.manager"
                }
            }
        ],
        "outputs": [
                "\"review_id\": \"SEC-REV-005\"",
                "\"original_task_id\": \"arch_005\"",
                "\"policy_violation_confirmed\": true",
                "\"violating_user\": \"user_004\"",
                "\"unauthorized_server\": \"personal-backup.company.com\"",
                "\"security_error_logged\": true",
                "\"admin_1_contact\": \"@maya.admin\"",
                "\"admin_2_contact\": \"@aria.manager\"",
                "\"escalation_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_053",
        "instruction": "Conduct comprehensive 'System Readiness Assessment' for file organization task 'dir_op_001' before execution by following standard operational practice. Verify user's security clearance for target server 'server-data-01.company.com' and assess server's resource health against 60% operational threshold for CPU and memory. When server health check fails, follow standard procedure for postponing task by logging the issue, marking all constituent files of operation as 'failed' to halt execution, and alerting 'Operations' channel with this message: 'Task dir_op_001 postponed for user @bob.dev due to high resource usage on server-data-01.company.com (CPU: 62%, MEM: 72%).'",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "dir_op_001",
                    "task_type": "pre_execution_check",
                    "user_id": "user_002",
                    "error_type": "high_resource_usage",
                    "severity": "warning",
                    "details_json": {
                        "cpu_percent": 62,
                        "memory_percent": 72,
                        "threshold_percent": 60,
                        "action_taken": "deferred"
                    }
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "failed"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "Task dir_op_001 postponed for user @bob.dev due to high resource usage on server-data-01.company.com (CPU: 62%, MEM: 72%)."
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"dir_op_001\"",
                "\"security_clearance_status\": \"passed\"",
                "\"server_cpu_usage\": 62",
                "\"health_check_status\": \"failed\"",
                "\"warning_log_created\": true",
                "\"files_in_operation\": 6",
                "\"file_statuses_updated_to_failed\": 6",
                "\"user_notified\": \"@ryan.dev\"",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_054",
        "instruction": "Conduct comprehensive post-mortem on failed archive task 'arch_005' through dual investigation. Execute 'Task Failure Diagnosis Protocol' to confirm technical root cause first. Since task involved an intern, conduct mandatory 'Pre-Execution Security Clearance Protocol' as security review of original operation. Log findings for both technical failure and any discovered security violations. Conclude by sending comprehensive incident report to 'System Alerts', notifying responsible user and system administrators ('user_001', 'user_005') with this message: 'Post-mortem for arch_005 COMPLETE. Technical failure: Insufficient storage. Security review: Critical policy violation found. User: @dave.intern. See logs for details. cc @alice.admin @eve.manager'",
        "actions": [
            {
                "name": "GetErrorLogDetails",
                "arguments": {
                    "task_id": "arch_005"
                },
            },
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_005"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "dave_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_005",
                    "task_type": "archive",
                    "user_id": "user_004",
                    "error_type": "insufficient_remote_storage",
                    "severity": "medium",
                    "details_json": {
                        "reason": "Insufficient storage space on remote server personal-backup.company.com."
                    }
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_005",
                    "task_type": "security_review",
                    "user_id": "user_004",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User 'user_004' (intern) attempted access to unauthorized server 'personal-backup.company.com'."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Post-mortem for arch_005 COMPLETE. Technical failure: Insufficient storage. Security review: Critical policy violation found. User: @dave.intern. See logs for details. cc @alice.admin @eve.manager"
                }
            }
        ],
        "outputs": [
                "\"incident_task_id\": \"arch_005\"",
                "\"technical_root_cause\": \"Insufficient storage space\"",
                "\"security_review_status\": \"failed\"",
                "\"policy_violation_confirmed\": true",
                "\"technical_error_logged\": true",
                "\"security_error_logged\": true",
                "\"user_contact\": \"@ethan.intern\"",
                "\"admin_1_contact\": \"@maya.admin\"",
                "\"admin_2_contact\": \"@aria.manager\"",
                "\"slack_report_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_055",
        "instruction": "Handle pending file check task 'fc_task_001' by ensuring operation is fully compliant with all security policies through standard pre-execution clearance. After authorization, complete the task by following established file check protocol.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_001"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "eve_rsa_key"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "directory": "/var/log/applications"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_001",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_001",
                    "task_type": "file_check",
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "File Check"
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"fc_task_001\"",
                "\"security_clearance\": \"passed\"",
                "\"server_status\": \"online\"",
                "\"files_found_count\": 3",
                "\"task_status_updated\": true",
                "\"completion_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_056",
        "instruction": "Process file check task 'fc_task_004' by adhering to standard security procedure requiring full 'Pre-Execution Security Clearance Protocol' for requesting user ('user_002') on target server ('server-config.company.com'). When policy violation is discovered, halt operation, log 'critical' 'permission_denied' error detailing violation, and alert 'System Alerts' with this message: 'Task fc_task_004 aborted due to security policy violation. User @bob.dev does not have required permissions for server-config.company.com. See logs for details.'",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_004"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "fc_task_004",
                    "task_type": "file_check",
                    "user_id": "user_002",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User role 'developer' is not authorized for server 'server-config.company.com' per SSH Access Policy."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Task fc_task_004 aborted due to security policy violation. User @bob.dev does not have required permissions for server-config.company.com. See logs for details."
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"fc_task_004\"",
                "\"user_role\": \"developer\"",
                "\"ssh_key_id\": \"bob_rsa_key\"",
                "\"security_clearance_status\": \"failed\"",
                "\"policy_violation_detected\": true",
                "\"task_aborted\": true",
                "\"error_log_created\": true",
                "\"user_notified\": \"@ryan.dev\"",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_058",
        "instruction": "Fulfill analyst's ('user_003') request for recent application logs snapshot from 'server-prod-01.company.com' for performance investigation through assignment 'PROVISION-LOGS-001'. Identify relevant log files by applying criteria from standard maintenance task 'fc_task_001'. Securely copy identified files to new, temporary directory '/data/temp/log_snapshot_20240120/' on 'server-data-01.company.com' for analyst access. Facilitate transfer through administrator ('user_001'). Execute complete task, including database modification to update underlying maintenance task status and logging successful data provisioning.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_001"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "directory": "/var/log/applications"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/temp/log_snapshot_20240120"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "TransferFileToRemote",
                "arguments": {
                    "source_path": "/var/log/applications/webapp.log",
                    "remote_address": "server-data-01.company.com",
                    "destination_path": "/data/temp/log_snapshot_20240120/webapp.log",
                    "ssh_key": "alice_rsa_key"
                },
            },
            {
                "name": "TransferFileToRemote",
                "arguments": {
                    "source_path": "/var/log/applications/api_requests.log",
                    "remote_address": "server-data-01.company.com",
                    "destination_path": "/data/temp/log_snapshot_20240120/api_requests.log",
                    "ssh_key": "alice_rsa_key"
                },
            },
            {
                "name": "TransferFileToRemote",
                "arguments": {
                    "source_path": "/var/log/applications/error.log",
                    "remote_address": "server-data-01.company.com",
                    "destination_path": "/data/temp/log_snapshot_20240120/error.log",
                    "ssh_key": "alice_rsa_key"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_001",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "PROVISION-LOGS-001",
                    "task_type": "data_provisioning",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"fc_task_001\"",
                "\"files_identified_for_provisioning\": 3",
                "\"destination_directory_created\": true",
                "\"admin_key_retrieved\": \"alice_rsa_key\"",
                "\"files_transferred\": 3",
                "\"original_task_status_updated\": true",
                "\"provisioning_task_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_059",
        "instruction": "Handle incident 'INC-DIROP-001' regarding paused file organization task 'dir_op_001', halted due to low disk space warning, by re-assessing the situation. Perform full readiness check including verification of user's ('user_002') security clearance and re-validation of live disk space on 'server-data-01.company.com'. When space is now sufficient (more than 1GB available), proceed with complete 'File Organization Protocol'. Upon successful completion, log incident resolution and notify 'Operations' channel that task is now complete.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/csv"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/dat"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/json"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/miscellaneous"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/sorted/csv/sales_data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/sorted/csv/customer_info.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/data/sorted/dat/inventory.dat"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/data/sorted/json/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/readme.txt",
                    "destination_path": "/data/sorted/miscellaneous/readme.txt"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/sorted/csv/data_0.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "INC-DIROP-001",
                    "task_type": "incident_response",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"incident_id\": \"INC-DIROP-001\"",
                "\"original_task_id\": \"dir_op_001\"",
                "\"security_clearance\": \"passed\"",
                "\"disk_space_ok\": true",
                "\"files_to_process\": 6",
                "\"files_moved\": 6",
                "\"all_statuses_updated\": true",
                "\"incident_resolved_and_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_061",
        "instruction": "Execute dual-purpose task 'AUDIT-HYGIENE-01' with two components. Conduct security audit on user 'user_002' to ensure SSH key authorizations comply with 'SSH Access Policy', logging any discovered violations. Execute data hygiene task on 'server-data-01.company.com' following 'Stale File Cleanup Protocol' as defined by maintenance task 'fc_task_002'. Conclude by logging audit completion and sending comprehensive summary of all findings and actions to 'System Alerts' channel with this message: 'Audit & Cleanup AUDIT-HYGIENE-01 complete. Found 1 policy violation for user @bob.dev. Purged 1 stale file from server-data-01.com. See logs for details.'",
        "actions": [
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "AUDIT-HYGIENE-01",
                    "task_type": "security_audit",
                    "user_id": "user_002",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "unauthorized_server": "backup-server.company.com",
                        "policy_id": "sec_001"
                    }
                },
            },
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/temp_export_001.csv"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_002",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_002",
                    "task_type": "file_check",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "AUDIT-HYGIENE-01",
                    "task_type": "security_audit",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Audit & Cleanup AUDIT-HYGIENE-01 complete. Found 1 policy violation for user @bob.dev. Purged 1 stale file from server-data-01.com. See logs for details."
                }
            }
        ],
        "outputs": [
                "\"audit_id\": \"AUDIT-HYGIENE-01\"",
                "\"policy_violation_found\": true",
                "\"violation_logged\": true",
                "\"stale_files_identified\": 1",
                "\"files_purged\": 1",
                "\"cleanup_task_completed\": true",
                "\"cleanup_task_logged\": true",
                "\"overall_task_logged\": true",
                "\"violating_user_contact\": \"@ryan.dev\"",
                "\"slack_summary_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_066",
        "instruction": "Execute health audit 'HEALTH-AUDIT-02' by assessing 'server-prod-01.company.com' and 'server-data-01.company.com' health, enforcing 75% disk usage threshold. When server is found non-compliant, immediately escalate with alert then apply standard 'Stale File Cleanup Protocol' for that server using policies defined in maintenance task 'fc_task_002'. After remediation, log full audit and cleanup operation using ID 'HEALTH-AUDIT-02' and send comprehensive summary of actions to 'Operations' channel with this message: 'System Health Audit HEALTH-AUDIT-02 complete. server-data-01.company.com exceeded disk threshold and was remediated by purging 2 stale files. server-prod-01.company.com is healthy.'",
        "actions": [
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "HEALTH-AUDIT-02: Disk usage on server-data-01.company.com (78%) exceeds 75% threshold. Initiating cleanup."
                },
            },
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/temp_export_001.csv"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/cache_backup.dat"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_002",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "HEALTH-AUDIT-02",
                    "task_type": "system_health_audit",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "System Health Audit HEALTH-AUDIT-02 complete. server-data-01.company.com exceeded disk threshold and was remediated by purging 2 stale files. server-prod-01.company.com is healthy."
                }
            }
        ],
        "outputs": [
                "\"servers_checked\": 2",
                "\"threshold_breached_on\": \"server-data-01.company.com\"",
                "\"slack_alert_sent\": true",
                "\"cleanup_protocol_initiated\": true",
                "\"files_purged_count\": 2",
                "\"cleanup_task_status_updated\": true",
                "\"audit_operation_logged\": true",
                "\"slack_summary_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_068",
        "instruction": "Enforce data retention policy for temporary files on 'server-data-01.company.com' through assignment 'QUARANTINE-STALE-01'. Identify all stale files in '/data/temp' directory by applying rules defined in maintenance task 'fc_task_002'. Instead of purging, quarantine these files for manual review by relocating all identified files to new directory '/data/quarantine/stale_files_20240120/'. Execute the complete task, including database modification to update underlying maintenance task status, logging successful quarantine operation, and sending message to 'Operations' slack channel.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/quarantine/stale_files_20240120"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/temp/temp_export_001.csv",
                    "destination_path": "/data/quarantine/stale_files_20240120/temp_export_001.csv"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/temp/cache_backup.dat",
                    "destination_path": "/data/quarantine/stale_files_20240120/cache_backup.dat"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_002",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "QUARANTINE-STALE-01",
                    "task_type": "data_quarantine",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"fc_task_002\"",
                "\"files_identified_for_quarantine\": 2",
                "\"quarantine_directory_created\": true",
                "\"files_moved_to_quarantine\": 2",
                "\"original_task_status_updated\": true",
                "\"quarantine_task_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_069",
        "instruction": "Handle final data lifecycle stage of completed archive task 'arch_002' by purging all original source files. Perform 'Pre-Execution Security Clearance Protocol' before any deletions to ensure original user ('user_003') is authorized for source server 'server-analytics.company.com'. When policy violation is discovered, halt cleanup, update archive task status to 'failed', log security failure, and escalate to 'System Alerts' with this message: 'HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted.'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_002"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "carol_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_002",
                    "status": "failed"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_002",
                    "task_type": "archive_cleanup",
                    "user_id": "user_003",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User role 'data_analyst' is not authorized for server 'server-analytics.company.com' per SSH Access Policy."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted."
                }
            }
        ],
        "outputs": [
                "\"archive_id\": \"arch_002\"",
                "\"user_role\": \"data_analyst\"",
                "\"security_clearance_status\": \"failed\"",
                "\"policy_violation_detected\": true",
                "\"task_status_updated\": \"failed\"",
                "\"cleanup_aborted\": true",
                "\"error_log_created\": true",
                "\"user_notified\": \"@luna.analyst\"",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_071",
        "instruction": "Validate file organization mandate 'dir_op_001' through integrity audit 'AUDIT-DIR-OP-001' before execution by validating every file listed in operation's manifest on 'server-data-01.company.com'. Follow standard integrity verification practice including checking file existence and validating live checksums against recorded values. When any validation failure is discovered, follow standard protocol for failed audit: halt operation by updating all relevant database records to prevent execution, log specific failure, and escalate issue to 'System Alerts' with this message: 'AUDIT-DIR-OP-001 FAILED: Integrity check failed for dir_op_001 on server-data-01.company.com. File not found: /data/unsorted/inventory.dat. Operation halted.'",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/sales_data.csv"
                },
            },
            {
                "name": "GetRemoteFileChecksum",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/sales_data.csv"
                },
            },
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/inventory.dat"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "AUDIT-DIR-OP-001",
                    "task_type": "pre_flight_audit",
                    "user_id": "user_002",
                    "error_type": "file_not_found",
                    "severity": "critical",
                    "details_json": {
                        "filepath": "/data/unsorted/inventory.dat",
                        "server": "server-data-01.company.com"
                    }
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "failed"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "AUDIT-DIR-OP-001 FAILED: Integrity check failed for dir_op_001 on server-data-01.company.com. File not found: /data/unsorted/inventory.dat. Operation halted."
                }
            }
        ],
        "outputs": [
                "\"audit_id\": \"AUDIT-DIR-OP-001\"",
                "\"files_to_audit\": 6",
                "\"files_verified_ok\": 1",
                "\"audit_failed\": true",
                "\"failing_file\": \"/data/unsorted/inventory.dat\"",
                "\"error_log_created\": true",
                "\"files_in_operation\": 6",
                "\"file_statuses_updated_to_failed\": 6",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_073",
        "instruction": "Handle final data lifecycle stage of completed archive task 'arch_002' by purging all original source files. Perform 'Pre-Execution Security Clearance Protocol' before any deletions to ensure original user ('user_003') is authorized for source server 'server-analytics.company.com'. When policy violation is discovered, halt cleanup, update archive task status to 'failed', log security failure, and escalate to 'System Alerts' with this message: 'HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted.'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_002"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "carol_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_002",
                    "status": "failed"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_002",
                    "task_type": "archive_cleanup",
                    "user_id": "user_003",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User role 'data_analyst' is not authorized for server 'server-analytics.company.com' per SSH Access Policy."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted."
                }
            }
        ],
        "outputs": [
                "\"archive_id\": \"arch_002\"",
                "\"user_role\": \"data_analyst\"",
                "\"security_clearance_status\": \"failed\"",
                "\"policy_violation_detected\": true",
                "\"task_status_updated\": \"failed\"",
                "\"cleanup_aborted\": true",
                "\"error_log_created\": true",
                "\"user_notified\": \"@luna.analyst\"",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_075",
        "instruction": "Re-assess file organization task 'dir_op_001' through incident 'INC-DIROP-RETRY-01', previously deferred due to high resource load on 'server-data-01.company.com'. Perform full readiness check including verification of user's ('user_002') security clearance and re-validation of server's live resource usage against 60% operational threshold. When server is still under excessive load, follow standard deferral protocol: log reason, update status of all files in operation to 'failed' to prevent re-queueing, and notify 'Operations' channel with this message: 'Task dir_op_001 for @bob.dev has been deferred again due to persistent high resource usage (CPU: 62%, MEM: 72%) on server-data-01.company.com.'",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "dir_op_001",
                    "task_type": "pre_execution_check",
                    "user_id": "user_002",
                    "error_type": "high_resource_usage",
                    "severity": "warning",
                    "details_json": {
                        "cpu_percent": 62,
                        "memory_percent": 72,
                        "threshold_percent": 60,
                        "action_taken": "deferred"
                    }
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "failed"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "Task dir_op_001 for @bob.dev has been deferred again due to persistent high resource usage (CPU: 62%, MEM: 72%) on server-data-01.company.com."
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"dir_op_001\"",
                "\"security_clearance_status\": \"passed\"",
                "\"server_cpu_usage\": 62",
                "\"health_check_status\": \"failed\"",
                "\"warning_log_created\": true",
                "\"files_in_operation\": 6",
                "\"file_statuses_updated_to_failed\": 6",
                "\"user_notified\": \"@ryan.dev\"",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_076",
        "instruction": "Conduct 'System Readiness Assessment' for file organization task 'dir_op_001' with three required conditions: 1. Available disk space on 'server-data-01.company.com' must be at least 20% greater than total size of files in operation's manifest. 2. Server's real-time CPU and memory usage must both be at or below 70% operational threshold. 3. Requesting user ('user_002') must be authorized for server. When operational threshold is exceeded, follow appropriate practice to defer task by logging issue, updating status of all files in operation to 'failed' to halt execution, and alerting 'System Alerts'.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "dir_op_001",
                    "task_type": "pre_execution_check",
                    "user_id": "user_002",
                    "error_type": "high_resource_usage",
                    "severity": "warning",
                    "details_json": {
                        "server": "server-data-01.company.com",
                        "memory_percent": 72,
                        "threshold_percent": 70
                    }
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "failed"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "failed"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                }
            }
        ],
        "outputs": [
                "\"operation_id\": \"dir_op_001\"",
                "\"disk_space_ok\": true",
                "\"user_auth_ok\": true",
                "\"memory_usage_percent\": 72",
                "\"health_check_failed\": true",
                "\"warning_logged\": true",
                "\"files_halted\": 6",
                "\"task_deferred\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_077",
        "instruction": "Assess health of 'server-data-01.company.com' and 'storage-01.company.com' against 75% utilization threshold for audit 'HEALTH-AUDIT-DATA-TIER-02'. Follow standard practice for responding to health alerts. When server is non-compliant and has defined cleanup task (e.g., 'fc_task_002' for 'server-data-01.company.com'), apply full 'Stale File Cleanup Protocol'. For any other non-compliant server, log 'high_resource_usage' warning and escalate to system administrators ('user_001', 'user_005') via 'System Alerts'. After addressing all findings, log audit completion and send summary to 'Operations'.",
        "actions": [
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "storage-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "storage-01.company.com"
                },
            },
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/temp_export_001.csv"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/cache_backup.dat"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_002",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_002",
                    "task_type": "file_check",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "File Check"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "HEALTH-AUDIT-DATA-TIER-02",
                    "task_type": "health_check",
                    "user_id": "system_agent",
                    "error_type": "high_resource_usage",
                    "severity": "warning",
                    "details_json": {
                        "server": "storage-01.company.com",
                        "disk_percent": 82
                    }
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "HEALTH-AUDIT-DATA-TIER-02",
                    "task_type": "system_health_audit",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"servers_audited\": 2",
                "\"remediation_initiated_for\": \"server-data-01.company.com\"",
                "\"files_purged\": 2",
                "\"cleanup_protocol_complete\": true",
                "\"warning_logged_for\": \"storage-01.company.com\"",
                "\"escalation_sent_for_storage\": true",
                "\"audit_complete_and_logged\": true",
                "\"slack_summary_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_080",
        "instruction": "Oversee execution of file organization mandate 'dir_op_002' for task 'DEP-OP-002', permitted only when target server 'server-data-01.company.com' satisfies disk usage threshold of 75% or lower. When threshold is exceeded, enforce stale file policy defined in 'fc_task_002' to remediate server state before organization task can proceed. Verify user 'user_001' passes security clearance under 'SSH Access Policy' for the operation. After environment complies with these prerequisites, complete 'File Organization Protocol' for 'dir_op_002' with all activities properly logged and notifications dispatched to designated Slack channels.",
        "actions": [
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/temp_export_001.csv"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_002",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_002",
                    "task_type": "file_check",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "File Check"
                },
            },
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_002"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "alice_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_002"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/archive/projects/documents"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/archive/projects/source_code"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/tmp/project_files/project_spec.pdf",
                    "destination_path": "/archive/projects/documents/project_spec.pdf"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_007",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/tmp/project_files/src/main.py",
                    "destination_path": "/archive/projects/source_code/main.py"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_008",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "DEP-OP-002",
                    "task_type": "file_organization",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"dependency_check_passed\": true",
                "\"cleanup_protocol_initiated\": true",
                "\"files_purged\": 1",
                "\"cleanup_task_logged\": true",
                "\"security_clearance_passed\": true",
                "\"main_operation_files_moved\": 2",
                "\"main_operation_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_081",
        "instruction": "Handle incident 'INC-DIROP-PARTIAL-01' where file organization task 'dir_op_001' was deferred due to high server load and user ('user_002') has requested partial execution. Re-assess the situation by verifying server's ('server-data-01.company.com') current resource usage is below 80% operational threshold. When healthy, proceed with modified 'File Organization Protocol' by moving only CSV files to their correct destination. Move all other files (DAT, JSON, TXT) to new '/data/deferred/' directory for later processing. Update status for every file in manifest. Conclude by logging partial completion and notifying 'Operations' with detailed summary of which files were moved where.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/sorted/csv"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/data/deferred"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/data/sorted/csv/sales_data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/customer_info.csv",
                    "destination_path": "/data/sorted/csv/customer_info.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_002",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/subdir/data.csv",
                    "destination_path": "/data/sorted/csv/data_0.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_006",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/inventory.dat",
                    "destination_path": "/data/deferred/inventory.dat"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_003",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/config.json",
                    "destination_path": "/data/deferred/config.json"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_004",
                    "status": "completed"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/readme.txt",
                    "destination_path": "/data/deferred/readme.txt"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_005",
                    "status": "completed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "INC-DIROP-PARTIAL-01",
                    "task_type": "incident_response",
                    "user_id": "user_002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "Incident INC-DIROP-PARTIAL-01: Partial completion for dir_op_001. CSV files moved to /data/sorted/csv. Non-CSV files moved to /data/deferred for later processing."
                }
            }
        ],
        "outputs": [
                "\"server_health_ok\": true",
                "\"directories_created\": 2",
                "\"csv_files_moved\": 3",
                "\"other_files_deferred\": 3",
                "\"all_statuses_updated\": true",
                "\"partial_completion_logged\": true",
                "\"slack_summary_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_083",
        "instruction": "Manage immediate staging of critical sales data file from pending sorting job 'dir_op_001' for high-priority analysis through assignment 'PRIORITY-DATA-STAGING-001' on 'server-data-01.company.com'. Before relocation, follow standard readiness assessment practice including security clearance for developer ('user_002') and, crucially, verify integrity of target sales data file to prevent processing corrupt data. After validation, relocate file to new staging directory '/staging/priority_review/20240120/'. Execute complete task including database modification to update moved file status and logging successful staging. Conclude by notifying developer that file is ready for analysis with this message: 'Priority Staging Complete for PRIORITY-DATA-STAGING-001: The file sales_data.csv has been validated and moved to the priority review directory. cc @bob.dev'",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetRemoteFileChecksum",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/sales_data.csv"
                },
            },
            {
                "name": "CreateDirectoryOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory_path": "/staging/priority_review/20240120"
                },
            },
            {
                "name": "MoveFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "source_path": "/data/unsorted/sales_data.csv",
                    "destination_path": "/staging/priority_review/20240120/sales_data.csv"
                },
            },
            {
                "name": "UpdateDirectoryOperationStatus",
                "arguments": {
                    "file_id": "file_001",
                    "status": "completed"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "PRIORITY-DATA-STAGING-001",
                    "task_type": "data_staging",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "Priority Staging Complete for PRIORITY-DATA-STAGING-001: The file sales_data.csv has been validated and moved to the priority review directory. cc @bob.dev"
                }
            }
        ],
        "outputs": [
                "\"policy_task_id\": \"dir_op_001\"",
                "\"security_clearance_status\": \"passed\"",
                "\"files_identified_for_staging\": 1",
                "\"source_file_integrity_verified\": true",
                "\"staging_directory_created\": true",
                "\"files_moved_to_staging\": 1",
                "\"original_task_file_updated\": 1",
                "\"developer_contact_retrieved\": \"@ryan.dev\"",
                "\"staging_task_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_085",
        "instruction": "Handle final data lifecycle stage of completed archive task 'arch_001' by purging all original source files from 'server-prod-01.company.com'. Perform 'Pre-Execution Security Clearance Protocol' before any deletions to ensure original user ('user_001') is authorized. After clearance, retrieve archive's file manifest and systematically delete every source file listed. Following complete purging, update archive status to 'verified' via database write, signifying lifecycle completion. Conclude by logging cleanup operation ('CLEANUP-ARCH-001') and notifying 'Operations'.",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "alice_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/src/main.js"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/src/utils.js"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/config/database.json"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/docs/readme.md"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/tests/unit_tests.py"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_001",
                    "status": "verified"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "CLEANUP-ARCH-001",
                    "task_type": "archive_cleanup",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations"
                }
            }
        ],
        "outputs": [
                "\"archive_id\": \"arch_001\"",
                "\"security_clearance\": \"passed\"",
                "\"source_files_identified\": 5",
                "\"source_files_deleted\": 5",
                "\"task_status_updated\": \"verified\"",
                "\"cleanup_operation_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_086",
        "instruction": "Conduct pre-flight security audit for archive task 'arch_004' by enforcing all security protocols before execution. Apply Pre-Execution Security Clearance practice for requesting user ('user_005') against target server 'document-vault.company.com'. When security policy violation is discovered, immediately halt operation, update archive task status to 'failed' via database writes, log 'critical' 'permission_denied' error detailing exact violation, and escalate incident by notifying 'System Alerts' channel with this message: 'Task arch_004 HALTED on security violation. User @eve.manager key is not authorized for document-vault.company.com.'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_004"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "eve_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_004",
                    "status": "failed"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_004",
                    "task_type": "security_audit",
                    "user_id": "user_005",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "Key 'eve_rsa_key' is not authorized for server 'document-vault.company.com' as per its authorized_servers list."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Task arch_004 HALTED on security violation. User @eve.manager key is not authorized for document-vault.company.com."
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"arch_004\"",
                "\"user_role\": \"project_manager\"",
                "\"ssh_key_id\": \"eve_rsa_key\"",
                "\"authorization_check\": \"failed\"",
                "\"policy_violation_confirmed\": true",
                "\"task_status_updated\": \"failed\"",
                "\"security_error_logged\": true",
                "\"user_contact\": \"@aria.manager\"",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_088",
        "instruction": "Handle final data lifecycle stage of completed archive task 'arch_001' by purging all original source files from 'server-prod-01.company.com'. Perform 'Pre-Execution Security Clearance Protocol' before any deletions to ensure original user ('user_001') is authorized. After clearance, retrieve archive's file manifest and systematically delete every source file. Following purging, update archive status to 'verified' via database write, signifying lifecycle completion. Conclude by logging cleanup operation ('CLEANUP-ARCH-001') and notifying 'Operations' with this message: 'Lifecycle for arch_001 complete. Source files have been purged and task is now verified.'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_001"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "alice_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/src/main.js"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/src/utils.js"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/config/database.json"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/docs/readme.md"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-prod-01.company.com",
                    "filepath": "/home/projects/webapp/tests/unit_tests.py"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_001",
                    "status": "verified"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "CLEANUP-ARCH-001",
                    "task_type": "archive_cleanup",
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "Lifecycle for arch_001 complete. Source files have been purged and task is now verified."
                }
            }
        ],
        "outputs": [
                "\"archive_id\": \"arch_001\"",
                "\"security_clearance\": \"passed\"",
                "\"source_files_identified\": 5",
                "\"source_files_deleted\": 5",
                "\"task_status_updated\": \"verified\"",
                "\"cleanup_operation_logged\": true",
                "\"slack_notification_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_090",
        "instruction": "Perform post-archive cleanup for 'arch_002' following protocol requiring full security clearance check before deleting any files. Validate that original user ('user_003') has authorized access to source server ('server-analytics.company.com') per 'SSH Access Policy'. When policy violation is discovered, halt cleanup, log critical 'permission_denied' error via database write, update archive status to 'failed', and escalate to 'System Alerts' channel with this message: 'HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted.'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_002"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "carol_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_002_cleanup",
                    "task_type": "security_check",
                    "user_id": "user_003",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User role 'data_analyst' is not authorized for server 'server-analytics.company.com' per SSH Access Policy."
                    }
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_002",
                    "status": "failed"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_003"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted."
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"arch_002_cleanup\"",
                "\"user_role\": \"data_analyst\"",
                "\"ssh_key_id\": \"carol_rsa_key\"",
                "\"security_clearance_status\": \"failed\"",
                "\"policy_violation_detected\": true",
                "\"cleanup_aborted\": true",
                "\"error_log_created\": true",
                "\"task_status_updated\": \"failed\"",
                "\"user_notified\": \"@luna.analyst\"",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_091",
        "instruction": "Verify integrity of all source files intended for archive through pre-flight audit 'arch_preflight_006'. The manifest includes: `['/data/unsorted/sales_data.csv', '/data/unsorted/customer_info.csv', '/data/unsorted/non_existent_report.csv']` on server `server-data-01.company.com`. Follow standard practice to check existence of each file. When any file fails validation, halt, log 'file_not_found' failure against audit task ID, and alert 'Operations' with this message: 'Pre-flight audit arch_preflight_006 FAILED: Source file /data/unsorted/non_existent_report.csv not found on server-data-01.company.com. Archival process halted.'",
        "actions": [
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/sales_data.csv"
                },
            },
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/customer_info.csv"
                },
            },
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/non_existent_report.csv"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_preflight_006",
                    "task_type": "pre_flight_audit",
                    "user_id": "system_agent",
                    "error_type": "file_not_found",
                    "severity": "critical",
                    "details_json": {
                        "filepath": "/data/unsorted/non_existent_report.csv",
                        "server": "server-data-01.company.com"
                    }
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "Pre-flight audit arch_preflight_006 FAILED: Source file /data/unsorted/non_existent_report.csv not found on server-data-01.company.com. Archival process halted."
                }
            }
        ],
        "outputs": [
                "\"audit_id\": \"arch_preflight_006\"",
                "\"files_to_verify\": 3",
                "\"files_verified_ok\": 2",
                "\"verification_failed\": true",
                "\"missing_file\": \"/data/unsorted/non_existent_report.csv\"",
                "\"error_logged\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_092",
        "instruction": "Audit pending archive task 'arch_003' for user 'user_002' by conducting comprehensive System Readiness Assessment. Perform 'Pre-Execution Security Clearance Protocol' to validate user's access to destination server 'log-storage.company.com'. When security check fails, follow standard procedure to halt operation immediately, log critical error detailing specific failure, update task status to 'failed', and escalate to 'System Alerts' with detailed message.",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_003"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "bob_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_003",
                    "status": "failed"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "arch_003",
                    "task_type": "pre_execution_check",
                    "user_id": "user_002",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User 'user_002' with role 'developer' is not authorized for server 'log-storage.company.com' per SSH Access Policy."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Pre-flight check for task arch_003 failed: Security clearance denied for user @bob.dev on server log-storage.company.com. Task aborted."
                }
            }
        ],
        "outputs": [
                "\"task_id\": \"arch_003\"",
                "\"user_id\": \"user_002\"",
                "\"security_clearance_status\": \"failed\"",
                "\"policy_violation_detected\": true",
                "\"task_status_updated_to\": \"failed\"",
                "\"error_log_created\": true",
                "\"user_notified\": \"@ryan.dev\"",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_093",
        "instruction": "Assess health of primary servers 'server-prod-01.company.com' and 'server-data-01.company.com' against 75% disk usage threshold for audit 'HEALTH-AUDIT-PRIMARY-01'. When server is non-compliant, immediately escalate by sending alert then apply standard 'Stale File Cleanup Protocol' for that server using policies from maintenance task 'fc_task_002'. After addressing all findings, log completion of full audit and send summary report of actions to 'Operations' with this message: 'HEALTH-AUDIT-PRIMARY-01 complete. Server server-data-01.company.com remediated (2 files purged). Server server-prod-01.company.com is healthy.'",
        "actions": [
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-prod-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "HEALTH-AUDIT-PRIMARY-01: Disk usage on server-data-01.company.com (78%) exceeds threshold. Initiating automated cleanup."
                },
            },
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/temp_export_001.csv"
                },
            },
            {
                "name": "DeleteFileOnRemote",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/temp/cache_backup.dat"
                },
            },
            {
                "name": "UpdateFileCheckTaskStatus",
                "arguments": {
                    "task_id": "fc_task_002",
                    "completed": true
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "fc_task_002",
                    "task_type": "file_check",
                    "user_id": "user_001"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "HEALTH-AUDIT-PRIMARY-01",
                    "task_type": "system_health_audit",
                    "user_id": "system_agent"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "HEALTH-AUDIT-PRIMARY-01 complete. Server server-data-01.company.com remediated (2 files purged). Server server-prod-01.company.com is healthy."
                }
            }
        ],
        "outputs": [
                "\"servers_audited\": 2",
                "\"server-prod-01_status\": \"healthy\"",
                "\"server-data-01_status\": \"unhealthy\"",
                "\"remediation_initiated\": true",
                "\"files_purged_count\": 2",
                "\"cleanup_task_logged\": true",
                "\"audit_complete_and_logged\": true",
                "\"slack_summary_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_094",
        "instruction": "Conduct mandatory pre-flight integrity audit before file organization task 'dir_op_001' can proceed by validating every file listed in operation's manifest. For each file, confirm existence on source server ('server-data-01.company.com') and verify that live checksum matches checksum recorded in manifest. When any file fails validation, immediately halt process, log 'file_not_found' error with relevant details, and alert 'System Alerts'. When all files are verified, log successful audit and notify 'Operations' that organization task is cleared for execution.",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/sales_data.csv"
                },
            },
            {
                "name": "GetRemoteFileChecksum",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/sales_data.csv"
                },
            },
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/customer_info.csv"
                },
            },
            {
                "name": "GetRemoteFileChecksum",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/customer_info.csv"
                },
            },
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/inventory.dat"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "dir_op_001",
                    "task_type": "pre_flight_audit",
                    "user_id": "user_002",
                    "error_type": "file_not_found",
                    "severity": "critical",
                    "details_json": {
                        "filepath": "/data/unsorted/inventory.dat"
                    }
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts"
                }
            }
        ],
        "outputs": [
                "\"operation_id\": \"dir_op_001\"",
                "\"files_to_audit\": 6",
                "\"files_verified\": 2",
                "\"audit_failed\": true",
                "\"failing_file\": \"/data/unsorted/inventory.dat\"",
                "\"error_log_created\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_095",
        "instruction": "Verify operation compliance for completed file check task 'fc_task_005' through audit 'AUDIT-FC-005'. Follow appropriate practice including 'Pre-Execution File Transfer Security Clearance Protocol' for original user ('user_004'). When security violation is discovered, halt, log violation, and escalate. When compliant, retrieve task's completion message to find its log file and archive it to 'backup-server.company.com' in '/storage/audit_evidence/' directory.",
        "actions": [
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_005"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetUserDefaultSshKey",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "GetSshKeyById",
                "arguments": {
                    "key_id": "dave_rsa_key"
                },
            },
            {
                "name": "GetSecurityPolicyByName",
                "arguments": {
                    "policy_name": "SSH Access Policy"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "AUDIT-FC-005",
                    "task_type": "compliance_audit",
                    "user_id": "user_004",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User 'ethan_intern' (intern) is not authorized for server 'server-prod-01.company.com' per SSH Access Policy."
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_004"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "AUDIT-FC-005 FAILURE: Security violation detected for user @dave.intern during post-execution audit of fc_task_005. Operation was non-compliant."
                }
            }
        ],
        "outputs": [
                "\"audit_id\": \"AUDIT-FC-005\"",
                "\"original_task_id\": \"fc_task_005\"",
                "\"user_role\": \"intern\"",
                "\"security_clearance_status\": \"failed\"",
                "\"policy_violation_detected\": true",
                "\"audit_halted\": true",
                "\"error_log_created\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_096",
        "instruction": "Execute 'Proactive Server Health Check Protocol' with 70% utilization threshold for incident 'HRA-SRVDATA-01' regarding high resource usage on 'server-data-01.company.com'. When breached, escalate with forensic analysis of '/data/temp' directory against policy defined in task 'fc_task_002'. Log 'warning' severity 'high_resource_usage' error using incident ID, detailing breached metrics and count of policy-violating files. Conclude by alerting 'System Alerts' with structured message including incident ID, server name, and number of non-compliant files found.",
        "actions": [
            {
                "name": "GetServerResourceUsage",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "CheckRemoteDiskSpace",
                "arguments": {
                    "hostname": "server-data-01.company.com"
                },
            },
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_002"
                },
            },
            {
                "name": "ScanRemoteDirectory",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "directory": "/data/temp"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "HRA-SRVDATA-01",
                    "task_type": "system_monitoring",
                    "user_id": "system_agent",
                    "error_type": "high_resource_usage",
                    "severity": "warning",
                    "details_json": {
                        "server": "server-data-01.company.com",
                        "memory_percent": 72,
                        "disk_percent": 78,
                        "non_compliant_files_count": 1
                    }
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "Health Alert (HRA-SRVDATA-01): server-data-01.company.com has breached resource thresholds (MEM: 72%, DSK: 78%). Found 1 non-compliant file in /data/temp."
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "HRA-SRVDATA-01",
                    "task_type": "system_monitoring",
                    "user_id": "system_agent"
                }
            }
        ],
        "outputs": [
                "\"incident_id\": \"HRA-SRVDATA-01\"",
                "\"threshold_exceeded\": true",
                "\"memory_usage\": 72",
                "\"disk_usage\": 78",
                "\"non_compliant_files_found\": 1",
                "\"warning_log_created\": true",
                "\"slack_alert_sent\": true",
                "\"investigation_complete\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_097",
        "instruction": "Conduct root cause analysis 'RCA-FC-004' regarding 'connection_timeout' error on file check task 'fc_task_004' for user 'user_002'. Follow appropriate diagnostic practice by retrieving original error log to identify server and confirm its live status. When server is confirmed to be in maintenance, log new 'server_maintenance' error for this RCA task with 'medium' severity, summarizing findings. Conclude by notifying user and their manager ('user_005') in 'Operations' channel with this message: 'RCA for fc_task_004 complete: Failure was due to scheduled maintenance on server-config.company.com. No further action needed. cc @eve.manager @bob.dev'",
        "actions": [
            {
                "name": "GetErrorLogDetails",
                "arguments": {
                    "task_id": "fc_task_004"
                },
            },
            {
                "name": "GetFileCheckTaskById",
                "arguments": {
                    "task_id": "fc_task_004"
                },
            },
            {
                "name": "GetServerStatusByHostname",
                "arguments": {
                    "hostname": "server-config.company.com"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "RCA-FC-004",
                    "task_type": "forensics",
                    "user_id": "user_002",
                    "error_type": "server_maintenance",
                    "severity": "medium",
                    "details_json": {
                        "reason": "Server confirmed to be in maintenance mode.",
                        "original_task": "fc_task_004"
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_002"
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_005"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "RCA for fc_task_004 complete: Failure was due to scheduled maintenance on server-config.company.com. No further action needed. cc @eve.manager @bob.dev"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "RCA-FC-004",
                    "task_type": "investigation",
                    "user_id": "system_agent"
                }
            }
        ],
        "outputs": [
                "\"rca_task_id\": \"RCA-FC-004\"",
                "\"original_error_confirmed\": \"Connection timeout\"",
                "\"live_server_status\": \"maintenance\"",
                "\"root_cause_confirmed\": \"Server maintenance\"",
                "\"incident_log_created\": true",
                "\"user_notified\": \"@ryan.dev\"",
                "\"manager_notified\": \"@aria.manager\"",
                "\"investigation_logged\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_098",
        "instruction": "Move project files as defined in 'dir_op_001' on server 'server-data-01.company.com' for migration 'MIGRATE-PROJECTS-001'. Before migration, verify integrity of every file in manifest by following appropriate integrity verification practice through checking each file's existence and validating live checksum. When any file fails validation, halt operation, log 'file_not_found' error, and escalate to 'Operations' with this message: 'MIGRATE-PROJECTS-001 HALTED: Pre-flight integrity check failed. File not found: /data/unsorted/inventory.dat. Migration aborted.'",
        "actions": [
            {
                "name": "GetDirectoryOperationById",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "GetFilesForDirectoryOperation",
                "arguments": {
                    "operation_id": "dir_op_001"
                },
            },
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/sales_data.csv"
                },
            },
            {
                "name": "GetRemoteFileChecksum",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/sales_data.csv"
                },
            },
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/customer_info.csv"
                },
            },
            {
                "name": "GetRemoteFileChecksum",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/customer_info.csv"
                },
            },
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "server-data-01.company.com",
                    "filepath": "/data/unsorted/inventory.dat"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "MIGRATE-PROJECTS-001",
                    "task_type": "file_migration",
                    "user_id": "user_002",
                    "error_type": "file_not_found",
                    "severity": "critical",
                    "details_json": {
                        "filepath": "/data/unsorted/inventory.dat",
                        "server": "server-data-01.company.com"
                    }
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "Operations",
                    "message": "MIGRATE-PROJECTS-001 HALTED: Pre-flight integrity check failed. File not found: /data/unsorted/inventory.dat. Migration aborted."
                }
            }
        ],
        "outputs": [
                "\"migration_task_id\": \"MIGRATE-PROJECTS-001\"",
                "\"files_to_verify\": 6",
                "\"integrity_check_passed_for\": 2",
                "\"integrity_check_failed\": true",
                "\"failing_file\": \"/data/unsorted/inventory.dat\"",
                "\"operation_halted\": true",
                "\"error_log_created\": true",
                "\"slack_alert_sent\": true"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "USER_100",
        "instruction": "Verify operation's final state and compliance for post-completion audit 'AUDIT-ARCH-001' where archive task 'arch_001' was reported as having transfer integrity issues. Locate final archive file on 'backup-server.company.com' based on details from original task instructions and related error logs. When file is missing, log 'critical' 'file_not_found' error against this audit task and escalate to 'System Alerts' with this message: 'AUDIT FAILURE (AUDIT-ARCH-001): Final archive for task arch_001 is MISSING from destination. Immediate investigation required. cc @alice.admin'",
        "actions": [
            {
                "name": "GetArchiveInstructionsById",
                "arguments": {
                    "archive_id": "arch_001"
                },
            },
            {
                "name": "GetErrorLogDetails",
                "arguments": {
                    "task_id": "arch_001"
                },
            },
            {
                "name": "CheckRemoteFileExists",
                "arguments": {
                    "hostname": "backup-server.company.com",
                    "filepath": "/tmp/archives/project_backup_2024_20240115_160000.tar.gz"
                },
            },
            {
                "name": "GetUserInfoById",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "LogErrorMessage",
                "arguments": {
                    "task_id": "AUDIT-ARCH-001",
                    "task_type": "security_audit",
                    "user_id": "user_001",
                    "error_type": "file_not_found",
                    "severity": "critical",
                    "details_json": {
                        "server": "backup-server.company.com",
                        "filepath": "/tmp/archives/project_backup_2024_20240115_160000.tar.gz"
                    }
                },
            },
            {
                "name": "GetUserContactInfo",
                "arguments": {
                    "user_id": "user_001"
                },
            },
            {
                "name": "SendSlackMessage",
                "arguments": {
                    "channel_name": "System Alerts",
                    "message": "AUDIT FAILURE (AUDIT-ARCH-001): Final archive for task arch_001 is MISSING from destination. Immediate investigation required. cc @alice.admin"
                },
            },
            {
                "name": "UpdateArchiveTaskStatus",
                "arguments": {
                    "archive_id": "arch_001",
                    "status": "failed"
                },
            },
            {
                "name": "LogTaskCompletion",
                "arguments": {
                    "task_id": "AUDIT-ARCH-001",
                    "task_type": "security_audit",
                    "user_id": "system_agent"
                }
            }
        ],
        "outputs": [
                "\"audit_id\": \"AUDIT-ARCH-001\"",
                "\"archive_existence_verified\": false",
                "\"error_log_created\": true",
                "\"slack_escalation_sent\": true",
                "\"original_task_status_updated\": \"failed\"",
                "\"audit_logged_as_complete\": true"
        ]
    }
]
