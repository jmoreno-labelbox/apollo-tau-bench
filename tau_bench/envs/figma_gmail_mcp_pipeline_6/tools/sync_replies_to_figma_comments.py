from tau_bench.envs.tool import Tool
import json
from typing import Any

class sync_replies_to_figma_comments(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str, artifact_id: str) -> str:
        """
        Synchronizes replies from Gmail threads into comments in Figma.
        - Retrieves all Gmail messages associated with the specified thread_id.
        - Generates Figma comments for any messages that are not yet included.
        - Connects comments to the corresponding original Gmail message.
        """
        gmail_messages = data.get("gmail_messages", [])
        figma_comments = data.get("figma_comments", [])

        synced_count = 0
        for msg in gmail_messages:
            if msg.get("thread_id") != thread_id:
                continue

            msg_id = msg.get("message_id")
            msg_content = msg.get("body_text_stripped")
            already_synced = any(
                c.get("source_message_id_nullable") == msg_id
                and c.get("artifact_id") == artifact_id
                for c in figma_comments
            )

            if not already_synced:
                new_comment = {
                    "comment_id": f"comment_auto_{len(figma_comments)+1:03d}",
                    "artifact_id": artifact_id,
                    "author_email": msg.get("sender_email"),
                    "content": msg_content,
                    "source_message_id_nullable": msg_id,
                    "created_ts": msg.get("sent_ts"),
                    "resolved_flag": False,
                }
                figma_comments.append(new_comment)
                synced_count += 1
        payload = {"synced_count": synced_count, "total_comments": len(figma_comments)}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SyncRepliesToFigmaComments",
                "description": "Syncs Gmail thread replies into Figma comments for the given artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "artifact_id": {"type": "string"},
                    },
                    "required": ["thread_id", "artifact_id"],
                },
            },
        }
