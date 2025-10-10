# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TransferFile(Tool):
    """Simulates transferring a file by creating its record on the destination server in file_system.json. Creates server and directory if they do not exist."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        source_path = kwargs.get("source_path")
        destination_full_path = kwargs.get("destination_path")

        source_file_details = None
        file_found = False
        source_server_hostname = None
        for server in list(data.get("file_system", {}).values()):
            for directory in server.get("directories", []):
                for file in directory.get("files", []):
                    if f"{directory.get('path')}/{file.get('filename')}" == source_path:
                        source_file_details = file.copy()
                        source_server_hostname = server.get("hostname")
                        file_found = True
                        break
                if file_found: break
            if file_found: break
        
        if not source_file_details:
             # Check if the source path includes a server name (for inter-server transfers)
            try:
                source_hostname, path = source_path.split(":", 1)
                for server in list(data.get("file_system", {}).values()):
                    if server.get("hostname") == source_hostname:
                         for directory in server.get("directories", []):
                            for file in directory.get("files", []):
                                if f"{directory.get('path')}/{file.get('filename')}" == path:
                                    source_file_details = file.copy()
                                    source_server_hostname = server.get("hostname")
                                    file_found = True
                                    break
                            if file_found: break
                    if file_found: break
            except ValueError:
                pass # Not a server-specified path
        
        if not source_file_details:
            return json.dumps({"error": f"Source file not found: {source_path}"})

        try:
            dest_hostname, dest_path = destination_full_path.split(":", 1)
            dest_dir_path = "/".join(dest_path.split("/")[:-1])
            dest_filename = dest_path.split("/")[-1]
        except ValueError:
            return json.dumps({"error": "Invalid destination format. Expected 'hostname:/path/to/file'"})

        dest_server = None
        for server in data["file_system"]:
            if server.get("hostname") == dest_hostname:
                dest_server = server
                break
        
        if not dest_server:
            max_id = 0
            for s in data["file_system"]:
                try:
                    current_id_num = int(s.get("server_id", "srv_000").split("_")[1])
                    if current_id_num > max_id:
                        max_id = current_id_num
                except (IndexError, ValueError):
                    continue
            new_id_num = max_id + 1
            new_server_id = f"srv_{new_id_num:03d}"
            dest_server = {"server_id": new_server_id, "hostname": dest_hostname, "directories": []}
            data["file_system"].append(dest_server)

        dest_directory = None
        for directory in dest_server["directories"]:
            if directory.get("path") == dest_dir_path:
                dest_directory = directory
                break

        if not dest_directory:
            dest_directory = {"path": dest_dir_path, "files": []}
            dest_server["directories"].append(dest_directory)
        
        new_file_entry = source_file_details
        new_file_entry["filename"] = dest_filename
        dest_directory["files"].append(new_file_entry)

        return json.dumps({"status": "success", "message": f"File transferred from {source_path} to {destination_full_path}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_file",
                "description": "Simulates transferring a file by creating its record on the destination server in file_system.json. Creates server and directory if they do not exist.",
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
