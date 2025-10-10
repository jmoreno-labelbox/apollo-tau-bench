from domains.dto import Task, Action

TASKS = [



    Task(
        annotator="0",
        user_id="USER_106",
        instruction=(
            "You are a Security Analyst assigned to 'SEC-REVIEW-CONFIG-01'. Your objective is to isolate potentially sensitive configuration files from the pending file organization task 'dir_op_001' for a security review. You must identify all '.dat' and '.json' files within the operation's manifest on 'server-data-01.company.com'. Instead of allowing them to be sorted, your directive is to quarantine these specific files by relocating them to a new secure directory, '/secure/quarantine/config_review_20240120/'. You are responsible for the full execution of this task, including performing database modifications to update the status of the moved files and logging the successful quarantine operation."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/secure/quarantine/config_review_20240120"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/secure/quarantine/config_review_20240120/inventory.dat"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/secure/quarantine/config_review_20240120/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "SEC-REVIEW-CONFIG-01", "task_type": "security_quarantine", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"})
        ],
        outputs=[
            '"policy_task_id": "dir_op_001"',
            '"files_identified_for_quarantine": 2',
            '"quarantine_directory_created": true',
            '"files_moved_to_quarantine": 2',
            '"original_task_files_updated": 2',
            '"quarantine_task_logged": true',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_104",
        instruction=(
            "You are a Data Analyst Support Specialist assigned to 'PRIORITY-REVIEW-001'. A high-priority analysis requires immediate access to all CSV files from the pending sorting job 'dir_op_001'. Your objective is to intercept these specific files. You must identify all CSV files in the operation's manifest on 'server-data-01.company.com'. Instead of letting them proceed to the standard sorting destination, your directive is to relocate all identified CSV files to a new priority review directory, '/data/priority_review/20240120/'. You are responsible for the full execution of this task, including performing database modifications to update the status of the moved files within the original 'dir_op_001' mandate and logging the successful staging operation."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/priority_review/20240120"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/priority_review/20240120/sales_data.csv"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/priority_review/20240120/customer_info.csv"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/priority_review/20240120/data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "PRIORITY-REVIEW-001", "task_type": "data_staging", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"policy_task_id": "dir_op_001"',
            '"files_identified_for_staging": 3',
            '"staging_directory_created": true',
            '"files_moved_to_staging": 3',
            '"original_task_files_updated": 3',
            '"staging_task_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_099",
        instruction=(
            "You are a Data Analyst Support Specialist assigned to 'PRIORITY-REVIEW-001'. A high-priority analysis requires immediate access to all CSV files from the pending sorting job 'dir_op_001'. Your objective is to intercept these specific files. You must identify all CSV files in the operation's manifest on 'server-data-01.company.com'. Instead of letting them proceed to the standard sorting destination, your directive is to relocate all identified CSV files to a new priority review directory, '/data/priority_review/20240120/'. You are responsible for the full execution of this task, including performing database modifications to update the status of the moved files within the original 'dir_op_001' mandate and logging the successful staging operation and send slack message to 'Operations' channel."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/priority_review/20240120"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/priority_review/20240120/sales_data.csv"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/priority_review/20240120/customer_info.csv"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/priority_review/20240120/data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "PRIORITY-REVIEW-001", "task_type": "data_staging", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"policy_task_id": "dir_op_001"',
            '"files_identified_for_staging": 3',
            '"staging_directory_created": true',
            '"files_moved_to_staging": 3',
            '"original_task_files_updated": 3',
            '"staging_task_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_079",
        instruction=(
            "You are a Data Archival Specialist assigned to 'EOY-REPORTS-ARCHIVAL-01'. As part of the end-of-year procedure, all recent financial reports must be moved to a permanent archive location. Before any file operations, you must conduct a full System Readiness Assessment. This includes performing the Pre-Execution File Transfer Security Clearance practices for the user associated with the audit task ('user_003') and verifying that the target server, 'server-analytics.company.com', is online and has sufficient disk space. Once all checks pass, your directive is to identify all reports that meet the criteria defined in 'fc_task_003' and relocate them to a new, permanent directory at '/analytics/final_reports/2023/'. You are responsible for the full execution of this task, which includes performing a database modification to update the status of the underlying audit task and logging the successful archival operation and also send a slack message to the 'Operations' channel"
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_003"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_003"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_003"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "carol_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-analytics.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-analytics.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-analytics.company.com", "directory": "/analytics/reports"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-analytics.company.com", "directory_path": "/analytics/final_reports/2023"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/final_reports/2023/daily_sales_report.csv"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/final_reports/2023/monthly_trends.csv"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_003", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "EOY-REPORTS-ARCHIVAL-01", "task_type": "data_archival", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"policy_task_id": "fc_task_003"',
            '"security_clearance_status": "passed"',
            '"server_status": "online"',
            '"disk_space_ok": true',
            '"files_identified_for_archival": 2',
            '"archive_directory_created": true',
            '"files_moved_to_archive": 2',
            '"original_task_status_updated": true',
            '"archival_task_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_074",
        instruction=(
            "You are an Incident Commander conducting a full post-mortem on the failed archive task 'arch_005'. We need to diagnose the technical root cause of the failure and also conduct a mandatory security review of the original operation due to the user's role. You must log your findings for both the technical failure and any discovered security violations using the original task ID. Conclude by sending a comprehensive incident report to 'System Alerts', notifying the responsible user ('user_004') and all system administrators ('user_001', 'user_005') with the message: 'Post-mortem for arch_005 COMPLETE. Technical failure: Insufficient storage. Security review: Critical policy violation found. User: @dave.intern. See logs for details. cc @alice.admin @eve.manager'"
        ),
        actions=[
            Action(name="get_error_log_details", kwargs={"task_id": "arch_005"}),
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_005"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_004"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_004"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "dave_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_005", "task_type": "post_mortem", "user_id": "user_004", "error_type": "insufficient_remote_storage", "severity": "medium",
                    "details_json": {"reason": "Insufficient storage space on remote server personal-backup.company.com."}
                }
            ),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_005", "task_type": "security_review", "user_id": "user_004", "error_type": "permission_denied", "severity": "critical",
                    "details_json": {"reason": "User 'user_004' (intern) attempted access to unauthorized server 'personal-backup.company.com'."}
                }
            ),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_004"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_001"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "Post-mortem for arch_005 COMPLETE. Technical failure: Insufficient storage. Security review: Critical policy violation found. User: @dave.intern. See logs for details. cc @alice.admin @eve.manager"
                }
            )
        ],
        outputs=[
            '"incident_task_id": "arch_005"',
            '"technical_root_cause": "Insufficient storage space"',
            '"security_review_status": "failed"',
            '"policy_violation_confirmed": true',
            '"technical_error_logged": true',
            '"security_error_logged": true',
            '"user_contact": "@dave.intern"',
            '"admin_1_contact": "@alice.admin"',
            '"admin_2_contact": "@eve.manager"',
            '"slack_report_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_021",
        instruction=(
            "You are a Data Analyst Specialist responsible for completing file audit 'fc_task_003'. "
            "The operation must follow Standard File Check practices and ensure that every part of the workflow "
            "is carried out with secure data handling. "
            "The audit scan findings are to be archived and transferred from 'server-analytics.company.com' "
            "to '/storage/file_check_results/' on 'storage-01.company.com', with the transfer validated for integrity. "
            "Following the transfer, appropriate cleanup is required, the delivery must be logged against the original task ID, "
            "and a final confirmation must be issued to the 'Operations' channel once the audit is fully completed."
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_003"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-analytics.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-analytics.company.com", "directory": "/analytics/reports"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_003", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_003", "task_type": "file_check", "user_id": "user_003"}),
            Action(name="send_slack_message", kwargs={"channel_name": "File Check"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "storage-01.company.com"}),
            Action(
                name="create_archive_on_remote",
                kwargs={
                    "hostname": "server-analytics.company.com", "archive_path": "/tmp/fc_task_003_results.tar.gz",
                    "files_to_include": ["/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]
                }
            ),
            Action(
                name="transfer_file_to_remote",
                kwargs={
                    "source_path": "/tmp/fc_task_003_results.tar.gz", "remote_address": "storage-01.company.com",
                    "destination_path": "/storage/file_check_results/fc_task_003_results.tar.gz", "ssh_key": "carol_rsa_key"
                }
            ),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "filepath": "/tmp/fc_task_003_results.tar.gz"}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_003", "task_type": "results_delivery", "user_id": "user_003"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"file_check_complete": true',
            '"file_check_logged": true',
            '"file_check_notification_sent": true',
            '"results_archive_created": true',
            '"transfer_complete_and_verified": true',
            '"source_cleanup_complete": true',
            '"delivery_logged": true',
            '"final_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_049",
        instruction=(
            "You are a Security Operations Analyst conducting a post-mortem security review, 'SEC-REV-005', on the failed archive task 'arch_005'. "
            "The task was initiated by 'user_004' to target 'personal-backup.company.com'. Your directive is to perform the full Pre-Execution Security Clearance practices on the original task parameters to determine if a security policy was violated before the storage error occurred. "
            "If you confirm a violation, you must log a new, separate 'critical' 'permission_denied' security violation error using the review ID. "
            "Following this, you must escalate by notifying system administrators ('user_001', 'user_005') via the 'System Alerts' channel with the explicit message: 'CRITICAL SECURITY VIOLATION (SEC-REV-005): User @dave.intern (role: intern) attempted unauthorized archive operation to personal-backup.company.com. Key 'dave_rsa_key' is not authorized. cc @alice.admin @eve.manager'"
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_005"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_004"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_004"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "dave_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="log_error_message", kwargs={"task_id": "SEC-REV-005", "task_type": "security_review", "user_id": "user_004", "error_type": "permission_denied", "severity": "critical", "details_json": {"reason": "User 'user_004' (intern) with key 'dave_rsa_key' attempted access to unauthorized server 'personal-backup.company.com'."}}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_004"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_001"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "CRITICAL SECURITY VIOLATION (SEC-REV-005): User @dave.intern (role: intern) attempted unauthorized archive operation to personal-backup.company.com. Key 'dave_rsa_key' is not authorized. cc @alice.admin @eve.manager"})
        ],
        outputs=[
            '"review_id": "SEC-REV-005"',
            '"original_task_id": "arch_005"',
            '"policy_violation_confirmed": true',
            '"violating_user": "user_004"',
            '"unauthorized_server": "personal-backup.company.com"',
            '"security_error_logged": true',
            '"admin_1_contact": "@alice.admin"',
            '"admin_2_contact": "@eve.manager"',
            '"escalation_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_047",
        instruction=(
            "You are a Data Integrity Specialist responsible for carrying out the secure lifecycle of the archive task 'arch_001'. "
            "Your duty is to ensure that all pre-flight security and readiness checks are satisfied on the target server 'backup-server.company.com' "
            "before any archival activity begins. "
            "Once validated, you must oversee execution of the Secure Archive Creation practices so that a complete archive is generated and transferred. "
            "The transfer process must include integrity verification to guarantee that the archive arrives intact. "
            "After successful confirmation, the source system 'server-prod-01.company.com' must be left clean and free of temporary artifacts, "
            "the task formally marked as completed, and the operation recorded for audit purposes. "
            "A clear completion notice must be issued to the 'Operations' channel summarizing that the archive was secured, validated, "
            "cleaned up, and finalized according to policy. "
            "The expected outcome is that all validations are passed, the archive is created and transferred with integrity confirmed, "
            "the source is cleared, the task is updated and logged, and the Operations team is notified."
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_001"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_001"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "alice_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "backup-server.company.com"}),
            Action(name="create_archive_on_remote", kwargs={"hostname": "server-prod-01.company.com", "archive_path": "/tmp/project_backup_2024.tar.gz", "files_to_include": ["/home/projects/webapp/src/main.js", "/home/projects/webapp/src/utils.js", "/home/projects/webapp/config/database.json", "/home/projects/webapp/docs/readme.md", "/home/projects/webapp/tests/unit_tests.py"]}),
            Action(name="transfer_file_to_remote", kwargs={"source_path": "/tmp/project_backup_2024.tar.gz", "remote_address": "backup-server.company.com", "destination_path": "/tmp/archives/project_backup_2024.tar.gz", "ssh_key": "alice_rsa_key"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/tmp/project_backup_2024.tar.gz"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_001", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "arch_001", "task_type": "archive", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"archive_id": "arch_001"',
            '"security_clearance": "passed"',
            '"disk_space_ok": true',
            '"archive_created": true',
            '"transfer_complete": true',
            '"checksum_verified": true',
            '"source_cleanup_complete": true',
            '"task_status_updated": "completed"',
            '"completion_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_035",
        instruction=(
            "You are an Automated Data Librarian assigned to carry out the file organization mandate 'dir_op_001'. "
            "Your responsibility is to ensure that this mandate is completed securely and in full. "
            "This involves confirming that the requesting user ('user_002') has valid security clearance for the target server 'server-data-01.company.com'. "
            "Once authorization is confirmed, the entire file organization practice must be executed: "
            "all files in the operation manifest are to be relocated into their correct destination subdirectories on the target server, "
            "with the necessary directory structures created where they do not already exist. "
            "Each file processed must have its operation status correctly updated to reflect successful completion. "
            "The operation should conclude with a success notification being delivered to the 'Operations' channel. "
            "The outcome must reflect that security was verified, all directories were prepared, all files were moved, "
            "statuses were updated, and the final notification was sent."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/csv"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/dat"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/json"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/miscellaneous"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/sorted/csv/sales_data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/sorted/csv/customer_info.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/data/sorted/dat/inventory.dat"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/data/sorted/json/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/readme.txt", "destination_path": "/data/sorted/miscellaneous/readme.txt"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/sorted/csv/data_0.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"operation_id": "dir_op_001"',
            '"security_clearance": "passed"',
            '"files_to_process": 6',
            '"directories_created": 4',
            '"files_moved": 6',
            '"all_statuses_updated": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_045",
        instruction=(
            "You are a Pre-flight Operations Coordinator. A critical, multi-server data synchronization operation for 'user_003' is pending. "
            "Your directive is to conduct a full 'System Readiness Assessment' across all participating servers: 'server-data-01.company.com' and 'server-analytics.company.com', following standard operational practice. "
            "For each server, the assessment must validate that the server is online, has at least 100GB of available disk space, and that the user's default SSH key is explicitly authorized for access. "
            "If all checks pass for all servers, you must log the successful assessment under the task ID 'readiness_check_user_003' and notify the 'Operations' channel with the message: 'System readiness assessment for user_003 sync operation passed. All target servers are online, have sufficient disk space, and user is authorized. Ready to proceed.'"
        ),
        actions=[
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_003"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_003"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "carol_rsa_key"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-analytics.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-analytics.company.com"}),
            Action(name="log_task_completion", kwargs={"task_id": "readiness_check_user_003", "task_type": "readiness_check", "user_id": "user_003"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "Operations",
                    "message": "System readiness assessment for user_003 sync operation passed. All target servers are online, have sufficient disk space, and user is authorized. Ready to proceed."
                }
            )
        ],
        outputs=[
            '"user_key_id": "carol_rsa_key"',
            '"server_1_status": "online"',
            '"server_1_disk_ok": true',
            '"server_1_auth_ok": true',
            '"server_2_status": "online"',
            '"server_2_disk_ok": true',
            '"server_2_auth_ok": true',
            '"overall_readiness": "passed"',
            '"assessment_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_084",
        instruction=(
            "You are a Security Analyst responding to 'INCIDENT-LOG-ISOLATION-01'. A potential security incident requires the immediate isolation and containment of recent application logs on 'server-prod-01.company.com'. Your directive is to follow the secure evidence collection practice under the authority of the Project Manager ('user_005'). This requires you to identify all target log files that match the criteria from 'fc_task_001'. You must then create a secure archive of these logs, transfer it to the central evidence locker at '/storage/incident_evidence/' on 'backup-server.company.com', and then purge the original source log files from the production server as a containment measure. You must see this task through to completion, including performing a database modification to update the status of the original file check task and logging the successful isolation of the evidence."
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_005"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_005"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "eve_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-prod-01.company.com", "directory": "/var/log/applications"}),
            Action(name="create_archive_on_remote", kwargs={"hostname": "server-prod-01.company.com", "archive_path": "/tmp/INCIDENT-LOG-ISOLATION-01.tar.gz", "files_to_include": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="transfer_file_to_remote", kwargs={"source_path": "/tmp/INCIDENT-LOG-ISOLATION-01.tar.gz", "remote_address": "backup-server.company.com", "destination_path": "/storage/incident_evidence/INCIDENT-LOG-ISOLATION-01.tar.gz", "ssh_key": "eve_rsa_key"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/var/log/applications/webapp.log"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/var/log/applications/api_requests.log"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/var/log/applications/error.log"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_001", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "INCIDENT-LOG-ISOLATION-01", "task_type": "forensics", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"})
        ],
        outputs=[
            '"policy_task_id": "fc_task_001"',
            '"security_clearance_status": "passed"',
            '"server_status": "online"',
            '"files_identified_for_isolation": 3',
            '"evidence_archive_created": true',
            '"evidence_transfer_successful": true',
            '"source_files_purged": 3',
            '"original_task_status_updated": true',
            '"forensics_task_logged": true',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_060",
        instruction=(
            "You are an Automated Data Librarian. Your mission is to execute the file organization mandate 'dir_op_001'. Before proceeding with any file operations, you must conduct a full System Readiness Assessment. This requires ensuring the requesting user ('user_002') is fully authorized for the target server ('server-data-01.company.com') according to all security policies, and that the server's resource health is within its 80% utilization threshold. Once all pre-flight checks are passed, you are to execute the file organization process in its entirety. Conclude all operations with a final success notification to the 'Operations' channel."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/csv"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/dat"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/json"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/miscellaneous"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/sorted/csv/sales_data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/sorted/csv/customer_info.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/data/sorted/dat/inventory.dat"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/data/sorted/json/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/readme.txt", "destination_path": "/data/sorted/miscellaneous/readme.txt"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/sorted/csv/data_0.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "dir_op_001", "task_type": "file_organization", "user_id": "user_002"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"operation_id": "dir_op_001"',
            '"security_clearance_status": "passed"',
            '"server_health_status": "passed"',
            '"files_to_process": 6',
            '"directories_created": 4',
            '"files_moved": 6',
            '"all_statuses_updated": true',
            '"completion_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_078",
        instruction=(
            "You are a Security Analyst responding to 'INCIDENT-LOG-ISOLATION-01'. A potential security incident requires the immediate isolation of recent application logs on 'server-prod-01.company.com'. Before any action, if needed perform the Pre-Execution File Transfer Security Clearance practices for the project manager ('user_005') who has authorized this action. Your directive is to then secure the logs for forensic analysis by identifying all target log files that match the criteria from 'fc_task_001'. Once identified, you are to relocate all these files to a new, secure directory at '/var/forensics/incident_20240120/'. You must see this task through to completion, which includes performing a database modification to update the status of the original file check task, and logging the successful isolation of the potentially compromised files."
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_005"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_005"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "eve_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-prod-01.company.com", "directory": "/var/log/applications"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-prod-01.company.com", "directory_path": "/var/forensics/incident_20240120"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "source_path": "/var/log/applications/webapp.log", "destination_path": "/var/forensics/incident_20240120/webapp.log"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "source_path": "/var/log/applications/api_requests.log", "destination_path": "/var/forensics/incident_20240120/api_requests.log"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "source_path": "/var/log/applications/error.log", "destination_path": "/var/forensics/incident_20240120/error.log"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_001", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "INCIDENT-LOG-ISOLATION-01", "task_type": "forensics", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"})
        ],
        outputs=[
            '"policy_task_id": "fc_task_001"',
            '"security_clearance_status": "passed"',
            '"server_status": "online"',
            '"files_identified_for_isolation": 3',
            '"forensics_directory_created": true',
            '"files_moved_to_isolation": 3',
            '"original_task_status_updated": true',
            '"forensics_task_logged": true',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_072",
        instruction=(
            "You are a Forensic Investigator assigned to 'RCA-STO-001' for a high disk usage alert on 'storage-01.company.com'. Your mission is to determine the cause. Your protocol requires you to confirm the server's live resource usage. Then, you must identify the most recently completed 'archive' task that targeted this server as the likely cause. If your investigation confirms this correlation, you must log a new 'high' severity 'disk_space_warning' error using the RCA task ID. The log must detail the server, its usage, and the contributing task ID. Finally, alert administrators ('user_001', 'user_005') in 'System Alerts' with your findings, using the message: 'RCA Complete (RCA-STO-001): High disk usage (82%) on storage-01.company.com correlated with task arch_002. @alice.admin @eve.manager please review.'"
        ),
        actions=[
            Action(name="get_server_resource_usage", kwargs={"hostname": "storage-01.company.com"}),
            Action(name="get_last_successful_task_run", kwargs={"task_type": "archive"}),
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_002"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "RCA-STO-001", "task_type": "forensics", "user_id": "system_agent", "error_type": "disk_space_warning", "severity": "high",
                    "details_json": {"server": "storage-01.company.com", "usage_percent": 82, "likely_cause_task": "arch_002"}
                }
            ),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_001"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "RCA Complete (RCA-STO-001): High disk usage (82%) on storage-01.company.com correlated with task arch_002. @alice.admin @eve.manager please review."
                }
            ),
            Action(name="log_task_completion", kwargs={"task_id": "RCA-STO-001", "task_type": "investigation", "user_id": "system_agent"})
        ],
        outputs=[
            '"disk_usage_confirmed_percent": 82',
            '"last_archive_task": "arch_002"',
            '"correlation_confirmed": true',
            '"incident_log_created": true',
            '"admin_1_contact": "@alice.admin"',
            '"admin_2_contact": "@eve.manager"',
            '"slack_escalation_sent": true',
            '"investigation_complete_and_logged": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_024",
        instruction=(
            "You are a Data Custodian responsible for data lifecycle management. "
            "The archival task 'arch_002' has reached the cleanup stage. "
            "You can use the Archive Finalization Practices to retrieve the task record for 'arch_002' in order to identify the original source filepaths. "
            "All of these original files must be securely purged from 'server-analytics.company.com'. "
            "Once the cleanup is complete, the archive record must be updated in the system so that its status is 'verified', confirming that the entire lifecycle has been completed. "
            "This finalization must also be logged for auditability. "
            "To close the process, you must notify the Operations team by sending a confirmation to the 'Operations' channel."
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_002"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "filepath": "/analytics/raw_data/user_events_2023.csv"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "filepath": "/analytics/raw_data/page_views_2023.csv"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "filepath": "/analytics/processed/monthly_reports_2023.json"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "filepath": "/analytics/processed/yearly_summary_2023.pdf"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_002", "status": "verified"}),
            Action(name="log_task_completion", kwargs={"task_id": "arch_002", "task_type": "archive_cleanup", "user_id": "user_003"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"archive_id": "arch_002"',
            '"source_files_deleted": 4',
            '"task_status_updated": "verified"',
            '"operation_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_030",
        instruction=(
            "You are a Proactive System Maintainer. The '/data/temp' directory on 'server-data-01.company.com' requires routine cleanup to manage disk space. The Stale File Cleanup practices can be used for maintenance task 'fc_task_002'. This involves identifying and purging all files that violate the task's defined data retention and size policies. After the cleanup is complete, you must formally mark the task as completed, log the operational success for auditing, and report the results to the 'Operations' channel."
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_002", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_002", "task_type": "file_check", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"cleanup_task_id": "fc_task_002"',
            '"filters_applied": ["older_than_30_days", "max_size_100MB"]',
            '"files_identified_for_deletion": 1',
            '"file_deleted": "/data/temp/temp_export_001.csv"',
            '"cleanup_completed": true',
            '"task_status_updated": true',
            '"operation_logged": true'
        ]
    ),
     Task(
        annotator="0",
        user_id="USER_022",
        instruction=(
            "You are a Proactive System Maintainer responsible for executing the 'System Health Audit' identified as 'HEALTH-AUDIT-01'. "
            "This audit covers the primary data servers: 'server-data-01.company.com' and 'server-prod-01.company.com'. "
            "Your responsibility is to verify that each server’s disk usage remains below the operational threshold of 75%. "
            "Any breach of this threshold must be treated as a critical issue: it requires immediate escalation to the 'System Alerts' channel "
            "and remediation by applying the Stale File Cleanup practices defined in maintenance task 'fc_task_002'. "
            "Once the audit and any corrective actions are complete, you must ensure the entire process is properly logged under 'HEALTH-AUDIT-01' "
            "and provide the 'Operations' channel with a clear, comprehensive summary of the audit outcome, including any breaches detected and actions taken. "
            "The expected outcome is that all servers are audited, any issues are escalated and remediated in line with policy, "
            "the audit is logged, and the final report is communicated."
        ),
        actions=[
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "HEALTH-AUDIT-01: Disk usage on server-data-01.company.com (78%) exceeds 75% threshold. Initiating cleanup."
                }
            ),
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/cache_backup.dat"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_002", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "HEALTH-AUDIT-01", "task_type": "system_health_audit", "user_id": "system_agent"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "Operations",
                    "message": "System Health Audit HEALTH-AUDIT-01 complete. server-data-01.company.com exceeded disk threshold and was remediated by purging 2 stale files. server-prod-01.company.com is healthy."
                }
            )
        ],
        outputs=[
            '"servers_checked": 2',
            '"threshold_breached_on": "server-data-01.company.com"',
            '"slack_alert_sent": true',
            '"cleanup_protocol_initiated": true',
            '"files_purged_count": 2',
            '"cleanup_task_status_updated": true',
            '"audit_operation_logged": true',
            '"slack_summary_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_012",
        instruction=(
            "You are an Incident Responder assigned to case 'INC-PERM-007'. "
            "A security audit has confirmed that user 'user_003' gained unauthorized access to 'server-data-01.company.com' using the credential 'carol_rsa_key'. "
            "Your directive is to respond to this incident. The response requires that the violation be formally logged. As a forensic measure, you must collect evidence from the compromised server’s primary data directories: `/data/temp` and `/data/unsorted`. "
            "All collected evidence must be preserved in an archive and securely transferred under administrative account 'user_001' to '/storage/incident_evidence/' on 'backup-server.company.com'. "
            "To complete the incident response, you must notify the Operations team by sending the following structured message to the 'Operations' channel: "
            "'Incident INC-PERM-007 remediated. Unauthorized access by user_003 on server-data-01.company.com has been logged. A full forensic archive of data directories has been created and stored for review.'"
        ),
        actions=[
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_003"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "carol_rsa_key"}),
            Action(name="log_error_message", kwargs={"task_id": "INC-PERM-007", "task_type": "incident_response", "user_id": "user_003", "error_type": "permission_denied", "severity": "critical", "details_json": {"user": "user_003", "server": "server-data-01.company.com", "reason": "Unauthorized key found during audit."}}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/unsorted"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_001"}),
            Action(name="create_archive_on_remote", kwargs={"hostname": "server-data-01.company.com", "archive_path": "/tmp/INC-PERM-007_evidence.tar.gz", "files_to_include": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat", "/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="transfer_file_to_remote", kwargs={"source_path": "/tmp/INC-PERM-007_evidence.tar.gz", "remote_address": "backup-server.company.com", "destination_path": "/storage/incident_evidence/INC-PERM-007_evidence.tar.gz", "ssh_key": "alice_rsa_key"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/tmp/INC-PERM-007_evidence.tar.gz"}),
            Action(name="log_task_completion", kwargs={"task_id": "INC-PERM-007", "task_type": "incident_response", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations", "message": "Incident INC-PERM-007 remediated. Unauthorized access by user_003 on server-data-01.company.com has been logged. A full forensic archive of data directories has been created and stored for review."})
        ],
        outputs=[
            '"incident_id": "INC-PERM-007"',
            '"violation_logged": true',
            '"directories_scanned": 2',
            '"files_inventoried": 4',
            '"admin_ssh_key_retrieved": "alice_rsa_key"',
            '"forensic_archive_created": true',
            '"evidence_transfer_complete": true',
            '"source_cleanup_complete": true',
            '"incident_response_logged": true',
            '"slack_summary_sent": true'
        ]
    ),
    Task(
            annotator="0",
            user_id="USER_016",
            instruction=(
                "You are a Data Security Officer assigned to conduct a pre-flight security audit for archive task 'arch_003'. Your directive is to enforce all security protocols by following the 'Pre-Execution File Transfer Security Clearance Protocol' for the requesting user ('user_002') against the target server 'log-storage.company.com'. If a security policy violation is discovered, you must follow the standard practice for halting an operation due to a critical security failure, which includes updating all relevant database records and escalating the incident. Your escalation to 'System Alerts' must contain the message: 'Task arch_003 HALTED on security violation. User @bob.dev is not authorized for log-storage.company.com.'"
            ),
            actions=[
                Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_003"}),
                Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
                Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_002"}),
                Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
                Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
                Action(name="update_archive_task_status", kwargs={"archive_id": "arch_003", "status": "failed"}),
                Action(name="log_error_message", kwargs={"task_id": "arch_003", "task_type": "security_audit", "user_id": "user_002", "error_type": "permission_denied", "severity": "critical", "details_json": {"reason": "Key 'bob_rsa_key' is not authorized for server 'log-storage.company.com' as per its authorized_servers list."}}),
                Action(name="get_user_contact_info", kwargs={"user_id": "user_002"}),
                Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "Task arch_003 HALTED on security violation. User @bob.dev is not authorized for log-storage.company.com."})
            ],
            outputs=[
                '"task_id": "arch_003"',
                '"user_role": "developer"',
                '"ssh_key_id": "bob_rsa_key"',
                '"authorization_check": "failed"',
                '"policy_violation_confirmed": true',
                '"task_status_updated": "failed"',
                '"security_error_logged": true',
                '"user_contact": "@bob.dev"',
                '"slack_alert_sent": true'
            ]
    ),
   Task(
        annotator="0",
        user_id="USER_019",
        instruction=(
            "You are a Senior Systems Administrator. Your directive is to ensure that the source server ('server-prod-01.company.com') is in a healthy state before proceeding with the pending archive task 'arch_001' for user 'user_001'. "
            "A health check is required and must confirm that CPU, memory, and disk utilization are each below the 75% threshold. "
            "If the server meets these conditions, the Secure Archive Creation protocol must be carried out to completion. "
            "Once the archive has been created and transferred successfully, the task must be finalized in accordance with policy, including updating its status, logging completion, and sending a notification to the 'Operations' channel."
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_001"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_001"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "backup-server.company.com"}),
            Action(name="create_archive_on_remote", kwargs={"hostname": "server-prod-01.company.com", "archive_path": "/tmp/project_backup_2024.tar.gz", "files_to_include": ["/home/projects/webapp/src/main.js", "/home/projects/webapp/src/utils.js", "/home/projects/webapp/config/database.json", "/home/projects/webapp/docs/readme.md", "/home/projects/webapp/tests/unit_tests.py"]}),
            Action(name="transfer_file_to_remote", kwargs={"source_path": "/tmp/project_backup_2024.tar.gz", "remote_address": "backup-server.company.com", "destination_path": "/tmp/archives/project_backup_2024.tar.gz", "ssh_key": "alice_rsa_key"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_001", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "arch_001", "task_type": "archive", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"source_server_health_status": "healthy"',
            '"destination_disk_space_ok": true',
            '"archive_created": true',
            '"transfer_successful": true',
            '"task_status_updated": true',
            '"completion_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_020",
        instruction=(
            "You are an Incident Responder assigned to 'INC-ARCH-003'. The archive task 'arch_003' has been flagged due to a pre-execution failure. Your directive is to conduct a full 'Task Failure Diagnosis Protocol' to determine the root cause. If the failure is confirmed to be a security policy violation, you must perform a database write to log a new 'critical' 'permission_denied' error for this incident, update the original archive task's status to 'failed', and then escalate the finding. Your escalation must be sent to the 'System Alerts' channel, notifying the original user and all system administrators ('user_001', 'user_005') with the message: 'Incident INC-ARCH-003: Task arch_003 failed due to security policy violation. User @bob.dev (developer) is not authorized for log-storage.company.com. Task aborted. cc @alice.admin @eve.manager'"
        ),
        actions=[
            Action(name="get_error_log_details", kwargs={"task_id": "arch_003"}),
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_003"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "INC-ARCH-003", "task_type": "incident_response", "user_id": "user_002", "error_type": "permission_denied", "severity": "critical",
                    "details_json": {"reason": "User 'user_002' with role 'developer' has no authorization for 'log-storage.company.com' per policy.", "original_task": "arch_003"}
                }
            ),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_003", "status": "failed"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_002"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_001"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "Incident INC-ARCH-003: Task arch_003 failed due to security policy violation. User @bob.dev (developer) is not authorized for log-storage.company.com. Task aborted. cc @alice.admin @eve.manager"
                }
            ),
            Action(name="log_task_completion", kwargs={"task_id": "INC-ARCH-003", "task_type": "incident_response", "user_id": "system_agent"})
        ],
        outputs=[
            '"incident_id": "INC-ARCH-003"',
            '"root_cause_confirmed": "permission_denied"',
            '"policy_violation_found": true',
            '"error_log_created": true',
            '"original_task_status_updated": "failed"',
            '"user_notified": "@bob.dev"',
            '"admins_notified": true',
            '"incident_response_logged": true',
            '"slack_alert_sent": true'
        ]
    ),
   Task(
        annotator="0",
        user_id="USER_087",
        instruction=(
            "You are a Forensic Investigator assigned to 'RCA-STO-001', tasked with conducting root cause analysis for a high disk usage alert (82%) on 'storage-01.company.com'. "
            "The investigation must establish the current usage level on the server and determine whether a recently completed archive task contributed to the condition. "
            "Confirmation requires validating the most recent successful archive targeting this server, including retrieval of its instructions to assess its contribution. "
            "If correlation is found, the findings must be recorded in the system by creating a 'disk_space_warning' entry under the RCA task ID, with high severity. "
            "The error record must include the affected server, its usage, the contributing task identifier, and the archive size. "
            "The outcome of the RCA must be communicated to administrators ('user_001' and 'user_005') through the 'System Alerts' channel with an explicit message reporting the correlation and tagging @alice.admin and @eve.manager for review."
        ),
        actions=[
            Action(name="check_remote_disk_space", kwargs={"hostname": "storage-01.company.com"}),
            Action(name="get_last_successful_task_run", kwargs={"task_type": "archive"}),
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_002"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "RCA-STO-001",
                    "task_type": "forensics",
                    "user_id": "system_agent",
                    "error_type": "disk_space_warning",
                    "severity": "high",
                    "details_json": {
                        "server": "storage-01.company.com", "usage_percent": 82, "likely_cause_task": "arch_002", "archive_size_display": "487.0MB"
                    }
                }
            ),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_001"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_005"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "RCA Complete (RCA-STO-001): High disk usage (82%) on storage-01.company.com correlated with task arch_002 (487.0MB). @alice.admin @eve.manager please review."
                }
            ),
            Action(name="log_task_completion", kwargs={"task_id": "RCA-STO-001", "task_type": "investigation", "user_id": "system_agent"})
        ],
        outputs=[
            '"disk_usage_confirmed_percent": 82',
            '"contributing_task_id": "arch_002"',
            '"correlation_confirmed": true',
            '"incident_log_created": true',
            '"admin_1_contact": "@alice.admin"',
            '"admin_2_contact": "@eve.manager"',
            '"slack_escalation_sent": true',
            '"investigation_complete_and_logged": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_089",
        instruction=(
            "You are a Security Operations Analyst conducting a post-mortem security review, 'SEC-REV-005', on the failed archive task 'arch_005'. The task was initiated by 'user_004' to target 'personal-backup.company.com'. Your directive is to perform the full 'Pre-Execution Security Clearance Protocol' on the original task parameters to determine if a security policy was violated before the storage error occurred. If you confirm a violation, you must log a new, separate 'critical' 'permission_denied' security violation error using the review ID. Following this, you must escalate by notifying system administrators ('user_001', 'user_005') via the 'System Alerts' channel with the explicit message: 'CRITICAL SECURITY VIOLATION (SEC-REV-005): User @dave.intern (role: intern) attempted unauthorized archive operation to personal-backup.company.com. Key 'dave_rsa_key' is not authorized. cc @alice.admin @eve.manager'"
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_005"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_004"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_004"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "dave_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="log_error_message", kwargs={"task_id": "SEC-REV-005", "task_type": "security_review", "user_id": "user_004", "error_type": "permission_denied", "severity": "critical", "details_json": {"reason": "User 'user_004' (intern) with key 'dave_rsa_key' attempted access to unauthorized server 'personal-backup.company.com'."}}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_004"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_001"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "CRITICAL SECURITY VIOLATION (SEC-REV-005): User @dave.intern (role: intern) attempted unauthorized archive operation to personal-backup.company.com. Key 'dave_rsa_key' is not authorized. cc @alice.admin @eve.manager"})
        ],
        outputs=[
            '"review_id": "SEC-REV-005"',
            '"original_task_id": "arch_005"',
            '"policy_violation_confirmed": true',
            '"violating_user": "user_004"',
            '"unauthorized_server": "personal-backup.company.com"',
            '"security_error_logged": true',
            '"admin_1_contact": "@alice.admin"',
            '"admin_2_contact": "@eve.manager"',
            '"escalation_sent": true'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_007",
        instruction=(
            "You are a Security Analyst assigned to 'SEC-REVIEW-CONFIG-01'. Your objective is to isolate potentially sensitive configuration files from the pending file organization task 'dir_op_001' for a security review. You must identify all '.dat' and '.json' files within the operation's manifest on 'server-data-01.company.com'. Instead of allowing them to be sorted, your directive is to quarantine these specific files by relocating them to a new secure directory, '/secure/quarantine/config_review_20240120/'. You are responsible for the full execution of this task, including performing database modifications to update the status of the moved files and logging the successful quarantine operation."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/secure/quarantine/config_review_20240120"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/secure/quarantine/config_review_20240120/inventory.dat"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/secure/quarantine/config_review_20240120/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "SEC-REVIEW-CONFIG-01", "task_type": "security_quarantine", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"})
        ],
        outputs=[
            '"policy_task_id": "dir_op_001"',
            '"files_identified_for_quarantine": 2',
            '"quarantine_directory_created": true',
            '"files_moved_to_quarantine": 2',
            '"original_task_files_updated": 2',
            '"quarantine_task_logged": true',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_063",
        instruction=(
            "You are a Security Automation Engineer. Your directive is to perform a full Pre-Execution Security Clearance for the pending archive task 'arch_004'. "
            "This clearance requires validating that the requesting user's role ('project_manager') is permitted access under the 'SSH Access Policy', and that the user's default SSH key is explicitly authorized for the destination server 'document-vault.company.com'. "
            "If either of these validations fails, the operation must not proceed. In such cases, the archive task should be marked as 'failed', a 'critical' 'permission_denied' error must be logged with details of the violation, and a notification should be sent to the 'System Alerts' channel."
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_004"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_005"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_005"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "eve_rsa_key"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_004", "status": "failed"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_004",
                    "task_type": "archive",
                    "user_id": "user_005",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "SSH key 'eve_rsa_key' is not authorized for destination server 'document-vault.company.com'."
                    }
                }
            ),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"})
        ],
        outputs=[
            '"task_id": "arch_004"',
            '"user_role_check": "passed"',
            '"ssh_key_check": "failed"',
            '"violating_key": "eve_rsa_key"',
            '"unauthorized_server": "document-vault.company.com"',
            '"task_status_updated": "failed"',
            '"security_error_logged": true',
            '"user_contact": "@eve.manager"',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_036",
        instruction=(
            "You are a System Hygiene Specialist. Your objective is to resolve maintenance task 'fc_task_002'. Before execution, you must perform a full pre-flight readiness check. This includes conducting the Pre-Execution Security Clearance practices for the designated user ('user_001') and verifying the target server's operational status. If all checks pass, Stale File Cleanup Practices might be needed here, ensuring you only purge files that strictly match all policy filters defined within the task. Conclude by notifying the 'File Check' channel with the message: 'Maintenance task fc_task_002 completed successfully. 1 stale file purged from /data/temp on server-data-01.company.com.'"
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_001"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_001"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "alice_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_002", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_002", "task_type": "file_check", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "File Check", "message": "Maintenance task fc_task_002 completed successfully. 1 stale file purged from /data/temp on server-data-01.company.com."})
        ],
        outputs=[
            '"task_id": "fc_task_002"',
            '"security_clearance_status": "passed"',
            '"server_status": "online"',
            '"files_scanned": 2',
            '"files_matching_criteria": 1',
            '"files_deleted_count": 1',
            '"task_status_updated": true',
            '"completion_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_057",
        instruction=(
            "You are a Security Analyst assigned to 'SEC-REVIEW-CONFIG-01'. Your objective is to isolate potentially sensitive configuration files from the pending file organization task 'dir_op_001' for a security review. You must identify all '.dat' and '.json' files within the operation's manifest on 'server-data-01.company.com'. Instead of allowing them to be sorted, your directive is to quarantine these specific files by relocating them to a new secure directory, '/secure/quarantine/config_review_20240120/'. You are responsible for the full execution of this task, including performing database modifications to update the status of the moved files and logging the successful quarantine operation."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/secure/quarantine/config_review_20240120"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/secure/quarantine/config_review_20240120/inventory.dat"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/secure/quarantine/config_review_20240120/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "SEC-REVIEW-CONFIG-01", "task_type": "security_quarantine", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"})
        ],
        outputs=[
            '"policy_task_id": "dir_op_001"',
            '"files_identified_for_quarantine": 2',
            '"quarantine_directory_created": true',
            '"files_moved_to_quarantine": 2',
            '"original_task_files_updated": 2',
            '"quarantine_task_logged": true',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_070",
        instruction=(
            "You are a Data Analyst Specialist. Your mission is to execute file audit 'fc_task_003' and securely deliver the findings. This requires you to first follow the 'Standard File Check Protocol'. Once the scan is complete, you must then follow the appropriate practice to archive the files found by the scan and securely transfer the resulting archive to '/storage/file_check_results/' on 'storage-01.company.com'. You must ensure the integrity of the transfer is confirmed, perform cleanup of the temporary archive on the source server, log the delivery using the original task ID, and send a final confirmation to 'Operations'."
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_003"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-analytics.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-analytics.company.com", "directory": "/analytics/reports"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_003", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_003", "task_type": "file_check", "user_id": "user_003"}),
            Action(name="send_slack_message", kwargs={"channel_name": "File Check"}),
            Action(
                name="create_archive_on_remote",
                kwargs={
                    "hostname": "server-analytics.company.com", "archive_path": "/tmp/fc_task_003_results.tar.gz",
                    "files_to_include": ["/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]
                }
            ),
            Action(
                name="transfer_file_to_remote",
                kwargs={
                    "source_path": "/tmp/fc_task_003_results.tar.gz", "remote_address": "storage-01.company.com",
                    "destination_path": "/storage/file_check_results/fc_task_003_results.tar.gz", "ssh_key": "carol_rsa_key"
                }
            ),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "filepath": "/tmp/fc_task_003_results.tar.gz"}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_003", "task_type": "results_delivery", "user_id": "user_003"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"file_check_complete": true',
            '"file_check_logged": true',
            '"file_check_notification_sent": true',
            '"results_archive_created": true',
            '"transfer_complete_and_verified": true',
            '"source_cleanup_complete": true',
            '"delivery_logged": true',
            '"final_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_038",
        instruction=(
            "You are a Security Automation Engineer tasked with conducting the 'Pre-Execution Security Clearance' for archive task 'arch_004'. "
            "This clearance must validate both role-based and key-based authorization under the SSH Access Policy. "
            "The requesting user's role ('project_manager') must be verified against the policy to ensure it permits server access, and the user's default SSH key must be confirmed as authorized for the destination server ('document-vault.company.com'). "
            "If any violation is detected, the system must record the violation as a critical permission error, reflect the failure in the task status, and escalate to the 'System Alerts' channel with the message: 'Task arch_004 HALTED on security violation. User @eve.manager's key 'eve_rsa_key' is not authorized for destination server 'document-vault.company.com'. Operation aborted.'"
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_004"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_005"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_005"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "eve_rsa_key"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_004", "status": "failed"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_004",
                    "task_type": "archive",
                    "user_id": "user_005",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "SSH key 'eve_rsa_key' is not authorized for destination server 'document-vault.company.com'."
                    }
                }
            ),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "Task arch_004 HALTED on security violation. User @eve.manager's key 'eve_rsa_key' is not authorized for destination server 'document-vault.company.com'. Operation aborted."})
        ],
        outputs=[
            '"task_id": "arch_004"',
            '"user_role_check": "passed"',
            '"ssh_key_check": "failed"',
            '"violating_key": "eve_rsa_key"',
            '"unauthorized_server": "document-vault.company.com"',
            '"task_status_updated": "failed"',
            '"security_error_logged": true',
            '"user_contact": "@eve.manager"',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_039",
        instruction=(
            "You are a Senior Incident Manager responsible for overseeing remediation of the failed archive task 'arch_005'. "
            "Your mandate is to carry out the Task Failure Diagnosis practices, ensuring the root cause is identified and recorded. "
            "As part of remediation planning, available storage capacity on alternative servers 'backup-server.company.com' and 'storage-01.company.com' must be assessed to determine a viable destination. "
            "The chosen alternative and supporting diagnostic details are to be logged as part of remediation analysis. "
            "A structured remediation plan must then be communicated to the 'Operations' channel with message 'Remediation Plan for arch_005: Retry task using 'backup-server.company.com' as the destination (4250GB available). cc @dave.intern', and the incident must be finalized with proper completion logging."
        ),
        actions=[
            Action(name="get_error_log_details", kwargs={"task_id": "arch_005"}),
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_005"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_004"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_004"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "backup-server.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "storage-01.company.com"}),
            Action(
                name="log_error_message",
                kwargs={
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
                }
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "Operations",
                    "message": "Remediation Plan for arch_005: Retry task using 'backup-server.company.com' as the destination (4250GB available). cc @dave.intern"
                }
            ),
            Action(name="log_task_completion", kwargs={"task_id": "arch_005", "task_type": "incident_response", "user_id": "system_agent"})
        ],
        outputs=[
            '"failed_task_id": "arch_005"',
            '"root_cause_identified": "Insufficient storage space on remote server"',
            '"user_contact": "@dave.intern"',
            '"alternative_server_1_space": 4250',
            '"alternative_server_2_space": 1800',
            '"remediation_log_created": true',
            '"remediation_plan_sent": true',
            '"incident_fully_processed": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_009",
        instruction=(
            "You are a Data Analyst Support Specialist assigned to 'PRIORITY-REVIEW-001'. A high-priority analysis requires immediate access to all CSV files from the pending sorting job 'dir_op_001'. Your objective is to intercept these specific files. You must identify all CSV files in the operation's manifest on 'server-data-01.company.com'. Instead of letting them proceed to the standard sorting destination, your directive is to relocate all identified CSV files to a new priority review directory, '/data/priority_review/20240120/'. You are responsible for the full execution of this task, including performing database modifications to update the status of the moved files within the original 'dir_op_001' mandate and logging the successful staging operation."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/priority_review/20240120"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/priority_review/20240120/sales_data.csv"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/priority_review/20240120/customer_info.csv"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/priority_review/20240120/data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "PRIORITY-REVIEW-001", "task_type": "data_staging", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"policy_task_id": "dir_op_001"',
            '"files_identified_for_staging": 3',
            '"staging_directory_created": true',
            '"files_moved_to_staging": 3',
            '"original_task_files_updated": 3',
            '"staging_task_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_064",
        instruction=(
            "You are an Incident Commander conducting a full post-mortem on the failed archive task 'arch_005'. Your mission is a dual investigation following all appropriate protocols. First, diagnose the technical root cause of the failure. Second, conduct a mandatory security review of the original operation due to the user's role. You must log your findings for both the technical failure and any discovered security violations. Conclude by sending a comprehensive incident report to 'System Alerts', notifying the responsible user ('user_004') and all system administrators ('user_001', 'user_005') with the message: 'Post-mortem for arch_005 COMPLETE. Technical failure: Insufficient storage. Security review: Critical policy violation found. User: @dave.intern. See logs for details. cc @alice.admin @eve.manager'"
        ),
        actions=[
            Action(name="get_error_log_details", kwargs={"task_id": "arch_005"}),
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_005"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_004"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_004"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "dave_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_005", "task_type": "post_mortem", "user_id": "user_004", "error_type": "insufficient_remote_storage", "severity": "medium",
                    "details_json": {"reason": "Insufficient storage space on remote server personal-backup.company.com."}
                }
            ),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_005", "task_type": "security_review", "user_id": "user_004", "error_type": "permission_denied", "severity": "critical",
                    "details_json": {"reason": "User 'user_004' (intern) attempted access to unauthorized server 'personal-backup.company.com'."}
                }
            ),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_004"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_001"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "Post-mortem for arch_005 COMPLETE. Technical failure: Insufficient storage. Security review: Critical policy violation found. User: @dave.intern. See logs for details. cc @alice.admin @eve.manager"
                }
            )
        ],
        outputs=[
            '"incident_task_id": "arch_005"',
            '"technical_root_cause": "Insufficient storage space"',
            '"security_review_status": "failed"',
            '"policy_violation_confirmed": true',
            '"technical_error_logged": true',
            '"security_error_logged": true',
            '"user_contact": "@dave.intern"',
            '"admin_1_contact": "@alice.admin"',
            '"admin_2_contact": "@eve.manager"',
            '"slack_report_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_062",
        instruction=(
            "You are a Data Governance Officer assigned to 'GOVERNANCE-REVIEW-Q1'. A quarterly review process has been initiated, and you must secure all relevant recent reports. Your directive is to identify all reports on 'server-analytics.company.com' that match the criteria defined in the standard file audit task 'fc_task_003'. To prevent modification during the review, you must relocate all identified files to a new, secure directory at '/analytics/reports/review_pending_q1/'. You are responsible for seeing this task to its conclusion, which includes performing a database modification to update the status of the audit task to reflect its completion for this quarter, and logging the successful governance action, and also send slack message to Operations"
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_003"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-analytics.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-analytics.company.com", "directory": "/analytics/reports"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-analytics.company.com", "directory_path": "/analytics/reports/review_pending_q1"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/reports/review_pending_q1/daily_sales_report.csv"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/reports/review_pending_q1/monthly_trends.csv"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_003", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "GOVERNANCE-REVIEW-Q1", "task_type": "data_governance", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"policy_task_id": "fc_task_003"',
            '"files_identified_for_review": 2',
            '"review_directory_created": true',
            '"files_moved_to_review": 2',
            '"original_task_status_updated": true',
            '"governance_task_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_065",
        instruction=(
            "You are an Automated Data Librarian. Your directive is to execute the file organization mandate 'dir_op_001'. Before proceeding, you must conduct a full System Readiness Assessment. This includes performing the Pre-Execution Security Clearance practice for the user ('user_002') on the target server, 'server-data-01.company.com', and a Proactive Server Health Check practice using an 80% utilization threshold. The server's current disk usage is high, so you must log a 'low_storage_warning' before proceeding. If all pre-flight checks pass despite the warning, you are to execute the File Organization practice in its entirety. Conclude all operations with a final success notification to the 'Operations' channel."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "dir_op_001", "task_type": "pre_execution_check", "user_id": "user_002", "error_type": "low_storage_warning", "severity": "warning",
                    "details_json": {"disk_percent": 78, "threshold_percent": 80}
                }
            ),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/csv"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/dat"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/json"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/miscellaneous"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/sorted/csv/sales_data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/sorted/csv/customer_info.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/data/sorted/dat/inventory.dat"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/data/sorted/json/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/readme.txt", "destination_path": "/data/sorted/miscellaneous/readme.txt"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/sorted/csv/data_0.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"operation_id": "dir_op_001"',
            '"security_clearance_status": "passed"',
            '"server_health_status": "passed"',
            '"low_storage_warning_logged": true',
            '"files_to_process": 6',
            '"directories_created": 4',
            '"files_moved": 6',
            '"all_statuses_updated": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_067",
        instruction=(
            "You are an Incident Responder assigned to incident 'INC-DIROP-RETRY-01', concerning the deferred file organization task 'dir_op_001'. "
            "Your responsibility is to reassess the operational environment by determining whether the current resource usage on 'server-data-01.company.com' is within acceptable limits, defined as below 60% CPU utilization. "
            "If the server remains above this threshold, the operation must not proceed. In such cases, the deferral protocol requires the system to record the cause of non-execution, update all files in the task to a failed state to prevent re-queueing, and provide visibility to stakeholders through the 'Operations' channel. "
            "The notification should explicitly state that 'dir_op_001' remains deferred due to persistent high resource usage on the server, including the actual CPU and memory percentages, and tag @bob.dev for awareness."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "dir_op_001", "task_type": "pre_execution_check", "user_id": "user_002", "error_type": "high_resource_usage", "severity": "warning",
                    "details_json": {"cpu_percent": 62, "memory_percent": 72, "threshold_percent": 60, "action_taken": "deferred"}
                }
            ),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "failed"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_002"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "Operations",
                    "message": "Task dir_op_001 remains deferred due to persistent high resource usage on server-data-01.company.com (CPU: 62%, MEM: 72%). cc @bob.dev"
                }
            )
        ],
        outputs=[
            '"task_id": "dir_op_001"',
            '"server_cpu_usage": 62',
            '"health_check_status": "failed"',
            '"warning_log_created": true',
            '"files_in_operation": 6',
            '"file_statuses_updated_to_failed": 6',
            '"user_notified": "@bob.dev"',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_001",
        instruction=(
            "You are a Senior Systems Administrator responsible for carrying out the archive operation 'arch_003'. "
            "This task must be executed with strict adherence to security and operational policies. "
            "The requesting user ('user_002') must be verified for authorization to access the destination server ('log-storage.company.com') "
            "under the SSH Access Policy before any file operations can proceed. "
            "If authorization is not confirmed, the archive operation must not continue, and the system must reflect a failed state with the reason clearly recorded. "
            "Any policy violations should be captured as critical permission errors in the task logs, with full details for audit. "
            "The task status should be updated accordingly, and relevant parties must be notified, including a system-wide alert to the 'System Alerts' channel stating: "
            "'Archive task arch_003 failed pre-execution security clearance. User @bob.dev is not authorized for the destination server. See error logs for details.'"
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_003"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_003",
                    "task_type": "archive",
                    "user_id": "user_002",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User role 'developer' is not authorized for 'log-storage.company.com' per SSH Access Policy."
                    }
                }
            ),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_003", "status": "failed"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_002"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "Archive task arch_003 failed pre-execution security clearance. User @bob.dev is not authorized for the destination server. See error logs for details."
                }
            )
        ],
        outputs=[
            '"task_id": "arch_003"',
            '"user_role": "developer"',
            '"ssh_key_id": "bob_rsa_key"',
            '"security_clearance_status": "failed"',
            '"policy_violation_detected": true',
            '"error_log_created": true',
            '"task_status_updated_to": "failed"',
            '"user_notified": "@bob.dev"',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_002",
        instruction=(
            "You are a Senior Incident Manager responsible for handling a high-priority failure of archive task 'arch_005'. "
            "Your mission is to apply practices related to Task Failure Diagnosis to investigate the incident and confirm whether the root cause is storage-related. "
            "If insufficient storage is confirmed on the primary server ('personal-backup.company.com'), you must determine a viable remediation path by evaluating available capacity on designated alternative servers, including 'backup-server.company.com' and 'storage-01.company.com'. "
            "The outcome of this analysis must be recorded in the system with a remediation analysis entry that documents the confirmed root cause, severity level, and the best available alternative server with its capacity. "
            "The remediation plan must also be communicated to stakeholders through the 'Operations' channel, with an explicit message describing the recommended retry destination, the available space, the identified root cause, and tagging the responsible user (@dave.intern) for visibility."
        ),
        actions=[
            Action(name="get_error_log_details", kwargs={"task_id": "arch_005"}),
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_005"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "backup-server.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "storage-01.company.com"}),
            Action(
                name="log_error_message",
                kwargs={
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
                }
            ),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_004"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_004"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "Operations",
                    "message": "Remediation Plan for arch_005: Retry task using backup-server.company.com as the destination (4250GB available). Root cause: insufficient space on personal-backup.company.com. cc @dave.intern"
                }
            ),
            Action(name="log_task_completion", kwargs={"task_id": "arch_005", "task_type": "incident_response", "user_id": "system_agent"})
        ],
        outputs=[
            '"failed_task_id": "arch_005"',
            '"root_cause_identified": "Insufficient storage space on remote server. Available: 45MB, Required: 234MB"',
            '"alternative_server_1_space_gb": 4250',
            '"alternative_server_2_space_gb": 1800',
            '"remediation_log_created": true',
            '"user_contact": "@dave.intern"',
            '"remediation_plan_sent_to_ops": true',
            '"incident_fully_processed": true'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_004",
        instruction=(
            "You are a Security Analyst responding to 'INCIDENT-LOG-ISOLATION-01'. A potential security incident requires the immediate isolation of recent application logs on 'server-prod-01.company.com'. Your directive is to follow the secure evidence collection practice. This requires you to identify all target log files by applying the criteria from the standard file check task 'fc_task_001'. Once identified, you are to create a secure archive of these files, transfer the archive to the central evidence locker at '/storage/incident_evidence/' on 'backup-server.company.com' using an administrative account ('user_001'), and then purge the source log files from the production server to contain the incident. You must see this task through to completion, which includes performing a database modification to update the status of the original file check task, and logging the successful isolation of the potentially compromised files."
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_001"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-prod-01.company.com", "directory": "/var/log/applications"}),
            Action(name="create_archive_on_remote", kwargs={"hostname": "server-prod-01.company.com", "archive_path": "/tmp/INCIDENT-LOG-ISOLATION-01.tar.gz", "files_to_include": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_001"}),
            Action(name="transfer_file_to_remote", kwargs={"source_path": "/tmp/INCIDENT-LOG-ISOLATION-01.tar.gz", "remote_address": "backup-server.company.com", "destination_path": "/storage/incident_evidence/INCIDENT-LOG-ISOLATION-01.tar.gz", "ssh_key": "alice_rsa_key"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/var/log/applications/webapp.log"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/var/log/applications/api_requests.log"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/var/log/applications/error.log"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_001", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "INCIDENT-LOG-ISOLATION-01", "task_type": "forensics", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"})
        ],
        outputs=[
            '"policy_task_id": "fc_task_001"',
            '"files_identified_for_isolation": 3',
            '"evidence_archive_created": true',
            '"admin_key_retrieved": "alice_rsa_key"',
            '"evidence_transfer_successful": true',
            '"source_files_purged": 3',
            '"original_task_status_updated": true',
            '"forensics_task_logged": true',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_005",
        instruction=(
            "You are an Incident Responder assigned to 'INC-DIROP-PARTIAL-01'. The file organization task 'dir_op_001' was deferred. The user ('user_002') has requested a partial execution. After verifying the server's ('server-data-01.company.com') health is below the 80% operational threshold, proceed with a modified 'File Organization Protocol'. You must only move the CSV files to their correct destination. All other file types must be moved to a new '/data/deferred/' directory for later processing. Ensure you perform a database modification by updating the status for every file in the manifest. If we need to send a slack message,  send it to Operations with the message 'Incident INC-DIROP-PARTIAL-01: Partial completion for dir_op_001. CSV files moved to /data/sorted/csv. Non-CSV files moved to /data/deferred for later processing.'"
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/csv"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/deferred"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/sorted/csv/sales_data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/sorted/csv/customer_info.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/sorted/csv/data_0.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/data/deferred/inventory.dat"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/data/deferred/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/readme.txt", "destination_path": "/data/deferred/readme.txt"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "INC-DIROP-PARTIAL-01", "task_type": "incident_response", "user_id": "user_002"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations", "message": "Incident INC-DIROP-PARTIAL-01: Partial completion for dir_op_001. CSV files moved to /data/sorted/csv. Non-CSV files moved to /data/deferred for later processing."})
        ],
        outputs=[
            '"server_health_ok": true',
            '"directories_created": 2',
            '"csv_files_moved": 3',
            '"other_files_deferred": 3',
            '"all_statuses_updated": true',
            '"partial_completion_logged": true',
            '"slack_summary_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_006",
        instruction=(
            "You are a System Hygiene Specialist assigned to task 'HYGIENE-PROD-LOGS-01'. "
            "Your responsibility is to ensure proper archival and removal of outdated log files located in `/var/log/applications` on `server-prod-01.company.com`. "
            "Target files must be identified in compliance with the Standard File Check practices defined in maintenance task 'fc_task_001`. "
            "Archival is required under the 'Secure File Archive Creation Protocol', and only the files identified by the scan may be included. "
            "The archive must be stored in `/backups/log_hygiene/` on `backup-server.company.com`, with the operation carried out under the authority of the designated manager ('user_005'). "
            "In accordance with data lifecycle policy, any files successfully archived must then be purged from the source system. "
            "The system must reflect completion by updating the original file check task, logging the hygiene activity, and providing notification to stakeholders via the 'Operations' channel."
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_001"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-prod-01.company.com", "directory": "/var/log/applications"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "backup-server.company.com"}),
            Action(name="create_archive_on_remote", kwargs={"hostname": "server-prod-01.company.com", "archive_path": "/tmp/HYGIENE-PROD-LOGS-01.tar.gz", "files_to_include": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="transfer_file_to_remote", kwargs={"source_path": "/tmp/HYGIENE-PROD-LOGS-01.tar.gz", "remote_address": "backup-server.company.com", "destination_path": "/backups/log_hygiene/HYGIENE-PROD-LOGS-01.tar.gz", "ssh_key": "eve_rsa_key"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/var/log/applications/webapp.log"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/var/log/applications/api_requests.log"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/var/log/applications/error.log"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_001", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "HYGIENE-PROD-LOGS-01", "task_type": "system_hygiene", "user_id": "user_005"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"policy_task_id": "fc_task_001"',
            '"files_found_to_archive": 3',
            '"destination_disk_space_ok": true',
            '"archive_created": true',
            '"transfer_successful": true',
            '"source_files_purged": 3',
            '"original_task_status_updated": true',
            '"hygiene_task_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_008",
        instruction=(
            "You are a Data Custodian responsible for the final data lifecycle stage of the completed archive task 'arch_001'. Your directive is to purge all original source files from 'server-prod-01.company.com'. Before any deletions, you must perform the 'Pre-Execution Security Clearance Protocol' to ensure the original user ('user_001') is authorized. Once cleared, retrieve the archive's file manifest and systematically delete every source file. After purging, perform a database write to update the archive's status to 'verified', signifying the completion of its lifecycle. Conclude by logging the cleanup operation ('CLEANUP-ARCH-001') and notifying 'Operations'."
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_001"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_001"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "alice_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/src/main.js"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/src/utils.js"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/config/database.json"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/docs/readme.md"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/tests/unit_tests.py"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_001", "status": "verified"}),
            Action(name="log_task_completion", kwargs={"task_id": "CLEANUP-ARCH-001", "task_type": "archive_cleanup", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"archive_id": "arch_001"',
            '"security_clearance": "passed"',
            '"source_files_identified": 5',
            '"source_files_deleted": 5',
            '"task_status_updated": "verified"',
            '"cleanup_operation_logged": true',
            '"slack_notification_sent": true'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_010",
        instruction=(
            "You are a Data Integrity Auditor responsible for 'AUDIT-DIR-OP-001', performing a pre-flight integrity verification of the directory operation 'dir_op_001'. "
            "The audit requires validating that every file in the operation's manifest exists on 'server-data-01.company.com' and that each file’s live checksum matches the reference checksum stored in the manifest. "
            "The audit outcome must reflect whether all files pass these validations. "
            "If any file fails due to absence or checksum mismatch, the failure protocol must be enforced: the audit must be marked unsuccessful, a critical error log entry must be created identifying the file and the type of violation, all files in the operation must have their status updated to 'failed', and administrators must be notified through the 'System Alerts' channel."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_remote_file_checksum", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/sales_data.csv"}),
            Action(name="get_remote_file_checksum", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/customer_info.csv"}),
            Action(name="check_remote_file_exists", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/inventory.dat"}),
            Action(name="log_error_message", kwargs={"task_id": "AUDIT-DIR-OP-001", "task_type": "pre_flight_audit", "user_id": "user_002", "error_type": "file_not_found", "severity": "critical", "details_json": {"filepath": "/data/unsorted/inventory.dat", "server": "server-data-01.company.com"}}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "failed"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"})
        ],
        outputs=[
            '"audit_id": "AUDIT-DIR-OP-001"',
            '"files_to_audit": 6',
            '"files_verified": 2',
            '"audit_failed": true',
            '"failing_file": "/data/unsorted/inventory.dat"',
            '"error_log_created": true',
            '"files_in_operation": 6',
            '"file_statuses_updated_to_failed": 6',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_011",
        instruction=(
            "You are an Operations Coordinator assigned to task 'DEP-OP-002'. Your goal is to execute the file organization mandate 'dir_op_002'. This operation is dependent on first remediating a high disk usage issue on the target server, 'server-data-01.company.com'. You must begin by following the 'Stale File Cleanup Protocol' as defined in maintenance task 'fc_task_002', ensuring you only purge files that strictly match *all* defined policy filters (age and size). After the cleanup practice is fully complete, you may then proceed with the full 'File Organization Protocol' for 'dir_op_002' as requested by 'user_001'."
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_002", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_002", "task_type": "cleanup", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "File Check"}),
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_002"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_002"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/archive/projects/documents"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/archive/projects/source_code"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/archive/projects/data_files"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/archive/projects/miscellaneous"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/tmp/project_files/project_spec.pdf", "destination_path": "/archive/projects/documents/project_spec.pdf"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_007", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/tmp/project_files/src/main.py", "destination_path": "/archive/projects/source_code/main.py"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_008", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "DEP-OP-002", "task_type": "file_organization", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"dependency_check_passed": true',
            '"cleanup_protocol_initiated": true',
            '"files_purged": 1',
            '"cleanup_task_logged": true',
            '"main_operation_files_found": 2',
            '"directories_created": 4',
            '"main_operation_files_moved": 2',
            '"all_statuses_updated": true',
            '"main_operation_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_013",
        instruction=(
            "You are a Forensic Investigator assigned to 'RCA-STO-001', a root cause analysis for a high disk usage alert (82%) on 'storage-01.company.com'. "
            "Your mission is to find the cause. We need to confirm the live disk usage. Also to find the most recently completed 'archive' task that targeted this server; you have intelligence suggesting 'arch_002' is the likely candidate. "
            "Validate this by retrieving the archive's instructions. If confirmed, perform a database write, logging a new 'high' severity 'disk_space_warning' error using the RCA task ID. The log's details must include the server, its usage, the contributing task ID, and that task's archive size. "
            "Alert for administrators is needed ('user_001', 'user_005') in 'System Alerts' with the message: 'RCA Complete (RCA-STO-001): High disk usage (82%) on storage-01.company.com correlated with task arch_002 (487.0MB). @alice.admin @eve.manager please review.'"
        ),
        actions=[
            Action(name="check_remote_disk_space", kwargs={"hostname": "storage-01.company.com"}),
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_002"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "RCA-STO-001",
                    "task_type": "forensics",
                    "user_id": "system_agent",
                    "error_type": "disk_space_warning",
                    "severity": "high",
                    "details_json": {
                        "server": "storage-01.company.com", "usage_percent": 82, "likely_cause_task": "arch_002", "archive_size_bytes": 510654976
                    }
                }
            ),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_001"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_005"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "RCA Complete (RCA-STO-001): High disk usage (82%) on storage-01.company.com correlated with task arch_002 (487.0MB). @alice.admin @eve.manager please review."
                }
            ),
            Action(name="log_task_completion", kwargs={"task_id": "RCA-STO-001", "task_type": "investigation", "user_id": "system_agent"})
        ],
        outputs=[
            '"disk_usage_confirmed_percent": 82',
            '"contributing_task_id": "arch_002"',
            '"correlation_confirmed": true',
            '"incident_log_created": true',
            '"admin_1_contact": "@alice.admin"',
            '"admin_2_contact": "@eve.manager"',
            '"slack_escalation_sent": true',
            '"investigation_complete_and_logged": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_014",
        instruction=(
            "You are a Data Custodian. Your primary objective is to execute the pending archive operation 'arch_002' from initiation to final cleanup. You must follow the 'Secure File Archive Creation Protocol' to create and transfer the archive to its destination directory. After the transfer is complete, you must follow the appropriate data lifecycle practice by purging all original source files from 'server-analytics.company.com'. As a final step, perform a database modification by updating the archive's status to 'verified' to signify the completion of its lifecycle."
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_002"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "storage-01.company.com"}),
            Action(name="create_archive_on_remote", kwargs={"hostname": "server-analytics.company.com", "archive_path": "/tmp/analytics_data_archive_20240116_103000.tar.gz", "files_to_include": ["/analytics/raw_data/user_events_2023.csv", "/analytics/raw_data/page_views_2023.csv", "/analytics/processed/monthly_reports_2023.json", "/analytics/processed/yearly_summary_2023.pdf"]}),
            Action(name="transfer_file_to_remote", kwargs={"source_path": "/tmp/analytics_data_archive_20240116_103000.tar.gz", "remote_address": "storage-01.company.com", "destination_path": "/var/backups/analytics_data_archive_20240116_103000.tar.gz", "ssh_key": "carol_rsa_key"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_002", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "arch_002", "task_type": "archive", "user_id": "user_003"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "filepath": "/analytics/raw_data/user_events_2023.csv"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "filepath": "/analytics/raw_data/page_views_2023.csv"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "filepath": "/analytics/processed/monthly_reports_2023.json"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "filepath": "/analytics/processed/yearly_summary_2023.pdf"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_002", "status": "verified"})
        ],
        outputs=[
            '"archive_id": "arch_002"',
            '"disk_space_ok": true',
            '"archive_created": true',
            '"transfer_successful": true',
            '"initial_status_updated": "completed"',
            '"source_files_purged": 4',
            '"final_status_updated": "verified"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_015",
        instruction=(
            "You are a Data Migration Specialist assigned to 'MIGRATE-DATA-ONLY-001'. Your objective is to perform a partial migration of data-related files from the file organization mandate 'dir_op_001'. Before proceeding, you must ensure the operation is fully authorized and the target server, 'server-data-01.company.com', is ready for the operation. Once all pre-flight checks are passed, your directive is to identify only the data-specific files ('.dat' and '.json') from the operation's manifest and relocate them to a new pre-migration staging directory at '/staging/data_migration_q1/'. You are responsible for the full execution of this task, including performing database modifications to update the status of the moved files and logging the successful staging."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/staging/data_migration_q1"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/staging/data_migration_q1/inventory.dat"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/staging/data_migration_q1/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "MIGRATE-DATA-ONLY-001", "task_type": "data_staging", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"policy_task_id": "dir_op_001"',
            '"security_clearance_status": "passed"',
            '"disk_space_ok": true',
            '"files_identified_for_staging": 2',
            '"staging_directory_created": true',
            '"files_moved_to_staging": 2',
            '"original_task_files_updated": 2',
            '"staging_task_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_017",
        instruction=(
            "You are a Data Analyst Support Specialist assigned to 'PRIORITY-REVIEW-001'. A high-priority analysis requires immediate access to all CSV files from the pending sorting job 'dir_op_001'. Your objective is to intercept these specific files. You must identify all CSV files in the operation's manifest on 'server-data-01.company.com'. Instead of letting them proceed to the standard sorting destination, your directive is to relocate all identified CSV files to a new priority review directory, '/data/priority_review/20240120/'. You are responsible for the full execution of this task, including performing database modifications to update the status of the moved files within the original 'dir_op_001' mandate and logging the successful staging operation, and also send message to the 'Operation' channel"
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/priority_review/20240120"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/priority_review/20240120/sales_data.csv"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/priority_review/20240120/customer_info.csv"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/priority_review/20240120/data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "PRIORITY-REVIEW-001", "task_type": "data_staging", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"policy_task_id": "dir_op_001"',
            '"files_identified_for_staging": 3',
            '"staging_directory_created": true',
            '"files_moved_to_staging": 3',
            '"original_task_files_updated": 3',
            '"staging_task_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_018",
        instruction=(
            "You are a Data Security Officer assigned to conduct a pre-flight security audit for archive task 'arch_004'. Your directive is to enforce all security protocols before execution. You must perform the full 'Pre-Execution Security Clearance Protocol' for the requesting user ('user_005') against the target server 'document-vault.company.com'. If you discover a security policy violation, your protocol is to immediately halt the operation. You must then perform the necessary database writes to update the archive task's status to 'failed', log a 'critical' 'permission_denied' error detailing the exact violation, and escalate the incident by notifying the 'System Alerts' channel."
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_004"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_005"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_005"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "eve_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_004", "status": "failed"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_004",
                    "task_type": "security_audit",
                    "user_id": "user_005",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "Key 'eve_rsa_key' is not authorized for server 'document-vault.company.com' as per its authorized_servers list."
                    }
                }
            ),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"})
        ],
        outputs=[
            '"task_id": "arch_004"',
            '"user_role": "project_manager"',
            '"ssh_key_id": "eve_rsa_key"',
            '"authorization_check": "failed"',
            '"policy_violation_confirmed": true',
            '"task_status_updated": "failed"',
            '"security_error_logged": true',
            '"user_contact": "@eve.manager"',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_023",
        instruction=(
            "You are a Senior Systems Administrator. Your primary objective is to successfully complete the pending archive operation 'arch_001'. This is a critical task requiring full adherence to security and operational best practices. Before execution, you must ensure the user is authorized to access the destination server and that the server has adequate disk space for the operation. Once all pre-flight checks are passed, you are to create the archive on the source server, 'server-prod-01.company.com', and transfer it. Conclude by updating all relevant database records to reflect the task's completion and notifying the 'Operations' channel with the message: 'Archive task arch_001 completed successfully. Archive transferred to backup-server.company.com:/tmp/archives/.'"
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_001"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_001"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "alice_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "backup-server.company.com"}),
            Action(name="create_archive_on_remote", kwargs={"hostname": "server-prod-01.company.com", "archive_path": "/tmp/project_backup_2024.tar.gz", "files_to_include": ["/home/projects/webapp/src/main.js", "/home/projects/webapp/src/utils.js", "/home/projects/webapp/config/database.json", "/home/projects/webapp/docs/readme.md", "/home/projects/webapp/tests/unit_tests.py"]}),
            Action(name="transfer_file_to_remote", kwargs={"source_path": "/tmp/project_backup_2024.tar.gz", "remote_address": "backup-server.company.com", "destination_path": "/tmp/archives/project_backup_2024.tar.gz", "ssh_key": "alice_rsa_key"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_001", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "arch_001", "task_type": "archive", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations", "message": "Archive task arch_001 completed successfully. Archive transferred to backup-server.company.com:/tmp/archives/."})
        ],
        outputs=[
            '"archive_id": "arch_001"',
            '"security_clearance_status": "passed"',
            '"sufficient_disk_space": true',
            '"archive_created": true',
            '"transfer_successful": true',
            '"task_status_updated": "completed"',
            '"completion_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_025",
        instruction=(
            "You are an Operations Coordinator assigned to task 'DEP-OP-001'. Your goal is to execute the file organization mandate 'dir_op_001'. This operation is dependent on the health of the target server, 'server-data-01.company.com'. You must first perform a health check against a 75% disk usage threshold. If the server is unhealthy, you must first remediate the issue by following the 'Stale File Cleanup Protocol' for the designated cleanup task, 'fc_task_002'. After remediation is fully complete, you may proceed with the full 'File Organization Protocol' for 'dir_op_001'."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/cache_backup.dat"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_002", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_002", "task_type": "file_check", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "File Check"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/csv"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/dat"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/json"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/miscellaneous"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/sorted/csv/sales_data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/sorted/csv/customer_info.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/data/sorted/dat/inventory.dat"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/data/sorted/json/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/readme.txt", "destination_path": "/data/sorted/miscellaneous/readme.txt"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/sorted/csv/data_0.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "DEP-OP-001", "task_type": "file_organization", "user_id": "user_002"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"dependency_check_passed": true',
            '"cleanup_protocol_initiated": true',
            '"files_purged": 2',
            '"cleanup_task_logged": true',
            '"files_in_main_op": 6',
            '"main_operation_files_moved": 6',
            '"all_statuses_updated": true',
            '"main_operation_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_026",
        instruction=(
            "You are a Compliance Officer assigned to 'FIN-AUDIT-PREP-Q1'. Your objective is to prepare financial reports for a compliance audit. You must identify all relevant reports on 'server-analytics.company.com' by applying the rules defined in the standing audit task 'fc_task_003'. To prevent modification during the review, your directive is to securely isolate these files by relocating all identified reports to a new, centralized quarantine directory at '/secure/quarantine/financial_audit_q1/'. You are responsible for the full execution of this task, including performing a database modification to update the status of the underlying audit task and logging the successful preparation for the compliance review."
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_003"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-analytics.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-analytics.company.com", "directory": "/analytics/reports"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-analytics.company.com", "directory_path": "/secure/quarantine/financial_audit_q1"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/secure/quarantine/financial_audit_q1/daily_sales_report.csv"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-analytics.company.com", "source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/secure/quarantine/financial_audit_q1/monthly_trends.csv"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_003", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "FIN-AUDIT-PREP-Q1", "task_type": "compliance_prep", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"})
        ],
        outputs=[
            '"policy_task_id": "fc_task_003"',
            '"files_identified_for_quarantine": 2',
            '"quarantine_directory_created": true',
            '"files_moved_to_quarantine": 2',
            '"original_task_status_updated": true',
            '"compliance_task_logged": true',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_027",
        instruction=(
            "You are an Operations Coordinator assigned to task 'DEP-OP-001'. Your goal is to execute the file organization mandate 'dir_op_001'. This operation is dependent on the health of the target server, 'server-data-01.company.com'. You must first perform a health check against a 75% disk usage threshold. If the server is unhealthy, you must first remediate the issue by following the 'Stale File Cleanup Protocol' for the designated cleanup task, 'fc_task_002'. After remediation, you may proceed with the full 'File Organization Protocol' for 'dir_op_001'."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/cache_backup.dat"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_002", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_002", "task_type": "file_check", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "File Check"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/csv"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/dat"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/json"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/miscellaneous"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/sorted/csv/sales_data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/sorted/csv/customer_info.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/data/sorted/dat/inventory.dat"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/data/sorted/json/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/readme.txt", "destination_path": "/data/sorted/miscellaneous/readme.txt"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/sorted/csv/data_0.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "DEP-OP-001", "task_type": "file_organization", "user_id": "user_002"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"dependency_check_passed": true',
            '"cleanup_protocol_initiated": true',
            '"files_purged": 2',
            '"cleanup_task_logged": true',
            '"files_in_main_op": 6',
            '"main_operation_files_moved": 6',
            '"all_statuses_updated": true',
            '"main_operation_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_028",
        instruction=(
            "You are a Data Integrity Specialist. Before executing the archive operation 'arch_002', you must perform a mandatory pre-flight integrity audit on its source files, which reside on 'server-analytics.company.com'. Your directive is to follow the appropriate practice to verify every source file listed in the task's manifest. If any file is not found, you must immediately halt, update the archive's status to 'failed' in the database, log a 'critical' 'file_not_found' error, and alert 'System Alerts' with the message: 'Pre-flight audit for arch_002 FAILED: Source file /analytics/raw_data/page_views_2023.csv not found. Archival process halted.'"
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_002"}),
            Action(name="check_remote_file_exists", kwargs={"hostname": "server-analytics.company.com", "filepath": "/analytics/raw_data/user_events_2023.csv"}),
            Action(name="check_remote_file_exists", kwargs={"hostname": "server-analytics.company.com", "filepath": "/analytics/raw_data/page_views_2023.csv"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_002", "status": "failed"}),
            Action(name="log_error_message", kwargs={"task_id": "arch_002", "task_type": "pre_flight_audit", "user_id": "user_003", "error_type": "file_not_found", "severity": "critical", "details_json": {"filepath": "/analytics/raw_data/page_views_2023.csv"}}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "Pre-flight audit for arch_002 FAILED: Source file /analytics/raw_data/page_views_2023.csv not found. Archival process halted."})
        ],
        outputs=[
            '"archive_id": "arch_002"',
            '"files_to_audit": 4',
            '"audit_failed": true',
            '"failing_file": "/analytics/raw_data/page_views_2023.csv"',
            '"task_status_updated": "failed"',
            '"error_log_created": true',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_029",
        instruction=(
            "You are a Security Compliance Officer. A file check task, 'fc_task_001', has been requested by user 'user_005'. "
            "Before execution, you must perform the full pre-execution security clearance. "
            "This involves verifying the user's default SSH key is authorized for the target server and that their role ('project_manager') complies with the 'SSH Access Policy'. "
            "Only after confirming authorization and checking the server is online may you proceed with the file scan. "
            "Upon completion, update the task status, log the results, and notify the 'File Check' channel."
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_001"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_005"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "eve_rsa_key"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_005"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-prod-01.company.com", "directory": "/var/log/applications"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_001", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_001", "task_type": "file_check", "user_id": "user_005"}),
            Action(name="send_slack_message", kwargs={"channel_name": "File Check"})
        ],
        outputs=[
            '"task_id": "fc_task_001"',
            '"user_id": "user_005"',
            '"ssh_key_id": "eve_rsa_key"',
            '"authorization_status": "approved"',
            '"server_status": "online"',
            '"files_found_count": 3',
            '"task_completed_status": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_031",
        instruction=(
            "You are a Security Automation Engineer. The pending archive task 'arch_004' has been flagged for a security compliance review. Your directive is to audit this task against our 'SSH Access Policy'. You must determine if the user's role and SSH key authorizations permit access to the target server, 'document-vault.company.com'. If a policy violation is confirmed, you are required to immediately neutralize the threat by canceling the operation, logging a critical 'permission_denied' security error, and alerting the 'System Alerts' channel about the enforcement action."
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_004"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_005"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_005"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "eve_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_004", "status": "failed"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_004",
                    "task_type": "archive",
                    "user_id": "user_005",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {"reason": "Key 'eve_rsa_key' not authorized for server 'document-vault.company.com'."}
                }
            ),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"})
        ],
        outputs=[
            '"task_id": "arch_004"',
            '"user_role": "project_manager"',
            '"ssh_key_id": "eve_rsa_key"',
            '"authorization_check": "failed"',
            '"policy_violation_confirmed": true',
            '"task_status_updated": "failed"',
            '"security_error_logged": true',
            '"slack_alert_sent": true'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_032",
        instruction=(
            "You are an Automated Data Librarian. Your assignment is to execute the file organization mandate 'dir_op_001'. "
            "Your goal is to systematically process the entire contents of the '/data/unsorted' directory on 'server-data-01.company.com'. "
            "First, create the required subdirectory structure within '/data/sorted'. Then, you must meticulously relocate every file to its designated new home, "
            "ensuring each individual move is tracked by updating the file's status to 'completed'. Once all files are successfully organized, send a final confirmation to the 'Operations' channel."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/csv"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/dat"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/json"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/miscellaneous"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/sorted/csv/sales_data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/sorted/csv/customer_info.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/data/sorted/dat/inventory.dat"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/data/sorted/json/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/readme.txt", "destination_path": "/data/sorted/miscellaneous/readme.txt"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/sorted/csv/data_0.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"operation_id": "dir_op_001"',
            '"files_to_process": 6',
            '"directories_created": 4',
            '"files_moved": 6',
            '"file_statuses_updated": 6',
            '"task_fully_completed": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_033",
        instruction=(
            "You are an Incident Responder. A file check task, 'fc_task_004', has failed. Your mission is to conduct a root cause analysis by retrieving the technical error log. After confirming the root cause, "
            "your protocol requires you to create a formal, user-facing incident record by logging a new error message that summarizes the issue. "
            "Finally, identify the user who initiated the task and notify them with a detailed message in the 'System Alerts' channel: 'Incident report for task fc_task_004: Connection timeout to server-config.company.com. User: @bob.dev. Server is in maintenance mode.'"
        ),
        actions=[
            Action(name="get_error_log_details", kwargs={"task_id": "fc_task_004"}),
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_004"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "fc_task_004",
                    "task_type": "file_check",
                    "user_id": "user_002",
                    "error_type": "connection_timeout",
                    "severity": "high",
                    "details_json": {"server": "server-config.company.com", "reason": "Server is in maintenance mode."}
                }
            ),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_002"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "Incident report for task fc_task_004: Connection timeout to server-config.company.com. User: @bob.dev. Server is in maintenance mode."
                }
            )
        ],
        outputs=[
            '"failed_task_id": "fc_task_004"',
            '"root_cause": "Connection timeout to server-config.company.com - server may be in maintenance mode"',
            '"database_updated": true',
            '"new_error_msg_id": "err_msg_006"',
            '"user_contact": "@bob.dev"',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_034",
        instruction=(
            """You are a Proactive System Maintainer. A critical storage alert 'storage_alert_S01' is active for 'storage-01.company.com'. Confirm live disk usage. If usage_percent > 80, create a low_storage_warning log with structured fields (server, usage_percent, threshold_percent), then notify admins 'user_001' and 'user_005' via 'System Alerts' with the message ith the message: 'CRITICAL: Server storage-01.company.com has reached 82 percent disk usage. Immediate action required. @alice.admin @eve.manager please investigate.'.""",
        ),
        actions=[
            Action(name="check_remote_disk_space", kwargs={"hostname": "storage-01.company.com"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "storage_alert_S01",
                    "task_type": "system_monitoring",
                    "user_id": "system_agent",
                    "error_type": "low_storage_warning",
                    "severity": "warning",
                    "details_json": {"server": "storage-01.company.com", "usage_percent": 82, "threshold_percent": 80}
                }
            ),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_001"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_005"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "CRITICAL: Server storage-01.company.com has reached 82 percent disk usage. Immediate action required. @alice.admin @eve.manager please investigate."
                }
            ),
            Action(name="log_task_completion", kwargs={"task_id": "storage_alert_S01", "task_type": "system_monitoring", "user_id": "system_agent"})
        ],
        outputs=[
            '"disk_usage_percent": 82',
            '"threshold_exceeded": true',
            '"warning_log_created": true',
            '"admin_1_contact": "@alice.admin"',
            '"admin_2_contact": "@eve.manager"',
            '"escalation_complete": true',
            '"slack_notification_sent": true',
            '"completion_logged": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_037",
        instruction=(
            "You are an Incident Responder assigned to 'INC-FC004-MAINT', concerning the failure of task 'fc_task_004'. Your mission is to formally process this incident. First, investigate the failure by retrieving the original error log and confirming the live status and current resource load of the target server. After verifying the root cause, you must perform a database write by logging a new, formal incident record with 'medium' severity under the error type 'server_maintenance', using the incident ID as the task identifier. Conclude by composing and sending a structured notification message to the 'File Check' channel, which must include the incident ID, the affected user's slack handle, and the server's confirmed status."
        ),
        actions=[
            Action(name="get_error_log_details", kwargs={"task_id": "fc_task_004"}),
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_004"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-config.company.com"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-config.company.com"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_002"}),
            Action(
                name="log_error_message",
                kwargs={
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
                }
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "File Check",
                    "message": "Task Deferred: Task fc_task_004 for user @bob.dev is deferred. Reason: Target server server-config.company.com confirmed status is maintenance. Tracking ID: INC-FC004-MAINT."
                }
            ),
            Action(name="log_task_completion", kwargs={"task_id": "INC-FC004-MAINT", "task_type": "incident_response", "user_id": "system_agent"})
        ],
        outputs=[
            '"original_task_id": "fc_task_004"',
            '"root_cause": "Connection timeout to server-config.company.com - server may be in maintenance mode"',
            '"live_server_status": "maintenance"',
            '"root_cause_confirmed": true',
            '"incident_log_created": true',
            '"user_contact": "@bob.dev"',
            '"user_notification_sent": true',
            '"incident_response_logged": true',
            '"incident_fully_processed": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_040",
        instruction=(
            "You are a System Sentry assigned to incident 'HRA-SRVDATA-01' regarding high resource usage on 'server-data-01.company.com'. Your directive is to execute the 'Proactive Server Health Check Protocol' with a 70% utilization threshold. If breached, your escalation must include a forensic analysis of the '/data/temp' directory against the policy defined in task 'fc_task_002'. You must then log a 'warning' severity 'high_resource_usage' error using the incident ID, detailing the breached metrics and the count of policy-violating files. Conclude by alerting 'System Alerts' with a structured message including the incident ID and the server name."
        ),
        actions=[
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "HRA-SRVDATA-01",
                    "task_type": "system_monitoring",
                    "user_id": "system_agent",
                    "error_type": "high_resource_usage",
                    "severity": "warning",
                    "details_json": { "server": "server-data-01.company.com", "memory_percent": 72, "disk_percent": 78, "non_compliant_files_count": 1 }
                }
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "Health Alert (HRA-SRVDATA-01): server-data-01.company.com has breached resource thresholds. MEM: 72%, DSK: 78%."
                }
            ),
            Action(name="log_task_completion", kwargs={"task_id": "HRA-SRVDATA-01", "task_type": "system_monitoring", "user_id": "system_agent"})
        ],
        outputs=[
            '"incident_id": "HRA-SRVDATA-01"',
            '"threshold_exceeded": true',
            '"memory_usage": 72',
            '"disk_usage": 78',
            '"non_compliant_files_found": 1',
            '"warning_log_created": true',
            '"slack_alert_sent": true',
            '"investigation_complete": true'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_041",
        instruction=(
            "You are a System Hygiene Specialist responsible for the full lifecycle of maintenance task 'fc_task_002'. Your directive is to resolve this task, which involves purging stale files from the target server according to the task's defined policies. Before executing any file deletions, you must ensure the operation is secure by validating that the requesting user ('user_001') has fully authorized access to the target server. After successful execution and cleanup, you must finalize the process by updating all relevant database records and sending a comprehensive completion summary to the 'Operations' channel with the message: 'Maintenance task fc_task_002 completed successfully. A total of 2 stale files were purged from /data/temp on server-data-01.company.com.'"
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_001"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_001"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "alice_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/cache_backup.dat"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_002", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_002", "task_type": "file_check", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations", "message": "Maintenance task fc_task_002 completed successfully. A total of 2 stale files were purged from /data/temp on server-data-01.company.com."})
        ],
        outputs=[
            '"task_id": "fc_task_002"',
            '"security_clearance_status": "passed"',
            '"server_status": "online"',
            '"files_scanned": 2',
            '"non_compliant_files_found": 2',
            '"files_deleted": 2',
            '"task_status_updated": true',
            '"completion_logged": true',
            '"slack_notification_sent": true'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_042",
        instruction=(
            "You are a Deployment Coordinator assigned to 'DEPLOY-PREP-001'. Before a new data processing job is deployed, you must stage the relevant input files. Your directive is to isolate all CSV files from the file organization mandate 'dir_op_001' on 'server-data-01.company.com'. Instead of moving them to their final sorted location, you are to relocate all identified CSV files to a new, temporary staging directory at '/staging/data_processing_job_v2/'. You are responsible for the full execution of this task, including performing database modifications to update the status of the moved files within the original mandate and logging the successful staging operation."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/staging/data_processing_job_v2"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/staging/data_processing_job_v2/sales_data.csv"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/staging/data_processing_job_v2/customer_info.csv"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/staging/data_processing_job_v2/data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "DEPLOY-PREP-001", "task_type": "data_staging", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"policy_task_id": "dir_op_001"',
            '"files_identified_for_staging": 6',
            '"staging_directory_created": true',
            '"csv_files_moved_to_staging": 3',
            '"original_task_files_updated": 3',
            '"staging_task_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_043",
        instruction=(
            "You are a Data Staging Specialist assigned to 'STAGE-PROJECT-FILES-002'. Your objective is to prepare a set of project files for pre-production review. You must identify all files associated with the file organization mandate 'dir_op_002'. Instead of moving them to the final archive, your directive is to relocate all identified files to a new staging directory on 'server-data-01.company.com' at '/staging/review/dir_op_002/'. You are responsible for the full execution of this task, including performing a database modification to update the status of all files within the original mandate and logging the successful staging operation and send slack message to Operations"
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_002"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_002"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/staging/review/dir_op_002"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/tmp/project_files/project_spec.pdf", "destination_path": "/staging/review/dir_op_002/project_spec.pdf"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/tmp/project_files/src/main.py", "destination_path": "/staging/review/dir_op_002/main.py"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_007", "status": "completed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_008", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "STAGE-PROJECT-FILES-002", "task_type": "data_staging", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"policy_task_id": "dir_op_002"',
            '"files_identified_for_staging": 2',
            '"staging_directory_created": true',
            '"files_moved_to_staging": 2',
            '"original_task_files_updated": 2',
            '"staging_task_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_044",
        instruction=(
            "You are an Automated Data Librarian responsible for the file organization mandate 'dir_op_001'. Before executing the file moves, it is your duty to follow standard pre-flight operational practice. "
            "This includes a full readiness assessment of the target server, 'server-data-01.company.com', verifying both the requesting user's ('user_002') security clearance and the server's resource health. "
            "If you detect that the server is under heavy load (e.g., memory or disk usage > 75%), standard procedure requires you to log a 'high_resource_usage' warning and alert 'System Alerts' before proceeding. "
            "Once all pre-flight checks are passed, you are to execute the file organization task in its entirety, ensuring all files are moved and their statuses are updated."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "dir_op_001", "task_type": "pre_execution_check", "user_id": "user_002", "error_type": "high_resource_usage", "severity": "warning",
                    "details_json": { "server": "server-data-01.company.com", "disk_percent": 78, "threshold_percent": 75 }
                }
            ),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/csv"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/dat"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/json"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/miscellaneous"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/sorted/csv/sales_data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/sorted/csv/customer_info.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/data/sorted/dat/inventory.dat"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/data/sorted/json/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/readme.txt", "destination_path": "/data/sorted/miscellaneous/readme.txt"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/sorted/csv/data_0.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"operation_id": "dir_op_001"',
            '"security_clearance_status": "passed"',
            '"heavy_load_detected": true',
            '"warning_log_created": true',
            '"slack_alert_sent": true',
            '"files_to_process": 6',
            '"files_moved": 6',
            '"all_statuses_updated": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_046",
        instruction=(
            "You are a System Sentry responding to alert 'HRA-SRVPROD-01' for 'server-prod-01.company.com'. Your directive is to investigate the cause. "
            "Standard practice for this alert requires you to confirm if server resource usage (memory or disk) has breached the 50% operational threshold. "
            "If so, you must perform a forensic scan of the '/var/log/applications' directory to identify oversized files (>20MB). "
            "Following your analysis, you must log your findings and escalate by notifying the appropriate channels and personnel. The project manager for this system is Eve Brown ('user_005'). Your escalation should include a confirmation to 'System Alerts' and a remediation proposal to 'Operations' with the message: 'Remediation Plan for HRA-SRVPROD-01: Oversized files ['webapp.log', 'api_requests.log'] found in /var/log/applications. Recommend cleanup task. cc @eve.manager'"
        ),
        actions=[
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-prod-01.company.com", "directory": "/var/log/applications"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "HRA-SRVPROD-01", "task_type": "system_monitoring", "user_id": "system_agent", "error_type": "high_resource_usage", "severity": "warning",
                    "details_json": { "server": "server-prod-01.company.com", "threshold_percent": 50, "memory_percent": 58, "disk_percent": 65, "oversized_files_found": ["webapp.log", "api_requests.log"] }
                }
            ),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_005"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "High Resource Usage Confirmed: HRA-SRVPROD-01 on server-prod-01.company.com. MEM: 58%, DSK: 65%."}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "Operations",
                    "message": "Remediation Plan for HRA-SRVPROD-01: Oversized files ['webapp.log', 'api_requests.log'] found in /var/log/applications. Recommend cleanup task. cc @eve.manager"
                }
            ),
            Action(name="log_task_completion", kwargs={"task_id": "HRA-SRVPROD-01", "task_type": "investigation", "user_id": "system_agent"})
        ],
        outputs=[
            '"alert_id": "HRA-SRVPROD-01"',
            '"threshold_exceeded": true',
            '"oversized_files_count": 2',
            '"warning_log_created": true',
            '"system_alert_sent": true',
            '"remediation_plan_sent": true',
            '"investigation_logged": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_048",
        instruction=(
            "You are a Proactive System Maintainer responsible for audit 'HEALTH-AUDIT-02'. Your directive is to assess the health of 'server-prod-01.company.com' and 'server-data-01.company.com', enforcing a 75% disk usage threshold. If a server is found to be non-compliant, you must immediately escalate with an alert and then apply the standard remediation procedure for stale files as defined by maintenance task 'fc_task_002'. Conclude the audit by logging its completion and reporting a full summary of findings and actions taken to the 'Operations' channel with the message: 'System Health Audit HEALTH-AUDIT-02 complete. Server server-data-01.company.com exceeded disk threshold (78%) and was remediated by purging 2 stale files. Server server-prod-01.company.com is healthy.'"
        ),
        actions=[
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "HEALTH-AUDIT-02: Disk usage on server-data-01.company.com (78%) exceeds 75% threshold. Initiating cleanup."}),
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/cache_backup.dat"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_002", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_002", "task_type": "file_check", "user_id": "user_001"}),
            Action(name="log_task_completion", kwargs={"task_id": "HEALTH-AUDIT-02", "task_type": "system_health_audit", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations", "message": "System Health Audit HEALTH-AUDIT-02 complete. Server server-data-01.company.com exceeded disk threshold (78%) and was remediated by purging 2 stale files. Server server-prod-01.company.com is healthy."})
        ],
        outputs=[
            '"servers_checked": 2',
            '"threshold_breached_on": "server-data-01.company.com"',
            '"initial_alert_sent": true',
            '"cleanup_protocol_initiated": true',
            '"files_purged_count": 2',
            '"maintenance_task_status_updated": true',
            '"cleanup_task_logged": true',
            '"audit_operation_logged": true',
            '"slack_summary_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_050",
        instruction=(
            "You are an Automated Data Librarian. Your directive is to execute the file organization mandate 'dir_op_001', which has been delayed due to a low disk space warning. Your first priority is to conduct a full readiness assessment. This involves performing the 'Pre-Execution Security Clearance Protocol' for the requesting user ('user_002') and re-validating the health of the target server, 'server-data-01.company.com'. If all pre-flight checks pass, you are to proceed with the full 'File Organization Protocol' as originally specified. Conclude all operations with a final success notification to the 'Operations' channel."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/csv"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/dat"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/json"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/miscellaneous"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/sorted/csv/sales_data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/sorted/csv/customer_info.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/data/sorted/dat/inventory.dat"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/data/sorted/json/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/readme.txt", "destination_path": "/data/sorted/miscellaneous/readme.txt"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/sorted/csv/data_0.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"operation_id": "dir_op_001"',
            '"security_clearance": "passed"',
            '"server_health_ok": true',
            '"disk_space_ok": true',
            '"files_to_process": 6',
            '"directories_created": 4',
            '"files_moved": 6',
            '"all_statuses_updated": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_051",
        instruction=(
            "You are a Data Custodian attempting to perform post-archive cleanup for 'arch_002'. Your protocol requires a full security clearance check before deleting any files. You must validate that the original user ('user_003') has authorized access to the source server ('server-analytics.company.com') per the 'SSH Access Policy'. If a policy violation is discovered, you must halt the cleanup, perform a database write by logging a critical 'permission_denied' error, and escalate to the 'System Alerts' channel with the message: 'HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted.'"
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_002"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_003"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_003"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "carol_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_002_cleanup",
                    "task_type": "security_check",
                    "user_id": "user_003",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User role 'data_analyst' is not authorized for server 'server-analytics.company.com' per SSH Access Policy."
                    }
                }
            ),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_003"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted."
                }
            )
        ],
        outputs=[
            '"task_id": "arch_002_cleanup"',
            '"user_role": "data_analyst"',
            '"ssh_key_id": "carol_rsa_key"',
            '"security_clearance_status": "failed"',
            '"policy_violation_detected": true',
            '"cleanup_aborted": true',
            '"error_log_created": true',
            '"user_notified": "@carol.analyst"',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_052",
        instruction=(
            "You are a Security Operations Analyst conducting a post-mortem security review, 'SEC-REV-005', on the failed archive task 'arch_005'. Your directive is to perform the 'Pre-Execution Security Clearance Protocol' on the original task parameters. The task was initiated by 'user_004' to target 'personal-backup.company.com'. If you confirm a policy violation, you must log a new, separate 'critical' 'permission_denied' security violation error using the review ID. Following this, you must escalate by notifying system administrators ('user_001', 'user_005') via the 'System Alerts' channel with the message: 'CRITICAL SECURITY VIOLATION (SEC-REV-005): User @dave.intern (role: intern) attempted unauthorized archive operation to personal-backup.company.com. Key 'dave_rsa_key' is not authorized. cc @alice.admin @eve.manager'"
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_005"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_004"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_004"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "dave_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="log_error_message", kwargs={"task_id": "SEC-REV-005", "task_type": "security_review", "user_id": "user_004", "error_type": "permission_denied", "severity": "critical", "details_json": {"reason": "User 'user_004' (intern) with key 'dave_rsa_key' attempted access to unauthorized server 'personal-backup.company.com'."}}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_004"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_001"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "CRITICAL SECURITY VIOLATION (SEC-REV-005): User @dave.intern (role: intern) attempted unauthorized archive operation to personal-backup.company.com. Key 'dave_rsa_key' is not authorized. cc @alice.admin @eve.manager"})
        ],
        outputs=[
            '"review_id": "SEC-REV-005"',
            '"original_task_id": "arch_005"',
            '"policy_violation_confirmed": true',
            '"violating_user": "user_004"',
            '"unauthorized_server": "personal-backup.company.com"',
            '"security_error_logged": true',
            '"admin_1_contact": "@alice.admin"',
            '"admin_2_contact": "@eve.manager"',
            '"escalation_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_053",
        instruction=(
            "You are a Pre-flight Operations Coordinator for file organization task 'dir_op_001'. Your directive is to conduct a full 'System Readiness Assessment' before execution. You must follow standard operational practice, which requires verifying the user's security clearance for the target server 'server-data-01.company.com' and assessing the server's resource health against a 60% operational threshold for CPU and memory. If the server's health check fails, you must follow the standard procedure for postponing a task. This includes logging the issue, marking all constituent files of the operation as 'failed' to halt execution, and alerting the 'Operations' channel with the message: 'Task dir_op_001 postponed for user @bob.dev due to high resource usage on server-data-01.company.com (CPU: 62%, MEM: 72%).'"
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "dir_op_001", "task_type": "pre_execution_check", "user_id": "user_002", "error_type": "high_resource_usage", "severity": "warning",
                    "details_json": {"cpu_percent": 62, "memory_percent": 72, "threshold_percent": 60, "action_taken": "deferred"}
                }
            ),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "failed"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_002"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations", "message": "Task dir_op_001 postponed for user @bob.dev due to high resource usage on server-data-01.company.com (CPU: 62%, MEM: 72%)."})
        ],
        outputs=[
            '"task_id": "dir_op_001"',
            '"security_clearance_status": "passed"',
            '"server_cpu_usage": 62',
            '"health_check_status": "failed"',
            '"warning_log_created": true',
            '"files_in_operation": 6',
            '"file_statuses_updated_to_failed": 6',
            '"user_notified": "@bob.dev"',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_054",
        instruction=(
            "You are an Incident Commander conducting a full post-mortem on the failed archive task 'arch_005'. Your mission is a dual investigation. First, execute the 'Task Failure Diagnosis Protocol' to confirm the technical root cause. Second, because the task involved an intern, you must conduct a mandatory 'Pre-Execution Security Clearance Protocol' as a security review of the original operation. You must log your findings for both the technical failure and any discovered security violations. Conclude by sending a comprehensive incident report to 'System Alerts', notifying the responsible user and system administrators ('user_001', 'user_005') with the message: 'Post-mortem for arch_005 COMPLETE. Technical failure: Insufficient storage. Security review: Critical policy violation found. User: @dave.intern. See logs for details. cc @alice.admin @eve.manager'"
        ),
        actions=[
            Action(name="get_error_log_details", kwargs={"task_id": "arch_005"}),
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_005"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_004"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_004"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "dave_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="log_error_message", kwargs={"task_id": "arch_005", "task_type": "archive", "user_id": "user_004", "error_type": "insufficient_remote_storage", "severity": "medium", "details_json": {"reason": "Insufficient storage space on remote server personal-backup.company.com."}}),
            Action(name="log_error_message", kwargs={"task_id": "arch_005", "task_type": "security_review", "user_id": "user_004", "error_type": "permission_denied", "severity": "critical", "details_json": {"reason": "User 'user_004' (intern) attempted access to unauthorized server 'personal-backup.company.com'."}}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_004"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_001"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "Post-mortem for arch_005 COMPLETE. Technical failure: Insufficient storage. Security review: Critical policy violation found. User: @dave.intern. See logs for details. cc @alice.admin @eve.manager"})
        ],
        outputs=[
            '"incident_task_id": "arch_005"',
            '"technical_root_cause": "Insufficient storage space"',
            '"security_review_status": "failed"',
            '"policy_violation_confirmed": true',
            '"technical_error_logged": true',
            '"security_error_logged": true',
            '"user_contact": "@dave.intern"',
            '"admin_1_contact": "@alice.admin"',
            '"admin_2_contact": "@eve.manager"',
            '"slack_report_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_055",
        instruction=(
            "You are a Security Compliance Officer responsible for the pending file check task 'fc_task_001'. Before proceeding, you are required to ensure the operation is fully compliant with all security policies by conducting the standard pre-execution clearance. Once authorized, you must see the task through to completion by following the established file check protocol."
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_001"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_005"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "eve_rsa_key"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_005"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-prod-01.company.com", "directory": "/var/log/applications"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_001", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_001", "task_type": "file_check", "user_id": "user_005"}),
            Action(name="send_slack_message", kwargs={"channel_name": "File Check"})
        ],
        outputs=[
            '"task_id": "fc_task_001"',
            '"security_clearance": "passed"',
            '"server_status": "online"',
            '"files_found_count": 3',
            '"task_status_updated": true',
            '"completion_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_056",
        instruction=(
            "You are a Security Automation Engineer. Your directive is to process the file check task 'fc_task_004'. You must adhere to standard security procedure, which requires performing the full 'Pre-Execution Security Clearance Protocol' for the requesting user ('user_002') on the target server ('server-config.company.com'). If a policy violation is discovered, you must halt the operation, log a 'critical' 'permission_denied' error detailing the violation, and alert 'System Alerts' with the message: 'Task fc_task_004 aborted due to security policy violation. User @bob.dev does not have required permissions for server-config.company.com. See logs for details.'"
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_004"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="log_error_message", kwargs={"task_id": "fc_task_004", "task_type": "file_check", "user_id": "user_002", "error_type": "permission_denied", "severity": "critical", "details_json": {"reason": "User role 'developer' is not authorized for server 'server-config.company.com' per SSH Access Policy."}}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_002"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "Task fc_task_004 aborted due to security policy violation. User @bob.dev does not have required permissions for server-config.company.com. See logs for details."})
        ],
        outputs=[
            '"task_id": "fc_task_004"',
            '"user_role": "developer"',
            '"ssh_key_id": "bob_rsa_key"',
            '"security_clearance_status": "failed"',
            '"policy_violation_detected": true',
            '"task_aborted": true',
            '"error_log_created": true',
            '"user_notified": "@bob.dev"',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_058",
        instruction=(
            "You are a Data Provisioning Specialist assigned to 'PROVISION-LOGS-001'. An analyst ('user_003') requires a snapshot of recent application logs from 'server-prod-01.company.com' for a performance investigation. Your directive is to fulfill this request. You must identify the relevant log files by applying the criteria from the standard maintenance task 'fc_task_001'. Once identified, you are to securely copy these files to a new, temporary directory, '/data/temp/log_snapshot_20240120/', on 'server-data-01.company.com', which the analyst can access. This transfer must be facilitated by an administrator ('user_001'). You are responsible for the full execution of this task, including performing a database modification to update the status of the underlying maintenance task and logging the successful data provisioning."
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_001"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-prod-01.company.com", "directory": "/var/log/applications"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/temp/log_snapshot_20240120"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_001"}),
            Action(name="transfer_file_to_remote", kwargs={"source_path": "/var/log/applications/webapp.log", "remote_address": "server-data-01.company.com", "destination_path": "/data/temp/log_snapshot_20240120/webapp.log", "ssh_key": "alice_rsa_key"}),
            Action(name="transfer_file_to_remote", kwargs={"source_path": "/var/log/applications/api_requests.log", "remote_address": "server-data-01.company.com", "destination_path": "/data/temp/log_snapshot_20240120/api_requests.log", "ssh_key": "alice_rsa_key"}),
            Action(name="transfer_file_to_remote", kwargs={"source_path": "/var/log/applications/error.log", "remote_address": "server-data-01.company.com", "destination_path": "/data/temp/log_snapshot_20240120/error.log", "ssh_key": "alice_rsa_key"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_001", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "PROVISION-LOGS-001", "task_type": "data_provisioning", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"policy_task_id": "fc_task_001"',
            '"files_identified_for_provisioning": 3',
            '"destination_directory_created": true',
            '"admin_key_retrieved": "alice_rsa_key"',
            '"files_transferred": 3',
            '"original_task_status_updated": true',
            '"provisioning_task_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_059",
        instruction=(
            "You are an Incident Responder assigned to 'INC-DIROP-001' regarding the paused file organization task 'dir_op_001'. The task was halted due to a low disk space warning. Your mission is to re-assess the situation. First, perform a full readiness check, which includes verifying the user's ('user_002') security clearance and re-validating the live disk space on 'server-data-01.company.com'. If the space is now sufficient (e.g., more than 1GB available), you are to proceed with the 'File Organization Protocol' in its entirety. Upon successful completion, log the resolution of the incident and notify the 'Operations' channel that the task is now complete."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/csv"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/dat"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/json"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/miscellaneous"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/sorted/csv/sales_data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/sorted/csv/customer_info.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/data/sorted/dat/inventory.dat"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/data/sorted/json/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/readme.txt", "destination_path": "/data/sorted/miscellaneous/readme.txt"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/sorted/csv/data_0.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "INC-DIROP-001", "task_type": "incident_response", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"incident_id": "INC-DIROP-001"',
            '"original_task_id": "dir_op_001"',
            '"security_clearance": "passed"',
            '"disk_space_ok": true',
            '"files_to_process": 6',
            '"files_moved": 6',
            '"all_statuses_updated": true',
            '"incident_resolved_and_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_061",
        instruction=(
            "You are a Security and Hygiene Specialist assigned to task 'AUDIT-HYGIENE-01'. Your directive has two parts. First, you must conduct a security audit on user 'user_002' to ensure their SSH key authorizations comply with the 'SSH Access Policy'. You must log any discovered violations. Second, you are to execute a data hygiene task on 'server-data-01.company.com', following the 'Stale File Cleanup Protocol' as defined by maintenance task 'fc_task_002'. Conclude by logging the completion of the audit and sending a comprehensive summary of all findings and actions to the 'System Alerts' channel with the message: 'Audit & Cleanup AUDIT-HYGIENE-01 complete. Found 1 policy violation for user @bob.dev. Purged 1 stale file from server-data-01.com. See logs for details.'"
        ),
        actions=[
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="log_error_message", kwargs={"task_id": "AUDIT-HYGIENE-01", "task_type": "security_audit", "user_id": "user_002", "error_type": "permission_denied", "severity": "critical", "details_json": {"unauthorized_server": "backup-server.company.com", "policy_id": "sec_001"}}),
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_002", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_002", "task_type": "file_check", "user_id": "system_agent"}),
            Action(name="log_task_completion", kwargs={"task_id": "AUDIT-HYGIENE-01", "task_type": "security_audit", "user_id": "system_agent"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_002"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "Audit & Cleanup AUDIT-HYGIENE-01 complete. Found 1 policy violation for user @bob.dev. Purged 1 stale file from server-data-01.com. See logs for details."})
        ],
        outputs=[
            '"audit_id": "AUDIT-HYGIENE-01"',
            '"policy_violation_found": true',
            '"violation_logged": true',
            '"stale_files_identified": 1',
            '"files_purged": 1',
            '"cleanup_task_completed": true',
            '"cleanup_task_logged": true',
            '"overall_task_logged": true',
            '"violating_user_contact": "@bob.dev"',
            '"slack_summary_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_066",
        instruction=(
            "You are a Proactive System Maintainer executing 'HEALTH-AUDIT-02'. Your directive is to assess the health of 'server-prod-01.company.com' and 'server-data-01.company.com', enforcing a 75% disk usage threshold. If a server is found non-compliant, you must immediately escalate with an alert and then apply the standard 'Stale File Cleanup Protocol' for that server, using the policies defined in maintenance task 'fc_task_002'. After remediation, log the full audit and cleanup operation using the ID 'HEALTH-AUDIT-02' and send a comprehensive summary of actions to the 'Operations' channel with the message: 'System Health Audit HEALTH-AUDIT-02 complete. server-data-01.company.com exceeded disk threshold and was remediated by purging 2 stale files. server-prod-01.company.com is healthy.'"
        ),
        actions=[
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "HEALTH-AUDIT-02: Disk usage on server-data-01.company.com (78%) exceeds 75% threshold. Initiating cleanup."
                }
            ),
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/cache_backup.dat"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_002", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "HEALTH-AUDIT-02", "task_type": "system_health_audit", "user_id": "system_agent"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "Operations",
                    "message": "System Health Audit HEALTH-AUDIT-02 complete. server-data-01.company.com exceeded disk threshold and was remediated by purging 2 stale files. server-prod-01.company.com is healthy."
                }
            )
        ],
        outputs=[
            '"servers_checked": 2',
            '"threshold_breached_on": "server-data-01.company.com"',
            '"slack_alert_sent": true',
            '"cleanup_protocol_initiated": true',
            '"files_purged_count": 2',
            '"cleanup_task_status_updated": true',
            '"audit_operation_logged": true',
            '"slack_summary_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_068",
        instruction=(
            "You are a Data Quality Steward assigned to 'QUARANTINE-STALE-01'. Your objective is to enforce the data retention policy for temporary files on 'server-data-01.company.com'. You must identify all stale files in the '/data/temp' directory by applying the rules defined in maintenance task 'fc_task_002'. Instead of purging, your current directive is to quarantine these files for manual review. You are to relocate all identified files to a new directory, '/data/quarantine/stale_files_20240120/'. You are responsible for the full execution of this task, including performing a database modification to update the status of the underlying maintenance task and logging the successful quarantine operation and also send message to the slack channel for 'Operations'."
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/quarantine/stale_files_20240120"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/temp/temp_export_001.csv", "destination_path": "/data/quarantine/stale_files_20240120/temp_export_001.csv"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/quarantine/stale_files_20240120/cache_backup.dat"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_002", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "QUARANTINE-STALE-01", "task_type": "data_quarantine", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"policy_task_id": "fc_task_002"',
            '"files_identified_for_quarantine": 2',
            '"quarantine_directory_created": true',
            '"files_moved_to_quarantine": 2',
            '"original_task_status_updated": true',
            '"quarantine_task_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_069",
        instruction=(
            "You are a Data Custodian responsible for the final data lifecycle stage of the completed archive task 'arch_002'. Your directive is to purge all original source files. Before any deletions, you must perform the 'Pre-Execution Security Clearance Protocol' to ensure the original user ('user_003') is authorized for the source server, 'server-analytics.company.com'. If a policy violation is discovered, you must halt the cleanup, update the archive task's status to 'failed', log the security failure, and escalate to 'System Alerts' with the message: 'HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted.'"
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_002"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_003"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "carol_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_002", "status": "failed"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_002", "task_type": "archive_cleanup", "user_id": "user_003", "error_type": "permission_denied", "severity": "critical",
                    "details_json": {"reason": "User role 'data_analyst' is not authorized for server 'server-analytics.company.com' per SSH Access Policy."}
                }
            ),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_003"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted."
                }
            )
        ],
        outputs=[
            '"archive_id": "arch_002"',
            '"user_role": "data_analyst"',
            '"security_clearance_status": "failed"',
            '"policy_violation_detected": true',
            '"task_status_updated": "failed"',
            '"cleanup_aborted": true',
            '"error_log_created": true',
            '"user_notified": "@carol.analyst"',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_071",
        instruction=(
            "You are a Data Integrity Auditor assigned to 'AUDIT-DIR-OP-001'. An integrity audit is required for the file organization mandate 'dir_op_001' before it can be executed. Your objective is to validate every file listed in the operation's manifest on 'server-data-01.company.com'. You must follow the standard integrity verification practice, which includes checking for file existence and validating live checksums against the recorded values. If you discover any validation failure, you must follow the standard protocol for a failed audit: halt the operation by updating all relevant database records to prevent execution, log the specific failure, and escalate the issue to 'System Alerts' with the message: 'AUDIT-DIR-OP-001 FAILED: Integrity check failed for dir_op_001 on server-data-01.company.com. File not found: /data/unsorted/inventory.dat. Operation halted.'"
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="check_remote_file_exists", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/sales_data.csv"}),
            Action(name="get_remote_file_checksum", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/sales_data.csv"}),
            Action(name="check_remote_file_exists", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/inventory.dat"}),
            Action(name="log_error_message", kwargs={"task_id": "AUDIT-DIR-OP-001", "task_type": "pre_flight_audit", "user_id": "user_002", "error_type": "file_not_found", "severity": "critical", "details_json": {"filepath": "/data/unsorted/inventory.dat", "server": "server-data-01.company.com"}}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "failed"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "AUDIT-DIR-OP-001 FAILED: Integrity check failed for dir_op_001 on server-data-01.company.com. File not found: /data/unsorted/inventory.dat. Operation halted."})
        ],
        outputs=[
            '"audit_id": "AUDIT-DIR-OP-001"',
            '"files_to_audit": 6',
            '"files_verified_ok": 1',
            '"audit_failed": true',
            '"failing_file": "/data/unsorted/inventory.dat"',
            '"error_log_created": true',
            '"files_in_operation": 6',
            '"file_statuses_updated_to_failed": 6',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_073",
        instruction=(
            "You are a Data Custodian responsible for the final data lifecycle stage of the completed archive task 'arch_002'. Your directive is to purge all original source files. Before any deletions, you must perform the 'Pre-Execution Security Clearance Protocol' to ensure the original user ('user_003') is authorized for the source server, 'server-analytics.company.com'. If a policy violation is discovered, you must halt the cleanup, update the archive task's status to 'failed', log the security failure, and escalate to 'System Alerts' with the message: 'HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted.'"
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_002"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_003"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_003"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "carol_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_002", "status": "failed"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_002", "task_type": "archive_cleanup", "user_id": "user_003", "error_type": "permission_denied", "severity": "critical",
                    "details_json": {"reason": "User role 'data_analyst' is not authorized for server 'server-analytics.company.com' per SSH Access Policy."}
                }
            ),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_003"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted."
                }
            )
        ],
        outputs=[
            '"archive_id": "arch_002"',
            '"user_role": "data_analyst"',
            '"security_clearance_status": "failed"',
            '"policy_violation_detected": true',
            '"task_status_updated": "failed"',
            '"cleanup_aborted": true',
            '"error_log_created": true',
            '"user_notified": "@carol.analyst"',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_075",
        instruction=(
            "You are an Incident Responder assigned to 'INC-DIROP-RETRY-01'. The file organization task 'dir_op_001' was previously deferred due to high resource load on 'server-data-01.company.com'. Your mission is to re-assess the situation. First, perform a full readiness check, including verifying the user's ('user_002') security clearance and re-validating the server's live resource usage against a 60% operational threshold. If the server is still under excessive load, you must follow the standard deferral protocol: log the reason, update the status of all files in the operation to 'failed' to prevent re-queueing, and notify the 'Operations' channel with the message: 'Task dir_op_001 for @bob.dev has been deferred again due to persistent high resource usage (CPU: 62%, MEM: 72%) on server-data-01.company.com.'"
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "dir_op_001", "task_type": "pre_execution_check", "user_id": "user_002", "error_type": "high_resource_usage", "severity": "warning",
                    "details_json": {"cpu_percent": 62, "memory_percent": 72, "threshold_percent": 60, "action_taken": "deferred"}
                }
            ),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "failed"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_002"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations", "message": "Task dir_op_001 for @bob.dev has been deferred again due to persistent high resource usage (CPU: 62%, MEM: 72%) on server-data-01.company.com."})
        ],
        outputs=[
            '"task_id": "dir_op_001"',
            '"security_clearance_status": "passed"',
            '"server_cpu_usage": 62',
            '"health_check_status": "failed"',
            '"warning_log_created": true',
            '"files_in_operation": 6',
            '"file_statuses_updated_to_failed": 6',
            '"user_notified": "@bob.dev"',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_076",
        instruction=(
            "You are a Pre-flight Operations Coordinator. Your objective is to conduct a 'System Readiness Assessment' for the file organization task 'dir_op_001'. The assessment is passed if three conditions are met: 1. Available disk space on 'server-data-01.company.com' must be at least 20% greater than the total size of the files in the operation's manifest. 2. The server's real-time CPU and memory usage must both be at or below the 70% operational threshold. 3. The requesting user ('user_002') must be authorized for the server. If the operational threshold is exceeded, you must follow the appropriate practice to defer the task, which includes logging the issue, updating the status of all files in the operation to 'failed' to halt execution, and alerting 'System Alerts'."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="log_error_message", kwargs={"task_id": "dir_op_001", "task_type": "pre_execution_check", "user_id": "user_002", "error_type": "high_resource_usage", "severity": "warning", "details_json": {"server": "server-data-01.company.com", "memory_percent": 72, "threshold_percent": 70}}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "failed"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "failed"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"})
        ],
        outputs=[
            '"operation_id": "dir_op_001"',
            '"disk_space_ok": true',
            '"user_auth_ok": true',
            '"memory_usage_percent": 72',
            '"health_check_failed": true',
            '"warning_logged": true',
            '"files_halted": 6',
            '"task_deferred": true',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_077",
        instruction=(
            "You are a Proactive System Maintainer for audit 'HEALTH-AUDIT-DATA-TIER-02'. Your directive is to assess the health of 'server-data-01.company.com' and 'storage-01.company.com' against a 75% utilization threshold. You must follow standard practice for responding to health alerts. If a server is non-compliant and has a defined cleanup task (e.g., 'fc_task_002' for 'server-data-01.company.com'), you must apply the full 'Stale File Cleanup Protocol'. For any other non-compliant server, your protocol is to log a 'high_resource_usage' warning and escalate to system administrators ('user_001', 'user_005') via 'System Alerts'. After addressing all findings, log the completion of the audit and send a summary to 'Operations'."
        ),
        actions=[
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "storage-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "storage-01.company.com"}),
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/cache_backup.dat"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_002", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_002", "task_type": "file_check", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "File Check"}),
            Action(name="log_error_message", kwargs={"task_id": "HEALTH-AUDIT-DATA-TIER-02", "task_type": "health_check", "user_id": "system_agent", "error_type": "high_resource_usage", "severity": "warning", "details_json": {"server": "storage-01.company.com", "disk_percent": 82}}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"}),
            Action(name="log_task_completion", kwargs={"task_id": "HEALTH-AUDIT-DATA-TIER-02", "task_type": "system_health_audit", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"servers_audited": 2',
            '"remediation_initiated_for": "server-data-01.company.com"',
            '"files_purged": 2',
            '"cleanup_protocol_complete": true',
            '"warning_logged_for": "storage-01.company.com"',
            '"escalation_sent_for_storage": true',
            '"audit_complete_and_logged": true',
            '"slack_summary_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_080",
        instruction=(
            "You are an Operations Coordinator responsible for task 'DEP-OP-002', overseeing execution of the file organization mandate 'dir_op_002'. "
            "The operation is permitted only if the target server 'server-data-01.company.com' satisfies a disk usage threshold of 75% or lower. "
            "If this threshold is exceeded, the stale file policy defined in 'fc_task_002' must be enforced to remediate the server state before the organization task can proceed. "
            "The operation also requires user 'user_001' to pass security clearance under the 'SSH Access Policy'. "
            "Once the environment is compliant with these prerequisites, the 'File Organization Protocol' for 'dir_op_002' must be completed, with all activities properly logged and notifications dispatched to the designated Slack channels."
        ),
        actions=[
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_002", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_002", "task_type": "file_check", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "File Check"}),
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_002"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_001"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "alice_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_002"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/archive/projects/documents"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/archive/projects/source_code"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/tmp/project_files/project_spec.pdf", "destination_path": "/archive/projects/documents/project_spec.pdf"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_007", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/tmp/project_files/src/main.py", "destination_path": "/archive/projects/source_code/main.py"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_008", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "DEP-OP-002", "task_type": "file_organization", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"dependency_check_passed": true',
            '"cleanup_protocol_initiated": true',
            '"files_purged": 1',
            '"cleanup_task_logged": true',
            '"security_clearance_passed": true',
            '"main_operation_files_moved": 2',
            '"main_operation_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_081",
        instruction=(
            "You are an Incident Responder assigned to 'INC-DIROP-PARTIAL-01'. The file organization task 'dir_op_001' was deferred due to high server load. The user ('user_002') has requested a partial execution. Your mission is to re-assess the situation. First, verify the server's ('server-data-01.company.com') current resource usage is below the 80% operational threshold. If healthy, proceed with a modified 'File Organization Protocol'. You must only move the CSV files to their correct destination. All other files (DAT, JSON, TXT) must be moved to a new '/data/deferred/' directory for later processing. Ensure you update the status for every file in the manifest. Conclude by logging the partial completion and notifying 'Operations' with a detailed summary of which files were moved where."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/sorted/csv"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/data/deferred"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/sorted/csv/sales_data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/sorted/csv/customer_info.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_002", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/subdir/data.csv", "destination_path": "/data/sorted/csv/data_0.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_006", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/inventory.dat", "destination_path": "/data/deferred/inventory.dat"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_003", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/config.json", "destination_path": "/data/deferred/config.json"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_004", "status": "completed"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/readme.txt", "destination_path": "/data/deferred/readme.txt"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_005", "status": "completed"}),
            Action(name="log_task_completion", kwargs={"task_id": "INC-DIROP-PARTIAL-01", "task_type": "incident_response", "user_id": "user_002"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations", "message": "Incident INC-DIROP-PARTIAL-01: Partial completion for dir_op_001. CSV files moved to /data/sorted/csv. Non-CSV files moved to /data/deferred for later processing."})
        ],
        outputs=[
            '"server_health_ok": true',
            '"directories_created": 2',
            '"csv_files_moved": 3',
            '"other_files_deferred": 3',
            '"all_statuses_updated": true',
            '"partial_completion_logged": true',
            '"slack_summary_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_083",
        instruction=(
            "You are a Data Staging Specialist assigned to 'PRIORITY-DATA-STAGING-001'. A high-priority analysis requires the immediate staging of a critical sales data file from the pending sorting job 'dir_op_001'. Your directive is to manage this process on 'server-data-01.company.com'. Before relocation, you must follow the standard readiness assessment practice. This includes performing security clearance for the developer ('user_002') and, crucially, verifying the integrity of the target sales data file to prevent processing corrupt data. Once validated, you are to relocate the file to a new staging directory, '/staging/priority_review/20240120/'. You are responsible for the full execution of this task, including performing a database modification to update the status of the moved file and logging the successful staging. Conclude by notifying the developer that the file is ready for analysis with the message: 'Priority Staging Complete for PRIORITY-DATA-STAGING-001: The file sales_data.csv has been validated and moved to the priority review directory. cc @bob.dev'"
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_remote_file_checksum", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/sales_data.csv"}),
            Action(name="create_directory_on_remote", kwargs={"hostname": "server-data-01.company.com", "directory_path": "/staging/priority_review/20240120"}),
            Action(name="move_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "source_path": "/data/unsorted/sales_data.csv", "destination_path": "/staging/priority_review/20240120/sales_data.csv"}),
            Action(name="update_directory_operation_status", kwargs={"file_id": "file_001", "status": "completed"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_002"}),
            Action(name="log_task_completion", kwargs={"task_id": "PRIORITY-DATA-STAGING-001", "task_type": "data_staging", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations", "message": "Priority Staging Complete for PRIORITY-DATA-STAGING-001: The file sales_data.csv has been validated and moved to the priority review directory. cc @bob.dev"})
        ],
        outputs=[
            '"policy_task_id": "dir_op_001"',
            '"security_clearance_status": "passed"',
            '"files_identified_for_staging": 1',
            '"source_file_integrity_verified": true',
            '"staging_directory_created": true',
            '"files_moved_to_staging": 1',
            '"original_task_file_updated": 1',
            '"developer_contact_retrieved": "@bob.dev"',
            '"staging_task_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_085",
        instruction=(
            "You are a Data Custodian responsible for the final data lifecycle stage of the completed archive task 'arch_001'. Your directive is to purge all original source files from 'server-prod-01.company.com'. Before any deletions, you must perform the 'Pre-Execution Security Clearance Protocol' to ensure the original user ('user_001') is authorized. Once cleared, retrieve the archive's file manifest and systematically delete every source file listed. After purging all files, perform a database write to update the archive's status to 'verified', signifying the completion of its lifecycle. Conclude by logging the cleanup operation ('CLEANUP-ARCH-001') and notifying 'Operations'."
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_001"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_001"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "alice_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/src/main.js"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/src/utils.js"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/config/database.json"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/docs/readme.md"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/tests/unit_tests.py"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_001", "status": "verified"}),
            Action(name="log_task_completion", kwargs={"task_id": "CLEANUP-ARCH-001", "task_type": "archive_cleanup", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations"})
        ],
        outputs=[
            '"archive_id": "arch_001"',
            '"security_clearance": "passed"',
            '"source_files_identified": 5',
            '"source_files_deleted": 5',
            '"task_status_updated": "verified"',
            '"cleanup_operation_logged": true',
            '"slack_notification_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_086",
        instruction=(
            "You are a Data Security Officer assigned to conduct a pre-flight security audit for archive task 'arch_004'. Your directive is to enforce all security protocols before execution. Pre-Execution Security Clearance practice might be needed for the requesting user ('user_005') against the target server 'document-vault.company.com'. If you discover a security policy violation, your protocol is to immediately halt the operation. You must then perform the necessary database writes to update the archive task's status to 'failed', log a 'critical' 'permission_denied' error detailing the exact violation, and escalate the incident by notifying the 'System Alerts' channel with the message: 'Task arch_004 HALTED on security violation. User @eve.manager key is not authorized for document-vault.company.com.'"
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_004"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_005"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_005"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "eve_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_004", "status": "failed"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_004",
                    "task_type": "security_audit",
                    "user_id": "user_005",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "Key 'eve_rsa_key' is not authorized for server 'document-vault.company.com' as per its authorized_servers list."
                    }
                }
            ),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "Task arch_004 HALTED on security violation. User @eve.manager key is not authorized for document-vault.company.com."})
        ],
        outputs=[
            '"task_id": "arch_004"',
            '"user_role": "project_manager"',
            '"ssh_key_id": "eve_rsa_key"',
            '"authorization_check": "failed"',
            '"policy_violation_confirmed": true',
            '"task_status_updated": "failed"',
            '"security_error_logged": true',
            '"user_contact": "@eve.manager"',
            '"slack_alert_sent": true'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_088",
        instruction=(
            "You are a Data Custodian responsible for the final data lifecycle stage of the completed archive task 'arch_001'. Your directive is to purge all original source files from 'server-prod-01.company.com'. Before any deletions, you must perform the 'Pre-Execution Security Clearance Protocol' to ensure the original user ('user_001') is authorized. Once cleared, retrieve the archive's file manifest and systematically delete every source file. After purging, perform a database write to update the archive's status to 'verified', signifying the completion of its lifecycle. Conclude by logging the cleanup operation ('CLEANUP-ARCH-001') and notifying 'Operations' with the message: 'Lifecycle for arch_001 complete. Source files have been purged and task is now verified.'"
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_001"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_001"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_001"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "alice_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/src/main.js"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/src/utils.js"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/config/database.json"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/docs/readme.md"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-prod-01.company.com", "filepath": "/home/projects/webapp/tests/unit_tests.py"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_001", "status": "verified"}),
            Action(name="log_task_completion", kwargs={"task_id": "CLEANUP-ARCH-001", "task_type": "archive_cleanup", "user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations", "message": "Lifecycle for arch_001 complete. Source files have been purged and task is now verified."})
        ],
        outputs=[
            '"archive_id": "arch_001"',
            '"security_clearance": "passed"',
            '"source_files_identified": 5',
            '"source_files_deleted": 5',
            '"task_status_updated": "verified"',
            '"cleanup_operation_logged": true',
            '"slack_notification_sent": true'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_090",
        instruction=(
            "You are a Data Custodian attempting to perform post-archive cleanup for 'arch_002'. Your protocol requires a full security clearance check before deleting any files. You must validate that the original user ('user_003') has authorized access to the source server ('server-analytics.company.com') per the 'SSH Access Policy'. If a policy violation is discovered, you must halt the cleanup, perform a database write by logging a critical 'permission_denied' error, update the archive's status to 'failed', and escalate to the 'System Alerts' channel with the message: 'HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted.'"
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_002"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_003"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_003"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "carol_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_002_cleanup",
                    "task_type": "security_check",
                    "user_id": "user_003",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {
                        "reason": "User role 'data_analyst' is not authorized for server 'server-analytics.company.com' per SSH Access Policy."
                    }
                }
            ),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_002", "status": "failed"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_003"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "HALT on arch_002 cleanup: Security violation detected for user @carol.analyst. Unauthorized access to server-analytics.company.com. Cleanup aborted."
                }
            )
        ],
        outputs=[
            '"task_id": "arch_002_cleanup"',
            '"user_role": "data_analyst"',
            '"ssh_key_id": "carol_rsa_key"',
            '"security_clearance_status": "failed"',
            '"policy_violation_detected": true',
            '"cleanup_aborted": true',
            '"error_log_created": true',
            '"task_status_updated": "failed"',
            '"user_notified": "@carol.analyst"',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_091",
        instruction=(
            "You are a Pre-flight Auditor for a new task, 'arch_preflight_006'. Your mission is to verify the integrity of all source files intended for an archive. The manifest is: `['/data/unsorted/sales_data.csv', '/data/unsorted/customer_info.csv', '/data/unsorted/non_existent_report.csv']` on server `server-data-01.company.com`. You must follow standard practice to check for the existence of each file. If any file fails validation, halt, log the 'file_not_found' failure against the audit task ID, and alert 'Operations' with the message: 'Pre-flight audit arch_preflight_006 FAILED: Source file /data/unsorted/non_existent_report.csv not found on server-data-01.company.com. Archival process halted.'"
        ),
        actions=[
            Action(name="check_remote_file_exists", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/sales_data.csv"}),
            Action(name="check_remote_file_exists", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/customer_info.csv"}),
            Action(name="check_remote_file_exists", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/non_existent_report.csv"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_preflight_006",
                    "task_type": "pre_flight_audit",
                    "user_id": "system_agent",
                    "error_type": "file_not_found",
                    "severity": "critical",
                    "details_json": {"filepath": "/data/unsorted/non_existent_report.csv", "server": "server-data-01.company.com"}
                }
            ),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "Operations",
                    "message": "Pre-flight audit arch_preflight_006 FAILED: Source file /data/unsorted/non_existent_report.csv not found on server-data-01.company.com. Archival process halted."
                }
            )
        ],
        outputs=[
            '"audit_id": "arch_preflight_006"',
            '"files_to_verify": 3',
            '"files_verified_ok": 2',
            '"verification_failed": true',
            '"missing_file": "/data/unsorted/non_existent_report.csv"',
            '"error_logged": true',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_092",
        instruction=(
            "You are a Pre-flight Operations Coordinator assigned to audit the pending archive task 'arch_003' for user 'user_002'. You must conduct a full System Readiness Assessment. This involves performing the 'Pre-Execution Security Clearance Protocol' to validate the user's access to the destination server 'log-storage.company.com'. If the security check fails, you must follow standard procedure to halt the operation immediately, log a critical error detailing the specific failure, update the task status to 'failed', and escalate to 'System Alerts' with a detailed message."
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_003"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_002"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_002"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "bob_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_003", "status": "failed"}),
            Action(
                name="log_error_message",
                kwargs={
                    "task_id": "arch_003",
                    "task_type": "pre_execution_check",
                    "user_id": "user_002",
                    "error_type": "permission_denied",
                    "severity": "critical",
                    "details_json": {"reason": "User 'user_002' with role 'developer' is not authorized for server 'log-storage.company.com' per SSH Access Policy."}
                }
            ),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_002"}),
            Action(
                name="send_slack_message",
                kwargs={
                    "channel_name": "System Alerts",
                    "message": "Pre-flight check for task arch_003 failed: Security clearance denied for user @bob.dev on server log-storage.company.com. Task aborted."
                }
            )
        ],
        outputs=[
            '"task_id": "arch_003"',
            '"user_id": "user_002"',
            '"security_clearance_status": "failed"',
            '"policy_violation_detected": true',
            '"task_status_updated_to": "failed"',
            '"error_log_created": true',
            '"user_notified": "@bob.dev"',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_093",
        instruction=(
            "You are an Automated System Sentry assigned to audit 'HEALTH-AUDIT-PRIMARY-01'. Your directive is to assess the health of primary servers 'server-prod-01.company.com' and 'server-data-01.company.com' against a 75% disk usage threshold. If a server is non-compliant, you must immediately escalate by sending an alert and then apply the standard 'Stale File Cleanup Protocol' for that server, using the policies from maintenance task 'fc_task_002'. After addressing all findings, log the completion of the full audit and send a summary report of actions to 'Operations' with the message: 'HEALTH-AUDIT-PRIMARY-01 complete. Server server-data-01.company.com remediated (2 files purged). Server server-prod-01.company.com is healthy.'"
        ),
        actions=[
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-prod-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "HEALTH-AUDIT-PRIMARY-01: Disk usage on server-data-01.company.com (78%) exceeds threshold. Initiating automated cleanup."}),
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="delete_file_on_remote", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/temp/cache_backup.dat"}),
            Action(name="update_file_check_task_status", kwargs={"task_id": "fc_task_002", "completed": True}),
            Action(name="log_task_completion", kwargs={"task_id": "fc_task_002", "task_type": "file_check", "user_id": "user_001"}),
            Action(name="log_task_completion", kwargs={"task_id": "HEALTH-AUDIT-PRIMARY-01", "task_type": "system_health_audit", "user_id": "system_agent"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations", "message": "HEALTH-AUDIT-PRIMARY-01 complete. Server server-data-01.company.com remediated (2 files purged). Server server-prod-01.company.com is healthy."})
        ],
        outputs=[
            '"servers_audited": 2',
            '"server-prod-01_status": "healthy"',
            '"server-data-01_status": "unhealthy"',
            '"remediation_initiated": true',
            '"files_purged_count": 2',
            '"cleanup_task_logged": true',
            '"audit_complete_and_logged": true',
            '"slack_summary_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_094",
        instruction=(
            "You are a Data Integrity Auditor. Before file organization task 'dir_op_001' can proceed, you must conduct a mandatory pre-flight integrity audit. Your mission is to validate every file listed in the operation's manifest. For each file, you must confirm its existence on the source server ('server-data-01.company.com') and verify that its live checksum matches the checksum recorded in the manifest. If any file fails validation, you must immediately halt the process, log a 'file_not_found' error with the relevant details, and alert 'System Alerts'. If all files are verified, log the successful audit and notify 'Operations' that the organization task is cleared for execution."
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="check_remote_file_exists", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/sales_data.csv"}),
            Action(name="get_remote_file_checksum", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/sales_data.csv"}),
            Action(name="check_remote_file_exists", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/customer_info.csv"}),
            Action(name="get_remote_file_checksum", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/customer_info.csv"}),
            Action(name="check_remote_file_exists", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/inventory.dat"}),
            Action(name="log_error_message", kwargs={"task_id": "dir_op_001", "task_type": "pre_flight_audit", "user_id": "user_002", "error_type": "file_not_found", "severity": "critical", "details_json": {"filepath": "/data/unsorted/inventory.dat"}}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts"})
        ],
        outputs=[
            '"operation_id": "dir_op_001"',
            '"files_to_audit": 6',
            '"files_verified": 2',
            '"audit_failed": true',
            '"failing_file": "/data/unsorted/inventory.dat"',
            '"error_log_created": true',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_095",
        instruction=(
            "You are a Compliance Officer assigned to 'AUDIT-FC-005'. The file check task 'fc_task_005' completed, but a post-execution audit is required. Your directive is to verify the operation's compliance. You must follow the appropriate practice, which includes performing the 'Pre-Execution File Transfer Security Clearance Protocol' for the original user ('user_004'). If you discover a security violation, you must halt, log the violation, and escalate. If compliant, you must retrieve the task's completion message to find its log file and archive it to 'backup-server.company.com' in the '/storage/audit_evidence/' directory."
        ),
        actions=[
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_005"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_004"}),
            Action(name="get_user_default_ssh_key", kwargs={"user_id": "user_004"}),
            Action(name="get_ssh_key_by_id", kwargs={"key_id": "dave_rsa_key"}),
            Action(name="get_security_policy_by_name", kwargs={"policy_name": "SSH Access Policy"}),
            Action(name="log_error_message", kwargs={"task_id": "AUDIT-FC-005", "task_type": "compliance_audit", "user_id": "user_004", "error_type": "permission_denied", "severity": "critical", "details_json": {"reason": "User 'dave_intern' (intern) is not authorized for server 'server-prod-01.company.com' per SSH Access Policy."}}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_004"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "AUDIT-FC-005 FAILURE: Security violation detected for user @dave.intern during post-execution audit of fc_task_005. Operation was non-compliant."})
        ],
        outputs=[
            '"audit_id": "AUDIT-FC-005"',
            '"original_task_id": "fc_task_005"',
            '"user_role": "intern"',
            '"security_clearance_status": "failed"',
            '"policy_violation_detected": true',
            '"audit_halted": true',
            '"error_log_created": true',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_096",
        instruction=(
            "You are an Automated System Sentry assigned to incident 'HRA-SRVDATA-01' regarding high resource usage on 'server-data-01.company.com'. Your directive is to execute the 'Proactive Server Health Check Protocol' with a 70% utilization threshold. If breached, your escalation must include a forensic analysis of the '/data/temp' directory against the policy defined in task 'fc_task_002'. You must then log a 'warning' severity 'high_resource_usage' error using the incident ID, detailing the breached metrics and the count of policy-violating files. Conclude by alerting 'System Alerts' with a structured message including the incident ID, the server name, and the number of non-compliant files found."
        ),
        actions=[
            Action(name="get_server_resource_usage", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="check_remote_disk_space", kwargs={"hostname": "server-data-01.company.com"}),
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_002"}),
            Action(name="scan_remote_directory", kwargs={"hostname": "server-data-01.company.com", "directory": "/data/temp"}),
            Action(name="log_error_message", kwargs={"task_id": "HRA-SRVDATA-01", "task_type": "system_monitoring", "user_id": "system_agent", "error_type": "high_resource_usage", "severity": "warning", "details_json": { "server": "server-data-01.company.com", "memory_percent": 72, "disk_percent": 78, "non_compliant_files_count": 1 }}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "Health Alert (HRA-SRVDATA-01): server-data-01.company.com has breached resource thresholds (MEM: 72%, DSK: 78%). Found 1 non-compliant file in /data/temp."}),
            Action(name="log_task_completion", kwargs={"task_id": "HRA-SRVDATA-01", "task_type": "system_monitoring", "user_id": "system_agent"})
        ],
        outputs=[
            '"incident_id": "HRA-SRVDATA-01"',
            '"threshold_exceeded": true',
            '"memory_usage": 72',
            '"disk_usage": 78',
            '"non_compliant_files_found": 1',
            '"warning_log_created": true',
            '"slack_alert_sent": true',
            '"investigation_complete": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_097",
        instruction=(
            "You are a Forensic Investigator assigned to 'RCA-FC-004' regarding a 'connection_timeout' error on file check task 'fc_task_004' for user 'user_002'. Your mission is to conduct a root cause analysis. You must follow the appropriate diagnostic practice, which requires retrieving the original error log to identify the server and confirm its live status. If the server is confirmed to be in maintenance, log a new 'server_maintenance' error for this RCA task with 'medium' severity, summarizing your findings. Conclude by notifying the user and their manager ('user_005') in the 'Operations' channel with the message: 'RCA for fc_task_004 complete: Failure was due to scheduled maintenance on server-config.company.com. No further action needed. cc @eve.manager @bob.dev'"
        ),
        actions=[
            Action(name="get_error_log_details", kwargs={"task_id": "fc_task_004"}),
            Action(name="get_file_check_task_by_id", kwargs={"task_id": "fc_task_004"}),
            Action(name="get_server_status_by_hostname", kwargs={"hostname": "server-config.company.com"}),
            Action(name="log_error_message", kwargs={"task_id": "RCA-FC-004", "task_type": "forensics", "user_id": "user_002", "error_type": "server_maintenance", "severity": "medium", "details_json": {"reason": "Server confirmed to be in maintenance mode.", "original_task": "fc_task_004"}}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_002"}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_005"}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations", "message": "RCA for fc_task_004 complete: Failure was due to scheduled maintenance on server-config.company.com. No further action needed. cc @eve.manager @bob.dev"}),
            Action(name="log_task_completion", kwargs={"task_id": "RCA-FC-004", "task_type": "investigation", "user_id": "system_agent"})
        ],
        outputs=[
            '"rca_task_id": "RCA-FC-004"',
            '"original_error_confirmed": "Connection timeout"',
            '"live_server_status": "maintenance"',
            '"root_cause_confirmed": "Server maintenance"',
            '"incident_log_created": true',
            '"user_notified": "@bob.dev"',
            '"manager_notified": "@eve.manager"',
            '"investigation_logged": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_098",
        instruction=(
            "You are a Data Migration Specialist responsible for 'MIGRATE-PROJECTS-001'. Your directive is to move a set of project files as defined in 'dir_op_001' on server 'server-data-01.company.com'. Before the migration, you must verify the integrity of every file in the manifest by following the appropriate integrity verification practice. This involves checking for each file's existence and validating its live checksum. If any file fails validation, you must halt the operation, log a 'file_not_found' error, and escalate to 'Operations' with the message: 'MIGRATE-PROJECTS-001 HALTED: Pre-flight integrity check failed. File not found: /data/unsorted/inventory.dat. Migration aborted.'"
        ),
        actions=[
            Action(name="get_directory_operation_by_id", kwargs={"operation_id": "dir_op_001"}),
            Action(name="get_files_for_directory_operation", kwargs={"operation_id": "dir_op_001"}),
            Action(name="check_remote_file_exists", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/sales_data.csv"}),
            Action(name="get_remote_file_checksum", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/sales_data.csv"}),
            Action(name="check_remote_file_exists", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/customer_info.csv"}),
            Action(name="get_remote_file_checksum", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/customer_info.csv"}),
            Action(name="check_remote_file_exists", kwargs={"hostname": "server-data-01.company.com", "filepath": "/data/unsorted/inventory.dat"}),
            Action(name="log_error_message", kwargs={"task_id": "MIGRATE-PROJECTS-001", "task_type": "file_migration", "user_id": "user_002", "error_type": "file_not_found", "severity": "critical", "details_json": {"filepath": "/data/unsorted/inventory.dat", "server": "server-data-01.company.com"}}),
            Action(name="send_slack_message", kwargs={"channel_name": "Operations", "message": "MIGRATE-PROJECTS-001 HALTED: Pre-flight integrity check failed. File not found: /data/unsorted/inventory.dat. Migration aborted."})
        ],
        outputs=[
            '"migration_task_id": "MIGRATE-PROJECTS-001"',
            '"files_to_verify": 6',
            '"integrity_check_passed_for": 2',
            '"integrity_check_failed": true',
            '"failing_file": "/data/unsorted/inventory.dat"',
            '"operation_halted": true',
            '"error_log_created": true',
            '"slack_alert_sent": true'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_100",
        instruction=(
            "You are a Security Compliance Officer assigned post-completion audits 'AUDIT-ARCH-001'. The archive task 'arch_001' was reported as having transfer integrity issues. Your directive is to verify the operation's final state and compliance. You must locate the final archive file on 'backup-server.company.com' based on details from the original task instructions and any related error logs. If the file is missing, you must log a 'critical' 'file_not_found' error against this audit task and escalate to 'System Alerts' with the message: 'AUDIT FAILURE (AUDIT-ARCH-001): Final archive for task arch_001 is MISSING from destination. Immediate investigation required. cc @alice.admin'"
        ),
        actions=[
            Action(name="get_archive_instructions_by_id", kwargs={"archive_id": "arch_001"}),
            Action(name="get_error_log_details", kwargs={"task_id": "arch_001"}),
            Action(name="check_remote_file_exists", kwargs={"hostname": "backup-server.company.com", "filepath": "/tmp/archives/project_backup_2024_20240115_160000.tar.gz"}),
            Action(name="get_user_info_by_id", kwargs={"user_id": "user_001"}),
            Action(name="log_error_message", kwargs={"task_id": "AUDIT-ARCH-001", "task_type": "security_audit", "user_id": "user_001", "error_type": "file_not_found", "severity": "critical", "details_json": {"server": "backup-server.company.com", "filepath": "/tmp/archives/project_backup_2024_20240115_160000.tar.gz"}}),
            Action(name="get_user_contact_info", kwargs={"user_id": "user_001"}),
            Action(name="send_slack_message", kwargs={"channel_name": "System Alerts", "message": "AUDIT FAILURE (AUDIT-ARCH-001): Final archive for task arch_001 is MISSING from destination. Immediate investigation required. cc @alice.admin"}),
            Action(name="update_archive_task_status", kwargs={"archive_id": "arch_001", "status": "failed"}),
            Action(name="log_task_completion", kwargs={"task_id": "AUDIT-ARCH-001", "task_type": "security_audit", "user_id": "system_agent"})
        ],
        outputs=[
            '"audit_id": "AUDIT-ARCH-001"',
            '"archive_existence_verified": false',
            '"error_log_created": true',
            '"slack_escalation_sent": true',
            '"original_task_status_updated": "failed"',
            '"audit_logged_as_complete": true'
        ]
    ),
]
