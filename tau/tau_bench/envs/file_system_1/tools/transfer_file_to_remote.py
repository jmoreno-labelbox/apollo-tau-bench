# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TransferFileToRemote(Tool):
    """Simulates transferring a file to a remote server, typically using SCP or rsync."""
    @staticmethod
    def invoke(data: Dict[str, Any], destination_path, remote_address, source_path) -> str:
        return json.dumps({
            "status": "success", "source_file": source_path, "destination": f"{remote_address}:{destination_path}", "checksum_verified": True})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "transfer_file_to_remote", "description": "Transfers a file from a source to a remote destination using a secure protocol.", "parameters": {"type": "object", "properties": {"source_path": {"type": "string"}, "remote_address": {"type": "string"}, "destination_path": {"type": "string"}, "ssh_key": {"type": "string"}}, "required": ["source_path", "remote_address", "destination_path", "ssh_key"]}}}
