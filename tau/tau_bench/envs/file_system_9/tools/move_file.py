# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MoveFile(Tool):
    """Moves a file from a source path to a destination path."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        source_path = kwargs.get("source_path")
        destination_path = kwargs.get("destination_path")
        
        file_to_move = None
        source_directory = None

        for server in list(data.get("file_system", {}).values()):
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
            return json.dumps({"error": f"Source file not found: {source_path}"})

        source_directory["files"] = [f for f in source_directory["files"] if f"{source_directory.get('path')}/{f.get('filename')}" != source_path]

        dest_dir_path = "/".join(destination_path.split("/")[:-1])
        dest_filename = destination_path.split("/")[-1]
        
        file_to_move["filename"] = dest_filename

        for server in list(data.get("file_system", {}).values()):
            for directory in server.get("directories", []):
                if directory.get("path") == dest_dir_path:
                    directory["files"].append(file_to_move)
                    return json.dumps({"status": "success", "message": f"File moved from {source_path} to {destination_path}."})

        return json.dumps({"error": f"Destination directory not found: {dest_dir_path}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "move_file",
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
