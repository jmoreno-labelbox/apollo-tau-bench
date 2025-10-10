from typing import Any, Dict, List, Optional
import json
from domains.dto import Tool
FIXED_TS = '2025-01-27T10:00:00Z'

def _ok(payload: Dict[str, Any]) -> str:
    return json.dumps({'ok': True, **payload}, indent=2)

def _err(msg: str) -> str:
    return json.dumps({'ok': False, 'error': msg}, indent=2)

def _table(db: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return db.get(name, [])

def _loc_table(db: Dict[str, Any]) -> List[Dict[str, Any]]:
    return db.get('loc_strings') or db.get('loc_strongs') or []

class GetLocString(Tool):
    """Fetch a localization string row by string_key; optionally include a locale entry."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        string_key = kwargs.get('string_key')
        locale = kwargs.get('locale')
        rows = _loc_table(data)
        for row in rows:
            if row.get('string_key') == string_key:
                if locale:
                    entry = (row.get('translations') or {}).get(locale)
                    return json.dumps({'loc_string': row, 'locale_entry': entry}, indent=2)
                return json.dumps({'loc_string': row}, indent=2)
        return _err(f'string_key not found: {string_key}')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_loc_string', 'description': 'Fetch a loc string by string_key (optionally include a single-locale view).', 'parameters': {'type': 'object', 'properties': {'string_key': {'type': 'string'}, 'locale': {'type': 'string'}}, 'required': ['string_key']}}}

class CreateTmsJob(Tool):
    """Create a minimal TMS job entry (deterministic; error on duplicate id)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        jobs = _table(data, 'tms_jobs')
        jid = kwargs.get('id')
        if not jid:
            jid = f"tms_job_{len(jobs) + 1:04d}"
        
        if any((j.get('id') == jid for j in jobs)):
            return _err(f'TMS job id {jid} already exists')
        job = {'id': jid, 'tms_project_id': kwargs.get('tms_project_id', 'proj_001'), 'job_name': kwargs.get('job_name', f'tms_job_{jid}'), 'job_type': kwargs.get('job_type', 'translation'), 'status': 'queued', 'created_at': kwargs.get('created_at', FIXED_TS), 'started_at': None, 'completed_at': None, 'total_segments': kwargs.get('total_segments', 0), 'completed_segments': 0, 'assigned_translators': kwargs.get('assigned_translators', []), 'assigned_reviewers': kwargs.get('assigned_reviewers', []), 'source_locale': kwargs.get('source_locale', 'en'), 'target_locales': kwargs.get('target_locales', []), 'priority': kwargs.get('priority', 'medium'), 'due_date': kwargs.get('due_date'), 'metadata': kwargs.get('metadata', {})}
        jobs.append(job)
        return _ok({'tms_job': job})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'create_tms_job', 'description': 'Create a queued TMS job with deterministic fields.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'tms_project_id': {'type': 'string'}, 'job_name': {'type': 'string'}, 'job_type': {'type': 'string'}, 'source_locale': {'type': 'string'}, 'target_locales': {'type': 'array', 'items': {'type': 'string'}}, 'priority': {'type': 'string'}, 'due_date': {'type': 'string'}, 'total_segments': {'type': 'integer'}, 'assigned_translators': {'type': 'array', 'items': {'type': 'string'}}, 'assigned_reviewers': {'type': 'array', 'items': {'type': 'string'}}, 'metadata': {'type': 'object'}}, 'required': ['source_locale', 'target_locales']}}}

class RecordTranslations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        entries = kwargs.get('entries', [])
        reflect = bool(kwargs.get('reflect_in_loc', True))
        translations = _table(data, 'translations')
        loc_rows = _loc_table(data)
        ALLOWED = {'loc_string_id', 'string_key', 'locale', 'target_string', 'metadata'}

        added = 0
        for e_in in entries:
            e = {k: v for k, v in e_in.items() if k in ALLOWED}
            eid = f"translation_{len(translations) + 1:04d}"
            e['id'] = eid
            if any(t.get('id') == eid for t in translations):
                continue

            translations.append(e)
            added += 1

            if reflect:
                lsid = e.get('loc_string_id')
                skey = e.get('string_key')
                locale = e.get('locale')
                target = e.get('target_string')
                for row in loc_rows:
                    if (lsid and row.get('id') == lsid) or (skey and row.get('string_key') == skey):
                        row.setdefault('translations', {})
                        loc_entry = row['translations'].setdefault(locale, {})
                        loc_entry['translation'] = target
                        loc_entry['status'] = loc_entry.get('status', 'translated')
                        loc_entry['validation_status'] = loc_entry.get('validation_status', 'pending')
                        if e.get('metadata') is not None:
                            loc_entry['metadata'] = e['metadata']
                        break
        return _ok({'added_count': added})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'record_translations',
                'description': 'Append translation entries and (optionally) reflect into loc_strings. Mirrors per-entry metadata when provided.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'entries': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'loc_string_id': {'type': 'string'},
                                    'string_key': {'type': 'string'},
                                    'locale': {'type': 'string'},
                                    'target_string': {'type': 'string'},
                                    'metadata': {'type': 'object'}
                                },
                                'required': ['locale', 'target_string']
                            }
                        },
                        'reflect_in_loc': {'type': 'boolean'}
                    },
                    'required': ['entries']
                }
            }
        }

class UpdateLocaleValidation(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        loc_string_id = kwargs.get('loc_string_id')
        string_key = kwargs.get('string_key')
        locale = kwargs.get('locale')
        new_status = kwargs.get('validation_status')
        validation_error = kwargs.get('validation_error')
        metadata = kwargs.get('metadata')
        loc_rows = _loc_table(data)
        target_row: Optional[Dict[str, Any]] = None
        for row in loc_rows:
            if loc_string_id and row.get('id') == loc_string_id or (string_key and row.get('string_key') == string_key):
                target_row = row
                break
        if not target_row:
            return _err('loc string not found')
        target_row.setdefault('translations', {})
        entry = target_row['translations'].setdefault(locale, {})
        if new_status is not None:
            entry['validation_status'] = new_status
        if validation_error is not None:
            entry['validation_error'] = validation_error
        if metadata is not None:
            entry['metadata'] = metadata
        return _ok({'updated': {'string_key': target_row.get('string_key'), 'locale': locale, 'validation_status': new_status, 'validation_error': validation_error}})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'update_locale_validation', 'description': 'Update locale validation and mirror into translations. Optionally attach CI/linkage metadata.', 'parameters': {'type': 'object', 'properties': {'loc_string_id': {'type': 'string'}, 'string_key': {'type': 'string'}, 'locale': {'type': 'string'}, 'validation_status': {'type': 'string'}, 'validation_error': {'type': 'string'}, 'metadata': {'type': 'object'}}, 'required': ['locale']}}}

class LinkWorkItems(Tool):
    """Create or confirm a link {parent_id, child_id, link_type} (idempotent)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        parent_id = kwargs.get('parent_id')
        child_id = kwargs.get('child_id')
        link_type = kwargs.get('link_type', 'relates_to')
        if not parent_id or not child_id:
            return _err('parent_id and child_id are required')
        if parent_id == child_id:
            return _err('cannot link an item to itself')
        links = _table(data, 'work_item_links')
        for l in links:
            if l.get('parent_id') == parent_id and l.get('child_id') == child_id and (l.get('link_type') == link_type):
                return _ok({'message': 'link already exists', 'parent_id': parent_id, 'child_id': child_id, 'link_type': link_type})
        links.append({'parent_id': parent_id, 'child_id': child_id, 'link_type': link_type})
        return _ok({'created_link': {'parent_id': parent_id, 'child_id': child_id, 'link_type': link_type}})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'link_work_items', 'description': 'Link two work items (parent/child/link_type).', 'parameters': {'type': 'object', 'properties': {'parent_id': {'type': 'string'}, 'child_id': {'type': 'string'}, 'link_type': {'type': 'string'}}, 'required': ['parent_id', 'child_id']}}}

class TagWorkItemWithLabel(Tool):
    """Attach a label to a work item; create label by name if needed (deterministic ids)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        work_item_id = kwargs.get('work_item_id')
        label_id = kwargs.get('label_id')
        label_name = kwargs.get('label_name')
        labels = _table(data, 'labels')
        wils = _table(data, 'work_item_labels')
        if not label_id:
            if not label_name:
                return _err('either label_id or label_name must be provided')
            found = next((l for l in labels if l.get('name') == label_name), None)
            if found:
                label_id = found.get('id')
            else:
                label_id = f'label_{len(labels) + 1:03d}'
                labels.append({'id': label_id, 'project_id': 'project_001', 'name': label_name, 'color': '#000000'})
        for m in wils:
            if m.get('work_item_id') == work_item_id and m.get('label_id') == label_id:
                return _ok({'message': 'label already attached', 'work_item_id': work_item_id, 'label_id': label_id})
        wils.append({'work_item_id': work_item_id, 'label_id': label_id})
        return _ok({'tagged': {'work_item_id': work_item_id, 'label_id': label_id}})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'tag_work_item_with_label', 'description': 'Attach a label to a work item (idempotent).', 'parameters': {'type': 'object', 'properties': {'work_item_id': {'type': 'string'}, 'label_id': {'type': 'string'}, 'label_name': {'type': 'string'}}, 'required': ['work_item_id']}}}

class SendNotification(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        notifications = _table(data, 'notifications')
        nid = kwargs.get('id')
        # --- FIX: Generate ID if not provided ---
        if not nid:
            nid = f"notification_{len(notifications) + 1:04d}"

        if any((n.get('id') == nid for n in notifications)):
            return _err(f'notification id {nid} already exists')
        record = {'id': nid, 'project_id': kwargs.get('project_id', 'project_001'), 'notification_type': kwargs.get('notification_type', 'info'), 'title': kwargs.get('title', ''), 'message': kwargs.get('message', ''), 'recipient_id': kwargs.get('recipient_id', 'user_000'), 'channel': kwargs.get('channel', 'slack'), 'sent_at': kwargs.get('sent_at', FIXED_TS), 'read_at': kwargs.get('read_at')}
        if not record['message']:
            return _err('message must be non-empty')
        md = kwargs.get('metadata')
        if md is not None:
            record['metadata'] = md
        notifications.append(record)
        return _ok({'notification': record})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'send_notification', 'description': 'Record a notification (deterministic timestamp). Optionally include CI/linkage metadata.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'project_id': {'type': 'string'}, 'notification_type': {'type': 'string'}, 'title': {'type': 'string'}, 'message': {'type': 'string'}, 'recipient_id': {'type': 'string'}, 'channel': {'type': 'string'}, 'sent_at': {'type': 'string'}, 'read_at': {'type': 'string'}, 'metadata': {'type': 'object'}}, 'required': ['message']}}}

class UpdateSubtitleTiming(Tool):
    """Update subtitle_timing row fields (e.g., subtitle_start/end/text) with basic guards."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sub_id = kwargs.get('id')
        updates: Dict[str, Any] = kwargs.get('updates', {})
        table = _table(data, 'subtitle_timing')
        row = next((r for r in table if r.get('id') == sub_id), None)
        if not row:
            return _err(f'subtitle_timing id not found: {sub_id}')
        if 'subtitle_start' in updates and 'subtitle_end' in updates:
            s, e = (updates['subtitle_start'], updates['subtitle_end'])
            if not (isinstance(s, (int, float)) and isinstance(e, (int, float))):
                return _err('subtitle_start/subtitle_end must be numeric')
            if not 0 <= s < e:
                return _err('subtitle_start must be >= 0 and < subtitle_end')
        row.update(updates)
        return _ok({'updated_subtitle': {'id': sub_id, 'applied_updates': updates}})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'update_subtitle_timing', 'description': 'Update a subtitle_timing record with basic timing guards.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'updates': {'type': 'object'}}, 'required': ['id', 'updates']}}}

class CreateLocalizationWorkflow(Tool):
    """Create a localization_workflow record (deterministic; error on duplicate id)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        table = _table(data, 'localization_workflow')
        wid = kwargs.get('id')
        # --- FIX: Generate ID if not provided ---
        if not wid:
            wid = f"loc_workflow_{len(table) + 1:04d}"

        if any((w.get('id') == wid for w in table)):
            return _err(f'localization_workflow id {wid} already exists')
        record = {'id': wid, 'pr_number': kwargs.get('pr_number'), 'changed_keys': kwargs.get('changed_keys', []), 'locales_processed': kwargs.get('locales_processed', []), 'bundle_uris': kwargs.get('bundle_uris', {}), 'overflow_issues': kwargs.get('overflow_issues', 0), 'tms_job_id': kwargs.get('tms_job_id'), 'status': kwargs.get('status', 'queued'), 'timestamp': kwargs.get('timestamp', FIXED_TS), 'metadata': kwargs.get('metadata', {})}
        table.append(record)
        return _ok({'localization_workflow': record})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'create_localization_workflow', 'description': 'Create a localization_workflow record (deterministic fields).', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'pr_number': {'type': 'integer'}, 'changed_keys': {'type': 'array', 'items': {'type': 'string'}}, 'locales_processed': {'type': 'array', 'items': {'type': 'string'}}, 'bundle_uris': {'type': 'object'}, 'overflow_issues': {'type': 'integer'}, 'tms_job_id': {'type': 'string'}, 'status': {'type': 'string'}, 'timestamp': {'type': 'string'}, 'metadata': {'type': 'object'}}, 'required': ['pr_number', 'changed_keys']}}}

class GetBuildRun(Tool):
    """Fetch a build run by id; optionally filter by commit_sha."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rid = kwargs.get('id')
        commit = kwargs.get('commit_sha')
        rows = _table(data, 'build_runs')
        row = next((r for r in rows if rid and r.get('id') == rid or (commit and r.get('commit_sha') == commit)), None)
        return _ok({'build_run': row}) if row else _err('build_run not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_build_run', 'description': 'Fetch a build run by id (or commit_sha).', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'commit_sha': {'type': 'string'}}, 'required': []}}}

class GetSourceChange(Tool):
    """Fetch a source change by commit_sha or id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get('id')
        sha = kwargs.get('commit_sha')
        rows = _table(data, 'source_changes')
        row = next((r for r in rows if cid and r.get('id') == cid or (sha and r.get('commit_sha') == sha)), None)
        return _ok({'source_change': row}) if row else _err('source_change not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_source_change', 'description': 'Fetch a source change by commit_sha (or id).', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'commit_sha': {'type': 'string'}}, 'required': []}}}

class GetTestResult(Tool):
    """Fetch a test result by id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tid = kwargs.get('id')
        rows = _table(data, 'test_results')
        row = next((r for r in rows if r.get('id') == tid), None)
        return _ok({'test_result': row}) if row else _err('test_result not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_test_result', 'description': 'Fetch a test result by id.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}}, 'required': ['id']}}}

class GetAutomationRun(Tool):
    """Fetch an automation run by id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get('id')
        rows = _table(data, 'automation_runs')
        row = next((r for r in rows if r.get('id') == aid), None)
        return _ok({'automation_run': row}) if row else _err('automation_run not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_automation_run', 'description': 'Fetch an automation run by id.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}}, 'required': ['id']}}}

class GetOwnershipForPath(Tool):
    """Fetch ownership entry for a given file_path."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        path = kwargs.get('file_path')
        rows = _table(data, 'ownership_map')
        row = next((r for r in rows if r.get('file_path') == path), None)
        return _ok({'ownership': row}) if row else _err('ownership not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_ownership_for_path', 'description': 'Fetch ownership record by file_path.', 'parameters': {'type': 'object', 'properties': {'file_path': {'type': 'string'}}, 'required': ['file_path']}}}

class GetAsset(Tool):
    """Fetch an asset by asset_path or id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get('id')
        apath = kwargs.get('asset_path')
        rows = _table(data, 'asset_catalog')
        row = next((r for r in rows if aid and r.get('id') == aid or (apath and r.get('asset_path') == apath)), None)
        return _ok({'asset': row}) if row else _err('asset not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_asset', 'description': 'Fetch an asset by asset_path (or id).', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'asset_path': {'type': 'string'}}, 'required': []}}}

class GetTmsJob(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        jid = kwargs.get('id')
        rows = _table(data, 'tms_jobs')
        row = next((r for r in rows if r.get('id') == jid), None)
        return _ok({'tms_job': row}) if row else _err('tms_job not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_tms_job', 'description': 'Fetch TMS job by id.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}}, 'required': ['id']}}}

class GetLocalizationWorkflow(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        wid = kwargs.get('id')
        rows = _table(data, 'localization_workflow')
        row = next((r for r in rows if r.get('id') == wid), None)
        return _ok({'localization_workflow': row}) if row else _err('localization_workflow not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_localization_workflow', 'description': 'Fetch localization_workflow by id.', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}}, 'required': ['id']}}}
TOOLS = [
    GetLocString(),
    CreateTmsJob(),
    RecordTranslations(),
    UpdateLocaleValidation(),
    LinkWorkItems(),
    TagWorkItemWithLabel(),
    SendNotification(),
    UpdateSubtitleTiming(),
    CreateLocalizationWorkflow(),
    GetBuildRun(),
    GetSourceChange(),
    GetTestResult(),
    GetAutomationRun(),
    GetOwnershipForPath(),
    GetAsset(),
    GetTmsJob(),
    GetLocalizationWorkflow(),
]