import json
from typing import Any, Dict, List, Optional
from domains.dto import Tool

class GetArchiveInstructionsByID(Tool):
    """Retrieves a specific archival task by its ID from the instructions database."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        archive_id = kwargs.get("archive_id")
        for instruction in data.get('archive_instructions', []):
            if instruction.get('archive_id') == archive_id:
                return json.dumps(instruction)
        return json.dumps({"error": f"Archive instruction with ID '{archive_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_archive_instructions_by_id", "description": "Fetches a specific archival task (e.g., files to include, destination) by its unique ID.", "parameters": {"type": "object", "properties": {"archive_id": {"type": "string", "description": "The unique ID of the archive task (e.g., 'arch_001')."}}, "required": ["archive_id"]}}}

class GetFileCheckTaskByID(Tool):
    """Retrieves a specific file check task by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_id = kwargs.get("task_id")
        for task in data.get('file_check_db', []):
            if task.get('task_id') == task_id:
                return json.dumps(task)
        return json.dumps({"error": f"File check task with ID '{task_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_file_check_task_by_id", "description": "Fetches the full details and parsed instructions for a file check task by its ID.", "parameters": {"type": "object", "properties": {"task_id": {"type": "string", "description": "The unique ID of the file check task (e.g., 'fc_task_001')."}}, "required": ["task_id"]}}}

class GetDirectoryOperationByID(Tool):
    """Retrieves a file organization (directory operation) task by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        operation_id = kwargs.get("operation_id")
        for op in data.get('directories', []):
            if op.get('operation_id') == operation_id:
                return json.dumps(op)
        return json.dumps({"error": f"Directory operation with ID '{operation_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_directory_operation_by_id", "description": "Fetches the details for a file organization task, including source, destination, and file type mappings.", "parameters": {"type": "object", "properties": {"operation_id": {"type": "string", "description": "The unique ID of the directory operation (e.g., 'dir_op_001')."}}, "required": ["operation_id"]}}}

class GetServerStatusByHostname(Tool):
    """Checks the status of a remote server (e.g., online, maintenance)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hostname = kwargs.get("hostname")
        for server in data.get('remote_servers', []):
            if server.get('hostname') == hostname:
                return json.dumps({"hostname": hostname, "status": server.get("status")})
        return json.dumps({"error": f"Server with hostname '{hostname}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_server_status_by_hostname", "description": "Retrieves the current operational status of a server by its hostname.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string", "description": "The fully qualified domain name of the server."}}, "required": ["hostname"]}}}

class CheckRemoteDiskSpace(Tool):
    """Checks the available disk space on a remote server's filesystem."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hostname = kwargs.get("hostname")
        for server_resources in data.get('system_resources', []):
            if server_resources.get('hostname') == hostname:
                disk_info = server_resources.get('disk', {})
                return json.dumps({
                    "hostname": hostname, "available_gb": disk_info.get("available_gb"), "total_gb": disk_info.get("total_gb"), "usage_percent": disk_info.get("usage_percent")})
        return json.dumps({"error": f"Resource information for server '{hostname}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "check_remote_disk_space", "description": "Checks the available disk space on a remote server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string", "description": "The hostname of the server to check."}}, "required": ["hostname"]}}}

class GetServerResourceUsage(Tool):
    """Retrieves a server's real-time CPU, memory, and disk usage."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hostname = kwargs.get("hostname")
        for server in data.get('system_resources', []):
            if server.get('hostname') == hostname:
                return json.dumps(server)
        return json.dumps({"error": f"Resource usage for server '{hostname}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_server_resource_usage", "description": "Retrieves current CPU, memory, and disk usage for a specific server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}}, "required": ["hostname"]}}}

class GetSecurityPolicyByName(Tool):
    """Retrieves a specific security policy by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        policy_name = kwargs.get("policy_name")
        for policy in data.get('security_policies', []):
            if policy.get('name') == policy_name:
                return json.dumps(policy)
        return json.dumps({"error": f"Security policy named '{policy_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_security_policy_by_name", "description": "Fetches an entire security policy document by its name (e.g., 'SSH Access Policy').", "parameters": {"type": "object", "properties": {"policy_name": {"type": "string", "description": "The name of the security policy."}}, "required": ["policy_name"]}}}

class GetUserInfoByID(Tool):
    """Retrieves a user's profile, including their role and permissions."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        for user in data.get('user_preferences', []):
            if user.get('user_id') == user_id:
                return json.dumps(user)
        return json.dumps({"error": f"User with ID '{user_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_user_info_by_id", "description": "Fetches user details like role and permissions using their unique user ID.", "parameters": {"type": "object", "properties": {"user_id": {"type": "string", "description": "The unique ID of the user (e.g., 'user_001')."}}, "required": ["user_id"]}}}

class GetUserContactInfo(Tool):
    """Retrieves a user's contact details (email, Slack) by their user ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        for contact in data.get('user_contacts', []):
            if contact.get('user_id') == user_id:
                return json.dumps(contact)
        return json.dumps({"error": f"Contact info for user ID '{user_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_user_contact_info", "description": "Fetches a user's contact details (email, Slack handle) for notifications.", "parameters": {"type": "object", "properties": {"user_id": {"type": "string"}}, "required": ["user_id"]}}}

class GetSshKeyByID(Tool):
    """Fetches details for a specific SSH key, including which servers it is authorized on."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        key_id = kwargs.get("key_id")
        for key in data.get('ssh_keys', []):
            if key.get('key_id') == key_id:
                return json.dumps(key)
        return json.dumps({"error": f"SSH key with ID '{key_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_ssh_key_by_id", "description": "Retrieves details for a specific SSH key, including its list of authorized servers.", "parameters": {"type": "object", "properties": {"key_id": {"type": "string", "description": "The ID of the SSH key (e.g., 'alice_rsa_key')."}}, "required": ["key_id"]}}}

class GetUserDefaultSshKey(Tool):
    """Finds a user's default SSH key ID from their preferences."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        for user in data.get('user_preferences', []):
            if user.get('user_id') == user_id and 'default_ssh_key' in user:
                return json.dumps({"user_id": user_id, "default_ssh_key": user['default_ssh_key']})
        return json.dumps({"error": f"Default SSH key for user ID '{user_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_user_default_ssh_key", "description": "Looks up the default SSH key associated with a user's profile.", "parameters": {"type": "object", "properties": {"user_id": {"type": "string"}}, "required": ["user_id"]}}}

class CheckRemoteFileExists(Tool):
    """Verifies that a specific file exists on a given remote server."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hostname = kwargs.get("hostname")
        filepath = kwargs.get("filepath")
        for server in data.get('file_system', []):
            if server.get('hostname') == hostname:
                for directory in server.get('directories', []):
                    for file in directory.get('files', []):
                        if f"{directory.get('path')}/{file.get('filename')}" == filepath:
                             return json.dumps({"exists": True, "file_details": file})
        return json.dumps({"exists": False})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "check_remote_file_exists", "description": "Checks if a file exists at a specific path on a remote server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}, "filepath": {"type": "string"}}, "required": ["hostname", "filepath"]}}}

class GetErrorLogDetails(Tool):
    """Retrieves the detailed step-by-step log for a specific failed task."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_id = kwargs.get("task_id")
        for log in data.get('error_logs', []):
            if log.get('task_id') == task_id:
                return json.dumps(log)
        return json.dumps({"error": f"No detailed error log found for task ID '{task_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_error_log_details", "description": "Fetches the detailed step-by-step trace for a failed task to aid in debugging.", "parameters": {"type": "object", "properties": {"task_id": {"type": "string"}}, "required": ["task_id"]}}}

# ==============================================================================
# 2. Discovery & Search Tools
# ==============================================================================

class FindPendingTasksByType(Tool):
    """Finds all pending tasks of a specified type (e.g., 'archive', 'file_check')."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_type = kwargs.get("task_type")
        pending_tasks = []
        if task_type == 'archive':
            db = data.get('archive_instructions', [])
            pending_tasks = [t for t in db if t.get('status') == 'pending']
        elif task_type == 'file_check':
            db = data.get('file_check_db', [])
            pending_tasks = [t for t in db if not t.get('completed')]
        elif task_type == 'file_organization':
            db = data.get('file_lists', [])
            op_ids = {f['operation_id'] for f in db if f.get('status') == 'pending'}
            all_ops = data.get('directories', [])
            pending_tasks = [op for op in all_ops if op['operation_id'] in op_ids]

        return json.dumps({"pending_tasks": pending_tasks, "count": len(pending_tasks)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_pending_tasks_by_type", "description": "Scans the databases for all tasks of a specific type that are in a 'pending' state.", "parameters": {"type": "object", "properties": {"task_type": {"type": "string", "enum": ["archive", "file_check", "file_organization"]}}, "required": ["task_type"]}}}

class GetFilesForDirectoryOperation(Tool):
    """Retrieves the list of files to be moved for a file organization task."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        operation_id = kwargs.get("operation_id")
        files = [f for f in data.get('file_lists', []) if f.get('operation_id') == operation_id]
        return json.dumps({"files": files, "count": len(files)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_files_for_directory_operation", "description": "Retrieves the manifest of files associated with a specific file organization operation.", "parameters": {"type": "object", "properties": {"operation_id": {"type": "string"}}, "required": ["operation_id"]}}}

class GetLastSuccessfulTaskRun(Tool):
    """Finds the log of the last time a task of a certain type completed successfully."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_type = kwargs.get("task_type")
        successful_runs = [log for log in data.get('task_logs', []) if log.get('task_type') == task_type and log.get('result') == 'success']
        if not successful_runs:
            return json.dumps({"error": f"No successful run found for type '{task_type}'."})
        last_run = max(successful_runs, key=lambda x: x['completed_at'])
        return json.dumps(last_run)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_last_successful_task_run", "description": "Finds when a specific type of task last completed successfully.", "parameters": {"type": "object", "properties": {"task_type": {"type": "string", "enum": ["archive", "file_check", "file_organization"]}}, "required": ["task_type"]}}}

# ==============================================================================
# 3. Action & Execution Tools
# ==============================================================================

class ScanRemoteDirectory(Tool):
    """Scans a directory on a remote server and returns files matching the criteria."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hostname = kwargs.get("hostname")
        directory_path = kwargs.get("directory")
        found_files = []
        for server in data.get('file_system', []):
            if server.get('hostname') == hostname:
                for directory in server.get('directories', []):
                    if directory.get('path') == directory_path:
                        # This is a simplified simulation
                        found_files.extend(directory.get('files', []))
        return json.dumps({"files_found": found_files, "count": len(found_files)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "scan_remote_directory", "description": "Performs a scan of a remote directory to find files matching specific criteria.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}, "directory": {"type": "string"}, "last_access_days": {"type": "integer"}, "max_size_bytes": {"type": "integer"}, "owner": {"type": "string"}}, "required": ["hostname", "directory"]}}}

class CreateDirectoryOnRemote(Tool):
    """Simulates creating a directory on a remote server."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({
            "status": "success", "message": f"Directory '{kwargs.get('directory_path')}' created on {kwargs.get('hostname')}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_directory_on_remote", "description": "Creates a new directory at the specified path on a remote server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}, "directory_path": {"type": "string"}}, "required": ["hostname", "directory_path"]}}}

class MoveFileOnRemote(Tool):
    """Simulates moving a file from a source to a destination on the same remote server."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({
            "status": "success", "message": f"Moved {kwargs.get('source_path')} to {kwargs.get('destination_path')} on {kwargs.get('hostname')}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "move_file_on_remote", "description": "Moves a file on a remote server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}, "source_path": {"type": "string"}, "destination_path": {"type": "string"}}, "required": ["hostname", "source_path", "destination_path"]}}}

class CreateArchiveOnRemote(Tool):
    """Simulates creating a compressed tarball (tar.gz) on a remote server."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hostname = kwargs.get("hostname")
        archive_path = kwargs.get("archive_path")
        file_count = len(kwargs.get("files_to_include", []))
        return json.dumps({
            "status": "success", "hostname": hostname, "archive_path": archive_path, "message": f"Successfully created archive '{archive_path}' with {file_count} files on {hostname}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_archive_on_remote", "description": "Creates a compressed tar.gz archive from a list of files on a remote server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}, "archive_path": {"type": "string"}, "files_to_include": {"type": "array", "items": {"type": "string"}}}, "required": ["hostname", "archive_path", "files_to_include"]}}}

class TransferFileToRemote(Tool):
    """Simulates transferring a file to a remote server, typically using SCP or rsync."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({
            "status": "success", "source_file": kwargs.get("source_path"), "destination": f"{kwargs.get('remote_address')}:{kwargs.get('destination_path')}", "checksum_verified": True})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "transfer_file_to_remote", "description": "Transfers a file from a source to a remote destination using a secure protocol.", "parameters": {"type": "object", "properties": {"source_path": {"type": "string"}, "remote_address": {"type": "string"}, "destination_path": {"type": "string"}, "ssh_key": {"type": "string"}}, "required": ["source_path", "remote_address", "destination_path", "ssh_key"]}}}

class DeleteFileOnRemote(Tool):
    """Simulates deleting a file from a remote server."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({
            "status": "success", "message": f"Deleted {kwargs.get('filepath')} from {kwargs.get('hostname')}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "delete_file_on_remote", "description": "Deletes a specified file from a remote server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}, "filepath": {"type": "string"}}, "required": ["hostname", "filepath"]}}}

class GetRemoteFileChecksum(Tool):
    """Calculates the checksum (e.g., SHA256) of a file on a remote server."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hostname = kwargs.get("hostname")
        filepath = kwargs.get("filepath")
        for server in data.get('file_system', []):
            if server.get('hostname') == hostname:
                for directory in server.get('directories', []):
                    for file in directory.get('files', []):
                        if f"{directory.get('path')}/{file.get('filename')}" == filepath:
                             return json.dumps({"filepath": filepath, "checksum": file.get("checksum")})
        return json.dumps({"error": f"File '{filepath}' not found on '{hostname}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_remote_file_checksum", "description": "Calculates and retrieves the checksum of a specific file on a remote server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}, "filepath": {"type": "string"}}, "required": ["hostname", "filepath"]}}}

# ==============================================================================
# 4. State Management & Logging Tools
# ==============================================================================

class UpdateArchiveTaskStatus(Tool):
    """Updates the status of an archive task in the instructions database."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        archive_id = kwargs.get("archive_id")
        new_status = kwargs.get("status")
        for instruction in data.get('archive_instructions', []):
            if instruction.get('archive_id') == archive_id:
                instruction['status'] = new_status
                return json.dumps({"status": "success", "updated_task": instruction})
        return json.dumps({"status": "failure", "error": f"Archive ID '{archive_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_archive_task_status", "description": "Updates the status of an archive task (e.g., 'in_progress', 'completed', 'failed').", "parameters": {"type": "object", "properties": {"archive_id": {"type": "string"}, "status": {"type": "string", "enum": ["in_progress", "completed", "failed", "verified"]}}, "required": ["archive_id", "status"]}}}

class UpdateFileCheckTaskStatus(Tool):
    """Updates the status of a file check task."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_id = kwargs.get("task_id")
        is_completed = kwargs.get("completed")
        for task in data.get('file_check_db', []):
            if task.get('task_id') == task_id:
                task['completed'] = is_completed
                return json.dumps({"status": "success", "updated_task": task})
        return json.dumps({"status": "failure", "error": f"File check task ID '{task_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_file_check_task_status", "description": "Updates the completion status of a file check task.", "parameters": {"type": "object", "properties": {"task_id": {"type": "string"}, "completed": {"type": "boolean"}}, "required": ["task_id", "completed"]}}}

class UpdateDirectoryOperationStatus(Tool):
    """Updates the status of a single file in a file organization task."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_id = kwargs.get("file_id")
        new_status = kwargs.get("status")
        for file in data.get('file_lists', []):
            if file.get('file_id') == file_id:
                file['status'] = new_status
                return json.dumps({"status": "success", "updated_file": file})
        return json.dumps({"status": "failure", "error": f"File ID '{file_id}' not found in any directory operation."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_directory_operation_status", "description": "Updates the status of an individual file within a file organization task.", "parameters": {"type": "object", "properties": {"file_id": {"type": "string"}, "status": {"type": "string", "enum": ["completed", "failed", "in_progress"]}}, "required": ["file_id", "status"]}}}

class LogErrorMessage(Tool):
    """Creates a structured error message log for a failed task."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        error_logs = data.get('error_messages', [])
        new_id = f"err_msg_{max((int(e['msg_id'].split('_')[-1]) for e in error_logs), default=0) + 1:03d}"

        # Automatically generate message based on error type and task details
        error_type = kwargs.get("error_type")
        task_type = kwargs.get("task_type")
        task_id = kwargs.get("task_id")

        # Generate appropriate message based on error type
        if error_type == "permission_denied":
            message = f"Permission denied while executing {task_type} task {task_id}"
        elif error_type == "file_not_found":
            message = f"Required file not found during {task_type} task {task_id}"
        elif error_type == "network_error":
            message = f"Network connection failed during {task_type} task {task_id}"
        elif error_type == "timeout":
            message = f"Operation timed out during {task_type} task {task_id}"
        elif error_type == "validation_failed":
            message = f"Data validation failed for {task_type} task {task_id}"
        else:
            message = f"Error occurred during {task_type} task {task_id}: {error_type}"

        new_log = {
            "msg_id": new_id, "err_type": error_type, "task_id": task_id, "task_type": task_type, "user_id": kwargs.get("user_id"), "msg": message, "created_at": "2024-01-20T12:00:00Z", "severity": kwargs.get("severity"), "details": kwargs.get("details_json")}
        error_logs.append(new_log)
        data['error_messages'] = error_logs
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "log_error_message", "description": "Logs a structured error message for auditing and alerting purposes.", "parameters": {"type": "object", "properties": {"task_id": {"type": "string"}, "task_type": {"type": "string"}, "user_id": {"type": "string"}, "error_type": {"type": "string"}, "severity": {"type": "string", "enum": ["low", "medium", "high", "critical"]}, "details_json": {"type": "object"}}, "required": ["task_id", "task_type", "user_id", "error_type", "severity"]}}}

class LogTaskCompletion(Tool):
    """Creates a log entry for a successfully completed task."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_logs = data.get('task_logs', [])

        # Automatically generate notes based on task type
        task_type = kwargs.get("task_type")
        task_id = kwargs.get("task_id")

        if task_type == "archive":
            notes = f"Archive task {task_id} completed successfully"
        elif task_type == "file_check":
            notes = f"File check task {task_id} completed successfully"
        elif task_type == "file_organization":
            notes = f"File organization task {task_id} completed successfully"
        else:
            notes = f"{task_type.title()} task {task_id} completed successfully"

        new_log = {
            "task_id": task_id, "task_type": task_type, "user_id": kwargs.get("user_id"), "result": "success", "completed_at": "2024-01-20T13:00:00Z", "notes": notes}
        task_logs.append(new_log)
        data['task_logs'] = task_logs
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "log_task_completion", "description": "Writes a record to the main task log for a successfully completed task.", "parameters": {"type": "object", "properties": {"task_id": {"type": "string"}, "task_type": {"type": "string"}, "user_id": {"type": "string"}}, "required": ["task_id", "task_type", "user_id"]}}}

# ==============================================================================
# 5. Communication Tools
# ==============================================================================

class SendSlackMessage(Tool):
    """Sends a message to a specified Slack channel."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        messages = data.get('slack_messages', [])
        new_id = f"msg_{max((int(m['message_id'].split('_')[-1]) for m in messages), default=0) + 1:03d}"
        channel_name = kwargs.get("channel_name")

        # Automatically generate appropriate message based on channel name
        if channel_name == "System Alerts":
            message = f"System alert notification sent to {channel_name} channel at {new_id}"
        elif channel_name == "Operations":
            message = f"Operations update sent to {channel_name} channel at {new_id}"
        elif channel_name == "File Check":
            message = f"File check notification sent to {channel_name} channel at {new_id}"
        else:
            message = f"Automated notification sent to {channel_name} channel at {new_id}"

        channel_id = ""
        for channel in data.get('slack_channels', []):
            if channel.get('name') == channel_name:
                channel_id = channel.get("channel_id")
                break
        if not channel_id:
            return json.dumps({"error": f"Channel '{channel_name}' not found."})

        new_message = {
            "message_id": new_id, "channel_id": channel_id, "user_id": "system_agent", "username": "AutomationAgent", "message": message, "timestamp": "2024-01-20T14:00:00Z", "type": "notification"}
        messages.append(new_message)
        data['slack_messages'] = messages
        return json.dumps(new_message)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "send_slack_message", "description": "Posts an automatically generated message to a Slack channel for notifications and alerts.", "parameters": {"type": "object", "properties": {"channel_name": {"type": "string", "description": "The name of the public channel (e.g., 'System Alerts', 'Operations', 'File Check')."}}, "required": ["channel_name"]}}}


TOOLS = [
    # Information & Validation
    GetArchiveInstructionsByID(),
    GetFileCheckTaskByID(),
    GetDirectoryOperationByID(),
    GetServerStatusByHostname(),
    CheckRemoteDiskSpace(),
    GetServerResourceUsage(),
    GetSecurityPolicyByName(),
    GetUserInfoByID(),
    GetUserContactInfo(),
    GetSshKeyByID(),
    GetUserDefaultSshKey(),
    CheckRemoteFileExists(),
    GetErrorLogDetails(),
    # Discovery & Search
    FindPendingTasksByType(),
    GetFilesForDirectoryOperation(),
    GetLastSuccessfulTaskRun(),
    # Action & Execution
    ScanRemoteDirectory(),
    CreateDirectoryOnRemote(),
    MoveFileOnRemote(),
    CreateArchiveOnRemote(),
    TransferFileToRemote(),
    DeleteFileOnRemote(),
    GetRemoteFileChecksum(),
    # State Management & Logging
    UpdateArchiveTaskStatus(),
    UpdateFileCheckTaskStatus(),
    UpdateDirectoryOperationStatus(),
    LogErrorMessage(),
    LogTaskCompletion(),
    # Communication
    SendSlackMessage(),
]
