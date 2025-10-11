# Copyright Sierra

from .scan_incomplete_tasks_tool import ScanIncompleteTasksTool
from .parse_file_check_instructions_tool import ParseFileCheckInstructionsTool
from .send_slack_notification_tool import SendSlackNotificationTool
from .check_ssh_connection_tool import CheckSshConnectionTool
from .create_tmux_session_tool import CreateTmuxSessionTool
from .get_idle_cpu_count_tool import GetIdleCpuCountTool
from .find_and_stat_files_tool import FindAndStatFilesTool
from .filter_file_log_tool import FilterFileLogTool
from .add_header_to_file_log_tool import AddHeaderToFileLogTool
from .compute_checksum_tool import ComputeChecksumTool
from .copy_file_to_host_tool import CopyFileToHostTool
from .verify_local_checksum_tool import VerifyLocalChecksumTool
from .local_cleanup_tool import LocalCleanupTool
from .remote_cleanup_tool import RemoteCleanupTool
from .update_task_status_tool import UpdateTaskStatusTool
from .parse_directory_restructure_instructions_tool import ParseDirectoryRestructureInstructionsTool
from .create_file_list_for_move_tool import CreateFileListForMoveTool
from .get_disk_space_tool import GetDiskSpaceTool
from .verify_space_requirements_tool import VerifySpaceRequirementsTool
from .populate_checksums_in_file_list_tool import PopulateChecksumsInFileListTool
from .compute_and_resolve_destination_paths_tool import ComputeAndResolveDestinationPathsTool
from .copy_and_verify_files_tool import CopyAndVerifyFilesTool
from .clean_original_directory_tool import CleanOriginalDirectoryTool
from .calculate_total_size_tool import CalculateTotalSizeTool
from .verify_remote_checksum_tool import VerifyRemoteChecksumTool
from .log_task_completion_tool import LogTaskCompletionTool
from .update_archive_status_tool import UpdateArchiveStatusTool
from .parse_archive_instructions_tool import ParseArchiveInstructionsTool
from .validate_files_exist_tool import ValidateFilesExistTool
from .create_tar_archive_tool import CreateTarArchiveTool
from .transfer_archive_rsync_tool import TransferArchiveRsyncTool
from .delete_source_files_tool import DeleteSourceFilesTool

ALL_TOOLS = [
    ScanIncompleteTasksTool,
    ParseFileCheckInstructionsTool,
    SendSlackNotificationTool,
    CheckSshConnectionTool,
    CreateTmuxSessionTool,
    GetIdleCpuCountTool,
    FindAndStatFilesTool,
    FilterFileLogTool,
    AddHeaderToFileLogTool,
    ComputeChecksumTool,
    CopyFileToHostTool,
    VerifyLocalChecksumTool,
    LocalCleanupTool,
    RemoteCleanupTool,
    UpdateTaskStatusTool,
    ParseDirectoryRestructureInstructionsTool,
    CreateFileListForMoveTool,
    GetDiskSpaceTool,
    VerifySpaceRequirementsTool,
    PopulateChecksumsInFileListTool,
    ComputeAndResolveDestinationPathsTool,
    CopyAndVerifyFilesTool,
    CleanOriginalDirectoryTool,
    CalculateTotalSizeTool,
    VerifyRemoteChecksumTool,
    LogTaskCompletionTool,
    UpdateArchiveStatusTool,
    ParseArchiveInstructionsTool,
    ValidateFilesExistTool,
    CreateTarArchiveTool,
    TransferArchiveRsyncTool,
    DeleteSourceFilesTool,
]
