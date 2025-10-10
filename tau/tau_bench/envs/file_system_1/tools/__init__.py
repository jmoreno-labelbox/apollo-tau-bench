# Copyright owned by Sierra

from .get_archive_instructions_by_id import GetArchiveInstructionsByID
from .get_file_check_task_by_id import GetFileCheckTaskByID
from .get_directory_operation_by_id import GetDirectoryOperationByID
from .get_server_status_by_hostname import GetServerStatusByHostname
from .check_remote_disk_space import CheckRemoteDiskSpace
from .get_server_resource_usage import GetServerResourceUsage
from .get_security_policy_by_name import GetSecurityPolicyByName
from .get_user_info_by_id import GetUserInfoByID
from .get_user_contact_info import GetUserContactInfo
from .get_ssh_key_by_id import GetSshKeyByID
from .get_user_default_ssh_key import GetUserDefaultSshKey
from .check_remote_file_exists import CheckRemoteFileExists
from .get_error_log_details import GetErrorLogDetails
from .find_pending_tasks_by_type import FindPendingTasksByType
from .get_files_for_directory_operation import GetFilesForDirectoryOperation
from .get_last_successful_task_run import GetLastSuccessfulTaskRun
from .scan_remote_directory import ScanRemoteDirectory
from .create_directory_on_remote import CreateDirectoryOnRemote
from .move_file_on_remote import MoveFileOnRemote
from .create_archive_on_remote import CreateArchiveOnRemote
from .transfer_file_to_remote import TransferFileToRemote
from .delete_file_on_remote import DeleteFileOnRemote
from .get_remote_file_checksum import GetRemoteFileChecksum
from .update_archive_task_status import UpdateArchiveTaskStatus
from .update_file_check_task_status import UpdateFileCheckTaskStatus
from .update_directory_operation_status import UpdateDirectoryOperationStatus
from .log_error_message import LogErrorMessage
from .log_task_completion import LogTaskCompletion
from .send_slack_message import SendSlackMessage

ALL_TOOLS = [
    GetArchiveInstructionsByID,
    GetFileCheckTaskByID,
    GetDirectoryOperationByID,
    GetServerStatusByHostname,
    CheckRemoteDiskSpace,
    GetServerResourceUsage,
    GetSecurityPolicyByName,
    GetUserInfoByID,
    GetUserContactInfo,
    GetSshKeyByID,
    GetUserDefaultSshKey,
    CheckRemoteFileExists,
    GetErrorLogDetails,
    FindPendingTasksByType,
    GetFilesForDirectoryOperation,
    GetLastSuccessfulTaskRun,
    ScanRemoteDirectory,
    CreateDirectoryOnRemote,
    MoveFileOnRemote,
    CreateArchiveOnRemote,
    TransferFileToRemote,
    DeleteFileOnRemote,
    GetRemoteFileChecksum,
    UpdateArchiveTaskStatus,
    UpdateFileCheckTaskStatus,
    UpdateDirectoryOperationStatus,
    LogErrorMessage,
    LogTaskCompletion,
    SendSlackMessage,
]
