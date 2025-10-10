# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateArchiveOnRemote(Tool):
    """Simulates creating a compressed tarball (tar.gz) on a remote server."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hostname = kwargs.get("hostname")
        archive_path = kwargs.get("archive_path")
        file_count = len(kwargs.get("files_to_include", []))
        return json.dumps({
            "status": "success", "hostname": hostname, "archive_path": archive_path, "message": f"Successfully created archive '{archive_path}' with {file_count} files on {hostname}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_archive_on_remote", "description": "Creates a compressed tar.gz archive from a list of files on a remote server.", "parameters": {"type": "object", "properties": {"hostname": {"type": "string"}, "archive_path": {"type": "string"}, "files_to_include": {"type": "array", "items": {"type": "string"}}}, "required": ["hostname", "archive_path", "files_to_include"]}}}
