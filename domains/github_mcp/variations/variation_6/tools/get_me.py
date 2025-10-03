from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetMe(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        username: str = None,
        auth_key: str = None,
        instruction: str = None,
    ) -> str:
        """Authenticate user by validating username and AUTH_KEY, return comprehensive user information."""
        pass
        import re

        auth_users = data.get("authentication", [])
        repositories = data.get("repositories", [])

        if not auth_users:
            payload = {
                    "success": False,
                    "error": "No authentication data available",
                    "error_code": "AUTH_DATA_NOT_FOUND",
                    "metadata": {
                        "authentication_method": "unknown",
                        "session_expires": None,
                        "last_login": None,
                    },
                    "suggestions": [
                        "Ensure authentication data is loaded",
                        "Check system configuration",
                    ],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Retrieve auth_key from the instruction if it exists
        if instruction and not auth_key:
            #Search for the pattern: "auth_key is xxx (owner: yyy)"
            auth_key_match = re.search(
                r"auth_key is ([a-zA-Z0-9_]+) \(owner: ([^)]+)\)", instruction
            )
            if auth_key_match:
                auth_key = auth_key_match.group(1)
                if not username:
                    username = auth_key_match.group(2)

        #Identify the authentication method and locate the user
        user = None
        auth_method = "default"

        if username and auth_key:
            #Complete authentication: ensure both username and auth_key are correct
            auth_method = "username_and_key"
            for auth_user in auth_users:
                if (
                    auth_user.get("username") == username
                    and auth_user.get("auth_key") == auth_key
                ):
                    user = auth_user
                    break

            if not user:
                payload = {
                        "success": False,
                        "error": "Authentication failed: username and auth_key combination invalid",
                        "error_code": "AUTH_MISMATCH",
                        "metadata": {
                            "provided_username": username,
                            "provided_key": auth_key[:10] + "..." if auth_key else None,
                            "authentication_method": "username_and_key",
                            "session_expires": None,
                            "last_login": None,
                        },
                        "suggestions": [
                            "Verify both username and AUTH_KEY are correct",
                            "Check that the username matches the token owner",
                            "Ensure you're using valid GitHub credentials",
                        ],
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

        elif auth_key and not username:
            #Auth key only: locate user by matching AUTH_KEY
            auth_method = "auth_key_only"
            for auth_user in auth_users:
                if auth_user.get("auth_key") == auth_key:
                    user = auth_user
                    break

            if not user:
                payload = {
                        "success": False,
                        "error": "Invalid authentication key",
                        "error_code": "INVALID_AUTH_KEY",
                        "metadata": {
                            "provided_key": auth_key[:10] + "..." if auth_key else None,
                            "authentication_method": "auth_key_only",
                            "session_expires": None,
                            "last_login": None,
                        },
                        "suggestions": [
                            "Verify the AUTH_KEY is correct",
                            "Check that the token hasn't expired",
                            "Ensure you're using a valid GitHub token",
                        ],
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

        elif username and not auth_key:
            #Username only: identify user by username (not as secure)
            auth_method = "username_only"
            for auth_user in auth_users:
                if auth_user.get("username") == username:
                    user = auth_user
                    break

            if not user:
                payload = {
                        "success": False,
                        "error": "Username not found",
                        "error_code": "USERNAME_NOT_FOUND",
                        "metadata": {
                            "provided_username": username,
                            "authentication_method": "username_only",
                            "session_expires": None,
                            "last_login": None,
                        },
                        "suggestions": [
                            "Verify the username is correct",
                            "Check available usernames in the system",
                            "Consider using auth_key for better security",
                        ],
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        else:
            #No parameters given: default to the first user (for backward compatibility)
            auth_method = "default"
            user = auth_users[0]

        final_username = user["username"]

        #Compute statistics for the repository
        owned_repos = [repo for repo in repositories if repo["owner"] == final_username]
        total_owned = len(owned_repos)

        #Retrieve organization memberships (users sharing email domains)
        user_domain = user["email"].split("@")[1]
        organizations = list(
            {
                auth_user["email"].split("@")[1]
                for auth_user in auth_users
                if auth_user["email"].split("@")[1] == user_domain
                and auth_user["username"] != final_username
            }
        )

        #Simulate extra user data using username patterns
        display_name = final_username.replace("-", " ").title()
        avatar_url = f"https://avatars.githubusercontent.com/{final_username}"
        member_since = "2023-01-15T09:30:00Z"
        two_factor_enabled = "team" in final_username or "lead" in final_username

        #Improved response including authentication verification
        result = {
            "success": True,
            "authenticated": True,
            "data": {
                "username": final_username,
                "email": user["email"],
                "auth_key": user["auth_key"],
                "display_name": display_name,
                "avatar_url": avatar_url,
                "permissions": (
                    ["read", "write", "admin"]
                    if "lead" in final_username or "manager" in final_username
                    else ["read", "write"]
                ),
                "member_since": member_since,
                "two_factor_enabled": two_factor_enabled,
            },
            "metadata": {
                "authentication_method": "token",
                "authenticated_at": "2023-12-05T10:00:00Z",
                "session_expires": "2024-12-31T23:59:59Z",
                "last_login": "2023-12-05T10:00:00Z",
                "auth_validation": auth_method,
            },
            "relationships": {
                "organizations": organizations,
                "repositories_count": len(
                    [
                        repo
                        for repo in repositories
                        if final_username in [repo["owner"]]
                        or final_username in str(repo)
                    ]
                ),
                "owned_repositories_count": total_owned,
            },
            "authentication_details": {
                "username_verified": username is not None,
                "email_verified": True,
                "auth_key_verified": auth_key is not None,
                "authentication_source": auth_method,
                "security_level": (
                    "high"
                    if auth_method == "username_and_key"
                    else (
                        "medium"
                        if auth_method in ["auth_key_only", "username_only"]
                        else "low"
                    )
                ),
            },
        }
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMe",
                "description": "Authenticate user by validating username and AUTH_KEY, return comprehensive user information including profile data, permissions, repository relationships, and organizational memberships. Can extract auth_key from instruction if provided.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "GitHub username for user identification (optional)",
                        },
                        "auth_key": {
                            "type": "string",
                            "description": "GitHub authentication token/key for validation (optional)",
                        },
                        "instruction": {
                            "type": "string",
                            "description": "Task instruction that may contain auth_key information in format 'auth_key is xxx (owner: yyy)' (optional)",
                        },
                    },
                    "required": [],
                },
            },
        }
