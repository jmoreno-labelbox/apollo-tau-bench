from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListOfPRForRepo(Tool):
    """
    Lists pull requests for a repository.
    - Inputs: owner, repo_name, (optional) state in {'open','closed','merged'}
    - Returns an array of PR summaries (number, title, state, branches, head_sha, timestamps, files).
    - Reads from data.get('pull_requests', {}).values() or top-level list.
    """

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = "", repo_name: str = "", state: str = "") -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        state_filter = state.strip().lower()  # optional

        if not owner or not repo_name:
            payload = {"error": "Parameters 'owner' and 'repo_name' are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if state_filter and state_filter not in {"open", "closed", "merged"}:
            payload = {"error": "Invalid 'state'. Use one of: 'open', 'closed', 'merged'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Load PR DB (supports dict with 'pull_requests' or a top-level list)
        pr_db = _convert_db_to_list(data.get("pull_requests", {}).values()

        if not isinstance(pr_db, list):
            payload = {"error": "Invalid pull requests DB: expected a list."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Find the repo bucket
        rec = next(
            (
                r
                for r in pr_db
                if r.get("owner") == owner and r.get("repo_name") == repo_name
            ),
            None,
        )
        if rec is None:
            payload = {
                    "error": f"No pull requests found for repository '{owner}/{repo_name}'."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        pr_numbers: list[int] = rec.get("pr_numbers", [])

        def get_at(name: str, i: int):
            arr = rec.get(name, [])
            return arr[i] if i < len(arr) else None

        # Build list of (number, index) and sort by PR number ascending
        indexed: list[tuple] = [(num, i) for i, num in enumerate(pr_numbers)]
        indexed.sort(key=lambda t: t[0])

        results: list[dict[str, Any]] = []
        for num, idx in indexed:
            pr_state = get_at("pr_states", idx)
            merged_flag = bool(get_at("merged_flags", idx))
            # If a state filter is set, apply it
            if state_filter:
                if state_filter == "merged" and not merged_flag:
                    continue
                if state_filter in {"open", "closed"} and pr_state != state_filter:
                    continue

            files_entry = get_at(
                "pr_files", idx
            )  # stored shape is typically [ [ "fileA", ... ] ]
            pr_summary = {
                "number": num,
                "title": get_at("pr_titles", idx),
                "body": get_at("pr_bodies", idx),
                "state": pr_state,
                "merged": merged_flag,
                "mergeable": get_at("mergeable_flags", idx),
                "base_branch": get_at("base_branches", idx),
                "head_branch": get_at("head_branches", idx),
                "head_sha": get_at("head_shas", idx),
                "files": files_entry,
                "created_ts": get_at("created_ts", idx),
                "updated_ts": get_at("updated_ts", idx),
            }
            results.append(pr_summary)
        payload = {
                "owner": owner,
                "repo_name": repo_name,
                "count": len(results),
                "pull_requests": results,
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
                "name": "listOfPrForRepo",
                "description": "List pull requests for a repository, optionally filtered by state.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name.",
                        },
                        "state": {
                            "type": "string",
                            "enum": ["open", "closed", "merged"],
                            "description": "Optional filter by PR state.",
                        },
                    },
                    "required": ["owner", "repo_name"],
                },
            },
        }
