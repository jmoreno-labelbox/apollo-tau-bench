from tau_bench.envs.tool import Tool
import json
from typing import Any

class AppendTerminal(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], command: str) -> str:
        """Execute terminal-like commands for GitHub operations analysis and workflow insights."""
        pass
        #Confirm that terminal data is present and correctly structured
        if "terminal" not in data or not data["terminal"]:
            data["terminal"] = [{"printed_ts": [], "commands": [], "outputs": []}]

        terminal_data = data["terminal"]

        #Verify that the first element is present and properly structured
        if not terminal_data or not isinstance(terminal_data[0], dict):
            terminal_data[0] = {"printed_ts": [], "commands": [], "outputs": []}

        #Confirm that all necessary keys are present
        if "printed_ts" not in terminal_data[0]:
            terminal_data[0]["printed_ts"] = []
        if "commands" not in terminal_data[0]:
            terminal_data[0]["commands"] = []
        if "outputs" not in terminal_data[0]:
            terminal_data[0]["outputs"] = []

        timestamp = "2023-12-05T12:00:00Z"
        terminal_data[0]["printed_ts"].append(timestamp)
        terminal_data[0]["commands"].append(command)

        #Handle various terminal commands for analyzing GitHub workflows
        if command.startswith("git status"):
            output = "Repository status: Clean working directory, all changes committed"
        elif command.startswith("git log"):
            output = "Recent commits: Latest changes include security fixes and feature updates"
        elif command.startswith("ps aux"):
            output = "GitHub Actions: workflow running, authentication verified, API rate limits OK"
        elif command.startswith("ls -la"):
            output = "Repository contents: .github/ workflows/ src/ docs/ README.md .gitignore"
        elif command.startswith("env"):
            output = "Environment: GITHUB_TOKEN=*****, NODE_ENV=production, CI=true"
        elif command.startswith("curl"):
            output = "API Health Check: GitHub API responding, rate limit: 4999/5000 remaining"
        elif command.startswith("docker"):
            output = "Container Status: GitHub Actions runner healthy, image pulls successful"
        elif command.startswith("npm"):
            output = "Dependencies: All packages installed, security audit passed, no vulnerabilities"
        elif command.startswith("echo"):
            #Retrieve the message following the echo
            message = command.replace("echo ", "").strip("\"'")
            output = f"DEBUG: {message}"
        elif command.startswith("cat"):
            output = (
                "File contents: Configuration loaded successfully, secrets validated"
            )
        elif command.startswith("grep"):
            output = "Search results: Pattern found in 3 files, context extracted"
        elif command.startswith("tail"):
            output = "Log tail: [INFO] Authentication successful [INFO] Repository access granted [INFO] Operation completed"
        elif command.startswith("whoami"):
            output = "Current user: github-actions-bot (authenticated via token)"
        elif command.startswith("pwd"):
            output = "Current directory: /github/workspace/repository-name"
        elif command.startswith("free"):
            output = "Memory usage: 2.1GB used / 7GB total, GitHub Actions limits OK"
        elif command.startswith("top"):
            output = "Processes: git-daemon, node, npm, github-runner (all healthy)"
        else:
            output = f"Command executed: {command} - GitHub workflow operation logged"

        terminal_data[0]["outputs"].append(output)
        payload = {
                "command": command,
                "output": output,
                "timestamp": timestamp,
                "session_id": "github-actions-session-001",
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
                "name": "appendTerminal",
                "description": "Execute terminal-like commands for GitHub operations analysis, debugging, and workflow insights. Supports git, system, and CI/CD commands.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "command": {
                            "type": "string",
                            "description": "Terminal command to execute (e.g., 'git status', 'ps aux', 'echo \"Debug message\"', 'curl api/health')",
                        }
                    },
                    "required": ["command"],
                },
            },
        }
