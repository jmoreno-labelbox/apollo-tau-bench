import json
from typing import Any

from domains.dto import Tool


class GetArchiveInstructionsByID(Tool):
    """Fetches a particular archival task using its ID from the instructions database."""

    @staticmethod
    def invoke(data: dict[str, Any], archive_id: str = None) -> str:
        for instruction in data.get("archive_instructions", []):
            if instruction.get("archive_id") == archive_id:
                payload = instruction
                out = json.dumps(payload)
                return out
        payload = {"error": f"Archive instruction with ID '{archive_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetArchiveInstructionsById",
                "description": "Fetches a specific archival task (e.g., files to include, destination) by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_id": {
                            "type": "string",
                            "description": "The unique ID of the archive task (e.g., 'arch_001').",
                        }
                    },
                    "required": ["archive_id"],
                },
            },
        }


class GetFileCheckTaskByID(Tool):
    """Fetches a specific file check task using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None) -> str:
        for task in data.get("file_check_db", []):
            if task.get("task_id") == task_id:
                payload = task
                out = json.dumps(payload)
                return out
        payload = {"error": f"File check task with ID '{task_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFileCheckTaskById",
                "description": "Fetches the full details and parsed instructions for a file check task by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The unique ID of the file check task (e.g., 'fc_task_001').",
                        }
                    },
                    "required": ["task_id"],
                },
            },
        }


class GetDirectoryOperationByID(Tool):
    """Fetches a file organization task (directory operation) using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], operation_id: str = None) -> str:
        for op in data.get("directories", []):
            if op.get("operation_id") == operation_id:
                payload = op
                out = json.dumps(payload)
                return out
        payload = {"error": f"Directory operation with ID '{operation_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDirectoryOperationById",
                "description": "Fetches the details for a file organization task, including source, destination, and file type mappings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "operation_id": {
                            "type": "string",
                            "description": "The unique ID of the directory operation (e.g., 'dir_op_001').",
                        }
                    },
                    "required": ["operation_id"],
                },
            },
        }


class GetServerStatusByHostname(Tool):
    """Verifies the status of a remote server (e.g., online, under maintenance)."""

    @staticmethod
    def invoke(data: dict[str, Any], hostname: str = None) -> str:
        for server in data.get("remote_servers", []):
            if server.get("hostname") == hostname:
                payload = {"hostname": hostname, "status": server.get("status")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Server with hostname '{hostname}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetServerStatusByHostname",
                "description": "Retrieves the current operational status of a server by its hostname.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {
                            "type": "string",
                            "description": "The fully qualified domain name of the server.",
                        }
                    },
                    "required": ["hostname"],
                },
            },
        }


class CheckRemoteDiskSpace(Tool):
    """Verifies the available disk space on the filesystem of a remote server."""

    @staticmethod
    def invoke(data: dict[str, Any], hostname: str = None) -> str:
        for server_resources in data.get("system_resources", []):
            if server_resources.get("hostname") == hostname:
                disk_info = server_resources.get("disk", {})
                payload = {
                    "hostname": hostname,
                    "available_gb": disk_info.get("available_gb"),
                    "total_gb": disk_info.get("total_gb"),
                    "usage_percent": disk_info.get("usage_percent"),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Resource information for server '{hostname}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckRemoteDiskSpace",
                "description": "Checks the available disk space on a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {
                            "type": "string",
                            "description": "The hostname of the server to check.",
                        }
                    },
                    "required": ["hostname"],
                },
            },
        }


class GetServerResourceUsage(Tool):
    """Fetches the real-time CPU, memory, and disk utilization of a server."""

    @staticmethod
    def invoke(data: dict[str, Any], hostname: str = None) -> str:
        for server in data.get("system_resources", []):
            if server.get("hostname") == hostname:
                payload = server
                out = json.dumps(payload)
                return out
        payload = {"error": f"Resource usage for server '{hostname}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetServerResourceUsage",
                "description": "Retrieves current CPU, memory, and disk usage for a specific server.",
                "parameters": {
                    "type": "object",
                    "properties": {"hostname": {"type": "string"}},
                    "required": ["hostname"],
                },
            },
        }


class GetSecurityPolicyByName(Tool):
    """Fetches a particular security policy using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], policy_name: str = None) -> str:
        for policy in data.get("security_policies", []):
            if policy.get("name") == policy_name:
                payload = policy
                out = json.dumps(payload)
                return out
        payload = {"error": f"Security policy named '{policy_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSecurityPolicyByName",
                "description": "Fetches an entire security policy document by its name (e.g., 'SSH Access Policy').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "policy_name": {
                            "type": "string",
                            "description": "The name of the security policy.",
                        }
                    },
                    "required": ["policy_name"],
                },
            },
        }


class GetUserInfoByID(Tool):
    """Fetches a user's profile, encompassing their role and permissions."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        for user in data.get("user_preferences", []):
            if user.get("user_id") == user_id:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": f"User with ID '{user_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserInfoById",
                "description": "Fetches user details like role and permissions using their unique user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user (e.g., 'user_001').",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class GetUserContactInfo(Tool):
    """Fetches a user's contact information (email, Slack) using their user ID."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        for contact in data.get("user_contacts", []):
            if contact.get("user_id") == user_id:
                payload = contact
                out = json.dumps(payload)
                return out
        payload = {"error": f"Contact info for user ID '{user_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserContactInfo",
                "description": "Fetches a user's contact details (email, Slack handle) for notifications.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class GetSshKeyByID(Tool):
    """Retrieves information for a specific SSH key, including the servers it is permitted on."""

    @staticmethod
    def invoke(data: dict[str, Any], key_id: str = None) -> str:
        for key in data.get("ssh_keys", []):
            if key.get("key_id") == key_id:
                payload = key
                out = json.dumps(payload)
                return out
        payload = {"error": f"SSH key with ID '{key_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSshKeyById",
                "description": "Retrieves details for a specific SSH key, including its list of authorized servers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "key_id": {
                            "type": "string",
                            "description": "The ID of the SSH key (e.g., 'alice_rsa_key').",
                        }
                    },
                    "required": ["key_id"],
                },
            },
        }


class GetUserDefaultSshKey(Tool):
    """Identifies a user's default SSH key ID based on their preferences."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        for user in data.get("user_preferences", []):
            if user.get("user_id") == user_id and "default_ssh_key" in user:
                payload = {"user_id": user_id, "default_ssh_key": user["default_ssh_key"]}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Default SSH key for user ID '{user_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserDefaultSshKey",
                "description": "Looks up the default SSH key associated with a user's profile.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class CheckRemoteFileExists(Tool):
    """Confirms the existence of a specific file on a designated remote server."""

    @staticmethod
    def invoke(data: dict[str, Any], hostname: str = None, filepath: str = None) -> str:
        for server in data.get("file_system", []):
            if server.get("hostname") == hostname:
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if (
                            f"{directory.get('path')}/{file.get('filename')}"
                            == filepath
                        ):
                            payload = {"exists": True, "file_details": file}
                            out = json.dumps(payload)
                            return out
        payload = {"exists": False}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckRemoteFileExists",
                "description": "Checks if a file exists at a specific path on a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {"type": "string"},
                        "filepath": {"type": "string"},
                    },
                    "required": ["hostname", "filepath"],
                },
            },
        }


class GetErrorLogDetails(Tool):
    """Fetches the comprehensive step-by-step log for a particular failed task."""

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None) -> str:
        for log in data.get("error_logs", []):
            if log.get("task_id") == task_id:
                payload = log
                out = json.dumps(payload)
                return out
        payload = {"error": f"No detailed error log found for task ID '{task_id}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetErrorLogDetails",
                "description": "Fetches the detailed step-by-step trace for a failed task to aid in debugging.",
                "parameters": {
                    "type": "object",
                    "properties": {"task_id": {"type": "string"}},
                    "required": ["task_id"],
                },
            },
        }


#==============================================================================
#2. Discovery and Search Tools
#==============================================================================


class FindPendingTasksByType(Tool):
    """Identifies all outstanding tasks of a given type (e.g., 'archive', 'file_check')."""

    @staticmethod
    def invoke(data: dict[str, Any], task_type: str = None) -> str:
        pending_tasks = []
        if task_type == "archive":
            db = data.get("archive_instructions", [])
            pending_tasks = [t for t in db if t.get("status") == "pending"]
        elif task_type == "file_check":
            db = data.get("file_check_db", [])
            pending_tasks = [t for t in db if not t.get("completed")]
        elif task_type == "file_organization":
            db = data.get("file_lists", [])
            op_ids = {f["operation_id"] for f in db if f.get("status") == "pending"}
            all_ops = data.get("directories", [])
            pending_tasks = [op for op in all_ops if op["operation_id"] in op_ids]
        payload = {"pending_tasks": pending_tasks, "count": len(pending_tasks)}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findPendingTasksByType",
                "description": "Scans the databases for all tasks of a specific type that are in a 'pending' state.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_type": {
                            "type": "string",
                            "enum": ["archive", "file_check", "file_organization"],
                        }
                    },
                    "required": ["task_type"],
                },
            },
        }


class GetFilesForDirectoryOperation(Tool):
    """Fetches the list of files designated for movement in a file organization task."""

    @staticmethod
    def invoke(data: dict[str, Any], operation_id: str = None) -> str:
        files = [
            f
            for f in data.get("file_lists", [])
            if f.get("operation_id") == operation_id
        ]
        payload = {"files": files, "count": len(files)}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFilesForDirectoryOperation",
                "description": "Retrieves the manifest of files associated with a specific file organization operation.",
                "parameters": {
                    "type": "object",
                    "properties": {"operation_id": {"type": "string"}},
                    "required": ["operation_id"],
                },
            },
        }


class GetLastSuccessfulTaskRun(Tool):
    """Identifies the log entry for the last successful completion of a task of a specific type."""

    @staticmethod
    def invoke(data: dict[str, Any], task_type: str = None) -> str:
        successful_runs = [
            log
            for log in data.get("task_logs", [])
            if log.get("task_type") == task_type and log.get("result") == "success"
        ]
        if not successful_runs:
            payload = {"error": f"No successful run found for type '{task_type}'."}
            out = json.dumps(payload)
            return out
        last_run = max(successful_runs, key=lambda x: x["completed_at"])
        payload = last_run
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLastSuccessfulTaskRun",
                "description": "Finds when a specific type of task last completed successfully.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_type": {
                            "type": "string",
                            "enum": ["archive", "file_check", "file_organization"],
                        }
                    },
                    "required": ["task_type"],
                },
            },
        }


#==============================================================================
#3. Action and Execution Tools
#==============================================================================


class ScanRemoteDirectory(Tool):
    """Examines a directory on a remote server and returns files that meet the criteria."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        directory: Any = None,
        directory_path: str = None,
        hostname: str = None
    ) -> str:
        # Support 'directory' as an alias for 'directory_path'
        if directory is not None:
            directory_path = directory
        found_files = []
        for server in data.get("file_system", []):
            if server.get("hostname") == hostname:
                for directory in server.get("directories", []):
                    if directory.get("path") == directory_path:
                        # This represents a basic simulation
                        found_files.extend(directory.get("files", []))
        payload = {"files_found": found_files, "count": len(found_files)}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ScanRemoteDirectory",
                "description": "Performs a scan of a remote directory to find files matching specific criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {"type": "string"},
                        "directory": {"type": "string"},
                        "last_access_days": {"type": "integer"},
                        "max_size_bytes": {"type": "integer"},
                        "owner": {"type": "string"},
                    },
                    "required": ["hostname", "directory"],
                },
            },
        }


class CreateDirectoryOnRemote(Tool):
    """Imitates the creation of a directory on a remote server."""

    @staticmethod
    def invoke(data: dict[str, Any], directory_path: str = None, hostname: str = None) -> str:
        payload = {
            "status": "success",
            "message": f"Directory '{directory_path}' created on {hostname}.",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDirectoryOnRemote",
                "description": "Creates a new directory at the specified path on a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {"type": "string"},
                        "directory_path": {"type": "string"},
                    },
                    "required": ["hostname", "directory_path"],
                },
            },
        }


class MoveFileOnRemote(Tool):
    """Imitates transferring a file from one location to another on the same remote server."""

    @staticmethod
    def invoke(data: dict[str, Any], source_path: str = None, destination_path: str = None, hostname: str = None) -> str:
        payload = {
            "status": "success",
            "message": f"Moved {source_path} to {destination_path} on {hostname}.",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MoveFileOnRemote",
                "description": "Moves a file on a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {"type": "string"},
                        "source_path": {"type": "string"},
                        "destination_path": {"type": "string"},
                    },
                    "required": ["hostname", "source_path", "destination_path"],
                },
            },
        }


class CreateArchiveOnRemote(Tool):
    """Imitates the creation of a compressed tarball (tar.gz) on a remote server."""

    @staticmethod
    def invoke(data: dict[str, Any], hostname: str = None, archive_path: str = None, files_to_include: list = None) -> str:
        file_count = len(files_to_include or [])
        payload = {
            "status": "success",
            "hostname": hostname,
            "archive_path": archive_path,
            "message": f"Successfully created archive '{archive_path}' with {file_count} files on {hostname}.",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateArchiveOnRemote",
                "description": "Creates a compressed tar.gz archive from a list of files on a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {"type": "string"},
                        "archive_path": {"type": "string"},
                        "files_to_include": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["hostname", "archive_path", "files_to_include"],
                },
            },
        }


class TransferFileToRemote(Tool):
    """Imitates the transfer of a file to a remote server, usually via SCP or rsync."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        destination_path: str = None,
        remote_address: str = None,
        source_path: str = None,
        ssh_key: Any = None
    ) -> str:
        payload = {
            "status": "success",
            "source_file": source_path,
            "destination": f"{remote_address}:{destination_path}",
            "checksum_verified": True,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TransferFileToRemote",
                "description": "Transfers a file from a source to a remote destination using a secure protocol.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_path": {"type": "string"},
                        "remote_address": {"type": "string"},
                        "destination_path": {"type": "string"},
                        "ssh_key": {"type": "string"},
                    },
                    "required": [
                        "source_path",
                        "remote_address",
                        "destination_path",
                        "ssh_key",
                    ],
                },
            },
        }


class DeleteFileOnRemote(Tool):
    """Imitates the removal of a file from a remote server."""

    @staticmethod
    def invoke(data: dict[str, Any], filepath: str = None, hostname: str = None) -> str:
        payload = {
            "status": "success",
            "message": f"Deleted {filepath} from {hostname}.",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteFileOnRemote",
                "description": "Deletes a specified file from a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {"type": "string"},
                        "filepath": {"type": "string"},
                    },
                    "required": ["hostname", "filepath"],
                },
            },
        }


class GetRemoteFileChecksum(Tool):
    """Computes the checksum (e.g., SHA256) for a file located on a remote server."""

    @staticmethod
    def invoke(data: dict[str, Any], hostname: str = None, filepath: str = None) -> str:
        for server in data.get("file_system", []):
            if server.get("hostname") == hostname:
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if (
                            f"{directory.get('path')}/{file.get('filename')}"
                            == filepath
                        ):
                            payload = {"filepath": filepath, "checksum": file.get("checksum")}
                            out = json.dumps(
                                payload)
                            return out
        payload = {"error": f"File '{filepath}' not found on '{hostname}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRemoteFileChecksum",
                "description": "Calculates and retrieves the checksum of a specific file on a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hostname": {"type": "string"},
                        "filepath": {"type": "string"},
                    },
                    "required": ["hostname", "filepath"],
                },
            },
        }


#==============================================================================
#4. State Management and Logging Tools
#==============================================================================


class UpdateArchiveTaskStatus(Tool):
    """Modifies the status of an archival task within the instructions database."""

    @staticmethod
    def invoke(data: dict[str, Any], archive_id: str = None, status: str = None) -> str:
        for instruction in data.get("archive_instructions", []):
            if instruction.get("archive_id") == archive_id:
                instruction["status"] = status
                payload = {"status": "success", "updated_task": instruction}
                out = json.dumps(payload)
                return out
        payload = {"status": "failure", "error": f"Archive ID '{archive_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateArchiveTaskStatus",
                "description": "Updates the status of an archive task (e.g., 'in_progress', 'completed', 'failed').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_id": {"type": "string"},
                        "status": {
                            "type": "string",
                            "enum": ["in_progress", "completed", "failed", "verified"],
                        },
                    },
                    "required": ["archive_id", "status"],
                },
            },
        }


class UpdateFileCheckTaskStatus(Tool):
    """Modifies the status of a file check task."""

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, completed: bool = None) -> str:
        for task in data.get("file_check_db", []):
            if task.get("task_id") == task_id:
                task["completed"] = completed
                payload = {"status": "success", "updated_task": task}
                out = json.dumps(payload)
                return out
        payload = {"status": "failure", "error": f"File check task ID '{task_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFileCheckTaskStatus",
                "description": "Updates the completion status of a file check task.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "completed": {"type": "boolean"},
                    },
                    "required": ["task_id", "completed"],
                },
            },
        }


class UpdateDirectoryOperationStatus(Tool):
    """Modifies the status of an individual file within a file organization task."""

    @staticmethod
    def invoke(data: dict[str, Any], file_id: str = None, status: str = None) -> str:
        for file in data.get("file_lists", []):
            if file.get("file_id") == file_id:
                file["status"] = status
                payload = {"status": "success", "updated_file": file}
                out = json.dumps(payload)
                return out
        payload = {
                "status": "failure",
                "error": f"File ID '{file_id}' not found in any directory operation.",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDirectoryOperationStatus",
                "description": "Updates the status of an individual file within a file organization task.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_id": {"type": "string"},
                        "status": {
                            "type": "string",
                            "enum": ["completed", "failed", "in_progress"],
                        },
                    },
                    "required": ["file_id", "status"],
                },
            },
        }


class LogErrorMessage(Tool):
    """Generates a structured log of error messages for a failed task."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        error_type: str = None,
        task_type: str = None,
        task_id: str = None,
        user_id: str = None,
        severity: str = None,
        details_json: str = None
    ) -> str:
        error_logs = data.get("error_messages", [])
        new_id = f"err_msg_{max((int(e['msg_id'].split('_')[-1]) for e in error_logs), default=0) + 1:03d}"

        # Automatically create a message according to the error type and task specifics
        # Create a suitable message depending on the error type
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
            "msg_id": new_id,
            "err_type": error_type,
            "task_id": task_id,
            "task_type": task_type,
            "user_id": user_id,
            "msg": message,
            "created_at": "2024-01-20T12:00:00Z",
            "severity": severity,
            "details": details_json,
        }
        error_logs.append(new_log)
        data["error_messages"] = error_logs
        payload = new_log
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogErrorMessage",
                "description": "Logs a structured error message for auditing and alerting purposes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "task_type": {"type": "string"},
                        "user_id": {"type": "string"},
                        "error_type": {"type": "string"},
                        "severity": {
                            "type": "string",
                            "enum": ["low", "medium", "high", "critical"],
                        },
                        "details_json": {"type": "object"},
                    },
                    "required": [
                        "task_id",
                        "task_type",
                        "user_id",
                        "error_type",
                        "severity",
                    ],
                },
            },
        }


class LogTaskCompletion(Tool):
    """Generates a log entry for a task that has been successfully completed."""

    @staticmethod
    def invoke(data: dict[str, Any], task_type: str = None, task_id: str = None, user_id: str = None) -> str:
        task_logs = data.get("task_logs", [])

        # Automatically create notes according to the type of task
        if task_type == "archive":
            notes = f"Archive task {task_id} completed successfully"
        elif task_type == "file_check":
            notes = f"File check task {task_id} completed successfully"
        elif task_type == "file_organization":
            notes = f"File organization task {task_id} completed successfully"
        else:
            notes = f"{task_type.title()} task {task_id} completed successfully"

        new_log = {
            "task_id": task_id,
            "task_type": task_type,
            "user_id": user_id,
            "result": "success",
            "completed_at": "2024-01-20T13:00:00Z",
            "notes": notes,
        }
        task_logs.append(new_log)
        data["task_logs"] = task_logs
        payload = new_log
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogTaskCompletion",
                "description": "Writes a record to the main task log for a successfully completed task.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "task_type": {"type": "string"},
                        "user_id": {"type": "string"},
                    },
                    "required": ["task_id", "task_type", "user_id"],
                },
            },
        }


#==============================================================================
#5. Communication Resources
#==============================================================================


class SendSlackMessage(Tool):
    """Delivers a message to a designated Slack channel."""

    @staticmethod
    def invoke(data: dict[str, Any], channel_name: str = None, message: str = None) -> str:
        messages = data.get("slack_messages", [])
        new_id = f"msg_{max((int(m['message_id'].split('_')[-1]) for m in messages), default=0) + 1:03d}"

        # Automatically create a relevant message based on the channel name
        if channel_name == "System Alerts":
            message = (
                f"System alert notification sent to {channel_name} channel at {new_id}"
            )
        elif channel_name == "Operations":
            message = f"Operations update sent to {channel_name} channel at {new_id}"
        elif channel_name == "File Check":
            message = (
                f"File check notification sent to {channel_name} channel at {new_id}"
            )
        else:
            message = (
                f"Automated notification sent to {channel_name} channel at {new_id}"
            )

        channel_id = ""
        for channel in data.get("slack_channels", []):
            if channel.get("name") == channel_name:
                channel_id = channel.get("channel_id")
                break
        if not channel_id:
            payload = {"error": f"Channel '{channel_name}' not found."}
            out = json.dumps(payload)
            return out

        new_message = {
            "message_id": new_id,
            "channel_id": channel_id,
            "user_id": "system_agent",
            "username": "AutomationAgent",
            "message": message,
            "timestamp": "2024-01-20T14:00:00Z",
            "type": "notification",
        }
        messages.append(new_message)
        data["slack_messages"] = messages
        payload = new_message
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendSlackMessage",
                "description": "Posts an automatically generated message to a Slack channel for notifications and alerts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel_name": {
                            "type": "string",
                            "description": "The name of the public channel (e.g., 'System Alerts', 'Operations', 'File Check').",
                        }
                    },
                    "required": ["channel_name"],
                },
            },
        }


TOOLS = [
    #Information and Validation
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
    #Discovery and Search
    FindPendingTasksByType(),
    GetFilesForDirectoryOperation(),
    GetLastSuccessfulTaskRun(),
    #Action and Execution
    ScanRemoteDirectory(),
    CreateDirectoryOnRemote(),
    MoveFileOnRemote(),
    CreateArchiveOnRemote(),
    TransferFileToRemote(),
    DeleteFileOnRemote(),
    GetRemoteFileChecksum(),
    #State Management and Logging
    UpdateArchiveTaskStatus(),
    UpdateFileCheckTaskStatus(),
    UpdateDirectoryOperationStatus(),
    LogErrorMessage(),
    LogTaskCompletion(),
    #Communication
    SendSlackMessage(),
]
