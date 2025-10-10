# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchAttachmentsByFilename(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        filename = kwargs["filename"]
        matches = [a for a in list(data.get("attachments", {}).values()) if a.get("filename") == filename]
        return json.dumps({"matches": matches}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_attachments_by_filename",
                "description": "Search attachments (simulated Drive) by exact filename.",
                "parameters": {
                    "type": "object",
                    "properties": {"filename": {"type": "string"}},
                    "required": ["filename"]
                }
            }
        }
