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

class FindAndStatFilesTool(Tool):
    """Emulates the search for files based on specific criteria and records their metadata."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAndStatFiles",
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
    def invoke(
        data: dict[str, Any],
        last_access_days: int = None,
        parallel_processes: Any = None,
        target_directory: str = None
    ) -> str:
        log_name = "file_check_log.json"
        all_remote_files: list[dict[str, Any]] = []

        # Traverse the simulated file_system structure to gather files in a deterministic manner.
        for server in data.get("file_system", []):
            server_host = server.get("host", server.get("remote_address", "unknown"))
            for directory in server.get("directories", []):
                dir_path = directory.get("path", "")
                for f in directory.get("files", []) or []:
                    # accommodate string entries or dictionaries with different keys.
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

        # Log persistence should be deterministic.
        data[log_name] = {"data": all_remote_files}
        payload = {
            "status": "success",
            "log_name": log_name,
            "file_count": len(all_remote_files),
        }
        out = json.dumps(payload)
        return out
