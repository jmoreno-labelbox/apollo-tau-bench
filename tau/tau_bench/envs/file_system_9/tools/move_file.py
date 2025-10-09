from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class MoveFile(Tool):
    """Transfers a file from a source location to a target location."""

    @staticmethod
    def invoke(data: dict[str, Any], source_path: str = None, destination_path: str = None) -> str:
        file_to_move = None
        source_directory = None

        for server in data.get("file_system", {}).values():
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

        for server in data.get("file_system", {}).values():
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
