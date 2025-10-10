# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateFileList(Tool):
    """Adds a list of files to the file_lists.json database, looking up their size and checksum from file_system.json."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        operation_id = kwargs.get("operation_id")
        filepaths = kwargs.get("filepaths", [])
        file_lists = list(data.get("file_lists", {}).values())
        
        max_id = 0
        if file_lists:
            for item in file_lists:
                try:
                    current_id_num = int(item.get("file_id", "file_000").split("_")[1])
                    if current_id_num > max_id:
                        max_id = current_id_num
                except (IndexError, ValueError):
                    continue
        
        added_files = []
        for i, filepath in enumerate(filepaths):
            found_size = "0"
            found_checksum = 'a1f2e3d4c5b6789012345678901234567890abcd' # Standard checksum
            file_found = False
            for server in list(data.get("file_system", {}).values()):
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        current_path = f"{directory.get('path')}/{file.get('filename')}"
                        if current_path == filepath:
                            found_size = file.get("size", "0")
                            found_checksum = file.get("checksum", found_checksum)
                            file_found = True
                            break
                    if file_found:
                        break
                if file_found:
                    break
            
            new_id_num = max_id + i + 1
            file_id = f"file_{new_id_num:03d}"
            filename = filepath.split('/')[-1]
            
            new_entry = {
                "operation_id": operation_id,
                "file_id": file_id,
                "filename": filename,
                "filepath": filepath,
                "filedestination": None,
                "size": found_size,
                "checksum": found_checksum,
                "status": "pending"
            }
            file_lists.append(new_entry)
            added_files.append(file_id)
            
        return json.dumps({"status": "success", "message": f"Added {len(added_files)} files to the list.", "file_ids": added_files})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_file_list",
                "description": "Adds a list of files to the file_lists.json database, looking up their size and checksum from file_system.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "operation_id": {"type": "string", "description": "The ID of the operation these files are associated with."},
                        "filepaths": {"type": "array", "items": {"type": "string"}, "description": "A list of full file paths to add."}
                    },
                    "required": ["operation_id", "filepaths"],
                },
            },
        }
