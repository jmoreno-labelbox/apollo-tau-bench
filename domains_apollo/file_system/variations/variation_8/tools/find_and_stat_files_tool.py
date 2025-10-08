from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

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
        for server in data.get("file_system", []):
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
