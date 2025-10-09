from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateArchive(Tool):
    """Generates a new archive instruction along with a simulated archive file in the file_system.json state."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        destination_directory: str,
        archive_name: str,
        user_id: str = None,
        remote_address: str = None,
        filepaths: list[str] = None
    ) -> str:
        # Step 1: Generate the instruction in archive_instructions.json
        archive_instructions = data.get("archive_instructions", [])
        max_id = 0
        if archive_instructions:
            for instruction in archive_instructions:
                try:
                    current_id_num = int(
                        instruction.get("archive_id", "arch_000").split("_")[1]
                    )
                    if current_id_num > max_id:
                        max_id = current_id_num
                except (IndexError, ValueError):
                    continue
        new_id_num = max_id + 1
        archive_id = f"arch_{new_id_num:03d}"

        archive_path = f"{destination_directory}/{archive_name}.tar.gz"

        new_archive_instruction = {
            "archive_id": archive_id,
            "user_id": user_id,
            "destination_directory": destination_directory,
            "remote_address": remote_address,
            "archive_name": archive_name,
            "filepaths": filepaths,
            "status": "pending",
        }
        data["archive_instructions"].append(new_archive_instruction)

        # Step 2: Generate the simulated file in file_system.json
        if not filepaths:
            payload = {"error": "No filepaths provided for archive creation."}
            out = json.dumps(payload)
            return out

        # Locate the server and determine the size based on the source files
        source_server = None
        total_size = 0
        for path in filepaths:
            file_found = False
            for server in data.get("file_system", []):
                for directory in server.get("directories", []):
                    for file in directory.get("files", []):
                        if f"{directory.get('path')}/{file.get('filename')}" == path:
                            source_server = server
                            total_size += int(file.get("size", 0))
                            file_found = True
                            break
                    if file_found and source_server:
                        break
                if file_found and source_server:
                    break

        if not source_server:
            payload = {"error": f"Could not find the source server for files: {filepaths}"}
            out = json.dumps(payload)
            return out

        archive_size = int(total_size * 0.8)  # Emulate 80% compression
        archive_checksum = "a1f2e3d4c5b6789012345678901234567890abcd"
        new_archive_file = {
            "filename": f"{archive_name}.tar.gz",
            "size": str(archive_size),
            "owner": user_id,
            "permissions": "644",
            "last_modified": "2025-08-13T01:01:01Z",
            "checksum": archive_checksum,
        }

        # Place the archive in the destination directory on the source server
        dest_dir_found = False
        for directory in source_server["directories"]:
            if directory["path"] == destination_directory:
                directory["files"].append(new_archive_file)
                dest_dir_found = True
                break
        if not dest_dir_found:
            source_server["directories"].append(
                {"path": destination_directory, "files": [new_archive_file]}
            )
        payload = {
            "status": "success",
            "message": f"Archive instruction {archive_id} created and simulated file created at {source_server['hostname']}:{archive_path}.",
            "archive_id": archive_id,
            "archive_path": archive_path,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateArchive",
                "description": "Creates a new archive instruction and a simulated archive file in the file_system.json state.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "destination_directory": {"type": "string"},
                        "remote_address": {"type": "string"},
                        "archive_name": {"type": "string"},
                        "filepaths": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "user_id",
                        "destination_directory",
                        "remote_address",
                        "archive_name",
                        "filepaths",
                    ],
                },
            },
        }
