from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ArchiveMailbox(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, department: str = None) -> str:
        if employee_id is None or department is None:
            payload = {
                    "status": "error",
                    "description": "The employee_id and department fields are required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        mailboxes = data.get("mailboxes")
        archives = data.get("data_archives")

        for mailbox in mailboxes:
            if mailbox["employee_id"] == employee_id:
                archive = {
                    "archive_id": "arch_000000",
                    "employee_id": employee_id,
                    "mailbox_id": mailbox["mailbox_id"],
                    "archive_path": f"s3://corp-archives/mail/{employee_id}/{FIXED_NOW.split('T')[0]}",
                    "retention_policy": None,
                    "created_at": FIXED_NOW,
                }
                if department == "Finance":
                    archive["retention_policy"] = "finance_7y"
                else:
                    archive["retention_policy"] = "std_2y"

                archives.append(archive)
                payload = {"status": "ok", "description": "Successfully created mailbox"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"status": "error", "description": "Employee mailbox not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "archiveMailbox",
                "description": "Archives an employee's mailbox",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to archive.",
                        },
                        "department": {
                            "type": "string",
                            "description": "The employee's department.",
                        },
                    },
                    "required": ["employee_id", "department"],
                },
            },
        }
