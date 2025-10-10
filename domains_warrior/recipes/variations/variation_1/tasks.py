from domains.dto import Task, Action

TASKS = [

Task(
  annotator="saaish2",
  user_id="task_001",
  instruction=(
    "You create a standalone grocery list for the Garcia Household (household_id=208) under user_id=108, not linked to any meal plan, aggregated from exactly these dinners: [431,432,433,434]. Success means one new grocery_lists row with items aggregated from those recipes and status 'initialized', plus one audit event recording list creation. Return the list's status string."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":208}),
    Action(name="get_user_by_id", kwargs={"user_id":108}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":208,"source_meal_plan_id":None,"created_by_user_id":108,"status_enum":"initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[431,432,433,434]"}),
    Action(name="get_grocery_list_details", kwargs={"list_id":8003}),
    Action(name="log_audit_event", kwargs={"household_id":208,"user_id":108,"entity_type":"grocery_list","entity_id":8003,"action_enum":"list_created","payload_json":"{\"source\":\"recipes\",\"count\":4}"}),
  ],
  outputs=[
    "initialized"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_002",
  instruction=(
    "You have to set up a 4-day Lunch plan for the Johnson Large Family (household_id 207) for 2025-09-08 through 2025-09-11 using exactly these peanut-free recipes in order: 409, 410, 411, 412. Attach the fixed child-friendly note “Child-friendly: mild seasoning; cut to bite-size; soft textures.” to each entry, and record an audit of the creation. Acceptance: one meal plan for household 207 with week_start_date 2025-09-08 has four entries on 2025-09-08 to 2025-09-11 in that order with the appended child-friendly notes, and an audit exists for the creation."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 207}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 409}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 410}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 411}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 412}),
    Action(name="get_user_by_id", kwargs={"user_id": 107}),
    Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2025-09-08", "created_by_user_id": 107}),
    Action(
      name="bulk_add_meal_plan_entries",
      kwargs={
        "meal_plan_id": 6003,
        "week_start_date": "2025-09-08",
        "selected_recipe_ids_json": "[409,410,411,412]"
      }
    ),
    Action(
      name="update_meal_plan_entry_notes",
      kwargs={
        "meal_plan_id": 6003,
        "notes_map": {
          "409": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
          "410": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
          "411": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
          "412": "Child-friendly: mild seasoning; cut to bite-size; soft textures."
        }
      }
    ),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 207,
        "user_id": 107,
        "entity_type": "meal_plans",
        "entity_id": 6003,
        "action_enum": "create",
        "payload_json": {"week_start_date": "2025-09-08"}
      }
    ),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_003",
  instruction=(
    "You are coordinating five peanut-free weeknight dinners for the Johnson Large Family (household_id=207) for the week starting 2025-09-01. "
    "Acceptance criteria: a single meal plan exists with Dinner entries [402, 404, 407, 408, 423]; one grocery list is created from those recipes with sections and pantry flags set; "
    "store_id=9001 availability issues are addressed with peanut-free in-store substitutions when deterministically possible; "
    "a single delivery order is scheduled for 2025-01-02T10:00:00Z–12:00:00Z using lowest-price in-stock items, the order status is 'placed' and the list status is 'ordered'; "
    "audits are logged for meal plan creation, list creation, substitutions applied (even if zero), order placement, and list status change. "
    "Return the new order_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 207}),
    Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2025-09-01", "created_by_user_id": 107}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[402,404,407,408,423]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 207, "created_by_user_id": 107, "source_meal_plan_id": 6003, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,404,407,408,423]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-01"}}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9001}),
    Action(
      name="propose_substitute_products",
      kwargs={
        "store_id": 9001,
        "flagged_items": [
          {"ingredient_id": 1002}, {"ingredient_id": 1004}, {"ingredient_id": 1008}, {"ingredient_id": 1009},
          {"ingredient_id": 1010}, {"ingredient_id": 1011}, {"ingredient_id": 1013}, {"ingredient_id": 1016},
          {"ingredient_id": 1017}, {"ingredient_id": 1018}, {"ingredient_id": 1019}, {"ingredient_id": 1020},
          {"ingredient_id": 1022}, {"ingredient_id": 1024}, {"ingredient_id": 1045}, {"ingredient_id": 1078}
        ],
        "require_peanut_free": True
      },
    ),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id": 8003, "substitutions": []}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "substitutions_applied", "payload_json": {"count": 0}}),
    Action(name="create_order_from_list", kwargs={"household_id": 207, "store_id": 9001, "list_id": 8003, "scheduled_slot_start_ts": "2025-01-02T10:00:00Z", "scheduled_slot_end_ts": "2025-01-02T12:00:00Z"}),
    Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9001}),
    Action(name="update_order_status", kwargs={"order_id": 10003, "new_status": "placed"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ordered"}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "orders", "entity_id": 10003, "action_enum": "placed", "payload_json": {"list_id": 8003, "store_id": 9001}}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "status_update", "payload_json": {"status_enum": "ordered"}})
  ],
  outputs=[
    "10003"
  ]
),


Task(
  annotator="saaish2",
  user_id="task_004",
  instruction=(
    "You are assembling a pantry-first four-dinner plan for the Patel Extended Family (household_id=205) for the week starting 2025-09-01 and prepping a ready-to-shop list. "
    "Acceptance criteria: the plan exists with Dinner entries [402, 404, 405, 425]; one grocery list is created from those recipes; sections and pantry flags are set; 30-day overlap flags are computed with anchor_date=2025-08-31; "
    "the grocery list status is 'ready' and audits are logged for plan creation, list creation, and status change. "
    "Return the created meal_plan_id and grocery_list_id (in that order)."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 205}),
    Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2025-09-01", "created_by_user_id": 105}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[402,404,405,425]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 205, "created_by_user_id": 105, "source_meal_plan_id": 6003, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,404,405,425]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 205, "anchor_date": "2025-08-31"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-01"}}),
    Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
    Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "status_update", "payload_json": {"status_enum": "ready"}})
  ],
  outputs=[
    "6003",
    "8003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_005",
  instruction=(
    "You will finalize Grocery List 8002 for the Alvarez Household by updating sections and flags and setting status to 'ready'. Use 2025-09-07 as the overlap anchor date and record an audit reflecting the status change. Acceptance: list 8002 has refreshed grocery sections, pantry-staple flags, 30-day overlap flags anchored to 2025-09-07, status 'ready', and an audit exists for the update."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 202}),
    Action(name="get_grocery_list_details", kwargs={"list_id": 8002}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8002}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8002}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8002, "household_id": 202, "anchor_date": "2025-09-07"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8002, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_lists", "entity_id": 8002, "action_enum": "update", "payload_json": {"status": "ready"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_006",
  instruction=(
    "You are executing a 7-dinner high-protein plan for the Kowalski Couple (household_id=206) for the week starting 2024-12-30 with delivery from FreshMart Online (store_id=9001). "
    "Acceptance criteria (single deterministic terminal state): "
    "1) Exactly one meal plan exists for that week with Dinner entries [402, 404, 405, 407, 408, 428, 429]. "
    "2) Exactly one grocery list exists for that plan; items are aggregated from those recipes; sections and pantry flags are set; 30-day overlap flags use anchor_date=2024-12-29; list status is 'ordered'. "
    "3) Exactly one order exists for that list at store_id=9001 with scheduled_slot_start_ts='2025-01-02T10:00:00Z' and scheduled_slot_end_ts='2025-01-02T12:00:00Z'; order status is 'placed'. "
    "4) Audit events exist for meal plan creation, grocery list creation, and order placement. "
    "Return the grocery_list_id and order_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 206}),
    Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2024-12-30", "created_by_user_id": 106}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2024-12-30", "selected_recipe_ids_json": "[402,404,405,407,408,428,429]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 206, "created_by_user_id": 106, "source_meal_plan_id": 6003, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,404,405,407,408,428,429]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 206, "anchor_date": "2024-12-29"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9001}),
    Action(
      name="propose_substitute_products",
      kwargs={
        "store_id": 9001,
        "flagged_items": [
          {"ingredient_id": 1002},
          {"ingredient_id": 1003}, {"ingredient_id": 1004}, {"ingredient_id": 1008}, {"ingredient_id": 1009},
          {"ingredient_id": 1010}, {"ingredient_id": 1011}, {"ingredient_id": 1013}, {"ingredient_id": 1016},
          {"ingredient_id": 1017}, {"ingredient_id": 1018}, {"ingredient_id": 1019}, {"ingredient_id": 1020},
          {"ingredient_id": 1021}, {"ingredient_id": 1022}, {"ingredient_id": 1024}, {"ingredient_id": 1045},
          {"ingredient_id": 1047}, {"ingredient_id": 1068}, {"ingredient_id": 1078}, {"ingredient_id": 1139}
        ],
        "require_peanut_free": False
      },
    ),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id": 8003, "substitutions": []}),
    Action(name="create_order_from_list", kwargs={"household_id": 206, "store_id": 9001, "list_id": 8003, "scheduled_slot_start_ts": "2025-01-02T10:00:00Z", "scheduled_slot_end_ts": "2025-01-02T12:00:00Z"}),
    Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9001}),
    Action(name="update_order_status", kwargs={"order_id": 10003, "new_status": "placed"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ordered"}),
    Action(name="log_audit_event", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2024-12-30"}}),
    Action(name="log_audit_event", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
    Action(name="log_audit_event", kwargs={"household_id": 206, "user_id": 106, "entity_type": "orders", "entity_id": 10003, "action_enum": "placed", "payload_json": {"list_id": 8003, "store_id": 9001}}),
  ],
  outputs=[
    "8003",
    "10003"
  ]
),


Task(
  annotator="saaish2",
  user_id="task_007",
  instruction=(
    "You are running a budget-minded 7-dinner plan for the Kim-Smith Family (household_id=209) for the week starting 2024-12-30 and using Budget Foods Express (store_id=9004). "
    "Acceptance criteria (single deterministic terminal state): "
    "1) Exactly one meal plan exists for that week with Dinner recipes [402, 404, 405, 407, 408, 423, 427]. "
    "2) Exactly one grocery list is linked to that plan; it reflects aggregation from those recipes; sections and pantry flags are set; 30-day overlap flags use anchor_date=2024-12-29; list status is 'ordered'. "
    "3) Exactly one order is linked to that list at store_id=9004 with scheduled_slot_start_ts='2025-01-02T10:00:00Z' and scheduled_slot_end_ts='2025-01-02T12:00:00Z'; its final status is 'delivered'. "
    "4) The audit log records: creation of the meal plan, creation of the grocery list, the list status change to 'ordered', and the order changing to 'placed' and then 'delivered'. "
    "Return the final order status."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 209}),
    Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2024-12-30", "created_by_user_id": 109}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2024-12-30", "selected_recipe_ids_json": "[402,404,405,407,408,423,427]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 209, "created_by_user_id": 109, "source_meal_plan_id": 6003, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,404,405,407,408,423,427]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2024-12-29"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9004}),
    Action(
      name="propose_substitute_products",
      kwargs={
        "store_id": 9004,
        "flagged_items": [
          {"ingredient_id": 1001}, {"ingredient_id": 1002}, {"ingredient_id": 1003}, {"ingredient_id": 1006},
          {"ingredient_id": 1008}, {"ingredient_id": 1009}, {"ingredient_id": 1010}, {"ingredient_id": 1011},
          {"ingredient_id": 1013}, {"ingredient_id": 1015}, {"ingredient_id": 1016}, {"ingredient_id": 1017},
          {"ingredient_id": 1018}, {"ingredient_id": 1019}, {"ingredient_id": 1020}, {"ingredient_id": 1021},
          {"ingredient_id": 1022}, {"ingredient_id": 1024}, {"ingredient_id": 1045}, {"ingredient_id": 1077},
          {"ingredient_id": 1078}, {"ingredient_id": 1109}
        ],
        "require_peanut_free": False
      },
    ),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id": 8003, "substitutions": []}),
    Action(name="create_order_from_list", kwargs={"household_id": 209, "store_id": 9004, "list_id": 8003, "scheduled_slot_start_ts": "2025-01-02T10:00:00Z", "scheduled_slot_end_ts": "2025-01-02T12:00:00Z"}),
    Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9004}),
    Action(name="update_order_status", kwargs={"order_id": 10003, "new_status": "placed"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ordered"}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "status_update", "payload_json": {"status_enum": "ordered"}}),
    Action(name="update_order_status", kwargs={"order_id": 10003, "new_status": "delivered"}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2024-12-30"}}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "orders", "entity_id": 10003, "action_enum": "placed", "payload_json": {"list_id": 8003, "store_id": 9004}}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "orders", "entity_id": 10003, "action_enum": "delivered", "payload_json": {"list_id": 8003, "store_id": 9004}})
  ],
  outputs=[
    "delivered"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_008",
  instruction=(
    "You finalize the existing grocery list 8002 for the Alvarez Household (household_id=202) under user_id=102, ensuring items have sections and pantry staples flagged, then set the list status to 'finalized' and record one audit event for finalization. Return the final status string."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":202}),
    Action(name="get_user_by_id", kwargs={"user_id":102}),
    Action(name="get_grocery_list_details", kwargs={"list_id":8002}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8002}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id":8002}),
    Action(name="set_grocery_list_status", kwargs={"list_id":8002,"status_enum":"finalized"}),
    Action(name="log_audit_event", kwargs={"household_id":202,"user_id":102,"entity_type":"grocery_list","entity_id":8002,"action_enum":"list_finalized","payload_json":{"list_id":8002}}),
  ],
  outputs=[
    "finalized"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_009",
  instruction=(
    "You prepare a fixed-menu weekend Dinner grocery list for the Johnson Large Family using recipes 402, 404, and 406, anchored to 2025-09-06 for 30-day overlap checks. Acceptance: a new grocery list for household 207 reflects only those recipes, overlaps are flagged using the anchor date, and the list is aggregated."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 207}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 207, "source_meal_plan_id": None, "created_by_user_id": 107, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,404,406]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 207, "anchor_date": "2025-09-06"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "aggregated"}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "aggregated", "payload_json": {"anchor_date": "2025-09-06", "recipe_ids": [402,404,406]}}),
  ],
  outputs=[]
),


Task(
  annotator="saaish2",
  user_id="task_010",
  instruction=(
    "You assemble a peanut-free work-lunch selection for the Kim-Smith Family that uses Lunch recipes with at least 18 g protein per serving and minimizes new non-staple ingredients (no more than two per recipe). Acceptance: a dedicated grocery list for household 209 is created and audited at creation; sections are populated; pantry staples and 30-day overlaps (anchored to 2025-09-01) are flagged; the list status is set to ready_to_order with a status-change audit."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 209}),
    Action(name="list_recipes_by_filters", kwargs={"filter_token": "F:Lunch:P18:PF1:EX"}),
    Action(name="minimize_new_ingredients", kwargs={"recipe_ids_json": "[409,441,443,445,446,447]", "max_new_ingredients_per_recipe": 2}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 209, "source_meal_plan_id": None, "created_by_user_id": 109, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[447]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2025-09-01"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "aggregated"}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "aggregated", "payload_json": {"policy": "sections+pantry+overlap"}}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready_to_order"}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "status_changed", "payload_json": {"to": "ready_to_order"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_011",
  instruction=(
    "You will create a 3-night Dinner plan for the Williams-Brown Family (household_id 204) for the week starting 2025-09-15 using recipes [425, 428, 431] in that order across the first three days. Record an audit for the meal plan creation. Acceptance: one meal plan exists for household 204 with week_start_date 2025-09-15 and three Dinner entries in the specified order; an audit exists for the meal plan creation. Return the created meal_plan_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 204}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 425}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 428}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 431}),
    Action(name="get_user_by_id", kwargs={"user_id": 104}),
    Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2025-09-15", "created_by_user_id": 104}),
    Action(
      name="bulk_add_meal_plan_entries",
      kwargs={
        "meal_plan_id": 6003,
        "week_start_date": "2025-09-15",
        "selected_recipe_ids_json": "[425,428,431]",
        "meal_type_enum": "Dinner"
      }
    ),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 204,
        "user_id": 104,
        "entity_type": "meal_plans",
        "entity_id": 6003,
        "action_enum": "create",
        "payload_json": {"week_start_date": "2025-09-15"}
      }
    ),
  ],
  outputs=[
    "6003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_012",
  instruction=(
    "You will plan two dinners for Chen Solo for the week starting 2025-09-01, targeting ≈700 kcal and ≈35 g protein per serving (use the standard ±15% nutrition window, enforcing a ≥30 g protein floor). Build the plan using the top two dinners by nutrition closeness to those targets, aggregate a grocery list from those two dinners, categorize sections, flag pantry staples and 30-day overlaps using 2025-08-30 as the anchor, set the list to 'ready', and record audits for meal plan creation and grocery list creation/finalization. Accept when the plan and list exist, the list is 'ready', and the audits are recorded."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 203}),
    Action(name="get_user_by_id", kwargs={"user_id": 103}),
    Action(name="build_recipe_filters", kwargs={"meal_type": "Dinner", "min_protein_g": 30, "peanut_free": False, "cuisines_exclude": []}),
    Action(name="list_recipes_by_filters", kwargs={"filter_token": "F:Dinner:P30:PF0:EX"}),
    Action(name="rank_recipes_for_targets", kwargs={"recipe_ids_json": "[402, 404, 407, 423, 425, 427, 435]", "target_calories": 700, "target_protein": 35, "needed_count": 2}),
    Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-01", "created_by_user_id": 103}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[407, 423]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 203, "source_meal_plan_id": 6003, "created_by_user_id": 103, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[407, 423]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 203, "anchor_date": "2025-08-30"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-01"}}),
    Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"source_meal_plan_id": 6003}}),
    Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "finalized", "payload_json": {"status": "ready"}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_013",
  instruction=(
    "You will deliver a one-dinner weekly plan for Thompson Retirement (week starting 2025-09-01) whose recipe satisfies ≈650 kcal and ≈30 g protein per serving under the standard ±15% window (protein floor ≥26 g). The result must include a consolidated grocery list marked ready and audit logs for the plan and list transitions. Accept when a valid dinner plan exists, the grocery list is ready, and the audits are present."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 210}),
    Action(name="get_user_by_id", kwargs={"user_id": 110}),
    Action(name="build_recipe_filters", kwargs={"meal_type": "Dinner", "min_protein_g": 26, "peanut_free": False, "cuisines_exclude": []}),
    Action(name="list_recipes_by_filters", kwargs={"filter_token": "F:Dinner:P26:PF0:EX"}),
    Action(name="rank_recipes_for_targets", kwargs={"recipe_ids_json": "[402, 404, 407, 423, 425, 427, 429, 434, 435]", "target_calories": 650, "target_protein": 30, "needed_count": 1}),
    Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2025-09-01", "created_by_user_id": 110}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[427]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 210, "source_meal_plan_id": 6003, "created_by_user_id": 110, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[427]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-01"}}),
    Action(name="log_audit_event", kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"source_meal_plan_id": 6003}}),
    Action(name="log_audit_event", kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "finalized", "payload_json": {"status": "ready"}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_014",
  instruction=(
    "You deliver a five-dinner plan for the Kowalski Couple (household_id=206) for the week starting 2025-09-08 under user_id=106. You choose the five dinners closest to member_id=316’s targets from among exactly these candidates: [401, 402, 405, 406, 407, 408, 431], tie-breaking by higher protein then lower prep time. You validate the selected recipes, create the plan, and log an audit event for plan creation. Return the new meal_plan_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 206}),
    Action(name="get_user_by_id", kwargs={"user_id": 106}),
    Action(name="get_member_targets", kwargs={"member_id": 316}),
    Action(
      name="rank_recipes_for_targets",
      kwargs={
        "recipe_ids_json": "[401,402,405,406,407,408,431]",
        "needed_count": 5,
        "target_calories": 2400,
        "target_protein": 140,
      },
    ),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 407}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 402}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 405}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 408}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 401}),
    Action(
      name="create_meal_plan",
      kwargs={"household_id": 206, "week_start_date": "2025-09-08", "created_by_user_id": 106},
    ),
    Action(
      name="bulk_add_meal_plan_entries",
      kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[407,402,405,408,401]"},
    ),
    Action(
      name="log_audit_event",
      kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "meal_plan_created"},
    ),
  ],
  outputs=["6003"],
),

Task(
  annotator="saaish2",
  user_id="task_015",
  instruction=(
    "You plan four peanut-free Dinners for Sarah Chen’s household (household_id 203) for the week of 2025-09-01, favoring recipes with ≤4 non-staple ingredients each and at least ~18g protein. Use targets 1800 kcal and 80g protein to choose recipes. Success = one new meal_plan for that week with exactly four Dinner entries, and one grocery_list linked to the plan whose items equal the aggregated ingredients of those entries with 30-day overlap flags computed and status='finalized'."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 203}),
    Action(name="build_recipe_filters", kwargs={"meal_type": "Dinner", "min_protein_g": 18, "peanut_free": True, "cuisines_exclude": []}),
    Action(name="list_recipes_by_filters", kwargs={"filter_token": "F:Dinner:P18:PF1:EX"}),

    Action(name="minimize_new_ingredients", kwargs={
      "recipe_ids_json": "[402, 404, 405, 407, 408, 423, 425, 427, 428, 429, 432, 433, 434, 435]",
      "max_new_ingredients_per_recipe": 4
    }),

    Action(name="rank_recipes_for_targets", kwargs={
      "recipe_ids_json": "[402, 404, 407, 408, 423, 425, 427, 429, 432, 433, 435]",
      "needed_count": 4,
      "target_calories": 1800,
      "target_protein": 80
    }),

    Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-01", "created_by_user_id": 103}),
    Action(name="log_audit_event", kwargs={
      "household_id": 203, "user_id": 103,
      "entity_type": "meal_plan", "entity_id": 6003,
      "action_enum": "created",
      "payload_json": {"week_start_date": "2025-09-01"}
    }),

    Action(name="bulk_add_meal_plan_entries", kwargs={
      "meal_plan_id": 6003,
      "week_start_date": "2025-09-01",
      "selected_recipe_ids_json": "[425, 407, 423, 435]"
    }),

    Action(name="create_empty_grocery_list", kwargs={"household_id": 203, "source_meal_plan_id": 6003, "created_by_user_id": 103, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={
      "household_id": 203, "user_id": 103,
      "entity_type": "grocery_list", "entity_id": 8003,
      "action_enum": "created",
      "payload_json": {"source_meal_plan_id": 6003, "status": "initialized"}
    }),

    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[425, 407, 423, 435]"}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 203}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "finalized"}),
    Action(name="log_audit_event", kwargs={
      "household_id": 203, "user_id": 103,
      "entity_type": "grocery_list", "entity_id": 8003,
      "action_enum": "finalized",
      "payload_json": {"source_meal_plan_id": 6003, "status": "finalized"}
    }),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_016",
  instruction=(
    "You assemble a two-Dinner weekend grocery list for the Kim-Smith Family (household_id 209) without creating a new plan, using peanut-free Dinner recipes capped to one per cuisine and providing at least 20g protein, optimized for Rachel Kim’s targets (2600 kcal, 120g protein). Success is exactly one new grocery_list for the household with items equal to the aggregated ingredients from two selected dinners, items categorized, pantry_staple flags set, 30-day overlap flags computed, and status='finalized'."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 209}),
    Action(name="build_recipe_filters", kwargs={"meal_type": "Dinner", "min_protein_g": 20, "peanut_free": True, "cuisines_exclude": []}),
    Action(name="list_recipes_by_filters", kwargs={"filter_token": "F:Dinner:P20:PF1:EX"}),
    Action(name="apply_cuisine_cap", kwargs={
      "recipe_ids_json": "[402, 404, 405, 407, 408, 423, 425, 427, 428, 429, 433, 434, 435]",
      "max_per_cuisine": 1
    }),
    Action(name="rank_recipes_for_targets", kwargs={
      "recipe_ids_json": "[402, 404, 405, 407, 408, 423, 427, 429, 434]",
      "needed_count": 2,
      "target_calories": 2600,
      "target_protein": 120
    }),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 209, "created_by_user_id": 109, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={
      "household_id": 209, "user_id": 109,
      "entity_type": "grocery_list", "entity_id": 8003,
      "action_enum": "created",
      "payload_json": {"status": "initialized"}
    }),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[407, 423]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 209}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "finalized"}),
    Action(name="log_audit_event", kwargs={
      "household_id": 209, "user_id": 109,
      "entity_type": "grocery_list", "entity_id": 8003,
      "action_enum": "finalized",
      "payload_json": {"status": "finalized"}
    }),
  ],
  outputs=[]
),


Task(
  annotator="saaish2",
  user_id="task_017",
  instruction=(
    "You prepare a standalone grocery list for the Kim-Smith Family (household_id=209) under user_id=109 from exactly these dinners: [405, 431]. Check availability at store_id=9007 and record in-store substitutions deterministically when available; do not place an order. Success includes logging an audit event for list creation and another after applying any substitutions."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":209}),
    Action(name="get_user_by_id", kwargs={"user_id":109}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":209,"source_meal_plan_id":None,"created_by_user_id":109,"status_enum":"initialized"}),
    Action(name="log_audit_event", kwargs={"household_id":209,"user_id":109,"entity_type":"grocery_list","entity_id":8003,"action_enum":"list_created"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[405,431]"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id":8003,"store_id":9007}),
    Action(
      name="propose_substitute_products",
      kwargs={
        "store_id":9007,
        "flagged_items":[
          {"item_id":8114,"ingredient_id":1003,"stock_status_enum":"out_of_catalog"},
          {"item_id":8115,"ingredient_id":1021,"stock_status_enum":"out_of_catalog"},
          {"item_id":8116,"ingredient_id":1006,"stock_status_enum":"out_of_catalog"},
          {"item_id":8117,"ingredient_id":1009,"stock_status_enum":"out_of_catalog"},
          {"item_id":8118,"ingredient_id":1010,"stock_status_enum":"out_of_catalog"},
          {"item_id":8119,"ingredient_id":1065,"stock_status_enum":"out_of_catalog"},
          {"item_id":8120,"ingredient_id":1066,"stock_status_enum":"out_of_catalog"},
          {"item_id":8121,"ingredient_id":1073,"stock_status_enum":"out_of_catalog"},
          {"item_id":8123,"ingredient_id":1015,"stock_status_enum":"out_of_catalog"},
          {"item_id":8124,"ingredient_id":1089,"stock_status_enum":"out_of_catalog"}
        ],
        "require_peanut_free":False
      }
    ),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id":8003,"substitutions":[]}),
    Action(name="log_audit_event", kwargs={"household_id":209,"user_id":109,"entity_type":"grocery_list","entity_id":8003,"action_enum":"substitutions_applied"})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_018",
  instruction=(
    "You will create a pantry-first restock list for the Patel Extended Family by aggregating ingredients from exactly these three Dinner recipes: 424, 426, 431. Categorize items by grocery section, and set pantry-staple and 30-day overlap flags using 2025-09-07 as the anchor. Keep the list initialized. Acceptance: one new grocery list exists with items aggregated from those three recipes; sections assigned; pantry and overlap flags set; no store checks or orders."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 205}),
    Action(name="get_user_by_id", kwargs={"user_id": 105}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 205, "source_meal_plan_id": None, "created_by_user_id": 105, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[424,426,431]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 205, "anchor_date": "2025-09-07"}),
    Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"source":"pantry_first","recipes":[424,426,431]}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_019",
  instruction=(
    "You place a single curbside order for the Alvarez Household (household_id=202) using the existing grocery list list_id=8002 at store_id=9004, scheduled for 2025-09-09T10:00:00Z–12:00:00Z. Success means there is one new order for that list and store with status 'placed' and order_items selected as the lowest-price in-stock products per policy. Log an audit event after substitutions are applied, after order creation, after items are added, and after marking the order placed. Also set the grocery list status to 'ordered' once items are finalized. Return the created order_id and final total_cents."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":202}),
    Action(name="get_grocery_list_details", kwargs={"list_id":8002}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id":8002,"store_id":9004}),
    Action(
      name="propose_substitute_products",
      kwargs={
        "store_id":9004,
        "flagged_items":[
          {"item_id":8111,"ingredient_id":1026,"stock_status_enum":"out_of_catalog"},
          {"item_id":8112,"ingredient_id":1039,"stock_status_enum":"out_of_catalog"},
          {"item_id":8113,"ingredient_id":1038,"stock_status_enum":"out_of_catalog"}
        ],
        "require_peanut_free":False
      }
    ),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id":8002,"substitutions":[]}),
    Action(name="log_audit_event", kwargs={"household_id":202,"user_id":102,"entity_type":"grocery_list","entity_id":8002,"action_enum":"substitutions_applied"}),
    Action(name="create_order_from_list", kwargs={"household_id":202,"store_id":9004,"list_id":8002,"scheduled_slot_start_ts":"2025-09-09T10:00:00Z","scheduled_slot_end_ts":"2025-09-09T12:00:00Z"}),
    Action(name="log_audit_event", kwargs={"household_id":202,"user_id":102,"entity_type":"order","entity_id":10003,"action_enum":"order_created"}),
    Action(name="add_order_items_from_list", kwargs={"order_id":10003,"store_id":9004}),
    Action(name="log_audit_event", kwargs={"household_id":202,"user_id":102,"entity_type":"order","entity_id":10003,"action_enum":"order_items_added"}),
    Action(name="set_grocery_list_status", kwargs={"list_id":8002,"status_enum":"ordered"}),
    Action(name="update_order_status", kwargs={"order_id":10003,"new_status":"placed"}),
    Action(name="log_audit_event", kwargs={"household_id":202,"user_id":102,"entity_type":"order","entity_id":10003,"action_enum":"order_placed"})
  ],
  outputs=[
    "10003",
    "0"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_020",
  instruction=(
    "You will deliver the following final state for the Garcia Household: a weekday Dinner grocery list derived strictly from recipe IDs 401, 402, 425, 427; the list is categorized by grocery section and has pantry-staple and 30-day overlap flags anchored to 2025-09-07; availability is aligned to GrocerDash (store_id 9002); a draft order exists for delivery window 2025-09-03T10:00:00Z–2025-09-03T12:00:00Z containing only the lowest-price in-stock products for items on that list; the order remains in draft. Acceptance: exactly one list and one draft order exist as described."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 208}),
    Action(name="get_user_by_id", kwargs={"user_id": 108}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 208, "source_meal_plan_id": None, "created_by_user_id": 108, "status_enum": "initialized"}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 208,
        "user_id": 108,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "created",
        "payload_json": {"source": "recipes", "recipes": [401, 402, 425, 427]}
      }
    ),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,402,425,427]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 208, "anchor_date": "2025-09-07"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(name="create_order_from_list", kwargs={"household_id": 208, "store_id": 9002, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-03T10:00:00Z", "scheduled_slot_end_ts": "2025-09-03T12:00:00Z"}),
    Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9002, "product_overrides": {}}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 208,
        "user_id": 108,
        "entity_type": "order",
        "entity_id": 10003,
        "action_enum": "created",
        "payload_json": {"list_id": 8003, "store_id": 9002, "status": "draft"}
      }
    )
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_021",
  instruction=(
    "You create a standalone grocery list for the household “Patel Extended Family” (household_id=205) under created_by_user_id=105, not linked to any meal plan, aggregated from exactly these recipes: [403, 412, 431]. Success means there is one new grocery_lists row for that household with status 'initialized' and items equal to the exact aggregation of those recipes, and a single audit event records list creation. Return the new list_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":205}),
    Action(name="get_user_by_id", kwargs={"user_id":105}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":205,"source_meal_plan_id":None,"created_by_user_id":105,"status_enum":"initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[403,412,431]"}),
    Action(name="log_audit_event", kwargs={"household_id":205,"user_id":105,"entity_type":"grocery_list","entity_id":8003,"action_enum":"list_created"})
  ],
  outputs=[
    "8003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_022",
  instruction=(
    "You will deliver a complete end state for the Kim-Smith Family’s 7-night Dinners for the week beginning 2025-09-15 using exactly these recipe IDs: 402, 423, 425, 427, 428, 434, 435. Every entry must use the single fixed child-note template. The linked grocery list must aggregate those dinners, be categorized, and include pantry-staple and 30-day overlap flags anchored to 2025-09-21. Availability must be aligned to FreshMart Online (store_id 9001). Apply these deterministic in-store substitutions if needed: 1002→1048 and 1009→1066. A draft order for 2025-09-18T09:00:00Z–2025-09-18T11:00:00Z must exist and contain only the lowest-price in-stock products per ingredient after substitutions; keep the order in draft. Acceptance: one Dinner meal plan with template notes; one linked list with sections/pantry/overlap; store 9001 availability checked; the two substitutions applied when relevant; one draft order created and populated; no placed_ts on draft."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 209}),
    Action(name="get_user_by_id", kwargs={"user_id": 109}),
    Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2025-09-15", "created_by_user_id": 109}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-15", "selected_recipe_ids_json": "[402,423,425,427,428,434,435]"}),
    Action(
      name="update_meal_plan_entry_notes",
      kwargs={
        "meal_plan_id": 6003,
        "notes_map": {
          "402": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
          "423": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
          "425": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
          "427": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
          "428": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
          "434": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
          "435": "Child-friendly: mild seasoning; cut to bite-size; soft textures."
        }
      }
    ),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 209, "source_meal_plan_id": 6003, "created_by_user_id": 109, "status_enum": "initialized"}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 209,
        "user_id": 109,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "created",
        "payload_json": {"source_meal_plan_id": 6003}
      }
    ),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,423,425,427,428,434,435]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2025-09-21"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9001}),
    Action(name="propose_substitute_products", kwargs={"store_id": 9001, "flagged_items": [{"ingredient_id": 1002}, {"ingredient_id": 1009}], "require_peanut_free": False}),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id": 8003, "substitutions": [{"ingredient_id": 1002, "substitute_ingredient_id": 1048}, {"ingredient_id": 1009, "substitute_ingredient_id": 1066}]}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9001}),
    Action(name="create_order_from_list", kwargs={"household_id": 209, "store_id": 9001, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-18T09:00:00Z", "scheduled_slot_end_ts": "2025-09-18T11:00:00Z"}),
    Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9001, "product_overrides": {}}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 209,
        "user_id": 109,
        "entity_type": "meal_plan",
        "entity_id": 6003,
        "action_enum": "created",
        "payload_json": {"week_start_date": "2025-09-15", "entries": 7}
      }
    ),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 209,
        "user_id": 109,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "updated",
        "payload_json": {
          "flags": ["sections", "pantry", "overlap"],
          "substitutions_applied": [{"from": 1002, "to": 1048}, {"from": 1009, "to": 1066}]
        }
      }
    ),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 209,
        "user_id": 109,
        "entity_type": "order",
        "entity_id": 10003,
        "action_enum": "created",
        "payload_json": {"store_id": 9001, "status": "draft"}
      }
    )
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_023",
  instruction=(
    "You plan a 2-night vegetarian dinner micro-plan for the household “Chen Solo” (household_id=203) for the week starting 2025-09-01, using exactly recipes 403 (Chickpea Curry) and 405 (Teriyaki Tofu Bowl). Create one new meal plan for that week under user_id=103 and insert exactly two Dinner entries mapped to those recipes with default servings and no free-text notes. Log a single audit event recording the creation. Return the created entry_id list for the new plan."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":203}),
    Action(name="get_user_by_id", kwargs={"user_id":103}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id":403}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id":405}),
    Action(name="create_meal_plan", kwargs={"household_id":203,"week_start_date":"2025-09-01","created_by_user_id":103}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-01","selected_recipe_ids_json":"[403,405]"}),
    Action(name="log_audit_event", kwargs={"household_id":203,"user_id":103,"entity_type":"meal_plans","entity_id":6003,"action_enum":"create_meal_plan","payload_json":{"week_start_date":"2025-09-01"}}),
  ],
  outputs=[6118, 6119]
),

Task(
  annotator="saaish2",
  user_id="task_024",
  instruction=(
    "You will deliver a Dessert grocery list for the Patel Extended Family (household_id 205) using exactly recipes [414, 415], validated against Organic Valley Co-op (store_id 9003), with a creation audit that names the store checked. Acceptance: one new list exists with items aggregated from those recipes; availability has been evaluated at store 9003; and the creation audit payload includes \"store_checked\": 9003. Return the creation audit_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 205}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 205, "created_by_user_id": 105, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[414,415]"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9003}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 205,
        "user_id": 105,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "created",
        "payload_json": {"status": "initialized", "store_checked": 9003},
      },
    ),
  ],
  outputs=[
    "12014"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_025",
  instruction=(
    "You set up a single-dinner plan for the household “Thompson Retirement” (household_id=210) for week starting 2025-09-15 with exactly recipe 408 (Lentil Soup), then derive a grocery list tied to that plan and flag 30-day overlap against recent meals using anchor_date=2025-08-20. Log one audit event for list generation. Return the new meal_plan_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":210}),
    Action(name="get_user_by_id", kwargs={"user_id":110}),
    Action(name="create_meal_plan", kwargs={"household_id":210,"week_start_date":"2025-09-15","created_by_user_id":110}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-15","selected_recipe_ids_json":"[408]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":210,"source_meal_plan_id":6003,"created_by_user_id":110,"status_enum":"initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[408]"}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id":8003,"household_id":210,"anchor_date":"2025-08-20"}),
    Action(name="log_audit_event", kwargs={"household_id":210,"user_id":110,"entity_type":"grocery_lists","entity_id":8003,"action_enum":"generate_list","payload_json":{"source_meal_plan_id":6003}}),
  ],
  outputs=[
    "6003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_026",
  instruction=(
    "You run a pantry-first dinner restock for the household “Kim-Smith Family” (household_id=209) for the week starting 2025-09-08. Success requires: one meal plan under user_id=109 containing exactly two dinners chosen from {401,402,403,404}; selection must minimize the summed absolute deviation from the adult target (member_id=327) in protein (primary criterion) with absolute calorie deviation as the tie-breaker and lower recipe_id as the final tie-breaker; each chosen recipe must introduce no more than three non-staple ingredients; a single grocery list derived exactly from those two dinners; availability and product choice at store_id=9001 using lowest-price items with stock_status in {in_stock, low} for the scheduled slot 2025-09-09T09:00:00Z–11:00:00Z; and one audit event recording order placement. Return the created order_id and final total_cents."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":209}),
    Action(name="get_user_by_id", kwargs={"user_id":109}),
    Action(name="get_member_targets", kwargs={"member_id":327}),
    Action(name="minimize_new_ingredients", kwargs={"recipe_ids_json":"[401,402,403,404]","max_new_ingredients_per_recipe":3}),
    Action(name="rank_recipes_for_targets", kwargs={"recipe_ids_json":"[401,404]","needed_count":2,"target_calories":2600,"target_protein":120}),
    Action(name="create_meal_plan", kwargs={"household_id":209,"week_start_date":"2025-09-08","created_by_user_id":109}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-08","selected_recipe_ids_json":"[404, 401]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":209,"source_meal_plan_id":6003,"created_by_user_id":109,"status_enum":"initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[404,401]"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id":8003,"store_id":9001}),
    Action(name="propose_substitute_products", kwargs={"list_id":8003,"store_id":9001}),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id":8003}),
    Action(name="create_order_from_list", kwargs={"household_id":209,"store_id":9001,"list_id":8003,"scheduled_slot_start_ts":"2025-09-09T09:00:00Z","scheduled_slot_end_ts":"2025-09-09T11:00:00Z"}),
    Action(name="add_order_items_from_list", kwargs={"order_id":10003,"store_id":9001}),
    Action(name="log_audit_event", kwargs={"household_id":209,"user_id":109,"entity_type":"orders","entity_id":10003,"action_enum":"place_order","payload_json":{"list_id":8003,"store_id":9001}}),
  ],
  outputs=[
    "10003",
    "1597"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_027",
  instruction=(
    "You will ensure Alvarez Household’s grocery list 8002 (household_id 202) is procurable at FreshMart Online (store_id 9001) by honoring store availability and applying in-store substitutions where available, and you will record an audit summarizing any changes. Acceptance: availability is evaluated for list 8002 at store 9001; when the store carries in-stock/low alternatives, appropriate substitutions are applied per policy; the list reflects any changes; and an audit payload summarizes the updated item count. Return the number of updated list items."
  ),
  actions=[
    Action(name="get_grocery_list_details", kwargs={"list_id": 8002}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8002, "store_id": 9001}),
    Action(name="propose_substitute_products", kwargs={
      "store_id": 9001,
      "flagged_items": [
        {"ingredient_id": 1026, "status": "out_of_catalog"},
        {"ingredient_id": 1039, "status": "out_of_catalog"},
        {"ingredient_id": 1038, "status": "out_of_catalog"}
      ],
      "require_peanut_free": False
    }),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id": 8002, "substitutions": []}),
    Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8002, "action_enum": "substitutions_applied", "payload_json": {"updated_items": 0}}),
  ],
  outputs=[
    "0"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_028",
  instruction=(
    "You deliver a 7-night family dinner plan for the household “Johnson Large Family” (household_id=207) for the week starting 2025-09-08. Success means a single plan under user_id=107 with exactly seven peanut-free dinners each providing at least 20 g protein and best aligned to the adult target (member_id=319); one grocery list derived from those same seven recipes; availability resolved at store_id=9001 with a single placed order for 2025-09-09T10:00:00Z–12:00:00Z selecting lowest-price items with stock_status in {in_stock, low} per policy; and one audit event recording order placement. Return the created order_id and final total_cents."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":207}),
    Action(name="get_user_by_id", kwargs={"user_id":107}),
    Action(name="get_member_targets", kwargs={"member_id":319}),
    Action(name="build_recipe_filters", kwargs={"meal_type":"Dinner","min_protein_g":20,"peanut_free":True,"cuisines_exclude":[]}),
    Action(name="list_recipes_by_filters", kwargs={"filter_token":"F:Dinner:P20:PF1:EX"}),
    Action(name="rank_recipes_for_targets", kwargs={"recipe_ids_json":"[402,404,405,407,408,423,425,427,428,429,433,434,435]","needed_count":7,"target_calories":2300,"target_protein":125}),
    Action(name="create_meal_plan", kwargs={"household_id":207,"week_start_date":"2025-09-08","created_by_user_id":107}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-08","selected_recipe_ids_json":"[425,407,423,435,404,427,402]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":207,"source_meal_plan_id":6003,"created_by_user_id":107,"status_enum":"initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[425,407,423,435,404,427,402]"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id":8003,"store_id":9001}),
    Action(name="propose_substitute_products", kwargs={"list_id":8003,"store_id":9001}),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id":8003}),
    Action(name="create_order_from_list", kwargs={"household_id":207,"store_id":9001,"list_id":8003,"scheduled_slot_start_ts":"2025-09-09T10:00:00Z","scheduled_slot_end_ts":"2025-09-09T12:00:00Z"}),
    Action(name="add_order_items_from_list", kwargs={"order_id":10003,"store_id":9001,"allowed_stock_statuses_json":"[\"in_stock\",\"low\"]"}),
    Action(name="log_audit_event", kwargs={"household_id":207,"user_id":107,"entity_type":"orders","entity_id":10003,"action_enum":"place_order","payload_json":{"list_id":8003,"store_id":9001}}),
  ],
  outputs=[
    "10003",
    "3195"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_029",
  instruction=(
    "You create a three-dinner plan and linked grocery list for Chen Solo (household_id 203) using exactly Dinner recipes 401, 402, and 404 for the week starting 2025-09-08. Acceptance: the meal plan exists for that week, an aggregated grocery list is linked to it with items categorized and pantry/30-day overlap flags set using 2025-09-07 as the anchor, and the list status is “ready”."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 203}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 401}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 402}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 404}),
    Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-08", "created_by_user_id": 103}),
    Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-08"}}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[401,402,404]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 203, "source_meal_plan_id": 6003, "created_by_user_id": 103, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,402,404]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 203, "anchor_date": "2025-09-07"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"source": "meal_plan", "meal_plan_id": 6003}}),
    Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"flags": ["pantry_staple","overlap_30d"], "categorized": True}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_030",
  instruction=(
    "You build a peanut-free school-lunch grocery list for the Alvarez Household (household_id 202) from exactly lunch recipes 409, 410, and 411. Acceptance: a single list exists, items are aggregated and categorized with pantry/30-day overlap flags set using 2025-09-07, store 9002 inventory is checked, and the list status is “inventory_checked”. Return the list_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 202}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 409}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 410}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 411}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 202, "source_meal_plan_id": None, "created_by_user_id": 102, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,411]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 202, "anchor_date": "2025-09-07"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "inventory_checked"}),
    Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "inventory_checked", "payload_json": {"store_id": 9002}}),
    Action(name="get_grocery_list_details", kwargs={"list_id": 8003})
  ],
  outputs=[
    "8003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_031",
  instruction=(
    "You prepare a dinner grocery list for the Johnson Large Family (household_id 207) using exactly recipes 424 and 433, then draft a single order from store 9004 for delivery on 2025-09-05T10:00:00Z–12:00:00Z. Acceptance: one list exists that is categorized and flagged using 2025-09-07; store 9004 inventory has been checked; any available in-store substitutes (if any) are applied; and a draft order exists for the slot with only available items."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 207}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 424}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 433}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 207, "source_meal_plan_id": None, "created_by_user_id": 107, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[424,433]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 207, "anchor_date": "2025-09-07"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9004}),
    Action(name="propose_substitute_products", kwargs={"list_id": 8003, "store_id": 9004, "require_peanut_free": False}),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id": 8003}),
    Action(name="create_order_from_list", kwargs={"household_id": 207, "store_id": 9004, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-05T10:00:00Z", "scheduled_slot_end_ts": "2025-09-05T12:00:00Z"}),
    Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9004}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"list_id": 8003, "store_id": 9004}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_032",
  instruction=(
    "You assemble a five-day peanut-free school-lunch pack for the Alvarez Household (household_id 202) aligned to the child’s targets (member_id 305) by selecting five Lunch recipes with ≥20 g protein under the platform’s deterministic rules. Acceptance: a dedicated list exists with those five lunches; items are categorized and flagged using 2025-09-07; store 9002 inventory is checked; any available in-store substitutes that meet peanut-free constraints are applied; and the list status is “ready”."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 202}),
    Action(name="get_member_targets", kwargs={"member_id": 305}),
    Action(name="build_recipe_filters", kwargs={"meal_type": "Lunch", "min_protein_g": 20, "peanut_free": True, "cuisines_exclude": []}),
    Action(name="list_recipes_by_filters", kwargs={"filter_token": "F:Lunch:P20:PF1:EX"}),
    Action(name="minimize_new_ingredients", kwargs={"recipe_ids_json": "[409,441,443,445,447]"}),
    Action(name="rank_recipes_for_targets", kwargs={"recipe_ids_json": "[409,441,443,445,447]", "needed_count": 5, "target_calories": 1600, "target_protein": 45}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 202, "source_meal_plan_id": None, "created_by_user_id": 102, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[445,443,409,447,441]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 202, "anchor_date": "2025-09-07"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(
      name="propose_substitute_products",
      kwargs={
        "list_id": 8003,
        "store_id": 9002,
        "require_peanut_free": True,
        "flagged_items": [
          {"ingredient_id": 1024},
          {"ingredient_id": 1013},
          {"ingredient_id": 1020},
          {"ingredient_id": 1109},
          {"ingredient_id": 1050},
          {"ingredient_id": 1069},
          {"ingredient_id": 1001},
          {"ingredient_id": 1089},
          {"ingredient_id": 1012}
        ]
      }
    ),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id": 8003}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"store_checked": 9002}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_033",
  instruction=(
    "You plan four weeknight dinners for the Kim-Smith Family (household_id 209) using exactly recipes 401, 404, 407, and 435 for the week starting 2025-09-08, and place one order at store 9004 for delivery on 2025-09-06T14:00:00Z–16:00:00Z. Acceptance: the plan exists with a linked grocery list categorized and flagged using 2025-09-07; store 9004 inventory is checked and any available in-store substitutes are applied; an order exists for that slot containing only available items and its status is “placed”. Return the created meal_plan_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 209}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 401}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 404}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 407}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id": 435}),
    Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2025-09-08", "created_by_user_id": 109}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-08"}}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[401,404,407,435]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 209, "source_meal_plan_id": 6003, "created_by_user_id": 109, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,404,407,435]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2025-09-07"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9004}),
    Action(name="propose_substitute_products", kwargs={"list_id": 8003, "store_id": 9004, "require_peanut_free": False}),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id": 8003}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "inventory_checked"}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "inventory_checked", "payload_json": {"store_id": 9004}}),
    Action(name="create_order_from_list", kwargs={"household_id": 209, "store_id": 9004, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-06T14:00:00Z", "scheduled_slot_end_ts": "2025-09-06T16:00:00Z"}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"list_id": 8003, "store_id": 9004}}),
    Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9004}),
    Action(name="update_order_status", kwargs={"order_id": 10003, "new_status": "placed"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ordered"}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "order", "entity_id": 10003, "action_enum": "placed", "payload_json": {"list_id": 8003, "store_id": 9004}}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ordered", "payload_json": {"order_id": 10003}})
  ],
  outputs=[
    "6003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_034",
  instruction=(
    "You create a seven-day dinner plan for the Garcia Household (household_id 208) for the week starting 2025-09-08 that honors a maximum of two dinners per cuisine and is chosen to be closest to the adult member’s targets (member_id 324) under the platform’s deterministic rules. Use delivery slot 2025-09-07T10:00:00Z–12:00:00Z. Acceptance: the plan exists; its linked grocery list is categorized and flagged using 2025-09-07; store 9001 inventory is checked and any available in-store substitutes are applied; and one order exists for that slot with only available items and status “placed”."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 208}),
    Action(name="get_member_targets", kwargs={"member_id": 324}),
    Action(name="build_recipe_filters", kwargs={"meal_type": "Dinner", "min_protein_g": 20, "peanut_free": False, "cuisines_exclude": []}),
    Action(name="list_recipes_by_filters", kwargs={"filter_token": "F:Dinner:P20:PF0:EX"}),
    Action(name="apply_cuisine_cap", kwargs={"recipe_ids_json": "[402,404,405,407,408,423,425,427,428,429,430,433,434,435]", "max_per_cuisine": 2}),
    Action(name="rank_recipes_for_targets", kwargs={"recipe_ids_json": "[402,404,405,407,408,423,425,427,429,430,434]", "needed_count": 7, "target_calories": 2400, "target_protein": 130}),
    Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2025-09-08", "created_by_user_id": 108}),
    Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-08"}}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[425,407,423,404,427,402,429]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 208, "source_meal_plan_id": 6003, "created_by_user_id": 108, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[425,407,423,404,427,402,429]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 208, "anchor_date": "2025-09-07"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9001}),
    Action(
      name="propose_substitute_products",
      kwargs={
        "list_id": 8003,
        "store_id": 9001,
        "require_peanut_free": False,
        "flagged_items": [
          {"ingredient_id": 1008},
          {"ingredient_id": 1019},
          {"ingredient_id": 1018},
          {"ingredient_id": 1013},
          {"ingredient_id": 1024},
          {"ingredient_id": 1002},
          {"ingredient_id": 1022},
          {"ingredient_id": 1016},
          {"ingredient_id": 1017},
          {"ingredient_id": 1009},
          {"ingredient_id": 1010},
          {"ingredient_id": 1020},
          {"ingredient_id": 1045},
          {"ingredient_id": 1078},
          {"ingredient_id": 1106},
          {"ingredient_id": 1107},
          {"ingredient_id": 1109},
          {"ingredient_id": 1077},
          {"ingredient_id": 1047},
          {"ingredient_id": 1068},
          {"ingredient_id": 1139}
        ]
      }
    ),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id": 8003}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"flags": ["pantry_staple","overlap_30d"], "categorized": True}}),
    Action(name="create_order_from_list", kwargs={"household_id": 208, "store_id": 9001, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-07T10:00:00Z", "scheduled_slot_end_ts": "2025-09-07T12:00:00Z"}),
    Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"list_id": 8003, "store_id": 9001, "slot": "2025-09-07T10:00:00Z/2025-09-07T12:00:00Z"}}),
    Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9001}),
    Action(name="update_order_status", kwargs={"order_id": 10003, "new_status": "placed"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ordered"}),
    Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "order", "entity_id": 10003, "action_enum": "placed", "payload_json": {"store_id": 9001}}),
    Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ordered", "payload_json": {"order_id": 10003}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_035",
  instruction=(
    "You have to create a peanut-free, no-heat school-lunch pack for the Alvarez household (household_id=202) using exactly recipes 409 and 410. The deliverable is a single grocery list under user_id=102 that reflects only those two lunches and complies with standard policy hygiene and auditing requirements. Do not place an order or propose substitutions."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":202}),
    Action(name="get_user_by_id", kwargs={"user_id":102}),
    Action(name="build_recipe_filters", kwargs={"meal_type":"Lunch", "min_protein_g":0, "peanut_free":True, "cuisines_exclude":[]}),
    Action(name="list_recipes_by_filters", kwargs={"filter_token":"F:Lunch:P0:PF1:EX"}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id":409}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id":410}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":202, "source_meal_plan_id":None, "created_by_user_id":102, "status_enum":"initialized"}),
    Action(name="log_audit_event", kwargs={"household_id":202, "user_id":102, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"created", "payload_json":{"peanut_free":True, "no_heat":True}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003, "recipe_ids_json":"[409,410]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id":8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id":8003, "household_id":202, "anchor_date":"2025-08-31"})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_036",
  instruction=(
    "You have to plan three pantry-first dinners for Chen Solo (household_id=203) for the week starting 2025-09-01 that satisfy household policy (no repeats in the last 30 days, cuisine diversity, ≤3 non-staple ingredients) and align to the adult target member (member_id=306). Success is one meal plan with exactly three dinners chosen from {401, 404, 408} and one derived grocery list that meets standard policy hygiene at anchor_date=2025-08-31. Return the created meal_plan_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":203}),
    Action(name="get_member_targets", kwargs={"member_id":306}),
    Action(name="list_recent_meal_history", kwargs={"household_id":203, "days_back":30, "anchor_date":"2025-08-31"}),
    Action(name="apply_cuisine_cap", kwargs={"recipe_ids_json":"[404,408,401]", "max_per_cuisine":3}),
    Action(name="minimize_new_ingredients", kwargs={"recipe_ids_json":"[404,408,401]", "max_new_ingredients_per_recipe":3}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id":404}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id":408}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id":401}),
    Action(name="create_meal_plan", kwargs={"household_id":203, "week_start_date":"2025-09-01", "created_by_user_id":103}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id":6003, "week_start_date":"2025-09-01", "selected_recipe_ids_json":"[404,408,401]"}),
    Action(name="log_audit_event", kwargs={"household_id":203, "user_id":103, "entity_type":"meal_plan", "entity_id":6003, "action_enum":"created", "payload_json":{"week_start_date":"2025-09-01"}}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":203, "source_meal_plan_id":6003, "created_by_user_id":103, "status_enum":"initialized"}),
    Action(name="log_audit_event", kwargs={"household_id":203, "user_id":103, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"created", "payload_json":{"source_meal_plan_id":6003}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003, "recipe_ids_json":"[404,408,401]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id":8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id":8003, "household_id":203, "anchor_date":"2025-08-31"})
  ],
  outputs=[
    "6003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_037",
  instruction=(
    "You have to prepare a peanut-safe, pantry-first breakfast restock for Thompson Retirement (household_id=210) using exactly three Breakfast recipes from {418, 421, 439}. “Pantry-first” here means staples are flagged for review per policy without adding extra non-staple items beyond the recipe aggregation. Deliver a single grocery list under user_id=110 that reflects only those breakfasts and meets standard policy hygiene at anchor_date=2025-08-31. Do not place an order."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":210}),
    Action(name="get_user_by_id", kwargs={"user_id":110}),
    Action(name="build_recipe_filters", kwargs={"meal_type":"Breakfast", "min_protein_g":0, "peanut_free":True, "cuisines_exclude":[]}),
    Action(name="list_recipes_by_filters", kwargs={"filter_token":"F:Breakfast:P0:PF1:EX"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":210, "source_meal_plan_id":None, "created_by_user_id":110, "status_enum":"initialized"}),
    Action(name="log_audit_event", kwargs={"household_id":210, "user_id":110, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"created", "payload_json":{"peanut_free":True}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003, "recipe_ids_json":"[418,421,439]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id":8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id":8003, "household_id":210, "anchor_date":"2025-08-31"})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_038",
  instruction=(
    "You fulfill a FreshMart Online delivery for the Williams-Brown Family (household_id=204) based on recipe 404 in the 2025-09-05T16:00:00Z–18:00:00Z pickup/delivery slot at store_id=9001. Acceptance: exactly one order is created and set to 'placed' using policy inventory rules (lowest-price in-stock/low items only; unavailable items are omitted if no valid substitution is proposed), and a single audit event records the placement. Return the created order_id and final total_cents."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":204}),
    Action(name="get_user_by_id", kwargs={"user_id":104}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":204, "source_meal_plan_id":None, "created_by_user_id":104, "status_enum":"initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003, "recipe_ids_json":"[404]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id":8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id":8003, "household_id":204, "anchor_date":"2025-08-31"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id":8003, "store_id":9001}),
    Action(name="set_grocery_list_status", kwargs={"list_id":8003, "status_enum":"finalized"}),
    Action(name="create_order_from_list", kwargs={"household_id":204, "store_id":9001, "list_id":8003, "scheduled_slot_start_ts":"2025-09-05T16:00:00Z", "scheduled_slot_end_ts":"2025-09-05T18:00:00Z"}),
    Action(name="add_order_items_from_list", kwargs={"order_id":10003, "store_id":9001, "product_overrides":{}}),
    Action(name="update_order_status", kwargs={"order_id":10003, "new_status":"placed"}),
    Action(name="log_audit_event", kwargs={"household_id":204, "user_id":104, "entity_type":"order", "entity_id":10003, "action_enum":"placed", "payload_json":{"list_id":8003, "store_id":9001}})
  ],
  outputs=[
    "10003",
    "899"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_039",
  instruction=(
    "You assemble a five-day, peanut-free school-lunch set for the Garcia Household (household_id=208) with a protein emphasis (≥12 g/serving). Success requires five Lunch recipes chosen from {409, 410, 411, 412, 413} under the ≤4 non-staple-ingredients policy; one grocery list under user_id=108 reflects the exact aggregation with correct section categorization and refreshed pantry and 30-day overlap flags at anchor_date=2025-08-31; and audits exist for meal-plan creation and list creation. Do not evaluate store inventory or place an order."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":208}),
    Action(name="build_recipe_filters", kwargs={"meal_type":"Lunch", "min_protein_g":12, "peanut_free":True, "cuisines_exclude":[]}),
    Action(name="list_recipes_by_filters", kwargs={"filter_token":"F:Lunch:P12:PF1:EX"}),
    Action(name="minimize_new_ingredients", kwargs={"recipe_ids_json":"[409,410,411,412,413]", "max_new_ingredients_per_recipe":4}),
    Action(name="create_meal_plan", kwargs={"household_id":208, "week_start_date":"2025-09-01", "created_by_user_id":108}),
    Action(name="log_audit_event", kwargs={"household_id":208, "user_id":108, "entity_type":"meal_plan", "entity_id":6003, "action_enum":"created", "payload_json":{"week_start_date":"2025-09-01"}}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id":6003, "week_start_date":"2025-09-01", "selected_recipe_ids_json":"[409,410,411,412,413]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":208, "source_meal_plan_id":6003, "created_by_user_id":108, "status_enum":"initialized"}),
    Action(name="log_audit_event", kwargs={"household_id":208, "user_id":108, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"created", "payload_json":{"peanut_free":True}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003, "recipe_ids_json":"[409,410,411,412,413]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id":8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id":8003, "household_id":208, "anchor_date":"2025-08-31"})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_040",
  instruction=(
    "You will produce a peanut-free Lunch grocery list for the Chen Solo household (household_id 203) from lunch recipes 409, 410, and 412 (no meal plan). The list must reflect aggregated quantities per (ingredient_id, unit), categorized sections, pantry-staple flags, and last-30-days overlap flags using 2025-09-07 as the anchor, and be left in 'ready' status with an audit of that state."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 203}),
    Action(name="get_user_by_id", kwargs={"user_id": 103}),
    Action(
      name="create_empty_grocery_list",
      kwargs={"household_id": 203, "source_meal_plan_id": None, "created_by_user_id": 103, "status_enum": "initialized"},
    ),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,412]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(
      name="flag_overlap_last_month_on_list",
      kwargs={"list_id": 8003, "household_id": 203, "anchor_date": "2025-09-07"},
    ),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 203,
        "user_id": 103,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "finalized",
        "payload_json": {"status": "ready", "list_id": 8003, "source_meal_plan_id": None},
      },
    ),
  ],
  outputs=[],
),

Task(
  annotator="saaish2",
  user_id="task_041",
  instruction=(
    "You will prepare a pantry-first Dinner grocery list for the Kowalski Couple (household_id 206) using recipes 408 and 405 (no meal plan). The final list must show aggregated quantities per (ingredient_id, unit), have grocery sections populated, include pantry-staple and last-30-days overlap flags computed with 2025-09-07 as the anchor, and be left in 'ready' status with an audit reflecting that state."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 206}),
    Action(name="get_user_by_id", kwargs={"user_id": 106}),
    Action(
      name="create_empty_grocery_list",
      kwargs={"household_id": 206, "source_meal_plan_id": None, "created_by_user_id": 106, "status_enum": "initialized"},
    ),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 206,
        "user_id": 106,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "created",
        "payload_json": {"status": "initialized", "list_id": 8003, "source_meal_plan_id": None},
      },
    ),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[408,405]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(
      name="flag_overlap_last_month_on_list",
      kwargs={"list_id": 8003, "household_id": 206, "anchor_date": "2025-09-07"},
    ),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 206,
        "user_id": 106,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "finalized",
        "payload_json": {"status": "ready", "list_id": 8003},
      },
    ),
  ],
  outputs=[],
),

Task(
  annotator="saaish2",
  user_id="task_042",
  instruction=(
    "You will plan five peanut-optional Dinners for the Johnson Large Family (household_id 207) for the week starting 2025-09-15, tuned toward adult targets (≈2300 kcal, 125g protein) with no repeats from the last 14 days and at most two per cuisine. The resulting plan should drive a single grocery list linked to it that includes categorized sections, pantry-staple flags, and last-30-days overlap flags using 2025-09-21 as the anchor; the list is left in 'ready' status with appropriate audits. Acceptance: one new meal plan with five Dinner entries; one linked list showing sections, pantry, and overlap flags; list status 'ready'; audits cover meal plan creation and list lifecycle."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 207}),
    Action(name="build_recipe_filters", kwargs={"meal_type": "Dinner", "min_protein_g": 25, "peanut_free": False, "cuisines_exclude": []}),
    Action(name="list_recipes_by_filters", kwargs={"filter_token": "F:Dinner:P25:PF0:EX"}),
    Action(name="list_recent_meal_history", kwargs={"household_id": 207, "days_back": 14, "anchor_date": "2025-09-21"}),
    Action(
      name="exclude_recipe_ids",
      kwargs={"candidate_recipe_ids_json": "[402,404,407,423,425,427,428,429,430,434,435]", "exclude_recipe_ids": []},
    ),
    Action(
      name="apply_cuisine_cap",
      kwargs={"recipe_ids_json": "[402,404,407,423,425,427,428,429,430,434,435]", "max_per_cuisine": 2},
    ),
    Action(
      name="rank_recipes_for_targets",
      kwargs={"recipe_ids_json": "[402,404,407,423,425,427,429,430,434]", "needed_count": 5, "target_calories": 2300, "target_protein": 125},
    ),
    Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2025-09-15", "created_by_user_id": 107}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 207,
        "user_id": 107,
        "entity_type": "meal_plan",
        "entity_id": 6003,
        "action_enum": "created",
        "payload_json": {"week_start_date": "2025-09-15", "entry_count": 5},
      },
    ),
    Action(
      name="bulk_add_meal_plan_entries",
      kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-15", "selected_recipe_ids_json": "[425,407,423,404,427]"},
    ),
    Action(
      name="create_empty_grocery_list",
      kwargs={"household_id": 207, "source_meal_plan_id": 6003, "created_by_user_id": 107, "status_enum": "initialized"},
    ),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 207,
        "user_id": 107,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "created",
        "payload_json": {"status": "initialized", "source_meal_plan_id": 6003},
      },
    ),
    Action(
      name="upsert_grocery_list_items_from_recipes",
      kwargs={"list_id": 8003, "recipe_ids_json": "[425,407,423,404,427]"},
    ),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(
      name="flag_overlap_last_month_on_list",
      kwargs={"list_id": 8003, "household_id": 207, "anchor_date": "2025-09-21"},
    ),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 207,
        "user_id": 107,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "updated",
        "payload_json": {"status": "ready", "source_meal_plan_id": 6003},
      },
    ),
  ],
  outputs=[],
),

Task(
  annotator="saaish2",
  user_id="task_043",
  instruction=(
    "You have to create a peanut-free, no-heat school-lunch pack for the “Alvarez Household” (household_id=202) using exactly five lunch recipes with prep time ≤10 minutes. Choose the five lowest recipe_id values from the filtered candidates, produce a ready grocery list (categories applied; pantry staples and 30-day overlaps flagged with anchor_date=2025-09-08), capture audits for list creation and finalization, and return the created list_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":202}),
    Action(name="get_user_by_id", kwargs={"user_id":102}),
    Action(name="build_recipe_filters", kwargs={"meal_type":"Lunch","peanut_free":True,"no_heat":True,"max_prep_minutes":10}),
    Action(name="list_recipes_by_filters", kwargs={"filter_token":"F:Lunch:P0:PF1:EX"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":202,"created_by_user_id":102,"status_enum":"initialized"}),
    Action(name="log_audit_event", kwargs={"household_id":202,"user_id":102,"entity_type":"grocery_list","entity_id":8003,"action_enum":"grocery_list_created","payload_json":{"status":"initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[409,410,411,412,413]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id":8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id":8003,"household_id":202,"anchor_date":"2025-09-08"}),
    Action(name="set_grocery_list_status", kwargs={"list_id":8003,"status_enum":"ready"}),
    Action(name="log_audit_event", kwargs={"household_id":202,"user_id":102,"entity_type":"grocery_list","entity_id":8003,"action_enum":"grocery_list_status_set","payload_json":{"status":"ready"}})
  ],
  outputs=["8003"]
),

Task(
  annotator="saaish2",
  user_id="task_044",
  instruction=(
    "You prepare a breakfast starter list for the “Garcia Household” (household_id=208) built from recipes 418 and 421. The result is a single ready grocery list with sections categorized, pantry staples flagged, overlaps flagged using anchor_date=2025-09-05, and audit events for list creation and finalization."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":208}),
    Action(name="get_user_by_id", kwargs={"user_id":108}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":208,"created_by_user_id":108,"status_enum":"initialized"}),
    Action(name="log_audit_event", kwargs={"household_id":208,"user_id":108,"entity_type":"grocery_list","entity_id":8003,"action_enum":"grocery_list_created","payload_json":{"status":"initialized"}}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id":418}),
    Action(name="get_recipe_by_id", kwargs={"recipe_id":421}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[418,421]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id":8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id":8003,"household_id":208,"anchor_date":"2025-09-05"}),
    Action(name="set_grocery_list_status", kwargs={"list_id":8003,"status_enum":"ready"}),
    Action(name="log_audit_event", kwargs={"household_id":208,"user_id":108,"entity_type":"grocery_list","entity_id":8003,"action_enum":"grocery_list_status_set","payload_json":{"status":"ready"}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_045",
  instruction=(
    "You create a light snack bundle for the “Thompson Retirement” household (household_id=210) using exactly two snack recipes (recipe_id ∈ {449, 450}). Deliver a single ready grocery list for household_id=210 with sections categorized, pantry staples flagged, 30-day overlaps flagged using anchor_date=2025-09-05, and audit events for list creation and finalization."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":210}),
    Action(name="get_user_by_id", kwargs={"user_id":110}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":210,"created_by_user_id":110,"status_enum":"initialized"}),
    Action(name="log_audit_event", kwargs={"household_id":210,"user_id":110,"entity_type":"grocery_list","entity_id":8003,"action_enum":"grocery_list_created","payload_json":{"status":"initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[449,450]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id":8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id":8003,"household_id":210,"anchor_date":"2025-09-05"}),
    Action(name="set_grocery_list_status", kwargs={"list_id":8003,"status_enum":"ready"}),
    Action(name="log_audit_event", kwargs={"household_id":210,"user_id":110,"entity_type":"grocery_list","entity_id":8003,"action_enum":"grocery_list_status_set","payload_json":{"status":"ready"}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_046",
  instruction=(
    "You will finalize the Mercer Family’s existing grocery list (ID 8001) by marking pantry staples and last-30-day overlap using that household’s meal history. Then set the list status to “ready” and record an audit of this transition. Acceptance: for list 8001, pantry_staple_flag and overlap_last_month_flag are updated on all items; status_enum == 'ready'; one audit exists against list 8001 for this change."
  ),
  actions=[
    Action(name="get_grocery_list_details", kwargs={"list_id": 8001}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8001}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8001, "household_id": 201}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8001, "status_enum": "ready"}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 201,
        "user_id": 101,
        "entity_type": "grocery_list",
        "entity_id": 8001,
        "action_enum": "flags_and_ready",
        "payload_json": {"list_id": 8001, "status": "ready"}
      }
    ),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_047",
  instruction=(
    "You will create a peanut-free school-lunch grocery list for the Garcia Household using exactly these Lunch recipe IDs: 409, 410, 444. Categorize items by store section, mark pantry staples, and record an audit of list creation. Leave the list in 'initialized' status. Finally, return the grocery_list_id you created."
  ),
  actions=[
    Action(
      name="create_empty_grocery_list",
      kwargs={"household_id": 208, "created_by_user_id": 108, "status_enum": "initialized"}
    ),
    Action(
      name="upsert_grocery_list_items_from_recipes",
      kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,444]"}
    ),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 208,
        "user_id": 108,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "created_from_lunches",
        "payload_json": {"list_id": 8003, "recipes": [409, 410, 444]}
      }
    ),
    Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
  ],
  outputs=["8003"]
),

Task(
  annotator="saaish2",
  user_id="task_048",
  instruction=(
    "You create a seven-lunch meal plan for the Johnson Large Family (household_id=207) for the week starting 2025-09-08 under user_id=107 using exactly these recipes, in order: [409,410,411,412,441,442,447]. Success means a single new meal_plans row with seven Lunch entries for those recipes starting 2025-09-08, and one audit event recording plan creation. Return the stored week_start_date for the created plan."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":207}),
    Action(name="get_user_by_id", kwargs={"user_id":107}),
    Action(name="create_meal_plan", kwargs={"household_id":207,"week_start_date":"2025-09-08","created_by_user_id":107}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-08","selected_recipe_ids_json":"[409,410,411,412,441,442,447]"}),
    Action(name="log_audit_event", kwargs={"household_id":207,"user_id":107,"entity_type":"meal_plan","entity_id":6003,"action_enum":"plan_created","payload_json":{"week_start":"2025-09-08","entries":7}}),
  ],
  outputs=[
    "2025-09-08"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_049",
  instruction=(
    "You have to re-categorize the existing Alvarez Household grocery list (ID 8002), keep its status as 'initialized', check availability at GrocerDash (store_id 9002), and record an audit of the inventory check. Acceptance: for list 8002, grocery sections are set, status_enum == 'initialized', and one audit exists for the inventory check."
  ),
  actions=[
    Action(name="get_grocery_list_details", kwargs={"list_id": 8002}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8002}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8002, "status_enum": "initialized"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8002, "store_id": 9002}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 202,
        "user_id": 102,
        "entity_type": "grocery_list",
        "entity_id": 8002,
        "action_enum": "inventory_checked",
        "payload_json": {"list_id": 8002, "store_id": 9002}
      }
    ),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_050",
  instruction=(
    "You will create a small Dinner grocery list for the Williams-Brown Family from exactly these two Dinner recipe IDs: 431 and 432. Populate items from these recipes, mark last-30-day overlap for household meals, set the list status to 'ready', and log an audit of the change. Acceptance: a new list exists with items from only 431 and 432, overlap flags set, status_enum == 'ready', and an audit recorded."
  ),
  actions=[
    Action(
      name="create_empty_grocery_list",
      kwargs={"household_id": 204, "created_by_user_id": 104, "status_enum": "initialized"}
    ),
    Action(
      name="upsert_grocery_list_items_from_recipes",
      kwargs={"list_id": 8003, "recipe_ids_json": "[431,432]"}
    ),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 204}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 204,
        "user_id": 104,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "flags_and_ready",
        "payload_json": {"list_id": 8003, "recipes": [431, 432], "status": "ready"}
      }
    ),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_051",
  instruction=(
    "You will create a peanut-free Lunch grocery list for the Kim-Smith Family using exactly these Lunch recipe IDs: 441 and 445. Populate items, check availability at Health First Market (store_id 9006), and log an audit of the availability check. Leave the list in 'initialized' status. Acceptance: a new list exists containing only those recipes, availability was checked at store 9006, and an audit is recorded."
  ),
  actions=[
    Action(
      name="create_empty_grocery_list",
      kwargs={"household_id": 209, "created_by_user_id": 109, "status_enum": "initialized"}
    ),
    Action(
      name="upsert_grocery_list_items_from_recipes",
      kwargs={"list_id": 8003, "recipe_ids_json": "[441,445]"}
    ),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9006}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 209,
        "user_id": 109,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "inventory_checked",
        "payload_json": {"list_id": 8003, "store_id": 9006}
      }
    ),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_052",
  instruction=(
    "You create a standalone grocery list for the household “Chen Solo” (household_id=203) under created_by_user_id=103, not linked to any meal plan, aggregated from exactly these recipes: [401, 402]. Success means a single new grocery_lists row for that household with items aggregated from those recipes and status ‘initialized’; record one audit of list creation. Return the new list_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":203}),
    Action(name="get_user_by_id", kwargs={"user_id":103}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":203,"source_meal_plan_id":None,"created_by_user_id":103,"status_enum":"initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[401,402]"}),
    Action(name="log_audit_event", kwargs={"household_id":203,"user_id":103,"entity_type":"grocery_lists","entity_id":8003,"action_enum":"list_created","payload_json":{"recipe_ids":[401,402]}})
  ],
  outputs=["8003"]
),

Task(
  annotator="saaish2",
  user_id="task_053",
  instruction=(
    "You finalize and hygiene-refresh the existing grocery list list_id=8002 for the “Alvarez Household” (household_id=202). Success means the list’s sections are refreshed from ingredient metadata, pantry_staple_flag is consistent, and the list status is set to ‘finalized’ with an audit recorded."
  ),
  actions=[
    Action(name="get_grocery_list_details", kwargs={"list_id":8002}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8002}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id":8002}),
    Action(name="set_grocery_list_status", kwargs={"list_id":8002,"status_enum":"finalized"}),
    Action(name="log_audit_event", kwargs={"household_id":202,"user_id":102,"entity_type":"grocery_lists","entity_id":8002,"action_enum":"list_finalized","payload_json":{"status_after":"finalized"}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_054",
  instruction=(
    "You mark 30-day overlap flags for the “Alvarez Household” (household_id=202) on grocery list list_id=8002 using anchor_date=2025-08-31. Success means each grocery_list_items row in that list has overlap_last_month_flag set according to the household’s last 30 days of meals, and an audit is recorded."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":202}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id":8002,"household_id":202,"anchor_date":"2025-08-31"}),
    Action(name="log_audit_event", kwargs={"household_id":202,"user_id":102,"entity_type":"grocery_lists","entity_id":8002,"action_enum":"overlap_flags_updated","payload_json":{"anchor_date":"2025-08-31"}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_055",
  instruction=(
    "You create a compact two-dinner plan for the “Garcia Household” (household_id=208) for the week starting 2025-09-01 under created_by_user_id=108 using exactly these dinner recipes in order: [406, 407]. Success means a single new meal_plans row for that week linked to that household and exactly two Dinner entries on that plan. Return the created meal_plan_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":208}),
    Action(name="create_meal_plan", kwargs={"household_id":208,"week_start_date":"2025-09-01","created_by_user_id":108}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-01","selected_recipe_ids_json":"[406,407]"}),
    Action(name="log_audit_event", kwargs={"household_id":208,"user_id":108,"entity_type":"meal_plans","entity_id":6003,"action_enum":"meal_plan_created","payload_json":{"week_start_date":"2025-09-01","entry_count":2}})
  ],
  outputs=["6003"]
),

Task(
  annotator="saaish2",
  user_id="task_056",
  instruction=(
    "For the existing plan meal_plan_id=6002 of the “Alvarez Household”, you apply the standard child-friendly modification note to recipe_id=407 and persist it on the corresponding Dinner entry. Success means that entry’s notes equal the fixed child-mods template and an audit is recorded."
  ),
  actions=[
    Action(name="get_meal_plan_details", kwargs={"meal_plan_id":6002}),
    Action(name="generate_child_modifications", kwargs={"recipe_ids_json":"[407]"}),
    Action(name="update_meal_plan_entry_notes", kwargs={"meal_plan_id":6002,"notes_map":{"407":"Reduce spice for kids. Child-friendly: mild seasoning; cut to bite-size; soft textures."}}),
    Action(name="log_audit_event", kwargs={"household_id":202,"user_id":102,"entity_type":"meal_plans","entity_id":6002,"action_enum":"entry_notes_updated","payload_json":{"recipe_id":407}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_057",
  instruction=(
    "You prepare a quick grocery list for the “Johnson Large Family” (household_id=207) built from exactly these two dinner recipes: [401, 402]. Success means one new grocery_lists row for that household, items aggregated from those recipes, grocery sections refreshed, and a creation audit is recorded."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":207}),
    Action(name="get_user_by_id", kwargs={"user_id":107}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":207,"source_meal_plan_id":None,"created_by_user_id":107,"status_enum":"initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[401,402]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
    Action(name="log_audit_event", kwargs={"household_id":207,"user_id":107,"entity_type":"grocery_lists","entity_id":8003,"action_enum":"list_created","payload_json":{"recipe_ids":[401,402]}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_058",
  instruction=(
    "You have to create a 5-night Dinner mini-plan for the Chen Solo household (household_id 203) for the week starting 2025-09-08 using exactly these recipes, in order: 401, 402, 403, 404, 405. Produce one grocery list linked to that plan from those recipes, evaluate 30-day overlap flags using 2025-09-14 as the anchor, and leave the list in 'ready' status. Acceptance: one meal plan with five Dinner entries dated 2025-09-08 through 2025-09-12 in the specified order; one linked grocery list aggregated from those recipes with overlap flags set; list status 'ready'; exactly two audits recorded (plan created; list ready). Return the meal_plan_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 203}),
    Action(name="get_user_by_id", kwargs={"user_id": 103}),
    Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-08", "created_by_user_id": 103}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[401,402,403,404,405]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 203, "source_meal_plan_id": 6003, "created_by_user_id": 103, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,402,403,404,405]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 203, "anchor_date": "2025-09-14"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-08"}}),
    Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"status": "ready"}})
  ],
  outputs=[
    "6003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_059",
  instruction=(
    "You have to assemble a peanut-free weekday Lunch list for the Williams-Brown Family (household_id 204) from exactly these Lunch recipes: 409, 410, 412, 445. Honor peanut-free constraints when resolving availability at GrocerDash (store_id 9002). Create a delivery order for 2025-09-03T10:00:00Z–2025-09-03T12:00:00Z, add all available items at the lowest price, leave the order in 'placed' status, and set the list to 'ordered'. Acceptance: one list aggregated from those recipes; inventory checked at store 9002; safe substitutions applied when deterministically available; one order created and populated only with available items; order 'placed'; list 'ordered'; audits include order creation, order placed, and list ordered in chronological order."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 204}),
    Action(name="get_user_by_id", kwargs={"user_id": 104}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 204, "source_meal_plan_id": None, "created_by_user_id": 104, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,412,445]"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(name="propose_substitute_products", kwargs={"store_id": 9002, "flagged_items": [{"ingredient_id": 1001}, {"ingredient_id": 1005}, {"ingredient_id": 1013}, {"ingredient_id": 1014}, {"ingredient_id": 1015}, {"ingredient_id": 1024}, {"ingredient_id": 1043}, {"ingredient_id": 1044}, {"ingredient_id": 1089}], "require_peanut_free": True}),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id": 8003, "substitutions": []}),
    Action(name="create_order_from_list", kwargs={"household_id": 204, "store_id": 9002, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-03T10:00:00Z", "scheduled_slot_end_ts": "2025-09-03T12:00:00Z"}),
    Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"store_id": 9002, "slot_start": "2025-09-03T10:00:00Z", "slot_end": "2025-09-03T12:00:00Z"}}),
    Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9002}),
    Action(name="update_order_status", kwargs={"order_id": 10003, "new_status": "placed"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ordered"}),
    Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "order", "entity_id": 10003, "action_enum": "placed", "payload_json": {"store_id": 9002}}),
    Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ordered", "payload_json": {"status": "ordered"}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_060",
  instruction=(
    "You will deliver a vegetarian Dinner plan for the Patel Extended Family (household_id 205) covering 2025-09-15 to 2025-09-18, using exactly these four recipes in this order: 405, 424, 426, 432. Acceptance: four Dinner entries dated 2025-09-15 through 2025-09-18 in the specified order; a single linked grocery list aggregated from those recipes with 30-day overlap flags evaluated using 2025-09-14 as the anchor; list status 'ready'; exactly two audits recorded (plan created; list ready). Return the grocery_list_id and the total item count."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 205}),
    Action(name="get_user_by_id", kwargs={"user_id": 105}),
    Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2025-09-15", "created_by_user_id": 105}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-15", "selected_recipe_ids_json": "[405,424,426,432]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 205, "source_meal_plan_id": 6003, "created_by_user_id": 105, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[405,424,426,432]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 205, "anchor_date": "2025-09-14"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-15"}}),
    Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"status": "ready"}})
  ],
  outputs=[
    "8003",
    "15"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_061",
  instruction=(
    "You will prepare a peanut-free school-lunch list for the Kim-Smith Family (household_id 209) using exactly these Lunch recipes: 441, 442, 444. Set 30-day overlap flags using 2025-09-07 as the anchor, evaluate availability at GrocerDash (store_id 9002) with peanut-safe substitution policy, apply safe in-store substitutions if available, and leave the list in 'ready' status. Record audits for list creation and readiness. Acceptance: one grocery list aggregated from those recipes; overlap flags set; inventory checked at 9002 honoring peanut-free substitutions; status 'ready'; two audits. Return the grocery_list_id and the total item count."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 209}),
    Action(name="get_user_by_id", kwargs={"user_id": 109}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 209, "source_meal_plan_id": None, "created_by_user_id": 109, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[441,442,444]"}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2025-09-07"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(name="propose_substitute_products", kwargs={"store_id": 9002, "flagged_items": [{"ingredient_id": 1009}, {"ingredient_id": 1013}, {"ingredient_id": 1014}, {"ingredient_id": 1020}, {"ingredient_id": 1024}, {"ingredient_id": 1043}, {"ingredient_id": 1044}, {"ingredient_id": 1070}, {"ingredient_id": 1090}, {"ingredient_id": 1109}], "require_peanut_free": True}),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id": 8003, "substitutions": []}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"status": "ready"}})
  ],
  outputs=[
    "8003",
    "14"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_062",
  instruction=(
    "You have to create a 4-night, low-prep Dinner plan for the Thompson Retirement household (household_id 210) covering 2025-09-05 to 2025-09-08 using exactly these recipes in order: 435, 428, 423, 425. Provide one linked grocery list from those recipes, honor store availability at FreshMart Online (store_id 9001) with deterministic in-store substitutions when available, and schedule delivery for 2025-09-05T17:00:00Z–2025-09-05T19:00:00Z. The order should be set to 'placed' and the list to 'ordered'. Acceptance: one plan with four Dinner entries dated 2025-09-05 through 2025-09-08; one linked list; availability checked and substitutions applied when deterministic; one order created and populated only with available items; order 'placed'; list 'ordered'; audits recorded for meal plan creation, grocery list creation, order creation, order placed, and list ordered."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 210}),
    Action(name="get_user_by_id", kwargs={"user_id": 110}),
    Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2025-09-05", "created_by_user_id": 110}),
    Action(
      name="log_audit_event",
      kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-05"}}
    ),
    Action(
      name="bulk_add_meal_plan_entries",
      kwargs={
        "meal_plan_id": 6003,
        "week_start_date": "2025-09-05",
        "selected_recipe_ids_json": "[435,428,423,425]",
        "meal_type_enum": "Dinner",
        "entry_dates_json": "[\"2025-09-05\",\"2025-09-06\",\"2025-09-07\",\"2025-09-08\"]",
        "enforce_cuisine_diversity": True,
        "enforce_nutrition_window": True
      }
    ),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 210, "source_meal_plan_id": 6003, "created_by_user_id": 110, "status_enum": "initialized"}),
    Action(
      name="log_audit_event",
      kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}
    ),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[435,428,423,425]"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9001}),
    Action(
      name="create_order_from_list",
      kwargs={"household_id": 210, "store_id": 9001, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-05T17:00:00Z", "scheduled_slot_end_ts": "2025-09-05T19:00:00Z"}
    ),
    Action(
      name="add_order_items_from_list",
      kwargs={
        "order_id": 10003,
        "store_id": 9001,
        "only_in_stock": True,
        "allow_instore_substitutions": True,
        "price_strategy": "lowest"
      }
    ),
    Action(
      name="update_order_status",
      kwargs={"order_id": 10003, "new_status": "placed"}
    ),
    Action(
      name="set_grocery_list_status",
      kwargs={"list_id": 8003, "status_enum": "ordered"}
    ),
    Action(
      name="log_audit_event",
      kwargs={"household_id": 210, "user_id": 110, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"store_id": 9001}}
    ),
    Action(
      name="log_audit_event",
      kwargs={"household_id": 210, "user_id": 110, "entity_type": "order", "entity_id": 10003, "action_enum": "placed", "payload_json": {"store_id": 9001}}
    ),
    Action(
      name="log_audit_event",
      kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ordered", "payload_json": {"status": "ordered"}}
    ),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_063",
  instruction=(
    "You have to prepare a single standalone grocery order for the “Mercer Family” (household_id=201) under user_id=101 using exactly recipes [401, 402]. Honor store 9001 availability, apply any in-store substitutes before checkout, schedule the order for 2025-01-02T10:00:00Z–12:00:00Z, and finish with the grocery list in status “ordered.” Record audits for the list’s creation and ordering and for the order’s creation and placement."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":201}),
    Action(name="get_user_by_id", kwargs={"user_id":101}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":201,"source_meal_plan_id":None,"created_by_user_id":101,"status_enum":"initialized"}),
    Action(name="log_audit_event", kwargs={
      "household_id":201,"user_id":101,"entity_type":"grocery_list","entity_id":8003,
      "action_enum":"created","payload_json":{"status":"initialized"}
    }),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[401,402]"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id":8003,"store_id":9001}),
    Action(name="propose_substitute_products", kwargs={
      "store_id":9001,
      "flagged_items":[
        {"ingredient_id":1008},
        {"ingredient_id":1010},
        {"ingredient_id":1011},
        {"ingredient_id":1013},
        {"ingredient_id":1016},
        {"ingredient_id":1017},
        {"ingredient_id":1018},
        {"ingredient_id":1019},
        {"ingredient_id":1024}
      ]
    }),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id":8003,"substitutions":[]}),
    Action(name="create_order_from_list", kwargs={
      "household_id":201,"store_id":9001,"list_id":8003,
      "scheduled_slot_start_ts":"2025-01-02T10:00:00Z","scheduled_slot_end_ts":"2025-01-02T12:00:00Z"
    }),
    Action(name="log_audit_event", kwargs={
      "household_id":201,"user_id":101,"entity_type":"order","entity_id":10003,
      "action_enum":"created","payload_json":{"store_id":9001}
    }),
    Action(name="add_order_items_from_list", kwargs={"order_id":10003,"store_id":9001}),
    Action(name="update_order_status", kwargs={"order_id":10003,"new_status":"placed"}),
    Action(name="set_grocery_list_status", kwargs={"list_id":8003,"status_enum":"ordered"}),
    Action(name="log_audit_event", kwargs={
      "household_id":201,"user_id":101,"entity_type":"order","entity_id":10003,
      "action_enum":"placed","payload_json":{"store_id":9001}
    }),
    Action(name="log_audit_event", kwargs={
      "household_id":201,"user_id":101,"entity_type":"grocery_list","entity_id":8003,
      "action_enum":"ordered","payload_json":{"status":"ordered"}
    }),
  ],
  outputs=[]
),


Task(
  annotator="saaish2",
  user_id="task_064",
  instruction=(
    "You create a new order (order shell) for the Mercer Family (household_id=201) at FreshMart Online (store_id=9001) from existing grocery list 8001, scheduled for 2025-09-02T16:00:00Z–18:00:00Z, and populate order_items by selecting lowest-price in-stock products per policy. Record one audit event of order creation. Do not change order status."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":201}),
    Action(name="get_user_by_id", kwargs={"user_id":101}),
    Action(name="create_order_from_list", kwargs={"household_id":201,"store_id":9001,"list_id":8001,"scheduled_slot_start_ts":"2025-09-02T16:00:00Z","scheduled_slot_end_ts":"2025-09-02T18:00:00Z"}),
    Action(name="add_order_items_from_list", kwargs={"order_id":10003,"store_id":9001}),
    Action(name="log_audit_event", kwargs={"household_id":201,"user_id":101,"entity_type":"order","entity_id":10003,"action_enum":"order_created","payload_json":"{\"source_list\":8001}"}),
  ],
  outputs=[
  ]
),

Task(
  annotator="saaish2",
  user_id="task_065",
  instruction=(
    "You execute a family grocery run for the “Johnson Large Family” (household_id=207) under user_id=107 using exactly recipes [423, 425, 435] as one standalone list. Success means store 9003 availability is honored with in-store substitutions applied where needed before placing a single order for 2025-01-02T10:00:00Z–12:00:00Z using lowest-price in-stock items; the grocery list ends in status “ordered”; and audits capture the order’s creation and placement and the list’s final ordering."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":207}),
    Action(name="get_user_by_id", kwargs={"user_id":107}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":207,"source_meal_plan_id":None,"created_by_user_id":107,"status_enum":"initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[423,425,435]"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id":8003,"store_id":9003}),
    Action(name="propose_substitute_products", kwargs={
      "store_id":9003,
      "flagged_items":[
        {"ingredient_id":1045},
        {"ingredient_id":1009},
        {"ingredient_id":1010},
        {"ingredient_id":1020},
        {"ingredient_id":1006},
        {"ingredient_id":1078},
        {"ingredient_id":1049},
        {"ingredient_id":1022},
        {"ingredient_id":1106},
        {"ingredient_id":1107},
        {"ingredient_id":1002},
        {"ingredient_id":1066},
        {"ingredient_id":1111}
      ]
    }),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id":8003,"substitutions":[]}),
    Action(name="create_order_from_list", kwargs={
      "household_id":207,"store_id":9003,"list_id":8003,
      "scheduled_slot_start_ts":"2025-01-02T10:00:00Z","scheduled_slot_end_ts":"2025-01-02T12:00:00Z"
    }),
    Action(name="log_audit_event", kwargs={
      "household_id":207,"user_id":107,"entity_type":"order","entity_id":10003,
      "action_enum":"created","payload_json":{"store_id":9003}
    }),
    Action(name="add_order_items_from_list", kwargs={"order_id":10003,"store_id":9003}),
    Action(name="update_order_status", kwargs={"order_id":10003,"new_status":"placed"}),
    Action(name="set_grocery_list_status", kwargs={"list_id":8003,"status_enum":"ordered"}),
    Action(name="log_audit_event", kwargs={
      "household_id":207,"user_id":107,"entity_type":"order","entity_id":10003,
      "action_enum":"placed","payload_json":{"store_id":9003}
    }),
    Action(name="log_audit_event", kwargs={
      "household_id":207,"user_id":107,"entity_type":"grocery_list","entity_id":8003,
      "action_enum":"ordered","payload_json":{"status":"ordered"}
    }),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_066",
  instruction=(
    "You have to deliver a seven-night dinner plan for the “Alvarez Household” (household_id=202) for the week starting 2025-09-15 under user_id=102 using recipes [441, 442, 444, 435, 428, 423, 425]. Build one linked grocery list, apply categorization and pantry-staples hygiene, set 30-day overlap flags at anchor_date=2025-08-31, finalize the list, and record audits for meal-plan creation and grocery-list finalization only."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":202}),
    Action(name="get_user_by_id", kwargs={"user_id":102}),
    Action(name="create_meal_plan", kwargs={"household_id":202,"week_start_date":"2025-09-15","created_by_user_id":102}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-15","selected_recipe_ids_json":"[441,442,444,435,428,423,425]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":202,"source_meal_plan_id":6003,"created_by_user_id":102,"status_enum":"initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[441,442,444,435,428,423,425]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id":8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id":8003,"household_id":202,"anchor_date":"2025-08-31"}),
    Action(name="set_grocery_list_status", kwargs={"list_id":8003,"status_enum":"finalized"}),
    Action(name="log_audit_event", kwargs={
      "household_id":202,"user_id":102,"entity_type":"meal_plan","entity_id":6003,
      "action_enum":"created","payload_json":{"week_start_date":"2025-09-15"}
    }),
    Action(name="log_audit_event", kwargs={
      "household_id":202,"user_id":102,"entity_type":"grocery_list","entity_id":8003,
      "action_enum":"finalized","payload_json":{"status":"finalized"}
    }),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_067",
  instruction=(
    "You will compile a peanut-free school-lunch grocery list for the Patel Extended Family (household_id 205) using exactly these seven Lunch recipe IDs: 409, 410, 412, 413, 441, 444, 445. Aggregate items, populate grocery sections, and mark the list ready with an audit recorded for the readiness change. Acceptance: one grocery list for household 205 with items aggregated from exactly the seven recipes above; grocery sections filled; list status = 'ready'; an audit exists noting the list moved from 'initialized' to 'ready'. Return the list_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 205}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 205, "created_by_user_id": 105, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,412,413,441,444,445]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"from": "initialized", "to": "ready"}}),
  ],
  outputs=["8003"]
),

Task(
  annotator="saaish2",
  user_id="task_068",
  instruction=(
    "You will create a 7-night Dinner plan for the Garcia Household (household_id 208) for the week starting 2025-09-08 using exactly these recipe IDs in order: 401, 402, 425, 427, 428, 431, 433. Link a grocery list to that plan and aggregate items; mark pantry-staple flags. Acceptance: one meal plan with seven Dinner entries dated 2025-09-08 through 2025-09-14 in the given order; one linked grocery list containing the aggregated items and pantry flags; list status remains 'initialized'. Return the meal_plan_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 208}),
    Action(name="get_user_by_id", kwargs={"user_id": 108}),
    Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2025-09-08", "created_by_user_id": 108}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[401,402,425,427,428,431,433]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 208, "source_meal_plan_id": 6003, "created_by_user_id": 108, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,402,425,427,428,431,433]"}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
  ],
  outputs=["6003"]
),

Task(
  annotator="saaish2",
  user_id="task_069",
  instruction=(
    "You will assemble a 5-day peanut-free school-lunch list for the Johnson Large Family (household_id 207) from exactly these Lunch recipe IDs: 409, 410, 411, 412, 413; then check availability at GrocerDash (store_id 9002), create an order for delivery slot 2025-09-03T10:00:00Z–2025-09-03T12:00:00Z, and populate it with the lowest-price available items (counting 'in_stock' or 'low' as available) from that store. Audit the major transitions: list creation, inventory checked, order created, and items added. Leave the order in its default status. Acceptance: one grocery list with aggregated items from those five recipes; inventory checked at store 9002; one order created and filled only with available items; required audit events exist. Return the order_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 207}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 207, "created_by_user_id": 107, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,411,412,413]"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "inventory_checked", "payload_json": {"store_id": 9002}}),
    Action(name="create_order_from_list", kwargs={"household_id": 207, "store_id": 9002, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-03T10:00:00Z", "scheduled_slot_end_ts": "2025-09-03T12:00:00Z"}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"store_id": 9002}}),
    Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9002}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "order", "entity_id": 10003, "action_enum": "items_added", "payload_json": {"source_list_id": 8003}}),
  ],
  outputs=["10003"]
),

Task(
  annotator="saaish2",
  user_id="task_070",
  instruction=(
    "You create a standalone grocery list for the Alvarez Household (household_id=202) under user_id=102, not linked to any meal plan, aggregated from exactly these lunch recipes: [409,410,413]. Success means one new grocery_lists row with items aggregated from those recipes and status 'initialized', plus one audit event recording list creation. Return the new list_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":202}),
    Action(name="get_user_by_id", kwargs={"user_id":102}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":202,"source_meal_plan_id":None,"created_by_user_id":102,"status_enum":"initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[409,410,413]"}),
    Action(name="log_audit_event", kwargs={"household_id":202,"user_id":102,"entity_type":"grocery_list","entity_id":8003,"action_enum":"list_created","payload_json":{"source":"recipes","count":3}}),
  ],
  outputs=[
    "8003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_071",
  instruction=(
    "You will create a 3-night Dinner grocery list for the Kowalski Couple (household_id 206) from exactly these recipe IDs: 404, 405, 431. Check availability at Budget Foods Express (store_id 9004), set pantry-staple flags and grocery sections, and mark the list 'ready'. Audit list creation and readiness change. Acceptance: one grocery list with aggregated items from those recipes; availability checked at store 9004; pantry flags and sections present; final list status 'ready'; required audit events exist. Return the list_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 206}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 206, "created_by_user_id": 106, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[404,405,431]"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9004}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"from": "initialized", "to": "ready"}}),
  ],
  outputs=["8003"]
),

Task(
  annotator="saaish2",
  user_id="task_072",
  instruction=(
    "You have to produce a single-store Dinner order for the Williams-Brown Family (household_id 204) based on exactly these seven recipes: 423, 424, 425, 426, 427, 428, 429. The result must be one draft order at FreshMart Online (store_id 9001) for 2025-09-05T18:00:00Z–20:00:00Z that sources only the store’s available items at the lowest price. Record audits for creation and item population. Acceptance: a dedicated list exists for those seven recipes; a matching draft order exists for store 9001 at the stated slot; the order contains only available items chosen at the lowest price; audits exist; return the order_id and final total_cents."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 204}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 204, "created_by_user_id": 104, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[423,424,425,426,427,428,429]"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9001}),
    Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "inventory_checked", "payload_json": {"store_id": 9001}}),
    Action(name="create_order_from_list", kwargs={"household_id": 204, "store_id": 9001, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-05T18:00:00Z", "scheduled_slot_end_ts": "2025-09-05T20:00:00Z"}),
    Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"store_id": 9001}}),
    Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9001}),
    Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "order", "entity_id": 10003, "action_enum": "items_added", "payload_json": {"source_list_id": 8003}}),
  ],
  outputs=["10003", "2746"]
),

Task(
  annotator="saaish2",
  user_id="task_073",
  instruction=(
    "You have to deliver a five-night Dinner plan for the Alvarez Household (household_id 202) covering 2025-09-08 through 2025-09-12 using exactly recipes 401, 402, 404, 405, 431 in that order. Provide one linked grocery list with aggregated items, correct grocery sections, pantry-staple flags, and leave the list in 'ready' with audits reflecting both meal plan creation and the list’s readiness change. Acceptance: one plan with five Dinner entries on the stated dates in the stated order; one linked list showing sections and pantry flags; final list status 'ready'; audits exist for meal plan creation and for the list moving from 'initialized' to 'ready'."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 202}),
    Action(name="get_user_by_id", kwargs={"user_id": 102}),
    Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2025-09-08", "created_by_user_id": 102}),
    Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-08"}}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[401,402,404,405,431]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 202, "source_meal_plan_id": 6003, "created_by_user_id": 102, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,402,404,405,431]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"from": "initialized", "to": "ready"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_074",
  instruction=(
    "You have to prepare a five-day, peanut-free school-lunch grocery list for the Johnson Large Family (household_id 207) from exactly Lunch recipes 409, 410, 411, 412, 413. The list must aggregate items, show correct grocery sections and pantry-staple flags, and reflect last-30-day overlap as of 2025-09-07. Keep the list in 'initialized' and record audits for creation, sections populated, and overlap evaluation (include peanut_free: true in the overlap-evaluated audit payload). Acceptance: one list for household 207 using exactly those recipes; sections and pantry flags present; overlap flags reflect meals in the 30-day window up to 2025-09-07; status remains 'initialized'; audits exist for creation, sections populated, and overlap evaluation indicating peanut_free true."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 207}),
    Action(name="get_user_by_id", kwargs={"user_id": 107}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 207, "created_by_user_id": 107, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,411,412,413]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="list_recent_meal_history", kwargs={"household_id": 207, "days_back": 30, "anchor_date": "2025-09-07"}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 207, "anchor_date": "2025-09-07"}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "sections_populated", "payload_json": {"sections": True}}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "overlap_evaluated", "payload_json": {"anchor_date": "2025-09-07", "peanut_free": True}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_075",
  instruction=(
    "You have to produce a seven-night Dinner plan for the Garcia Household (household_id 208) for 2025-09-15 through 2025-09-21 using exactly recipes 401, 402, 425, 427, 428, 431, 433 in that order, and provide a linked grocery list. Verify availability at Budget Foods Express (store_id 9004), then create a draft delivery order for 2025-09-16T18:00:00Z–20:00:00Z associated with that list (order population with items is not required). Audit meal plan creation, list creation, and order creation. Acceptance: one plan with seven entries on the specified dates in the specified order; one linked list; availability checked at store 9004; one draft order exists for the stated slot; audits exist for meal plan creation, list creation, and order creation."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 208}),
    Action(name="get_user_by_id", kwargs={"user_id": 108}),
    Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2025-09-15", "created_by_user_id": 108}),
    Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-15"}}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-15", "selected_recipe_ids_json": "[401,402,425,427,428,431,433]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 208, "source_meal_plan_id": 6003, "created_by_user_id": 108, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,402,425,427,428,431,433]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9004}),
    Action(name="create_order_from_list", kwargs={"household_id": 208, "store_id": 9004, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-16T18:00:00Z", "scheduled_slot_end_ts": "2025-09-16T20:00:00Z"}),
    Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"store_id": 9004}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_076",
  instruction=(
    "You have to assemble a combined Breakfast & Snacks grocery list for the Patel Extended Family (household_id 205) using exactly recipes 441, 444, 445. The list must aggregate items, categorize by grocery section, mark pantry-staple flags, and reflect 30-day overlap as of 2025-09-07. Set the list to 'ready' and record audits for creation, overlap evaluation, and readiness. Acceptance: one list using exactly those three recipes; sections and pantry flags present; overlap flags reflect the last 30 days up to 2025-09-07; final status 'ready'; audits exist for creation, overlap evaluation, and readiness."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 205}),
    Action(name="get_user_by_id", kwargs={"user_id": 105}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 205, "created_by_user_id": 105, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[441,444,445]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="list_recent_meal_history", kwargs={"household_id": 205, "days_back": 30, "anchor_date": "2025-09-07"}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 205, "anchor_date": "2025-09-07"}),
    Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "overlap_evaluated", "payload_json": {"anchor_date": "2025-09-07"}}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"from": "initialized", "to": "ready"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_077",
  instruction=(
    "You have to plan a weekend brunch set for the Kim-Smith Family (household_id 209) anchored to 2025-09-13 using exactly recipes 432, 435, 408 in that order. Provide one linked grocery list with aggregated items, correct grocery sections, pantry-staple flags, and last-30-day overlap as of 2025-09-07. Keep the list in 'initialized' and audit creation and overlap evaluation. Acceptance: one plan anchored to 2025-09-13 with three entries in the stated order; one linked list with sections, pantry flags, and correct overlap flags; status remains 'initialized'; audits exist for creation and overlap evaluation."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 209}),
    Action(name="get_user_by_id", kwargs={"user_id": 109}),
    Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2025-09-13", "created_by_user_id": 109}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-13", "selected_recipe_ids_json": "[432,435,408]"}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 209, "source_meal_plan_id": 6003, "created_by_user_id": 109, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[432,435,408]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="list_recent_meal_history", kwargs={"household_id": 209, "days_back": 30, "anchor_date": "2025-09-07"}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2025-09-07"}),
    Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "overlap_evaluated", "payload_json": {"anchor_date": "2025-09-07"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_078",
  instruction=(
    "You have to create a single-store, peanut-safe school-lunch draft order for the Williams-Brown Family (household_id 204) based on exactly Lunch recipes 409, 410, 411, 412, 413 at FreshMart Online (store_id 9001). Use a dedicated grocery list with aggregated items, correct grocery sections, and pantry-staple flags. Generate a draft delivery order for 2025-09-05T10:00:00Z–12:00:00Z associated with that list (item population is not required). Audit list creation and order creation, and record a peanut-free verification note. Acceptance: one list with those five Lunch recipes; sections and pantry flags present; one draft order exists for the stated slot at store 9001; audits exist for list creation, order creation, and a peanut-free verification note."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 204}),
    Action(name="get_user_by_id", kwargs={"user_id": 104}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 204, "created_by_user_id": 104, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,411,412,413]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="create_order_from_list", kwargs={"household_id": 204, "store_id": 9001, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-05T10:00:00Z", "scheduled_slot_end_ts": "2025-09-05T12:00:00Z"}),
    Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"store_id": 9001}}),
    Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "order", "entity_id": 10003, "action_enum": "policy_checked", "payload_json": {"peanut_free": True}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_079",
  instruction=(
    "You create a standalone grocery list for the household “Chen Solo” (household_id=203) under created_by_user_id=103, aggregated from exactly these peanut-free lunch recipes: [409, 410, 444]. Success means one new grocery_lists row for that household with items equal to the aggregate of those recipes (no duplicate ingredient entries), grocery_section values populated, status set to “finalized,” and a single audit recording list creation. Return the new list_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":203}),
    Action(name="get_user_by_id", kwargs={"user_id":103}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":203, "created_by_user_id":103}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003, "recipe_ids_json":"[409,410,444]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
    Action(name="set_grocery_list_status", kwargs={"list_id":8003, "status_enum":"finalized"}),
    Action(name="log_audit_event", kwargs={"household_id":203, "user_id":103, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"created"})
  ],
  outputs=[
    "8003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_080",
  instruction=(
    "You deliver a dinner-only grocery outcome for the household “Johnson Large Family” (household_id=207) using exactly these recipes: [401, 402, 405, 406], acting under created_by_user_id=107. The result must satisfy policy for store 9004 by addressing any unavailable items with allowed in-catalog alternatives, and conclude with a finalized list. Success is one grocery list for that household whose items equal the aggregate of those recipes (no duplicate ingredient/unit rows), sections are consistent with the catalog, any initially unavailable items are resolved by valid substitutes when required, and the list is finalized. Do not place an order."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":207}),
    Action(name="get_user_by_id", kwargs={"user_id":107}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":207, "created_by_user_id":107}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003, "recipe_ids_json":"[401,402,405,406]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id":8003, "store_id":9004}),
    Action(name="propose_substitute_products", kwargs={
      "store_id":9004,
      "flagged_items":[
        {"item_id":8115,"ingredient_id":1012},
        {"item_id":8116,"ingredient_id":1010},
        {"item_id":8117,"ingredient_id":1011},
        {"item_id":8118,"ingredient_id":1015},
        {"item_id":8119,"ingredient_id":1016},
        {"item_id":8120,"ingredient_id":1017},
        {"item_id":8121,"ingredient_id":1001},
        {"item_id":8122,"ingredient_id":1008},
        {"item_id":8123,"ingredient_id":1019},
        {"item_id":8124,"ingredient_id":1018},
        {"item_id":8125,"ingredient_id":1013},
        {"item_id":8126,"ingredient_id":1024},
        {"item_id":8127,"ingredient_id":1003},
        {"item_id":8128,"ingredient_id":1021},
        {"item_id":8129,"ingredient_id":1006},
        {"item_id":8130,"ingredient_id":1009},
        {"item_id":8131,"ingredient_id":1007},
        {"item_id":8132,"ingredient_id":1014},
        {"item_id":8133,"ingredient_id":1022}
      ]
    }),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id":8003, "substitutions":[]}),
    Action(name="set_grocery_list_status", kwargs={"list_id":8003, "status_enum":"finalized"}),
    Action(name="log_audit_event", kwargs={"household_id":207, "user_id":107, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"created"}),
    Action(name="log_audit_event", kwargs={"household_id":207, "user_id":107, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"finalized"})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_081",
  instruction=(
    "You create a pantry-first restock list for the “Patel Extended Family” (household_id=205) under created_by_user_id=105 by keeping only the recipes from [441, 444, 446, 447] that have ≤2 non-staple ingredients and aggregating the kept set into a single list. Success means exactly one list for that household derived from the kept recipes, last-30-days overlap flags computed with anchor_date=2025-08-31, and the list marked “finalized.” Do not evaluate store inventory or place an order."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":205}),
    Action(name="get_user_by_id", kwargs={"user_id":105}),
    Action(name="minimize_new_ingredients", kwargs={"recipe_ids_json":"[441,444,446,447]", "max_new_ingredients_per_recipe":2}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":205, "created_by_user_id":105}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003, "recipe_ids_json":"[447]"}),
    Action(name="log_audit_event", kwargs={"household_id":205, "user_id":105, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"created"}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id":8003, "household_id":205, "anchor_date":"2025-08-31"}),
    Action(name="set_grocery_list_status", kwargs={"list_id":8003, "status_enum":"finalized"}),
    Action(name="log_audit_event", kwargs={"household_id":205, "user_id":105, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"finalized"})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_082",
  instruction=(
    "You have to create a dedicated Dinner grocery list for the Kim-Smith Family (household_id 209) from recipes [423, 424, 426], leave it in status 'ready', and record an audit of the update. Acceptance: one grocery list exists for household 209 with aggregated items from those recipes, status 'ready', and an audit exists for the update. Return the created list_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 209}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 209, "created_by_user_id": 109, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[423,424,426]"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 209,
        "user_id": 109,
        "entity_type": "grocery_lists",
        "entity_id": 8003,
        "action_enum": "update",
        "payload_json": {"status": "ready"}
      }
    ),
  ],
  outputs=[
    "8003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_083",
  instruction=(
    "You prepare a peanut-free school-lunch pack for the “Kim-Smith Family” (household_id=209) under created_by_user_id=109 using exactly these five lunches: [409, 410, 411, 442, 444]. Success is one new grocery list for that household combining those lunches, with recent-overlap annotations at anchor_date=2025-08-31, sections categorized, and an availability scan at store_id=9006 that yields peanut-free substitution proposals (do not apply them)."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":209}),
    Action(name="get_user_by_id", kwargs={"user_id":109}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":209, "created_by_user_id":109}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003, "recipe_ids_json":"[409,410,411,442,444]"}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id":8003, "household_id":209, "anchor_date":"2025-08-31"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id":8003, "store_id":9006}),
    Action(name="propose_substitute_products", kwargs={
      "store_id":9006,
      "flagged_items":[
        {"ingredient_id":1007},{"ingredient_id":1009},{"ingredient_id":1013},
        {"ingredient_id":1014},{"ingredient_id":1024},{"ingredient_id":1026},
        {"ingredient_id":1038},{"ingredient_id":1039},{"ingredient_id":1040},
        {"ingredient_id":1043},{"ingredient_id":1044},{"ingredient_id":1070},
        {"ingredient_id":1090}
      ],
      "require_peanut_free":True
    })
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_084",
  instruction=(
    "You build a three-dinner grocery list for the “Kowalski Couple” (household_id=206) under created_by_user_id=106 from exactly these recipes: [431, 433, 435]. Success means one new list for that household aggregated from those dinners, pantry staples flagged and grocery sections populated, the list marked “finalized,” and a single audit recording finalization."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id":206}),
    Action(name="get_user_by_id", kwargs={"user_id":106}),
    Action(name="create_empty_grocery_list", kwargs={"household_id":206, "created_by_user_id":106}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003, "recipe_ids_json":"[431,433,435]"}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id":8003}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
    Action(name="set_grocery_list_status", kwargs={"list_id":8003, "status_enum":"finalized"}),
    Action(name="log_audit_event", kwargs={"household_id":206, "user_id":106, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"finalized"})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_085",
  instruction=(
    "You will create a fixed 3-night Dinner mini-plan for the Kowalski Couple (household_id 206) spanning 2025-09-12 to 2025-09-14 using the exact recipe IDs in order: 434, 432, 431. Acceptance: one meal plan exists with three Dinner entries on those dates in that order; an audit exists recording the meal plan’s creation with week_start_date 2025-09-12."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 206}),
    Action(name="get_user_by_id", kwargs={"user_id": 106}),
    Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2025-09-12", "created_by_user_id": 106}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-12", "selected_recipe_ids_json": "[434,432,431]"}),
    Action(name="log_audit_event", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-12"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_086",
  instruction=(
    "You will assemble a dedicated grocery list for the Kowalski Couple (household_id 206) from exactly these two Dinner recipe IDs: 431 and 402. Keep the list in 'initialized' status. Acceptance: one grocery list exists for household 206 with items aggregated strictly from those recipes; grocery sections are populated; pantry-staple flags are set; an audit exists capturing list creation with source 'recipes' and status 'initialized'."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 206}),
    Action(name="get_user_by_id", kwargs={"user_id": 106}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 206, "created_by_user_id": 106, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[431,402]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="log_audit_event", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"source": "recipes", "status": "initialized"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_087",
  instruction=(
    "You will prepare a peanut-free school-lunch pack for the Garcia Household (household_id 208) using exactly these Lunch recipe IDs: 409 and 413. First check GrocerDash (store_id 9002) availability for the list, then propose peanut-free substitutes for any unavailable items; do not update the list with them. Acceptance: one grocery list exists in 'initialized' status aggregated strictly from those recipes; store availability has been checked at store_id 9002; a peanut-free substitution proposal is generated; and an audit exists noting a substitution proposal event."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 208}),
    Action(name="get_user_by_id", kwargs={"user_id": 108}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 208, "created_by_user_id": 108, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,413]"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(
      name="propose_substitute_products",
      kwargs={
        "store_id": 9002,
        "flagged_items": [
          {"ingredient_id": 1024},
          {"ingredient_id": 1013},
          {"ingredient_id": 1023},
          {"ingredient_id": 1035}
        ],
        "require_peanut_free": True
      }
    ),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 208,
        "user_id": 108,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "substitution_proposed",
        "payload_json": {
          "peanut_free": True,
          "store_id": 9002,
          "flagged_ingredient_ids": [1024, 1013, 1023, 1035]
        }
      }
    ),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_088",
  instruction=(
    "Using the Alvarez Household’s existing weekday list (list_id 8002), you will open a draft delivery order at GrocerDash (store_id 9002) for slot 2025-09-03T16:00:00Z–2025-09-03T18:00:00Z, add all available items at the lowest price from that store, and record an audit of order creation. Leave the order as draft. Acceptance: one draft order is created for household_id 202 linked to list_id 8002 with items added; an audit exists reflecting order creation in 'draft'."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 202}),
    Action(name="create_order_from_list", kwargs={"household_id": 202, "store_id": 9002, "list_id": 8002, "scheduled_slot_start_ts": "2025-09-03T16:00:00Z", "scheduled_slot_end_ts": "2025-09-03T18:00:00Z"}),
    Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9002}),
    Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"status": "draft"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_089",
  instruction=(
    "You will create a 4-night Dinner plan for the Johnson Large Family (household_id 207) for 2025-09-08 through 2025-09-11 using these exact recipes in order: 401, 402, 406, 425, and set each entry’s note to include exactly: \"Child-friendly: mild seasoning; cut to bite-size; soft textures.\" Acceptance: one meal plan exists with four Dinner entries on those dates in the specified order; each entry’s note includes that exact child-friendly text; an audit exists recording the meal plan’s creation with week_start_date 2025-09-08."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 207}),
    Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2025-09-08", "created_by_user_id": 107}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[401,402,406,425]"}),
    Action(name="update_meal_plan_entry_notes", kwargs={"meal_plan_id": 6003, "notes_map": {"401": "Child-friendly: mild seasoning; cut to bite-size; soft textures.", "402": "Child-friendly: mild seasoning; cut to bite-size; soft textures.", "406": "Child-friendly: mild seasoning; cut to bite-size; soft textures.", "425": "Child-friendly: mild seasoning; cut to bite-size; soft textures."}}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-08"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_090",
  instruction=(
    "You will create a grocery list for the Alvarez Household (household_id 202) from exactly these Dinner recipe IDs: 425 and 427; keep the list in 'initialized' status (created_by_user_id 102); compute 30-day overlap flags using 2025-09-07 as the anchor; and populate grocery sections. Acceptance: one grocery list exists with items aggregated strictly from those recipes; overlap_last_month flags reflect anchor 2025-09-07; grocery sections are populated; an audit exists reflecting the list update with the stated anchor."
  ),
  actions=[
    Action(name="create_empty_grocery_list", kwargs={"household_id": 202, "created_by_user_id": 102, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[425,427]"}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 202, "anchor_date": "2025-09-07"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 202,
        "user_id": 102,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "updated",
        "payload_json": {"overlap_anchor": "2025-09-07"}
      }
    ),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_091",
  instruction=(
    "You deliver a single finalized grocery list for the household “Chen Solo” (household_id=203), created by user_id=103 and sourced only from recipes [401, 402]. Success means exactly one new list exists for that household, is finalized, and is policy-compliant with rules.py hygiene at anchor_date=2025-08-31. Do not create any order."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 203}),
    Action(name="get_user_by_id", kwargs={"user_id": 103}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 203, "source_meal_plan_id": None, "created_by_user_id": 103, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "grocery_list_created", "created_at": "2025-08-31T00:00:00Z", "payload_json": {"source_recipes": [401, 402], "anchor_date": "2025-08-31"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,402]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 203, "anchor_date": "2025-08-31"}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "finalized"}),
    Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "grocery_list_finalized", "created_at": "2025-08-31T00:00:00Z", "payload_json": {"status": "finalized", "anchor_date": "2025-08-31"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_092",
  instruction=(
    "You compile a peanut-free school-lunch grocery list for the “Johnson Large Family” (household_id=207) under created_by_user_id=107 from exactly these lunch recipes: [409, 410, 411, 412, 413]. Success means one new list for that household is policy-compliant and peanut-free at the ingredient level (validated from the recipes’ ingredient rows), is not linked to any meal plan (source_meal_plan_id=None), initializes with status 'initialized', last-30-day overlap is evaluated at anchor_date=2025-09-01, availability is checked at store_id=9001, and no order is created or updated."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 207}),
    Action(name="get_user_by_id", kwargs={"user_id": 107}),
    Action(name="list_recipe_ingredients", kwargs={"recipe_id": 409}),
    Action(name="list_recipe_ingredients", kwargs={"recipe_id": 410}),
    Action(name="list_recipe_ingredients", kwargs={"recipe_id": 411}),
    Action(name="list_recipe_ingredients", kwargs={"recipe_id": 412}),
    Action(name="list_recipe_ingredients", kwargs={"recipe_id": 413}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 207, "source_meal_plan_id": None, "created_by_user_id": 107, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "grocery_list_created", "created_at": "2025-09-01T00:00:00Z", "payload_json": {"source_recipes": [409, 410, 411, 412, 413], "peanut_free_validated": True, "anchor_date": "2025-09-01"}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,411,412,413]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 207, "anchor_date": "2025-09-01"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9001}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_093",
  instruction=(
    "You prepare a budget-store pickup shell order for the “Garcia Household” (household_id=208) using a new list by user_id=108 from recipes [401, 405]. Success means a policy-compliant list exists for that household; availability is evaluated at store_id=9004 with an in-store substitution review where the catalog lacks items; a draft order for 2025-09-02T10:00:00Z–12:00:00Z is created for that store; no order items are added; and audit logs record the list creation and order creation. The order remains a draft."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 208}),
    Action(name="get_user_by_id", kwargs={"user_id": 108}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 208, "source_meal_plan_id": None, "created_by_user_id": 108, "status_enum": "initialized"}),
    Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "grocery_list_created", "payload_json": {"source_recipes": [401, 405]}}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,405]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9004}),
    Action(name="propose_substitute_products", kwargs={"store_id": 9004, "flagged_items": [{"ingredient_id": 1003}, {"ingredient_id": 1006}, {"ingredient_id": 1009}, {"ingredient_id": 1010}, {"ingredient_id": 1011}, {"ingredient_id": 1012}, {"ingredient_id": 1015}, {"ingredient_id": 1016}, {"ingredient_id": 1017}, {"ingredient_id": 1021}], "require_peanut_free": False}),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id": 8003, "substitutions": []}),
    Action(name="create_order_from_list", kwargs={"household_id": 208, "store_id": 9004, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-02T10:00:00Z", "scheduled_slot_end_ts": "2025-09-02T12:00:00Z"}),
    Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "order", "entity_id": 10003, "action_enum": "order_created", "payload_json": {"store_id": 9004, "list_id": 8003, "slot": ["2025-09-02T10:00:00Z", "2025-09-02T12:00:00Z"]}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_094",
  instruction=(
    "You deliver a seven-night Dinner plan for the household “Johnson Large Family” (household_id=207) for the week starting 2025-09-08 under user_id=107, using exactly these recipes: [401, 402, 403, 404, 405, 406, 407]. Success means exactly one meal_plan exists for that week with seven Dinner entries for those recipes, and each entry’s note equals exactly: “Child-note v1: mild seasoning; cut to bite-size; soft textures.” No grocery list or order is produced."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 207}),
    Action(name="get_user_by_id", kwargs={"user_id": 107}),
    Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2025-09-08", "created_by_user_id": 107}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "meal_plan_created", "payload_json": {"week_start_date": "2025-09-08"}}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[401,402,403,404,405,406,407]"}),
    Action(name="update_meal_plan_entry_notes", kwargs={"meal_plan_id": 6003, "notes_map": {"401": "Child-note v1: mild seasoning; cut to bite-size; soft textures.", "402": "Child-note v1: mild seasoning; cut to bite-size; soft textures.", "403": "Child-note v1: mild seasoning; cut to bite-size; soft textures.", "404": "Child-note v1: mild seasoning; cut to bite-size; soft textures.", "405": "Child-note v1: mild seasoning; cut to bite-size; soft textures.", "406": "Child-note v1: mild seasoning; cut to bite-size; soft textures.", "407": "Child-note v1: mild seasoning; cut to bite-size; soft textures."}}),
    Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "meal_plan_entries_added", "payload_json": {"count": 7}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_095",
  instruction=(
    "You place a single new order for the “Alvarez Household” (household_id=202) from the existing grocery list list_id=8002 at store_id=9002 for 2025-09-03T16:00:00Z–18:00:00Z. Success means the order is created from that list, items are selected per policy, the order status is placed, the source list status becomes ordered, and audit logs record the order creation, item population, status change, and list update."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 202}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8002, "store_id": 9002}),
    Action(name="create_order_from_list", kwargs={"household_id": 202, "store_id": 9002, "list_id": 8002, "scheduled_slot_start_ts": "2025-09-03T16:00:00Z", "scheduled_slot_end_ts": "2025-09-03T18:00:00Z"}),
    Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "order", "entity_id": 10003, "action_enum": "order_created", "payload_json": {"store_id": 9002, "list_id": 8002, "slot": ["2025-09-03T16:00:00Z", "2025-09-03T18:00:00Z"]}}),
    Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9002}),
    Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "order", "entity_id": 10003, "action_enum": "order_items_added", "payload_json": {"source_list_id": 8002}}),
    Action(name="update_order_status", kwargs={"order_id": 10003, "new_status": "placed"}),
    Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "order", "entity_id": 10003, "action_enum": "order_placed", "payload_json": {"status": "placed"}}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8002, "status_enum": "ordered"}),
    Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8002, "action_enum": "grocery_list_ordered", "payload_json": {"status": "ordered", "linked_order_id": 10003}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_096",
  instruction=(
    "You prepare a peanut-free school-lunch list with a substitution review for the “Alvarez Household” (household_id=202) under created_by_user_id=102 from exactly these recipes: [409, 413]. Success means one new list aggregated from those recipes; store availability checked at store_id=9002; a substitution pass run that honors peanut-free rules and leaves items unchanged when no in-store substitutes exist; no order is created and the list remains in its initial state."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 202}),
    Action(name="get_user_by_id", kwargs={"user_id": 102}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 202, "source_meal_plan_id": None, "created_by_user_id": 102, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,413]"}),
    Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(
      name="propose_substitute_products",
      kwargs={
        "store_id": 9002,
        "flagged_items": [
          {"ingredient_id": 1013},
          {"ingredient_id": 1023},
          {"ingredient_id": 1024},
          {"ingredient_id": 1035}
        ],
        "require_peanut_free": True
      },
    ),
    Action(name="update_grocery_list_with_substitutes", kwargs={"list_id": 8003, "substitutions": []}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_097",
  instruction=(
    "You will create a categorized Dinner grocery list for the Mercer Family (household_id 201) using exactly recipes [403, 405]. You will not create a meal plan. You will leave the list in its default status and record an audit for grocery-list creation. Acceptance: one new grocery list linked to household 201 with items aggregated from those recipes, grocery sections filled, pantry-staple flags set per policy, and an audit reflecting the list’s initialized state. Return the new grocery_list_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 201}),
    Action(name="get_user_by_id", kwargs={"user_id": 101}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 201, "created_by_user_id": 101, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[403,405]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 201,
        "user_id": 101,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "created",
        "payload_json": {"status": "initialized"},
      },
    ),
  ],
  outputs=[
    "8003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_098",
  instruction=(
    "You will set up a 7-day Dinner rotation for Chen Solo (household_id 203) for the week starting 2025-09-08 using recipes [431, 432, 434] in that order across the week’s seven days. You will append the fixed child-friendly text \"Child-friendly: mild seasoning; cut to bite-size; soft textures.\" to those entries, and you will record an audit for meal-plan creation. Acceptance: one meal plan for household 203 exists for week_start_date 2025-09-08 with seven Dinner entries following the rotation, and each of those entries has the appended child-friendly note. Return the created meal_plan_id."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 203}),
    Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-08", "created_by_user_id": 103}),
    Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[431,432,434,431,432,434,431]"}),
    Action(name="update_meal_plan_entry_notes", kwargs={
      "meal_plan_id": 6003,
      "notes_map": {
        "431": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
        "432": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
        "434": "Child-friendly: mild seasoning; cut to bite-size; soft textures."
      }
    }),
    Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-08"}}),
  ],
  outputs=[
    "6003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_099",
  instruction=(
    "You will create a Breakfast-focused grocery list for Thompson Retirement (household_id 210) using exactly recipes [418, 419], categorize the list, set the list status to \"ready,\" and record an audit reflecting the list’s \"ready\" state. Acceptance: one new grocery list for household 210 with aggregated items, sections populated, status \"ready,\" and a corresponding audit entry. Return the final list status string."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 210}),
    Action(name="create_empty_grocery_list", kwargs={"household_id": 210, "created_by_user_id": 110, "status_enum": "initialized"}),
    Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[418,419]"}),
    Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
    Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="log_audit_event", kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "status_updated"}),
    Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
  ],
  outputs=[
    "ready"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_100",
  instruction=(
    "You will use the existing grocery list 8001 (household_id 201) to create a draft delivery order at FreshMart Online (store_id 9001) for 2025-09-05T09:00:00Z–2025-09-05T11:00:00Z and populate items at the lowest price available in that store, then record an audit for order creation. Acceptance: one new draft order for list 8001 at store 9001 with lowest-price items added and a creation audit. Return the new order_id and the final total_cents."
  ),
  actions=[
    Action(name="get_household_by_id", kwargs={"household_id": 201}),
    Action(
      name="create_order_from_list",
      kwargs={
        "household_id": 201,
        "store_id": 9001,
        "list_id": 8001,
        "scheduled_slot_start_ts": "2025-09-05T09:00:00Z",
        "scheduled_slot_end_ts": "2025-09-05T11:00:00Z",
      },
    ),
    Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9001}),
    Action(
      name="log_audit_event",
      kwargs={
        "household_id": 201,
        "user_id": 101,
        "entity_type": "order",
        "entity_id": 10003,
        "action_enum": "created",
        "payload_json": {"status": "draft"},
      },
    ),
  ],
  outputs=[
    "10003",
    "2196"
  ]
),


# Task(
#   annotator="saaish2",
#   user_id="task_000",
#   instruction=(
#     "You are planning a compact 3-dinner mini-plan for the Chen Solo household (household_id=203) for the week starting 2025-09-01. "
#     "Acceptance criteria (deterministic terminal state): "
#     "1) Exactly one new meal plan exists for that week and household. "
#     "2) The plan has three Dinner entries using protein-forward, peanut-free recipes [402, 404, 407]. "
#     "3) One grocery list exists for that plan; items are aggregated from those recipes, sections categorized, pantry flags set; list status is left as 'initialized' and readiness is noted via audit. "
#     "4) Log audits for the meal plan creation and the grocery list creation using deterministic payloads. "
#     "Return the new grocery_list_id."
#   ),
#   actions=[
#     Action(name="get_household_by_id", kwargs={"household_id": 203}),
#     Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-01", "created_by_user_id": 103}),
#     Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[402,404,407]"}),
#     Action(name="create_empty_grocery_list", kwargs={"household_id": 203, "created_by_user_id": 103, "source_meal_plan_id": 6003, "status_enum": "initialized"}),
#     Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,404,407]"}),
#     Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
#     Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
#     Action(
#       name="log_audit_event",
#       kwargs={
#         "household_id": 203,
#         "user_id": 103,
#         "entity_type": "meal_plans",
#         "entity_id": 6003,
#         "action_enum": "create",
#         "payload_json": {"week_start_date": "2025-09-01"},
#       },
#     ),
#     Action(
#       name="log_audit_event",
#       kwargs={
#         "household_id": 203,
#         "user_id": 103,
#         "entity_type": "grocery_lists",
#         "entity_id": 8003,
#         "action_enum": "create",
#         "payload_json": {"source_meal_plan_id": 6003},
#       },
#     ),
#   ],
#   outputs=[
#     "8003"
#   ]
# ),


# Task(
#   annotator="saaish2",
#   user_id="task_000",
#   instruction=(
#     "You are producing a full 7-dinner, child-friendly plan for the Williams-Brown Family (household_id=204) for the week starting 2025-09-01 and placing a FreshMart Online (store_id=9001) order. "
#     "Acceptance criteria: "
#     "1) One new meal plan exists for that week with Dinner entries using recipes [402, 404, 405, 407, 408, 423, 427]. "
#     "2) Child-friendly notes are applied to all new entries using the deterministic template. "
#     "3) A grocery list is created from those recipes; sections and pantry flags are set; 30-day overlap flags computed with anchor_date=2025-08-31; list status set to 'ready'. "
#     "4) In-store availability is checked at store_id=9001; suggested substitutes are applied where available; an order is created for 2025-09-03T18:00:00Z–20:00:00Z, items added at lowest price, order status set to 'placed', and the list status set to 'ordered'. "
#     "5) Audit the plan creation, list creation, order placement, and list status update. "
#     "Return the list of created meal_plan entry_ids in ascending order."
#   ),
#   actions=[
#     Action(name="get_household_by_id", kwargs={"household_id": 204}),
#     Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2025-09-01", "created_by_user_id": 104}),
#     Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[402,404,405,407,408,423,427]"}),
#     Action(name="generate_child_modifications", kwargs={"recipe_ids_json": "[402,404,405,407,408,423,427]"}),
#     Action(
#       name="update_meal_plan_entry_notes",
#       kwargs={
#         "meal_plan_id": 6003,
#         "notes_map": {
#           "402":"Child-friendly: mild seasoning; cut to bite-size; soft textures.",
#           "404":"Child-friendly: mild seasoning; cut to bite-size; soft textures.",
#           "405":"Child-friendly: mild seasoning; cut to bite-size; soft textures.",
#           "407":"Child-friendly: mild seasoning; cut to bite-size; soft textures.",
#           "408":"Child-friendly: mild seasoning; cut to bite-size; soft textures.",
#           "423":"Child-friendly: mild seasoning; cut to bite-size; soft textures.",
#           "427":"Child-friendly: mild seasoning; cut to bite-size; soft textures."
#         }
#       },
#     ),
#     Action(name="create_empty_grocery_list", kwargs={"household_id": 204, "created_by_user_id": 104, "source_meal_plan_id": 6003, "status_enum": "initialized"}),
#     Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,404,405,407,408,423,427]"}),
#     Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
#     Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
#     Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 204, "anchor_date": "2025-08-31"}),
#     Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
#     Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9001}),
#     # Flag only ingredients that were out_of_stock in the inventory check at 9001 (deterministic: [1002]).
#     Action(
#       name="propose_substitute_products",
#       kwargs={
#         "store_id": 9001,
#         "flagged_items": [{"ingredient_id": 1002}],
#         "require_peanut_free": False
#       },
#     ),
#     # No viable substitutions available at this store for the flagged item; apply none.
#     Action(
#       name="update_grocery_list_with_substitutes",
#       kwargs={"list_id": 8003, "substitutions": []},
#     ),
#     Action(
#       name="create_order_from_list",
#       kwargs={
#         "household_id": 204,
#         "store_id": 9001,
#         "list_id": 8003,
#         "scheduled_slot_start_ts": "2025-09-03T18:00:00Z",
#         "scheduled_slot_end_ts": "2025-09-03T20:00:00Z",
#       },
#     ),
#     Action(name="add_order_items_from_list", kwargs={"order_id": 10003, "store_id": 9001}),
#     Action(name="update_order_status", kwargs={"order_id": 10003, "new_status": "placed"}),
#     Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ordered"}),
#     Action(
#       name="log_audit_event",
#       kwargs={
#         "household_id": 204,
#         "user_id": 104,
#         "entity_type": "meal_plans",
#         "entity_id": 6003,
#         "action_enum": "create",
#         "payload_json": {"week_start_date": "2025-09-01"},
#       },
#     ),
#     Action(
#       name="log_audit_event",
#       kwargs={
#         "household_id": 204,
#         "user_id": 104,
#         "entity_type": "grocery_lists",
#         "entity_id": 8003,
#         "action_enum": "create",
#         "payload_json": {"source_meal_plan_id": 6003},
#       },
#     ),
#     Action(
#       name="log_audit_event",
#       kwargs={
#         "household_id": 204,
#         "user_id": 104,
#         "entity_type": "orders",
#         "entity_id": 10003,
#         "action_enum": "placed",
#         "payload_json": {"list_id": 8003, "store_id": 9001},
#       },
#     ),
#     Action(
#       name="log_audit_event",
#       kwargs={
#         "household_id": 204,
#         "user_id": 104,
#         "entity_type": "grocery_lists",
#         "entity_id": 8003,
#         "action_enum": "status_update",
#         "payload_json": {"status_enum": "ordered"},
#       },
#     ),
#   ],
#   outputs=[
#     "6118","6119","6120","6121","6122","6123","6124"
#   ]
# ),

# Task(
#   annotator="saaish2",
#   user_id="task_000",
#   instruction=(
#     "You will create a peanut-free 3-day school-lunch plan for the Kim-Smith Family anchored to the week starting 2025-09-01. Use recipes with ≥20 g protein per serving and, when more than three qualify, pick the top three by protein; break any remaining ties by lower prep_minutes, then lower recipe_id. Build a dedicated grocery list from those three lunches, categorize by store section, flag pantry staples and 30-day overlaps using 2025-08-30 as the anchor, set the list status to 'ready', and record audits for meal plan creation and grocery list creation/finalization. Accept when the lunch plan exists, the list aggregates exactly those lunches, the status is 'ready', and the audits are recorded."
#   ),
#   actions=[
#     Action(name="get_household_by_id", kwargs={"household_id": 209}),
#     Action(name="get_user_by_id", kwargs={"user_id": 109}),
#     Action(name="build_recipe_filters", kwargs={"meal_type": "Lunch", "min_protein_g": 20, "peanut_free": True, "cuisines_exclude": []}),
#     Action(name="list_recipes_by_filters", kwargs={"filter_token": "F:Lunch:P20:PF1:EX"}),
#     Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2025-09-01", "created_by_user_id": 109}),
#     Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[445, 443, 409]"}),
#     Action(name="create_empty_grocery_list", kwargs={"household_id": 209, "source_meal_plan_id": 6003, "created_by_user_id": 109, "status_enum": "initialized"}),
#     Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[445, 443, 409]"}),
#     Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
#     Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
#     Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2025-08-30"}),
#     Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "ready"}),
#     Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-01"}}),
#     Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"source_meal_plan_id": 6003}}),
#     Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "finalized", "payload_json": {"status": "ready"}})
#   ],
#   outputs=[]
# ),

# Task(
#   annotator="saaish2",
#   user_id="task_000",
#   instruction=(
#     "You manage weekly dinners for the Mercer Family (household_id 201). Create a new meal plan for the week of 2025-09-01 with exactly three peanut-free Dinner entries on 2025-09-01 through 2025-09-03, each providing at least 22g protein and avoiding any dinners this household cooked from 2025-08-01 to 2025-08-20. Use targets 2200 kcal and 120g protein to choose recipes. Success means: one new meal_plan for that week tied to three Dinner entries dated 2025-09-01..2025-09-03, and one new grocery_list linked to the plan with items equal to the aggregated recipe ingredients, categorized by section, and status='finalized', plus one audit row for that list."
#   ),
#   actions=[
#     Action(name="get_household_by_id", kwargs={"household_id": 201}),
#     Action(name="build_recipe_filters", kwargs={"meal_type": "Dinner", "min_protein_g": 22, "peanut_free": True, "cuisines_exclude": []}),
#     # Known deterministic token for this filter
#     Action(name="list_recipes_by_filters", kwargs={"filter_token": "F:Dinner:P22:PF1:EX"}),
#     # Deterministic 20-day window ending 2025-08-20
#     Action(name="list_recent_meal_history", kwargs={"household_id": 201, "days_back": 20, "anchor_date": "2025-08-20"}),
#     # Exclude ALL recent recipe_ids intersecting the candidate list (404,405,407 were recent)
#     Action(name="exclude_recipe_ids", kwargs={
#       "candidate_recipe_ids_json": "[402, 404, 405, 407, 423, 425, 427, 428, 429, 434, 435]",
#       "exclude_recipe_ids": [404, 405, 407]
#     }),
#     # Rank strictly over the exclude output; pick 3 by stated targets
#     Action(name="rank_recipes_for_targets", kwargs={
#       "recipe_ids_json": "[402, 423, 425, 427, 428, 429, 434, 435]",
#       "needed_count": 3,
#       "target_calories": 2200,
#       "target_protein": 120
#     }),
#     Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2025-09-01", "created_by_user_id": 101}),
#     # Use exactly the three selected in the previous step
#     Action(name="bulk_add_meal_plan_entries", kwargs={
#       "meal_plan_id": 6003,
#       "week_start_date": "2025-09-01",
#       "selected_recipe_ids_json": "[425, 423, 435]"
#     }),
#     Action(name="create_empty_grocery_list", kwargs={"household_id": 201, "source_meal_plan_id": 6003, "created_by_user_id": 101, "status_enum": "initialized"}),
#     Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[425, 423, 435]"}),
#     Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
#     Action(name="set_grocery_list_status", kwargs={"list_id": 8003, "status_enum": "finalized"}),
#     Action(name="log_audit_event", kwargs={
#       "household_id": 201, "user_id": 101,
#       "entity_type": "grocery_list", "entity_id": 8003,
#       "action_enum": "finalized",
#       "payload_json": {"source_meal_plan_id": 6003, "status": "finalized"}
#     }),
#   ],
#   outputs=[]
# ),

# Task(
#   annotator="saaish2",
#   user_id="task_000",
#   instruction=(
#     "You will plan a full 7-night Dinner week for the Mercer Family for the exact week starting 2025-09-01 using exactly these seven Dinner recipe IDs: 402, 423, 425, 427, 428, 429, 430. Apply the single fixed child-note template to every entry. Keep servings at defaults. Acceptance: the week is populated for all seven days under one new meal plan; each entry has exactly the fixed child-note template (and nothing else); no store or ordering changes."
#   ),
#   actions=[
#     Action(name="get_household_by_id", kwargs={"household_id": 201}),
#     Action(name="get_user_by_id", kwargs={"user_id": 101}),
#     Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2025-09-01", "created_by_user_id": 101}),
#     Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[402,423,425,427,428,429,430]"}),
#     # Apply one deterministic, fixed template string to every entry (no extra prose):
#     Action(
#       name="update_meal_plan_entry_notes",
#       kwargs={
#         "meal_plan_id": 6003,
#         "notes_map": {
#           "402": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
#           "423": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
#           "425": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
#           "427": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
#           "428": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
#           "429": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
#           "430": "Child-friendly: mild seasoning; cut to bite-size; soft textures."
#         }
#       }
#     ),
#     Action(
#       name="log_audit_event",
#       kwargs={
#         "household_id": 201,
#         "user_id": 101,
#         "entity_type": "meal_plan",
#         "entity_id": 6003,
#         "action_enum": "created",
#         "payload_json": {"week_start_date": "2025-09-01", "entries": 7}
#       }
#     )
#   ],
#   outputs=[]
# ),

# Task(
#   annotator="saaish2",
#   user_id="task_000",
#   instruction=(
#     "You will prepare a peanut-free school-lunch pack for Chen Solo by building a dedicated grocery list from exactly these five peanut-free Lunch recipes: 409, 410, 412, 443, 445. Categorize by section and set both pantry-staple and 30-day overlap flags with 2025-09-07 as the anchor. Keep the list initialized. Acceptance: one new list exists with items aggregated from those five lunches; sections assigned; pantry and overlap flags set; no store checks or orders."
#   ),
#   actions=[
#     Action(name="get_household_by_id", kwargs={"household_id": 203}),
#     Action(name="get_user_by_id", kwargs={"user_id": 103}),
#     Action(name="create_empty_grocery_list", kwargs={"household_id": 203, "source_meal_plan_id": None, "created_by_user_id": 103, "status_enum": "initialized"}),
#     Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,412,443,445]"}),
#     Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
#     Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
#     Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 203, "anchor_date": "2025-09-07"})
#   ],
#   outputs=[]
# ),

# Task(
#   annotator="saaish2",
#   user_id="task_000",
#   instruction=(
#     "You will prepare a peanut-free school-lunch pack for the Johnson Large Family by creating a dedicated grocery list from exactly these five Lunch recipes: 443, 409, 447, 441, 445. Categorize items and set pantry-staple and 30-day overlap flags using 2025-09-14 as the anchor. Keep the list initialized. Acceptance: one list exists with items aggregated from those five lunches; sections assigned; pantry and overlap flags set; no store checks or orders."
#   ),
#   actions=[
#     Action(name="get_household_by_id", kwargs={"household_id": 207}),
#     Action(name="get_user_by_id", kwargs={"user_id": 107}),
#     Action(name="list_household_members", kwargs={"household_id": 207}),
#     Action(name="list_inventory_by_household", kwargs={"household_id": 207}),
#     Action(name="list_recent_meal_history", kwargs={"household_id": 207, "days_back": 30, "anchor_date": "2025-09-14"}),
#     Action(name="create_empty_grocery_list", kwargs={"household_id": 207, "source_meal_plan_id": None, "created_by_user_id": 107, "status_enum": "initialized"}),
#     Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id": 8003, "recipe_ids_json": "[443,409,447,441,445]"}),
#     Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
#     Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
#     Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 207, "anchor_date": "2025-09-14"}),
#     Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
#     Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"source":"peanut_free_lunch","selected_recipes":[443,409,447,441,445]}})
#   ],
#   outputs=[]
# ),

# Task(
#   annotator="saaish2",
#   user_id="task_000",
#   instruction=(
#     "You generate a grocery list for the household “Patel Extended Family” (household_id=205) from recipes 401 and 402, created by user_id=105. Build a new list (status initialized), aggregate items from those two recipes, set grocery sections from ingredient metadata, and flag pantry staples on the list. Log one audit event for list generation. Return the new grocery list_id."
#   ),
#   actions=[
#     Action(name="get_household_by_id", kwargs={"household_id":205}),
#     Action(name="get_user_by_id", kwargs={"user_id":105}),
#     Action(name="create_empty_grocery_list", kwargs={"household_id":205,"source_meal_plan_id":None,"created_by_user_id":105,"status_enum":"initialized"}),
#     Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[401,402]"}),
#     Action(name="categorize_grocery_list_sections", kwargs={"list_id":8003}),
#     Action(name="flag_pantry_staples_on_list", kwargs={"list_id":8003}),
#     Action(name="log_audit_event", kwargs={"household_id":205,"user_id":105,"entity_type":"grocery_lists","entity_id":8003,"action_enum":"generate_list","payload_json":{"recipe_ids":[401,402]}}),
#   ],
#   outputs=[
#     "8003"
#   ]
# ),

# Task(
#   annotator="saaish2",
#   user_id="task_000",
#   instruction=(
#     "You run a pantry-first dinner restock for the household “Kim-Smith Family” (household_id=209) for the week starting 2025-09-08. Success requires: one meal plan under user_id=109 containing up to two dinners chosen from {401,402,403,404} that each introduce no more than three non-staple ingredients and align best with the adult target (member_id=327); a single grocery list derived exactly from the selected dinners; availability and product choice at store_id=9001 using lowest-price in-stock/low items for the scheduled slot 2025-09-09T09:00:00Z–11:00:00Z; and one audit event recording order placement. Return the created order_id and final total_cents."
#   ),
#   actions=[
#     Action(name="get_household_by_id", kwargs={"household_id":209}),
#     Action(name="get_user_by_id", kwargs={"user_id":109}),
#     Action(name="get_member_targets", kwargs={"member_id":327}),
#     Action(name="minimize_new_ingredients", kwargs={"recipe_ids_json":"[401,402,403,404]","max_new_ingredients_per_recipe":3}),
#     Action(name="rank_recipes_for_targets", kwargs={"recipe_ids_json":"[401,404]","needed_count":2,"target_calories":2600,"target_protein":120}),
#     Action(name="create_meal_plan", kwargs={"household_id":209,"week_start_date":"2025-09-08","created_by_user_id":109}),
#     Action(name="log_audit_event", kwargs={"household_id":209,"user_id":109,"entity_type":"meal_plans","entity_id":6003,"action_enum":"create_meal_plan","payload_json":{"week_start_date":"2025-09-08"}}),
#     Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-08","selected_recipe_ids_json":"[404, 401]"}),
#     Action(name="create_empty_grocery_list", kwargs={"household_id":209,"source_meal_plan_id":6003,"created_by_user_id":109,"status_enum":"initialized"}),
#     Action(name="log_audit_event", kwargs={"household_id":209,"user_id":109,"entity_type":"grocery_lists","entity_id":8003,"action_enum":"create_grocery_list","payload_json":{"source_meal_plan_id":6003}}),
#     Action(name="upsert_grocery_list_items_from_recipes", kwargs={"list_id":8003,"recipe_ids_json":"[404,401]"}),
#     Action(name="check_store_inventory_for_list", kwargs={"list_id":8003,"store_id":9001}),
#     Action(name="propose_substitute_products", kwargs={"list_id":8003,"store_id":9001}),
#     Action(name="update_grocery_list_with_substitutes", kwargs={"list_id":8003}),
#     Action(name="create_order_from_list", kwargs={"household_id":209,"store_id":9001,"list_id":8003,"scheduled_slot_start_ts":"2025-09-09T09:00:00Z","scheduled_slot_end_ts":"2025-09-09T11:00:00Z"}),
#     Action(name="add_order_items_from_list", kwargs={"order_id":10003,"store_id":9001}),
#     Action(name="log_audit_event", kwargs={"household_id":209,"user_id":109,"entity_type":"orders","entity_id":10003,"action_enum":"place_order","payload_json":{"list_id":8003,"store_id":9001}}),
#   ],
#   outputs=[
#     "10003",
#     "1597"
#   ]
# ),

]
