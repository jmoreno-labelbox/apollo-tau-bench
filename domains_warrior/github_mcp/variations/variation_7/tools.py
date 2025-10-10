from typing import Any, Dict, List, Optional
import json
from datetime import datetime
from domains.dto import Tool


def _actor_name(data: Dict[str, Any]) -> str:
    auth = data.get("authentication") or [{}]
    return auth[0].get("username") or "anonymous"


DEFAULT_TS = "2025-08-21T12:00:00Z"

def get_current_timestamp() -> str:
    """Deterministic timestamp used across all create/update ops."""
    return DEFAULT_TS


def _repos(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("repositories", [])


def _issues(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("issues", [])


def _prs(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("pull_requests", [])


def _commits(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("commits", [])


def _alerts(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("code_scanning_alerts", [])


def _terminal(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("terminal", [])


def _find_repo(data: Dict[str, Any], owner: str, repo: str) -> Optional[Dict[str, Any]]:
    for r in _repos(data):
        if r.get("owner") == owner and (r.get("repo_name") or r.get("name")) == repo:
            return r
    return None


#  tools 

class WhoAmI(Tool):
    """Return the current user (from authentication)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        auth = data.get("authentication") or [{}]
        user = auth[0]
        return json.dumps({
            "username": user.get("username"),
            "email": user.get("email")
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "who_am_i",
                "description": "Return the authenticated username and email.",
                "parameters": {"type": "object", "properties": {}}
            },
        }


class ListRepos(Tool):
    """List repositories owned by the authenticated user."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _actor_name(data)
        items = [r for r in _repos(data) if r.get("owner") == me]
        return json.dumps(items)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_repos",
                "description": "List repositories for the current user.",
                "parameters": {"type": "object", "properties": {}}
            },
        }


class CreateRepo(Tool):
    """Create a repository with basic fields."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _actor_name(data)
        name = kwargs.get("name")
        private = bool(kwargs.get("private", False))
        if not name:
            raise RuntimeError("'name' is required")
        if _find_repo(data, me, name):
            raise RuntimeError("Repository already exists")
        repo = {
            "owner": me,
            "repo_name": name,
            "private": private,
            "default_branch": "main",
            "branches": ["main"],
            "created_at": get_current_timestamp(),
            "topics": [],
        }
        _repos(data).append(repo)
        return json.dumps(repo)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_repo",
                "description": "Create a repository for the current user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "private": {"type": "boolean"}
                    },
                    "required": ["name"]
                }
            },
        }


class DeleteRepo(Tool):
    """Delete a repository you own."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _actor_name(data)
        name = kwargs.get("name")
        if not name:
            raise RuntimeError("'name' is required")
        before = len(_repos(data))
        data["repositories"] = [r for r in _repos(data) if not (r.get("owner") == me and (r.get("repo_name") or r.get("name")) == name)]
        return json.dumps({"deleted": before - len(_repos(data))})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_repo",
                "description": "Delete a repository by name (owned by you).",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"]
                }
            },
        }


class ListBranches(Tool):
    """List branches for a repo."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        r = _find_repo(data, owner, repo)
        if not r:
            raise RuntimeError("Repository not found")
        return json.dumps({
            "default": r.get("default_branch"),
            "branches": r.get("branches") or []
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_branches",
                "description": "List branches in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"}
                    },
                    "required": ["repo"]
                }
            },
        }


class CreateBranch(Tool):
    """Create a new branch off default."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        name = kwargs.get("branch")
        r = _find_repo(data, owner, repo)
        if not r:
            raise RuntimeError("Repository not found")
        if not name:
            raise RuntimeError("'branch' is required")
        branches = r.setdefault("branches", [])
        if name in branches:
            raise RuntimeError("Branch exists")
        branches.append(name)
        return json.dumps({"created": name})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_branch",
                "description": "Create a branch in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"}
                    },
                    "required": ["repo", "branch"]
                }
            },
        }


class OpenIssue(Tool):
    """Open a new issue."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        title = kwargs.get("title")
        body = kwargs.get("body", "")
        if not (_find_repo(data, owner, repo)):
            raise RuntimeError("Repository not found")
        if not title:
            raise RuntimeError("'title' is required")
        seq = sum(1 for it in _issues(data) if it.get("owner") == owner and it.get("repo") == repo) + 1
        issue = {
            "owner": owner,
            "repo": repo,
            "number": seq,
            "title": title,
            "body": body,
            "state": "open",
            "assignees": [],
            "labels": [],
            "comments": [],
            "created_at": get_current_timestamp(),
        }
        _issues(data).append(issue)
        return json.dumps(issue)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "open_issue",
                "description": "Create an issue in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"}
                    },
                    "required": ["repo", "title"]
                }
            },
        }


class ListIssues(Tool):
    """List issues for a repo with optional state filter."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        state = kwargs.get("state")
        result = [i for i in _issues(data) if i.get("owner") == owner and i.get("repo") == repo]
        if state:
            result = [i for i in result if i.get("state") == state]
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_issues",
                "description": "List issues in a repository (optionally by state).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "state": {"type": "string", "enum": ["open", "closed"]}
                    },
                    "required": ["repo"]
                }
            },
        }


class SetIssueState(Tool):
    """Close or reopen an issue."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        number = kwargs.get("number")
        state = kwargs.get("state")
        for i in _issues(data):
            if i.get("owner") == owner and i.get("repo") == repo and i.get("number") == number:
                i["state"] = state
                i["updated_at"] = get_current_timestamp()
                return json.dumps(i)
        raise RuntimeError("Issue not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_issue_state",
                "description": "Set issue state to open or closed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "state": {"type": "string", "enum": ["open", "closed"]}
                    },
                    "required": ["repo", "number", "state"]
                }
            },
        }


class CommentIssue(Tool):
    """Add a comment to an issue."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        number = kwargs.get("number")
        comment = kwargs.get("comment") or ""
        for i in _issues(data):
            if i.get("owner") == owner and i.get("repo") == repo and i.get("number") == number:
                i.setdefault("comments", []).append({
                    "author": _actor_name(data),
                    "message": comment,
                    "created_at": get_current_timestamp()
                })
                return json.dumps({"ok": True})
        raise RuntimeError("Issue not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "comment_issue",
                "description": "Add a comment to an issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "comment": {"type": "string"}
                    },
                    "required": ["repo", "number", "comment"]
                }
            },
        }


class AddLabel(Tool):
    """Add a label to an issue or PR."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        kind = kwargs.get("kind")
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        number = kwargs.get("number")
        label = kwargs.get("label")
        target_list = _issues(data) if kind == "issue" else _prs(data)
        for obj in target_list:
            if obj.get("owner") == owner and obj.get("repo") == repo and obj.get("number") == number:
                labels = obj.setdefault("labels", [])
                if label and label not in labels:
                    labels.append(label)
                return json.dumps(obj)
        raise RuntimeError("Target not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_label",
                "description": "Add a label to an issue or PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {"type": "string", "enum": ["issue", "pr"]},
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "label": {"type": "string"}
                    },
                    "required": ["kind", "repo", "number", "label"]
                }
            },
        }


class OpenPR(Tool):
    """Open a pull request."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        title = kwargs.get("title")
        head = kwargs.get("head_branch")
        base = kwargs.get("base_branch", "main")
        if not (_find_repo(data, owner, repo)):
            raise RuntimeError("Repository not found")
        seq = sum(1 for pr in _prs(data) if pr.get("owner") == owner and pr.get("repo") == repo) + 1
        pr = {
            "owner": owner,
            "repo": repo,
            "number": seq,
            "title": title or f"PR {seq}",
            "state": "open",
            "head": head,
            "base": base,
            "labels": [],
            "review_states": [],
            "created_at": get_current_timestamp(),
        }
        _prs(data).append(pr)
        return json.dumps(pr)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "open_pr",
                "description": "Open a pull request with head and base branches.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "title": {"type": "string"},
                        "head_branch": {"type": "string"},
                        "base_branch": {"type": "string"}
                    },
                    "required": ["repo", "head_branch"]
                }
            },
        }


class ListPRs(Tool):
    """List pull requests for a repo with optional state filter."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        state = kwargs.get("state")
        result = [p for p in _prs(data) if p.get("owner") == owner and p.get("repo") == repo]
        if state:
            result = [p for p in result if p.get("state") == state]
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_prs",
                "description": "List pull requests for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "state": {"type": "string", "enum": ["open", "closed", "merged"]}
                    },
                    "required": ["repo"]
                }
            },
        }


class MergePR(Tool):
    """Merge a PR by number (marks as merged)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        number = kwargs.get("number")
        for p in _prs(data):
            if p.get("owner") == owner and p.get("repo") == repo and p.get("number") == number:
                p["state"] = "merged"
                p["merged_at"] = get_current_timestamp()
                return json.dumps(p)
        raise RuntimeError("PR not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "merge_pr",
                "description": "Mark a pull request as merged.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"}
                    },
                    "required": ["repo", "number"]
                }
            },
        }


class SubmitReview(Tool):
    """Submit a review on a PR (approve, request_changes, or comment)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        number = kwargs.get("number")
        state = kwargs.get("state")
        note = kwargs.get("note", "")
        for p in _prs(data):
            if p.get("owner") == owner and p.get("repo") == repo and p.get("number") == number:
                p.setdefault("review_states", []).append({
                    "reviewer": _actor_name(data),
                    "state": state,
                    "note": note,
                    "created_at": get_current_timestamp(),
                })
                return json.dumps({"ok": True})
        raise RuntimeError("PR not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "submit_review",
                "description": "Submit a review on a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "state": {"type": "string", "enum": ["approve", "request_changes", "comment"]},
                        "note": {"type": "string"}
                    },
                    "required": ["repo", "number", "state"]
                }
            },
        }


class AddCommit(Tool):
    """Record a commit on a branch (very lightweight)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        branch = kwargs.get("branch", "main")
        message = kwargs.get("message") or ""
        if not (_find_repo(data, owner, repo)):
            raise RuntimeError("Repository not found")
        seq = sum(1 for c in _commits(data) if c.get("owner") == owner and c.get("repo") == repo) + 1
        sha = f"{branch}-{seq:06d}"
        c = {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "sha": sha,
            "message": message,
            "author": _actor_name(data),
            "timestamp": get_current_timestamp(),
        }
        _commits(data).append(c)
        return json.dumps(c)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_commit",
                "description": "Add a commit record to a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"},
                        "message": {"type": "string"}
                    },
                    "required": ["repo"]
                }
            },
        }


class ListCommits(Tool):
    """List commits for a repo (optional branch filter)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        branch = kwargs.get("branch")
        result = [c for c in _commits(data) if c.get("owner") == owner and c.get("repo") == repo]
        if branch:
            result = [c for c in result if c.get("branch") == branch]
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_commits",
                "description": "List commit records for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"}
                    },
                    "required": ["repo"]
                }
            },
        }


class SearchWork(Tool):
    """Simple text search across issues and PR titles."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        q = (kwargs.get("query") or "").lower()
        hits_issues = [i for i in _issues(data) if i.get("owner") == owner and i.get("repo") == repo and q in (i.get("title", "") + " " + i.get("body", "")).lower()]
        hits_prs = [p for p in _prs(data) if p.get("owner") == owner and p.get("repo") == repo and q in (p.get("title", "") or "").lower()]
        return json.dumps({"issues": hits_issues, "pull_requests": hits_prs})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_work",
                "description": "Search issues and PRs by text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "query": {"type": "string"}
                    },
                    "required": ["repo", "query"]
                }
            },
        }


class ListAlerts(Tool):
    """List code scanning alerts for a repo."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        result = [a for a in _alerts(data) if a.get("owner") == owner and a.get("repo") == repo]
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_alerts",
                "description": "List static analysis / scanning alerts for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"owner": {"type": "string"}, "repo": {"type": "string"}},
                    "required": ["repo"]
                }
            },
        }


class ResolveAlert(Tool):
    """Resolve a code scanning alert by id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        alert_id = kwargs.get("alert_id")
        for a in _alerts(data):
            if a.get("owner") == owner and a.get("repo") == repo and a.get("id") == alert_id:
                a["state"] = "resolved"
                a["resolved_at"] = get_current_timestamp()
                return json.dumps(a)
        raise RuntimeError("Alert not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "resolve_alert",
                "description": "Mark a code scanning alert as resolved.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "alert_id": {"type": "string"}
                    },
                    "required": ["repo", "alert_id"]
                }
            },
        }


class ActivityFeed(Tool):
    """Return a simple combined feed of recent issues/PRs/commits for a repo."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        limit = int(kwargs.get("limit", 20))
        feed: List[Dict[str, Any]] = []
        for i in _issues(data):
            if i.get("owner") == owner and i.get("repo") == repo:
                feed.append({"type": "issue", "title": i.get("title"), "state": i.get("state"), "ts": i.get("created_at")})
        for p in _prs(data):
            if p.get("owner") == owner and p.get("repo") == repo:
                feed.append({"type": "pr", "title": p.get("title"), "state": p.get("state"), "ts": p.get("created_at")})
        for c in _commits(data):
            if c.get("owner") == owner and c.get("repo") == repo:
                feed.append({"type": "commit", "title": c.get("message"), "state": "n/a", "ts": c.get("timestamp")})
        feed.sort(key=lambda x: x.get("ts") or "", reverse=True)
        return json.dumps(feed[:limit])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "activity_feed",
                "description": "Return a simple sorted feed of repo activity (issues/PRs/commits).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "limit": {"type": "integer"}
                    },
                    "required": ["repo"]
                }
            },
        }


class AppendTerminal(Tool):
    """Append a line to the in-memory terminal log."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cmd = kwargs.get("line") or ""
        _terminal(data).append({"line": cmd, "when": get_current_timestamp()})
        return json.dumps({"ok": True})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_terminal",
                "description": "Append a line to an in-memory terminal log.",
                "parameters": {"type": "object", "properties": {"line": {"type": "string"}}, "required": ["line"]}
            },
        }


class ListTerminal(Tool):
    """List terminal log entries (most recent first)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        limit = int(kwargs.get("limit", 50))
        logs = list(reversed(_terminal(data)))[:limit]
        return json.dumps(logs)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_terminal",
                "description": "List recent terminal log entries.",
                "parameters": {"type": "object", "properties": {"limit": {"type": "integer"}}}
            },
        }


class AssignUser(Tool):
    """Assign a user to an issue or PR."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        kind = kwargs.get("kind")
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        number = kwargs.get("number")
        username = kwargs.get("username")
        target_list = _issues(data) if kind == "issue" else _prs(data)
        for obj in target_list:
            if obj.get("owner") == owner and obj.get("repo") == repo and obj.get("number") == number:
                assignees = obj.setdefault("assignees", [])
                if username and username not in assignees:
                    assignees.append(username)
                return json.dumps(obj)
        raise RuntimeError("Target not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_user",
                "description": "Assign a username to an issue or PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {"type": "string", "enum": ["issue", "pr"]},
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "username": {"type": "string"}
                    },
                    "required": ["kind", "repo", "number", "username"]
                }
            },
        }


class SetMilestone(Tool):
    """Set a plain-text milestone field on an issue or PR."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        kind = kwargs.get("kind")
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        number = kwargs.get("number")
        milestone = kwargs.get("milestone")
        target_list = _issues(data) if kind == "issue" else _prs(data)
        for obj in target_list:
            if obj.get("owner") == owner and obj.get("repo") == repo and obj.get("number") == number:
                obj["milestone"] = milestone
                return json.dumps(obj)
        raise RuntimeError("Target not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_milestone",
                "description": "Set a milestone string on an issue or PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {"type": "string", "enum": ["issue", "pr"]},
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "milestone": {"type": "string"}
                    },
                    "required": ["kind", "repo", "number", "milestone"]
                }
            },
        }


class RemoveLabel(Tool):
    """Remove a label from an issue or PR."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        kind = kwargs.get("kind")
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        number = kwargs.get("number")
        label = kwargs.get("label")
        target_list = _issues(data) if kind == "issue" else _prs(data)
        for obj in target_list:
            if obj.get("owner") == owner and obj.get("repo") == repo and obj.get("number") == number:
                labels = obj.setdefault("labels", [])
                if label in labels:
                    labels.remove(label)
                return json.dumps(obj)
        raise RuntimeError("Target not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_label",
                "description": "Remove a label from an issue or PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {"type": "string", "enum": ["issue", "pr"]},
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "label": {"type": "string"}
                    },
                    "required": ["kind", "repo", "number", "label"]
                }
            },
        }


class ClosePR(Tool):
    """Close (but not merge) a PR."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        number = kwargs.get("number")
        for p in _prs(data):
            if p.get("owner") == owner and p.get("repo") == repo and p.get("number") == number:
                p["state"] = "closed"
                p["closed_at"] = get_current_timestamp()
                return json.dumps(p)
        raise RuntimeError("PR not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "close_pr",
                "description": "Close a pull request without merging.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"}
                    },
                    "required": ["repo", "number"]
                }
            },
        }


class ReopenPR(Tool):
    """Reopen a previously closed PR."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        number = kwargs.get("number")
        for p in _prs(data):
            if p.get("owner") == owner and p.get("repo") == repo and p.get("number") == number:
                p["state"] = "open"
                p["reopened_at"] = get_current_timestamp()
                return json.dumps(p)
        raise RuntimeError("PR not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reopen_pr",
                "description": "Reopen a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"}
                    },
                    "required": ["repo", "number"]
                }
            },
        }


class RepoTopics(Tool):
    """Set or list repository topics (simple list of strings)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        topics = kwargs.get("topics")
        r = _find_repo(data, owner, repo)
        if not r:
            raise RuntimeError("Repository not found")
        if isinstance(topics, list):
            r["topics"] = [str(t) for t in topics]
        return json.dumps({"topics": r.get("topics", [])})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "repo_topics",
                "description": "Set or get repo topics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "topics": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["repo"]
                }
            },
        }


class TransferRepo(Tool):
    """Transfer repository ownership to another username (string only)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        current = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        new_owner = kwargs.get("new_owner")
        r = _find_repo(data, current, repo)
        if not r:
            raise RuntimeError("Repository not found")
        r["owner"] = new_owner
        return json.dumps({"ok": True, "owner": new_owner})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_repo",
                "description": "Transfer repo ownership to a new owner.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "new_owner": {"type": "string"}
                    },
                    "required": ["repo", "new_owner"]
                }
            },
        }


TOOLS: List[type] = [
    WhoAmI(),
    ListRepos(),
    CreateRepo(),
    DeleteRepo(),
    ListBranches(),
    CreateBranch(),
    OpenIssue(),
    ListIssues(),
    SetIssueState(),
    CommentIssue(),
    AddLabel(),
    RemoveLabel(),
    AssignUser(),
    SetMilestone(),
    OpenPR(),
    ListPRs(),
    ClosePR(),
    ReopenPR(),
    MergePR(),
    SubmitReview(),
    AddCommit(),
    ListCommits(),
    SearchWork(),
    ListAlerts(),
    ResolveAlert(),
    ActivityFeed(),
    AppendTerminal(),
    ListTerminal(),
    RepoTopics(),
    TransferRepo(),
]

