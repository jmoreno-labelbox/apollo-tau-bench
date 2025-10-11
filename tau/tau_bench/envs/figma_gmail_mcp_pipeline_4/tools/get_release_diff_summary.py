# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReleaseDiffSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], change_type, component_filter, diff_id, release_id, include_changelog = True) -> str:
        """
        Retrieves release diff information and change summaries between releases.
        """

        release_diffs = data.get('release_diffs', [])
        releases = data.get('releases', [])

        # Return the specified diff if diff_id is given.
        if diff_id:
            diff_info = None
            for diff in release_diffs:
                if diff.get('diff_id') == diff_id:
                    diff_info = diff
                    break

            if not diff_info:
                return json.dumps({"error": f"Release diff with ID '{diff_id}' not found."})

            # Enhance with version details.
            release_info = None
            for release in releases:
                if release.get('release_id') == diff_info.get('release_id'):
                    release_info = release
                    break

            summary = {
                "diff_info": diff_info,
                "release_info": release_info,
                "change_summary": {
                    "frames_added": len(diff_info.get('frames_added', [])),
                    "frames_updated": len(diff_info.get('frames_updated', [])),
                    "frames_removed": len(diff_info.get('frames_removed', [])),
                    "component_versions": len(diff_info.get('component_version_bumps', []))
                }
            }

            return json.dumps(summary, indent=2)

        # Apply criteria to filter differences.
        results = []
        for diff in release_diffs:
            # Implement filters
            if release_id:
                if diff.get('release_id') != release_id:
                    continue

            if component_filter:
                components = diff.get('component_version_bumps', [])
                if not any(component_filter.lower() in comp.lower() for comp in components):
                    continue

            if change_type:
                if change_type == 'added' and not diff.get('frames_added', []):
                    continue
                elif change_type == 'updated' and not diff.get('frames_updated', []):
                    continue
                elif change_type == 'removed' and not diff.get('frames_removed', []):
                    continue

            # Enhance with a summary of modifications.
            diff_copy = diff.copy()
            diff_copy['change_summary'] = {
                "frames_added": len(diff.get('frames_added', [])),
                "frames_updated": len(diff.get('frames_updated', [])),
                "frames_removed": len(diff.get('frames_removed', [])),
                "component_versions": len(diff.get('component_version_bumps', []))
            }

            if not include_changelog:
                diff_copy.pop('changelog_highlights', None)

            results.append(diff_copy)

        summary = {
            "total_diffs": len(results),
            "aggregate_changes": {
                "total_frames_added": sum(len(d.get('frames_added', [])) for d in results),
                "total_frames_updated": sum(len(d.get('frames_updated', [])) for d in results),
                "total_frames_removed": sum(len(d.get('frames_removed', [])) for d in results),
                "total_component_bumps": sum(len(d.get('component_version_bumps', [])) for d in results)
            },
            "diffs": results
        }

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_release_diff_summary",
                "description": "Retrieves release diff information and change summaries between releases including frame changes, component updates, and changelog highlights.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "diff_id": {"type": "string", "description": "The ID of a specific release diff to retrieve."},
                        "release_id": {"type": "string", "description": "Filter diffs by associated release ID."},
                        "component_filter": {"type": "string", "description": "Filter diffs by component name pattern (e.g., 'Button' to find button-related changes)."},
                        "change_type": {"type": "string", "description": "Filter diffs by change type ('added', 'updated', or 'removed')."},
                        "include_changelog": {"type": "boolean", "description": "Include changelog highlights in the results (default: true)."}
                    }
                }
            }
        }
