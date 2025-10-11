# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AnalyzeAttachmentFileInventoryTool(Tool):
    """Queries attachments table analyzing file types, sizes, and email linkage patterns across candidates."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, file_type_filter) -> str:

        attachments = data.get("attachments", [])
        emails = data.get("emails", [])

        # Generate a map for rapid access.
        email_id_to_candidate_id = {
            e.get("message_id"): e.get("candidate_id_nullable") for e in emails
        }

        # Apply filter based on candidate if available
        if candidate_id:
            # Retrieve all attachment IDs associated with the candidate's emails.
            candidate_attachment_ids = set()
            for email in emails:
                if str(email.get("candidate_id_nullable")) == str(candidate_id):
                    for att_id in email.get("attachments_ids", []):
                        candidate_attachment_ids.add(att_id)

            attachments = [
                att for att in attachments
                if att.get("attachment_id") in candidate_attachment_ids
            ]

        # Restrict by file format
        if file_type_filter:
            attachments = [
                att for att in attachments
                if att.get("mime_type") == file_type_filter
            ]

        # Examination
        total_size = sum(att.get("size_bytes", 0) for att in attachments)
        file_type_distribution = {}
        for att in attachments:
            mime_type = att.get("mime_type", "unknown")
            file_type_distribution[mime_type] = file_type_distribution.get(mime_type, 0) + 1

        result = {
            "total_attachments": len(attachments),
            "total_size_bytes": total_size,
            "file_type_distribution": file_type_distribution,
            "attachments_sample": attachments[:10] # an example
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
