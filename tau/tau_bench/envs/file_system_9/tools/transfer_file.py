from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class TransferFile(Tool):
    """Emulates the transfer of a file by establishing its record on the destination server in file_system.json. Creates the server and directory if they are absent."""

    @staticmethod
    def invoke(data: dict[str, Any], source_path: str = None, destination_path: str = None) -> str:
        source_file_details = None
        file_found = False
        for server in data.get("file_system", {}).values():
            for directory in server.get("directories", []):
                for file in directory.get("files", []):
                    if f"{directory.get('path')}/{file.get('filename')}" == source_path:
                        source_file_details = file.copy()
                        server.get("hostname")
                        file_found = True
                        break
                if file_found:
                    break
            if file_found:
                break

        if not source_file_details:
            # Verify if the source path contains a server name (for transfers between servers)
            try:
                source_hostname, path = source_path.split(":", 1)
                for server in data.get("file_system", {}).values():
                    if server.get("hostname") == source_hostname:
                        for directory in server.get("directories", []):
                            for file in directory.get("files", []):
                                if (
                                    f"{directory.get('path')}/{file.get('filename')}"
                                    == path
                                ):
                                    source_file_details = file.copy()
                                    server.get("hostname")
                                    file_found = True
                                    break
                            if file_found:
                                break
                    if file_found:
                        break
            except ValueError:
                pass  # Path not designated for a server

        if not source_file_details:
            payload = {"error": f"Source file not found: {source_path}"}
            out = json.dumps(payload)
            return out

        try:
            dest_hostname, dest_path = destination_path.split(":", 1)
            dest_dir_path = "/".join(dest_path.split("/")[:-1])
            dest_filename = dest_path.split("/")[-1]
        except ValueError:
            payload = {
                "error": "Invalid destination format. Expected 'hostname:/path/to/file'"
            }
            out = json.dumps(payload)
            return out

        dest_server = None
        for server in data["file_system"].values():
            if server.get("hostname") == dest_hostname:
                dest_server = server
                break

        if not dest_server:
            max_id = 0
            for s in data["file_system"].values():
                try:
                    current_id_num = int(s.get("server_id", "srv_000").split("_")[1])
                    if current_id_num > max_id:
                        max_id = current_id_num
                except (IndexError, ValueError):
                    continue
            new_id_num = max_id + 1
            new_server_id = f"srv_{new_id_num:03d}"
            dest_server = {
                "server_id": new_server_id,
                "hostname": dest_hostname,
                "directories": [],
            }
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
        payload = {
            "status": "success",
            "message": f"File transferred from {source_path} to {destination_path}.",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TransferFile",
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
