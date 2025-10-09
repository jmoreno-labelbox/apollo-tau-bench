import datetime
import hashlib
import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


class FindIncompleteTasksTool(Tool):
    """Tool for identifying pending tasks in the file_check_db."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ScanIncompleteTasks",
                "description": "Scans the file_check_db for the first task with 'completed' status set to False.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], file_check_db: list = None) -> str:
        database = file_check_db if file_check_db is not None else []

        # Find the initial task with a completed flag set to False
        incomplete_task = next(
            (entry for entry in database if not entry.get("completed", True)), None
        )

        if incomplete_task:
            payload = {"task_id": incomplete_task.get("task_id"), "task": incomplete_task}
            out = json.dumps(payload)
            return out
        payload = {"task_id": None, "message": "No incomplete tasks found."}
        out = json.dumps(payload)
        return out
class ExtractTaskInstructionsTool(Tool):
    """Retrieves and saves task instructions from the file check database."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "parseFileCheckInstructions",
                "description": "Parses instructions from file_check_db for a specific task_id and populates the task_instructions table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The ID of the task to parse.",
                        }
                    },
                    "required": ["task_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str) -> str:
        target_task_id = task_id

        # Fetch task from the database
        task_record = None
        for record in data.get("file_check_db", {}).values():
            if record["task_id"] == target_task_id:
                task_record = record
                break

        if task_record is None:
            payload = {"error": f"Task ID {target_task_id} not found."}
            out = json.dumps(payload)
            return out

        # Obtain pre-parsed instructions from the task record
        instruction_data = task_record.get("parsed_instructions", {}).values()

        # Set up storage if necessary
        if "task_instructions" not in data:
            data["task_instructions"] = []

        # Create a simplified instruction entry from the detailed parsed information
        simplified_entry = {
            "task_id": target_task_id,
            "remote_address": task_record.get("remote_server"),
            "max_size": instruction_data.get("size_filter", {}).values().get("max_bytes"),
            "last_access_days": instruction_data.get("time_filter", {}).values().get("days"),
            "users": list(instruction_data.get("user_filter", {}).values()),
        }

        data["task_instructions"].append(simplified_entry)
        payload = {"status": "success", "parsed_instruction": simplified_entry}
        out = json.dumps(payload)
        return out
class SlackMessageDispatcherTool(Tool):
    """Manages message delivery to specified Slack channels."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendSlackNotification",
                "description": "Sends a message to a specified Slack channel.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
                            "description": "The Slack channel to send the message to (e.g., 'File Check').",
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the message.",
                        },
                    },
                    "required": ["channel", "message"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], channel: str, message: str, mention_users: list = None, priority: str = None) -> str:
        target_channel = channel
        msg_content = message

        # Set up slack logging if it is absent
        if data.get("slack_log") is None:
            data["slack_log"] = []

        # Generate and save a log record
        notification_entry = {"channel": target_channel, "message": msg_content}
        data["slack_log"].append(notification_entry)

        result = {"status": "success", "log_entry": notification_entry}
        payload = result
        out = json.dumps(payload)
        return out
class SshConnectivityVerifierTool(Tool):
    """Utility for verifying SSH access to target servers."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckSshConnection",
                "description": "Verifies that a remote address is accessible. For simulation, this always succeeds.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "remote_address": {
                            "type": "string",
                            "description": "The address of the remote server.",
                        }
                    },
                    "required": ["remote_address"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], remote_address: str) -> str:
        server_address = remote_address

        # Consistently returns a successful connection for simulation
        response_data = {"status": "connected", "remote_address": server_address}
        payload = response_data
        out = json.dumps(payload)
        return out
class TmuxSessionManagerTool(Tool):
    """Oversees tmux session creation for ongoing remote processes."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createTmuxSession",
                "description": "Creates a named tmux session to ensure process persistence.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_name": {
                            "type": "string",
                            "description": "The name for the tmux session.",
                        }
                    },
                    "required": ["session_name"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], session_name: str) -> str:
        requested_session = session_name

        # Establish session tracking
        data.setdefault("tmux_sessions", [])

        # Verify if a session is already present
        if requested_session in data["tmux_sessions"]:
            payload = {"status": "exists", "session_name": requested_session}
            out = json.dumps(payload)
            return out

        # Create a new session
        data["tmux_sessions"].append(requested_session)
        payload = {"status": "created", "session_name": requested_session}
        out = json.dumps(payload)
        return out
class GetIdleCpuCountTool(Tool):
    """Emulates checking server CPU usage to determine the count of idle cores."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getIdleCpuCount",
                "description": "Gets the total number of idle CPU cores to use for parallel processing. Simulates using 'top' and 'awk'. Returns a fixed value for determinism.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    def invoke(data: dict[str, Any], unexpected: Any = None) -> str:
        payload = {"idle_cpus": 6}
        out = json.dumps(payload)
        return out
class FindAndStatFilesTool(Tool):
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAndStatFiles",
                "description": "Finds files on a remote server and gets their metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_directory": {"type": "string"},
                        "last_access_days": {"type": "integer"},
                        "parallel_processes": {
                            "type": "integer",
                            "description": "Number of parallel jobs. Defaults to 6.",
                        },
                    },
                    "required": ["target_directory", "last_access_days"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        last_access_days: int = None,
        target_directory: Any = None,
        parallel_processes: int = None
    ) -> str:
        log_name = "file_check_log.json"
        all_remote_files: list[dict[str, Any]] = []

        # Traverse the simulated file_system structure and gather files in a deterministic manner.
        for server in data.get("file_system", {}).values():
            server_host = server.get("host", server.get("remote_address", "unknown"))
            for directory in server.get("directories", []):
                dir_path = directory.get("path", "")
                for f in directory.get("files", []) or []:
                    # accommodate string entries or dictionaries with different keys
                    if isinstance(f, str):
                        name = f
                        path = (
                            f
                            if f.startswith("/")
                            else f"{dir_path}/{f}".replace("//", "/")
                        )
                        size = 0
                        user = "unknown"
                        last_access = None
                    elif isinstance(f, dict):
                        name = (
                            f.get("name")
                            or f.get("filename")
                            or f.get("file_name")
                            or (f.get("path") and f.get("path").split("/")[-1])
                        )
                        path = f.get("path") or (
                            f"{dir_path}/{name}".replace("//", "/")
                            if name
                            else f"{dir_path}/"
                        )
                        size = (
                            int(f.get("size", 0))
                            if isinstance(f.get("size", 0), (int, float, str))
                            else 0
                        )
                        user = f.get("user", "unknown")
                        last_access = f.get("last_access")
                    else:
                        continue

                    entry = {
                        "path": path,
                        "filename": name,
                        "size": int(size),
                        "user": user,
                        "last_access": last_access,
                        "host": server_host,
                    }
                    all_remote_files.append(entry)

        # Store the log in a deterministic way
        data[log_name] = {"data": all_remote_files}
        payload = {
            "status": "success",
            "log_name": log_name,
            "file_count": len(all_remote_files),
        }
        out = json.dumps(payload)
        return out
class FilterFileLogTool(Tool):
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterFileLog",
                "description": "Filters a generated file log based on max size and a list of users.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "Defaults to 'file_check_log.json'.",
                        },
                        "max_size": {"type": "integer"},
                        "users": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["max_size", "users"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], log_name: str = "file_check_log.json", max_size: int = None, users: list = None) -> str:
        if log_name not in data:
            payload = {"error": f"Log '{log_name}' not found."}
            out = json.dumps(payload)
            return out

        original_count = len(data[log_name]["data"])
        data[log_name]["data"] = [
            f
            for f in data[log_name]["data"]
            if f["size"] < max_size and f["user"] in users
        ]
        payload = {
                "status": "success",
                "original_count": original_count,
                "filtered_count": len(data[log_name]["data"]),
            }
        out = json.dumps(payload)
        return out
class AddHeaderToFileLogTool(Tool):
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddHeaderToFileLog",
                "description": "Adds a top-level 'task_id' key to the specified log file object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "Defaults to 'file_check_log.json'.",
                        },
                        "task_id": {"type": "string"},
                    },
                    "required": ["task_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], log_name: str = "file_check_log.json", task_id: str = None) -> str:
        if log_name not in data:
            payload = {"error": f"Log '{log_name}' not found."}
            out = json.dumps(payload)
            return out
        # Encapsulate existing data within a 'data' key and include 'task_id' at the top level
        log_data = data[log_name]["data"]
        data[log_name] = {"task_id": task_id, "data": log_data}
        payload = {"status": "success", "log_name": log_name, "header_added": "task_id"}
        out = json.dumps(payload)
        return out
class ComputeChecksumTool(Tool):
    """Calculates a sha256sum for a data object, mimicking checksum generation."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeChecksum",
                "description": "Computes and returns a sha256 checksum for a given log file.",
                "parameters": {
                    "type": "object",
                    "properties": {"log_name": {"type": "string"}},
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], log_name: str) -> str:
        if log_name not in data:
            payload = {"error": f"Log '{log_name}' not found."}
            out = json.dumps(payload)
            return out
        content_str = json.dumps(data[log_name], sort_keys=True)
        checksum = hashlib.sha256(content_str.encode()).hexdigest()
        #store checksum using a deterministic key '<log_name>.sha256'
        data[f"{log_name}.sha256"] = checksum
        payload = {"log_name": log_name, "checksum": checksum}
        out = json.dumps(payload)
        return out
class CopyFileToHostTool(Tool):
    """Emulates transferring a file (along with its checksum) from remote to host via scp."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CopyFileToHost",
                "description": "Simulates copying a log and its checksum file from a remote source to the local host.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "The name of the log file to copy.",
                        }
                    },
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], log_name: str) -> str:
        checksum_name = f"{log_name}.sha256"
        if log_name not in data or checksum_name not in data:
            payload = {"error": "Log or checksum not found for copying."}
            out = json.dumps(payload)
            return out

        local_log_name = f"local_{log_name}"
        local_checksum_name = f"local_{checksum_name}"

        data[local_log_name] = data[log_name]
        data[local_checksum_name] = data[checksum_name]
        payload = {"status": "success", "copied_files": [local_log_name, local_checksum_name]}
        out = json.dumps(payload)
        return out
class VerifyLocalChecksumTool(Tool):
    """Confirms the checksum of a file copied locally."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifyLocalChecksum",
                "description": "Verifies the integrity of a copied file by re-computing its checksum and comparing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "The base name of the local log file to verify.",
                        }
                    },
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], log_name: str) -> str:
        checksum_name = f"{log_name}.sha256"
        if log_name not in data or checksum_name not in data:
            payload = {"error": "Log or checksum not found for copying."}
            out = json.dumps(payload)
            return out

        local_log_name = f"local_{log_name}"
        local_checksum_name = f"local_{checksum_name}"

        data[local_log_name] = data[log_name]
        data[local_checksum_name] = data[checksum_name]
        payload = {"status": "success", "copied_files": [local_log_name, local_checksum_name]}
        out = json.dumps(payload)
        return out
class LocalCleanupTool(Tool):
    """Removes local files, including downloaded logs and checksums."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "localCleanup",
                "description": "Deletes specified files from the local environment simulation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "files_to_delete": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of local file keys to delete (e.g., 'local_file_check_log.json').",
                        }
                    },
                    "required": ["files_to_delete"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], files_to_delete: list[str]) -> str:
        deleted = [
            f_key
            for f_key in files_to_delete
            if data.pop(f_key, None) is not None
        ]
        payload = {"deleted_local_files": deleted}
        out = json.dumps(payload)
        return out
class RemoteCleanupTool(Tool):
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoteCleanup",
                "description": "Deletes specified files and optionally a tmux session.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "files_to_delete": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "session_to_kill": {
                            "type": "string",
                            "description": "Optional tmux session to kill.",
                        },
                    },
                    "required": ["files_to_delete"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], files_to_delete: list[str] = None, session_to_kill: str = None) -> str:
        files_to_delete = set(files_to_delete or [])
        deleted: list[str] = []

        # Eliminate top-level keys that correspond to files_to_delete
        for key in list(files_to_delete):
            if data.pop(key, None) is not None:
                deleted.append(key)

        # Delete entries from remote_storage by matching either path or basename
        if "remote_storage" in data:
            remaining = []
            for item in data["remote_storage"].values():
                path = item.get("path")
                basename = path.split("/")[-1] if path else None
                if path in files_to_delete or basename in files_to_delete:
                    deleted.append(path)
                else:
                    remaining.append(item)
            data["remote_storage"] = remaining

        # Delete files located in server directories
        for server in data.get("file_system", {}).values():
            for directory in server.get("directories", []):
                remaining_files = []
                for f in directory.get("files", []):
                    # Manage both string and dictionary file entries
                    if isinstance(f, str):
                        full_path = f"{directory.get('path', '')}/{f}".replace(
                            "//", "/"
                        )
                        name = f
                    else:  # is a dictionary
                        name = f.get("name")  # Retrieve name securely
                        full_path = f"{directory.get('path', '')}/{name}".replace(
                            "//", "/"
                        )

                    if full_path in files_to_delete or name in files_to_delete:
                        deleted.append(full_path)
                    else:
                        remaining_files.append(f)
                directory["files"] = remaining_files

        # Terminate tmux session if requested
        session_killed = False
        if session_to_kill and "tmux_sessions" in data and session_to_kill in data["tmux_sessions"]:
            data["tmux_sessions"].remove(session_to_kill)
            session_killed = True

        # Remove duplicates from the deleted list
        deleted = list(dict.fromkeys(deleted))
        payload = {
            "status": "success",
            "deleted_remote_files": deleted,
            "session_killed": session_killed,
        }
        out = json.dumps(payload)
        return out
class UpdateTaskStatusTool(Tool):
    """Modifies the status of a task in the file_check_db."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTaskStatus",
                "description": "Updates the 'completed' field for a task in the file_check_db.",
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

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str, completed: bool) -> str:
        task = next(
            (t for t in data.get("file_check_db", {}).values() if t["task_id"] == task_id), None
        )
        if task:
            task["completed"] = completed
            payload = {"status": "success", "task_id": task_id, "completed": completed}
            out = json.dumps(payload)
            return out
        payload = {"error": f"Task ID {task_id} not found."}
        out = json.dumps(payload)
        return out
class ParseDirectoryRestructureInstructionsTool(Tool):
    """Interprets user instructions for organizing and relocating files into a structured format."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ParseDirectoryRestructureInstructions",
                "description": "Parses instructions to move files from a target directory to a destination, sorting by file type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_directory": {"type": "string"},
                        "destination_directory": {"type": "string"},
                        "sort_rules": {
                            "type": "object",
                            "description": "A dictionary mapping file extensions to subdirectory names.",
                        },
                    },
                    "required": [
                        "target_directory",
                        "destination_directory",
                        "sort_rules",
                    ],
                },
            },
        }

    @staticmethod

    def invoke(

        data: dict[str, Any],

        instruction: dict[str, Any] = None,

        target_directory: Any = None,

        destination_directory: str = None,

        sort_rules: dict = None

    ) -> str:
        if "directories_db" not in data:
            data["directories_db"] = []
        data["directories_db"].append(instruction)
        payload = {"status": "success", "instruction": instruction}
        out = json.dumps(payload)
        return out
class CreateFileListForMoveTool(Tool):
    """Examines a target directory and generates a list of files to be relocated."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFileListForMove",
                "description": "Generates a file_list database from files in a target directory.",
                "parameters": {
                    "type": "object",
                    "properties": {"target_directory": {"type": "string"}},
                    "required": ["target_directory"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], target_directory: str) -> str:
        file_list: list[dict[str, Any]] = []

        for server in data.get("file_system", {}).values():
            for directory in server.get("directories", []):
                dir_path = directory.get("path", "")
                for f in directory.get("files", []) or []:
                    if isinstance(f, str):
                        name = f
                        full_path = (
                            name
                            if name.startswith("/")
                            else f"{dir_path}/{name}".replace("//", "/")
                        )
                        size = 0
                        user = "unknown"
                    elif isinstance(f, dict):
                        name = (
                            f.get("name")
                            or f.get("filename")
                            or f.get("file_name")
                            or (f.get("path") and f.get("path").split("/")[-1])
                        )
                        full_path = f.get("path") or f"{dir_path}/{name}".replace(
                            "//", "/"
                        )
                        size = (
                            int(f.get("size", 0))
                            if isinstance(f.get("size", 0), (int, float, str))
                            else 0
                        )
                        user = f.get("user", "unknown")
                    else:
                        continue

                    if full_path.startswith(target_directory):
                        entry = {
                            "path": full_path,
                            "filename": name,
                            "size": int(size),
                            "user": user,
                        }
                        file_list.append(entry)

        data["file_list"] = file_list
        payload = {"status": "success", "file_count": len(file_list)}
        out = json.dumps(payload)
        return out
class GetDiskSpaceTool(Tool):
    """Emulates checking the available disk space."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDiskSpace",
                "description": "Returns the available disk space. In this simulation, it returns a fixed large number for determinism.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "The path to check for disk space (unused in simulation).",
                        }
                    },
                    "required": ["path"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], path: str) -> str:
        available_space = 10**12  # 1 Terabyte
        data[f"disk_space_{path.replace('/', '_')}"] = available_space
        payload = {"available_space": available_space, "path": path}
        out = json.dumps(payload)
        return out
class VerifySpaceRequirementsTool(Tool):
    """Contrasts total file size with available disk space to confirm adequate space."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifySpaceRequirements",
                "description": "Compares the total size of files to be moved against available disk space at the destination to ensure the operation can proceed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_path": {
                            "type": "string",
                            "description": "The destination path to check space for.",
                        }
                    },
                    "required": ["destination_path"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], destination_path: str) -> str:
        # Obtain the total size from the previous calculation
        total_size = data.get("last_total_size", 0)

        # Determine available space for the destination
        disk_space_key = f"disk_space_{destination_path.replace('/', '_')}"
        available_space = data.get(
            disk_space_key, 10**12
        )  # Fallback to 1TB if not located

        if total_size <= available_space:
            payload = {
                "status": "sufficient_space",
                "total_size": total_size,
                "available_space": available_space,
                "space_check": "passed",
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {
                "status": "insufficient_space",
                "total_size": total_size,
                "available_space": available_space,
                "space_check": "failed",
                "error": f"Insufficient disk space. Need {total_size} bytes but only {available_space} bytes available.",
            }
            out = json.dumps(payload)
            return out
class PopulateChecksumsInFileListTool(Tool):
    """Calculates and fills in checksums for every file in the file_list."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PopulateChecksumsInFileList",
                "description": "Iterates through the file_list and populates the 'checksum' field for each entry using SHA256.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], file_list_directory: Any = None) -> str:
        if "file_list" not in data:
            payload = {"error": "file_list not found."}
            out = json.dumps(payload)
            return out
        for file in data["file_list"].values():
            file["checksum"] = hashlib.sha256(file["path"].encode()).hexdigest()
        payload = {"status": "success", "populated_count": len(data["file_list"])}
        out = json.dumps(payload)
        return out
class ComputeAndResolveDestinationPathsTool(Tool):
    """Determines destination paths for files according to sorting rules and addresses name conflicts."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeAndResolveDestinationPaths",
                "description": "Computes destination paths for all files in file_list, handles conflicts by appending integers, and populates the 'destination_path' field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_directory": {"type": "string"},
                        "sort_rules": {"type": "object"},
                    },
                    "required": ["destination_directory", "sort_rules"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], destination_directory: str, sort_rules: dict[str, str]) -> str:
        dest_dir = destination_directory
        sort_rules = sort_rules
        destination_paths: set[str] = set()

        for file in data.get("file_list", {}).values():
            ext = file["filename"].split(".")[-1] if "." in file["filename"] else ""
            sub_dir = sort_rules.get(ext, "miscellaneous")
            base = (
                ".".join(file["filename"].split(".")[:-1])
                if "." in file["filename"]
                else file["filename"]
            )
            ext_suffix = f".{ext}" if ext else ""
            new_name = f"{base}{ext_suffix}"
            new_path = f"{dest_dir}/{sub_dir}/{new_name}"

            counter = 0
            candidate = new_path
            while candidate in destination_paths:
                candidate = f"{dest_dir}/{sub_dir}/{base}_{counter}{ext_suffix}"
                counter += 1

            destination_paths.add(candidate)
            file["destination_path"] = candidate
        payload = {"status": "success", "paths_resolved": len(data.get("file_list", {}))}
        out = json.dumps(
            payload)
        return out
class CopyAndVerifyFilesTool(Tool):
    """Emulates transferring files to their new locations and validating checksums."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CopyAndVerifyFiles",
                "description": "Copies files from original path to destination path and verifies their checksums.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any],
    source_directory: Any = None,
    ) -> str:
        copied_files: list[dict[str, Any]] = []
        if "moved_files" not in data:
            data["moved_files"] = []

        for file in data.get("file_list", {}).values():
            # Emulate checksum computation if absent
            if "checksum" not in file:
                file["checksum"] = hashlib.sha256(file["path"].encode()).hexdigest()

            # Emulate copying by appending an entry to moved_files (maintain checksum)
            moved = {
                "original": file["path"],
                "destination": file.get("destination_path"),
                "checksum": file["checksum"],
            }
            data["moved_files"].append(moved)
            copied_files.append(moved)

        # Verification after moving: confirm destination checksums align with source checksum (simulated deterministic)
        verified_count = len(copied_files)
        payload = {"status": "success", "verified_and_copied": verified_count}
        out = json.dumps(payload)
        return out
class CleanOriginalDirectoryTool(Tool):
    """Emulates removing all original files following a successful copy and verification process."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CleanOriginalDirectory",
                "description": "Deletes the original files that have been successfully moved and returns the count of cleaned files.",
                "parameters": {
                    "type": "object",
                    "properties": {"target_directory": {"type": "string"}},
                    "required": ["target_directory"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], target_directory: str) -> str:
        cleaned_count = 0

        # Count files present in the file_list (these are the ones being cleaned)
        if "file_list" in data:
            cleaned_count = len(data["file_list"])

        # Save the count of cleaned files for output
        data["cleaned_files_count"] = cleaned_count
        payload = {"status": "success", "cleaned_files_count": cleaned_count}
        out = json.dumps(payload)
        return out
class CalculateTotalSizeTool(Tool):
    """Determines the total size of a collection of files."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTotalSize",
                "description": "Computes the sum of the sizes for a given list of file paths.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_paths": {
                            "type": "array",
                            "items": {
},
                        },
                        "file_list_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], file_paths: list = None, file_list_name: str = None, file_list_directory: str = None) -> str:
        pass
        # Allow either direct file_paths or a reference to a file list contained in data
        file_entries = []
        if file_paths is not None:
            file_entries = file_paths or []
        elif file_list_name:
            name = file_list_name
            stored = data.get(name)
            if isinstance(stored, dict) and isinstance(stored.get("data"), list):
                file_entries = stored.get("data")
            else:
                payload = {
                    "status": "error",
                    "message": "file_list_not_found",
                    "file_list_name": name,
                }
                out = json.dumps(payload)
                return out
        else:
            # attempt to identify a default 'file_list' or 'file_check_log.json'
            if "file_list" in data and isinstance(data["file_list"], list):
                file_entries = data["file_list"]
            elif "file_check_log.json" in data and isinstance(
                data["file_check_log.json"].get("data"), list
            ):
                file_entries = data["file_check_log.json"]["data"]
            else:
                payload = {"status": "error", "message": "no_file_entries_provided"}
                out = json.dumps(payload)
                return out

        # utility to obtain size from different entry formats
        def entry_size(entry):
            pass
            if isinstance(entry, dict):
                if "size" in entry and isinstance(entry["size"], (int, float)):
                    return int(entry["size"])
                # the entry might be nested
                if (
                    "metadata" in entry
                    and isinstance(entry["metadata"], dict)
                    and "size" in entry["metadata"]
                ):
                    return int(entry["metadata"]["size"])
                # might contain a path that we can reference
                path = entry.get("path") or entry.get("file_path")
            else:
                path = entry

            # retrieve size using the path
            if path:
                # verify file_index
                idx = data.get("file_index", {}).values()
                if (
                    isinstance(idx, dict)
                    and path in idx
                    and isinstance(idx[path].get("size"), (int, float))
                ):
                    return int(idx[path]["size"])
                for item in data.get("files", {}).values() or []:
                    if (
                        isinstance(item, dict)
                        and item.get("path") == path
                        and isinstance(item.get("size"), (int, float))
                    ):
                        return int(item["size"])
                for server in data.get("file_system", {}).values() or []:
                    for f in server.get("files", []) or []:
                        if f.get("path") == path and isinstance(
                            f.get("size"), (int, float)
                        ):
                            return int(f.get("size"))
            # size is unspecified
            return None

        total = 0
        unknown: list[str] = []
        for e in file_entries.values():
            s = entry_size(e)
            if s is None:
                # attempt to display useful information
                if isinstance(e, dict):
                    unknown.append(e.get("path") or str(e))
                else:
                    unknown.append(str(e))
            else:
                total += s

        if unknown:
            payload = {"status": "error", "message": "unknown_sizes", "unknown": unknown}
            out = json.dumps(payload)
            return out

        # save a deterministic field for subsequent tools
        data["last_total_size"] = total
        payload = {"status": "success", "total_size": total}
        out = json.dumps(payload)
        return out
class VerifyRemoteChecksumTool(Tool):
    """Confirms the checksum of the transferred archive on the remote host."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verifyRemoteChecksum",
                "description": "Checks the integrity of the archive file on the remote storage by comparing checksums. Simulates 'ssh remote sha256sum -c'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "remote_path": {"type": "string"},
                        "expected_checksum": {"type": "string"},
                    },
                    "required": ["remote_path"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        remote_path: str,
        expected_checksum: str = None
    ) -> str:
        remote_file = next(
            (
                f
                for f in data.get("remote_storage", {}).values()
                if f["path"] == remote_path
            ),
            None,
        )
        if not remote_file:
            payload = {
                "status": "error",
                "error": "remote_file_not_found",
                "remote_path": remote_path,
            }
            out = json.dumps(payload)
            return out

        # If the caller has not supplied an expected checksum, consider the remote stored checksum as the definitive value
        if expected_checksum is None:
            expected_checksum = remote_file.get("checksum")

        if remote_file.get("checksum") == expected_checksum:
            payload = {"status": "verified"}
            out = json.dumps(payload)
            return out

        payload = {
            "status": "failed",
            "error": "Checksum mismatch.",
            "expected": remote_file.get("checksum"),
            "got": expected_checksum,
        }
        out = json.dumps(payload)
        return out
class LogTaskCompletionTool(Tool):
    """Records the completion information of a task in a central log."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogTaskCompletion",
                "description": "Logs the result and notes of a completed task to the task_log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "task_name": {"type": "string"},
                        "result": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["task_id", "task_name", "result"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        log_entry: dict[str, Any] = None,
        task_id: Any = None,
        task_name: str = None,
        result: str = None,
        timestamp: str = None,
        notes: str = None,
        severity: str = None, timestamp_format: Any = None) -> str:
        if "task_log" not in data:
            data["task_log"] = []
        log = log_entry
        data["task_log"].append(log)
        payload = {"status": "logged", "entry": log}
        out = json.dumps(payload)
        return out
class UpdateArchiveStatusTool(Tool):
    """Modifies the status of a task in the archive_instructions database."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateArchiveStatus",
                "description": "Finds an archive instruction by its 'archive_id' and updates its 'status' field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_id": {
                            "type": "string",
                            "description": "The ID of the archive task to update (e.g., 'arch_001').",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status to set (e.g., 'completed', 'failed').",
                        },
                    },
                    "required": ["archive_id", "status"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], archive_id: str = None, status: str = None) -> str:
        archive_task = next(
            (
                t
                for t in data.get("archive_instructions", {}).values()
                if t.get("archive_id") == archive_id
            ),
            None,
        )
        if archive_task:
            archive_task["status"] = status
            payload = {"status": "success", "archive_id": archive_id, "new_status": status}
            out = json.dumps(payload)
            return out
        payload = {"error": f"Archive ID {archive_id} not found."}
        out = json.dumps(payload)
        return out
class ParseArchiveInstructionsTool(Tool):
    """Interprets user instructions for generating and moving an archive."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ParseArchiveInstructions",
                "description": "Loads and validates instructions for an archival task.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_name": {"type": "string"},
                        "destination_directory": {"type": "string"},
                        "remote_address": {"type": "string"},
                        "files_to_archive": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": [
                        "archive_name",
                        "destination_directory",
                        "remote_address",
                        "files_to_archive",
                    ],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        instructions: dict[str, Any] = None,
        archive_name: Any = None,
        destination_directory: str = None,
        remote_address: str = None,
        files_to_archive: list = None,
        compression_level: int = None,
        encryption_key_id: str = None,
        retention_days: int = None,
        archive_tier: str = None, encryption_enabled: Any = None,
        create_manifest: Any = None,
        verify_after_creation: Any = None,
        ) -> str:
        data["archive_instruct"] = instructions
        payload = {"status": "success", "instructions": instructions}
        out = json.dumps(payload)
        return out
class ValidateFilesExistTool(Tool):
    """Verifies the existence of all specified files for archiving."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateFilesExist",
                "description": "Validates that all file paths in a list exist in the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_paths": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["file_paths"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], file_paths: list[str] = None, check_permissions: bool = None, minimum_size_bytes: int = None) -> str:
        existing_paths = {f["path"] for f in data.get("remote_files", {}).values()}
        missing_files = [p for p in file_paths.values() if p not in existing_paths]
        if missing_files:
            payload = {"status": "failed", "missing_files": missing_files}
            out = json.dumps(payload)
            return out
        payload = {"status": "success", "all_files_exist": True}
        out = json.dumps(payload)
        return out
class CreateTarArchiveTool(Tool):
    """Emulates the creation of a compressed tar archive."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createTarArchive",
                "description": "Creates a compressed .tar.gz archive with a timestamp from a list of files.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "base_archive_name": {"type": "string"},
                        "file_paths": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["base_archive_name", "file_paths"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], base_archive_name: str, file_paths: list[str]) -> str:
        archive_name = f"{base_archive_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.tar.gz"
        # Compute the total size of files to ascertain archive size
        total_size = sum(
            f["size"]
            for f in data.get("remote_files", {}).values()
            if f["path"] in file_paths
        )
        archive_size = int(total_size * 0.7)  # Estimate of the compression ratio
        data["archive_file"] = {
            "name": archive_name,
            "size": archive_size,
            "original_size": total_size,
        }
        payload = data["archive_file"]
        out = json.dumps(payload)
        return out
class TransferArchiveRsyncTool(Tool):
    """Emulates the transfer of an archive to a remote location using rsync."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transferArchiveRsync",
                "description": "Transfers the created archive file to a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_name": {"type": "string"},
                        "remote_address": {"type": "string"},
                        "destination_path": {"type": "string"},
                    },
                    "required": ["archive_name", "remote_address", "destination_path"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], destination_path: str, archive_name: str, remote_address: str) -> str:
        if "remote_storage" not in data:
            data["remote_storage"] = []
        remote_file = {
            "path": f"{destination_path}/{archive_name}",
            "remote_address": remote_address,
        }
        data["remote_storage"].append(remote_file)
        payload = {"status": "success", "transferred_file": remote_file}
        out = json.dumps(payload)
        return out
class DeleteSourceFilesTool(Tool):
    """Removes the original source files once they have been processed successfully."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteSourceFiles",
                "description": "Deletes the original source files after they have been successfully archived and transferred.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_paths": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of original file paths to delete.",
                        }
                    },
                    "required": ["file_paths"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], file_paths: list[str]) -> str:
        paths_to_delete = set(file_paths)
        original_count = len(data.get("remote_files", {}))
        data["remote_files"] = [
            f for f in data.get("remote_files", {}).values() if f["path"] not in paths_to_delete
        ]
        payload = {
            "status": "success",
            "deleted_count": original_count - len(data["remote_files"]),
        }
        out = json.dumps(payload)
        return out
TOOLS = [
    UpdateArchiveStatusTool(),
    FindIncompleteTasksTool(),
    ExtractTaskInstructionsTool(),
    SlackMessageDispatcherTool(),
    SshConnectivityVerifierTool(),
    TmuxSessionManagerTool(),
    GetIdleCpuCountTool(),
    FindAndStatFilesTool(),
    FilterFileLogTool(),
    AddHeaderToFileLogTool(),
    ComputeChecksumTool(),
    CopyFileToHostTool(),
    VerifyLocalChecksumTool(),
    LocalCleanupTool(),
    RemoteCleanupTool(),
    UpdateTaskStatusTool(),
    ParseDirectoryRestructureInstructionsTool(),
    CreateFileListForMoveTool(),
    GetDiskSpaceTool(),
    VerifySpaceRequirementsTool(),
    PopulateChecksumsInFileListTool(),
    ComputeAndResolveDestinationPathsTool(),
    CopyAndVerifyFilesTool(),
    CleanOriginalDirectoryTool(),
    ParseArchiveInstructionsTool(),
    ValidateFilesExistTool(),
    CalculateTotalSizeTool(),
    CreateTarArchiveTool(),
    TransferArchiveRsyncTool(),
    VerifyRemoteChecksumTool(),
    DeleteSourceFilesTool(),
    LogTaskCompletionTool(),
]
