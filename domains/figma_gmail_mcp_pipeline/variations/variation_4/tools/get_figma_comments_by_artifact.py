from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetFigmaCommentsByArtifact(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        comment_id: str = None,
        artifact_id: str = None,
        author_email: str = None,
        resolved_status: bool = None,
        content_keywords: list[str] = [],
        created_after: str = None,
        created_before: str = None
    ) -> str:
        """
        Obtains Figma comments filtered by artifact, author, and additional criteria.
        """
        figma_comments = data.get("figma_comments", [])

        # Return the specific comment if comment_id is supplied
        if comment_id:
            for comment in figma_comments:
                if comment.get("comment_id") == comment_id:
                    payload = comment
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Comment with ID '{comment_id}' not found."}
            out = json.dumps(payload)
            return out

        # Sort comments based on specified criteria
        results = []
        for comment in figma_comments:
            # Implement filters
            if artifact_id:
                if comment.get("artifact_id") != artifact_id:
                    continue

            if author_email:
                if comment.get("author_email") != author_email:
                    continue

            if resolved_status is not None:
                if comment.get("resolved_flag") != resolved_status:
                    continue

            if content_keywords:
                content = comment.get("content", "").lower()
                if not any(keyword.lower() in content for keyword in content_keywords):
                    continue

            # Enforce date filters
            if created_after:
                comment_created = comment.get("created_ts", "")
                if comment_created < created_after:
                    continue

            if created_before:
                comment_created = comment.get("created_ts", "")
                if comment_created > created_before:
                    continue

            results.append(comment)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFigmaCommentsByArtifact",
                "description": "Retrieves Figma comments filtered by artifact ID, author email, resolution status, content keywords, and date ranges for comprehensive comment management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "comment_id": {
                            "type": "string",
                            "description": "The ID of a specific comment to retrieve.",
                        },
                        "artifact_id": {
                            "type": "string",
                            "description": "Filter comments by associated artifact ID.",
                        },
                        "author_email": {
                            "type": "string",
                            "description": "Filter comments by resolution status (true for resolved, false for unresolved).",
                        },
                        "resolved_status": {
                            "type": "boolean",
                            "description": "Filter comments by resolution status (true for resolved, false for unresolved).",
                        },
                        "content_keywords": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter comments by keywords in the content.",
                        },
                        "created_after": {
                            "type": "string",
                            "description": "Filter comments created after this ISO timestamp.",
                        },
                        "created_before": {
                            "type": "string",
                            "description": "Filter comments created before this ISO timestamp.",
                        },
                    },
                },
            },
        }
