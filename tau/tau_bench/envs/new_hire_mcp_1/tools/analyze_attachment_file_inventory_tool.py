# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AnalyzeAttachmentFileInventoryTool(Tool):
    """Queries attachments table analyzing file types, sizes, and email linkage patterns across candidates."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        file_type_filter = kwargs.get("file_type_filter")

        attachments = data.get("attachments", [])
        emails = data.get("emails", [])

        # Create a map for quick lookup
        email_id_to_candidate_id = {
            e.get("message_id"): e.get("candidate_id_nullable") for e in emails
        }

        # Filter by candidate if provided
        if candidate_id:
            # Get all attachment IDs linked to the candidate's emails
            candidate_attachment_ids = set()
            for email in emails:
                if str(email.get("candidate_id_nullable")) == str(candidate_id):
                    for att_id in email.get("attachments_ids", []):
                        candidate_attachment_ids.add(att_id)

            attachments = [
                att for att in attachments
                if att.get("attachment_id") in candidate_attachment_ids
            ]

        # Filter by file type
        if file_type_filter:
            attachments = [
                att for att in attachments
                if att.get("mime_type") == file_type_filter
            ]

        # Analysis
        total_size = sum(att.get("size_bytes", 0) for att in attachments)
        file_type_distribution = {}
        for att in attachments:
            mime_type = att.get("mime_type", "unknown")
            file_type_distribution[mime_type] = file_type_distribution.get(mime_type, 0) + 1

        result = {
            "total_attachments": len(attachments),
            "total_size_bytes": total_size,
            "file_type_distribution": file_type_distribution,
            "attachments_sample": attachments[:10] # a sample
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyze_attachment_file_inventory",
                "description": "Queries attachments table analyzing file types, sizes, and email linkage patterns across candidates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "Specific candidate or null for system-wide analysis"},
                        "file_type_filter": {"type": "string", "description": "MIME type filter"}
                    },
                    "required": [],
                },
            },
        }
