from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AnalyzeAttachmentFileInventoryTool(Tool):
    """Searches the attachments table to analyze file types, sizes, and email linkage patterns among candidates."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, file_type_filter: str = None) -> str:
        attachments = data.get("attachments", {}).values()
        emails = data.get("emails", {}).values()

        # Generate a map for fast retrieval
        email_id_to_candidate_id = {
            e.get("message_id"): e.get("candidate_id_nullable") for e in emails.values()
        }

        # Filter based on candidate if specified
        if candidate_id:
            # Retrieve all attachment IDs associated with the candidate's emails
            candidate_attachment_ids = set()
            for email in emails.values():
                if str(email.get("candidate_id_nullable")) == str(candidate_id):
                    for att_id in email.get("attachments_ids", []):
                        candidate_attachment_ids.add(att_id)

            attachments = [
                att
                for att in attachments.values() if att.get("attachment_id") in candidate_attachment_ids
            ]

        # Filter according to file type
        if file_type_filter:
            attachments = [
                att for att in attachments.values() if att.get("mime_type") == file_type_filter
            ]

        # Evaluation
        total_size = sum(att.get("size_bytes", 0) for att in attachments.values()
        file_type_distribution = {}
        for att in attachments:
            mime_type = att.get("mime_type", "unknown")
            file_type_distribution[mime_type] = (
                file_type_distribution.get(mime_type, 0) + 1
            )

        result = {
            "total_attachments": len(attachments),
            "total_size_bytes": total_size,
            "file_type_distribution": file_type_distribution,
            "attachments_sample": attachments[:10],  # an example
        }
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyzeAttachmentFileInventory",
                "description": "Queries attachments table analyzing file types, sizes, and email linkage patterns across candidates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {
                            "type": "string",
                            "description": "Specific candidate or null for system-wide analysis",
                        },
                        "file_type_filter": {
                            "type": "string",
                            "description": "MIME type filter",
                        },
                    },
                    "required": [],
                },
            },
        }
