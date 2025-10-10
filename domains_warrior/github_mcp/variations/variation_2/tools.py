import json
from typing import Any, Dict, List, Optional
from domains.dto import Tool
from collections import Counter, defaultdict


def get_current_timestamp() -> str:
    # Fixed timestamp to keep runs deterministic
    return "2025-08-21T12:00:00Z"

# Deterministic ID/Number generators (database resets between tasks)
def get_next_pr_number() -> int:
    return 1

def get_next_issue_number() -> int:
    return 1

def get_next_alert_number() -> int:
    return 1

def get_next_commit_sha() -> str:
    # Deterministic placeholder SHA-like string
    return "sha_0000000000000000000000000000000000000000"

def get_next_branch_name(purpose: str) -> str:
    purpose = (purpose or "change").strip().lower().replace(" ", "-")
    return f"feature-{purpose}"

def _repos(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("repositories", [])

def _commits(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("commits", [])

def _prs(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("pull_requests", [])

def _issues(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("issues", [])

def _alerts(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("code_scanning_alerts", [])

def _terminal(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("terminal", [])

def _auth(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return acting identity as {"username": "...", "email": "..."}.
    Requires get_me(username=...) to have set data["_me"].
    """
    me = data.get("_me")
    if isinstance(me, dict) and "username" in me:
        return me
    raise Exception("No acting identity set. Call get_me(username=...) first.")


def _find_repo_record(data: Dict[str, Any], repo_name: str) -> Dict[str, Any]:
    """
    Find a repo owned by the acting user. repositories is a LIST in our dataset,
    so iterate; do NOT use dict.get.
    """
    me = _auth(data)["username"]
    repos = data.get("repositories") or []
    for r in repos:
        if r.get("owner") == me and r.get("repo_name") == repo_name:
            return r
    # Mirror RULES: if not found, surface a crisp error (no workarounds)
    raise Exception(f"Repository not found for owner '{me}': {repo_name}")


def _branch_index(repo: Dict[str, Any], branch: Optional[str]) -> int:
    """
    Map a branch name to the correct index for branch_files/branch_contents.
    If branch is None, fall back to repo['default_branch'].
    """
    branches = repo.get("branches") or []
    if not branches:
        # Some repos may only carry default branch files in file_paths; treat that as index 0.
        return 0
    target = branch or repo.get("default_branch")
    if target in branches:
        return branches.index(target)
    # If caller passed wrong branch, surface error (per RULES).
    raise Exception(f"Branch '{target}' not found in repository '{repo.get('repo_name')}'.")


def _resolve_pr_number(data: Dict[str, Any], repo_name: str, pr_number: Any) -> int:
    """
    Resolve PR number, handling placeholder strings by finding the most recently created PR.
    Returns the actual PR number as an integer.
    """
    # If it's a placeholder string or any non-integer, find the most recent PR
    if not isinstance(pr_number, int) or str(pr_number) == "{{PR_NUMBER}}":
        me = _auth(data)["username"]
        prs = data.get("pull_requests") or []
        block = next((b for b in prs if b.get("owner") == me and b.get("repo_name") == repo_name), None)
        if not block or not block["pr_numbers"]:
            raise Exception("No pull requests found for this repository")
        # Use the most recently created PR (last in the list)
        return block["pr_numbers"][-1]
    else:
        # Return the actual number (should be an integer)
        return int(pr_number)

class GetRepository(Tool):
    """Returns details about a repository by name, regardless of owner."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        try:
            # Search all repos in dataset, not just those owned by auth user
            for repo in _repos(data):
                if repo.get("repo_name") == repo_name:
                    return json.dumps(repo, indent=2)
            return json.dumps({"error": f"Repository not found: {repo_name}"}, indent=2)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repository",
                "description": "Returns details about a repository by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string", "description": "The name of the repository"},
                    },
                    "required": ["repo_name"],
                },
            },
        }

class GetDefaultBranch(Tool):
    """Returns the default branch of a given repo owned by the acting user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        try:
            repo = _find_repo_record(data, repo_name)
            return json.dumps({"default_branch": repo.get("default_branch")}, indent=2)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_default_branch",
                "description": "Returns the default branch name of a given repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                    },
                    "required": ["repo_name"],
                },
            },
        }

class CreateBranch(Tool):
    """Creates a new branch from an existing branch in the repo."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        source_branch = kwargs.get("source_branch")
        new_branch = kwargs.get("new_branch")

        if not all([repo_name, source_branch, new_branch]):
            return json.dumps({"error": "repo_name, source_branch, and new_branch are required."}, indent=2)

        try:
            repo = _find_repo_record(data, repo_name)
            if new_branch in repo.get("branches", []):
                return json.dumps({"error": f"Branch '{new_branch}' already exists."}, indent=2)

            idx = _branch_index(repo, source_branch)
            repo.setdefault("branches", []).append(new_branch)
            repo.setdefault("branch_files", []).append(list(repo["branch_files"][idx]))
            repo.setdefault("branch_contents", []).append(list(repo["branch_contents"][idx]))
            repo.setdefault("branch_shas", []).append(get_next_commit_sha())

            return json.dumps({
                "message": "Branch created",
                "new_branch": new_branch,
                "from": source_branch
            }, indent=2)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_branch",
                "description": "Creates a new branch from an existing one in the repo.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "source_branch": {"type": "string"},
                        "new_branch": {"type": "string"},
                    },
                    "required": ["repo_name", "source_branch", "new_branch"],
                },
            },
        }

class WriteFileToBranch(Tool):
    """Adds or updates a file in a branch (does not commit)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        branch = kwargs.get("branch")
        path = kwargs.get("path")
        content = kwargs.get("content")

        if not all([repo_name, branch, path, content]):
            return json.dumps({"error": "repo_name, branch, path, and content are required."}, indent=2)

        try:
            repo = _find_repo_record(data, repo_name)
            idx = _branch_index(repo, branch)

            files = repo["branch_files"][idx]
            contents = repo["branch_contents"][idx]

            if path in files:
                i = files.index(path)
                contents[i] = content
            else:
                files.append(path)
                contents.append(content)

            return json.dumps({
                "message": "File added or updated",
                "repo": repo_name,
                "branch": branch,
                "path": path
            }, indent=2)

        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "write_file_to_branch",
                "description": "Adds or updates a file in the given branch (without committing).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "path": {"type": "string"},
                        "content": {"type": "string"}
                    },
                    "required": ["repo_name", "branch", "path", "content"]
                }
            }
        }

class CommitChangesToBranch(Tool):
    """Commits changes to a branch with a message (generates SHA and metadata)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        branch = kwargs.get("branch")
        commit_message = kwargs.get("commit_message")

        if not all([repo_name, branch, commit_message]):
            return json.dumps({"error": "repo_name, branch, and commit_message are required."}, indent=2)

        try:
            repo = _find_repo_record(data, repo_name)
            idx = _branch_index(repo, branch)

            new_sha = get_next_commit_sha()
            repo["branch_shas"][idx] = new_sha

            commits = _commits(data)
            me = _auth(data)["username"]

            commit_block = next((c for c in commits if c["owner"] == me and c["repo_name"] == repo_name), None)
            if not commit_block:
                commit_block = {
                    "owner": me,
                    "repo_name": repo_name,
                    "branch_names": [],
                    "commit_shas": [],
                    "commit_messages": [],
                    "commit_authors": [],
                    "commit_timestamps": [],
                }
                commits.append(commit_block)

            if branch not in commit_block["branch_names"]:
                commit_block["branch_names"].append(branch)
                commit_block["commit_shas"].append([new_sha])
                commit_block["commit_messages"].append([commit_message])
                commit_block["commit_authors"].append([me])
                commit_block["commit_timestamps"].append([get_current_timestamp()])
            else:
                bidx = commit_block["branch_names"].index(branch)
                commit_block["commit_shas"][bidx].append(new_sha)
                commit_block["commit_messages"][bidx].append(commit_message)
                commit_block["commit_authors"][bidx].append(me)
                commit_block["commit_timestamps"][bidx].append(get_current_timestamp())

            return json.dumps({
                "message": "Committed to branch",
                "repo": repo_name,
                "branch": branch,
                "commit_sha": new_sha,
                "commit_message": commit_message
            }, indent=2)

        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "commit_changes_to_branch",
                "description": "Commits all current changes to a branch with the given message.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "commit_message": {"type": "string"}
                    },
                    "required": ["repo_name", "branch", "commit_message"]
                }
            }
        }

class ListRepositoriesSortedByLastUpdated(Tool):
    """Returns all repositories owned by the acting user, sorted by last update time (descending)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        repos = sorted(
            [r for r in _repos(data) if r.get("owner") == me],
            key=lambda r: r.get("last_updated", ""),
            reverse=True
        )
        return json.dumps([{"repo_name": r["repo_name"], "last_updated": r.get("last_updated")} for r in repos], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_repositories_sorted_by_last_updated",
                "description": "Returns repositories owned by the current user, sorted by last_updated.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }

class AggregateRepositoryActivity(Tool):
    """Returns activity summary for each repo owned by acting user — counts of PRs, issues, alerts, commits."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        repos = [r for r in _repos(data) if r.get("owner") == me]
        repo_names = [r["repo_name"] for r in repos]

        prs = _prs(data)
        issues = _issues(data)
        alerts = _alerts(data)
        commits = _commits(data)

        summary = []
        for repo_name in repo_names:
            pr_count = sum(1 for pr in prs if pr.get("owner") == me and pr.get("repo_name") == repo_name)
            issue_count = sum(1 for i in issues if i.get("owner") == me and i.get("repo_name") == repo_name)
            alert_count = sum(1 for a in alerts if a.get("repo_name") == repo_name)
            commit_block = next((c for c in commits if c["owner"] == me and c["repo_name"] == repo_name), None)
            commit_count = sum(len(c) for c in commit_block["commit_shas"]) if commit_block else 0

            summary.append({
                "repo_name": repo_name,
                "prs": pr_count,
                "issues": issue_count,
                "alerts": alert_count,
                "commits": commit_count
            })

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "aggregate_repo_activity",
                "description": "Returns counts of PRs, issues, alerts, and commits per repository owned by current user.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }

class ListPullRequests(Tool):
    """Lists pull requests for a specific repository or all repositories."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        repo_name = kwargs.get("repo_name")

        result = []
        for pr in _prs(data):
            if repo_name and pr["repo_name"] != repo_name:
                continue
            result.extend([
                {
                    "owner": pr["owner"],
                    "repo_name": pr["repo_name"],
                    "pr_number": number,
                    "title": title,
                    "state": state,
                    "head_sha": head_sha,
                    "files": files
                }
                for number, title, state, head_sha, files in zip(
                    pr["pr_numbers"],
                    pr["pr_titles"],
                    pr["pr_states"],
                    pr["head_shas"],
                    [x[0] for x in pr["pr_files"]],
                )
            ])

        return json.dumps({"pull_requests": result}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_pull_requests",
                "description": "List all pull requests optionally filtered by repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {
                            "type": "string",
                            "description": "Optional name of the repository to filter PRs"
                        }
                    },
                    "required": []
                }
            }
        }

class ListMergedPullRequestsWithFiles(Tool):
    """Returns merged PRs for a given repo and owner, including changed files."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _auth(data)["username"]
        repo_name = kwargs.get("repo_name")
        if not all([owner, repo_name]):
            return json.dumps({"error": "owner and repo_name are required."}, indent=2)

        prs = _prs(data)
        merged = [
            {"number": pr["number"], "title": pr["title"], "files": pr.get("files", [])}
            for pr in prs
            if pr.get("owner") == owner and pr.get("repo_name") == repo_name and pr.get("state") == "merged"
        ]
        return json.dumps(merged, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_merged_pull_requests_with_files",
                "description": "Returns merged PRs for the given owner/repo with changed files.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo_name": {"type": "string"},
                    },
                    "required": ["owner", "repo_name"]
                }
            }
        }

class ListAlerts(Tool):
    """Returns code scanning alerts for a given repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        alerts = _alerts(data)
        filtered = [
            {
                "alert_number": a.get("alert_number"),
                "rule": a.get("rule"),
                "severity": a.get("severity"),
                "state": a.get("state"),
                "dismissed": a.get("dismissed", False)
            }
            for a in alerts
            if a.get("repo_name") == repo_name
        ]
        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_alerts",
                "description": "Returns code scanning alerts for a given repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"}
                    },
                    "required": ["repo_name"]
                }
            }
        }

class GetAlertSeverityDistribution(Tool):
    """Returns global severity counts across all code scanning alerts."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alerts = _alerts(data)
        counter = Counter(a.get("severity", "Unknown") for a in alerts)
        return json.dumps(dict(counter), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_alert_severity_distribution",
                "description": "Returns global severity count distribution across all alerts.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }

class ListOpenAlerts(Tool):
    """Lists all open code-scanning alerts with repo, alert ID, and severity."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alerts = _alerts(data)
        open_alerts = [
            {
                "repo_name": a.get("repo_name"),
                "alert_number": a.get("alert_number"),
                "severity": a.get("severity")
            }
            for a in alerts
            if a.get("state") != "closed"
        ]
        return json.dumps(open_alerts, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_open_alerts",
                "description": "Returns open alerts across all repositories with ID and severity.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }

class GetCommitSummary(Tool):
    """Returns commit count for a given repo and owner, broken down by branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _auth(data)["username"]
        repo_name = kwargs.get("repo_name")
        if not all([owner, repo_name]):
            return json.dumps({"error": "owner and repo_name are required."}, indent=2)

        commits = _commits(data)
        summary = {}

        for c in commits:
            if c.get("owner") == owner and c.get("repo_name") == repo_name:
                for branch, shas in zip(c["branch_names"], c["commit_shas"]):
                    summary[branch] = len(shas)

        return json.dumps({"repo_name": repo_name, "commit_summary": summary}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_commit_summary",
                "description": "Returns commit summary per branch for a repo and owner.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo_name": {"type": "string"},
                    },
                    "required": ["owner", "repo_name"]
                }
            }
        }

class GetTopCommitAuthors(Tool):
    """Returns top commit authors globally across all repositories."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        commits = _commits(data)
        counter = Counter()

        for c in commits:
            for author_list in c.get("commit_authors", []):
                counter.update(author_list)

        top_authors = counter.most_common(10)
        return json.dumps([{"author": a, "commits": count} for a, count in top_authors], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_top_commit_authors",
                "description": "Returns top commit authors across all repositories.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }

class AnalyzeTerminalActivityTypes(Tool):
    """Returns frequency of inferred terminal activity types (e.g., git, docker, pytest)"""

    DEFAULT_KEYWORDS = ["git", "docker", "kubectl", "pytest", "helm", "make", "terraform", "pip", "npm"]

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        logs = _terminal(data)
        keywords = kwargs.get("keywords", AnalyzeTerminalActivityTypes.DEFAULT_KEYWORDS)

        counter = Counter()
        for entry in logs:
            msg = entry.get("message", "").lower()
            for keyword in keywords:
                if keyword in msg:
                    counter[keyword] += 1

        return json.dumps(dict(counter), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyze_terminal_activity_types",
                "description": "Returns frequency of terminal activity types using known or custom keywords.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keywords": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of keywords to count (e.g., git, docker)"
                        }
                    }
                }
            }
        }

class GetTerminalTimelineBounds(Tool):
    """Returns first and last printed_ts from terminal log."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        logs = _terminal(data)
        timestamps = sorted([entry.get("printed_ts") for entry in logs if entry.get("printed_ts")])
        if not timestamps:
            return json.dumps({"error": "No terminal entries with timestamps found."}, indent=2)

        return json.dumps({
            "first_timestamp": timestamps[0],
            "last_timestamp": timestamps[-1]
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_terminal_timeline_bounds",
                "description": "Returns first and last terminal log timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }

class CountPublicPrivateRepos(Tool):
    """Returns count of public vs private repositories owned by the acting user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        repos = [r for r in _repos(data) if r.get("owner") == me]

        result = {"public": 0, "private": 0}
        for r in repos:
            vis = r.get("visibility")
            if vis == "public":
                result["public"] += 1
            elif vis == "private":
                result["private"] += 1

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "count_public_private_repos",
                "description": "Returns counts of public and private repositories owned by the user.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }

class FindReposWithDocsFolder(Tool):
    """Returns repositories containing files under the 'docs/' folder."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        matches = []

        for r in _repos(data):
            if r.get("owner") != me:
                continue
            for file_list in r.get("branch_files", []):
                if any(f.startswith("docs/") for f in file_list):
                    matches.append(r["repo_name"])
                    break

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "find_repos_with_docs_folder",
                "description": "Finds repositories with files under 'docs/' folder.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }

class FindReposWithDockerCompose(Tool):
    """Returns repositories that contain a 'docker-compose.yml' file in any branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        results = []

        for r in _repos(data):
            if r.get("owner") != me:
                continue
            for files in r.get("branch_files", []):
                if "docker-compose.yml" in files:
                    results.append(r["repo_name"])
                    break

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "find_repos_with_docker_compose",
                "description": "Finds repositories that contain 'docker-compose.yml'.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }

class FindReposWithKubernetesFolder(Tool):
    """Returns repositories with files inside 'kubernetes/' directory."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        matched = []

        for r in _repos(data):
            if r.get("owner") != me:
                continue
            for file_list in r.get("branch_files", []):
                if any(f.startswith("kubernetes/") for f in file_list):
                    matched.append(r["repo_name"])
                    break

        return json.dumps(matched, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "find_repos_with_kubernetes_folder",
                "description": "Finds repositories with files under 'kubernetes/' folder.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }

class ListAllMergedPullRequests(Tool):
    """Returns all merged PRs across all repositories owned by acting user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        prs = [
            {
                "repo_name": pr["repo_name"],
                "number": pr["number"],
                "title": pr["title"],
                "state": pr["state"]
            }
            for pr in _prs(data)
            if pr.get("owner") == me and pr.get("state") == "merged"
        ]
        return json.dumps(prs, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_all_merged_pull_requests",
                "description": "Returns all merged pull requests for repos owned by current user.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }

class ListIssuesByLabel(Tool):
    """Returns all issues that have a given label (e.g., 'bug')"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        label = kwargs.get("label")
        if not label:
            return json.dumps({"error": "label is required."}, indent=2)

        issues = _issues(data)
        result = []

        for issue in issues:
            numbers = issue["issue_numbers"]
            labels_list = issue.get("labels", [])

            for idx, lbls in enumerate(labels_list):
                if label in lbls:
                    result.append(numbers[idx])

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_issues_by_label",
                "description": "Returns all issues containing the given label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "label": {"type": "string"}
                    },
                    "required": ["label"]
                }
            }
        }

class GetAlertSummaryPerRepo(Tool):
    """Returns code scanning alert summary (count + severity breakdown) for specified repositories."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_names = kwargs.get("repo_names", [])
        if not repo_names:
            return json.dumps({"error": "repo_names is required."}, indent=2)

        alerts = _alerts(data)
        summary = defaultdict(lambda: {"total": 0, "severity_counts": defaultdict(int)})

        for a in alerts:
            repo = a.get("repo_name")
            if repo in repo_names:
                summary[repo]["total"] += 1
                sev = a.get("severity", "Unknown")
                summary[repo]["severity_counts"][sev] += 1

        # Convert nested defaultdicts to normal dicts
        clean_summary = {
            repo: {
                "total": val["total"],
                "severity_counts": dict(val["severity_counts"])
            } for repo, val in summary.items()
        }

        return json.dumps(clean_summary, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_alert_summary_per_repo",
                "description": "Returns alert summary (total and by severity) for given repo list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_names": {
                            "type": "array",
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["repo_names"]
                }
            }
        }

class GetBranchFileInventory(Tool):
    """Returns file list and latest SHA for a given branch in a repo owned by the user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        branch = kwargs.get("branch")

        if not all([repo_name, branch]):
            return json.dumps({"error": "repo_name and branch are required."}, indent=2)

        try:
            repo = _find_repo_record(data, repo_name)
            idx = _branch_index(repo, branch)

            files = repo.get("branch_files", [])[idx]
            sha = repo.get("branch_shas", [])[idx]

            return json.dumps({
                "repo_name": repo_name,
                "branch": branch,
                "commit_sha": sha,
                "files": files
            }, indent=2)

        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_branch_file_inventory",
                "description": "Returns latest SHA and file list for a given repo and branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"}
                    },
                    "required": ["repo_name", "branch"]
                }
            }
        }

class RenameRepository(Tool):
    """Renames a repository owned by the acting user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        old_name = kwargs.get("old_name")
        new_name = kwargs.get("new_name")

        if not all([old_name, new_name]):
            return json.dumps({"error": "old_name and new_name are required."}, indent=2)

        repos = _repos(data)
        for r in repos:
            if r.get("owner") == me and r.get("repo_name") == old_name:
                r["repo_name"] = new_name
                return json.dumps({"message": "Repository renamed", "new_name": new_name}, indent=2)

        return json.dumps({"error": f"Repository '{old_name}' not found."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "rename_repository",
                "description": "Renames an existing repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "old_name": {"type": "string"},
                        "new_name": {"type": "string"}
                    },
                    "required": ["old_name", "new_name"]
                }
            }
        }

class SetRepositoryVisibility(Tool):
    """Changes the visibility of a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        repo_name = kwargs.get("repo_name")
        visibility = kwargs.get("visibility")

        if not all([repo_name, visibility]):
            return json.dumps({"error": "repo_name and visibility are required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        if visibility not in ["public", "private"]:
            return json.dumps({"error": "Invalid visibility. Must be 'public' or 'private'."}, indent=2)

        repo["visibility"] = visibility
        return json.dumps({"message": "Visibility updated", "repo_name": repo_name, "visibility": visibility}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_repository_visibility",
                "description": "Updates visibility of a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "visibility": {"type": "string", "enum": ["public", "private"]}
                    },
                    "required": ["repo_name", "visibility"]
                }
            }
        }

class ListBranches(Tool):
    """Lists all branches in a given repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        try:
            for repo in _repos(data):
                if repo.get("repo_name") == repo_name:
                    return json.dumps({"branches": repo.get("branches", [])}, indent=2)
            return json.dumps({"error": f"Repository not found: {repo_name}"}, indent=2)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_branches",
                "description": "Returns all branches in the given repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"}
                    },
                    "required": ["repo_name"]
                }
            }
        }

class GetPullRequest(Tool):
    """Returns details of a specific pull request."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        pr_number = int(kwargs.get("pr_number"))

        if not all([repo_name, pr_number]):
            return json.dumps({"error": "repo_name and pr_number are required."}, indent=2)

        me = _auth(data)["username"]
        for pr in _prs(data):
            if pr["owner"] == me and pr["repo_name"] == repo_name:
                if pr_number in pr["pr_numbers"]:
                    idx = pr["pr_numbers"].index(pr_number)
                    single_pr = {
                        "repo_name": pr["repo_name"],
                        "pr_number": pr_number,
                        "title": pr["pr_titles"][idx],
                        "body": pr["pr_bodies"][idx],
                        "state": pr["pr_states"][idx],
                        "head_branch": pr["head_branches"][idx],
                        "base_branch": pr["base_branches"][idx],
                        "head_sha": pr["head_shas"][idx],
                        "mergeable": pr["mergeable_flags"][idx],
                        "merged": pr["merged_flags"][idx],
                        "files": pr["pr_files"][idx],
                        "comments": pr["pr_comments"][idx],
                        "comment_users": pr["pr_comment_users"][idx],
                        "reviewers": pr["reviewers"][idx],
                        "review_states": pr["review_states"][idx],
                        "review_events": pr["review_events"][idx],
                        "created_ts": pr["created_ts"][idx],
                        "updated_ts": pr["updated_ts"][idx],
                    }
                    return json.dumps(single_pr, indent=2)

        return json.dumps({"error": "Pull request not found."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_pull_request",
                "description": "Returns details of a specific pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"}
                    },
                    "required": ["repo_name"]
                }
            }
        }

class GetIssue(Tool):
    """Returns details of a specific issue."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        number = kwargs.get("issue_number")
        if not all([repo_name, number]):
            return json.dumps({"error": "repo_name and issue_number are required."}, indent=2)

        for issue in _issues(data):
            # print("ISUEEE: ", issue)

            # ✅ Case 1: flat dict with single issue
            if issue.get("repo_name") == repo_name and issue.get("number") == int(number):
                return json.dumps(issue, indent=2)

            # ✅ Case 2: batched issue structure
            if issue.get("repo_name") == repo_name and int(number) in (issue.get("issue_numbers") or []):
                idx = issue["issue_numbers"].index(int(number))
                return json.dumps({
                    "repo_name": repo_name,
                    "number": int(number),
                    "title": issue["issue_titles"][idx],
                    "body": issue["issue_bodies"][idx],
                    "state": issue["issue_states"][idx],
                    "labels": issue["labels"][idx],
                    "assignees": issue["assignees"][idx],
                    "comments": issue["issue_comments"][idx],
                    "comment_users": issue["issue_comment_users"][idx],
                    "created_ts": issue["created_ts"][idx],
                    "updated_ts": issue["updated_ts"][idx],
                }, indent=2)

        return json.dumps({"error": "Issue not found."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_issue",
                "description": "Returns details of a specific issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"}
                    },
                    "required": ["repo_name", "issue_number"]
                }
            }
        }

class CreateIssue(Tool):
    """Creates a new issue in a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        title = kwargs.get("title")
        body = kwargs.get("body", "")
        labels = kwargs.get("labels", [])

        if not all([repo_name, title]):
            return json.dumps({"error": "repo_name and title are required."}, indent=2)

        number = get_next_issue_number()
        me = _auth(data)["username"]

        issue = {
            "repo_name": repo_name,
            "number": number,
            "title": title,
            "body": body,
            "labels": labels,
            "state": "open",
            "creator": me,
            "comments": [],
        }
        # print("issue:", issue)

        _issues(data).append(issue)
        # print("final data:", _issues(data))
        return json.dumps({"message": "Issue created", "number": number}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_issue",
                "description": "Creates a new issue in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "labels": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["repo_name", "title"]
                }
            }
        }

class UpdateIssue(Tool):
    """Updates an issue's fields. Supports both aggregated blocks and flat issue rows."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        issue_number = kwargs.get("issue_number")

        # Accept either `state` or legacy `updates` for compatibility
        new_state = kwargs.get("state") or kwargs.get("updates")
        new_title = kwargs.get("title")
        new_body = kwargs.get("body")
        new_labels = kwargs.get("labels")  # replace entire label list if provided

        if not repo_name or issue_number is None:
            return json.dumps({"error": "repo_name and issue_number are required."}, indent=2)

        target = int(issue_number)

        # 1) Aggregated blocks (original dataset shape)
        for block in _issues(data):
            if block.get("repo_name") != repo_name:
                continue

            nums = block.get("issue_numbers")
            if isinstance(nums, list) and target in nums:
                idx = nums.index(target)

                # Ensure parallel arrays exist & are long enough, then update in place
                def _ensure_len(lst, fill, n):
                    if lst is None or not isinstance(lst, list):
                        lst = []
                    if len(lst) < n:
                        lst += [fill] * (n - len(lst))
                    return lst

                n = len(nums)

                if new_state is not None:
                    states = _ensure_len(block.get("issue_states"), "open", n)
                    states[idx] = new_state
                    block["issue_states"] = states

                if new_title is not None:
                    titles = _ensure_len(block.get("issue_titles"), "", n)
                    titles[idx] = new_title
                    block["issue_titles"] = titles

                if new_body is not None:
                    bodies = _ensure_len(block.get("issue_bodies"), "", n)
                    bodies[idx] = new_body
                    block["issue_bodies"] = bodies

                if new_labels is not None:
                    labels = _ensure_len(block.get("labels"), [], n)
                    labels[idx] = list(new_labels)
                    block["labels"] = labels

                # Touch updated_ts if present
                if "updated_ts" in block and isinstance(block["updated_ts"], list):
                    from datetime import datetime, timezone
                    iso = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
                    uts = _ensure_len(block.get("updated_ts"), iso, n)
                    uts[idx] = iso
                    block["updated_ts"] = uts

                return json.dumps(
                    {"message": "Issue updated", "number": target, "state": (new_state or block.get("issue_states", [None])[idx])},
                    indent=2
                )

        # 2) Flat rows (created by CreateIssue)
        for row in _issues(data):
            if row.get("repo_name") == repo_name and row.get("number") == target:
                if new_state is not None:
                    row["state"] = new_state
                if new_title is not None:
                    row["title"] = new_title
                if new_body is not None:
                    row["body"] = new_body
                if new_labels is not None:
                    row["labels"] = list(new_labels)
                return json.dumps({"message": "Issue updated", "number": target, "state": row.get("state")}, indent=2)

        return json.dumps({"error": "Issue not found."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_issue",
                "description": "Updates an issue's fields (state/title/body/labels).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                        "state": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "labels": {"type": "array", "items": {"type": "string"}},
                        "updates": {"type": "string"}  # legacy alias for state
                    },
                    "required": ["repo_name", "issue_number"]
                }
            }
        }

class AddIssueComment(Tool):
    """Adds a comment to an issue. Supports both aggregated blocks and flat issue rows."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        issue_number = kwargs.get("issue_number")
        comment = kwargs.get("comment", "")

        if not all([repo_name, issue_number is not None, comment is not None]):
            return json.dumps({"error": "repo_name, issue_number, and comment are required."}, indent=2)

        target = int(issue_number)
        me = _auth(data)["username"]  # keep parity with CreateIssue

        # 1) Aggregated blocks (original dataset shape)
        for block in _issues(data):
            if block.get("repo_name") != repo_name:
                continue

            nums = block.get("issue_numbers")
            if isinstance(nums, list) and target in nums:
                idx = nums.index(target)

                # Ensure parallel lists exist and are long enough
                if "issue_comments" not in block or not isinstance(block["issue_comments"], list):
                    block["issue_comments"] = [[] for _ in nums]
                while len(block["issue_comments"]) < len(nums):
                    block["issue_comments"].append([])

                block["issue_comments"][idx].append(comment)

                # Optionally track comment user if the structure exists
                if "issue_comment_users" in block and isinstance(block["issue_comment_users"], list):
                    while len(block["issue_comment_users"]) < len(nums):
                        block["issue_comment_users"].append([])
                    block["issue_comment_users"][idx].append(me)

                # Update updated_ts if present (keeps dataset consistent)
                if "updated_ts" in block and isinstance(block["updated_ts"], list):
                    from datetime import datetime, timezone
                    iso = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
                    if len(block["updated_ts"]) < len(nums):
                        block["updated_ts"] += [iso] * (len(nums) - len(block["updated_ts"]))
                    block["updated_ts"][idx] = iso

                return json.dumps({"message": "Comment added."}, indent=2)

        # 2) Flat issue rows (created by CreateIssue)
        for row in _issues(data):
            if row.get("repo_name") == repo_name and row.get("number") == target:
                comments = row.get("comments")
                if not isinstance(comments, list):
                    comments = []
                comments.append(comment)
                row["comments"] = comments
                # keep a lightweight timestamp here too, if you want
                return json.dumps({"message": "Comment added."}, indent=2)

        return json.dumps({"error": "Issue not found."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "add_issue_comment",
                "description": "Adds a comment to an issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                        "comment": {"type": "string"},
                    },
                    "required": ["repo_name", "issue_number", "comment"]
                }
            }
        }

class MergePullRequest(Tool):
    """Merges the specified pull request into its base branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        pr_number = kwargs.get("pr_number")

        if not all([repo_name, pr_number]):
            return json.dumps({"error": "repo_name and pr_number are required."}, indent=2)

        me = _auth(data)["username"]
        pr = next(
            (p for p in _prs(data)
             if p["owner"] == me and p["repo_name"] == repo_name and int(pr_number) in p["pr_numbers"]),
            None
        )
        if not pr:
            return json.dumps({"error": "Pull request not found."}, indent=2)

        try:
            idx = pr["pr_numbers"].index(int(pr_number))
        except ValueError:
            return json.dumps({"error": "PR number not found in PR block."}, indent=2)

        # ✅ Validate PR is open before doing anything
        if pr["pr_states"][idx] != "open":
            return json.dumps({"error": "PR is not open."}, indent=2)

        # ✅ Forbid merging when head == base (no-op merges)
        head_branch = pr["head_branches"][idx]
        base_branch = pr["base_branches"][idx]
        if head_branch == base_branch:
            pr["pr_states"][idx] = "rejected"
            return json.dumps({
                "message": "Pull request rejected.",
                "reason": "head and base branch are the same",
                "merged": "false"
            }, indent=2)

        repo = _find_repo_record(data, repo_name)
        head_idx = _branch_index(repo, head_branch)
        base_idx = _branch_index(repo, base_branch)

        # Merge = replace base branch content with head branch content
        repo["branch_files"][base_idx] = list(repo["branch_files"][head_idx])
        repo["branch_contents"][base_idx] = list(repo["branch_contents"][head_idx])
        repo["branch_shas"][base_idx] = get_next_commit_sha()

        pr["pr_states"][idx] = "merged"

        return json.dumps({"message": "Pull request merged.", "merged": "true", "merge_method": "merge"}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "merge_pull_request",
                "description": "Merges the pull request into base branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"}
                    },
                    "required": ["repo_name", "pr_number"]
                }
            }
        }

class CommentOnPullRequest(Tool):
    """Adds a human comment to the pull request discussion thread."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        pr_number = kwargs.get("pr_number")
        comment = kwargs.get("comment")

        if not all([repo_name, pr_number, comment]):
            return json.dumps({"error": "repo_name, pr_number and comment are required."}, indent=2)

        me = _auth(data)["username"]
        pr = next((p for p in _prs(data) if p["owner"] == me and p["repo_name"] == repo_name and int(pr_number) in p["pr_numbers"]), None)

        if not pr:
            return json.dumps({"error": "Pull request not found."}, indent=2)

        pr.setdefault("comments", []).append({
            "author": me,
            "comment": comment,
            "timestamp": get_current_timestamp()
        })

        return json.dumps({"message": "Comment added to pull request."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "comment_on_pull_request",
                "description": "Adds a comment to a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "comment": {"type": "string"}
                    },
                    "required": ["repo_name", "pr_number", "comment"]
                }
            }
        }

class CreatePullRequestReview(Tool):
    """Adds a review (approve or changes requested or just a comment) to a pull request."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        pr_number = kwargs.get("pr_number")
        review_decision = kwargs.get("review_decision")  # approve | request_changes | comment
        comment = kwargs.get("comment", "")

        if not all([repo_name, pr_number, review_decision]):
            return json.dumps({"error": "repo_name, pr_number, and review_decision are required."}, indent=2)

        if review_decision not in ["approve", "request_changes", "comment"]:
            return json.dumps({"error": "Invalid review_decision (must be 'approve' or 'request_changes' or 'comment)."}, indent=2)

        me = _auth(data)["username"]
        pr = next((p for p in _prs(data) if p["owner"] == me and p["repo_name"] == repo_name and int(pr_number) in p["pr_numbers"]), None)

        if not pr:
            return json.dumps({"error": "Pull request not found."}, indent=2)

        pr.setdefault("reviews", []).append({
            "author": me,
            "decision": review_decision,
            "comment": comment,
            "timestamp": get_current_timestamp()
        })

        return json.dumps({"message": "Review submitted."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_pull_request_review",
                "description": "Adds a review (approve or request_changes or comment) to a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "review_decision": {"type": "string", "enum": ["approve", "request_changes", "comment"]},
                        "comment": {"type": "string"}
                    },
                    "required": ["repo_name", "pr_number", "review_decision"]
                }
            }
        }

class RequestPullRequestReviewers(Tool):
    """Requests one or more reviewers on a pull request."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        pr_number = kwargs.get("pr_number")
        reviewers = kwargs.get("reviewers", [])  # list[str]

        if not all([repo_name, pr_number]) or not isinstance(reviewers, list) or len(reviewers) == 0:
            return json.dumps({"error": "repo_name, pr_number and non-empty reviewers[] are required."}, indent=2)

        me = _auth(data)["username"]

        # find PR owned by current user (consistent with your other tools)
        pr = next(
            (p for p in _prs(data)
             if p["owner"] == me and p["repo_name"] == repo_name and int(pr_number) in p["pr_numbers"]),
            None
        )
        if not pr:
            return json.dumps({"error": "Pull request not found."}, indent=2)

        # Add reviewers
        existing = set(pr.get("requested_reviewers", []))
        for r in reviewers:
            if r != me:
                existing.add(r)
        pr["requested_reviewers"] = sorted(existing)

        return json.dumps({
            "message": "Reviewers requested.",
            "pr_number": pr_number,
            "requested_reviewers": pr["requested_reviewers"]
        }, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "request_pull_request_reviewers",
                "description": "Request reviewers on a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "reviewers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Usernames to request for review"
                        }
                    },
                    "required": ["repo_name", "pr_number", "reviewers"]
                }
            }
        }

class AddLabelToIssue(Tool):
    """Adds a label to the specified issue. Supports both aggregated and flat issue shapes."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        issue_number = kwargs.get("issue_number")
        label = kwargs.get("label")

        if not all([repo_name, issue_number, label]):
            return json.dumps({"error": "repo_name, issue_number, and label are required."}, indent=2)

        target = int(issue_number)

        # 1) Support aggregated blocks (original dataset shape)
        for block in _issues(data):
            if block.get("repo_name") != repo_name:
                continue
            if "issue_numbers" in block and "labels" in block:
                issue_numbers = block["issue_numbers"]
                if target in issue_numbers:
                    idx = issue_numbers.index(target)
                    labels_at_idx = list(set(block["labels"][idx] + [label]))
                    block["labels"][idx] = labels_at_idx
                    return json.dumps({"message": f"Label '{label}' added."}, indent=2)

        # 2) Support flat rows (created by CreateIssue)
        for row in _issues(data):
            if row.get("repo_name") == repo_name and row.get("number") == target:
                cur = set(row.get("labels", []))
                cur.add(label)
                row["labels"] = list(cur)
                return json.dumps({"message": f"Label '{label}' added."}, indent=2)

        return json.dumps({"error": "Issue not found."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "add_label_to_issue",
                "description": "Adds a label to an issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                        "label": {"type": "string"},
                    },
                    "required": ["repo_name", "issue_number", "label"]
                }
            }
        }

class CreateRelease(Tool):
    """Creates a release for a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name, tag, body = kwargs.get("repo_name"), kwargs.get("tag"), kwargs.get("body", "")
        if not all([repo_name, tag]):
            return json.dumps({"error": "repo_name and tag are required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        repo.setdefault("releases", []).append({
            "tag_name": tag,
            "body": body,
            "created_by": _auth(data)["username"],
            "created_at": get_current_timestamp()
        })

        return json.dumps({
            "message": "Release created.",
            "repo_name": repo_name,
            "tag_name": tag,
            "title": kwargs.get("title", "")
        }, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_release",
                "description": "Creates a new release (tag + body).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "tag": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"}
                    },
                    "required": ["repo_name", "tag"]
                }
            }
        }


class GetLatestRelease(Tool):
    """Returns the latest release (by timestamp) for a repo."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        releases = repo.get("releases", [])
        if not releases:
            return json.dumps({"error": "No releases found."}, indent=2)

        latest = sorted(releases, key=lambda r: r["created_at"], reverse=True)[0]
        return json.dumps(latest, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_latest_release",
                "description": "Gets the latest release for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"}
                    },
                    "required": ["repo_name"]
                }
            }
        }

class ListRepoTopics(Tool):
    """Lists all topics for a given repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo = _find_repo_record(data, kwargs.get("repo_name"))
        return json.dumps({"topics": repo.get("topics", [])}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_repo_topics",
                "description": "Returns the list of repository topics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"}
                    },
                    "required": ["repo_name"]
                }
            }
        }

class AddRepoTopic(Tool):
    """Adds a topic to a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo = _find_repo_record(data, kwargs.get("repo_name"))
        topic = kwargs.get("topic")
        if not topic:
            return json.dumps({"error": "topic is required."}, indent=2)

        topics = set(repo.get("topics", []))
        topics.add(topic)
        repo["topics"] = list(topics)
        return json.dumps({"message": f"Topic '{topic}' added."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "add_repo_topic",
                "description": "Adds a topic to a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "topic": {"type": "string"}
                    },
                    "required": ["repo_name", "topic"]
                }
            }
        }

class RemoveRepoTopic(Tool):
    """Removes a topic from a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo = _find_repo_record(data, kwargs.get("repo_name"))
        topic = kwargs.get("topic")
        if not topic:
            return json.dumps({"error": "topic is required."}, indent=2)

        repo["topics"] = [t for t in repo.get("topics", []) if t != topic]
        return json.dumps({"message": f"Topic '{topic}' removed."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "remove_repo_topic",
                "description": "Removes a topic from a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "topic": {"type": "string"}
                    },
                    "required": ["repo_name", "topic"]
                }
            }
        }

class GetBranchProtection(Tool):
    """Gets protection settings for a branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo = _find_repo_record(data, kwargs.get("repo_name"))
        idx = _branch_index(repo, kwargs.get("branch"))
        if "branch_protections" not in repo:
            repo["branch_protections"] = [False] * len(repo.get("branches", []))

        # Initialize if missing
        if "branch_protection_rules" not in repo:
            repo["branch_protection_rules"] = {}

        protection = repo.get("branch_protections", [{}])[idx]
        rules = repo.get("branch_protection_rules", {})[idx]

        return json.dumps({"protected": protection if protection else "false",
            "rules": rules}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_branch_protection",
                "description": "Gets branch protection rules for a given branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"}
                    },
                    "required": ["repo_name", "branch"]
                }
            }
        }

class SetBranchProtection(Tool):
    """Sets branch protection rules for a given branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo = _find_repo_record(data, kwargs.get("repo_name"))
        idx = _branch_index(repo, kwargs.get("branch"))
        protection = kwargs.get("protected")
        rules = kwargs.get("rules")

        # Initialize if missing
        if "branch_protections" not in repo:
            repo["branch_protections"] = [False] * len(repo.get("branches", []))
        repo["branch_protections"][idx] = protection

        # Initialize if missing
        if "branch_protection_rules" not in repo:
            repo["branch_protection_rules"] = {}

        repo["branch_protection_rules"][idx] = rules
        return json.dumps({
            "message": "Branch protection enabled." if protection else "Branch protection disabled.",
            "repo_name": repo["repo_name"],
            "branch": kwargs.get("branch"),
            "protected": protection if protection else "false",
            "rules": rules
        }, indent=2)


    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_branch_protection",
                "description": "Sets protection rules for a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "protected": {"type": "string"},
                        "rules": {"type": "object", "description": "Protection rule dictionary"}
                    },
                    "required": ["repo_name", "branch", "rules", "protected"]
                }
            }
        }

class SearchRepositories(Tool):
    """Searches repositories by name substring or owner."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name_query = kwargs.get("name", "").lower()
        owner_query = kwargs.get("owner", "").lower()
        results = []

        for repo in _repos(data):
            if (
                (name_query and name_query in repo.get("repo_name", "").lower()) or
                (owner_query and owner_query in repo.get("owner", "").lower())
            ):
                results.append(repo)

        return json.dumps({"results": results}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "search_repositories",
                "description": "Search repositories by name or owner substring.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "owner": {"type": "string"},
                    },
                },
            }
        }

class ListCommits(Tool):
    """Lists commits for a given repository and optional branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        branch = kwargs.get("branch")
        commits = _commits(data)

        for entry in commits:
            if entry["repo_name"] == repo_name:
                if not branch:
                    return json.dumps(entry, indent=2)

                if branch in entry["branch_names"]:
                    idx = entry["branch_names"].index(branch)
                    return json.dumps({
                        "branch": branch,
                        "commit_shas": entry["commit_shas"][idx],
                        "messages": entry["commit_messages"][idx],
                        "authors": entry["commit_authors"][idx],
                        "timestamps": entry["commit_timestamps"][idx],
                    }, indent=2)

        return json.dumps({
            "branch": branch,
            "commit_shas": [],
            "messages": [],
            "authors": [],
            "timestamps": [],
        }, indent=2)


    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_commits",
                "description": "Lists commits in a repository and branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name"]
                }
            }
        }

class SearchIssues(Tool):
    """Searches issues by title, label, or body keyword."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        query = kwargs.get("query", "").lower()
        results = []

        for issue in _issues(data):
            # print("ISWEU::", issue)
            title = issue.get("title", "").lower()
            body = issue.get("body", "").lower()
            raw_labels = issue.get("labels", [])
            flat_labels = [l for sub in raw_labels for l in (sub if isinstance(sub, list) else [sub])]
            labels = [l.lower() for l in flat_labels]


            if query in title or query in body or query in labels:
                results.append(issue.get("number"))

        return json.dumps({"results": results}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "search_issues",
                "description": "Search issues by keyword in title, body, or labels.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"}
                    },
                    "required": ["query"]
                }
            }
        }

class ListRepositories(Tool):
    """Lists all repositories owned by the current user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        owned = [r for r in _repos(data) if r["owner"] == me]
        return json.dumps({"repositories": owned}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_repositories",
                "description": "Returns all repositories owned by the current user.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }

class ListFiles(Tool):
    """Lists all file paths in the given branch of a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name, branch = kwargs.get("repo_name"), kwargs.get("branch")
        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        files = repo["branch_files"][idx]
        return json.dumps({"files": files}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_files",
                "description": "Lists all files in a given branch of a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"}
                    },
                    "required": ["repo_name", "branch"]
                }
            }
        }

class CreateRepository(Tool):
    """Creates a new repository owned by the current user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        visibility = kwargs.get("visibility", "public")
        default_branch = kwargs.get("default_branch", "main")

        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        me = _auth(data)["username"]

        repos = _repos(data)
        if any(r["owner"] == me and r["repo_name"] == repo_name for r in repos):
            return json.dumps({"error": "Repository already exists."}, indent=2)

        new_repo = {
            "owner": me,
            "repo_name": repo_name,
            "visibility": visibility,
            "default_branch": default_branch,
            "branches": [default_branch],
            "branch_files": [[]],
            "branch_contents": [[]],
            "branch_shas": [get_next_commit_sha()],
            "branch_protections": [{}],
            "topics": [],
            "releases": [],
        }
        repos.append(new_repo)

        return json.dumps({"message": "Repository created", "repo_name": repo_name}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_repository",
                "description": "Creates a new repository for the current user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "visibility": {"type": "string"},
                        "default_branch": {"type": "string"},
                    },
                    "required": ["repo_name"]
                }
            }
        }

class DeleteBranch(Tool):
    """Deletes a branch from a repository, except the default branch (deduped)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        branch = kwargs.get("branch")

        if not all([repo_name, branch]):
            return json.dumps({"error": "repo_name and branch are required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        if branch == repo.get("default_branch"):
            return json.dumps({"error": "Cannot delete the default branch."}, indent=2)

        if branch not in repo.get("branches", []):
            return json.dumps({"error": "Branch not found."}, indent=2)

        idx = repo["branches"].index(branch)

        # Remove parallel entries safely
        for key in ["branches", "branch_files", "branch_contents", "branch_shas"]:
            if key in repo and len(repo[key]) > idx:
                repo[key].pop(idx)

        # Optional arrays
        if "branch_protections" in repo and len(repo["branch_protections"]) > idx:
            repo["branch_protections"].pop(idx)

        return json.dumps(
            {"message": f"Branch '{branch}' deleted from repo '{repo_name}'"}, indent=2
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "delete_branch",
                "description": "Deletes a branch (except the default branch).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name", "branch"],
                },
            },
        }

class ListCodeScanningAlerts(Tool):
    """Lists all code scanning alerts for a given repository and optional severity."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        severity_filter = kwargs.get("severity")

        flat_alerts = []

        for record in _alerts(data):
            if repo_name and record.get("repo_name") != repo_name:
                continue

            for i, alert_number in enumerate(record.get("alert_numbers", [])):
                alert = {
                    "alert_number": alert_number,
                    "severity": record.get("severities", [])[i],
                    "state": record.get("states", [])[i],
                    "description": record.get("descriptions", [])[i],
                }

                if severity_filter:
                    if alert["severity"].lower() != severity_filter.lower():
                        continue

                flat_alerts.append(alert)

        return json.dumps({"alerts": flat_alerts}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_code_scanning_alerts",
                "description": "Lists all code scanning alerts optionally filtered by repository and severity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "severity": {"type": "string"},
                    },
                }
            }
        }

class ListTerminalLastMessage(Tool):
    """Returns last terminal log entry."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        terminal_log = _terminal(data)
        # print("terminal log:", terminal_log)
        if not terminal_log:
            return json.dumps({"error": "No terminal messages found."}, indent=2)

        # Get the last message from the most recent log group
        last_ts = terminal_log[-1]["printed_ts"]
        # print("term_log::", terminal_log)
        last_item = terminal_log[-1]
        last_msg = (
            last_item.get("messages")[-1]
            if last_item.get("messages")
            else last_item.get("message")
        )
        print("last_msg:::", last_msg)

        return json.dumps({
            "timestamp": last_ts,
            "message": last_msg
        }, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_terminal_last_message",
                "description": "Returns terminal last log message with timestamp.",
                "parameters": {"type": "object", "properties": {}},
            }
        }

class GetHeadSha(Tool):
    """Returns the SHA of the latest commit on a given branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name, branch = kwargs.get("repo_name"), kwargs.get("branch")
        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        return json.dumps({"branch": repo["branches"][idx], "sha": repo["branch_shas"][idx]}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_head_sha",
                "description": "Gets the SHA of the head commit on a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name"]
                }
            }
        }

class AppendTerminal(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        msg = kwargs.get("message")
        if not msg:
            return json.dumps({"error": "message is required."}, indent=2)
        entry = {"printed_ts": get_current_timestamp(), "message": str(msg)}
        _terminal(data).append(entry)
        return json.dumps(entry, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "append_terminal",
                "description": "Appends a message to terminal log with timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {"type": "string"}
                    },
                    "required": ["message"]
                }
            }
        }

class GetMe(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        existing = data.get("_me")
        if isinstance(existing, dict) and "username" in existing and not kwargs:
            return json.dumps(existing, indent=2)

        username = kwargs.get("username")
        if username:
            auth_list = data.get("authentication") or []
            match = next((a for a in auth_list if a.get("username") == username), None)
            if not match:
                return json.dumps({"error": f"Unknown username: {username}"}, indent=2)
            me = {"username": match.get("username"), "email": match.get("email")}
            data["_me"] = me
            return json.dumps(me, indent=2)

        return json.dumps({"error": "No acting identity set. Provide username to get_me."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_me",
                "description": "Gets/sets the acting identity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"}
                    },
                    "required": ["username"]
                }
            }
        }

class GetFileContents(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        path = kwargs.get("path")
        branch = kwargs.get("branch")

        if not all([repo_name, path]):
            return json.dumps({"error": "repo_name and path are required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        files = repo["branch_files"][idx]
        # print("fuiles:", files)
        contents = repo["branch_contents"][idx]
        # print("contents:", contents)

        if path not in files:
            return json.dumps({"error": f"File '{path}' not found."}, indent=2)

        i = files.index(path)
        return json.dumps({"path": path, "content": contents[i]}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_file_contents",
                "description": "Gets the contents of a file in a repository branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "path": {"type": "string"}
                    },
                    "required": ["repo_name", "path"]
                }
            }
        }

class CreatePullRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs["repo_name"]
        title = kwargs["title"]
        body = kwargs.get("body", "")
        head = kwargs["head"]
        base = kwargs["base"]

        me = _auth(data)["username"]
        repo = _find_repo_record(data, repo_name)
        # print("repooo:", repo)

        # Ensure pull request record exists
        pr_block = next(
            (b for b in _prs(data) if b.get("owner") == me and b.get("repo_name") == repo_name),
            None,
        )
        if not pr_block:
            # ✅ Create PR block if it doesn't exist
            pr_block = {
                "owner": me,
                "repo_name": repo_name,
                "pr_numbers": [],
                "pr_titles": [],
                "pr_bodies": [],
                "pr_states": [],
                "head_branches": [],
                "base_branches": [],
                "head_shas": [],
                "mergeable_flags": [],
                "merged_flags": [],
                "created_ts": [],
                "updated_ts": [],
                "pr_files": [],
                "pr_comments": [],
                "pr_comment_users": [],
                "reviewers": [],
                "review_states": [],
                "review_events": [],
            }
            _prs(data).append(pr_block)

        # Append PR metadata
        pr_number = 1
        pr_block["pr_numbers"].append(pr_number)
        pr_block["pr_titles"].append(title)
        pr_block["pr_bodies"].append(body)
        pr_block["pr_states"].append("open")
        pr_block["head_branches"].append(head)
        pr_block["base_branches"].append(base)
        pr_block["head_shas"].append("sha_0000000000000000000000000000000000000000")
        pr_block["mergeable_flags"].append(True)
        pr_block["merged_flags"].append(False)
        pr_block["created_ts"].append("2025-08-23T12:00:00Z")
        pr_block["updated_ts"].append("2025-08-23T12:00:00Z")

        # Detect changed files based on filenames and content
        try:
            head_idx = repo["branches"].index(head)
            base_idx = repo["branches"].index(base)
        except ValueError:
            return json.dumps({"error": "Invalid head or base branch."}, indent=2)

        head_files = set(repo["branch_files"][head_idx])
        base_files = set(repo["branch_files"][base_idx])
        file_diff = head_files.symmetric_difference(base_files)

        # Also check for content changes if filenames are same
        if not file_diff:
            file_diff = set()
            for path in repo["branch_files"][head_idx]:
                if path in repo["branch_files"][base_idx]:
                    head_i = next((i for i, p in enumerate(repo["branch_files"][head_idx]) if p == path), None)
                    base_i = next((i for i, p in enumerate(repo["branch_files"][base_idx]) if p == path), None)

                    if head_i is not None and base_i is not None:
                        if repo["branch_contents"][head_idx][head_i] != repo["branch_contents"][base_idx][base_i]:
                            file_diff.add(path)

                    if repo["branch_contents"][head_idx][head_i] != repo["branch_contents"][base_idx][base_i]:
                        file_diff.add(path)

        changed_files = sorted(list(file_diff))

        # Append changed file list as nested list (List[List[str]])
        if "pr_files" not in pr_block:
            pr_block["pr_files"] = []
        pr_block["pr_files"].append([changed_files])

        # Initialize empty nested structures for comments/reviews if needed
        pr_block.setdefault("pr_comments", []).append([[]])
        pr_block.setdefault("pr_comment_users", []).append([[]])
        pr_block.setdefault("reviewers", []).append([[]])
        pr_block.setdefault("review_states", []).append([[]])
        pr_block.setdefault("review_events", []).append([[]])

        return json.dumps({
            "message": "Pull request opened",
            "title": title,
            "base": base,
            "head": head,
            "pr_number": pr_number
        }, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_pull_request",
                "description": "Creates a pull request from head to base branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "base": {"type": "string"},
                        "head": {"type": "string"},
                    },
                    "required": ["repo_name", "title", "base", "head"]
                }
            }
        }

class ListPullRequestFiles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        pr_number = _resolve_pr_number(data, repo_name, kwargs.get("pr_number"))

        prs = _prs(data)
        pr_block = next((b for b in prs if b.get("repo_name") == repo_name), None)

        if not pr_block:
            return json.dumps({"error": "Pull request not found."}, indent=2)

        try:
            idx = pr_block["pr_numbers"].index(pr_number)
        except Exception:
            return json.dumps({"files": []}, indent=2)

        try:
            pr_files = pr_block["pr_files"][idx][0]
            if pr_files:
                return json.dumps({"files": pr_files}, indent=2)
        except Exception:
            pass  # fallback below

        # fallback to compute diff
        head_branch = pr_block["head_branches"][idx]
        base_branch = pr_block["base_branches"][idx]

        try:
            repo = next(r for r in _repos(data) if r["repo_name"] == repo_name)
            head_idx = _branch_index(repo, head_branch)
            base_idx = _branch_index(repo, base_branch)

            head_files = set(repo["branch_files"][head_idx])
            base_files = set(repo["branch_files"][base_idx])

            diff_files = list(head_files.symmetric_difference(base_files))
            if not diff_files:
                return json.dumps({"error": "No file diff found in fallback."}, indent=2)

            return json.dumps({"files": diff_files}, indent=2)
        except Exception as e:
            return json.dumps({"error": f"No file diff recorded for this pull request. {str(e)}"}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_pull_request_files",
                "description": "Lists files changed in pull request's head branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "pr_number"]
                }
            }
        }

class ListOpenPullRequests(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        me = _auth(data)["username"]

        prs = _prs(data)
        for block in prs:
            # print("block:::", block)
            if block["owner"] == me and block["repo_name"] == repo_name:
                results = [
                    {
                        "number": n,
                        "title": t,
                        "state": s,
                        "base": b,
                        "head": h
                    }
                    for n, t, s, b, h in zip(
                        block["pr_numbers"],
                        block["pr_titles"],
                        block["pr_states"],
                        block["base_branches"],
                        block["head_branches"]
                    ) if s == "open"
                ]
                return json.dumps({"pull_requests": results}, indent=2)

        return json.dumps({"pull_requests": []}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_open_pull_requests",
                "description": "Lists all open pull requests in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"}
                    },
                    "required": ["repo_name"]
                }
            }
        }

class InitializePullRequestsBlock(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs["repo_name"]
        me = _auth(data)["username"]
        existing = next((pr for pr in _prs(data) if pr["owner"] == me and pr["repo_name"] == repo_name), None)
        if existing:
            return json.dumps({"message": "PR block already exists"})
        _prs(data).append({
            "owner": me,
            "repo_name": repo_name,
            "pr_numbers": [],
            "pr_titles": [],
            "pr_bodies": [],
            "pr_states": [],
            "head_branches": [],
            "base_branches": [],
            "head_shas": [],
            "mergeable_flags": [],
            "merged_flags": [],
            "created_ts": [],
            "updated_ts": [],
            "pr_files": [],
        })
        return json.dumps({"message": "Initialized pull_requests block for repo."})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "initialize_pull_requests_block",
                "description": "Manually initializes a pull_requests entry for a new repo",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                    },
                    "required": ["repo_name"]
                }
            }
        }

TOOLS = [
    GetMe(),
    GetRepository(),
    GetDefaultBranch(),
    CreateBranch(),
    WriteFileToBranch(),
    CreatePullRequestReview(),
    CreatePullRequest(),
    CreateRepository(),
    DeleteBranch(),
    CommitChangesToBranch(),
    GetPullRequest(),
    CommentOnPullRequest(),
    MergePullRequest(),
    CreateIssue(),
    UpdateIssue(),
    AddIssueComment(),
    ListIssuesByLabel(),
    ListBranches(),
    RenameRepository(),
    ListRepoTopics(),
    AddRepoTopic(),
    GetBranchProtection(),
    SetBranchProtection(),
    ListPullRequests(),
    GetIssue(),
    AddLabelToIssue(),
    CreateRelease(),
    GetLatestRelease(),
    SearchRepositories(),
    ListCommits(),
    SearchIssues(),
    ListFiles(),
    GetHeadSha(),
    ListCodeScanningAlerts(),
    AppendTerminal(),
    GetFileContents(),
    ListPullRequestFiles(),
    ListOpenPullRequests(),
    InitializePullRequestsBlock(),
    ListTerminalLastMessage(),
    RequestPullRequestReviewers(),
    ListRepositories(),
    RemoveRepoTopic(),
    SetRepositoryVisibility(),
]
