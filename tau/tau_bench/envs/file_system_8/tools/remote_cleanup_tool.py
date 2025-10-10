# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoteCleanupTool(Tool):
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remote_cleanup",
                "description": "Deletes specified files and optionally a tmux session.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "files_to_delete": {"type": "array", "items": {"type": "string"}},
                        "session_to_kill": {"type": "string", "description": "Optional tmux session to kill."},
                    },
                    "required": ["files_to_delete"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        files_to_delete = set(kwargs.get("files_to_delete", []))
        deleted: List[str] = []

        # Eliminate primary keys that correspond to files_to_delete.
        for key in list(files_to_delete):
            if data.pop(key, None) is not None:
                deleted.append(key)

        # Eliminate entries from remote_storage by comparing path or basename.
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

        # Delete files located in the server directories.
        for server in data.get("file_system", []):
            for directory in server.get("directories", []):
                remaining_files = []
                for f in directory.get("files", []):
                    # Process file entries as either strings or dictionaries.
                    if isinstance(f, str):
                        full_path = f"{directory.get('path', '')}/{f}".replace(
                            "//", "/"
                        )
                        name = f
                    else:  # represents a dictionary
                        name = f.get("name")  # Retrieve name securely.
                        full_path = f"{directory.get('path', '')}/{name}".replace(
                            "//", "/"
                        )

                    if full_path in files_to_delete or name in files_to_delete:
                        deleted.append(full_path)
                    else:
                        remaining_files.append(f)
                directory["files"] = remaining_files

        # Terminate the tmux session if instructed.
        session = kwargs.get("session_to_kill")
        session_killed = False
        if session and "tmux_sessions" in data and session in data["tmux_sessions"]:
            data["tmux_sessions"].remove(session)
            session_killed = True

        # Remove duplicates from the deleted list.
        deleted = list(dict.fromkeys(deleted))

        return json.dumps(
            {
                "status": "success",
                "deleted_remote_files": deleted,
                "session_killed": session_killed,
            }
        )
