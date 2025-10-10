# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
    def invoke(data: Dict[str, Any], session_to_kill, files_to_delete = []) -> str:
        files_to_delete = set(files_to_delete)
        deleted: List[str] = []

        # Eliminate top-level keys that correspond to files_to_delete.
        for key in list(files_to_delete):
            if data.pop(key, None) is not None:
                deleted.append(key)

        # Eliminate entries in remote_storage by comparing path or basename.
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

        # Delete files located in server directories.
        for server in data.get("file_system", []):
            for directory in server.get("directories", []):
                remaining_files = []
                for f in directory.get("files", []):
                    # Manage file entries as both strings and dictionaries.
                    if isinstance(f, str):
                        full_path = f"{directory.get('path', '')}/{f}".replace("//", "/")
                        name = f
                    else: # represents a dictionary
                        name = f.get("name") # Securely retrieve the name.
                        full_path = f"{directory.get('path', '')}/{name}".replace("//", "/")

                    if full_path in files_to_delete or name in files_to_delete:
                        deleted.append(full_path)
                    else:
                        remaining_files.append(f)
                directory["files"] = remaining_files

        # Terminate the tmux session if requested.
        session = session_to_kill
        session_killed = False
        if session and "tmux_sessions" in data and session in data["tmux_sessions"]:
            data["tmux_sessions"].remove(session)
            session_killed = True

        # Remove duplicates from the deleted list.
        deleted = list(dict.fromkeys(deleted))

        return json.dumps({"status": "success", "deleted_remote_files": deleted, "session_killed": session_killed})
