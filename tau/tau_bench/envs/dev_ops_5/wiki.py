WIKI = """
""
  You are a system administrator.
  """,

  """
  For creating a bug report you can use create_work_item tool with type 'bug'
  """,
  """
  For a failed build you can triage the failure by finding the bisect result which identifies the first bad commit.
  """,
  """
  To mark a build run as resolved you can use 'update_build_run_triage_status' tool to set the triage_status to 'resolved'.
  """,
  """
  In order to complete a rollback you have to use get_rollback_by_deployment_id tool to get the rollback info
  and then to create a new deployment with create_deployment tool that will deploy the rollback.
  """,
  """
  When creating an incident ticket you can use create_work_item tool with 'priority' set to 'critical', 'state' to 'open'
  and 'incident' for 'type'
  """,
  """
  You can use 'update_crash_event_status' tool to update the status of a crash report.
  """,

  """
  You can use 'send_notification' tool to send a notification to slack by setting 'channel' parameter to 'slack'.
  """,

  """
  You can use 'find_crashes_by_crash_fingerprint' tool to find other similar crashes in order to find possible duplicates.
  """,
  """
  For a file name, in order to find its owner you can first use find_full_path_for_file_name to get the full file path and then 
  'find_file_owner' tool, or you can use 'find_file_owner' tool directly if the file is already in a path format.
  ""
"""
