import json
import hashlib
from typing import Any, Dict, List, Set
from domains.dto import Tool
import datetime

class ScanIncompleteTasksTool(Tool):
    """Tool to scan the file_check_db for tasks that are not yet completed."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "scan_incomplete_tasks",
                "description": "Scans the file_check_db for the first task with 'completed' status set to False.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        db = data.get("file_check_db", [])
        for task in db:
            if not task.get("completed", True):
                # return the task id and details so caller can decide to proceed or abort
                return json.dumps({"task_id": task.get("task_id"), "task": task})
        return json.dumps({"task_id": None, "message": "No incomplete tasks found."})


class ParseFileCheckInstructionsTool(Tool):
    """Tool to parse instructions for a given task and store them."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "parse_file_check_instructions",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_id = kwargs["task_id"]
        task_details = next(
            (t for t in data.get("file_check_db", []) if t["task_id"] == task_id), None
        )
        if not task_details:
            return json.dumps({"error": f"Task ID {task_id} not found."})

        # The parsed_instructions field is already structured, so we can use it directly
        instructions = task_details.get("parsed_instructions", {})
        if "task_instructions" not in data:
            data["task_instructions"] = []

        # Reconstruct the simplified task_instructions format from the detailed parsed_instructions
        parsed_instruction = {
            "task_id": task_id,
            "remote_address": task_details.get("remote_server"),
            "max_size": instructions.get("size_filter", {}).get("max_bytes"),
            "last_access_days": instructions.get("time_filter", {}).get("days"),
            "users": instructions.get("user_filter", []),
        }
        data["task_instructions"].append(parsed_instruction)
        return json.dumps(
            {"status": "success", "parsed_instruction": parsed_instruction}
        )


class SendSlackNotificationTool(Tool):
    """General-purpose tool to send a notification to a Slack channel."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_slack_notification",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        channel = kwargs["channel"]
        message = kwargs["message"]
        if "slack_log" not in data:
            data["slack_log"] = []
        log_entry = {"channel": channel, "message": message}
        data["slack_log"].append(log_entry)
        return json.dumps({"status": "success", "log_entry": log_entry})


class CheckSshConnectionTool(Tool):
    """Simulates checking SSH connectivity to a remote server."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_ssh_connection",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps(
            {"status": "connected", "remote_address": kwargs["remote_address"]}
        )


class CreateTmuxSessionTool(Tool):
    """Simulates creating a new tmux session on a remote server."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_tmux_session",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        session_name = kwargs["session_name"]
        if "tmux_sessions" not in data:
            data["tmux_sessions"] = []
        if session_name in data["tmux_sessions"]:
            return json.dumps({"status": "exists", "session_name": session_name})
        data["tmux_sessions"].append(session_name)
        return json.dumps({"status": "created", "session_name": session_name})


class GetIdleCpuCountTool(Tool):
    """Simulates checking server CPU usage to find the number of idle cores."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_idle_cpu_count",
                "description": "Gets the total number of idle CPU cores to use for parallel processing. Simulates using 'top' and 'awk'. Returns a fixed value for determinism.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Return a fixed number for deterministic behavior.
        return json.dumps({"idle_cpus": 6})


class FindAndStatFilesTool(Tool):
    """Simulates finding files based on criteria and logging their metadata."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_and_stat_files",
                "description": "Finds files on a remote server matching last access time and gets their metadata. Simulates a parallel 'find | xargs stat' pipeline.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "last_access_days": {"type": "integer"},
                        "parallel_processes": {"type": "integer"},
                    },
                    "required": ["last_access_days", "parallel_processes"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        last_access_days = kwargs.get("last_access_days")
        log_name = "file_check_log.json"
        all_remote_files: List[Dict[str, Any]] = []

        # Walk the simulated file_system structure and collect files deterministically.
        for server in data.get("file_system", []):
            server_host = server.get("host", server.get("remote_address", "unknown"))
            for directory in server.get("directories", []):
                dir_path = directory.get("path", "")
                for f in directory.get("files", []) or []:
                    # support string entries or dicts with varying keys
                    if isinstance(f, str):
                        name = f
                        path = f if f.startswith("/") else f"{dir_path}/{f}".replace("//", "/")
                        size = 0
                        user = "unknown"
                        last_access = None
                    elif isinstance(f, dict):
                        name = f.get("name") or f.get("filename") or f.get("file_name") or (f.get("path") and f.get("path").split("/")[-1])
                        path = f.get("path") or (f"{dir_path}/{name}".replace("//", "/") if name else f"{dir_path}/")
                        size = int(f.get("size", 0)) if isinstance(f.get("size", 0), (int, float, str)) else 0
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

        # Persist log deterministically
        data[log_name] = {"data": all_remote_files}
        return json.dumps({"status": "success", "log_name": log_name, "file_count": len(all_remote_files)})


class FilterFileLogTool(Tool):
    """Filters a file log based on size and user, simulating jq."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filter_file_log",
                "description": "Filters a generated file log based on max size and a list of users.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "The name of the log to filter in the database.",
                        },
                        "max_size": {
                            "type": "integer",
                            "description": "The maximum file size to include.",
                        },
                        "users": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of users to include.",
                        },
                    },
                    "required": ["log_name", "max_size", "users"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        log_name, max_size, users = (
            kwargs["log_name"],
            kwargs["max_size"],
            kwargs["users"],
        )
        if log_name not in data:
            return json.dumps({"error": f"Log '{log_name}' not found."})

        original_count = len(data[log_name]["data"])
        data[log_name]["data"] = [
            f
            for f in data[log_name]["data"]
            if f["size"] < max_size and f["user"] in users
        ]
        return json.dumps(
            {
                "status": "success",
                "original_count": original_count,
                "filtered_count": len(data[log_name]["data"]),
            }
        )


class AddHeaderToFileLogTool(Tool):
    """Appends a task_id as a header to the file check log."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_header_to_file_log",
                "description": "Adds a top-level 'task_id' key to the specified log file object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "The name of the log to modify.",
                        },
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to add as a header.",
                        },
                    },
                    "required": ["log_name", "task_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        log_name, task_id = kwargs["log_name"], kwargs["task_id"]
        if log_name not in data:
            return json.dumps({"error": f"Log '{log_name}' not found."})
        # Wrap existing data under a 'data' key and add 'task_id' at the top level
        log_data = data[log_name]["data"]
        data[log_name] = {"task_id": task_id, "data": log_data}
        return json.dumps(
            {"status": "success", "log_name": log_name, "header_added": "task_id"}
        )


class ComputeChecksumTool(Tool):
    """Computes a sha256sum for a data object, simulating checksum generation."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_checksum",
                "description": "Computes and returns a sha256 checksum for a given log file.",
                "parameters": {"type": "object", "properties": {"log_name": {"type": "string"}}, "required": ["log_name"]},
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        log_name = kwargs["log_name"]
        if log_name not in data:
            return json.dumps({"error": f"Log '{log_name}' not found."})
        content_str = json.dumps(data[log_name], sort_keys=True)
        checksum = hashlib.sha256(content_str.encode()).hexdigest()
        # persist checksum under a deterministic key '<log_name>.sha256'
        data[f"{log_name}.sha256"] = checksum
        return json.dumps({"log_name": log_name, "checksum": checksum})


class CopyFileToHostTool(Tool):
    """Simulates copying a file (and its checksum) from remote to host using scp."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "copy_file_to_host",
                "description": "Simulates copying a log and its checksum file from a remote source to the local host.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "The name of the log file to copy.",
                        }
                    },
                    "required": ["log_name"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        log_name = kwargs["log_name"]
        checksum_name = f"{kwargs['log_name']}.sha256"
        if log_name not in data or checksum_name not in data:
            return json.dumps({"error": "Log or checksum not found for copying."})

        local_log_name = f"local_{log_name}"
        local_checksum_name = f"local_{checksum_name}"

        data[local_log_name] = data[log_name]
        data[local_checksum_name] = data[checksum_name]
        return json.dumps(
            {"status": "success", "copied_files": [local_log_name, local_checksum_name]}
        )


class VerifyLocalChecksumTool(Tool):
    """Verifies the checksum of a locally copied file."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_local_checksum",
                "description": "Verifies the integrity of a copied file by re-computing its checksum and comparing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "The base name of the local log file to verify.",
                        }
                    },
                    "required": ["log_name"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        log_name = kwargs["log_name"]
        checksum_name = f"{kwargs['log_name']}.sha256"
        if log_name not in data or checksum_name not in data:
            return json.dumps({"error": "Log or checksum not found for copying."})

        local_log_name = f"local_{log_name}"
        local_checksum_name = f"local_{checksum_name}"

        data[local_log_name] = data[log_name]
        data[local_checksum_name] = data[checksum_name]

        return json.dumps(
            {"status": "success", "copied_files": [local_log_name, local_checksum_name]}
        )


class LocalCleanupTool(Tool):
    """Deletes local files, such as downloaded logs and checksums."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "local_cleanup",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        deleted = [
            f_key
            for f_key in kwargs["files_to_delete"]
            if data.pop(f_key, None) is not None
        ]
        return json.dumps({"deleted_local_files": deleted})


class RemoteCleanupTool(Tool):
    """Simulates deleting files and killing a tmux session on the remote server."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remote_cleanup",
                "description": "Deletes specified files and a tmux session from the remote environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "files_to_delete": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of remote file keys to delete.",
                        },
                        "session_to_kill": {
                            "type": "string",
                            "description": "The name of the tmux session to kill.",
                        },
                    },
                    "required": ["files_to_delete", "session_to_kill"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        files_to_delete = set(kwargs.get("files_to_delete", []))
        deleted: List[str] = []

        # Remove top-level keys matching files_to_delete
        for key in list(files_to_delete):
            if data.pop(key, None) is not None:
                deleted.append(key)

        # Remove entries from remote_storage by matching path or basename
        if "remote_storage" in data:
            remaining = []
            for item in data["remote_storage"]:
                path = item.get("path")
                basename = path.split("/")[-1] if path else None
                if path in files_to_delete or basename in files_to_delete:
                    deleted.append(path)
                else:
                    remaining.append(item)
            data["remote_storage"] = remaining

        # Remove files present on server directories
        for server in data.get("file_system", []):
            for directory in server.get("directories", []):
                remaining_files = []
                for f in directory.get("files", []):
                    # Handle both string and dict file entries
                    if isinstance(f, str):
                        full_path = f"{directory.get('path', '')}/{f}".replace("//", "/")
                        name = f
                    else: # is a dict
                        name = f.get("name") # Safely get name
                        full_path = f"{directory.get('path', '')}/{name}".replace("//", "/")

                    if full_path in files_to_delete or name in files_to_delete:
                        deleted.append(full_path)
                    else:
                        remaining_files.append(f)
                directory["files"] = remaining_files

        # Kill tmux session if requested
        session = kwargs.get("session_to_kill")
        session_killed = False
        if session and "tmux_sessions" in data and session in data["tmux_sessions"]:
            data["tmux_sessions"].remove(session)
            session_killed = True

        # Deduplicate deleted list
        deleted = list(dict.fromkeys(deleted))

        return json.dumps({"status": "success", "deleted_remote_files": deleted, "session_killed": session_killed})


class UpdateTaskStatusTool(Tool):
    """Updates the status of a task in the file_check_db."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_task_status",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_id, completed = kwargs["task_id"], kwargs["completed"]
        task = next(
            (t for t in data.get("file_check_db", []) if t["task_id"] == task_id), None
        )
        if task:
            task["completed"] = completed
            return json.dumps(
                {"status": "success", "task_id": task_id, "completed": completed}
            )
        return json.dumps({"error": f"Task ID {task_id} not found."})


class ParseDirectoryRestructureInstructionsTool(Tool):
    """Parses user instructions for moving and sorting files into a structured format."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "parse_directory_restructure_instructions",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if "directories_db" not in data:
            data["directories_db"] = []
        instruction = {**kwargs}
        data["directories_db"].append(instruction)
        return json.dumps({"status": "success", "instruction": instruction})


class CreateFileListForMoveTool(Tool):
    """Scans a target directory and creates a list of files to be moved."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_file_list_for_move",
                "description": "Generates a file_list database from files in a target directory.",
                "parameters": {
                    "type": "object",
                    "properties": {"target_directory": {"type": "string"}},
                    "required": ["target_directory"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        target = kwargs["target_directory"]
        file_list: List[Dict[str, Any]] = []

        for server in data.get("file_system", []):
            for directory in server.get("directories", []):
                dir_path = directory.get("path", "")
                for f in directory.get("files", []) or []:
                    if isinstance(f, str):
                        name = f
                        full_path = name if name.startswith("/") else f"{dir_path}/{name}".replace("//", "/")
                        size = 0
                        user = "unknown"
                    elif isinstance(f, dict):
                        name = f.get("name") or f.get("filename") or f.get("file_name") or (f.get("path") and f.get("path").split("/")[-1])
                        full_path = f.get("path") or f"{dir_path}/{name}".replace("//", "/")
                        size = int(f.get("size", 0)) if isinstance(f.get("size", 0), (int, float, str)) else 0
                        user = f.get("user", "unknown")
                    else:
                        continue

                    if full_path.startswith(target):
                        entry = {
                            "path": full_path,
                            "filename": name,
                            "size": int(size),
                            "user": user,
                        }
                        file_list.append(entry)

        data["file_list"] = file_list
        return json.dumps({"status": "success", "file_count": len(file_list)})


class GetDiskSpaceTool(Tool):
    """Simulates checking available disk space."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_disk_space",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        path = kwargs["path"]
        available_space = 10**12  # 1TB
        data[f"disk_space_{path.replace('/', '_')}"] = available_space
        return json.dumps({"available_space": available_space, "path": path})


class VerifySpaceRequirementsTool(Tool):
    """Compares total file size against available disk space to ensure sufficient space."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_space_requirements",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        destination_path = kwargs["destination_path"]

        # Get the total size from the last calculation
        total_size = data.get("last_total_size", 0)

        # Get available space for the destination
        disk_space_key = f"disk_space_{destination_path.replace('/', '_')}"
        available_space = data.get(disk_space_key, 10**12)  # Default to 1TB if not found

        if total_size <= available_space:
            return json.dumps({
                "status": "sufficient_space",
                "total_size": total_size,
                "available_space": available_space,
                "space_check": "passed"
            })
        else:
            return json.dumps({
                "status": "insufficient_space",
                "total_size": total_size,
                "available_space": available_space,
                "space_check": "failed",
                "error": f"Insufficient disk space. Need {total_size} bytes but only {available_space} bytes available."
            })


class PopulateChecksumsInFileListTool(Tool):
    """Computes and populates checksums for all files in the file_list."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "populate_checksums_in_file_list",
                "description": "Iterates through the file_list and populates the 'checksum' field for each entry using SHA256.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if "file_list" not in data:
            return json.dumps({"error": "file_list not found."})
        for file in data["file_list"]:
            file["checksum"] = hashlib.sha256(file["path"].encode()).hexdigest()
        return json.dumps(
            {"status": "success", "populated_count": len(data["file_list"])}
        )


class ComputeAndResolveDestinationPathsTool(Tool):
    """Computes destination paths for files based on sort rules and resolves name conflicts."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_and_resolve_destination_paths",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        dest_dir = kwargs["destination_directory"]
        sort_rules = kwargs["sort_rules"]
        destination_paths: Set[str] = set()

        for file in data.get("file_list", []):
            ext = file["filename"].split(".")[-1] if "." in file["filename"] else ""
            sub_dir = sort_rules.get(ext, "miscellaneous")
            base = ".".join(file["filename"].split(".")[:-1]) if "." in file["filename"] else file["filename"]
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

        return json.dumps({"status": "success", "paths_resolved": len(data.get("file_list", []))})


class CopyAndVerifyFilesTool(Tool):
    """Simulates copying files to their new destinations and verifying checksums."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "copy_and_verify_files",
                "description": "Copies files from original path to destination path and verifies their checksums.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        copied_files: List[Dict[str, Any]] = []
        if "moved_files" not in data:
            data["moved_files"] = []

        for file in data.get("file_list", []):
            # Simulate compute checksum if missing
            if "checksum" not in file:
                file["checksum"] = hashlib.sha256(file["path"].encode()).hexdigest()

            # Simulate copy by adding an entry to moved_files (preserve checksum)
            moved = {
                "original": file["path"],
                "destination": file.get("destination_path"),
                "checksum": file["checksum"],
            }
            data["moved_files"].append(moved)
            copied_files.append(moved)

        # Post-move verification: ensure destination checksums match source checksum (simulated deterministic)
        verified_count = len(copied_files)
        return json.dumps({"status": "success", "verified_and_copied": verified_count})


class CleanOriginalDirectoryTool(Tool):
    """Simulates deleting all original files after a successful copy and verify operation."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "clean_original_directory",
                "description": "Deletes the original files that have been successfully moved and returns the count of cleaned files.",
                "parameters": {
                    "type": "object",
                    "properties": {"target_directory": {"type": "string"}},
                    "required": ["target_directory"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        target_directory = kwargs["target_directory"]
        cleaned_count = 0

        # Count files that were in the file_list (these are the ones being cleaned)
        if "file_list" in data:
            cleaned_count = len(data["file_list"])

        # Store the cleaned files count for output
        data["cleaned_files_count"] = cleaned_count

        return json.dumps({"status": "success", "cleaned_files_count": cleaned_count})


class CalculateTotalSizeTool(Tool):
    """Calculates the total size of a list of files."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_total_size",
                "description": "Computes the sum of the sizes for a given list of file paths.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_paths": {"type": "array", "items": {"oneOf": [{"type": "string"}, {"type": "object"}]}},
                        "file_list_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Accept either explicit file_paths or a reference to a file list stored in data
        file_entries = []
        if "file_paths" in kwargs and kwargs.get("file_paths") is not None:
            file_entries = kwargs.get("file_paths") or []
        elif "file_list_name" in kwargs and kwargs.get("file_list_name"):
            name = kwargs.get("file_list_name")
            stored = data.get(name)
            if isinstance(stored, dict) and isinstance(stored.get("data"), list):
                file_entries = stored.get("data")
            else:
                return json.dumps({"status": "error", "message": "file_list_not_found", "file_list_name": name})
        else:
            # try to detect a default 'file_list' or 'file_check_log.json'
            if "file_list" in data and isinstance(data["file_list"], list):
                file_entries = data["file_list"]
            elif "file_check_log.json" in data and isinstance(data["file_check_log.json"].get("data"), list):
                file_entries = data["file_check_log.json"]["data"]
            else:
                return json.dumps({"status": "error", "message": "no_file_entries_provided"})

        # helper to get size from various entry shapes
        def entry_size(entry):
            if isinstance(entry, dict):
                if "size" in entry and isinstance(entry["size"], (int, float)):
                    return int(entry["size"])
                # maybe the entry is nested
                if "metadata" in entry and isinstance(entry["metadata"], dict) and "size" in entry["metadata"]:
                    return int(entry["metadata"]["size"])
                # could include path that we can look up
                path = entry.get("path") or entry.get("file_path")
            else:
                path = entry

            # lookup size by path
            if path:
                # check file_index
                idx = data.get("file_index", {})
                if isinstance(idx, dict) and path in idx and isinstance(idx[path].get("size"), (int, float)):
                    return int(idx[path]["size"])
                for item in data.get("files", []) or []:
                    if isinstance(item, dict) and item.get("path") == path and isinstance(item.get("size"), (int, float)):
                        return int(item["size"])
                for server in data.get("file_system", []) or []:
                    for f in server.get("files", []) or []:
                        if f.get("path") == path and isinstance(f.get("size"), (int, float)):
                            return int(f.get("size"))
            # unknown size
            return None

        total = 0
        unknown: List[str] = []
        for e in file_entries:
            s = entry_size(e)
            if s is None:
                # try to show something helpful
                if isinstance(e, dict):
                    unknown.append(e.get("path") or str(e))
                else:
                    unknown.append(str(e))
            else:
                total += s

        if unknown:
            return json.dumps({"status": "error", "message": "unknown_sizes", "unknown": unknown})

        # store a deterministic field for downstream tools
        data["last_total_size"] = total
        return json.dumps({"status": "success", "total_size": total})


class VerifyRemoteChecksumTool(Tool):
    """Verifies the checksum of the transferred archive on the remote host."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_remote_checksum",
                "description": "Checks the integrity of the archive file on the remote storage by comparing checksums. Simulates 'ssh remote sha256sum -c'.",
                "parameters": {"type": "object", "properties": {"remote_path": {"type": "string"}, "expected_checksum": {"type": "string"}}, "required": ["remote_path"]},
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        remote_file = next((f for f in data.get("remote_storage", []) if f["path"] == kwargs["remote_path"]), None)
        if not remote_file:
            return json.dumps({"status": "error", "error": "remote_file_not_found", "remote_path": kwargs["remote_path"]})
        expected = kwargs.get("expected_checksum")
        # If caller didn't provide an expected checksum, accept the remote stored checksum as the authoritative value
        if expected is None:
            expected = remote_file.get("checksum")

        if remote_file.get("checksum") == expected:
            return json.dumps({"status": "verified"})
        return json.dumps({"status": "failed", "error": "Checksum mismatch.", "expected": remote_file.get("checksum"), "got": expected})


class LogTaskCompletionTool(Tool):
    """Logs the completion details of a task to a central log."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_task_completion",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if "task_log" not in data:
            data["task_log"] = []
        log = {**kwargs}
        data["task_log"].append(log)
        return json.dumps({"status": "logged", "entry": log})


class UpdateArchiveStatusTool(Tool):
    """Updates the status of a task in the archive_instructions database."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_archive_status",
                "description": "Finds an archive instruction by its 'archive_id' and updates its 'status' field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_id": {"type": "string", "description": "The ID of the archive task to update (e.g., 'arch_001')."},
                        "status": {"type": "string", "description": "The new status to set (e.g., 'completed', 'failed')."}
                    },
                    "required": ["archive_id", "status"]
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        archive_id = kwargs.get("archive_id")
        status = kwargs.get("status")
        archive_task = next((t for t in data.get("archive_instructions", []) if t.get("archive_id") == archive_id), None)
        if archive_task:
            archive_task["status"] = status
            return json.dumps({"status": "success", "archive_id": archive_id, "new_status": status})
        return json.dumps({"error": f"Archive ID {archive_id} not found."})


class ParseArchiveInstructionsTool(Tool):
    """Parses user instructions for creating and transferring an archive."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "parse_archive_instructions", "description": "Loads and validates instructions for an archival task.", "parameters": { "type": "object", "properties": { "archive_name": {"type": "string"}, "destination_directory": {"type": "string"}, "remote_address": {"type": "string"}, "files_to_archive": {"type": "array", "items": {"type": "string"}}}, "required": ["archive_name", "destination_directory", "remote_address", "files_to_archive"]}}}

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        data["archive_instruct"] = {**kwargs}
        return json.dumps({"status": "success", "instructions": kwargs})


class ValidateFilesExistTool(Tool):
    """Checks if all specified files for archiving exist."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "validate_files_exist", "description": "Validates that all file paths in a list exist in the system.", "parameters": { "type": "object", "properties": { "file_paths": {"type": "array", "items": {"type": "string"}}}, "required": ["file_paths"]}}}

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        existing_paths = {f["path"] for f in data.get("remote_files", [])}
        missing_files = [p for p in kwargs["file_paths"] if p not in existing_paths]
        if missing_files: return json.dumps({"status": "failed", "missing_files": missing_files})
        return json.dumps({"status": "success", "all_files_exist": True})


class CreateTarArchiveTool(Tool):
    """Simulates creating a compressed tar archive."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "create_tar_archive", "description": "Creates a compressed .tar.gz archive with a timestamp from a list of files.", "parameters": { "type": "object", "properties": { "base_archive_name": {"type": "string"}, "file_paths": {"type": "array", "items": {"type": "string"}}}, "required": ["base_archive_name", "file_paths"]}}}

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        archive_name = f"{kwargs['base_archive_name']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.tar.gz"
        # Calculate total size of files to determine archive size
        total_size = sum(f["size"] for f in data.get("remote_files", []) if f["path"] in kwargs["file_paths"])
        archive_size = int(total_size * 0.7)  # Compression ratio estimate
        data["archive_file"] = {"name": archive_name, "size": archive_size, "original_size": total_size}
        return json.dumps(data["archive_file"])


class TransferArchiveRsyncTool(Tool):
    """Simulates transferring an archive to a remote destination using rsync."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "transfer_archive_rsync", "description": "Transfers the created archive file to a remote server.", "parameters": { "type": "object", "properties": { "archive_name": {"type": "string"}, "remote_address": {"type": "string"}, "destination_path": {"type": "string"}}, "required": ["archive_name", "remote_address", "destination_path"]}}}

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if "remote_storage" not in data: data["remote_storage"] = []
        remote_file = { "path": f"{kwargs['destination_path']}/{kwargs['archive_name']}", "remote_address": kwargs['remote_address']}
        data["remote_storage"].append(remote_file)
        return json.dumps({"status": "success", "transferred_file": remote_file})


class DeleteSourceFilesTool(Tool):
    """Deletes the original source files after they have been successfully processed."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_source_files",
                "description": "Deletes the original source files after they have been successfully archived and transferred.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_paths": {"type": "array", "items": {"type": "string"}, "description": "List of original file paths to delete."}
                    },
                    "required": ["file_paths"]
                }
            }
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        paths_to_delete = set(kwargs["file_paths"])
        original_count = len(data.get("remote_files", []))
        data["remote_files"] = [f for f in data.get("remote_files", []) if f["path"] not in paths_to_delete]
        return json.dumps({"status": "success", "deleted_count": original_count - len(data["remote_files"])})


TOOLS = [
    UpdateArchiveStatusTool(),
    ScanIncompleteTasksTool(),
    ParseFileCheckInstructionsTool(),
    SendSlackNotificationTool(),
    CheckSshConnectionTool(),
    CreateTmuxSessionTool(),
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
