from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

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
            for item in data["remote_storage"]:
                path = item.get("path")
                basename = path.split("/")[-1] if path else None
                if path in files_to_delete or basename in files_to_delete:
                    deleted.append(path)
                else:
                    remaining.append(item)
            data["remote_storage"] = remaining

        # Delete files located in server directories
        for server in data.get("file_system", []):
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
