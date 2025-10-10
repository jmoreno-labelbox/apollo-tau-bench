# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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

        # Traverse the simulated file_system layout and gather files in a consistent manner.
        for server in data.get("file_system", []):
            server_host = server.get("host", server.get("remote_address", "unknown"))
            for directory in server.get("directories", []):
                dir_path = directory.get("path", "")
                for f in directory.get("files", []) or []:
                    # handle string inputs or dictionaries with diverse keys
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

        # Ensure logs are saved in a consistent manner.
        data[log_name] = {"data": all_remote_files}
        return json.dumps({"status": "success", "log_name": log_name, "file_count": len(all_remote_files)})
