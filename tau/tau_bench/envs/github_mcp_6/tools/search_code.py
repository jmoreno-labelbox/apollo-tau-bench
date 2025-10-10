# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchCode(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], query: str, language: str = None, repo_filter: str = None, page: int = 1, per_page: int = 30) -> str:
        """Search code patterns with comprehensive results, metadata, and filtering capabilities."""
        import time
        import re

        start_time = time.time()
        repositories = list(data.get("repositories", {}).values())
        all_matches = []

        if not query.strip():
            return json.dumps({
                "success": False,
                "error": "Search query cannot be empty",
                "error_code": "EMPTY_QUERY",
                "metadata": {
                    "search_timestamp": "2023-12-05T12:00:00Z"
                },
                "suggestions": [
                    "Provide a non-empty search query",
                    "Use specific keywords or patterns to search for"
                ]
            }, indent=2)

        # Mapping of file extensions to their corresponding programming languages.
        language_map = {
            'py': 'python', 'js': 'javascript', 'ts': 'typescript', 'java': 'java',
            'cpp': 'cpp', 'c': 'c', 'go': 'go', 'rs': 'rust', 'rb': 'ruby',
            'php': 'php', 'md': 'markdown', 'txt': 'text', 'json': 'json',
            'yml': 'yaml', 'yaml': 'yaml', 'xml': 'xml', 'html': 'html'
        }

        repositories_searched = []
        file_types_found = set()
        by_language = {}
        by_repository = {}

        for repo in repositories:
            repo_name = f"{repo['owner']}/{repo['repo_name']}"
            repositories_searched.append(repo_name)

            # Implement repository filter when provided.
            if repo_filter and repo_filter.lower() not in repo_name.lower():
                continue

            repo_matches = 0

            for branch_idx, files in enumerate(repo["branch_files"]):
                branch_name = repo.get("branches", ["main"])[branch_idx] if branch_idx < len(repo.get("branches", [])) else "main"

                for file_idx, file_path in enumerate(files):
                    content = repo["branch_contents"][branch_idx][file_idx]

                    # Identify the language of the file.
                    file_extension = file_path.split('.')[-1].lower() if '.' in file_path else 'txt'
                    file_language = language_map.get(file_extension, 'text')
                    file_types_found.add(file_language)

                    # Implement language filter if provided
                    if language and language.lower() != file_language.lower():
                        continue

                    # Perform a case-insensitive search for matches.
                    lines = content.split('\n')
                    for line_num, line in enumerate(lines, 1):
                        if query.lower() in line.lower():
                            # Identify the precise location and associated context.
                            match_start = line.lower().find(query.lower())
                            matched_text = line[match_start:match_start + len(query)]

                            # Retrieve the preceding and succeeding context.
                            context_before = ""
                            context_after = ""
                            if line_num > 1:
                                context_before = lines[line_num - 2].strip()
                            if line_num < len(lines):
                                context_after = lines[line_num].strip() if line_num < len(lines) else ""

                            # Compute relevance score using various parameters.
                            score = 1.0
                            if query.lower() in file_path.lower():
                                score += 0.5  # Filename matching incentive
                            if line.strip().startswith(query):
                                score += 0.3  # Beginning of line reward
                            if file_language in ['python', 'javascript', 'java']:
                                score += 0.2  # Widely-used language incentive

                            match = {
                                "repository": repo_name,
                                "path": file_path,
                                "filename": file_path.split('/')[-1],
                                "language": file_language,
                                "score": round(score, 2),
                                "excerpt": line.strip(),
                                "line_number": line_num,
                                "matched_text": matched_text,
                                "context_before": context_before,
                                "context_after": context_after,
                                "sha": f"file_{hash(content) % 1000000:06d}"
                            }
                            all_matches.append(match)
                            repo_matches += 1

            # Refresh repository metrics
            if repo_matches > 0:
                by_repository[repo_name] = repo_matches

        # Revise language metrics.
        for match in all_matches:
            lang = match["language"]
            by_language[lang] = by_language.get(lang, 0) + 1

        # Order matches based on score in descending order.
        all_matches.sort(key=lambda x: x["score"], reverse=True)

        # Implement pagination.
        total_matches = len(all_matches)
        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        paginated_matches = all_matches[start_idx:end_idx]

        # Determine the duration of the search process.
        search_time_ms = int((time.time() - start_time) * 1000)

        # Create suggestions for related queries.
        related_queries = []
        if query.lower() in ['function', 'def', 'class']:
            related_queries = [f"{query} name", f"{query} definition", f"public {query}"]
        elif len(query.split()) == 1:
            related_queries = [f"{query} implementation", f"{query} usage", f"import {query}"]
        else:
            words = query.split()
            if len(words) > 1:
                related_queries = [words[0], words[-1], " ".join(words[:-1])]

        # Filtered data details
        filters_applied = {
            "language": language,
            "repository": repo_filter,
            "case_sensitive": False
        }

        result = {
            "success": True,
            "data": {
                "matches": paginated_matches
            },
            "metadata": {
                "query": query,
                "total_results": total_matches,
                "search_time_ms": search_time_ms,
                "filters_applied": filters_applied,
                "pagination": {
                    "page": page,
                    "per_page": per_page,
                    "has_more": end_idx < total_matches
                }
            },
            "relationships": {
                "repositories_searched": repositories_searched,
                "file_types_found": list(file_types_found),
                "related_queries": related_queries[:3]  # Restrict to three recommendations.
            },
            "counts": {
                "total_matches": total_matches,
                "repositories_with_matches": len(by_repository),
                "unique_files": len(set(match["path"] for match in all_matches)),
                "by_language": by_language,
                "by_repository": by_repository
            }
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_code",
                "description": "Search code patterns with comprehensive results including relevance scoring, language filtering, context extraction, and detailed statistics with pagination support.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Code search query"},
                        "language": {"type": "string", "description": "Filter by programming language (optional)"},
                        "repo_filter": {"type": "string", "description": "Filter by repository name pattern (optional)"},
                        "page": {"type": "integer", "description": "Page number for pagination (defaults to 1)", "default": 1},
                        "per_page": {"type": "integer", "description": "Results per page (defaults to 30)", "default": 30}
                    },
                    "required": ["query"]
                }
            }
        }
