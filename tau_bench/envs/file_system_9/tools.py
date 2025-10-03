import json
from typing import Any

from tau_bench.envs.tool import Tool


class GetFileMetadata(Tool):
    """Obtains metadata for a particular file on a designated server."""

    @staticmethod
    def invoke(data: dict[str, Any], filepath: str = None, server_hostname: str = None) -> str:
        for server in data.get("file_system", []):
            if server.get("hostname") == server_hostname:
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if (
                            f"{directory.get('path')}/{file.get('filename')}"
                            == filepath
                        ):
                            payload = file
                            out = json.dumps(payload)
                            return out
                payload = {"error": f"File not found: {filepath} on server {server_hostname}"}
                out = json.dumps(
                    payload)
                return out
        payload = {"error": f"Server not found: {server_hostname}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFileMetadata",
                "description": "Retrieves metadata for a specific file on a specific server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filepath": {
                            "type": "string",
                            "description": "The full path to the file.",
                        },
                        "server_hostname": {
                            "type": "string",
                            "description": "The hostname of the server where the file is located.",
                        },
                    },
                    "required": ["filepath", "server_hostname"],
                },
            },
        }


class GetLastAccessTime(Tool):
    """Fetches the last access timestamp for a particular file on a specified server."""

    @staticmethod
    def invoke(data: dict[str, Any], filepath: str = None, server_hostname: str = None) -> str:
        for server in data.get("file_system", []):
            if server.get("hostname") == server_hostname:
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if (
                            f"{directory.get('path')}/{file.get('filename')}"
                            == filepath
                        ):
                            payload = {"last_accessed": file.get("last_accessed")}
                            out = json.dumps(
                                payload)
                            return out
                payload = {"error": f"File not found: {filepath} on server {server_hostname}"}
                out = json.dumps(
                    payload)
                return out
        payload = {"error": f"Server not found: {server_hostname}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLastAccessTime",
                "description": "Retrieves the last access timestamp for a specific file on a specific server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filepath": {
                            "type": "string",
                            "description": "The full path to the file.",
                        },
                        "server_hostname": {
                            "type": "string",
                            "description": "The hostname of the server where the file is located.",
                        },
                    },
                    "required": ["filepath", "server_hostname"],
                },
            },
        }


class GetLastAccessedFile(Tool):
    """Acquires the file that was accessed most recently on a specific server."""

    @staticmethod
    def invoke(data: dict[str, Any], server_hostname: str = None) -> str:
        latest_file_path = None
        latest_timestamp = (
            "1970-01-01T00:00:00Z"  # Set up with an ancient timestamp
        )

        server_found = False
        for server in data.get("file_system", []):
            if server.get("hostname") == server_hostname:
                server_found = True
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if file.get("last_accessed") > latest_timestamp:
                            latest_timestamp = file.get("last_accessed")
                            latest_file_path = (
                                f"{directory.get('path')}/{file.get('filename')}"
                            )
                break  # Cease operation upon locating the server

        if not server_found:
            payload = {"error": f"Server not found: {server_hostname}"}
            out = json.dumps(payload)
            return out

        if not latest_file_path:
            payload = {
                "message": f"No files with access times found on server {server_hostname}."
            }
            out = json.dumps(payload)
            return out
        payload = {"filepath": latest_file_path, "last_accessed": latest_timestamp}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLastAccessedFile",
                "description": "Gets the most recently accessed file on a specific server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_hostname": {
                            "type": "string",
                            "description": "The hostname of the server to check.",
                        }
                    },
                    "required": ["server_hostname"],
                },
            },
        }


class FindFiles(Tool):
    """Locates files on a server according to defined criteria."""

    @staticmethod
    def invoke(data: dict[str, Any], server_hostname: str = None, search_path: str = None) -> str:
        found_files = []
        for server in data.get("file_system", []):
            if server.get("hostname") == server_hostname:
                for directory in server.get("directories", []):
                    if directory.get("path").startswith(search_path):
                        for file in directory.get("files", []):
                            found_files.append(
                                f"{directory.get('path')}/{file.get('filename')}"
                            )
        payload = {"files": found_files}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindFiles",
                "description": "Finds files on a server based on specified criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_hostname": {
                            "type": "string",
                            "description": "The hostname of the server to search.",
                        },
                        "search_path": {
                            "type": "string",
                            "description": "The directory path to start the search from.",
                        },
                    },
                    "required": ["server_hostname", "search_path"],
                },
            },
        }


class CheckDiskSpace(Tool):
    """Assesses the free disk space on a server."""

    @staticmethod
    def invoke(data: dict[str, Any], server_hostname: str = None) -> str:
        for server in data.get("system_resources", []):
            if server.get("hostname") == server_hostname:
                payload = server.get("disk")
                out = json.dumps(payload)
                return out
        payload = {"error": f"Server not found: {server_hostname}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckDiskSpace",
                "description": "Checks the available disk space on a server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_hostname": {
                            "type": "string",
                            "description": "The hostname of the server to check.",
                        }
                    },
                    "required": ["server_hostname"],
                },
            },
        }


class CreateArchive(Tool):
    """Generates a new archive instruction along with a simulated archive file in the file_system.json state."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        destination_directory: str,
        archive_name: str,
        user_id: str = None,
        remote_address: str = None,
        filepaths: list[str] = None
    ) -> str:
        # Step 1: Generate the instruction in archive_instructions.json
        archive_instructions = data.get("archive_instructions", [])
        max_id = 0
        if archive_instructions:
            for instruction in archive_instructions:
                try:
                    current_id_num = int(
                        instruction.get("archive_id", "arch_000").split("_")[1]
                    )
                    if current_id_num > max_id:
                        max_id = current_id_num
                except (IndexError, ValueError):
                    continue
        new_id_num = max_id + 1
        archive_id = f"arch_{new_id_num:03d}"

        archive_path = f"{destination_directory}/{archive_name}.tar.gz"

        new_archive_instruction = {
            "archive_id": archive_id,
            "user_id": user_id,
            "destination_directory": destination_directory,
            "remote_address": remote_address,
            "archive_name": archive_name,
            "filepaths": filepaths,
            "status": "pending",
        }
        data["archive_instructions"].append(new_archive_instruction)

        # Step 2: Generate the simulated file in file_system.json
        if not filepaths:
            payload = {"error": "No filepaths provided for archive creation."}
            out = json.dumps(payload)
            return out

        # Locate the server and determine the size based on the source files
        source_server = None
        total_size = 0
        for path in filepaths:
            file_found = False
            for server in data.get("file_system", []):
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if f"{directory.get('path')}/{file.get('filename')}" == path:
                            source_server = server
                            total_size += int(file.get("size", 0))
                            file_found = True
                            break
                    if file_found and source_server:
                        break
                if file_found and source_server:
                    break

        if not source_server:
            payload = {"error": f"Could not find the source server for files: {filepaths}"}
            out = json.dumps(payload)
            return out

        archive_size = int(total_size * 0.8)  # Emulate 80% compression
        archive_checksum = "a1f2e3d4c5b6789012345678901234567890abcd"
        new_archive_file = {
            "filename": f"{archive_name}.tar.gz",
            "size": str(archive_size),
            "owner": user_id,
            "permissions": "644",
            "last_modified": "2025-08-13T01:01:01Z",
            "checksum": archive_checksum,
        }

        # Place the archive in the destination directory on the source server
        dest_dir_found = False
        for directory in source_server["directories"]:
            if directory["path"] == destination_directory:
                directory["files"].append(new_archive_file)
                dest_dir_found = True
                break
        if not dest_dir_found:
            source_server["directories"].append(
                {"path": destination_directory, "files": [new_archive_file]}
            )
        payload = {
            "status": "success",
            "message": f"Archive instruction {archive_id} created and simulated file created at {source_server['hostname']}:{archive_path}.",
            "archive_id": archive_id,
            "archive_path": archive_path,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateArchive",
                "description": "Creates a new archive instruction and a simulated archive file in the file_system.json state.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "destination_directory": {"type": "string"},
                        "remote_address": {"type": "string"},
                        "archive_name": {"type": "string"},
                        "filepaths": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "user_id",
                        "destination_directory",
                        "remote_address",
                        "archive_name",
                        "filepaths",
                    ],
                },
            },
        }


class CreateFileList(Tool):
    """Incorporates a list of files into the file_lists.json database, retrieving their size and checksum from file_system.json."""

    @staticmethod
    def invoke(data: dict[str, Any], operation_id: str = None, filepaths: list = None) -> str:
        if filepaths is None:
            filepaths = []
        file_lists = data.get("file_lists", [])

        max_id = 0
        if file_lists:
            for item in file_lists:
                try:
                    current_id_num = int(item.get("file_id", "file_000").split("_")[1])
                    if current_id_num > max_id:
                        max_id = current_id_num
                except (IndexError, ValueError):
                    continue

        added_files = []
        for i, filepath in enumerate(filepaths):
            found_size = "0"
            found_checksum = (
                "a1f2e3d4c5b6789012345678901234567890abcd"  # Standard checksum
            )
            file_found = False
            for server in data.get("file_system", []):
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        current_path = f"{directory.get('path')}/{file.get('filename')}"
                        if current_path == filepath:
                            found_size = file.get("size", "0")
                            found_checksum = file.get("checksum", found_checksum)
                            file_found = True
                            break
                    if file_found:
                        break
                if file_found:
                    break

            new_id_num = max_id + i + 1
            file_id = f"file_{new_id_num:03d}"
            filename = filepath.split("/")[-1]

            new_entry = {
                "operation_id": operation_id,
                "file_id": file_id,
                "filename": filename,
                "filepath": filepath,
                "filedestination": None,
                "size": found_size,
                "checksum": found_checksum,
                "status": "pending",
            }
            file_lists.append(new_entry)
            added_files.append(file_id)
        payload = {
            "status": "success",
            "message": f"Added {len(added_files)} files to the list.",
            "file_ids": added_files,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFileList",
                "description": "Adds a list of files to the file_lists.json database, looking up their size and checksum from file_system.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "operation_id": {
                            "type": "string",
                            "description": "The ID of the operation these files are associated with.",
                        },
                        "filepaths": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of full file paths to add.",
                        },
                    },
                    "required": ["operation_id", "filepaths"],
                },
            },
        }


class TransferFile(Tool):
    """Emulates the transfer of a file by establishing its record on the destination server in file_system.json. Creates the server and directory if they are absent."""

    @staticmethod
    def invoke(data: dict[str, Any], source_path: str = None, destination_path: str = None) -> str:
        source_file_details = None
        file_found = False
        for server in data.get("file_system", []):
            for directory in server.get("directories", []):
                for file in directory.get("files", []):
                    if f"{directory.get('path')}/{file.get('filename')}" == source_path:
                        source_file_details = file.copy()
                        server.get("hostname")
                        file_found = True
                        break
                if file_found:
                    break
            if file_found:
                break

        if not source_file_details:
            # Verify if the source path contains a server name (for transfers between servers)
            try:
                source_hostname, path = source_path.split(":", 1)
                for server in data.get("file_system", []):
                    if server.get("hostname") == source_hostname:
                        for directory in server.get("directories", []):
                            for file in directory.get("files", []):
                                if (
                                    f"{directory.get('path')}/{file.get('filename')}"
                                    == path
                                ):
                                    source_file_details = file.copy()
                                    server.get("hostname")
                                    file_found = True
                                    break
                            if file_found:
                                break
                    if file_found:
                        break
            except ValueError:
                pass  # Path not designated for a server

        if not source_file_details:
            payload = {"error": f"Source file not found: {source_path}"}
            out = json.dumps(payload)
            return out

        try:
            dest_hostname, dest_path = destination_path.split(":", 1)
            dest_dir_path = "/".join(dest_path.split("/")[:-1])
            dest_filename = dest_path.split("/")[-1]
        except ValueError:
            payload = {
                "error": "Invalid destination format. Expected 'hostname:/path/to/file'"
            }
            out = json.dumps(payload)
            return out

        dest_server = None
        for server in data["file_system"]:
            if server.get("hostname") == dest_hostname:
                dest_server = server
                break

        if not dest_server:
            max_id = 0
            for s in data["file_system"]:
                try:
                    current_id_num = int(s.get("server_id", "srv_000").split("_")[1])
                    if current_id_num > max_id:
                        max_id = current_id_num
                except (IndexError, ValueError):
                    continue
            new_id_num = max_id + 1
            new_server_id = f"srv_{new_id_num:03d}"
            dest_server = {
                "server_id": new_server_id,
                "hostname": dest_hostname,
                "directories": [],
            }
            data["file_system"].append(dest_server)

        dest_directory = None
        for directory in dest_server["directories"]:
            if directory.get("path") == dest_dir_path:
                dest_directory = directory
                break

        if not dest_directory:
            dest_directory = {"path": dest_dir_path, "files": []}
            dest_server["directories"].append(dest_directory)

        new_file_entry = source_file_details
        new_file_entry["filename"] = dest_filename
        dest_directory["files"].append(new_file_entry)
        payload = {
            "status": "success",
            "message": f"File transferred from {source_path} to {destination_path}.",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TransferFile",
                "description": "Simulates transferring a file by creating its record on the destination server in file_system.json. Creates server and directory if they do not exist.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_path": {"type": "string"},
                        "destination_path": {"type": "string"},
                    },
                    "required": ["source_path", "destination_path"],
                },
            },
        }


class VerifyChecksum(Tool):
    """Confirms the checksum of a file against its initial record in file_lists.json."""

    @staticmethod
    def invoke(data: dict[str, Any], file_id: str = None, filepath: str = None) -> str:
        original_checksum = None
        for record in data.get("file_lists", []):
            if record.get("file_id") == file_id:
                original_checksum = record.get("checksum")
                break

        if not original_checksum:
            payload = {"error": f"File record not found for file_id: {file_id}"}
            out = json.dumps(payload)
            return out

        try:
            dest_hostname, dest_path = filepath.split(":", 1)
        except ValueError:
            payload = {"error": "Invalid filepath format. Expected 'hostname:/path/to/file'"}
            out = json.dumps(payload)
            return out

        actual_checksum = None
        file_found = False
        for server in data.get("file_system", []):
            if server.get("hostname") == dest_hostname:
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if (
                            f"{directory.get('path')}/{file.get('filename')}"
                            == dest_path
                        ):
                            actual_checksum = file.get("checksum")
                            file_found = True
                            break
                    if file_found:
                        break
                if file_found:
                    break

        if not file_found:
            payload = {"error": f"File not found at path: {filepath}"}
            out = json.dumps(payload)
            return out

        match = original_checksum == actual_checksum
        payload = {
            "match": match,
            "original_checksum": original_checksum,
            "actual_checksum": actual_checksum,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifyChecksum",
                "description": "Verifies the checksum of a file against its original record in file_lists.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_id": {
                            "type": "string",
                            "description": "The ID of the file record in file_lists.json.",
                        },
                        "filepath": {
                            "type": "string",
                            "description": "The full path of the file to verify, in 'hostname:/path/to/file' format.",
                        },
                    },
                    "required": ["file_id", "filepath"],
                },
            },
        }


class DeleteFile(Tool):
    """Removes a file from the file system."""

    @staticmethod
    def invoke(data: dict[str, Any], filepath: str) -> str:
        for server in data.get("file_system", []):
            for directory in server.get("directories", []):
                original_len = len(directory.get("files", []))
                directory["files"] = [
                    f
                    for f in directory.get("files", [])
                    if f"{directory.get('path')}/{f.get('filename')}" != filepath
                ]
                if len(directory.get("files", [])) < original_len:
                    payload = {"status": "success", "message": f"File {filepath} deleted."}
                    out = json.dumps(payload)
                    return out
        payload = {"error": f"File not found: {filepath}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteFile",
                "description": "Deletes a file from the file system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filepath": {
                            "type": "string",
                            "description": "The full path of the file to delete.",
                        }
                    },
                    "required": ["filepath"],
                },
            },
        }


class LogTaskStart(Tool):
    """Records the initiation of a new task in task_logs.json."""

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, user_id: str = None, task_type: str = None) -> str:
        new_task_log = {
            "task_id": task_id,
            "task_type": task_type,
            "user_id": user_id,
            "result": "in_progress",
            "started_at": "2025-08-13T01:01:01Z",  # Emulated timestamp
            "notes": "Task initiated by agent.",
        }
        data["task_logs"].append(new_task_log)
        payload = {"status": "success", "message": f"Task {task_id} logged as in_progress."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogTaskStart",
                "description": "Logs the start of a new task in task_logs.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "task_type": {"type": "string"},
                    },
                    "required": ["task_id", "user_id", "task_type"],
                },
            },
        }


class UpdateTaskStatus(Tool):
    """Modifies the status of a task across different logs."""

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, new_status: str = None) -> str:
        for task in data.get("task_logs", []):
            if task.get("task_id") == task_id:
                task["result"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Task {task_id} status updated to {new_status}.",
                }
                out = json.dumps(payload)
                return out
        for task in data.get("archive_instructions", []):
            if task.get("archive_id") == task_id:
                task["status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Task {task_id} status updated to {new_status}.",
                }
                out = json.dumps(payload)
                return out
        for task in data.get("directories", []):
            if task.get("operation_id") == task_id:
                payload = {
                    "status": "success",
                    "message": f"Task {task_id} status noted as {new_status}.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Task not found: {task_id}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTaskStatus",
                "description": "Updates the status of a task in various logs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["task_id", "new_status"],
                },
            },
        }


class LogCompletionMessage(Tool):
    """Records a completion message and provides the generated msg_id."""

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, user_id: str = None, message: str = None) -> str:
        completion_messages = data.get("completion_messages", [])
        max_id = 0
        if completion_messages:
            for msg in completion_messages:
                try:
                    current_id_num = int(msg.get("msg_id", "comp_000").split("_")[1])
                    if current_id_num > max_id:
                        max_id = current_id_num
                except (IndexError, ValueError):
                    continue
        new_id_num = max_id + 1
        msg_id = f"comp_{new_id_num:03d}"

        new_log = {
            "msg_id": msg_id,
            "task_id": task_id,
            "user_id": user_id,
            "msg": message,
        }
        data["completion_messages"].append(new_log)
        payload = {
                "status": "success",
                "message": "Completion message logged.",
                "msg_id": msg_id,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogCompletionMessage",
                "description": "Logs a completion message and returns the generated msg_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["task_id", "user_id", "message"],
                },
            },
        }


class SendSlackNotification(Tool):
    """Dispatches a notification to a Slack channel."""

    @staticmethod
    def invoke(data: dict[str, Any], channel_name: str = None, message: str = None) -> str:
        channel_id = None
        for channel in data.get("slack_channels", []):
            if channel.get("name") == channel_name:
                channel_id = channel.get("channel_id")
                break

        if not channel_id:
            payload = {"error": f"Channel '{channel_name}' not found."}
            out = json.dumps(payload)
            return out

        slack_messages = data.get("slack_messages", [])
        max_id = 0
        if slack_messages:
            for msg in slack_messages:
                try:
                    current_id_num = int(msg.get("message_id", "msg_000").split("_")[1])
                    if current_id_num > max_id:
                        max_id = current_id_num
                except (IndexError, ValueError):
                    continue
        new_id_num = max_id + 1
        message_id = f"msg_{new_id_num:03d}"

        new_message = {
            "message_id": message_id,
            "channel_id": channel_id,
            "user_id": "system_agent",
            "username": "SystemMonitor",
            "message": message,
            "timestamp": "2025-08-13T01:01:01Z",
            "type": "system_alert",
        }
        data["slack_messages"].append(new_message)
        payload = {"status": "success", "message": f"Message sent to {channel_name}."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendSlackNotification",
                "description": "Sends a notification to a Slack channel.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel_name": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["channel_name", "message"],
                },
            },
        }


class LogError(Tool):
    """Records an error message and returns the generated msg_id."""

    @staticmethod
    def invoke(data: dict[str, Any], err_type: str = None, task_id: str = None, user_id: str = None, message: str = None, severity: str = None) -> str:
        error_messages = data.get("error_messages", [])
        max_id = 0
        if error_messages:
            for msg in error_messages:
                try:
                    current_id_num = int(msg.get("msg_id", "err_msg_000").split("_")[2])
                    if current_id_num > max_id:
                        max_id = current_id_num
                except (IndexError, ValueError):
                    continue
        new_id_num = max_id + 1
        msg_id = f"err_msg_{new_id_num:03d}"

        new_error = {
            "msg_id": msg_id,
            "err_type": err_type,
            "task_id": task_id,
            "user_id": user_id,
            "msg": message,
            "severity": severity,
        }
        data["error_messages"].append(new_error)
        payload = {"status": "success", "message": "Error message logged.", "msg_id": msg_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "logError",
                "description": "Logs an error message and returns the generated msg_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "err_type": {"type": "string"},
                        "task_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "message": {"type": "string"},
                        "severity": {"type": "string"},
                    },
                    "required": [
                        "err_type",
                        "task_id",
                        "user_id",
                        "message",
                        "severity",
                    ],
                },
            },
        }


class GetPendingFileChecks(Tool):
    """Fetches tasks for pending file checks."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        pending_tasks = [
            task for task in data.get("file_check_db", []) if not task.get("completed")
        ]
        payload = {"pending_tasks": pending_tasks}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPendingFileChecks",
                "description": "Retrieves pending file check tasks.",
                "parameters": {},
            },
        }


class CreateDirectory(Tool):
    """Establishes a new directory."""

    @staticmethod
    def invoke(data: dict[str, Any], server_hostname: str = None, new_directory_path: str = None) -> str:
        for server in data.get("file_system", []):
            if server.get("hostname") == server_hostname:
                server["directories"].append({"path": new_directory_path, "files": []})
                payload = {
                    "status": "success",
                    "message": f"Directory '{new_directory_path}' created on '{server_hostname}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Server not found: {server_hostname}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDirectory",
                "description": "Creates a new directory on a server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_hostname": {
                            "type": "string",
                            "description": "The hostname of the server.",
                        },
                        "new_directory_path": {
                            "type": "string",
                            "description": "The full path of the new directory.",
                        },
                    },
                    "required": ["server_hostname", "new_directory_path"],
                },
            },
        }


class MoveFile(Tool):
    """Transfers a file from a source location to a target location."""

    @staticmethod
    def invoke(data: dict[str, Any], source_path: str = None, destination_path: str = None) -> str:
        file_to_move = None
        source_directory = None

        for server in data.get("file_system", []):
            for directory in server.get("directories", []):
                for file in directory.get("files", []):
                    if f"{directory.get('path')}/{file.get('filename')}" == source_path:
                        file_to_move = file
                        source_directory = directory
                        break
                if file_to_move:
                    break
            if file_to_move:
                break

        if not file_to_move:
            payload = {"error": f"Source file not found: {source_path}"}
            out = json.dumps(payload)
            return out

        source_directory["files"] = [
            f
            for f in source_directory["files"]
            if f"{source_directory.get('path')}/{f.get('filename')}" != source_path
        ]

        dest_dir_path = "/".join(destination_path.split("/")[:-1])
        dest_filename = destination_path.split("/")[-1]

        file_to_move["filename"] = dest_filename

        for server in data.get("file_system", []):
            for directory in server.get("directories", []):
                if directory.get("path") == dest_dir_path:
                    directory["files"].append(file_to_move)
                    payload = {
                            "status": "success",
                            "message": f"File moved from {source_path} to {destination_path}.",
                        }
                    out = json.dumps(
                        payload)
                    return out
        payload = {"error": f"Destination directory not found: {dest_dir_path}"}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MoveFile",
                "description": "Moves a file from a source path to a destination path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_path": {"type": "string"},
                        "destination_path": {"type": "string"},
                    },
                    "required": ["source_path", "destination_path"],
                },
            },
        }


#--- Compilation of all accessible tools ---
TOOLS = [
    GetFileMetadata(),
    GetLastAccessTime(),
    GetLastAccessedFile(),
    FindFiles(),
    CheckDiskSpace(),
    CreateArchive(),
    CreateFileList(),
    VerifyChecksum(),
    TransferFile(),
    DeleteFile(),
    LogTaskStart(),
    UpdateTaskStatus(),
    LogCompletionMessage(),
    SendSlackNotification(),
    LogError(),
    GetPendingFileChecks(),
    CreateDirectory(),
    MoveFile(),
]
