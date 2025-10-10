# Copyright Sierra


def _loc_table(data, table_name):
    """Get table from data as a list."""
    table = data.get(table_name, {})
    if isinstance(table, dict):
        return list(table.values())
    return table


from .get_loc_string import GetLocString
from .create_tms_job import CreateTmsJob
from .record_translations import RecordTranslations
from .update_locale_validation import UpdateLocaleValidation
from .link_work_items import LinkWorkItems
from .tag_work_item_with_label import TagWorkItemWithLabel
from .send_notification import SendNotification
from .update_subtitle_timing import UpdateSubtitleTiming
from .create_localization_workflow import CreateLocalizationWorkflow
from .get_build_run import GetBuildRun
from .get_source_change import GetSourceChange
from .get_test_result import GetTestResult
from .get_automation_run import GetAutomationRun
from .get_ownership_for_path import GetOwnershipForPath
from .get_asset import GetAsset
from .get_tms_job import GetTmsJob
from .get_localization_workflow import GetLocalizationWorkflow

_table = {}  # Global table storage


ALL_TOOLS = [
    GetLocString,
    CreateTmsJob,
    RecordTranslations,
    UpdateLocaleValidation,
    LinkWorkItems,
    TagWorkItemWithLabel,
    SendNotification,
    UpdateSubtitleTiming,
    CreateLocalizationWorkflow,
    GetBuildRun,
    GetSourceChange,
    GetTestResult,
    GetAutomationRun,
    GetOwnershipForPath,
    GetAsset,
    GetTmsJob,
    GetLocalizationWorkflow,
]
