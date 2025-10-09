from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateFileListForMoveTool(Tool):
    """Examines a target directory and generates a list of files designated for moving."""

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
