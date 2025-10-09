from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="001",
        instruction=(
            "You are a System Administrator. The disk usage on 'server-prod-01.company.com' is getting high. "
            "Find all log files in '/var/log/applications', create a record of the files to be archived, "
            "then create and transfer the archive 'prod_logs_backup' to 'backup-server.company.com:/tmp/archives'. "
            "After a successful transfer, delete the original log files to free up space. "
            "Also, log a completion message for this task and notify the 'System Alerts' channel with message 'Disk space cleared.'. "
            "For task id use 'arch_006' and for user_id 'user_001'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "arch_006", "user_id": "user_001", "task_type": "monitoring"}),
            # Action(name="CheckDiskSpace", kwargs={"server_hostname": "server-prod-01.company.com"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "arch_006", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_001", "destination_directory": "/tmp/archives", "remote_address": "backup-server.company.com", "archive_name": "prod_logs_backup", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="TransferFile", kwargs={"source_path": "/tmp/archives/prod_logs_backup.tar.gz", "destination_path": "backup-server.company.com:/tmp/archives/prod_logs_backup.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/var/log/applications/webapp.log"}),
            Action(name="DeleteFile", kwargs={"filepath": "/var/log/applications/api_requests.log"}),
            Action(name="DeleteFile", kwargs={"filepath": "/var/log/applications/error.log"}),
            # Action(name="UpdateTaskStatus", kwargs={"task_id": "arch_006", "new_status": "completed"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "arch_006", "user_id": "user_001", "message": "Disk space cleared."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Disk space cleared."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="002",
        instruction=(
            "You are a DevOps Engineer. A new project requires an organized directory structure on 'server-data-01.company.com'. "
            "You should create three new directories: '/data/sorted/csv', '/data/sorted/dat', and '/data/sorted/json'. "
            "Then, log the files to be moved and proceed to move 'sales_data.csv' and 'customer_info.csv' from '/data/unsorted' to the new 'csv' directory. "
            "Also, log a completion message for this task and notify the 'Operations' channel with message 'Project file structure created.'. "
            "For task id use 'dir_op_001' and for user_id 'user_002'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "dir_op_001", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/sorted/csv"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/sorted/dat"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/sorted/json"}),
            Action(name="CreateFileList", kwargs={"operation_id": "dir_op_001", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/sorted/csv/sales_data.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/sorted/csv/customer_info.csv"}),
            # Action(name="UpdateTaskStatus", kwargs={"task_id": "dir_op_001", "new_status": "completed"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "dir_op_001", "user_id": "user_002", "message": "Project file structure created."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Project file structure created."}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="003",
        instruction=(
            "You are a Data Analyst. You need to perform a file check for pending files on the analytics server. "
            "Create a file list entry for '/analytics/reports/daily_sales_report.csv' as part of an audit. "
            "And, retrieve its metadata from '/analytics/reports' on 'server-analytics.company.com'."
            "Also, log a completion message for this task and notify the 'Operations' channel with message 'File check completed.'. "
            "For task id use 'fc_task_003' and for user_id 'user_003'. "

        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "fc_task_003", "user_id": "user_003", "task_type": "monitoring"}),
            # Action(name="GetPendingFileChecks", kwargs={}),
            Action(name="CreateFileList", kwargs={"operation_id": "fc_task_003", "filepaths": ["/analytics/reports/daily_sales_report.csv"]}),
            Action(name="GetFileMetadata", kwargs={"server_hostname": "server-analytics.company.com", "filepath": "/analytics/reports/daily_sales_report.csv"}),
            # Action(name="UpdateTaskStatus", kwargs={"task_id": "fc_task_003", "new_status": "completed"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "fc_task_003", "user_id": "user_003", "message": "File check completed."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "File check completed."}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="005",
        instruction=(
            "You are a Project Manager. A project has been completed, and its temporary files on 'server-data-01.company.com' need to be cleaned up. "
            "You should create a file list record for 'temp_export_001.csv' to log the deletion. "
            "Also, delete the file from the '/data/temp' directory and check the available disk space to confirm cleanup. "
            "Update the task log and send a confirmation to the 'Operations' channel with message 'Temporary project files have been cleaned up.'."
            "For task id use 'dir_op_003' and for user_id 'user_005'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "dir_op_003", "user_id": "user_005", "task_type": "monitoring"}),
            Action(name="CreateFileList", kwargs={"operation_id": "dir_op_003", "filepaths": ["/data/temp/temp_export_001.csv"]}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="CheckDiskSpace", kwargs={"server_hostname": "server-data-01.company.com"}),
            # Action(name="UpdateTaskStatus", kwargs={"task_id": "dir_op_003", "new_status": "completed"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "dir_op_003", "user_id": "user_005", "message": "Temporary project files have been cleaned up."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Temporary project files have been cleaned up."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="006",
        instruction=(
            "You are a developer with a focus on security, ensure the webapp's critical api requests file, "
            "located at `/var/log/applications/api_requests.log` on `server-prod-01.company.com`, "
            "is securely backed up. The backup must be stored at `/backups/configs/api_requests.log` "
            "on `backup-server.company.com`. "
            "Confirm the integrity of the backup by performing a checksum verification. "
            "The entire operation must be logged, and a confirmation of the successful and "
            "verified backup should be sent to the 'Operations' channel with message 'Backup completed successfully with checksum verification.'. "
            "For task id you should use 'backup_op_001' and for user_id 'user_002'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "backup_op_001", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateFileList", kwargs={"operation_id": "backup_op_001", "filepaths": ["/var/log/applications/api_requests.log"]}),
            Action(name="TransferFile", kwargs={"source_path": "/var/log/applications/api_requests.log", "destination_path": "backup-server.company.com:/backups/configs/api_requests.log"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_009", "filepath": "backup-server.company.com:/backups/configs/api_requests.log"}),
            # Action(name="UpdateTaskStatus", kwargs={"task_id": "backup_op_001", "new_status": "completed"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "backup_op_001", "user_id": "user_002", "message": "Backup completed successfully with checksum verification."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Backup completed successfully with checksum verification."})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="007",
        instruction=(
            "As a compliance officer, you must periodically verify the integrity of critical data files. Please verify that the checksum for the main analytics archive, located at `/storage/archives/analytics_data_archive_20240116_103000.tar.gz` on `storage-01.company.com`, has not changed. "
            "Log the result of this audit and report the status to the 'System Alerts' channel with message 'File integrity is confirmed.'. "
            "For task id you should use 'audit_op_001' and for user_id 'user_005'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "audit_op_001", "user_id": "user_005", "task_type": "monitoring"}),
            Action(name="CreateFileList", kwargs={"operation_id": "audit_op_001", "filepaths": ["/storage/archives/analytics_data_archive_20240116_103000.tar.gz"]}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_009", "filepath": "storage-01.company.com:/storage/archives/analytics_data_archive_20240116_103000.tar.gz"}),
            # Action(name="UpdateTaskStatus", kwargs={"task_id": "audit_op_001", "new_status": "completed"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "audit_op_001", "user_id": "user_005", "message": "File integrity is confirmed."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "File integrity is confirmed."})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="049",
        instruction=(
            "You are a Data Analyst preparing for a new experiment. On `server-analytics.company.com`, create a dedicated directory for your work at `/analytics/experiments/exp_01/`. Move the primary raw dataset, `user_events_2023.csv`, from `/analytics/raw_data` into your new experiment directory to begin your analysis without touching the original report files. "
            "Notify the 'File Check' channel with the message 'Experiment workspace exp_01 is ready with source data.'. "
            "For task id you should use 'exp_setup_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "exp_setup_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/experiments"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/experiments/exp_01"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/raw_data"}),
            Action(name="CreateFileList", kwargs={"operation_id": "exp_setup_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/raw_data/user_events_2023.csv", "destination_path": "/analytics/experiments/exp_01/user_events_2023.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "exp_setup_01", "user_id": "user_003", "message": "Experiment workspace exp_01 is ready with source data."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Experiment workspace exp_01 is ready with source data."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="050",
        instruction=(
            "You are a System Administrator implementing a data tiering policy on `server-data-01.company.com`. Create a new structure at `/data/tiered_storage/` with `hot` and `cold` subdirectories. Based on file type (from '/data/temp'), move the `temp_export_001.csv` to `hot` and the `cache_backup.dat` to `cold`. "
            "Announce the completion in the 'System Alerts' channel with the message 'Temporary data has been tiered into hot and cold storage.'. "
            "For task id you should use 'tiering_setup_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "tiering_setup_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/tiered_storage"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/tiered_storage/hot"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/tiered_storage/cold"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/temp"}),
            Action(name="CreateFileList", kwargs={"operation_id": "tiering_setup_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/temp_export_001.csv", "destination_path": "/data/tiered_storage/hot/temp_export_001.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/tiered_storage/cold/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "tiering_setup_01", "user_id": "user_001", "message": "Temporary data has been tiered into hot and cold storage."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Temporary data has been tiered into hot and cold storage."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="059",
        instruction=(
            "You are a Data Analyst. To simplify access for the management team, consolidate all reports on `server-analytics.company.com` into a single location. Create a new directory at `/analytics/reports_consolidated/`. Move all files from `/analytics/reports` into this new directory. "
            "Notify the 'File Check' channel with the message 'All analytics reports have been consolidated into a single directory.'. "
            "For task id you should use 'report_consolidation_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "report_consolidation_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/reports_consolidated"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "report_consolidation_01", "filepaths": ["/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/reports_consolidated/daily_sales_report.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/reports_consolidated/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "report_consolidation_01", "user_id": "user_003", "message": "All analytics reports have been consolidated into a single directory."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "All analytics reports have been consolidated into a single directory."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="105",
        instruction=(
            "You are a System Administrator on `server-data-01.company.com`. You need to consolidate all temporary and unsorted files before a scheduled cleanup. Create a single directory at `/data/cleanup_staging/` and move all files from both `/data/temp` and `/data/unsorted` into it. "
            "Announce this in the 'System Alerts' channel with the message 'All temporary and unsorted data has been consolidated for cleanup.'. "
            "For task id you should use 'cleanup_consolidation_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "cleanup_consolidation_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/cleanup_staging"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/"}),
            Action(name="CreateFileList", kwargs={"operation_id": "cleanup_consolidation_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat", "/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/temp_export_001.csv", "destination_path": "/data/cleanup_staging/temp_export_001.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/cleanup_staging/cache_backup.dat"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/cleanup_staging/sales_data.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/cleanup_staging/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "cleanup_consolidation_01", "user_id": "user_001", "message": "All temporary and unsorted data has been consolidated for cleanup."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "All temporary and unsorted data has been consolidated for cleanup."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="106",
        instruction=(
            "You are a Project Manager on `storage-01.company.com`. After a successful data validation check, you need to move the verified archive to the correct folder. Create a new directory at `/storage/archives/verified/` and move the `analytics_data_archive_20240116_103000.tar.gz` from `/storage/archives` into it. "
            "Notify the 'Operations' channel with the message 'Analytics data archive has passed validation and been moved to the verified directory.'. "
            "For task id you should use 'archive_verification_01' and for user_id 'user_005'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "archive_verification_01", "user_id": "user_005", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "storage-01.company.com", "new_directory_path": "/storage/archives/verified"}),
            Action(name="FindFiles", kwargs={"server_hostname": "storage-01.company.com", "search_path": "/storage/archives"}),
            Action(name="CreateFileList", kwargs={"operation_id": "archive_verification_01", "filepaths": ["/storage/archives/analytics_data_archive_20240116_103000.tar.gz"]}),
            Action(name="MoveFile", kwargs={"source_path": "/storage/archives/analytics_data_archive_20240116_103000.tar.gz", "destination_path": "/storage/archives/verified/analytics_data_archive_20240116_103000.tar.gz"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "archive_verification_01", "user_id": "user_005", "message": "Analytics data archive has passed validation and been moved to the verified directory."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Analytics data archive has passed validation and been moved to the verified directory."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="107",
        instruction=(
            "You are a Developer preparing for the weekly error log review. On `server-prod-01.company.com`, create a new directory for this week's meeting at `/var/log/weekly_review/`. Move the `error.log` from `/var/log/applications` into this new directory to prepare it for discussion. "
            "Announce this in the 'Operations' channel with the message 'Error log has been staged for the weekly review meeting.'. "
            "For task id you should use 'error_review_prep_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "error_review_prep_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/weekly_review"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "error_review_prep_01", "filepaths": ["/var/log/applications/error.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/error.log", "destination_path": "/var/log/weekly_review/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "error_review_prep_01", "user_id": "user_002", "message": "Error log has been staged for the weekly review meeting."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Error log has been staged for the weekly review meeting."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="108",
        instruction=(
            "You are a Security Administrator. For a security audit on `server-prod-01.company.com`, you must securely isolate the `error.log`. Create a new directory `/var/log/secure_audit/` and move the `error.log` from `/var/log/applications` into it. It is critical that the moved file is an exact copy, so you must verify its checksum after the move. "
            "Announce the result in the 'System Alerts' channel with the message 'Production error log has been securely isolated and verified for audit.'. "
            "For task id you should use 'sec_audit_log_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "sec_audit_log_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/secure_audit"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "sec_audit_log_01", "filepaths": ["/var/log/applications/error.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/error.log", "destination_path": "/var/log/secure_audit/error.log"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_009", "filepath": "server-prod-01.company.com:/var/log/secure_audit/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "sec_audit_log_01", "user_id": "user_001", "message": "Production error log has been securely isolated and verified for audit."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Production error log has been securely isolated and verified for audit."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="109",
        instruction=(
            "You are a Data Analyst on `server-analytics.company.com`. The Q1 sales report is now final. Create a `/analytics/reports/final_q1/` directory and move the `daily_sales_report.csv` into it. You must verify the file's checksum after moving it to ensure the final version is intact. "
            "Notify the 'File Check' channel with the message 'Q1 sales report has been finalized and its integrity verified.'. "
            "For task id you should use 'finalize_report_q1' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "finalize_report_q1", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/reports/final_q1"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "finalize_report_q1", "filepaths": ["/analytics/reports/daily_sales_report.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/reports/final_q1/daily_sales_report.csv"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_009", "filepath": "server-analytics.company.com:/analytics/reports/final_q1/daily_sales_report.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "finalize_report_q1", "user_id": "user_003", "message": "Q1 sales report has been finalized and its integrity verified."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Q1 sales report has been finalized and its integrity verified."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="110",
        instruction=(
            "You are a Data Engineer on `server-data-01.company.com`. A new data pipeline requires all source files to be in a specific input directory. Create a new directory at `/data/pipeline_input/`. Move all files from `/data/unsorted` into this new location. Verify the checksum of each file after it is moved to guarantee a clean start for the pipeline. "
            "Announce this in the 'Operations' channel with the message 'All unsorted data has been relocated and verified for the new pipeline.'. "
            "For task id you should use 'pipeline_setup_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "pipeline_setup_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/pipeline_input"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "pipeline_setup_01", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/pipeline_input/sales_data.csv"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_009", "filepath": "server-data-01.company.com:/data/pipeline_input/sales_data.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/pipeline_input/customer_info.csv"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_010", "filepath": "server-data-01.company.com:/data/pipeline_input/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "pipeline_setup_01", "user_id": "user_002", "message": "All unsorted data has been relocated and verified for the new pipeline."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "All unsorted data has been relocated and verified for the new pipeline."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="111",
        instruction=(
            "You are a Data Engineer on `server-analytics.company.com`. The raw user data is ready for the next step. Create a new directory `/analytics/raw_data/ingestion_queue/` and move the `user_events_2023.csv` file into it. Crucially, you must verify the file's checksum after moving it to ensure its integrity before ingestion. "
            "Notify the 'Operations' channel with the message 'Raw user data is verified and queued for ingestion.'. "
            "For task id you should use 'ingest_queue_02' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "ingest_queue_02", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/raw_data/ingestion_queue"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/raw_data"}),
            Action(name="CreateFileList", kwargs={"operation_id": "ingest_queue_02", "filepaths": ["/analytics/raw_data/user_events_2023.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/raw_data/user_events_2023.csv", "destination_path": "/analytics/raw_data/ingestion_queue/user_events_2023.csv"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_009", "filepath": "server-analytics.company.com:/analytics/raw_data/ingestion_queue/user_events_2023.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "ingest_queue_02", "user_id": "user_002", "message": "Raw user data is verified and queued for ingestion."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Raw user data is verified and queued for ingestion."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="112",
        instruction=(
            "You are a System Administrator on `server-prod-01.company.com`. Reorganize the application logs for better clarity. Create a new directory at `/var/log/app_logs/` and move all files from `/var/log/applications` into it. Verify the checksum of each log file after moving to ensure no data was lost or corrupted during the move. "
            "Announce the successful reorganization in the 'System Alerts' channel with the message 'Application logs have been successfully reorganized and verified.'. "
            "For task id you should use 'log_reorg_02' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "log_reorg_02", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/app_logs"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "log_reorg_02", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/webapp.log", "destination_path": "/var/log/app_logs/webapp.log"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_009", "filepath": "server-prod-01.company.com:/var/log/app_logs/webapp.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/api_requests.log", "destination_path": "/var/log/app_logs/api_requests.log"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_010", "filepath": "server-prod-01.company.com:/var/log/app_logs/api_requests.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/error.log", "destination_path": "/var/log/app_logs/error.log"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_011", "filepath": "server-prod-01.company.com:/var/log/app_logs/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "log_reorg_02", "user_id": "user_001", "message": "Application logs have been successfully reorganized and verified."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Application logs have been successfully reorganized and verified."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="113",
        instruction=(
            "You are a System Administrator on `server-data-01.company.com`. You need to isolate all temporary files for a data integrity review. Create a new directory `/data/review/` and move all files from `/data/temp` into it. You must verify the checksum of each file after moving to ensure data integrity has been maintained. "
            "Announce the completion in the 'System Alerts' channel with the message 'Temporary data has been moved to a review directory and verified.'. "
            "For task id you should use 'review_temp_data_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "review_temp_data_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/review"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/temp"}),
            Action(name="CreateFileList", kwargs={"operation_id": "review_temp_data_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/temp_export_001.csv", "destination_path": "/data/review/temp_export_001.csv"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_009", "filepath": "server-data-01.company.com:/data/review/temp_export_001.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/review/cache_backup.dat"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_010", "filepath": "server-data-01.company.com:/data/review/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "review_temp_data_01", "user_id": "user_001", "message": "Temporary data has been moved to a review directory and verified."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Temporary data has been moved to a review directory and verified."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="114",
        instruction=(
            "You are a Data Analyst on `server-analytics.company.com`. You need to create a verified snapshot of the current reports. Create a new directory `/analytics/reports/snapshot_20240115/` and move all files from the parent `/analytics/reports` directory into it. Verify the checksum of each report after moving. "
            "Announce the successful snapshot in the 'File Check' channel with the message 'Analytics reports for 2024-01-15 have been snapshotted and verified.'. "
            "For task id you should use 'report_snapshot_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "report_snapshot_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/reports/snapshot_20240115"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "report_snapshot_01", "filepaths": ["/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/reports/snapshot_20240115/daily_sales_report.csv"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_009", "filepath": "server-analytics.company.com:/analytics/reports/snapshot_20240115/daily_sales_report.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/reports/snapshot_20240115/monthly_trends.csv"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_010", "filepath": "server-analytics.company.com:/analytics/reports/snapshot_20240115/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "report_snapshot_01", "user_id": "user_003", "message": "Analytics reports for 2024-01-15 have been snapshotted and verified."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Analytics reports for 2024-01-15 have been snapshotted and verified."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="115",
        instruction=(
            "You are a System Administrator on `server-data-01.company.com`. The data in `/data/unsorted` is now considered legacy and must be moved. Create a new directory `/data/legacy_data/` and move all files from `/data/unsorted` into it. After moving, verify the checksum of each file to ensure its integrity is maintained for archival purposes. "
            "Notify the 'Operations' channel with the message 'Unsorted data has been moved to a legacy directory and its integrity confirmed.'. "
            "For task id you should use 'legacy_data_move_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "legacy_data_move_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/legacy_data"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "legacy_data_move_01", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/legacy_data/sales_data.csv"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_009", "filepath": "server-data-01.company.com:/data/legacy_data/sales_data.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/legacy_data/customer_info.csv"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_010", "filepath": "server-data-01.company.com:/data/legacy_data/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "legacy_data_move_01", "user_id": "user_001", "message": "Unsorted data has been moved to a legacy directory and its integrity confirmed."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Unsorted data has been moved to a legacy directory and its integrity confirmed."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="116",
        instruction=(
            "You are a Security Administrator on `server-prod-01.company.com`. As part of an investigation, you must isolate API and error logs. Create a new directory `/var/log/security_review/` and move both `api_requests.log` and `error.log` from `/var/log/applications` into it. Verify the checksum of both files after the move to ensure the evidence is untampered. "
            "Notify the 'System Alerts' channel with the message 'API and error logs have been isolated and verified for security review.'. "
            "For task id you should use 'sec_review_02' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "sec_review_02", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/security_review"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "sec_review_02", "filepaths": ["/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/api_requests.log", "destination_path": "/var/log/security_review/api_requests.log"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_009", "filepath": "server-prod-01.company.com:/var/log/security_review/api_requests.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/error.log", "destination_path": "/var/log/security_review/error.log"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_010", "filepath": "server-prod-01.company.com:/var/log/security_review/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "sec_review_02", "user_id": "user_001", "message": "API and error logs have been isolated and verified for security review."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "API and error logs have been isolated and verified for security review."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="117",
        instruction=(
            "You are a Data Engineer on `server-analytics.company.com`. The raw user event data is ready for ingestion. Create a new directory `/analytics/ingestion_ready/` and move `user_events_2023.csv` from `/analytics/raw_data` into it. Verify the file's checksum after moving to ensure it is not corrupt before processing. "
            "Announce this in the 'Operations' channel with the message 'Raw user data has been verified and staged for ingestion.'. "
            "For task id you should use 'ingest_stage_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "ingest_stage_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/ingestion_ready"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/raw_data"}),
            Action(name="CreateFileList", kwargs={"operation_id": "ingest_stage_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/raw_data/user_events_2023.csv", "destination_path": "/analytics/ingestion_ready/user_events_2023.csv"}),
            Action(name="VerifyChecksum", kwargs={"file_id": "file_009", "filepath": "server-analytics.company.com:/analytics/ingestion_ready/user_events_2023.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "ingest_stage_01", "user_id": "user_002", "message": "Raw user data has been verified and staged for ingestion."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Raw user data has been verified and staged for ingestion."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="010",
        instruction=(
            "You are a DevOps Engineer. "
            "The `/data/temp` directory on `server-data-01.company.com` is consuming excessive space with old cache and export files. Archive all files within this directory to `backup-server.company.com:/backups/temp_data/` under the name `temp_data_cleanup_2023`. Once the transfer is complete and the archive is secure, remove the original files to reclaim storage. "
            "You should log completion message and notify the 'Operations' channel upon successful cleanup with message 'Cleanup of /data/temp on server-data-01.company.com is complete.'."
            "For task id you should use 'cleanup_001' and for user_id 'user_002'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "cleanup_001", "user_id": "user_002", "task_type": "cleanup"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/temp"}),
            Action(name="CreateFileList", kwargs={"operation_id": "cleanup_001", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_002", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "temp_data_cleanup_2023", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-data-01.company.com:/tmp/temp_data_cleanup_2023.tar.gz", "destination_path": "backup-server.company.com:/backups/temp_data/temp_data_cleanup_2023.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/temp/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "cleanup_001", "user_id": "user_002", "message": "Cleanup of /data/temp on server-data-01.company.com is complete."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Cleanup of /data/temp on server-data-01.company.com is complete."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="011",
        instruction=(
            "You are a Data Analyst, you must perform a routine data lifecycle action. "
            "The raw data file `user_events_2023.csv` from last year, "
            "located in `/analytics/raw_data` on `server-analytics.company.com`, needs to be archived for long-term storage using '/tmp' destination directory. "
            "The archive, named `raw_analytics_archive_2023`, should be moved to the primary storage server at `storage-01.company.com:/storage/archives/`. After confirming the transfer, please clean up the original file from the analytics server and report the successful archival to the 'File Check' channel with message 'Archival is complete.'"
            "For task id you should use 'arch_analytics_01' and for user_id 'user_003'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "arch_analytics_01", "user_id": "user_003", "task_type": "archival"}),
            Action(name="CreateFileList", kwargs={"operation_id": "arch_analytics_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_003", "destination_directory": "/tmp", "remote_address": "storage-01.company.com", "archive_name": "raw_analytics_archive_2023", "filepaths": ["/analytics/raw_data/user_events_2023.csv"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-analytics.company.com:/tmp/raw_analytics_archive_2023.tar.gz", "destination_path": "storage-01.company.com:/storage/archives/raw_analytics_archive_2023.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/analytics/raw_data/user_events_2023.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "arch_analytics_01", "user_id": "user_003", "message": "Archival is complete."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Archival is complete."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="013",
        instruction=(
            "You are a DevOps Engineer, it's time to clean up the `/data/unsorted` directory on `server-data-01.company.com`. All CSV files in this location have been processed and now need to be archived. Please create an archive named `unsorted_data_cleanup` containing all files from that directory, move it to `storage-01.company.com:/storage/cleanup/`, and then empty the source directory. "
            "Log the completion and notify the 'Operations' channel with message 'Unsorted data directory has been archived and cleared.'."
            "For task id you should use 'cleanup_002' and for user_id 'user_002'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "cleanup_002", "user_id": "user_002", "task_type": "cleanup"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "cleanup_002", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_002", "destination_directory": "/tmp", "remote_address": "storage-01.company.com", "archive_name": "unsorted_data_cleanup", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-data-01.company.com:/tmp/unsorted_data_cleanup.tar.gz", "destination_path": "storage-01.company.com:/storage/cleanup/unsorted_data_cleanup.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/unsorted/sales_data.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/unsorted/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "cleanup_002", "user_id": "user_002", "message": "Unsorted data directory has been archived and cleared."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Unsorted data directory has been archived and cleared."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="014",
        instruction=(
            "You are a Data Engineer. The files in the `/data/unsorted` directory on `server-data-01.company.com` have been processed and are now ready for archival. To maintain a clean data pipeline, please archive the entire contents of this directory into a single package named `processed_unsorted_data` and move it to the central storage server at `storage-01.company.com:/storage/processed/`. "
            "Once the archive is secure, clear the original directory and notify the 'Operations' channel with message 'Cleanup is complete.'."
            "For task id you should use 'arch_unsorted_01' and for user_id 'user_002'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "arch_unsorted_01", "user_id": "user_002", "task_type": "archival"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "arch_unsorted_01", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_002", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "processed_unsorted_data", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-data-01.company.com:/tmp/processed_unsorted_data.tar.gz", "destination_path": "storage-01.company.com:/storage/processed/processed_unsorted_data.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/unsorted/sales_data.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/unsorted/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "arch_unsorted_01", "user_id": "user_002", "message": "Cleanup is complete."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Cleanup is complete."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="015",
        instruction=(
            "You are a the Data Analyst, you are responsible for end-of-month processing. The contents of the `/analytics/reports` directory on `server-analytics.company.com` now need to be archived. Please create a compressed archive named `analytics_reports_eom` and transfer it to the main backup server at `backup-server.company.com:/backups/reports/`. After the transfer, the original report files should be removed. Please confirm when the task is complete in the 'File Check' channel with message 'EOM archival is complete.'."
            "For task id you should use 'arch_reports_01' and for user_id 'user_003'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "arch_reports_01", "user_id": "user_003", "task_type": "archival"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "arch_reports_01", "filepaths": ["/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_003", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "analytics_reports_eom", "filepaths": ["/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-analytics.company.com:/tmp/analytics_reports_eom.tar.gz", "destination_path": "backup-server.company.com:/backups/reports/analytics_reports_eom.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/analytics/reports/daily_sales_report.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/analytics/reports/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "arch_reports_01", "user_id": "user_003", "message": "EOM archival is complete."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "EOM archival is complete."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="016",
        instruction=(
            "You are a System Administrator performing maintenance. "
            "The `/data/temp` directory on `server-data-01.company.com` contains old files that need to be cleared. "
            "Archive the entire contents of this directory into a file named `temp_data_archive` and move it to `storage-01.company.com:/storage/temp_archives/`. Once the data is securely transferred, delete the original files to free up disk space and report the completion of the maintenance task to the 'System Alerts' channel with message 'Maintenance task complete'."
            "For task id you should use 'arch_temp_01' and for user_id 'user_001'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "arch_temp_01", "user_id": "user_001", "task_type": "maintenance"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/temp"}),
            Action(name="CreateFileList", kwargs={"operation_id": "arch_temp_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_001", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "temp_data_archive", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-data-01.company.com:/tmp/temp_data_archive.tar.gz", "destination_path": "storage-01.company.com:/storage/temp_archives/temp_data_archive.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/temp/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "arch_temp_01", "user_id": "user_001", "message": "Maintenance task complete"}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Maintenance task complete"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="018",
        instruction=(
            "You are a Data Analyst. To close out the 2023 user analysis project, all related data on `server-analytics.company.com` needs to be consolidated and archived. Please create an archive named `user_analysis_2023_complete` containing the raw data at `/analytics/raw_data/user_events_2023.csv` and the final report at `/analytics/reports/monthly_trends.csv`. Move this archive to `storage-01.company.com:/storage/analytics_archives/`. Once done, "
            "remove the original files from the analytics server and confirm completion in the 'File Check' channel with message 'data has been successfully archived and cleared from the active server'."
            "For task id you should use 'arch_analytics_02' and for user_id 'user_003'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "arch_analytics_02", "user_id": "user_003", "task_type": "archival"}),
            Action(name="CreateFileList", kwargs={"operation_id": "arch_analytics_02", "filepaths": ["/analytics/raw_data/user_events_2023.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_003", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "user_analysis_2023_complete", "filepaths": ["/analytics/raw_data/user_events_2023.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-analytics.company.com:/tmp/user_analysis_2023_complete.tar.gz", "destination_path": "storage-01.company.com:/storage/analytics_archives/user_analysis_2023_complete.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/analytics/raw_data/user_events_2023.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/analytics/reports/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "arch_analytics_02", "user_id": "user_003", "message": "data has been successfully archived and cleared from the active server"}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "data has been successfully archived and cleared from the active server"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="019",
        instruction=(
            "You are a Security Administrator. A critical error has been resolved, and the corresponding log file must be archived for a post-mortem investigation. Securely archive the `error.log` from `/var/log/applications` on `server-prod-01.company.com`. The archive, named `critical_log_20240113`, should be transferred to the secure document vault at `document-vault.company.com:/secure_logs/`. "
            "After transfer, delete the original log file and notify the 'System Alerts' channel of the successful archival with message 'Critical error log has been securely archived for post-mortem analysis.'."
            "For task id you should use 'sec_archive_01' and for user_id 'user_001'. "

        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "sec_archive_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateFileList", kwargs={"operation_id": "sec_archive_01", "filepaths": ["/var/log/applications/error.log"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_001", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "critical_log_20240113", "filepaths": ["/var/log/applications/error.log"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-prod-01.company.com:/tmp/critical_log_20240113.tar.gz", "destination_path": "document-vault.company.com:/secure_logs/critical_log_20240113.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/var/log/applications/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "sec_archive_01", "user_id": "user_001", "message": "Critical error log has been securely archived for post-mortem analysis."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Critical error log has been securely archived for post-mortem analysis."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="020",
        instruction=(
            "You are a Data Analyst. The 2023 user event analysis project is now complete. To preserve the findings and source data together, please create a consolidated archive named `user_events_2023_final_package`. This archive must contain the raw data from `server-analytics.company.com` at `/analytics/raw_data/user_events_2023.csv` and the final report at `/analytics/reports/daily_sales_report.csv`. The package should be moved to long-term storage at `storage-01.company.com:/storage/final_analytics_packages/`. "
            "Once transferred, clear the original files from the analytics server and notify the 'File Check' channel with reason 'project data has been consolidated and archived'."
            "For task id you should use 'arch_analytics_final_01' and for user_id 'user_003'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "arch_analytics_final_01", "user_id": "user_003", "task_type": "archival"}),
            Action(name="CreateFileList", kwargs={"operation_id": "arch_analytics_final_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv", "/analytics/reports/daily_sales_report.csv"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_003", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "user_events_2023_final_package", "filepaths": ["/analytics/raw_data/user_events_2023.csv", "/analytics/reports/daily_sales_report.csv"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-analytics.company.com:/tmp/user_events_2023_final_package.tar.gz", "destination_path": "storage-01.company.com:/storage/final_analytics_packages/user_events_2023_final_package.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/analytics/raw_data/user_events_2023.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/analytics/reports/daily_sales_report.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "arch_analytics_final_01", "user_id": "user_003", "message": "project data has been consolidated and archived"}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "project data has been consolidated and archived"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="021",
        instruction=(
            "You are a System Administrator responsible for log management. The application logs on `server-prod-01.company.com` in `/var/log/applications` must be rotated for compliance. Please archive all log files from this directory into a single archive named `app_logs_rotation_20240115`. This archive needs to be moved to the dedicated `log-storage.company.com` server at `/archives/prod_logs/`. "
            "After a successful transfer, you should clear the original log files from the production server "
            "and send a confirmation to the 'System Alerts' channel with message 'Log rotation is complete.'."
            "For task id you should use 'log_rotation_01' and for user_id 'user_001'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "log_rotation_01", "user_id": "user_001", "task_type": "log_rotation"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "log_rotation_01", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_001", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "app_logs_rotation_20240115", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-prod-01.company.com:/tmp/app_logs_rotation_20240115.tar.gz", "destination_path": "log-storage.company.com:/archives/prod_logs/app_logs_rotation_20240115.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/var/log/applications/webapp.log"}),
            Action(name="DeleteFile", kwargs={"filepath": "/var/log/applications/api_requests.log"}),
            Action(name="DeleteFile", kwargs={"filepath": "/var/log/applications/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "log_rotation_01", "user_id": "user_001", "message": "Log rotation is complete."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Log rotation is complete."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="022",
        instruction=(
            "You are a Developer. Your recent data processing work on `server-data-01.company.com` is complete, and the staging areas must be cleared. Archive the file `temp_export_001.csv` from `/data/temp` and `sales_data.csv` from `/data/unsorted` into a consolidated archive named `dev_staging_cleanup`. Transfer this archive to your personal backup space at `personal-backup.company.com:/dev_archives/`. "
            "After the transfer, remove the original files and notify the 'Operations' channel that the staging area is clean with reason 'Cleanup of developer staging directories is complete.'."
            "For task id you should use 'dev_cleanup_01' and for user_id 'user_002'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "dev_cleanup_01", "user_id": "user_002", "task_type": "cleanup"}),
            Action(name="CreateFileList", kwargs={"operation_id": "dev_cleanup_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/unsorted/sales_data.csv"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_002", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "dev_staging_cleanup", "filepaths": ["/data/temp/temp_export_001.csv", "/data/unsorted/sales_data.csv"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-data-01.company.com:/tmp/dev_staging_cleanup.tar.gz", "destination_path": "personal-backup.company.com:/dev_archives/dev_staging_cleanup.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/unsorted/sales_data.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "dev_cleanup_01", "user_id": "user_002", "message": "Cleanup of developer staging directories is complete."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Cleanup of developer staging directories is complete."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="023",
        instruction=(
            "You are a Data Analyst preparing for a compliance audit. The `monthly_trends.csv` report located at `/analytics/reports/` on `server-analytics.company.com` must be preserved in its current state. Please create an archive of this single file named `monthly_trends_audit_copy` and transfer it to the central storage server at `storage-01.company.com:/storage/audit_copies/`. Once the transfer is complete, "
            "remove the original file from the active reports directory and confirm the task's completion in the 'File Check' channel with message 'Audit copy has been securely archived.'."
            "For task id you should use 'audit_archive_01' and for user_id 'user_003'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "audit_archive_01", "user_id": "user_003", "task_type": "archival"}),
            Action(name="CreateFileList", kwargs={"operation_id": "audit_archive_01", "filepaths": ["/analytics/reports/monthly_trends.csv"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_003", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "monthly_trends_audit_copy", "filepaths": ["/analytics/reports/monthly_trends.csv"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-analytics.company.com:/tmp/monthly_trends_audit_copy.tar.gz", "destination_path": "storage-01.company.com:/storage/audit_copies/monthly_trends_audit_copy.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/analytics/reports/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "audit_archive_01", "user_id": "user_003", "message": "Audit copy has been securely archived."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Audit copy has been securely archived."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="024",
        instruction=(
            "You are a System Administrator, you must back up the contents of the `/data/temp` directory on `server-data-01.company.com` before a planned system update. Create a full archive of this directory named `data_temp_pre_update_backup`. The archive needs to be stored on the primary backup server at `backup-server.company.com:/backups/pre_update_snapshots/`. After the backup is securely transferred, please clear the original files from the temp directory and "
            "notify the 'System Alerts' channel with message 'Server is backed up and ready.'."
            "For task id you should use 'pre_update_backup_01' and for user_id 'user_001'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "pre_update_backup_01", "user_id": "user_001", "task_type": "backup"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/temp"}),
            Action(name="CreateFileList", kwargs={"operation_id": "pre_update_backup_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_001", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "data_temp_pre_update_backup", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-data-01.company.com:/tmp/data_temp_pre_update_backup.tar.gz", "destination_path": "backup-server.company.com:/backups/pre_update_snapshots/data_temp_pre_update_backup.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/temp/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "pre_update_backup_01", "user_id": "user_001", "message": "Server is backed up and ready."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Server is backed up and ready."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="025",
        instruction=(
            "You are a Project Manager, you require a complete snapshot of the application logs from `server-prod-01.company.com` for performance analysis. Please archive the entire contents of the `/var/log/applications` directory into an archive named `prod_logs_performance_review`. This consolidated log file should be transferred to the central storage server at `storage-01.company.com:/storage/log_reviews/`. After the transfer is complete, "
            "delete the original files to free up disk space and post a completion notice in the 'Operations' channel with message 'The log files are archived.'."
            "For task id you should use 'log_review_01' and for user_id 'user_005'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "log_review_01", "user_id": "user_005", "task_type": "archival"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "log_review_01", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_005", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "prod_logs_performance_review", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-prod-01.company.com:/tmp/prod_logs_performance_review.tar.gz", "destination_path": "storage-01.company.com:/storage/log_reviews/prod_logs_performance_review.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/var/log/applications/webapp.log"}),
            Action(name="DeleteFile", kwargs={"filepath": "/var/log/applications/api_requests.log"}),
            Action(name="DeleteFile", kwargs={"filepath": "/var/log/applications/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "log_review_01", "user_id": "user_005", "message": "The log files are archived."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "The log files are archived."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="027",
        instruction=(
            "You are a Developer, you need to clean up your staging directories on `server-data-01.company.com` now that your feature is in production. Archive the test dataset `customer_info.csv` from `/data/unsorted` and the temporary export file `temp_export_001.csv` from `/data/temp`. The combined archive should be named `feature_x_dev_assets` and stored on the main backup server at `backup-server.company.com:/backups/dev_staging/`. "
            "Once the transfer is complete, remove the original files and notify the 'Operations' channel with reason 'Staging cleaned up by the dev team.'."
            "For task id you should use 'dev_cleanup_02' and for user_id 'user_002'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "dev_cleanup_02", "user_id": "user_002", "task_type": "cleanup"}),
            Action(name="CreateFileList", kwargs={"operation_id": "dev_cleanup_02", "filepaths": ["/data/unsorted/customer_info.csv", "/data/temp/temp_export_001.csv"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_002", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "feature_x_dev_assets", "filepaths": ["/data/unsorted/customer_info.csv", "/data/temp/temp_export_001.csv"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-data-01.company.com:/tmp/feature_x_dev_assets.tar.gz", "destination_path": "backup-server.company.com:/backups/dev_staging/feature_x_dev_assets.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/unsorted/customer_info.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "dev_cleanup_02", "user_id": "user_002", "message": "Staging cleaned up by the dev team."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Staging cleaned up by the dev team."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="028",
        instruction=(
            "You are a System Administrator responding to a production incident. The `webapp.log` and `error.log` files from `/var/log/applications` on `server-prod-01.company.com` are critical for the incident post-mortem. You must securely archive these two logs into a package named `incident_20240115_logs` and transfer it to the dedicated log storage server at `log-storage.company.com:/secure/incident_review/`. "
            "After a successful transfer, remove the originals to prevent log tampering and notify 'System Alerts' with reason 'Production logs for incident have been securely archived.'."
            "For task id you should use 'incident_archive_01' and for user_id 'user_001'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "incident_archive_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "incident_archive_01", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/error.log"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_001", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "incident_20240115_logs", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/error.log"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-prod-01.company.com:/tmp/incident_20240115_logs.tar.gz", "destination_path": "log-storage.company.com:/secure/incident_review/incident_20240115_logs.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/var/log/applications/webapp.log"}),
            Action(name="DeleteFile", kwargs={"filepath": "/var/log/applications/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "incident_archive_01", "user_id": "user_001", "message": "Production logs for incident have been securely archived."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Production logs for incident have been securely archived."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="029",
        instruction=(
            "You are a System Administrator preparing for a database migration. To ensure no data is lost, you must create a complete snapshot of all data on `server-data-01.company.com`. Please archive all files from both the `/data/temp` and `/data/unsorted` directories into a single archive named `data_server_snapshot_pre_migration`. This archive must be stored on the main storage server at `storage-01.company.com:/storage/full_data_snapshots/`. "
            "After the transfer, clear the original directories and notify the 'Operations' channel that the server is ready for migration with message 'Server has been fully backed up and is ready for the planned migration.'."
            "For task id you should use 'data_snapshot_01' and for user_id 'user_001'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "data_snapshot_01", "user_id": "user_001", "task_type": "backup"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/temp"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "data_snapshot_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat", "/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_001", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "data_server_snapshot_pre_migration", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat", "/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-data-01.company.com:/tmp/data_server_snapshot_pre_migration.tar.gz", "destination_path": "storage-01.company.com:/storage/full_data_snapshots/data_server_snapshot_pre_migration.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/temp/temp_export_001.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/temp/cache_backup.dat"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/unsorted/sales_data.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/unsorted/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "data_snapshot_01", "user_id": "user_001", "message": "Server has been fully backed up and is ready for the planned migration."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Server has been fully backed up and is ready for the planned migration."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="030",
        instruction=(
            "You are a Data Analyst, you are preparing the dataset for the annual business review. Consolidate all CSV files, including raw data and reports, from the `server-analytics.company.com` server. This includes files in both `/analytics/raw_data` and `/analytics/reports`. The consolidated archive should be named `annual_review_dataset_2023` and placed on the central storage server at `storage-01.company.com:/storage/yearly_reports/`. "
            "Once the dataset is created, remove the source files to avoid using outdated data and notify the 'File Check' channel with reason 'The analytics dataset for the annual review is prepared and archived.'."
            "For task id you should use 'annual_review_01' and for user_id 'user_003'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "annual_review_01", "user_id": "user_003", "task_type": "archival"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/raw_data"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "annual_review_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv", "/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_003", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "annual_review_dataset_2023", "filepaths": ["/analytics/raw_data/user_events_2023.csv", "/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-analytics.company.com:/tmp/annual_review_dataset_2023.tar.gz", "destination_path": "storage-01.company.com:/storage/yearly_reports/annual_review_dataset_2023.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/analytics/raw_data/user_events_2023.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/analytics/reports/daily_sales_report.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/analytics/reports/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "annual_review_01", "user_id": "user_003", "message": "The analytics dataset for the annual review is prepared and archived."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "The analytics dataset for the annual review is prepared and archived."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="031",
        instruction=(
            "You are a Developer who has just completed a data import process. The raw source files in the `/data/unsorted` directory on `server-data-01.company.com` are no longer needed for active processing. Please archive these files under the name `import_source_files_20240115` and move them to the backup server at `backup-server.company.com:/backups/processed_imports/`. "
            "Once archived, clean up the original files and confirm the staging area is clear in the 'Operations' channel with message 'Post-import cleanup is complete.'."
            "For task id you should use 'import_cleanup_01' and for user_id 'user_002'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "import_cleanup_01", "user_id": "user_002", "task_type": "cleanup"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "import_cleanup_01", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_002", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "import_source_files_20240115", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-data-01.company.com:/tmp/import_source_files_20240115.tar.gz", "destination_path": "backup-server.company.com:/backups/processed_imports/import_source_files_20240115.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/unsorted/sales_data.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/data/unsorted/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "import_cleanup_01", "user_id": "user_002", "message": "Post-import cleanup is complete."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Post-import cleanup is complete."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="032",
        instruction=(
            "You are a Data Analyst preparing for a quarterly business review. You need to create a complete snapshot of all CSV data from `server-analytics.company.com`. This includes the raw data from `/analytics/raw_data` and all reports from `/analytics/reports`. Please create a consolidated archive named `analytics_csv_snapshot_q1` and move it to the central storage server at `storage-01.company.com:/storage/quarterly_snapshots/`. "
            "After the transfer, clear the original files and notify the 'File Check' channel with reason 'Quarterly snapshot of all CSVs is complete.'."
            "For task id you should use 'analytics_snapshot_01' and for user_id 'user_003'. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "analytics_snapshot_01", "user_id": "user_003", "task_type": "archival"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/raw_data"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "analytics_snapshot_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv", "/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="CreateArchive", kwargs={"user_id": "user_003", "destination_directory": "/tmp", "remote_address": "backup-server.company.com", "archive_name": "analytics_csv_snapshot_q1", "filepaths": ["/analytics/raw_data/user_events_2023.csv", "/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="TransferFile", kwargs={"source_path": "server-analytics.company.com:/tmp/analytics_csv_snapshot_q1.tar.gz", "destination_path": "storage-01.company.com:/storage/quarterly_snapshots/analytics_csv_snapshot_q1.tar.gz"}),
            Action(name="DeleteFile", kwargs={"filepath": "/analytics/raw_data/user_events_2023.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/analytics/reports/daily_sales_report.csv"}),
            Action(name="DeleteFile", kwargs={"filepath": "/analytics/reports/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "analytics_snapshot_01", "user_id": "user_003", "message": "Quarterly snapshot of all CSVs is complete."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Quarterly snapshot of all CSVs is complete."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="035",
        instruction=(
            "You are a System Administrator. To improve log analysis on `server-prod-01.company.com`, the application logs found in '/var/log/applications' need to be reorganized by type. Please create a new directory structure under `/var/log/sorted/` with two subdirectories: `general` and `errors`. Move the `webapp.log` and `api_requests.log` into the `general` directory, and place `error.log` into the `errors` directory. "
            "Notify 'System Alerts' when the log reorganization is complete with message 'Production logs have been reorganized by type.'."
            "For task id you should use 'log_org_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "log_org_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/sorted"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/sorted/general"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/sorted/errors"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "log_org_01", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/webapp.log", "destination_path": "/var/log/sorted/general/webapp.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/api_requests.log", "destination_path": "/var/log/sorted/general/api_requests.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/error.log", "destination_path": "/var/log/sorted/errors/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "log_org_01", "user_id": "user_001", "message": "Production logs have been reorganized by type."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Production logs have been reorganized by type."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="036",
        instruction=(
            "You are a Data Analyst setting up a new project workspace on `server-analytics.company.com`. To keep the project self-contained, create a main directory at `/analytics/projects/2023_review/`. Within it, create `source_data` and `project_reports` subdirectories. Move the raw data file `/analytics/raw_data/user_events_2023.csv` to the `source_data` folder and the `/analytics/reports/monthly_trends.csv` to the `project_reports` folder. "
            "Announce in the 'File Check' channel once the workspace is ready with message 'Workspace for the 2023 analytics review project is now ready.'."
            "For task id you should use 'proj_setup_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "proj_setup_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/projects/2023_review"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/projects/2023_review/source_data"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/projects/2023_review/project_reports"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics"}),
            Action(name="CreateFileList", kwargs={"operation_id": "proj_setup_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/raw_data/user_events_2023.csv", "destination_path": "/analytics/projects/2023_review/source_data/user_events_2023.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/projects/2023_review/project_reports/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "proj_setup_01", "user_id": "user_003", "message": "Workspace for the 2023 analytics review project is now ready."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Workspace for the 2023 analytics review project is now ready."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="037",
        instruction=(
            "You are a Data Engineer on `server-data-01.company.com`, you're implementing a new data-tiering policy for temporary files. Create a structure under `/data/tiered/` with `hot` and `cold` subdirectories. Move the newer file, `temp_export_001.csv` from `/data/temp`, into the `hot` directory. Move the older cache file, `cache_backup.dat`, into the `cold` directory. "
            "Announce the completion of this new organization in the 'Operations' channel with message 'Data tiering policy has been applied.'."
            "For task id you should use 'tiering_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "tiering_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/tiered"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/tiered/hot"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/tiered/cold"}),
            Action(name="CreateFileList", kwargs={"operation_id": "tiering_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/temp_export_001.csv", "destination_path": "/data/tiered/hot/temp_export_001.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/tiered/cold/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "tiering_01", "user_id": "user_002", "message": "Data tiering policy has been applied."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Data tiering policy has been applied."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="038",
        instruction=(
            "You are a System Administrator. To improve log analysis on `server-prod-01.company.com`, the application logs found in '/var/log/applications' need to be reorganized. Create a new structure under `/var/log/sorted/` with `general` and `errors` subdirectories. Move `webapp.log` and `api_requests.log` to `general`, and `error.log` to `errors`. "
            "Announce the completion in the 'System Alerts' channel with the message 'Production logs reorganized by type.'. "
            "For task id you should use 'log_org_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "log_org_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/sorted"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/sorted/general"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/sorted/errors"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "log_org_01", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/webapp.log", "destination_path": "/var/log/sorted/general/webapp.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/api_requests.log", "destination_path": "/var/log/sorted/general/api_requests.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/error.log", "destination_path": "/var/log/sorted/errors/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "log_org_01", "user_id": "user_001", "message": "Production logs reorganized by type."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Production logs reorganized by type."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="039",
        instruction=(
            "You are a Data Engineer preparing for a new ETL process on `server-data-01.company.com`. Create a new workspace at `/data/staging/`. Inside, make two subdirectories: `raw` and `processed`. Move the source files `sales_data.csv` and `customer_info.csv` from `/data/unsorted` into the new `raw` directory. "
            "Report the status to the 'Operations' channel with the message 'New ETL staging area is ready for use.'. "
            "For task id you should use 'etl_setup_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "etl_setup_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/staging"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/staging/raw"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/staging/processed"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "etl_setup_01", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/staging/raw/sales_data.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/staging/raw/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "etl_setup_01", "user_id": "user_002", "message": "New ETL staging area is ready for use."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "New ETL staging area is ready for use."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="040",
        instruction=(
            "You are a Data Analyst preparing for a presentation. On `server-analytics.company.com`, create a directory at `/analytics/presentations/q1_review/`. Move the `daily_sales_report.csv` and `monthly_trends.csv` from the `/analytics/reports` directory into this new location to consolidate your materials. "
            "Send a notification to the 'File Check' channel with the message 'Q1 presentation materials are now consolidated.'. "
            "For task id you should use 'preso_prep_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "preso_prep_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/presentations"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/presentations/q1_review"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "preso_prep_01", "filepaths": ["/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/presentations/q1_review/daily_sales_report.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/presentations/q1_review/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "preso_prep_01", "user_id": "user_003", "message": "Q1 presentation materials are now consolidated."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Q1 presentation materials are now consolidated."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="041",
        instruction=(
            "You are a System Administrator troubleshooting an issue on `server-data-01.company.com`. To isolate potential problem files, create a quarantine directory at `/data/quarantine/`. Move all files from the `/data/temp` directory into this new location for further inspection. "
            "Send a message to the 'System Alerts' channel with the reason 'Temporary files quarantined for inspection.'. "
            "For task id you should use 'quarantine_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "quarantine_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/quarantine"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/temp"}),
            Action(name="CreateFileList", kwargs={"operation_id": "quarantine_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/temp_export_001.csv", "destination_path": "/data/quarantine/temp_export_001.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/quarantine/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "quarantine_01", "user_id": "user_001", "message": "Temporary files quarantined for inspection."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Temporary files quarantined for inspection."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="042",
        instruction=(
            "You are a Data Analyst. To improve data organization on `server-analytics.company.com`, you need to move year-specific raw data into its own directory. Create a new directory `/analytics/raw_data/2023/`. Move the `user_events_2023.csv` file from '/analytics/raw_data' into this new directory. "
            "Announce the completion in the 'File Check' channel with the message 'Raw analytics data for 2023 has been organized by year.'. "
            "For task id you should use 'data_org_yearly_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "data_org_yearly_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/raw_data/2023"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/raw_data"}),
            Action(name="CreateFileList", kwargs={"operation_id": "data_org_yearly_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/raw_data/user_events_2023.csv", "destination_path": "/analytics/raw_data/2023/user_events_2023.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "data_org_yearly_01", "user_id": "user_003", "message": "Raw analytics data for 2023 has been organized by year."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Raw analytics data for 2023 has been organized by year."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="043",
        instruction=(
            "You are a Data Analyst. Management has requested specific reports for their quarterly review. On `server-analytics.company.com`, create a directory at `/analytics/for_review/`. Move the `daily_sales_report.csv` and `monthly_trends.csv` from the main reports folder ('/analytics/reports') into this new directory to prepare them for the review. "
            "Notify the 'File Check' channel with the message 'Quarterly review reports are staged and ready.'. "
            "For task id you should use 'review_prep_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "review_prep_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/for_review"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "review_prep_01", "filepaths": ["/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/for_review/daily_sales_report.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/for_review/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "review_prep_01", "user_id": "user_003", "message": "Quarterly review reports are staged and ready."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Quarterly review reports are staged and ready."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="044",
        instruction=(
            "You are a Security Administrator responding to a security alert on `server-prod-01.company.com`. You must quarantine all application logs for forensic analysis. Create a directory at `/var/log/quarantine/`. Move all files from `/var/log/applications` into this new directory immediately. "
            "Send a high-priority alert to the 'System Alerts' channel with the message 'Production logs have been quarantined for security analysis.'. "
            "For task id you should use 'sec_quarantine_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "sec_quarantine_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/quarantine"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "sec_quarantine_01", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/webapp.log", "destination_path": "/var/log/quarantine/webapp.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/api_requests.log", "destination_path": "/var/log/quarantine/api_requests.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/error.log", "destination_path": "/var/log/quarantine/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "sec_quarantine_01", "user_id": "user_001", "message": "Production logs have been quarantined for security analysis."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Production logs have been quarantined for security analysis."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="045",
        instruction=(
            "You are a Data Engineer improving the data structure on `server-data-01.company.com`. Create a new parent directory `/data/structured/` with two subdirectories: `customers` and `sales`. Move `customer_info.csv` from `/data/unsorted` to the `customers` directory, and move `sales_data.csv` to the `sales` directory. "
            "Announce the new structure in the 'Operations' channel with the message 'Unsorted data has been structured by type.'. "
            "For task id you should use 'data_struct_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "data_struct_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/structured"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/structured/customers"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/structured/sales"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "data_struct_01", "filepaths": ["/data/unsorted/customer_info.csv", "/data/unsorted/sales_data.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/structured/customers/customer_info.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/structured/sales/sales_data.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "data_struct_01", "user_id": "user_002", "message": "Unsorted data has been structured by type."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Unsorted data has been structured by type."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="046",
        instruction=(
            "You are a Data Analyst. To perform a focused analysis without affecting the main reporting area on `server-analytics.company.com`, create a new workspace at `/analytics/deep_dive/`. Move the `daily_sales_report.csv` from `/analytics/reports` into this new directory to begin your work. "
            "Notify the 'File Check' channel with the message 'Workspace for deep dive on sales data is ready.'. "
            "For task id you should use 'deep_dive_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "deep_dive_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/deep_dive"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "deep_dive_01", "filepaths": ["/analytics/reports/daily_sales_report.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/deep_dive/daily_sales_report.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "deep_dive_01", "user_id": "user_003", "message": "Workspace for deep dive on sales data is ready."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Workspace for deep dive on sales data is ready."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="047",
        instruction=(
            "You are a System Administrator performing a cleanup on `server-data-01.company.com`. To better manage temporary files, create a new consolidated directory at `/data/temp_consolidated/`. Move all files from the `/data/temp` directory into this new location. "
            "Send a notification to 'System Alerts' with the message 'Temporary files have been consolidated for review.'. "
            "For task id you should use 'temp_consolidation_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "temp_consolidation_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/temp_consolidated"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/temp"}),
            Action(name="CreateFileList", kwargs={"operation_id": "temp_consolidation_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/temp_export_001.csv", "destination_path": "/data/temp_consolidated/temp_export_001.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/temp_consolidated/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "temp_consolidation_01", "user_id": "user_001", "message": "Temporary files have been consolidated for review."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Temporary files have been consolidated for review."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="048",
        instruction=(
            "You are a Data Engineer setting up a new project on `server-data-01.company.com`. Create a project workspace at `/data/projects/sales_analyzer/` with an `input` subdirectory. Move the necessary source data, `sales_data.csv` and `customer_info.csv`, from `/data/unsorted` into the new `input` directory to begin the analysis. "
            "Announce the setup in the 'Operations' channel with the message 'Sales analyzer project workspace is set up.'. "
            "For task id you should use 'proj_setup_sales_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "proj_setup_sales_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/projects"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/projects/sales_analyzer"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/projects/sales_analyzer/input"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "proj_setup_sales_01", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/projects/sales_analyzer/input/sales_data.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/projects/sales_analyzer/input/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "proj_setup_sales_01", "user_id": "user_002", "message": "Sales analyzer project workspace is set up."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Sales analyzer project workspace is set up."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="051",
        instruction=(
            "You are a Project Manager. To prepare for a board meeting, you need to consolidate all key sales reports from `server-analytics.company.com`. Create a new folder at `/analytics/management_review/sales_q1/`. Move `daily_sales_report.csv` and `monthly_trends.csv` from `/analytics/reports` into this new directory. "
            "Notify the 'Operations' channel with the message 'Sales reports for Q1 management review have been consolidated.'. "
            "For task id you should use 'mgmt_review_01' and for user_id 'user_005'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "mgmt_review_01", "user_id": "user_005", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/management_review"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/management_review/sales_q1"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "mgmt_review_01", "filepaths": ["/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/management_review/sales_q1/daily_sales_report.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/management_review/sales_q1/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "mgmt_review_01", "user_id": "user_005", "message": "Sales reports for Q1 management review have been consolidated."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Sales reports for Q1 management review have been consolidated."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="052",
        instruction=(
            "You are a Data Analyst tasked with reorganizing the data on `server-analytics.company.com`. Create a new parent directory at `/analytics/organized/` with `raw_sources` and `final_reports` subdirectories. Move the `user_events_2023.csv` from `/analytics/raw_data` into `raw_sources`, and move `daily_sales_report.csv` from `/analytics/reports` into `final_reports`. "
            "Announce the successful reorganization in the 'File Check' channel with the message 'Analytics data has been reorganized by source and type.'. "
            "For task id you should use 'analytics_org_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "analytics_org_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/organized"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/organized/raw_sources"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/organized/final_reports"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics"}),
            Action(name="CreateFileList", kwargs={"operation_id": "analytics_org_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv", "/analytics/reports/daily_sales_report.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/raw_data/user_events_2023.csv", "destination_path": "/analytics/organized/raw_sources/user_events_2023.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/organized/final_reports/daily_sales_report.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "analytics_org_01", "user_id": "user_003", "message": "Analytics data has been reorganized by source and type."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Analytics data has been reorganized by source and type."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="053",
        instruction=(
            "You are a Developer debugging an issue on `server-prod-01.company.com`. Create a dedicated workspace for your investigation at `/var/log/debugging_sessions/session_7/`. To avoid clutter, move only the `error.log` from `/var/log/applications` into this new directory for focused analysis. "
            "Announce in the 'Operations' channel with the message 'Error log isolated for debugging session 7.'. "
            "For task id you should use 'debug_session_07' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "debug_session_07", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/debugging_sessions"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/debugging_sessions/session_7"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "debug_session_07", "filepaths": ["/var/log/applications/error.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/error.log", "destination_path": "/var/log/debugging_sessions/session_7/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "debug_session_07", "user_id": "user_002", "message": "Error log isolated for debugging session 7."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Error log isolated for debugging session 7."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="054",
        instruction=(
            "You are a Data Engineer preparing to run validation scripts. On `server-data-01.company.com`, create a new workspace at `/data/validation/`. Move both `sales_data.csv` and `customer_info.csv` from the `/data/unsorted` directory into this new location to begin the validation process. "
            "Notify the 'Operations' channel with the message 'Unsorted data has been staged in a validation workspace.'. "
            "For task id you should use 'validation_setup_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "validation_setup_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/validation"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "validation_setup_01", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/validation/sales_data.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/validation/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "validation_setup_01", "user_id": "user_002", "message": "Unsorted data has been staged in a validation workspace."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Unsorted data has been staged in a validation workspace."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="055",
        instruction=(
            "You are a Data Analyst creating a snapshot of the January reports on `server-analytics.company.com`. Create a new directory structure `/analytics/snapshots/january/`. Move the `monthly_trends.csv` file from `/analytics/reports` into this new directory to preserve the monthly record. "
            "Announce in the 'File Check' channel with the message 'January monthly report snapshot has been created.'. "
            "For task id you should use 'report_snapshot_jan' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "report_snapshot_jan", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/snapshots"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/snapshots/january"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "report_snapshot_jan", "filepaths": ["/analytics/reports/monthly_trends.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/snapshots/january/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "report_snapshot_jan", "user_id": "user_003", "message": "January monthly report snapshot has been created."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "January monthly report snapshot has been created."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="056",
        instruction=(
            "You are a System Administrator on `server-prod-01.company.com`. To simplify debugging, you need to separate the web and API logs. Create new directories at `/var/log/applications/web/` and `/var/log/applications/api/`. Move `webapp.log` into the `web` directory and `api_requests.log` into the `api` directory. "
            "Notify the 'System Alerts' channel with the message 'Production web and API logs have been separated.'. "
            "For task id you should use 'log_separation_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "log_separation_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/applications/web"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/applications/api"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "log_separation_01", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/webapp.log", "destination_path": "/var/log/applications/web/webapp.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/api_requests.log", "destination_path": "/var/log/applications/api/api_requests.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "log_separation_01", "user_id": "user_001", "message": "Production web and API logs have been separated."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Production web and API logs have been separated."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="057",
        instruction=(
            "You are a Data Engineer. To improve data organization on `server-data-01.company.com`, you need to sort files by their type. Create a new structure at `/data/sorted_by_type/` with `csv_files` and `dat_files` subdirectories. Move `sales_data.csv` from `/data/unsorted` to `csv_files`, and move `cache_backup.dat` from `/data/temp` to `dat_files`. "
            "Announce the new structure in the 'Operations' channel with the message 'Data on server-data-01 has been sorted by file type.'. "
            "For task id you should use 'data_sort_by_type_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "data_sort_by_type_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/sorted_by_type"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/sorted_by_type/csv_files"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/sorted_by_type/dat_files"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/"}),
            Action(name="CreateFileList", kwargs={"operation_id": "data_sort_by_type_01", "filepaths": ["/data/unsorted/sales_data.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/sorted_by_type/csv_files/sales_data.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/sorted_by_type/dat_files/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "data_sort_by_type_01", "user_id": "user_002", "message": "Data on server-data-01 has been sorted by file type."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Data on server-data-01 has been sorted by file type."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="058",
        instruction=(
            "You are a System Administrator. The `/data/temp` directory on `server-data-01.company.com` needs to be cleared. Create a new directory `/data/cold_storage/temp_files/` to serve as a new cold storage location. Move all files from `/data/temp` into this new directory. "
            "Announce the completion in the 'System Alerts' channel with the message 'Temporary files have been moved to a new cold storage location.'. "
            "For task id you should use 'cold_storage_setup_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "cold_storage_setup_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/cold_storage"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/cold_storage/temp_files"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/temp"}),
            Action(name="CreateFileList", kwargs={"operation_id": "cold_storage_setup_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/temp_export_001.csv", "destination_path": "/data/cold_storage/temp_files/temp_export_001.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/cold_storage/temp_files/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "cold_storage_setup_01", "user_id": "user_001", "message": "Temporary files have been moved to a new cold storage location."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Temporary files have been moved to a new cold storage location."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="061",
        instruction=(
            "You are a System Administrator. To prepare for a new log rotation system on `server-prod-01.company.com`, you must move all current logs into a new `active` subdirectory. Create the directory `/var/log/applications/active/` and move all log files from `/var/log/applications` into it. "
            "Notify the 'System Alerts' channel with the message 'Production logs moved to new active directory.'. "
            "For task id you should use 'log_restructure_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "log_restructure_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/applications/active"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "log_restructure_01", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/webapp.log", "destination_path": "/var/log/applications/active/webapp.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/api_requests.log", "destination_path": "/var/log/applications/active/api_requests.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/error.log", "destination_path": "/var/log/applications/active/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "log_restructure_01", "user_id": "user_001", "message": "Production logs moved to new active directory."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Production logs moved to new active directory."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="062",
        instruction=(
            "You are a System Administrator improving log hygiene from '/var/log/applications' on `server-prod-01.company.com`. Create a new directory structure at `/var/log/sorted_logs/` with `api` and `webapp` subdirectories. Separate the existing logs by moving `api_requests.log` to the `api` folder and `webapp.log` to the `webapp` folder, leaving the error log in its original location for now. "
            "Announce the change in the 'System Alerts' channel with the message 'Production logs have been separated by source.'. "
            "For task id you should use 'log_hygiene_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "log_hygiene_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/sorted_logs"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/sorted_logs/api"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/sorted_logs/webapp"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "log_hygiene_01", "filepaths": ["/var/log/applications/api_requests.log", "/var/log/applications/webapp.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/api_requests.log", "destination_path": "/var/log/sorted_logs/api/api_requests.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/webapp.log", "destination_path": "/var/log/sorted_logs/webapp/webapp.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "log_hygiene_01", "user_id": "user_001", "message": "Production logs have been separated by source."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Production logs have been separated by source."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="063",
        instruction=(
            "You are a DevOps Engineer preparing for a server migration. All staging data from `server-data-01.company.com` needs to be consolidated. Create a new directory `/data/migration_staging/` and move all files from both `/data/temp` and `/data/unsorted` into this single location for testing. "
            "Announce this in the 'Operations' channel with the message 'All staging data on server-data-01 has been consolidated for migration testing.'. "
            "For task id you should use 'migration_prep_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "migration_prep_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/migration_staging"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/"}),
            Action(name="CreateFileList", kwargs={"operation_id": "migration_prep_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat", "/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/temp_export_001.csv", "destination_path": "/data/migration_staging/temp_export_001.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/migration_staging/cache_backup.dat"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/migration_staging/sales_data.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/migration_staging/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "migration_prep_01", "user_id": "user_002", "message": "All staging data on server-data-01 has been consolidated for migration testing."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "All staging data on server-data-01 has been consolidated for migration testing."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="064",
        instruction=(
            "You are a Security Administrator conducting an audit. The existing analytics archive on `storage-01.company.com` needs to be moved to a secure location for review. Create a new directory at `/storage/secure_review/` and move the `analytics_data_archive_20240116_103000.tar.gz` from `/storage/archives` into it. "
            "Send a notification to the 'System Alerts' channel with the message 'Analytics archive has been moved to a secure directory for audit.'. "
            "For task id you should use 'secure_audit_move_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "secure_audit_move_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "storage-01.company.com", "new_directory_path": "/storage/secure_review"}),
            Action(name="FindFiles", kwargs={"server_hostname": "storage-01.company.com", "search_path": "/storage/archives"}),
            Action(name="CreateFileList", kwargs={"operation_id": "secure_audit_move_01", "filepaths": ["/storage/archives/analytics_data_archive_20240116_103000.tar.gz"]}),
            Action(name="MoveFile", kwargs={"source_path": "/storage/archives/analytics_data_archive_20240116_103000.tar.gz", "destination_path": "/storage/secure_review/analytics_data_archive_20240116_103000.tar.gz"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "secure_audit_move_01", "user_id": "user_001", "message": "Analytics archive has been moved to a secure directory for audit."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Analytics archive has been moved to a secure directory for audit."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="065",
        instruction=(
            "You are a Project Manager setting up a new initiative on `server-analytics.company.com`. Create a new workspace for this project at `/analytics/projects/customer_behavior_study/`. As a first step, move the `user_events_2023.csv` file from `/analytics/raw_data` into your new project directory to begin analysis. "
            "Announce in the 'Operations' channel with the message 'Workspace for customer behavior study is now active.'. "
            "For task id you should use 'raw_data_org_01' and for user_id 'user_005'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "raw_data_org_01", "user_id": "user_005", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/projects"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/projects/customer_behavior_study"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/raw_data"}),
            Action(name="CreateFileList", kwargs={"operation_id": "raw_data_org_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/raw_data/user_events_2023.csv", "destination_path": "/analytics/projects/customer_behavior_study/user_events_2023.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "raw_data_org_01", "user_id": "user_005", "message": "Workspace for customer behavior study is now active."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Workspace for customer behavior study is now active."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="066",
        instruction=(
            "You are a DevOps Engineer creating a 'gold copy' standard for essential logs on `server-prod-01.company.com`. Create a new directory at `/var/log/gold_copies/`. Move the `webapp.log` and `error.log` from `/var/log/applications` into this new directory to establish them as reference copies. "
            "Notify the 'Operations' channel with the message 'Gold copies of critical production logs have been created.'. "
            "For task id you should use 'gold_copy_logs_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "gold_copy_logs_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/gold_copies"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "gold_copy_logs_01", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/error.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/webapp.log", "destination_path": "/var/log/gold_copies/webapp.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/error.log", "destination_path": "/var/log/gold_copies/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "gold_copy_logs_01", "user_id": "user_002", "message": "Gold copies of critical production logs have been created."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Gold copies of critical production logs have been created."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="067",
        instruction=(
            "You are a Data Analyst. To prepare for different analysis tasks on `server-analytics.company.com`, you need to separate reports from '/analytics/reports'. Create two new directories: `/analytics/internal_analysis/` and `/analytics/sales_analysis/`. Move `monthly_trends.csv` to `internal_analysis` and `daily_sales_report.csv` to `sales_analysis`. "
            "Announce the completion in the 'File Check' channel with the message 'Analytics reports have been separated for focused analysis.'. "
            "For task id you should use 'analysis_focus_setup_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "analysis_focus_setup_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/internal_analysis"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/sales_analysis"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "analysis_focus_setup_01", "filepaths": ["/analytics/reports/monthly_trends.csv", "/analytics/reports/daily_sales_report.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/internal_analysis/monthly_trends.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/sales_analysis/daily_sales_report.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "analysis_focus_setup_01", "user_id": "user_003", "message": "Analytics reports have been separated for focused analysis."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Analytics reports have been separated for focused analysis."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="068",
        instruction=(
            "You are a Security Administrator investigating an incident on `server-prod-01.company.com`. To prevent tampering, you must isolate the `api_requests.log`. Create a new secure directory at `/var/log/incident_review/` and move the `api_requests.log` from `/var/log/applications` into it for analysis. "
            "Announce this action in the 'System Alerts' channel with the message 'API log has been isolated for incident review.'. "
            "For task id you should use 'sec_review_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "sec_review_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/incident_review"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "sec_review_01", "filepaths": ["/var/log/applications/api_requests.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/api_requests.log", "destination_path": "/var/log/incident_review/api_requests.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "sec_review_01", "user_id": "user_001", "message": "API log has been isolated for incident review."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "API log has been isolated for incident review."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="069",
        instruction=(
            "You are a Data Analyst preparing a data delivery for an external partner. On `server-analytics.company.com`, create a staging directory at `/analytics/partner_delivery/`. Move the `monthly_trends.csv` report from `/analytics/reports` into this new directory to prepare it for secure transfer. "
            "Notify the 'File Check' channel with the message 'Partner data delivery is staged and ready for transfer.'. "
            "For task id you should use 'partner_delivery_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "partner_delivery_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/partner_delivery"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "partner_delivery_01", "filepaths": ["/analytics/reports/monthly_trends.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/partner_delivery/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "partner_delivery_01", "user_id": "user_003", "message": "Partner data delivery is staged and ready for transfer."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Partner data delivery is staged and ready for transfer."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="070",
        instruction=(
            "You are a System Administrator on `server-data-01.company.com` implementing a new cleanup policy. Create a new directory `/data/to_be_deleted/`. Move the old `cache_backup.dat` from `/data/temp` into this directory to mark it for deletion in the next maintenance window. "
            "Announce this in the 'System Alerts' channel with the message 'Old cache file has been staged for deletion.'. "
            "For task id you should use 'cleanup_staging_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "cleanup_staging_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/to_be_deleted"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/temp"}),
            Action(name="CreateFileList", kwargs={"operation_id": "cleanup_staging_01", "filepaths": ["/data/temp/cache_backup.dat"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/to_be_deleted/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "cleanup_staging_01", "user_id": "user_001", "message": "Old cache file has been staged for deletion."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Old cache file has been staged for deletion."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="071",
        instruction=(
            "You are a Data Engineer on `server-data-01.company.com`. You need to organize the unsorted data from '/data/unsorted'. Create a new directory at `/data/processed/` with subdirectories `sales` and `customers`. Move `sales_data.csv` to the `sales` folder and `customer_info.csv` to the `customers` folder. "
            "Notify the 'Operations' channel with the message 'Unsorted data has been processed and organized.'. "
            "For task id you should use 'data_processing_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "data_processing_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/processed"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/processed/sales"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/processed/customers"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "data_processing_01", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/processed/sales/sales_data.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/processed/customers/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "data_processing_01", "user_id": "user_002", "message": "Unsorted data has been processed and organized."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Unsorted data has been processed and organized."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="072",
        instruction=(
            "You are a Developer investigating a performance issue. On `server-prod-01.company.com`, create a new workspace for your analysis at `/var/log/performance_analysis/`. Move the `webapp.log` from `/var/log/applications` into this new directory to begin your investigation without affecting the live log directory. "
            "Announce this in the 'Operations' channel with the message 'Webapp log has been staged for performance analysis.'. "
            "For task id you should use 'perf_analysis_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "perf_analysis_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/performance_analysis"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "perf_analysis_01", "filepaths": ["/var/log/applications/webapp.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/webapp.log", "destination_path": "/var/log/performance_analysis/webapp.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "perf_analysis_01", "user_id": "user_002", "message": "Webapp log has been staged for performance analysis."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Webapp log has been staged for performance analysis."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="074",
        instruction=(
            "You are a Data Engineer on `server-data-01.company.com`. The files in the `/data/temp` directory have been successfully processed. To reflect this, create a new directory `/data/temp_processed/` and move all files from `/data/temp` into it. "
            "Announce this in the 'Operations' channel with the message 'Temporary data has been moved to a processed state directory.'. "
            "For task id you should use 'temp_data_cleanup_02' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "temp_data_cleanup_02", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/temp_processed"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/temp"}),
            Action(name="CreateFileList", kwargs={"operation_id": "temp_data_cleanup_02", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/temp_export_001.csv", "destination_path": "/data/temp_processed/temp_export_001.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/temp_processed/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "temp_data_cleanup_02", "user_id": "user_002", "message": "Temporary data has been moved to a processed state directory."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Temporary data has been moved to a processed state directory."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="075",
        instruction=(
            "You are a Data Analyst starting a new customer retention project. On `server-data-01.company.com`, create a new project folder at `/data/projects/retention_analysis/`. Move the `customer_info.csv` file from `/data/unsorted` into this new directory to begin your analysis. "
            "Notify the 'File Check' channel with the message 'Customer data has been staged for the retention project.'. "
            "For task id you should use 'customer_data_prep_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "customer_data_prep_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/projects"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/projects/retention_analysis"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "customer_data_prep_01", "filepaths": ["/data/unsorted/customer_info.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/projects/retention_analysis/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "customer_data_prep_01", "user_id": "user_003", "message": "Customer data has been staged for the retention project."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Customer data has been staged for the retention project."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="076",
        instruction=(
            "You are a Project Manager. To improve clarity on `server-analytics.company.com`, you need to organize reports from '/analytics/reports'. Create a new directory `/analytics/organized_reports/` with subdirectories `sales` and `trends`. Move `daily_sales_report.csv` to the `sales` folder and `monthly_trends.csv` to the `trends` folder. "
            "Announce the completion in the 'Operations' channel with the message 'Analytics reports have been organized by type.'. "
            "For task id you should use 'report_org_by_type_01' and for user_id 'user_005'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "report_org_by_type_01", "user_id": "user_005", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/organized_reports"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/organized_reports/sales"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/organized_reports/trends"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "report_org_by_type_01", "filepaths": ["/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/organized_reports/sales/daily_sales_report.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/organized_reports/trends/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "report_org_by_type_01", "user_id": "user_005", "message": "Analytics reports have been organized by type."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Analytics reports have been organized by type."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="077",
        instruction=(
            "You are a Security Administrator on `server-analytics.company.com`. In response to a privacy review request, you must quarantine raw user data. Create a new secure directory at `/analytics/quarantine_review/`. Move the `user_events_2023.csv` from `/analytics/raw_data` into this new directory for a detailed inspection. "
            "Send a high-priority alert to the 'System Alerts' channel with the message 'Raw user event data has been quarantined for review.'. "
            "For task id you should use 'raw_data_quarantine_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "raw_data_quarantine_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/quarantine_review"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/raw_data"}),
            Action(name="CreateFileList", kwargs={"operation_id": "raw_data_quarantine_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/raw_data/user_events_2023.csv", "destination_path": "/analytics/quarantine_review/user_events_2023.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "raw_data_quarantine_01", "user_id": "user_001", "message": "Raw user event data has been quarantined for review."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Raw user event data has been quarantined for review."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="080",
        instruction=(
            "You are a DevOps Engineer improving the log structure from '/var/log/applications' on `server-prod-01.company.com`. Create a new parent directory at `/var/log/structured/` with `general` and `errors` subdirectories. Move the `webapp.log` and `api_requests.log` into the `general` folder, and move the `error.log` into the `errors` folder. "
            "Announce the new structure in the 'Operations' channel with the message 'Application logs have been structured into general and error directories.'. "
            "For task id you should use 'log_struct_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "log_struct_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/structured"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/structured/general"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/structured/errors"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "log_struct_01", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/webapp.log", "destination_path": "/var/log/structured/general/webapp.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/api_requests.log", "destination_path": "/var/log/structured/general/api_requests.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/error.log", "destination_path": "/var/log/structured/errors/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "log_struct_01", "user_id": "user_002", "message": "Application logs have been structured into general and error directories."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Application logs have been structured into general and error directories."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="082",
        instruction=(
            "You are a System Administrator on `server-data-01.company.com`. To ensure compliance with data retention policies, all files in `/data/unsorted` must be staged for review before deletion. Create a new directory `/data/review_before_delete/` and move all files from `/data/unsorted` into it. "
            "Notify the 'System Alerts' channel with the message 'Unsorted data has been moved to a review directory pending deletion.'. "
            "For task id you should use 'unsorted_review_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "unsorted_review_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/review_before_delete"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "unsorted_review_01", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/review_before_delete/sales_data.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/review_before_delete/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "unsorted_review_01", "user_id": "user_001", "message": "Unsorted data has been moved to a review directory pending deletion."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Unsorted data has been moved to a review directory pending deletion."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="085",
        instruction=(
            "You are a DevOps Engineer. A data restoration request has been approved for an analytics archive on `storage-01.company.com`. To begin the process, create a new directory at `/storage/restore_queue/`. Move the `analytics_data_archive_20240116_103000.tar.gz` from `/storage/archives` into the queue. "
            "Announce in the 'Operations' channel with the message 'Analytics archive is queued for data restoration.'. "
            "For task id you should use 'restore_queue_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "restore_queue_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "storage-01.company.com", "new_directory_path": "/storage/restore_queue"}),
            Action(name="FindFiles", kwargs={"server_hostname": "storage-01.company.com", "search_path": "/storage/archives"}),
            Action(name="CreateFileList", kwargs={"operation_id": "restore_queue_01", "filepaths": ["/storage/archives/analytics_data_archive_20240116_103000.tar.gz"]}),
            Action(name="MoveFile", kwargs={"source_path": "/storage/archives/analytics_data_archive_20240116_103000.tar.gz", "destination_path": "/storage/restore_queue/analytics_data_archive_20240116_103000.tar.gz"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "restore_queue_01", "user_id": "user_002", "message": "Analytics archive is queued for data restoration."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Analytics archive is queued for data restoration."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="086",
        instruction=(
            "You are a Data Engineer on `server-data-01.company.com` tasked with organizing the temp directory. Create two new directories, `/data/temp/exports` and `/data/temp/cache`. Move the `temp_export_001.csv` into the `exports` folder and `cache_backup.dat` into the `cache` folder. "
            "Notify the 'Operations' channel with the message 'Temporary data has been sorted by type.'. "
            "For task id you should use 'temp_sort_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "temp_sort_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/temp/exports"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/temp/cache"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/temp"}),
            Action(name="CreateFileList", kwargs={"operation_id": "temp_sort_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/temp_export_001.csv", "destination_path": "/data/temp/exports/temp_export_001.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/temp/cache/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "temp_sort_01", "user_id": "user_002", "message": "Temporary data has been sorted by type."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Temporary data has been sorted by type."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="087",
        instruction=(
            "You are a Project Manager on `server-analytics.company.com`. You need to set up a workspace for a new analyst. Create a new directory `/analytics/projects/analyst_carol/` and move the raw `user_events_2023.csv` from `/analytics/raw_data` into this new directory so they can begin their work. "
            "Announce this in the 'Operations' channel with the message 'Raw user data has been staged for Analyst Luna's project.'. "
            "For task id you should use 'analyst_staging_01' and for user_id 'user_005'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "analyst_staging_01", "user_id": "user_005", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/projects"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/projects/analyst_carol"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/raw_data"}),
            Action(name="CreateFileList", kwargs={"operation_id": "analyst_staging_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/raw_data/user_events_2023.csv", "destination_path": "/analytics/projects/analyst_carol/user_events_2023.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "analyst_staging_01", "user_id": "user_005", "message": "Raw user data has been staged for Analyst Luna's project."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Raw user data has been staged for Analyst Luna's project."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="088",
        instruction=(
            "You are a Data Scientist starting a new project on `server-data-01.company.com`. Create a dedicated project workspace at `/data/projects/sales_forecast/`. Move the `sales_data.csv` from the `/data/unsorted` directory into this new location to begin your modeling work. "
            "Announce this in the 'Operations' channel with the message 'Sales forecasting project workspace is ready for analysis.'. "
            "For task id you should use 'ds_proj_setup_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "ds_proj_setup_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/projects"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/projects/sales_forecast"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "ds_proj_setup_01", "filepaths": ["/data/unsorted/sales_data.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/projects/sales_forecast/sales_data.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "ds_proj_setup_01", "user_id": "user_003", "message": "Sales forecasting project workspace is ready for analysis."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Sales forecasting project workspace is ready for analysis."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="089",
        instruction=(
            "You are a System Administrator on `server-prod-01.company.com`. To keep logs organized by date, create a new directory at `/var/log/applications/2024-01-15/`. Move all log files from the parent `/var/log/applications` directory into this new dated folder. "
            "Announce the completion in the 'System Alerts' channel with the message 'Production logs for 2024-01-15 have been organized.'. "
            "For task id you should use 'log_date_org_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "log_date_org_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/applications/2024-01-15"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "log_date_org_01", "filepaths": ["/var/log/applications/webapp.log", "/var/log/applications/api_requests.log", "/var/log/applications/error.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/webapp.log", "destination_path": "/var/log/applications/2024-01-15/webapp.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/api_requests.log", "destination_path": "/var/log/applications/2024-01-15/api_requests.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/error.log", "destination_path": "/var/log/applications/2024-01-15/error.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "log_date_org_01", "user_id": "user_001", "message": "Production logs for 2024-01-15 have been organized."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Production logs for 2024-01-15 have been organized."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="090",
        instruction=(
            "You are a DevOps Engineer managing the data pipeline on `server-data-01.company.com`. All files currently in `/data/unsorted` need to be formally queued for processing. Create a new directory `/data/ingestion_queue/` and move all files from `/data/unsorted` into it. "
            "Notify the 'Operations' channel with the message 'All unsorted data has been moved to the ingestion queue.'. "
            "For task id you should use 'ingest_queue_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "ingest_queue_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/ingestion_queue"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "ingest_queue_01", "filepaths": ["/data/unsorted/sales_data.csv", "/data/unsorted/customer_info.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/sales_data.csv", "destination_path": "/data/ingestion_queue/sales_data.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/ingestion_queue/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "ingest_queue_01", "user_id": "user_002", "message": "All unsorted data has been moved to the ingestion queue."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "All unsorted data has been moved to the ingestion queue."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="093",
        instruction=(
            "You are a DevOps Engineer on `server-data-01.company.com`. The files in the `/data/temp` directory need to be formally queued for the next stage of the data pipeline. Create a new directory `/data/to_be_processed/` and move all files from `/data/temp` into it. "
            "Announce this in the 'Operations' channel with the message 'Temporary data has been queued for processing.'. "
            "For task id you should use 'queue_temp_data_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "queue_temp_data_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/to_be_processed"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/temp"}),
            Action(name="CreateFileList", kwargs={"operation_id": "queue_temp_data_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/temp_export_001.csv", "destination_path": "/data/to_be_processed/temp_export_001.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/to_be_processed/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "queue_temp_data_01", "user_id": "user_002", "message": "Temporary data has been queued for processing."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Temporary data has been queued for processing."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="094",
        instruction=(
            "You are a Data Analyst on `storage-01.company.com`. Before restoring an archive, you must validate its contents. Create a new directory at `/storage/validation_queue/` and move the `analytics_data_archive_20240116_103000.tar.gz` from `/storage/archives` into this new location for validation. "
            "Notify the 'File Check' channel with the message 'Analytics archive has been moved to the validation queue.'. "
            "For task id you should use 'validation_queue_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "validation_queue_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "storage-01.company.com", "new_directory_path": "/storage/validation_queue"}),
            Action(name="FindFiles", kwargs={"server_hostname": "storage-01.company.com", "search_path": "/storage/archives"}),
            Action(name="CreateFileList", kwargs={"operation_id": "validation_queue_01", "filepaths": ["/storage/archives/analytics_data_archive_20240116_103000.tar.gz"]}),
            Action(name="MoveFile", kwargs={"source_path": "/storage/archives/analytics_data_archive_20240116_103000.tar.gz", "destination_path": "/storage/validation_queue/analytics_data_archive_20240116_103000.tar.gz"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "validation_queue_01", "user_id": "user_003", "message": "Analytics archive has been moved to the validation queue."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Analytics archive has been moved to the validation queue."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="095",
        instruction=(
            "You are a System Administrator on `server-prod-01.company.com` implementing a log tiering policy for '/var/log/applications'. Create two new directories: `/var/log/hot_logs/` for critical errors and `/var/log/cold_logs/` for general traffic. Move the `error.log` into `hot_logs` and move the `api_requests.log` into `cold_logs`. "
            "Announce this in the 'System Alerts' channel with the message 'Production logs have been tiered into hot and cold storage.'. "
            "For task id you should use 'log_tiering_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "log_tiering_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/hot_logs"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/cold_logs"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "log_tiering_01", "filepaths": ["/var/log/applications/error.log", "/var/log/applications/api_requests.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/error.log", "destination_path": "/var/log/hot_logs/error.log"}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/api_requests.log", "destination_path": "/var/log/cold_logs/api_requests.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "log_tiering_01", "user_id": "user_001", "message": "Production logs have been tiered into hot and cold storage."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Production logs have been tiered into hot and cold storage."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="096",
        instruction=(
            "You are a Project Manager. To consolidate all assets for the user engagement project on `server-analytics.company.com`, create a new project directory at `/analytics/projects/user_engagement/`. Move both the raw data `user_events_2023.csv` from `/analytics/raw_data` and the final report `monthly_trends.csv` from `/analytics/reports` into this directory. "
            "Notify the 'Operations' channel with the message 'All assets for the user engagement project are now consolidated.'. "
            "For task id you should use 'proj_consolidation_01' and for user_id 'user_005'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "proj_consolidation_01", "user_id": "user_005", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/projects"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/projects/user_engagement"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics"}),
            Action(name="CreateFileList", kwargs={"operation_id": "proj_consolidation_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/raw_data/user_events_2023.csv", "destination_path": "/analytics/projects/user_engagement/user_events_2023.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/projects/user_engagement/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "proj_consolidation_01", "user_id": "user_005", "message": "All assets for the user engagement project are now consolidated."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "All assets for the user engagement project are now consolidated."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="097",
        instruction=(
            "You are a Data Engineer on `server-data-01.company.com`. You need to prepare data for a new analyst. Create a new directory `/data/analyst_staging/carol/` and move the `customer_info.csv` from the `/data/unsorted` directory into this new location for them to begin their work. "
            "Notify the 'Operations' channel with the message 'Customer data has been staged for analyst review.'. "
            "For task id you should use 'analyst_staging_02' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "analyst_staging_02", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/analyst_staging"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/analyst_staging/carol"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/unsorted"}),
            Action(name="CreateFileList", kwargs={"operation_id": "analyst_staging_02", "filepaths": ["/data/unsorted/customer_info.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/unsorted/customer_info.csv", "destination_path": "/data/analyst_staging/carol/customer_info.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "analyst_staging_02", "user_id": "user_002", "message": "Customer data has been staged for analyst review."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Customer data has been staged for analyst review."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="098",
        instruction=(
            "You are a Developer on `server-prod-01.company.com` starting a debugging session for a performance issue. Create a dedicated directory at `/var/log/debug_sessions/webapp_perf/` and move the `webapp.log` from `/var/log/applications` into it to analyze it without interrupting the live logging. "
            "Announce this in the 'Operations' channel with the message 'Webapp log staged for performance debugging.'. "
            "For task id you should use 'debug_webapp_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "debug_webapp_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/debug_sessions"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-prod-01.company.com", "new_directory_path": "/var/log/debug_sessions/webapp_perf"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-prod-01.company.com", "search_path": "/var/log/applications"}),
            Action(name="CreateFileList", kwargs={"operation_id": "debug_webapp_01", "filepaths": ["/var/log/applications/webapp.log"]}),
            Action(name="MoveFile", kwargs={"source_path": "/var/log/applications/webapp.log", "destination_path": "/var/log/debug_sessions/webapp_perf/webapp.log"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "debug_webapp_01", "user_id": "user_002", "message": "Webapp log staged for performance debugging."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Webapp log staged for performance debugging."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="099",
        instruction=(
            "You are a Data Analyst on `server-analytics.company.com` preparing for a quarterly business review. Consolidate all reports into a single folder. Create a new directory at `/analytics/reports/consolidated_q1/` and move all files from the parent `/analytics/reports` directory into it. "
            "Notify the 'File Check' channel with the message 'All Q1 reports have been consolidated for review.'. "
            "For task id you should use 'report_consolidate_02' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "report_consolidate_02", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/reports/consolidated_q1"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "report_consolidate_02", "filepaths": ["/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/reports/consolidated_q1/daily_sales_report.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/reports/consolidated_q1/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "report_consolidate_02", "user_id": "user_003", "message": "All Q1 reports have been consolidated for review."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "All Q1 reports have been consolidated for review."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="100",
        instruction=(
            "You are a System Administrator on `server-data-01.company.com`. As a preliminary step for a cleanup routine, all temporary files must be staged. Create a new directory `/data/temp/staged_for_archival/` and move all files from the parent `/data/temp` directory into it. "
            "Announce this in the 'System Alerts' channel with the message 'Temporary data has been staged for archival.'. "
            "For task id you should use 'stage_temp_cleanup_01' and for user_id 'user_001'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "stage_temp_cleanup_01", "user_id": "user_001", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-data-01.company.com", "new_directory_path": "/data/temp/staged_for_archival"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-data-01.company.com", "search_path": "/data/temp"}),
            Action(name="CreateFileList", kwargs={"operation_id": "stage_temp_cleanup_01", "filepaths": ["/data/temp/temp_export_001.csv", "/data/temp/cache_backup.dat"]}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/temp_export_001.csv", "destination_path": "/data/temp/staged_for_archival/temp_export_001.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/data/temp/cache_backup.dat", "destination_path": "/data/temp/staged_for_archival/cache_backup.dat"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "stage_temp_cleanup_01", "user_id": "user_001", "message": "Temporary data has been staged for archival."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "System Alerts", "message": "Temporary data has been staged for archival."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="101",
        instruction=(
            "You are a Project Manager on `server-analytics.company.com`. To kick off a new study, consolidate all existing data into one place. Create a new project directory at `/analytics/projects/user_trends_study/` and move all files from both `/analytics/raw_data` and `/analytics/reports` into this directory. "
            "Notify the 'Operations' channel with the message 'All data for the user trends study has been consolidated.'. "
            "For task id you should use 'proj_consolidate_02' and for user_id 'user_005'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "proj_consolidate_02", "user_id": "user_005", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/projects"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/projects/user_trends_study"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics"}),
            Action(name="CreateFileList", kwargs={"operation_id": "proj_consolidate_02", "filepaths": ["/analytics/raw_data/user_events_2023.csv", "/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/raw_data/user_events_2023.csv", "destination_path": "/analytics/projects/user_trends_study/user_events_2023.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/projects/user_trends_study/daily_sales_report.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/projects/user_trends_study/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "proj_consolidate_02", "user_id": "user_005", "message": "All data for the user trends study has been consolidated."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "All data for the user trends study has been consolidated."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="102",
        instruction=(
            "You are a Data Engineer on `server-analytics.company.com`. The raw data for user events has been successfully ingested into the data warehouse. To reflect this, create a new directory at `/analytics/raw_data/ingestion_complete/` and move the `user_events_2023.csv` file into it. "
            "Announce this pipeline step in the 'Operations' channel with the message 'Raw user event data has been marked as 'ingestion complete'.'. "
            "For task id you should use 'ingest_complete_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "ingest_complete_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/raw_data/ingestion_complete"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/raw_data"}),
            Action(name="CreateFileList", kwargs={"operation_id": "ingest_complete_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/raw_data/user_events_2023.csv", "destination_path": "/analytics/raw_data/ingestion_complete/user_events_2023.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "ingest_complete_01", "user_id": "user_002", "message": "Raw user event data has been marked as 'ingestion complete'."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Raw user event data has been marked as 'ingestion complete'."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="103",
        instruction=(
            "You are a Data Analyst on `server-analytics.company.com`. To clean up the main reporting directory, you need to move older reports to a legacy folder. Create a new directory at `/analytics/reports/legacy/` and move both `daily_sales_report.csv` and `monthly_trends.csv` into it. "
            "Announce the completion in the 'File Check' channel with the message 'Legacy analytics reports have been successfully migrated.'. "
            "For task id you should use 'legacy_reports_01' and for user_id 'user_003'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "legacy_reports_01", "user_id": "user_003", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/reports/legacy"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/reports"}),
            Action(name="CreateFileList", kwargs={"operation_id": "legacy_reports_01", "filepaths": ["/analytics/reports/daily_sales_report.csv", "/analytics/reports/monthly_trends.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/daily_sales_report.csv", "destination_path": "/analytics/reports/legacy/daily_sales_report.csv"}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/reports/monthly_trends.csv", "destination_path": "/analytics/reports/legacy/monthly_trends.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "legacy_reports_01", "user_id": "user_003", "message": "Legacy analytics reports have been successfully migrated."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "File Check", "message": "Legacy analytics reports have been successfully migrated."}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="104",
        instruction=(
            "You are a Data Engineer on `server-analytics.company.com` tasked with performing a data quality check. Create a new workspace at `/analytics/quality_assurance/` and move the raw data file `user_events_2023.csv` from `/analytics/raw_data` into this new directory for testing. "
            "Notify the 'Operations' channel with the message 'Raw user data has been staged for quality assurance testing.'. "
            "For task id you should use 'qa_setup_01' and for user_id 'user_002'. "
            "Also make sure to log the files list before moving them. "
        ),
        actions=[
            Action(name="LogTaskStart", kwargs={"task_id": "qa_setup_01", "user_id": "user_002", "task_type": "monitoring"}),
            Action(name="CreateDirectory", kwargs={"server_hostname": "server-analytics.company.com", "new_directory_path": "/analytics/quality_assurance"}),
            Action(name="FindFiles", kwargs={"server_hostname": "server-analytics.company.com", "search_path": "/analytics/raw_data"}),
            Action(name="CreateFileList", kwargs={"operation_id": "qa_setup_01", "filepaths": ["/analytics/raw_data/user_events_2023.csv"]}),
            Action(name="MoveFile", kwargs={"source_path": "/analytics/raw_data/user_events_2023.csv", "destination_path": "/analytics/quality_assurance/user_events_2023.csv"}),
            Action(name="LogCompletionMessage", kwargs={"task_id": "qa_setup_01", "user_id": "user_002", "message": "Raw user data has been staged for quality assurance testing."}),
            Action(name="SendSlackNotification", kwargs={"channel_name": "Operations", "message": "Raw user data has been staged for quality assurance testing."}),
        ],
        outputs=[]
    ),

]
