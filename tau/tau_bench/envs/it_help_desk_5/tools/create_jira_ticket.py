from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateJiraTicket(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], issue_type: str = None, summary: str = None, priority: str = None) -> str:
        jira_tickets = data.get("jira_tickets")

        if len(jira_tickets) > 0:
            last_jira_id = jira_tickets[-1]["jira_id"]
        else:
            last_jira_id = "ITSD-1000"

        id_components = last_jira_id.split("-")
        new_jira_id = f"{id_components[0]}-{str(int(id_components[1])+1).zfill(4)}"

        if issue_type is None:
            payload = {"status": "error", "reason": "issue_type parameter is required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if summary is None:
            payload = {"status": "error", "reason": "summary parameter is required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if priority is None:
            payload = {"status": "error", "reason": "priority parameter is required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        new_jira_ticket = {
            "jira_id": new_jira_id,
            "issue_type": issue_type,
            "summary": summary,
            "priority": priority,
            "status": "To Do",
            "created_at": "2025-07-10T13:00:00+00:00",
            "updated_at": "2025-07-14T15:30:00+00:00",
        }

        data["jira_tickets"][new_jira_ticket["jira_ticket_id"]] = new_jira_ticket
        payload = {
                "status": "ok",
                "reason": f"Successfully created a new Jira ticket {new_jira_id}.",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createJiraTicket",
                "description": "Creates a new Jira ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "issue_type": {
                            "type": "string",
                            "description": "The type of issue to assign to the Jira ticket",
                        },
                        "summary": {
                            "type": "string",
                            "description": "A description of the issue.",
                        },
                        "priority": {
                            "type": "string",
                            "description": "The priority of the issue.",
                        },
                    },
                    "required": ["issue_type", "summary", "priority"],
                },
            },
        }
