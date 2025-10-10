from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="recipes_v5_0001",
        instruction="You schedule a FreshMart‑ready Dinner week for household 201 starting 2026-09-07 with these exact seven dinners in order: 401, 404, 406, 423, 424, 433, 434. Build and categorize the grocery list. Return the list_id.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-09-07", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-09-07", "selected_recipe_ids_json": "[401,404,406,423,424,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
        ],
        outputs=["8003"]
    ),
    Task(
      annotator="0",
      user_id="recipes_v5_0002",
      instruction="You user '101' must validate a packet for a 'Dinner' rotation for household '201': schedule dinners '401', '404', '406', '423', '424', '433', '434' for '2026-09-28', generate the packet, log the creation, and return the 'meal_plan_id' and the packet URI.",
      actions=[
          Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-09-28", "created_by_user_id": 101}),
          Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-09-28", "selected_recipe_ids_json": "[401,404,406,423,424,433,434]"}),
          Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
          Action(name="log_audit_event", kwargs={
              "household_id": 201,
              "user_id": 101,
              "entity_type": "meal_plans",
              "entity_id": 6003,
              "action_enum": "create",
              "payload_json": {"week_start_date": "2026-09-28", "meal_plan_id": 6003}
          }),
      ],
      outputs=["6003", "packet://meal_plan/6003"]
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0003",
        instruction="You flag repeat‑risk ingredients for household 201: schedule 2026-10-05 dinners 401, 404, 406, 423, 424, 433, 434, build the list, then flag overlap using 2026-10-05 as the anchor and mark pantry staples. Return the list_id.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-10-05", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-05", "selected_recipe_ids_json": "[401,404,406,423,424,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 201, "anchor_date": "2026-10-05"}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0004",
        instruction=(
        "You must create a seven-dinner meal plan for household '201' for the week starting '2026-10-05', build the grocery list, and apply a no-change substitutions pass (nothing should change)."
        ),
        actions=[
        Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-10-05"}),
        Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-05"}),
        Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201}),
        Action(name="update_grocery_list_with_substitutes", kwargs={"list_id": 8003, "substitutions": []})
        ],
        outputs=[]
    ),    

  Task(
    annotator="0",
    user_id="recipes_v5_0005",
    instruction=(
      "You must return a grocery 'list_id' for household '201' for the week starting '2026-10-19' that is categorized, pantry-staple-flagged, and re-categorized to reflect final sections."
    ),
    actions=[
      Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-10-19"}),
      Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-19"}),
      Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201}),
      Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
      Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
      Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003})
    ],
    outputs=["8003"]
  ),
Task(
    annotator="0",
    user_id="recipes_v5_0006",
    instruction=(
      "You must ensure the order for household '201' at store '901' for the slot "
      "'2026-10-13T16:00:00Z'..'2026-10-13T18:00:00Z', created from the weekly plan starting '2026-10-12', "
      "ends with status 'canceled'. Return the 'order_id'."
    ),
    actions=[
      Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-10-12"}),
      Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-12"}),
      Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201}),
      Action(
        name="create_order_from_list",
        kwargs={
          "household_id": 201,
          "store_id": 901,
          "list_id": 8003,
          "scheduled_slot_start_ts": "2026-10-13T16:00:00Z",
          "scheduled_slot_end_ts": "2026-10-13T18:00:00Z"
        }
      ),
      Action(name="update_order_status", kwargs={"order_id": 10003, "new_status": "canceled"})
    ],
    outputs=["10003"]
  ),

    Task(
        annotator="0",
        user_id="recipes_v5_0007",
        instruction=(
            "You must schedule seven dinners for household '201' for the week starting '2026-07-13' with user "
            "'aiden.mercer@example.com' (user_id '101'), add recipes '[401,403,406,424,427,433,435]', create the grocery list, "
            "categorize sections, and return the resulting 'list_id'."
        ),
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "aiden.mercer@example.com"}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-07-13", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-07-13", "selected_recipe_ids_json": "[401,403,406,424,427,433,435]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0008",
        instruction=(
            "You must build a seven-dinner plan for household '201' for '2026-07-20' (user_id '101'), using the recipes "
            "'[402,404,405,423,424,432,434]', then generate the packet URI and return both the 'meal_plan_id' and the packet."
        ),
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-07-20", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-07-20", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003})
        ],
        outputs=["6003", "packet://meal_plan/6003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0009",
        instruction=(
            "You must create a weekly dinner plan for household '201' for '2026-07-27' (user 'aiden.mercer@example.com', user_id '101'), "
            "add recipes '[401,404,406,423,425,433,434]', then create the grocery list and flag pantry staples; return 'list_id'."
        ),
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "aiden.mercer@example.com"}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-07-27", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-07-27", "selected_recipe_ids_json": "[401,404,406,423,425,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0010",
        instruction=(
            "You must build a seven-dinner plan for household '201' for '2026-08-03' (user_id '101'), add recipes "
            "'[407,404,427,423,402,425,429]', create the grocery list, and flag last-30-day overlap using anchor '2026-08-03'; return 'list_id'."
        ),
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-08-03", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-08-03", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 201, "anchor_date": "2026-08-03"})
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0011",
        instruction=(
            "You must create a seven-dinner plan for household '201' for '2026-08-17' (user 'aiden.mercer@example.com', user_id '101'), "
            "add recipes '[402,404,405,423,424,432,434]', and create the grocery list; then categorize sections and return 'list_id'."
        ),
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "aiden.mercer@example.com"}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-08-17", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-08-17", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0012",
        instruction=(
            "You must create a weekly dinner plan for household '201' for '2026-08-31' (user 'aiden.mercer@example.com', user_id '101') with "
            "recipes '[407,404,427,423,402,425,429]', then create the grocery list and run an inventory check for store '901'. "
            "Return 'list_id'."
        ),
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "aiden.mercer@example.com"}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-08-31", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-08-31", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 901})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0013",
        instruction=(
            "You must schedule seven dinners for household '201' for '2026-09-07' (user_id '101') using recipes "
            "'[401,403,406,424,427,433,435]', generate the packet, and log plan creation; return the 'meal_plan_id' and packet."
        ),
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-09-07", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-09-07", "selected_recipe_ids_json": "[401,403,406,424,427,433,435]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
            Action(name="log_audit_event", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2026-09-07", "meal_plan_id": 6003}})
        ],
        outputs=["6003", "packet://meal_plan/6003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0014",
        instruction=(
            "You must create a seven-dinner plan for household '201' for '2026-09-14' (user 'aiden.mercer@example.com', user_id '101'), "
            "recipes '[402,404,405,423,424,432,434]', then create the grocery list and flag pantry staples; return 'list_id'."
        ),
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "aiden.mercer@example.com"}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-09-14", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-09-14", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0015",
        instruction=(
            "You must create a dinner plan for household '201' for '2026-09-28' (user 'aiden.mercer@example.com', user_id '101') with "
            "recipes '[407,404,427,423,402,425,429]', create the grocery list, and run an inventory check for store '901'. Return 'list_id'."
        ),
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "aiden.mercer@example.com"}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-09-28", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-09-28", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 901})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0016",
        instruction=(
            "You must build a weekly dinner plan for household '201' for '2026-10-05' (user_id '101') with recipes "
            "'[401,403,406,424,427,433,435]', then create the grocery list and log a 'create' audit for the list. Return 'list_id'."
        ),
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-10-05", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-05", "selected_recipe_ids_json": "[401,403,406,424,427,433,435]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="log_audit_event", kwargs={"household_id": 201, "user_id": 101, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"list_id": 8003, "source_meal_plan_id": 6003}})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0017",
        instruction=(
            "You must create a seven-dinner plan for household '201' for '2026-10-12' (user 'aiden.mercer@example.com', user_id '101') with "
            "recipes '[402,404,405,423,424,432,434]', create the grocery list, then categorize sections and return 'list_id'."
        ),
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "aiden.mercer@example.com"}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-10-12", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-12", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0018",
        instruction=(
            "You must build a weekly dinner plan for household '201' for '2026-10-19' (user_id '101') using recipes "
            "'[401,404,406,423,425,433,434]', and then generate the packet and return the 'meal_plan_id' with packet."
        ),
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-10-19", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-19", "selected_recipe_ids_json": "[401,404,406,423,425,433,434]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003})
        ],
        outputs=["6003", "packet://meal_plan/6003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0019",
        instruction=(
            "You must create a seven-dinner plan for household '201' for '2026-10-26' (user 'aiden.mercer@example.com', user_id '101') with "
            "recipes '[407,404,427,423,402,425,429]', then create the grocery list and flag pantry staples; return 'list_id'."
        ),
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "aiden.mercer@example.com"}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-10-26", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-26", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0020",
        instruction=(
            "You must create a seven-dinner plan for household '201' for '2026-11-02' (user_id '101') with recipes "
            "'[401,403,406,424,427,433,435]', create the grocery list, and run an inventory check for store '901'; return 'list_id'."
        ),
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-11-02", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-11-02", "selected_recipe_ids_json": "[401,403,406,424,427,433,435]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 901})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0021",
        instruction=(
            "You must plan seven dinners for household '201' for '2026-11-09' (user 'aiden.mercer@example.com', user_id '101') using recipes "
            "'[402,404,405,423,424,432,434]', generate the packet, and log plan creation. Return 'meal_plan_id' and packet."
        ),
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "aiden.mercer@example.com"}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-11-09", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-11-09", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
            Action(name="log_audit_event", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2026-11-09", "meal_plan_id": 6003}})
        ],
        outputs=["6003", "packet://meal_plan/6003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0022",
        instruction=(
            "You must create a weekly dinner plan for household '201' for '2026-11-16' (user_id '101') with recipes "
            "'[401,404,406,423,425,433,434]', then create the grocery list and categorize sections; return 'list_id'."
        ),
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-11-16", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-11-16", "selected_recipe_ids_json": "[401,404,406,423,425,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0023",
        instruction=(
            "You must schedule seven dinners for household '201' for '2026-11-23' (user 'aiden.mercer@example.com', user_id '101') using recipes "
            "'[407,404,427,423,402,425,429]', create the grocery list, and flag last-30-day overlap with anchor '2026-11-23'. Return 'list_id'."
        ),
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "aiden.mercer@example.com"}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-11-23", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-11-23", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 201, "anchor_date": "2026-11-23"})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0024",
        instruction=(
            "You must create a seven-dinner plan for household '201' for '2026-11-30' (user_id '101') with recipes "
            "'[401,403,406,424,427,433,435]', generate the packet, and return the 'meal_plan_id' and packet URI."
        ),
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-11-30", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-11-30", "selected_recipe_ids_json": "[401,403,406,424,427,433,435]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003})
        ],
        outputs=["6003", "packet://meal_plan/6003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0025",
        instruction=(
            "You must create a weekly dinner plan for household '201' for '2026-12-07' (user 'aiden.mercer@example.com', user_id '101') with "
            "recipes '[402,404,405,423,424,432,434]', create the grocery list, and log a 'create' audit for the list; return 'list_id'."
        ),
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "aiden.mercer@example.com"}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-12-07", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-12-07", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="log_audit_event", kwargs={"household_id": 201, "user_id": 101, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"list_id": 8003, "source_meal_plan_id": 6003}})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0026",
        instruction=(
            "You must schedule seven dinners for household '201' for '2026-12-14' (user_id '101') using recipes "
            "'[401,404,406,423,425,433,434]', create the grocery list, and categorize sections; return 'list_id'."
        ),
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-12-14", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-12-14", "selected_recipe_ids_json": "[401,404,406,423,425,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0027",
        instruction="You must generate the dinner recipe packet for household '201' which is linked to user '101' for the week starting '2027-02-22' by scheduling exactly these dinners '401,403,406,424,427,432,434', and then return the 'meal_plan_id' and the packet URI.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 101}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2027-02-22", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-02-22", "selected_recipe_ids_json": "[401,403,406,424,427,432,434]"}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
            Action(name="log_audit_event", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "packet_generated", "payload_json": {"week_start_date": "2027-02-22", "meal_plan_id": 6003, "packet_uri": "packet://meal_plan/6003", "scheduled_recipes": [401,403,406,424,427,432,434]}})
        ],
        outputs=["6003", "packet://meal_plan/6003"]
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0028",
        instruction="You must schedule Dinners for '2027-09-20' using recipes '[407,404,427,423,402,425,429]' for the household linked to user '103', generate the recipe packet, log a 'create' audit for the meal plan, build the grocery list, and return the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2027-09-20", "created_by_user_id": 103}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-09-20", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
            Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2027-09-20", "meal_plan_id": 6003}}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0029",
        instruction="You must schedule Dinners for '2027-10-11' using recipes '[423,424,425,427,432,433,434]' for the household linked to user '106', generate the recipe packet, log a 'create' audit for the meal plan, build the grocery list, and return the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 106}),
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2027-10-11", "created_by_user_id": 106}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-10-11", "selected_recipe_ids_json": "[423,424,425,427,432,433,434]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
            Action(name="log_audit_event", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2027-10-11", "meal_plan_id": 6003}}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0030",
        instruction="You must build a Dinner plan for '2027-10-25' using recipes '[401,404,405,423,424,433,435]' for the household linked to user '108', create the grocery list, flag pantry staples, categorize sections, check store '901' availability, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 108}),
            Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2027-10-25", "created_by_user_id": 108}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-10-25", "selected_recipe_ids_json": "[401,404,405,423,424,433,435]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 208, "created_by_user_id": 108}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 901}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0031",
        instruction="You must create Dinners for '2027-11-01' using recipes '[402,403,404,423,425,432,434]' for the household linked to user '109', generate the recipe packet, log a 'create' audit for the meal plan, build the grocery list, and return the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 109}),
            Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2027-11-01", "created_by_user_id": 109}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-11-01", "selected_recipe_ids_json": "[402,403,404,423,425,432,434]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
            Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2027-11-01", "meal_plan_id": 6003}}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 209, "created_by_user_id": 109}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0032",
        instruction="You must schedule Dinners for '2027-11-22' using recipes '[401,402,403,404,405,406,407]' for the household linked to user '102', generate the recipe packet, log a 'create' audit for the meal plan, build the grocery list, and return the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 102}),
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2027-11-22", "created_by_user_id": 102}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-11-22", "selected_recipe_ids_json": "[401,402,403,404,405,406,407]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
            Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2027-11-22", "meal_plan_id": 6003}}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0033",
        instruction="You must create a Dinner plan for '2027-12-27' using recipes '[401,403,406,424,427,433,435]' for the household linked to user '107', build the grocery list, flag pantry staples, categorize sections, check store '901' availability, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 107}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2027-12-27", "created_by_user_id": 107}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-12-27", "selected_recipe_ids_json": "[401,403,406,424,427,433,435]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 901}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0034",
        instruction="You must schedule Dinners for '2028-01-03' using recipes '[402,404,405,423,424,432,434]' for the household linked to user '108', generate the recipe packet, log a 'create' audit for the meal plan, build the grocery list, and return the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 108}),
            Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2028-01-03", "created_by_user_id": 108}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-03", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
            Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-01-03", "meal_plan_id": 6003}}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 208, "created_by_user_id": 108}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0035",
        instruction="You must create a Dinner plan for '2028-01-17' using recipes '[407,404,427,423,402,425,429]' for the household linked to user '110', build the grocery list, flag pantry staples, categorize sections, check store '901' availability, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 110}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2028-01-17", "created_by_user_id": 110}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-17", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 210, "created_by_user_id": 110}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 901}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0036",
        instruction="You must schedule Dinners for '2028-01-24' using recipes '[401,402,403,404,405,406,407]' for the household linked to user '101', generate the recipe packet, log a 'create' audit for the meal plan, build the grocery list, and return the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 101}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2028-01-24", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-24", "selected_recipe_ids_json": "[401,402,403,404,405,406,407]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
            Action(name="log_audit_event", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-01-24", "meal_plan_id": 6003}}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0037",
        instruction="You must create a Dinner plan for '2028-02-07' using recipes '[401,402,404,423,427,432,434]' for the household linked to user '103', build the grocery list, flag pantry staples, categorize sections, check store '901' availability, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2028-02-07", "created_by_user_id": 103}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-02-07", "selected_recipe_ids_json": "[401,402,404,423,427,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 901}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0038",
        instruction="You must schedule Dinners for '2028-02-14' using recipes '[401,403,404,423,427,433,434]' for the household linked to user '104', generate the recipe packet, log a 'create' audit for the meal plan, build the grocery list, and return the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 104}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2028-02-14", "created_by_user_id": 104}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-02-14", "selected_recipe_ids_json": "[401,403,404,423,427,433,434]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
            Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-02-14", "meal_plan_id": 6003}}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0039",
        instruction="You must create a Dinner plan for '2028-02-28' using recipes '[401,404,405,423,424,433,435]' for the household linked to user '106', build the grocery list, flag pantry staples, categorize sections, check store '901' availability, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 106}),
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2028-02-28", "created_by_user_id": 106}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-02-28", "selected_recipe_ids_json": "[401,404,405,423,424,433,435]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 901}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0040",
        instruction="You must schedule Dinners for '2028-03-06' using recipes '[402,403,404,423,425,432,434]' for the household linked to user '107', generate the recipe packet, log a 'create' audit for the meal plan, build the grocery list, and return the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 107}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2028-03-06", "created_by_user_id": 107}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-03-06", "selected_recipe_ids_json": "[402,403,404,423,425,432,434]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
            Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-03-06", "meal_plan_id": 6003}}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0041",
        instruction="You must schedule Dinners for '2028-03-27' using recipes '[407,404,427,423,402,425,429]' for the household linked to user '110', generate the recipe packet, log a 'create' audit for the meal plan, build the grocery list, and return the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 110}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2028-03-27", "created_by_user_id": 110}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-03-27", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
            Action(name="log_audit_event", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-03-27", "meal_plan_id": 6003}}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 210, "created_by_user_id": 110}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0042",
        instruction="You must create a Dinner plan for '2028-04-10' using recipes '[423,424,425,427,432,433,434]' for the household linked to user '102', build the grocery list, flag pantry staples, categorize sections, check store '901' availability, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 102}),
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2028-04-10", "created_by_user_id": 102}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-04-10", "selected_recipe_ids_json": "[423,424,425,427,432,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 901}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0043",
        instruction="You must schedule Dinners for '2028-04-17' using recipes '[401,402,404,423,427,432,434]' for the household linked to user '103', generate the recipe packet, log a 'create' audit for the meal plan, build the grocery list, and return the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2028-04-17", "created_by_user_id": 103}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-04-17", "selected_recipe_ids_json": "[401,402,404,423,427,432,434]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
            Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-04-17", "meal_plan_id": 6003}}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0044",
        instruction=(
            "You must create a household-compliant weekly Dinner plan for '2027-12-13' for the primary linked to user with the email 'aiden.mercer@example.com', "
            "ensuring the plan adheres to household policy (avoid dinners from the last '28' days and keep at most '2' recipes per cuisine). "
            "Deliver a valid plan using recipes '[429,430,431,432,433,434,435]' within policy, produce the grocery list, "
            "validate availability at store '9007', and return the 'list_id'."
        ),
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "aiden.mercer@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 101}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 201, "days_back": 28, "anchor_date": "2027-12-13"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[429,430,431,432,433,434,435]", "max_per_cuisine": 2}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2027-12-13", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-12-13", "selected_recipe_ids_json": "[429,430,431,432,433,434,435]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9007}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0045",
        instruction="You must use email 'lina.alvarez@example.com' to create a weekly Dinner plan for the week starting '2027-12-20', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[401,402,403,404,405,406,407]'; select exactly '7' dinners, build the grocery list, verify availability at store '9001', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "lina.alvarez@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 102}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 202, "days_back": 28, "anchor_date": "2027-12-20"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[401,402,403,404,405,406,407]", "max_per_cuisine": 2}),
            Action(name="rank_recipes_for_targets", kwargs={"recipe_ids_json": "[401,402,403,404,405,406,407]", "needed_count": 7}),
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2027-12-20", "created_by_user_id": 102}),
            Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2027-12-20"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-12-20", "selected_recipe_ids_json": "[407,404,402,405,401,403,406]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9001}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0046",
        instruction="You must use email 'sarah.chen@example.com' to create a weekly Dinner plan for the week starting '2027-12-27', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[408,409,410,411,412,413,414]'; select up to '7' dinners, build the grocery list, verify availability at store '9002', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "sarah.chen@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 203, "days_back": 28, "anchor_date": "2027-12-27"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[408,409,410,411,412,413,414]", "max_per_cuisine": 2}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2027-12-27", "created_by_user_id": 103}),
            Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2027-12-27"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-12-27", "selected_recipe_ids_json": "[408,409,410,411,412]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),
            Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9002}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0047",
        instruction="You must use email 'marcus.williams@example.com' to create a weekly Dinner plan for the week starting '2028-01-03', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[415,416,417,418,419,420,421]'; select up to '7' dinners, build the grocery list, verify availability at store '9003', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "marcus.williams@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 104}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 204, "days_back": 28, "anchor_date": "2028-01-03"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[415,416,417,418,419,420,421]", "max_per_cuisine": 2}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2028-01-03", "created_by_user_id": 104}),
            Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-01-03"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-03", "selected_recipe_ids_json": "[415,416,417,420,421]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9003}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0048",
        instruction="You must use email 'priya.patel@example.com' to create a weekly Dinner plan for the week starting '2028-01-10', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[422,423,424,425,426,427,428]'; select up to '7' dinners, build the grocery list, verify availability at store '9004', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "priya.patel@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 105}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 205, "days_back": 28, "anchor_date": "2028-01-10"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[422,423,424,425,426,427,428]", "max_per_cuisine": 2}),
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2028-01-10", "created_by_user_id": 105}),
            Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-01-10"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-10", "selected_recipe_ids_json": "[422,423,424,425,426,427]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 205, "created_by_user_id": 105}),
            Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9004}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0049",
        instruction="You must use email 'david.kowalski@example.com' to create a weekly Dinner plan for the week starting '2028-01-17', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[401,402,403,404,405,406,407]'; select exactly '7' dinners, build the grocery list, verify availability at store '9005', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "david.kowalski@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 106}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 206, "days_back": 28, "anchor_date": "2028-01-17"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[401,402,403,404,405,406,407]", "max_per_cuisine": 2}),
            Action(name="rank_recipes_for_targets", kwargs={"recipe_ids_json": "[401,402,403,404,405,406,407]", "needed_count": 7}),
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2028-01-17", "created_by_user_id": 106}),
            Action(name="log_audit_event", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-01-17"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-17", "selected_recipe_ids_json": "[407,404,402,405,401,403,406]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="log_audit_event", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9005}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0050",
        instruction="You must use email 'emma.johnson@example.com' to create a weekly Dinner plan for the week starting '2028-01-24', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[408,409,410,411,412,413,414]'; select up to '7' dinners, build the grocery list, verify availability at store '9006', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "emma.johnson@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 107}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 207, "days_back": 28, "anchor_date": "2028-01-24"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[408,409,410,411,412,413,414]", "max_per_cuisine": 2}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2028-01-24", "created_by_user_id": 107}),
            Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-01-24"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-24", "selected_recipe_ids_json": "[408,409,410,411,412]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9006}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0051",
        instruction="You must use email 'antonio.garcia@example.com' to create a weekly Dinner plan for the week starting '2028-01-31', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[415,416,417,418,419,420,421]'; select up to '7' dinners, build the grocery list, verify availability at store '9007', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "antonio.garcia@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 108}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 208, "days_back": 28, "anchor_date": "2028-01-31"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[415,416,417,418,419,420,421]", "max_per_cuisine": 2}),
            Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2028-01-31", "created_by_user_id": 108}),
            Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-01-31"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-31", "selected_recipe_ids_json": "[415,416,417,420,421]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 208, "created_by_user_id": 108}),
            Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9007}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0052",
        instruction="You must use email 'rachel.kim@example.com' to create a weekly Dinner plan for the week starting '2028-02-07', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[422,423,424,425,426,427,428]'; select up to '7' dinners, build the grocery list, verify availability at store '9008', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "rachel.kim@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 109}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 209, "days_back": 28, "anchor_date": "2028-02-07"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[422,423,424,425,426,427,428]", "max_per_cuisine": 2}),
            Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2028-02-07", "created_by_user_id": 109}),
            Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-02-07"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-02-07", "selected_recipe_ids_json": "[422,423,424,425,426,427]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 209, "created_by_user_id": 109}),
            Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9008}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0053",
        instruction="You must use email 'james.thompson@example.com' to create a weekly Dinner plan for the week starting '2028-02-14', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[401,403,406,424,427,433,435]'; select exactly '7' dinners, build the grocery list, verify availability at store '9009', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "james.thompson@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 110}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 210, "days_back": 28, "anchor_date": "2028-02-14"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[401,403,406,424,427,433,435]", "max_per_cuisine": 2}),
            Action(name="rank_recipes_for_targets", kwargs={"recipe_ids_json": "[401,403,406,424,427,433,435]", "needed_count": 7}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2028-02-14", "created_by_user_id": 110}),
            Action(name="log_audit_event", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-02-14"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-02-14", "selected_recipe_ids_json": "[427,435,401,403,406,433,424]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 210, "created_by_user_id": 110}),
            Action(name="log_audit_event", kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9009}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0054",
        instruction="You must use email 'aiden.mercer@example.com' to create a weekly Dinner plan for the week starting '2028-02-21', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[408,409,410,411,412,413,414]'; select up to '7' dinners, build the grocery list, verify availability at store '9010', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "aiden.mercer@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 101}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 201, "days_back": 28, "anchor_date": "2028-02-21"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[408,409,410,411,412,413,414]", "max_per_cuisine": 2}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2028-02-21", "created_by_user_id": 101}),
            Action(name="log_audit_event", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-02-21"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-02-21", "selected_recipe_ids_json": "[408,409,410,411,412]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="log_audit_event", kwargs={"household_id": 201, "user_id": 101, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9010}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0055",
        instruction="You must use email 'lina.alvarez@example.com' to create a weekly Dinner plan for the week starting '2028-02-28', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[415,416,417,418,419,420,421]'; select up to '7' dinners, build the grocery list, verify availability at store '9011', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "lina.alvarez@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 102}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 202, "days_back": 28, "anchor_date": "2028-02-28"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[415,416,417,418,419,420,421]", "max_per_cuisine": 2}),
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2028-02-28", "created_by_user_id": 102}),
            Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-02-28"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-02-28", "selected_recipe_ids_json": "[415,416,417,420,421]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9011}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0056",
        instruction="You must use email 'sarah.chen@example.com' to create a weekly Dinner plan for the week starting '2028-03-06', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[422,423,424,425,426,427,428]'; select up to '7' dinners, build the grocery list, verify availability at store '9012', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "sarah.chen@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 203, "days_back": 28, "anchor_date": "2028-03-06"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[422,423,424,425,426,427,428]", "max_per_cuisine": 2}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2028-03-06", "created_by_user_id": 103}),
            Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-03-06"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-03-06", "selected_recipe_ids_json": "[422,423,424,425,426,427]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),
            Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9012}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0057",
        instruction="You must use email 'marcus.williams@example.com' to create a weekly Dinner plan for the week starting '2028-03-13', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[429,430,431,432,433,434,435]'; select exactly '7' dinners, build the grocery list, verify availability at store '9013', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "marcus.williams@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 104}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 204, "days_back": 28, "anchor_date": "2028-03-13"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[429,430,431,432,433,434,435]", "max_per_cuisine": 2}),
            Action(name="rank_recipes_for_targets", kwargs={"recipe_ids_json": "[429,430,431,432,433,434,435]", "needed_count": 7}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2028-03-13", "created_by_user_id": 104}),
            Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-03-13"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-03-13", "selected_recipe_ids_json": "[429,430,435,434,433,431,432]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9013}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0058",
        instruction="You must use email 'priya.patel@example.com' to create a weekly Dinner plan for the week starting '2028-03-20', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[401,402,403,404,405,406,407]'; select exactly '7' dinners, build the grocery list, verify availability at store '9014', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "priya.patel@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 105}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 205, "days_back": 28, "anchor_date": "2028-03-20"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[401,402,403,404,405,406,407]", "max_per_cuisine": 2}),
            Action(name="rank_recipes_for_targets", kwargs={"recipe_ids_json": "[401,402,403,404,405,406,407]", "needed_count": 7}),
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2028-03-20", "created_by_user_id": 105}),
            Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-03-20"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-03-20", "selected_recipe_ids_json": "[407,404,402,405,401,403,406]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 205, "created_by_user_id": 105}),
            Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9014}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0059",
        instruction="You must use email 'david.kowalski@example.com' to create a weekly Dinner plan for the week starting '2028-03-27', avoiding recipes from the last '28' days and keeping at most '2' recipes per cuisine from the candidate set '[408,409,410,411,412,413,414]'; select up to '7' dinners, build the grocery list, verify availability at store '9015', and return the 'list_id'.",
        actions=[
            Action(name="get_user_by_email", kwargs={"email": "david.kowalski@example.com"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 106}),
            Action(name="list_recent_meal_history", kwargs={"household_id": 206, "days_back": 28, "anchor_date": "2028-03-27"}),
            Action(name="apply_cuisine_limit", kwargs={"recipe_ids_json": "[408,409,410,411,412,413,414]", "max_per_cuisine": 2}),
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2028-03-27", "created_by_user_id": 106}),
            Action(name="log_audit_event", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-03-27"}}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-03-27", "selected_recipe_ids_json": "[408,409,410,411,412]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="log_audit_event", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9015}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0060",
        instruction="You must schedule a Dinner week for the household linked to user '101' starting '2028-04-03' with these exact seven dinners in order: '401','404','406','423','424','433','434'. Build and categorize the grocery list, check availability at store '9001', and return the 'list_id'. For internal validation, also list the household members and fetch a meal-plan details snapshot to confirm ownership and 'week_start_date' (no need to include these validations in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 101}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2028-04-03", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-04-03", "selected_recipe_ids_json": "[401,404,406,423,424,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="list_household_members", kwargs={"household_id": 201}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9001}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0061",
        instruction="You must create a Dinner plan for the household linked to user '102' for the week starting '2028-04-10' using exactly these seven dinners in order: '402','404','405','423','424','432','434'. Build the grocery list, flag pantry staples, check store '9002', and return the 'list_id'. Additionally, produce an internal consistency check by listing the household members and retrieving a meal-plan details snapshot to verify correct ownership and dates (do not include these in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 102}),
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2028-04-10", "created_by_user_id": 102}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-04-10", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
            Action(name="list_household_members", kwargs={"household_id": 202}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9002}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0062",
        instruction="You must schedule a Dinner week for the household linked to user '103' starting '2028-04-17' with these exact dinners in order: '407','404','427','423','402','425','429'. Build the grocery list, flag last-30-day overlap using anchor '2028-04-17', and return the 'list_id'. Also create a minimal internal validation trail by listing household members and fetching a meal-plan details snapshot to confirm correct linkage (no need to include these in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2028-04-17", "created_by_user_id": 103}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-04-17", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),
            Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 203, "anchor_date": "2028-04-17"}),
            Action(name="list_household_members", kwargs={"household_id": 203}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0063",
        instruction="You must build a Dinner plan for the household linked to user '104' for the week starting '2028-04-24' with exactly '423','424','425','427','432','433','434'. Create the grocery list, flag pantry staples, validate availability at store '9003', and return the 'list_id'. Include an internal verification step by listing household members and retrieving a meal-plan details snapshot to confirm ownership and configuration (no need to include the verification in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 104}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2028-04-24", "created_by_user_id": 104}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-04-24", "selected_recipe_ids_json": "[423,424,425,427,432,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
            Action(name="list_household_members", kwargs={"household_id": 204}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9003}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0064",
        instruction="You must create a Dinner week for the household linked to user '105' starting '2028-05-01' using exactly '401','403','404','423','427','433','434'. Build and categorize the grocery list, and return the 'list_id'. For internal QA, list the household members, fetch the meal-plan details, retrieve the grocery-list details to confirm ownership/sections, and capture a brief household inventory snapshot for reconciliation (these validations are not required in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 105}),
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2028-05-01", "created_by_user_id": 105}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-05-01", "selected_recipe_ids_json": "[401,403,404,423,427,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 205, "created_by_user_id": 105}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="list_household_members", kwargs={"household_id": 205}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
            Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
            Action(name="list_inventory_by_household", kwargs={"household_id": 205}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0065",
        instruction="You must schedule a Dinner week for the household linked to user '106' starting '2028-05-08' with exactly '402','404','405','423','424','432','434'. Build the grocery list, validate store '9005', and return the 'list_id'. Include an internal verification step by fetching the grocery-list details, meal-plan details, and a brief household inventory snapshot for reconciliation (no need to include these verifications in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 106}),
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2028-05-08", "created_by_user_id": 106}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-05-08", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9005}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
            Action(name="list_inventory_by_household", kwargs={"household_id": 206}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0066",
        instruction="You must plan Dinners for the household linked to user '107' for the week starting '2028-05-15' using exactly '401','404','406','423','425','433','435'. Build the grocery list, categorize sections, flag pantry staples, and return the 'list_id'. As part of internal QA, fetch the grocery-list details, the meal-plan details, and a short household inventory snapshot to validate the list composition (nothing additional is required in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 107}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2028-05-15", "created_by_user_id": 107}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-05-15", "selected_recipe_ids_json": "[401,404,406,423,425,433,435]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
            Action(name="list_inventory_by_household", kwargs={"household_id": 207}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0067",
        instruction="You must create a Dinner plan for the household linked to user '108' for the week starting '2028-05-22' with exactly '407','404','427','423','402','425','429'. Build the grocery list, verify availability at store '9007', and return the 'list_id'. For internal validation, also retrieve the grocery-list details and meal-plan details and capture a brief household inventory snapshot (no additional data needs to be returned).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 108}),
            Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2028-05-22", "created_by_user_id": 108}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-05-22", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 208, "created_by_user_id": 108}),
            Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9007}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
            Action(name="list_inventory_by_household", kwargs={"household_id": 208}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0068",
        instruction="You must schedule Dinners for the household linked to user '109' for the week starting '2028-05-29' using exactly '402','403','404','423','425','432','434'. Build the grocery list, flag last-30-day overlap using anchor '2028-05-29', and return the 'list_id'. Also run internal verification by fetching grocery-list details, meal-plan details, and a short household inventory snapshot for reconciliation (these checks are not required in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 109}),
            Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2028-05-29", "created_by_user_id": 109}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-05-29", "selected_recipe_ids_json": "[402,403,404,423,425,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 209, "created_by_user_id": 109}),
            Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
            Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2028-05-29"}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
            Action(name="list_inventory_by_household", kwargs={"household_id": 209}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0069",
        instruction="You must build a Dinner plan for the household linked to user '110' for the week starting '2028-06-05' with exactly '401','403','406','424','427','432','434'. Create the grocery list, check availability at store '9009', and return the 'list_id'. To complete internal QA, fetch grocery-list details and meal-plan details and capture a short household inventory snapshot (no need to include the QA data in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 110}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2028-06-05", "created_by_user_id": 110}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-06-05", "selected_recipe_ids_json": "[401,403,406,424,427,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 210, "created_by_user_id": 110}),
            Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9009}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
            Action(name="list_inventory_by_household", kwargs={"household_id": 210}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0070",
        instruction="You must schedule a Dinner week for the household linked to user '102' starting '2028-06-12' with exactly '402','404','405','423','424','432','434' in that order. Build the grocery list, categorize sections, verify availability at store '9002', and return the 'list_id'. For internal QA, list the household members and fetch a meal-plan details snapshot (no need to include the QA in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 102}),
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2028-06-12", "created_by_user_id": 102}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-06-12", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9002}),
            Action(name="list_household_members", kwargs={"household_id": 202}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0071",
        instruction="You must build a Dinner week for the household linked to user '103' starting '2028-06-19' using exactly '407','404','427','423','402','425','429'. Build the grocery list, categorize sections, flag pantry staples, check store '9003', and return the 'list_id'. For internal QA, also retrieve the meal-plan details and the grocery-list details to confirm ownership and sections (no need to include QA in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),                                                          
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2028-06-19", "created_by_user_id": 103}), 
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-06-19", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),  
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),                                         
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),                                                 
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),                                                     
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9003}),                                
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),                                                       
            Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),                                                        
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0072",
        instruction=(
            "You must schedule a Dinner week for the household linked to user '104' starting '2028-06-26' using exactly "
            "'423','424','425','427','432','433','434'. Build the grocery list, flag last-30-day overlap using anchor '2028-06-26', "
            "validate availability at store '9004', and return the 'list_id'. For internal QA, also capture a meal-plan details snapshot "
            "and list household members (QA is not required in outputs)."
        ),
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 104}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2028-06-26", "created_by_user_id": 104}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-06-26", "selected_recipe_ids_json": "[423,424,425,427,432,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 204, "anchor_date": "2028-06-26"}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9004}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
            Action(name="list_household_members", kwargs={"household_id": 204}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0073",
        instruction=(
            "You must schedule a Dinner week for the household linked to user '106' starting '2028-07-10' using exactly "
            "'402','404','405','423','424','432','434'. Build the grocery list, verify availability at store '9006', and return the 'list_id'. "
            "For internal QA, list household members and retrieve both meal-plan and grocery-list details to confirm ownership and sections "
            "(QA data is not required in outputs)."
        ),
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 106}),
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2028-07-10", "created_by_user_id": 106}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-07-10", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9006}),
            Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
            Action(name="list_household_members", kwargs={"household_id": 206}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0074",
        instruction="You must schedule a Dinner week for the household linked to user '107' starting '2028-07-17' using exactly '401','404','406','423','425','433','435'. Build and categorize the grocery list, open an order at store '9007' for slot '2028-07-18T10:00:00Z'..'2028-07-18T12:00:00Z', set the order status to 'on_hold', and return the 'order_id'. For internal QA, take a meal-plan details snapshot (no need to include QA in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 107}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2028-07-17"}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "selected_recipe_ids_json": "[401,404,406,423,425,433,435]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="create_order_from_list", kwargs={"household_id": 207, "store_id": 9007, "list_id": 8003, "scheduled_slot_start_ts": "2028-07-18T10:00:00Z", "scheduled_slot_end_ts": "2028-07-18T12:00:00Z"}),
            Action(name="update_order_status", kwargs={"order_id": 10003, "new_status": "on_hold"}),
        ],
        outputs=["10003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0075",
        instruction="You must plan Dinners for the household linked to user '110' for the week starting '2028-08-07' using exactly '401','403','406','424','427','432','434'. Generate the recipe packet, build and categorize the grocery list, check store '9010', log a 'packet_generated' audit event for the meal plan, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 110}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2028-08-07"}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "selected_recipe_ids_json": "[401,403,406,424,427,432,434]"}),
            Action(name="generate_recipe_packet", kwargs={"meal_plan_id": 6003}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9010}),
            Action(name="log_audit_event", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "packet_generated"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0076",
        instruction="You must build a Dinner week for the household linked to user '104' starting '2028-09-04' using exactly '423','424','425','427','432','433','434'. Build and categorize the grocery list, check availability at store '9004', and return the 'list_id'. Include an internal QA snapshot by listing household members and fetching meal-plan details (not required in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 104}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2028-09-04", "created_by_user_id": 104}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-09-04", "selected_recipe_ids_json": "[423,424,425,427,432,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9004}),
            Action(name="list_household_members", kwargs={"household_id": 204}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0077",
        instruction="You must create a Dinner week for the household linked to user '105' starting '2028-09-11' using exactly '401','403','404','423','427','433','434'. Build and categorize the grocery list, flag pantry staples, check store '9005', log a 'create' audit event for the grocery list, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 105}),                                                                                                    
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2028-09-11", "created_by_user_id": 105}),                                           
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "selected_recipe_ids_json": "[401,403,404,423,427,433,434]"}),                               
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003}),                                                                                    
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),                                                                                           
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),                                                                                                
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9005}),                                                                           
            Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create"}),            
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="gen_v5",
        user_id="recipes_v5_0078",
        instruction="You must schedule a Dinner week for household '209' starting '2027-07-18' using exactly '402','403','404','423','425','432','434'; build the grocery list, validate store '9010', log a 'create' audit for the list, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 109}),
            Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2027-07-18", "created_by_user_id": 109}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-07-18", "selected_recipe_ids_json": "[402,403,404,423,425,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 209, "created_by_user_id": 109}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9010}),
            Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0079",
        instruction="You must build a Dinner week for the household linked to user '107' starting '2028-09-25' using exactly '401','404','406','423','425','433','435'. Build and categorize the grocery list, check store '9007', and return the 'list_id'. Include an internal meal-plan details snapshot for QA (not required in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 107}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2028-09-25", "created_by_user_id": 107}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-09-25", "selected_recipe_ids_json": "[401,404,406,423,425,433,435]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9007}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
            Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0080",
        instruction=(
            "You must create a Dinner week for the household linked to user '108' starting '2028-10-02' using exactly "
            "'407','404','427','423','402','425','429'. Build and categorize the grocery list, flag last-30-day overlap using anchor "
            "'2028-10-02', verify availability at store '9008', and return the 'list_id'."
        ),
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 108}),
            Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2028-10-02", "created_by_user_id": 108}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-10-02", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 208, "created_by_user_id": 108}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 208, "anchor_date": "2028-10-02"}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9008}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0081",
        instruction="You must build a Dinner week for the household linked to user '110' starting '2028-10-16' using exactly '401','403','406','424','427','432','434'. Build the grocery list, check store '9011', categorize sections, flag pantry staples, and return the 'list_id'. For internal QA, list household members and retrieve a meal-plan and grocery-list snapshot (no need to include QA in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 110}),                                                                                                     
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2028-10-16", "created_by_user_id": 110}),                                           
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "selected_recipe_ids_json": "[401,403,406,424,427,432,434]"}),                              
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 210, "created_by_user_id": 110}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9011}),                                                                       
            Action(name="list_household_members", kwargs={"household_id": 210}),                                                                                               
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),                                                                                                
            Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),                                                                                                   
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),                                                                                           
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),                                                                                                
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0082",
        instruction="You must schedule Dinners for the household linked to user '101' for the week starting '2028-10-23' using exactly '407','404','427','423','402','425','429'. Build and categorize the grocery list, flag pantry staples, check store '9012', and return the 'list_id'. For internal QA, list household members and retrieve meal-plan and grocery-list details (no need to include QA in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 101}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2028-10-23"}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9012}),
            Action(name="list_household_members", kwargs={"household_id": 201}),
            Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0083",
        instruction="You must build a Dinner week for the household linked to user '102' starting '2028-10-30' using exactly '402','404','405','423','424','432','434'. Build the grocery list, flag last-30-day overlap with anchor '2028-10-30', verify availability at store '9013', and return the 'list_id'. Add an internal meal-plan details snapshot for QA (do not include QA in outputs).",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 102}),
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2028-10-30", "created_by_user_id": 102}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-10-30", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="flag_overlap_last_month_on_list", kwargs={"list_id": 8003, "household_id": 202, "anchor_date": "2028-10-30"}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9013}),
            Action(name="get_meal_plan_details", kwargs={"meal_plan_id": 6003}),
            Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0084",
        instruction=(
            "You must schedule Dinners for the household linked to user '109' for the week starting '2028-10-09' using exactly "
            "'402','403','404','423','425','432','434'. Build and categorize the grocery list, flag pantry staples, check store '9009', "
            "log a 'create' audit event for the grocery list, and return the 'list_id'."
        ),
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 109}),
            Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2028-10-09", "created_by_user_id": 109}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "selected_recipe_ids_json": "[402,403,404,423,425,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003}),
            Action(name="categorize_grocery_list_sections", kwargs={"list_id": 8003}),
            Action(name="flag_pantry_staples_on_list", kwargs={"list_id": 8003}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9009}),
            Action(name="log_audit_event", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0085",
        instruction="You must schedule a Dinner week for household '201' starting '2027-01-03' using exactly '401','404','406','423','424','433','434' in that order; build the grocery list, verify availability at store '9001', log a 'create' audit for the list, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 101}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2027-01-03", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-01-03", "selected_recipe_ids_json": "[401,404,406,423,424,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="log_audit_event", kwargs={"household_id": 201, "user_id": 101, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0086",
        instruction="You must schedule a Dinner week for household '207' starting '2027-07-04' using exactly '401','404','406','423','425','433','435'; build the grocery list, validate store '9008', log a 'create' audit for the list, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 107}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2027-07-04", "created_by_user_id": 107}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-07-04", "selected_recipe_ids_json": "[401,404,406,423,425,433,435]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9008}),
            Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0087",
        instruction="You must schedule a Dinner week for household '204' starting '2027-01-24' using exactly '423','424','425','427','432','433','434'; build the grocery list, verify availability at store '9004', log a 'create' audit for the list, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 104}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2027-01-24", "created_by_user_id": 104}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-01-24", "selected_recipe_ids_json": "[423,424,425,427,432,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9004}),
            Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0088",
        instruction="You must schedule a Dinner week for household '205' starting '2027-01-31' using exactly '401','403','404','423','427','433','434'; build the grocery list, validate store '9005', log the grocery-list creation, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 105}),
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2027-01-31", "created_by_user_id": 105}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-01-31", "selected_recipe_ids_json": "[401,403,404,423,427,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 205, "created_by_user_id": 105}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9005}),
            Action(name="log_audit_event", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0089",
        instruction="You must schedule a Dinner week for household '206' starting '2027-02-07' using exactly '402','404','405','423','424','432','434'; build the grocery list, verify store '9006', log a 'create' audit for the list, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 106}),
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2027-02-07", "created_by_user_id": 106}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-02-07", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9006}),
            Action(name="log_audit_event", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0090",
        instruction="You must schedule a Dinner week for household '207' starting '2027-02-14' using exactly '401','404','406','423','425','433','435'; build the grocery list, validate availability at store '9007', log a 'create' audit for the list, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 107}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2027-02-14", "created_by_user_id": 107}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-02-14", "selected_recipe_ids_json": "[401,404,406,423,425,433,435]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9007}),
            Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0091",
        instruction="You must schedule a Dinner week for household '201' starting '2027-03-14' using exactly '401','404','406','423','424','433','434'; build the grocery list, validate store '9002', log the list creation, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 101}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2027-03-14", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-03-14", "selected_recipe_ids_json": "[401,404,406,423,424,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9002}),
            Action(name="log_audit_event", kwargs={"household_id": 201, "user_id": 101, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0092",
        instruction="You must schedule a Dinner week for household '202' starting '2027-03-21' using exactly '402','404','405','423','424','432','434'; build the grocery list, validate store '9003', log a 'create' audit for the list, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 102}),
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2027-03-21", "created_by_user_id": 102}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-03-21", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9003}),
            Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0093",
        instruction="You must schedule a Dinner week for household '203' starting '2027-03-28' using exactly '407','404','427','423','402','425','429'; build the grocery list, validate store '9004', log the list creation, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2027-03-28", "created_by_user_id": 103}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-03-28", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9004}),
            Action(name="log_audit_event", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0094",
        instruction="You must schedule a Dinner week for household '204' starting '2027-04-04' using exactly '423','424','425','427','432','433','434'; build the grocery list, verify store '9005', log a 'create' audit for the list, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 104}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2027-04-04", "created_by_user_id": 104}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-04-04", "selected_recipe_ids_json": "[423,424,425,427,432,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9005}),
            Action(name="log_audit_event", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0095",
        instruction="You must schedule a Dinner week for household '206' starting '2027-04-18' using exactly '402','404','405','423','424','432','434'; build the grocery list, validate store '9007', log the list creation, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 106}),
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2027-04-18", "created_by_user_id": 106}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-04-18", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9007}),
            Action(name="log_audit_event", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0096",
        instruction="You must schedule a Dinner week for household '207' starting '2027-04-25' using exactly '401','404','406','423','425','433','435'; build the grocery list, validate store '9008', log a 'create' audit for the list, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 107}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2027-04-25", "created_by_user_id": 107}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-04-25", "selected_recipe_ids_json": "[401,404,406,423,425,433,435]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9008}),
            Action(name="log_audit_event", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0097",
        instruction="You must schedule a Dinner week for household '208' starting '2027-05-02' using exactly '407','404','427','423','402','425','429'; build the grocery list, verify store '9009', log the list creation, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 108}),
            Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2027-05-02", "created_by_user_id": 108}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-05-02", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 208, "created_by_user_id": 108}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9009}),
            Action(name="log_audit_event", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0098",
        instruction="You must schedule a Dinner week for household '210' which is linked to user '110' starting '2027-05-16' using exactly '401','403','406','424','427','432','434'; build the grocery list, validate store '9001', log the list creation, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 110}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2027-05-16", "created_by_user_id": 110}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-05-16", "selected_recipe_ids_json": "[401,403,406,424,427,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 210, "created_by_user_id": 110}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="log_audit_event", kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0099",
        instruction="You must schedule a Dinner week for household '201' starting '2027-05-23' using exactly '401','404','406','423','424','433','434'; build the grocery list, validate store '9002', log a 'create' audit for the list, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 101}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2027-05-23", "created_by_user_id": 101}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-05-23", "selected_recipe_ids_json": "[401,404,406,423,424,433,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9002}),
            Action(name="log_audit_event", kwargs={"household_id": 201, "user_id": 101, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0100",
        instruction="You must schedule a Dinner week for household '202' starting '2027-05-30' using exactly '402','404','405','423','424','432','434'; build the grocery list, validate store '9003', log the list creation, and return the 'list_id'.",
        actions=[
            Action(name="get_household_by_user_id", kwargs={"user_id": 102}),
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2027-05-30", "created_by_user_id": 102}),
            Action(name="bulk_add_meal_plan_entries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-05-30", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="check_store_inventory_for_list", kwargs={"list_id": 8003, "store_id": 9003}),
            Action(name="log_audit_event", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
]