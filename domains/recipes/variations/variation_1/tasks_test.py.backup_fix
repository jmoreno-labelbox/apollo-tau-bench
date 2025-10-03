from tau_bench.types import Action, Task

TASKS = [

Task(
  annotator="saaish2",
  user_id="task_001",
        instruction=(
            "Formulate a standalone grocery list for the Rodriguez Household (household_id=208) under user_id=108 without associating it with any meal plan. Compile it using exactly these dinners: [431,432,433,434]. Success requires generating a new grocery_lists row, where items are compiled from these recipes, and the status is 'initialized', in addition to creating one audit event to record the list's creation. Return the list's status string."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":208}),
    Action(name="GetUserById", kwargs={"user_id":108}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":208,"source_meal_plan_id":None,"created_by_user_id":108,"status_enum":"initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[431,432,433,434]"}),
    Action(name="GetGroceryListDetails", kwargs={"list_id":8003}),
    Action(name="LogAuditEvent", kwargs={"household_id":208,"user_id":108,"entity_type":"grocery_list","entity_id":8003,"action_enum":"list_created","payload_json":"{\"source\":\"recipes\",\"count\":4}"}),
  ],
  outputs=[
    "initialized"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_002",
        instruction=(
            "Set up a 4-day Lunch plan for the Brown Large Family (household_id 207) from 2025-09-08 to 2025-09-11 using these specific peanut-free recipes in order: 409, 410, 411, 412. Associate the fixed child-friendly note “Child-friendly: mild seasoning; cut to bite-size; soft textures.” with each entry, and log the creation with an audit. Acceptance: one meal plan for household 207 with week_start_date 2025-09-08 must include four entries from 2025-09-08 to 2025-09-11 in that sequence with the appended child-friendly notes, and the creation should be documented with an audit."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 207}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 409}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 410}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 411}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 412}),
    Action(name="GetUserById", kwargs={"user_id": 107}),
    Action(name="CreateMealPlan", kwargs={"household_id": 207, "week_start_date": "2025-09-08", "created_by_user_id": 107}),
    Action(
      name="BulkAddMealPlanEntries",
      kwargs={
        "meal_plan_id": 6003,
        "week_start_date": "2025-09-08",
        "selected_recipe_ids_json": "[409,410,411,412]"
      }
    ),
    Action(
      name="UpdateMealPlanEntryNotes",
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
      name="LogAuditEvent",
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
            "Arrange five peanut-free weeknight dinners for the Brown Large Family (household_id=207) during the week commencing 2025-09-01. Acceptance criteria: establish one meal plan with Dinner entries [402, 404, 407, 408, 423]; generate a grocery list from these recipes with sections and pantry flags configured; resolve store_id=9001 availability issues by applying peanut-free in-store substitutions when deterministically possible; set up one delivery order for 2025-01-02T10:00:00Z–12:00:00Z using lowest-price in-stock items, ensuring the order status is 'placed' and the list status is 'ordered'; log audits for meal plan creation, list creation, substitutions applied (even if zero), order placement, and list status change. Provide the new order_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 207}),
    Action(name="CreateMealPlan", kwargs={"household_id": 207, "week_start_date": "2025-09-01", "created_by_user_id": 107}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[402,404,407,408,423]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 207, "created_by_user_id": 107, "source_meal_plan_id": 6003, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,404,407,408,423]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-01"}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9001}),
    Action(
      name="ProposeSubstituteProducts",
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
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id": 8003, "substitutions": []}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "substitutions_applied", "payload_json": {"count": 0}}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 207, "store_id": 9001, "list_id": 8003, "scheduled_slot_start_ts": "2025-01-02T10:00:00Z", "scheduled_slot_end_ts": "2025-01-02T12:00:00Z"}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9001}),
    Action(name="UpdateOrderStatus", kwargs={"order_id": 10003, "new_status": "placed"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ordered"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "orders", "entity_id": 10003, "action_enum": "placed", "payload_json": {"list_id": 8003, "store_id": 9001}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "status_update", "payload_json": {"status_enum": "ordered"}})
  ],
  outputs=[
    "10003"
  ]
),


Task(
  annotator="saaish2",
  user_id="task_004",
        instruction=(
            "Prepare a pantry-first four-dinner plan for the Shah Extended Family (household_id=205) for the week starting 2025-09-01, and get a ready-to-shop list ready. Acceptance criteria: ensure the plan exists with Dinner entries [402, 404, 405, 425]; create a grocery list from these recipes; ensure sections and pantry flags are set; compute 30-day overlap flags using anchor_date=2025-08-31; confirm the grocery list status is 'ready' and log audits for plan creation, list creation, and status change. Return the created meal_plan_id and grocery_list_id (in that order)."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 205}),
    Action(name="CreateMealPlan", kwargs={"household_id": 205, "week_start_date": "2025-09-01", "created_by_user_id": 105}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[402,404,405,425]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 205, "created_by_user_id": 105, "source_meal_plan_id": 6003, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,404,405,425]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 205, "anchor_date": "2025-08-31"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-01"}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "status_update", "payload_json": {"status_enum": "ready"}})
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
            "Handle the completion of Grocery List 8002 for the Martinez Household by amending sections and flags, then adjusting the status to 'ready'. Use 2025-09-07 as the reference overlap anchor date and record an audit to account for the status modification. Acceptance: list 8002 has updated grocery sections, pantry-staple flags, 30-day overlap flags linked to 2025-09-07, status 'ready', with an audit available for the update."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 202}),
    Action(name="GetGroceryListDetails", kwargs={"list_id": 8002}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8002}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8002}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8002, "household_id": 202, "anchor_date": "2025-09-07"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8002, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_lists", "entity_id": 8002, "action_enum": "update", "payload_json": {"status": "ready"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_006",
        instruction=(
            "Coordinate a 7-dinner high-protein plan for the Peterson Couple (household_id=206) for the week commencing 2024-12-30 with deliveries facilitated by GreenGrocer Digital (store_id=9001). Acceptance criteria (single deterministic terminal state): 1) Only one meal plan is available for that week with Dinner entries [402, 404, 405, 407, 408, 428, 429]. 2) There is a single grocery list for that plan; items are combined from these recipes; sections and pantry flags are applied; 30-day overlap flags employ anchor_date=2024-12-29; list status is 'ordered'. 3) A singular order is present for that list at store_id=9001 with scheduled_slot_start_ts='2025-01-02T10:00:00Z' and scheduled_slot_end_ts='2025-01-02T12:00:00Z'; order status is 'placed'. 4) Audit events should exist for meal plan creation, grocery list creation, and order placement. Provide the grocery_list_id and order_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 206}),
    Action(name="CreateMealPlan", kwargs={"household_id": 206, "week_start_date": "2024-12-30", "created_by_user_id": 106}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2024-12-30", "selected_recipe_ids_json": "[402,404,405,407,408,428,429]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 206, "created_by_user_id": 106, "source_meal_plan_id": 6003, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,404,405,407,408,428,429]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 206, "anchor_date": "2024-12-29"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9001}),
    Action(
      name="ProposeSubstituteProducts",
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
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id": 8003, "substitutions": []}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 206, "store_id": 9001, "list_id": 8003, "scheduled_slot_start_ts": "2025-01-02T10:00:00Z", "scheduled_slot_end_ts": "2025-01-02T12:00:00Z"}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9001}),
    Action(name="UpdateOrderStatus", kwargs={"order_id": 10003, "new_status": "placed"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ordered"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2024-12-30"}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 206, "user_id": 106, "entity_type": "orders", "entity_id": 10003, "action_enum": "placed", "payload_json": {"list_id": 8003, "store_id": 9001}}),
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
            "Coordinate a budget-friendly 7-night dinner itinerary for the Lee-Anderson Family (household_id=209) beginning the week of 2024-12-30, utilizing Value Groceries Direct (store_id=9004). Criteria for acceptance (single deterministic terminal states): 1) A single meal plan is established for that week with Dinner recipes [402, 404, 405, 407, 408, 423, 427]. 2) One grocery list solely associated with that plan is created, showing a total derived from these recipes; sections and pantry flags are designated; 30-day overlap flags rely on anchor_date=2024-12-29; list status is set to 'ordered'. 3) A unique order correlates with the list at store_id=9004, with a scheduled_slot_start_ts='2025-01-02T10:00:00Z' and scheduled_slot_end_ts='2025-01-02T12:00:00Z'; its final status is 'delivered'. 4) The audit log documents: creation of the meal plan, the grocery list construction, alteration of list status to 'ordered', and order progression to 'placed' then 'delivered'. Return the conclusive status of the order."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 209}),
    Action(name="CreateMealPlan", kwargs={"household_id": 209, "week_start_date": "2024-12-30", "created_by_user_id": 109}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2024-12-30", "selected_recipe_ids_json": "[402,404,405,407,408,423,427]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 209, "created_by_user_id": 109, "source_meal_plan_id": 6003, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,404,405,407,408,423,427]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2024-12-29"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9004}),
    Action(
      name="ProposeSubstituteProducts",
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
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id": 8003, "substitutions": []}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 209, "store_id": 9004, "list_id": 8003, "scheduled_slot_start_ts": "2025-01-02T10:00:00Z", "scheduled_slot_end_ts": "2025-01-02T12:00:00Z"}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9004}),
    Action(name="UpdateOrderStatus", kwargs={"order_id": 10003, "new_status": "placed"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ordered"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "status_update", "payload_json": {"status_enum": "ordered"}}),
    Action(name="UpdateOrderStatus", kwargs={"order_id": 10003, "new_status": "delivered"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2024-12-30"}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "orders", "entity_id": 10003, "action_enum": "placed", "payload_json": {"list_id": 8003, "store_id": 9004}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "orders", "entity_id": 10003, "action_enum": "delivered", "payload_json": {"list_id": 8003, "store_id": 9004}})
  ],
  outputs=[
    "delivered"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_008",
        instruction=(
            "Manage the completion of grocery list 8002 for the Martinez Household (household_id=202) under user_id=102, making sure items are assigned sections and pantry staples are marked, followed by setting the list status to 'finalized' and logging one audit event for the finalization. Return the definitive status string."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":202}),
    Action(name="GetUserById", kwargs={"user_id":102}),
    Action(name="GetGroceryListDetails", kwargs={"list_id":8002}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8002}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id":8002}),
    Action(name="SetGroceryListStatus", kwargs={"list_id":8002,"status_enum":"finalized"}),
    Action(name="LogAuditEvent", kwargs={"household_id":202,"user_id":102,"entity_type":"grocery_list","entity_id":8002,"action_enum":"list_finalized","payload_json":{"list_id":8002}}),
  ],
  outputs=[
    "finalized"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_009",
        instruction=(
            "Coordinate the creation of a fixed-menu weekend Dinner grocery list for the Brown Large Family utilizing recipes 402, 404, and 406, with an anchor date of 2025-09-06 for conducting 30-day overlap verifications. Acceptance: ensure a new grocery list for household 207 includes only those recipes, with overlaps flagged using the anchor date, and that the list is compiled."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 207}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 207, "source_meal_plan_id": None, "created_by_user_id": 107, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,404,406]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 207, "anchor_date": "2025-09-06"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "aggregated"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "aggregated", "payload_json": {"anchor_date": "2025-09-06", "recipe_ids": [402,404,406]}}),
  ],
  outputs=[]
),


Task(
  annotator="saaish2",
  user_id="task_010",
        instruction=(
            "Coordinate a selection of peanut-free work-lunch options for the Lee-Anderson Family, employing Lunch recipes with a minimum of 18 g protein per serving while minimizing the inclusion of new non-staple ingredients (limit to two per recipe). Acceptance: generate a specific grocery list for household 209 and perform an initial audit; ensure sections are filled; pantry essentials and 30-day overlaps (anchored to 2025-09-01) are identified; set the list status to ready_to_order with an audit of the status change."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 209}),
    Action(name="ListRecipesByFilters", kwargs={"filter_token": "F:Lunch:P18:PF1:EX"}),
    Action(name="MinimizeNewIngredients", kwargs={"recipe_ids_json": "[409,441,443,445,446,447]", "max_new_ingredients_per_recipe": 2}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 209, "source_meal_plan_id": None, "created_by_user_id": 109, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[447]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2025-09-01"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "aggregated"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "aggregated", "payload_json": {"policy": "sections+pantry+overlap"}}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready_to_order"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "status_changed", "payload_json": {"to": "ready_to_order"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_011",
        instruction=(
            "Organize a 3-night Dinner plan for the Brown-Brown Family (household_id 204) commencing the week of 2025-09-15 by using the recipes [425, 428, 431] in the specified sequence over the first three days. Log an audit for the creation of the meal plan. Acceptance criteria: one meal plan is present for household 204 with week_start_date 2025-09-15 and includes three Dinner entries in the designated order; an audit for the meal plan creation is available. Submit the generated meal_plan_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 204}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 425}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 428}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 431}),
    Action(name="GetUserById", kwargs={"user_id": 104}),
    Action(name="CreateMealPlan", kwargs={"household_id": 204, "week_start_date": "2025-09-15", "created_by_user_id": 104}),
    Action(
      name="BulkAddMealPlanEntries",
      kwargs={
        "meal_plan_id": 6003,
        "week_start_date": "2025-09-15",
        "selected_recipe_ids_json": "[425,428,431]",
        "meal_type_enum": "Dinner"
      }
    ),
    Action(
      name="LogAuditEvent",
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
            "Coordinate two dinners for Wang Solo in the week beginning 2025-09-01, aiming for approximately ≈700 kcal and ≈35 g protein per serving (utilizing the standard ±15% nutrition range, maintaining a ≥30 g protein minimum). Develop the plan by selecting the top two dinners closest to those nutritional targets, compile a grocery list from these two dinners, organize sections, label pantry staples and 30-day overlaps using 2025-08-30 as the reference date, ensure the list is marked 'ready', and document audits for the creation and finalization of the meal plan and grocery list. Approve once the plan and list are in place, the list is 'ready', and the audits are documented."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 203}),
    Action(name="GetUserById", kwargs={"user_id": 103}),
    Action(name="BuildRecipeFilters", kwargs={"meal_type": "Dinner", "min_protein_g": 30, "peanut_free": False, "cuisines_exclude": []}),
    Action(name="ListRecipesByFilters", kwargs={"filter_token": "F:Dinner:P30:PF0:EX"}),
    Action(name="RankRecipesForTargets", kwargs={"recipe_ids_json": "[402, 404, 407, 423, 425, 427, 435]", "target_calories": 700, "target_protein": 35, "needed_count": 2}),
    Action(name="CreateMealPlan", kwargs={"household_id": 203, "week_start_date": "2025-09-01", "created_by_user_id": 103}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[407, 423]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 203, "source_meal_plan_id": 6003, "created_by_user_id": 103, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[407, 423]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 203, "anchor_date": "2025-08-30"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-01"}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"source_meal_plan_id": 6003}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "finalized", "payload_json": {"status": "ready"}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_013",
        instruction=(
            "Coordinate the delivery of a weekly one-dinner plan for Davis Retirement (week commencing 2025-09-01) that satisfies approximately 650 kcal and about 30 g protein per serving, adhering to the standard ±15% range (protein minimum ≥26 g). Ensure the outcome includes a finalized grocery list marked as ready along with audit logs for both the plan and list transitions. Accept if a valid dinner plan is present, the grocery list is ready, and the audits have been completed."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 210}),
    Action(name="GetUserById", kwargs={"user_id": 110}),
    Action(name="BuildRecipeFilters", kwargs={"meal_type": "Dinner", "min_protein_g": 26, "peanut_free": False, "cuisines_exclude": []}),
    Action(name="ListRecipesByFilters", kwargs={"filter_token": "F:Dinner:P26:PF0:EX"}),
    Action(name="RankRecipesForTargets", kwargs={"recipe_ids_json": "[402, 404, 407, 423, 425, 427, 429, 434, 435]", "target_calories": 650, "target_protein": 30, "needed_count": 1}),
    Action(name="CreateMealPlan", kwargs={"household_id": 210, "week_start_date": "2025-09-01", "created_by_user_id": 110}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[427]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 210, "source_meal_plan_id": 6003, "created_by_user_id": 110, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[427]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-01"}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"source_meal_plan_id": 6003}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "finalized", "payload_json": {"status": "ready"}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_014",
        instruction=(
            "Coordinate the provision of a five-dinner plan for the Peterson Couple (household_id=206) for the week beginning 2025-09-08 under user_id=106. Select the five dinners that most closely match member_id=316’s goals from the following options: [401, 402, 405, 406, 407, 408, 431], resolving ties by higher protein content followed by shorter preparation time. Validate the chosen recipes, construct the plan, and record an audit entry for plan creation. Return the generated new meal_plan_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 206}),
    Action(name="GetUserById", kwargs={"user_id": 106}),
    Action(name="GetMemberTargets", kwargs={"member_id": 316}),
    Action(
      name="RankRecipesForTargets",
      kwargs={
        "recipe_ids_json": "[401,402,405,406,407,408,431]",
        "needed_count": 5,
        "target_calories": 2400,
        "target_protein": 140,
      },
    ),
    Action(name="GetRecipeById", kwargs={"recipe_id": 407}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 402}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 405}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 408}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 401}),
    Action(
      name="CreateMealPlan",
      kwargs={"household_id": 206, "week_start_date": "2025-09-08", "created_by_user_id": 106},
    ),
    Action(
      name="BulkAddMealPlanEntries",
      kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[407,402,405,408,401]"},
    ),
    Action(
      name="LogAuditEvent",
      kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "meal_plan_created"},
    ),
  ],
  outputs=["6003"],
),

Task(
  annotator="saaish2",
  user_id="task_015",
        instruction=(
            "Organize four peanut-free Dinners for Emily Wang’s household (household_id 203) for the week of 2025-09-01, preferring recipes with ≤4 non-staple ingredients each and at least ~18g protein. Utilize targets of 1800 kcal and 80g protein to select recipes. Success is defined as generating one new meal_plan for that week with precisely four Dinner entries, and one grocery_list linked to the plan where items match the aggregated ingredients of those entries, with 30-day overlap flags computed and status='finalized'."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 203}),
    Action(name="BuildRecipeFilters", kwargs={"meal_type": "Dinner", "min_protein_g": 18, "peanut_free": True, "cuisines_exclude": []}),
    Action(name="ListRecipesByFilters", kwargs={"filter_token": "F:Dinner:P18:PF1:EX"}),

    Action(name="MinimizeNewIngredients", kwargs={
      "recipe_ids_json": "[402, 404, 405, 407, 408, 423, 425, 427, 428, 429, 432, 433, 434, 435]",
      "max_new_ingredients_per_recipe": 4
    }),

    Action(name="RankRecipesForTargets", kwargs={
      "recipe_ids_json": "[402, 404, 407, 408, 423, 425, 427, 429, 432, 433, 435]",
      "needed_count": 4,
      "target_calories": 1800,
      "target_protein": 80
    }),

    Action(name="CreateMealPlan", kwargs={"household_id": 203, "week_start_date": "2025-09-01", "created_by_user_id": 103}),
    Action(name="LogAuditEvent", kwargs={
      "household_id": 203, "user_id": 103,
      "entity_type": "meal_plan", "entity_id": 6003,
      "action_enum": "created",
      "payload_json": {"week_start_date": "2025-09-01"}
    }),

    Action(name="BulkAddMealPlanEntries", kwargs={
      "meal_plan_id": 6003,
      "week_start_date": "2025-09-01",
      "selected_recipe_ids_json": "[425, 407, 423, 435]"
    }),

    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 203, "source_meal_plan_id": 6003, "created_by_user_id": 103, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={
      "household_id": 203, "user_id": 103,
      "entity_type": "grocery_list", "entity_id": 8003,
      "action_enum": "created",
      "payload_json": {"source_meal_plan_id": 6003, "status": "initialized"}
    }),

    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[425, 407, 423, 435]"}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 203}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "finalized"}),
    Action(name="LogAuditEvent", kwargs={
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
            "Coordinate a two-Dinner weekend grocery list for the Lee-Anderson Family (household_id 209) without initiating a new plan, using peanut-free Dinner recipes limited to one per cuisine and supplying at least 20g protein, optimized for Grace Lee’s targets (2600 kcal, 120g protein). Achievement is a single new grocery_list for the household with items corresponding to the aggregated ingredients from two chosen dinners, items categorized, pantry_staple flags assigned, 30-day overlap flags computed, and status='finalized'."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 209}),
    Action(name="BuildRecipeFilters", kwargs={"meal_type": "Dinner", "min_protein_g": 20, "peanut_free": True, "cuisines_exclude": []}),
    Action(name="ListRecipesByFilters", kwargs={"filter_token": "F:Dinner:P20:PF1:EX"}),
    Action(name="ApplyCuisineCap", kwargs={
      "recipe_ids_json": "[402, 404, 405, 407, 408, 423, 425, 427, 428, 429, 433, 434, 435]",
      "max_per_cuisine": 1
    }),
    Action(name="RankRecipesForTargets", kwargs={
      "recipe_ids_json": "[402, 404, 405, 407, 408, 423, 427, 429, 434]",
      "needed_count": 2,
      "target_calories": 2600,
      "target_protein": 120
    }),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 209, "created_by_user_id": 109, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={
      "household_id": 209, "user_id": 109,
      "entity_type": "grocery_list", "entity_id": 8003,
      "action_enum": "created",
      "payload_json": {"status": "initialized"}
    }),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[407, 423]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 209}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "finalized"}),
    Action(name="LogAuditEvent", kwargs={
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
            "Handle the creation of a standalone grocery list for the Lee-Anderson Family (household_id=209) linked to user_id=109 using precisely these dinners: [405, 431]. Verify availability at store_id=9007 and document in-store substitutions deterministically if available; refrain from placing an order. Success entails logging an audit event for the list creation and another after applying any substitutions."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":209}),
    Action(name="GetUserById", kwargs={"user_id":109}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":209,"source_meal_plan_id":None,"created_by_user_id":109,"status_enum":"initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id":209,"user_id":109,"entity_type":"grocery_list","entity_id":8003,"action_enum":"list_created"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[405,431]"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id":8003,"store_id":9007}),
    Action(
      name="ProposeSubstituteProducts",
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
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id":8003,"substitutions":[]}),
    Action(name="LogAuditEvent", kwargs={"household_id":209,"user_id":109,"entity_type":"grocery_list","entity_id":8003,"action_enum":"substitutions_applied"})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_018",
        instruction=(
            "Coordinate the creation of a pantry-first restock list for the Shah Extended Family by compiling ingredients from exactly these three Dinner recipes: 424, 426, 431. Classify items by grocery section, and set the pantry-staple and 30-day overlap flags using 2025-09-07 as the anchor date. Keep the list initialized. Acceptance: a new grocery list should exist with items collected from those three recipes; sections assigned; pantry and overlap flags set; no store checks or orders."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 205}),
    Action(name="GetUserById", kwargs={"user_id": 105}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 205, "source_meal_plan_id": None, "created_by_user_id": 105, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[424,426,431]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 205, "anchor_date": "2025-09-07"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"source":"pantry_first","recipes":[424,426,431]}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_019",
        instruction=(
            "Coordinate a single curbside order for the Martinez Household (household_id=202) using the established grocery list list_id=8002 at store_id=9004, set for 2025-09-09T10:00:00Z–12:00:00Z. Success is indicated by one new order for that list and store with status 'placed', and order_items chosen as the lowest-price in-stock products according to policy. Record an audit event post-substitution application, after order creation, once items are added, and after marking the order as placed. Additionally, update the grocery list status to 'ordered' once items are finalized. Provide the newly created order_id and the final total_cents."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":202}),
    Action(name="GetGroceryListDetails", kwargs={"list_id":8002}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id":8002,"store_id":9004}),
    Action(
      name="ProposeSubstituteProducts",
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
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id":8002,"substitutions":[]}),
    Action(name="LogAuditEvent", kwargs={"household_id":202,"user_id":102,"entity_type":"grocery_list","entity_id":8002,"action_enum":"substitutions_applied"}),
    Action(name="CreateOrderFromList", kwargs={"household_id":202,"store_id":9004,"list_id":8002,"scheduled_slot_start_ts":"2025-09-09T10:00:00Z","scheduled_slot_end_ts":"2025-09-09T12:00:00Z"}),
    Action(name="LogAuditEvent", kwargs={"household_id":202,"user_id":102,"entity_type":"order","entity_id":10003,"action_enum":"order_created"}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id":10003,"store_id":9004}),
    Action(name="LogAuditEvent", kwargs={"household_id":202,"user_id":102,"entity_type":"order","entity_id":10003,"action_enum":"order_items_added"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id":8002,"status_enum":"ordered"}),
    Action(name="UpdateOrderStatus", kwargs={"order_id":10003,"new_status":"placed"}),
    Action(name="LogAuditEvent", kwargs={"household_id":202,"user_id":102,"entity_type":"order","entity_id":10003,"action_enum":"order_placed"})
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
            "Ensure the Rodriguez Household's final state includes a weekday Dinner grocery list derived solely from recipe IDs 401, 402, 425, 427; the list should be organized by grocery section and feature pantry-staple and 30-day overlap flags anchored to 2025-09-07; availability should be synced to FoodExpress (store_id 9002); a draft order should be prepared for the delivery window 2025-09-03T10:00:00Z–2025-09-03T12:00:00Z containing only the most affordable in-stock products for items on that list; the order should remain in draft form. Acceptance criteria: exactly one list and one draft order should exist as described."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 208}),
    Action(name="GetUserById", kwargs={"user_id": 108}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 208, "source_meal_plan_id": None, "created_by_user_id": 108, "status_enum": "initialized"}),
    Action(
      name="LogAuditEvent",
      kwargs={
        "household_id": 208,
        "user_id": 108,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "created",
        "payload_json": {"source": "recipes", "recipes": [401, 402, 425, 427]}
      }
    ),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,402,425,427]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 208, "anchor_date": "2025-09-07"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 208, "store_id": 9002, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-03T10:00:00Z", "scheduled_slot_end_ts": "2025-09-03T12:00:00Z"}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9002, "product_overrides": {}}),
    Action(
      name="LogAuditEvent",
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
            "Manage the creation of a standalone grocery list for the household “Shah Extended Family” (household_id=205), authored by user_id=105, not associated with any meal plan, compiled precisely from these recipes: [403, 412, 431]. Success is defined as having one newly initialized grocery_lists row for that household with items matching the exact compilation from those recipes, and a singular audit event documenting the list creation. Provide the new list_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":205}),
    Action(name="GetUserById", kwargs={"user_id":105}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":205,"source_meal_plan_id":None,"created_by_user_id":105,"status_enum":"initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[403,412,431]"}),
    Action(name="LogAuditEvent", kwargs={"household_id":205,"user_id":105,"entity_type":"grocery_list","entity_id":8003,"action_enum":"list_created"})
  ],
  outputs=[
    "8003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_022",
        instruction=(
            "Coordinate the delivery of a full end state for the Lee-Anderson Family’s 7-night Dinners for the week starting 2025-09-15 using exactly the following recipe IDs: 402, 423, 425, 427, 428, 434, 435. Each entry must utilize the singular fixed child-note template. The associated grocery list must consolidate those dinners, be segmented into categories, and mark pantry-staple and 30-day overlap indicators set to 2025-09-21. Ensure availability aligns with GreenGrocer Digital (store_id 9001). Implement these defined in-store substitutions as needed: 1002→1048 and 1009→1066. Prepare a draft order for the timeframe 2025-09-18T09:00:00Z–2025-09-18T11:00:00Z, containing only the least expensive in-stock items per ingredient after substitutions, while keeping the order in draft form. Acceptance entails one Dinner meal plan with template notes, one linked list with categorized sections/pantry/overlap, confirmation of store 9001 availability, the application of two relevant substitutions, the creation and population of one draft order, and the absence of placed_ts on the draft."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 209}),
    Action(name="GetUserById", kwargs={"user_id": 109}),
    Action(name="CreateMealPlan", kwargs={"household_id": 209, "week_start_date": "2025-09-15", "created_by_user_id": 109}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-15", "selected_recipe_ids_json": "[402,423,425,427,428,434,435]"}),
    Action(
      name="UpdateMealPlanEntryNotes",
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
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 209, "source_meal_plan_id": 6003, "created_by_user_id": 109, "status_enum": "initialized"}),
    Action(
      name="LogAuditEvent",
      kwargs={
        "household_id": 209,
        "user_id": 109,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "created",
        "payload_json": {"source_meal_plan_id": 6003}
      }
    ),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,423,425,427,428,434,435]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2025-09-21"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9001}),
    Action(name="ProposeSubstituteProducts", kwargs={"store_id": 9001, "flagged_items": [{"ingredient_id": 1002}, {"ingredient_id": 1009}], "require_peanut_free": False}),
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id": 8003, "substitutions": [{"ingredient_id": 1002, "substitute_ingredient_id": 1048}, {"ingredient_id": 1009, "substitute_ingredient_id": 1066}]}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9001}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 209, "store_id": 9001, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-18T09:00:00Z", "scheduled_slot_end_ts": "2025-09-18T11:00:00Z"}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9001, "product_overrides": {}}),
    Action(
      name="LogAuditEvent",
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
      name="LogAuditEvent",
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
      name="LogAuditEvent",
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
            "Coordinate a 2-night vegetarian dinner micro-plan for the household “Wang Solo” (household_id=203) for the week commencing on 2025-09-01. Ensure utilization of precisely recipes 403 (Chickpea Curry) and 405 (Teriyaki Tofu Bowl). Formulate a new meal plan for that week with user_id=103 and incorporate exactly two Dinner entries associated with those recipes, using default servings and excluding free-text notes. Record a single audit event noting the creation. Provide the created entry_id list for the new plan."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":203}),
    Action(name="GetUserById", kwargs={"user_id":103}),
    Action(name="GetRecipeById", kwargs={"recipe_id":403}),
    Action(name="GetRecipeById", kwargs={"recipe_id":405}),
    Action(name="CreateMealPlan", kwargs={"household_id":203,"week_start_date":"2025-09-01","created_by_user_id":103}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-01","selected_recipe_ids_json":"[403,405]"}),
    Action(name="LogAuditEvent", kwargs={"household_id":203,"user_id":103,"entity_type":"meal_plans","entity_id":6003,"action_enum":"create_meal_plan","payload_json":{"week_start_date":"2025-09-01"}}),
  ],
  outputs=[6118, 6119]
),

Task(
  annotator="saaish2",
  user_id="task_024",
        instruction=(
            "Arrange to provide a Dessert grocery list for the Shah Extended Family (household_id 205), utilizing exactly recipes [414, 415], validated against Natural Farm Collective (store_id 9003). Conduct a creation audit specifying the store checked. Requirements include: one new list assembled with items collated from those recipes; availability assessed at store 9003; and inclusion of \"store_checked\": 9003 in the creation audit payload. Provide the creation audit_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 205}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 205, "created_by_user_id": 105, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[414,415]"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9003}),
    Action(
      name="LogAuditEvent",
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
            "Coordinate a single-dinner plan setup for the household “Davis Retirement” (household_id=210) for the week commencing 2025-09-15 using only recipe 408 (Lentil Soup). Then, create a grocery list linked to that plan and check for 30-day meal overlaps against recent meals using anchor_date=2025-08-20. Register one audit event for the generation of the list. Provide the new meal_plan_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":210}),
    Action(name="GetUserById", kwargs={"user_id":110}),
    Action(name="CreateMealPlan", kwargs={"household_id":210,"week_start_date":"2025-09-15","created_by_user_id":110}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-15","selected_recipe_ids_json":"[408]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":210,"source_meal_plan_id":6003,"created_by_user_id":110,"status_enum":"initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[408]"}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id":8003,"household_id":210,"anchor_date":"2025-08-20"}),
    Action(name="LogAuditEvent", kwargs={"household_id":210,"user_id":110,"entity_type":"grocery_lists","entity_id":8003,"action_enum":"generate_list","payload_json":{"source_meal_plan_id":6003}}),
  ],
  outputs=[
    "6003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_026",
        instruction=(
            "Handle a pantry-first dinner restock for the household “Lee-Anderson Family” (household_id=209) targeting the week beginning 2025-09-08. Fulfillment conditions include: one meal plan under user_id=109 containing exactly two dinners selected from {401,402,403,404}; the selection must minimize the total absolute deviation from the adult target (member_id=327) in protein (main criterion), using absolute calorie deviation as a tie-breaker and the lower recipe_id if needed as the final tie-breaker; each selected recipe should introduce no more than three non-staple ingredients; derive one grocery list precisely from those two dinners; ensure availability and product choice at store_id=9001 using items with the lowest prices and stock_status in {in_stock, low} for the designated slot 2025-09-09T09:00:00Z–11:00:00Z; document one audit event for the order placement. Return the generated order_id and final total_cents."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":209}),
    Action(name="GetUserById", kwargs={"user_id":109}),
    Action(name="GetMemberTargets", kwargs={"member_id":327}),
    Action(name="MinimizeNewIngredients", kwargs={"recipe_ids_json":"[401,402,403,404]","max_new_ingredients_per_recipe":3}),
    Action(name="RankRecipesForTargets", kwargs={"recipe_ids_json":"[401,404]","needed_count":2,"target_calories":2600,"target_protein":120}),
    Action(name="CreateMealPlan", kwargs={"household_id":209,"week_start_date":"2025-09-08","created_by_user_id":109}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-08","selected_recipe_ids_json":"[404, 401]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":209,"source_meal_plan_id":6003,"created_by_user_id":109,"status_enum":"initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[404,401]"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id":8003,"store_id":9001}),
    Action(name="ProposeSubstituteProducts", kwargs={"list_id":8003,"store_id":9001}),
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id":8003}),
    Action(name="CreateOrderFromList", kwargs={"household_id":209,"store_id":9001,"list_id":8003,"scheduled_slot_start_ts":"2025-09-09T09:00:00Z","scheduled_slot_end_ts":"2025-09-09T11:00:00Z"}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id":10003,"store_id":9001}),
    Action(name="LogAuditEvent", kwargs={"household_id":209,"user_id":109,"entity_type":"orders","entity_id":10003,"action_enum":"place_order","payload_json":{"list_id":8003,"store_id":9001}}),
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
            "Coordinate the procurement of Martinez Household's grocery list 8002 (household_id 202) from GreenGrocer Digital (store_id 9001) by respecting store availability and implementing in-store substitutions where possible. Document an audit summarizing all changes. Acceptance: the availability assessment for list 8002 at store 9001 is completed; when alternatives are in stock or low, suitable substitutions are made according to policy; the list is updated to reflect changes; an audit payload outlines the new item count. Return the number of items updated in the list."
        ),
  actions=[
    Action(name="GetGroceryListDetails", kwargs={"list_id": 8002}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8002, "store_id": 9001}),
    Action(name="ProposeSubstituteProducts", kwargs={
      "store_id": 9001,
      "flagged_items": [
        {"ingredient_id": 1026, "status": "out_of_catalog"},
        {"ingredient_id": 1039, "status": "out_of_catalog"},
        {"ingredient_id": 1038, "status": "out_of_catalog"}
      ],
      "require_peanut_free": False
    }),
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id": 8002, "substitutions": []}),
    Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8002, "action_enum": "substitutions_applied", "payload_json": {"updated_items": 0}}),
  ],
  outputs=[
    "0"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_028",
        instruction=(
            "Oversee the creation of a 7-night family dinner plan for the “Brown Large Family” (household_id=207) for the week beginning 2025-09-08. The plan succeeds if it is under user_id=107 and includes exactly seven peanut-free dinners, each offering at least 20 g of protein and primarily aligned with the adult target (member_id=319). Generate one grocery list from these seven recipes; resolve availability at store_id=9001 with a single order scheduled for 2025-09-09T10:00:00Z–12:00:00Z, selecting the lowest-price items with stock_status among {in_stock, low} as policy allows; and document one audit event for the order placement. Return the order_id created and the final total_cents."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":207}),
    Action(name="GetUserById", kwargs={"user_id":107}),
    Action(name="GetMemberTargets", kwargs={"member_id":319}),
    Action(name="BuildRecipeFilters", kwargs={"meal_type":"Dinner","min_protein_g":20,"peanut_free":True,"cuisines_exclude":[]}),
    Action(name="ListRecipesByFilters", kwargs={"filter_token":"F:Dinner:P20:PF1:EX"}),
    Action(name="RankRecipesForTargets", kwargs={"recipe_ids_json":"[402,404,405,407,408,423,425,427,428,429,433,434,435]","needed_count":7,"target_calories":2300,"target_protein":125}),
    Action(name="CreateMealPlan", kwargs={"household_id":207,"week_start_date":"2025-09-08","created_by_user_id":107}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-08","selected_recipe_ids_json":"[425,407,423,435,404,427,402]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":207,"source_meal_plan_id":6003,"created_by_user_id":107,"status_enum":"initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[425,407,423,435,404,427,402]"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id":8003,"store_id":9001}),
    Action(name="ProposeSubstituteProducts", kwargs={"list_id":8003,"store_id":9001}),
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id":8003}),
    Action(name="CreateOrderFromList", kwargs={"household_id":207,"store_id":9001,"list_id":8003,"scheduled_slot_start_ts":"2025-09-09T10:00:00Z","scheduled_slot_end_ts":"2025-09-09T12:00:00Z"}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id":10003,"store_id":9001,"allowed_stock_statuses_json":"[\"in_stock\",\"low\"]"}),
    Action(name="LogAuditEvent", kwargs={"household_id":207,"user_id":107,"entity_type":"orders","entity_id":10003,"action_enum":"place_order","payload_json":{"list_id":8003,"store_id":9001}}),
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
            "Design a three-dinner menu and associated shopping list for Wang Solo (household_id 203) utilizing Dinner recipes 401, 402, and 404 specifically for the week commencing on 2025-09-08. Acceptance: a meal plan is established for that period, a combined grocery list is attached with items sorted and flags for pantry/30-day overlap applied using 2025-09-07 as the reference point, and the list's status is \"ready\"."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 203}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 401}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 402}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 404}),
    Action(name="CreateMealPlan", kwargs={"household_id": 203, "week_start_date": "2025-09-08", "created_by_user_id": 103}),
    Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-08"}}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[401,402,404]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 203, "source_meal_plan_id": 6003, "created_by_user_id": 103, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,402,404]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 203, "anchor_date": "2025-09-07"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"source": "meal_plan", "meal_plan_id": 6003}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"flags": ["pantry_staple","overlap_30d"], "categorized": True}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_030",
        instruction=(
            "Draft a peanut-free school-lunch grocery list for the Martinez Household (household_id 202) employing lunch recipes 409, 410, and 411 exclusively. Acceptance: there is a single list in existence, ingredients are compiled and sorted with pantry/30-day overlap flags marked using 2025-09-07, store 9002's stock is verified, and the list's status reads \"inventory_checked\". Provide the list_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 202}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 409}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 410}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 411}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 202, "source_meal_plan_id": None, "created_by_user_id": 102, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,411]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 202, "anchor_date": "2025-09-07"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "inventory_checked"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "inventory_checked", "payload_json": {"store_id": 9002}}),
    Action(name="GetGroceryListDetails", kwargs={"list_id": 8003})
  ],
  outputs=[
    "8003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_031",
        instruction=(
            "Handle the preparation of a dinner grocery list for the Brown Large Family (household_id 207) using precisely recipes 424 and 433. Then, coordinate a single order from store 9004 for delivery within the timeframe 2025-09-05T10:00:00Z–12:00:00Z. Acceptance: there is one list that is categorized and flagged with 2025-09-07; the inventory of store 9004 has been verified; any available in-store substitutes (if any) are utilized; and there is a draft order for the slot with exclusively available items."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 207}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 424}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 433}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 207, "source_meal_plan_id": None, "created_by_user_id": 107, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[424,433]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 207, "anchor_date": "2025-09-07"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9004}),
    Action(name="ProposeSubstituteProducts", kwargs={"list_id": 8003, "store_id": 9004, "require_peanut_free": False}),
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id": 8003}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 207, "store_id": 9004, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-05T10:00:00Z", "scheduled_slot_end_ts": "2025-09-05T12:00:00Z"}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9004}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"list_id": 8003, "store_id": 9004}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_032",
        instruction=(
            "Coordinate the assembly of a five-day peanut-free school-lunch pack for the Martinez Household (household_id 202) in line with the child's targets (member_id 305) by choosing five Lunch recipes that meet the requirement of ≥20 g protein under the platform’s deterministic guidelines. Acceptance: a specific list exists containing those five lunches; items are categorized and flagged with 2025-09-07; the inventory of store 9002 is verified; any available in-store substitutes that adhere to peanut-free requirements are utilized; and the list status is \"ready\"."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 202}),
    Action(name="GetMemberTargets", kwargs={"member_id": 305}),
    Action(name="BuildRecipeFilters", kwargs={"meal_type": "Lunch", "min_protein_g": 20, "peanut_free": True, "cuisines_exclude": []}),
    Action(name="ListRecipesByFilters", kwargs={"filter_token": "F:Lunch:P20:PF1:EX"}),
    Action(name="MinimizeNewIngredients", kwargs={"recipe_ids_json": "[409,441,443,445,447]"}),
    Action(name="RankRecipesForTargets", kwargs={"recipe_ids_json": "[409,441,443,445,447]", "needed_count": 5, "target_calories": 1600, "target_protein": 45}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 202, "source_meal_plan_id": None, "created_by_user_id": 102, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[445,443,409,447,441]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 202, "anchor_date": "2025-09-07"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(
      name="ProposeSubstituteProducts",
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
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id": 8003}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"store_checked": 9002}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_033",
        instruction=(
            "Arrange four weeknight dinners for the Lee-Anderson Family (household_id 209) employing exactly recipes 401, 404, 407, and 435 for the week commencing 2025-09-08, and schedule a single order at store 9004 for delivery on 2025-09-06T14:00:00Z–16:00:00Z. Acceptance: the plan should be in place, accompanied by a grocery list that is categorized and flagged with the date 2025-09-07; verify the store 9004 inventory and apply any available in-store substitutes; ensure an order for the specified slot exists containing only available items with the status marked as “placed”. Return the generated meal_plan_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 209}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 401}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 404}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 407}),
    Action(name="GetRecipeById", kwargs={"recipe_id": 435}),
    Action(name="CreateMealPlan", kwargs={"household_id": 209, "week_start_date": "2025-09-08", "created_by_user_id": 109}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-08"}}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[401,404,407,435]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 209, "source_meal_plan_id": 6003, "created_by_user_id": 109, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,404,407,435]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2025-09-07"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9004}),
    Action(name="ProposeSubstituteProducts", kwargs={"list_id": 8003, "store_id": 9004, "require_peanut_free": False}),
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id": 8003}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "inventory_checked"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "inventory_checked", "payload_json": {"store_id": 9004}}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 209, "store_id": 9004, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-06T14:00:00Z", "scheduled_slot_end_ts": "2025-09-06T16:00:00Z"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"list_id": 8003, "store_id": 9004}}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9004}),
    Action(name="UpdateOrderStatus", kwargs={"order_id": 10003, "new_status": "placed"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ordered"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "order", "entity_id": 10003, "action_enum": "placed", "payload_json": {"list_id": 8003, "store_id": 9004}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ordered", "payload_json": {"order_id": 10003}})
  ],
  outputs=[
    "6003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_034",
        instruction=(
            "Develop a seven-day dinner schedule for the Rodriguez Household (household_id 208) for the week starting on 2025-09-08, ensuring no more than two dinners per cuisine, selected to align closely with the targets of the adult member (member_id 324) following the platform’s deterministic rules. Utilize the delivery slot 2025-09-07T10:00:00Z–12:00:00Z. Acceptance: the plan is verified; associated grocery list is categorized and tagged with the date 2025-09-07; check the store 9001 inventory and apply any in-store substitutes available; confirm that an order for this slot exists including only available items with the status “placed”."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 208}),
    Action(name="GetMemberTargets", kwargs={"member_id": 324}),
    Action(name="BuildRecipeFilters", kwargs={"meal_type": "Dinner", "min_protein_g": 20, "peanut_free": False, "cuisines_exclude": []}),
    Action(name="ListRecipesByFilters", kwargs={"filter_token": "F:Dinner:P20:PF0:EX"}),
    Action(name="ApplyCuisineCap", kwargs={"recipe_ids_json": "[402,404,405,407,408,423,425,427,428,429,430,433,434,435]", "max_per_cuisine": 2}),
    Action(name="RankRecipesForTargets", kwargs={"recipe_ids_json": "[402,404,405,407,408,423,425,427,429,430,434]", "needed_count": 7, "target_calories": 2400, "target_protein": 130}),
    Action(name="CreateMealPlan", kwargs={"household_id": 208, "week_start_date": "2025-09-08", "created_by_user_id": 108}),
    Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-08"}}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[425,407,423,404,427,402,429]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 208, "source_meal_plan_id": 6003, "created_by_user_id": 108, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[425,407,423,404,427,402,429]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 208, "anchor_date": "2025-09-07"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9001}),
    Action(
      name="ProposeSubstituteProducts",
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
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id": 8003}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"flags": ["pantry_staple","overlap_30d"], "categorized": True}}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 208, "store_id": 9001, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-07T10:00:00Z", "scheduled_slot_end_ts": "2025-09-07T12:00:00Z"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"list_id": 8003, "store_id": 9001, "slot": "2025-09-07T10:00:00Z/2025-09-07T12:00:00Z"}}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9001}),
    Action(name="UpdateOrderStatus", kwargs={"order_id": 10003, "new_status": "placed"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ordered"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "order", "entity_id": 10003, "action_enum": "placed", "payload_json": {"store_id": 9001}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ordered", "payload_json": {"order_id": 10003}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_035",
        instruction=(
            "Coordinate the creation of a peanut-free, no-heat school-lunch pack for the Martinez household (household_id=202) utilizing precisely recipes 409 and 410. The deliverable is a single grocery list under user_id=102 that captures only those two lunches and adheres to standard policy hygiene and auditing requirements. Refrain from placing an order or suggesting substitutions."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":202}),
    Action(name="GetUserById", kwargs={"user_id":102}),
    Action(name="BuildRecipeFilters", kwargs={"meal_type":"Lunch", "min_protein_g":0, "peanut_free":True, "cuisines_exclude":[]}),
    Action(name="ListRecipesByFilters", kwargs={"filter_token":"F:Lunch:P0:PF1:EX"}),
    Action(name="GetRecipeById", kwargs={"recipe_id":409}),
    Action(name="GetRecipeById", kwargs={"recipe_id":410}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":202, "source_meal_plan_id":None, "created_by_user_id":102, "status_enum":"initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id":202, "user_id":102, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"created", "payload_json":{"peanut_free":True, "no_heat":True}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003, "recipe_ids_json":"[409,410]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id":8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id":8003, "household_id":202, "anchor_date":"2025-08-31"})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_036",
        instruction=(
            "Organize three pantry-first dinners for Wang Solo (household_id=203) for the week commencing 2025-09-01, ensuring compliance with household policy (no repetitions in the past 30 days, cuisine variety, ≤3 non-staple ingredients) and suitability for the adult target member (member_id=306). Achieve success by producing a meal plan with exactly three dinners selected from {401, 404, 408} and one derived grocery list that fulfills standard policy hygiene at anchor_date=2025-08-31. Provide the constructed meal_plan_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":203}),
    Action(name="GetMemberTargets", kwargs={"member_id":306}),
    Action(name="ListRecentMealHistory", kwargs={"household_id":203, "days_back":30, "anchor_date":"2025-08-31"}),
    Action(name="ApplyCuisineCap", kwargs={"recipe_ids_json":"[404,408,401]", "max_per_cuisine":3}),
    Action(name="MinimizeNewIngredients", kwargs={"recipe_ids_json":"[404,408,401]", "max_new_ingredients_per_recipe":3}),
    Action(name="GetRecipeById", kwargs={"recipe_id":404}),
    Action(name="GetRecipeById", kwargs={"recipe_id":408}),
    Action(name="GetRecipeById", kwargs={"recipe_id":401}),
    Action(name="CreateMealPlan", kwargs={"household_id":203, "week_start_date":"2025-09-01", "created_by_user_id":103}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id":6003, "week_start_date":"2025-09-01", "selected_recipe_ids_json":"[404,408,401]"}),
    Action(name="LogAuditEvent", kwargs={"household_id":203, "user_id":103, "entity_type":"meal_plan", "entity_id":6003, "action_enum":"created", "payload_json":{"week_start_date":"2025-09-01"}}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":203, "source_meal_plan_id":6003, "created_by_user_id":103, "status_enum":"initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id":203, "user_id":103, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"created", "payload_json":{"source_meal_plan_id":6003}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003, "recipe_ids_json":"[404,408,401]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id":8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id":8003, "household_id":203, "anchor_date":"2025-08-31"})
  ],
  outputs=[
    "6003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_037",
        instruction=(
            "Coordinate a preparation for a peanut-safe, pantry-first breakfast replenishment for Davis Retirement (household_id=210) using exactly three Breakfast recipes from {418, 421, 439}. “Pantry-first” implies that staples undergo review per policy without adding any extra non-staple ingredients beyond the recipe combination. Formulate a single grocery list under user_id=110 that includes only those breakfasts and complies with standard policy hygiene as of anchor_date=2025-08-31. Avoid placing an order."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":210}),
    Action(name="GetUserById", kwargs={"user_id":110}),
    Action(name="BuildRecipeFilters", kwargs={"meal_type":"Breakfast", "min_protein_g":0, "peanut_free":True, "cuisines_exclude":[]}),
    Action(name="ListRecipesByFilters", kwargs={"filter_token":"F:Breakfast:P0:PF1:EX"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":210, "source_meal_plan_id":None, "created_by_user_id":110, "status_enum":"initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id":210, "user_id":110, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"created", "payload_json":{"peanut_free":True}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003, "recipe_ids_json":"[418,421,439]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id":8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id":8003, "household_id":210, "anchor_date":"2025-08-31"})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_038",
        instruction=(
            "Handle a GreenGrocer Digital delivery for the Brown-Brown Family (household_id=204) using recipe 404 within the 2025-09-05T16:00:00Z–18:00:00Z pickup/delivery timeframe at store_id=9001. Ensure that one order is created and marked as 'placed' utilizing policy inventory guidelines (prioritize lowest-price in-stock/low items only; exclude unavailable items if no valid substitute is available), and ensure a single audit event logs the placement. Provide the generated order_id and the final total_cents."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":204}),
    Action(name="GetUserById", kwargs={"user_id":104}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":204, "source_meal_plan_id":None, "created_by_user_id":104, "status_enum":"initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003, "recipe_ids_json":"[404]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id":8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id":8003, "household_id":204, "anchor_date":"2025-08-31"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id":8003, "store_id":9001}),
    Action(name="SetGroceryListStatus", kwargs={"list_id":8003, "status_enum":"finalized"}),
    Action(name="CreateOrderFromList", kwargs={"household_id":204, "store_id":9001, "list_id":8003, "scheduled_slot_start_ts":"2025-09-05T16:00:00Z", "scheduled_slot_end_ts":"2025-09-05T18:00:00Z"}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id":10003, "store_id":9001, "product_overrides":{}}),
    Action(name="UpdateOrderStatus", kwargs={"order_id":10003, "new_status":"placed"}),
    Action(name="LogAuditEvent", kwargs={"household_id":204, "user_id":104, "entity_type":"order", "entity_id":10003, "action_enum":"placed", "payload_json":{"list_id":8003, "store_id":9001}})
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
            "Organize a five-day set of peanut-free school lunches for the Rodriguez Household (household_id=208), focusing on protein (≥12 g/serving). To succeed, select five Lunch recipes from {409, 410, 411, 412, 413} adhering to the ≤4 non-staple-ingredients guideline. Use user_id=108 to generate a grocery list accurately reflecting the compiled recipes with proper section categorization and updated pantry and 30-day overlap indicators as of anchor_date=2025-08-31. Ensure audits for both meal-plan creation and list creation are in place. There is no need to assess store inventory or place orders."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":208}),
    Action(name="BuildRecipeFilters", kwargs={"meal_type":"Lunch", "min_protein_g":12, "peanut_free":True, "cuisines_exclude":[]}),
    Action(name="ListRecipesByFilters", kwargs={"filter_token":"F:Lunch:P12:PF1:EX"}),
    Action(name="MinimizeNewIngredients", kwargs={"recipe_ids_json":"[409,410,411,412,413]", "max_new_ingredients_per_recipe":4}),
    Action(name="CreateMealPlan", kwargs={"household_id":208, "week_start_date":"2025-09-01", "created_by_user_id":108}),
    Action(name="LogAuditEvent", kwargs={"household_id":208, "user_id":108, "entity_type":"meal_plan", "entity_id":6003, "action_enum":"created", "payload_json":{"week_start_date":"2025-09-01"}}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id":6003, "week_start_date":"2025-09-01", "selected_recipe_ids_json":"[409,410,411,412,413]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":208, "source_meal_plan_id":6003, "created_by_user_id":108, "status_enum":"initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id":208, "user_id":108, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"created", "payload_json":{"peanut_free":True}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003, "recipe_ids_json":"[409,410,411,412,413]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id":8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id":8003, "household_id":208, "anchor_date":"2025-08-31"})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_040",
        instruction=(
            "Prepare a peanut-free Lunch grocery list for the Wang Solo household (household_id 203) using lunch recipes 409, 410, and 412 (no meal plan needed). The list should present aggregated ingredient quantities per (ingredient_id, unit), categorized by sections, with pantry-staple and last-30-days overlap flags set using 2025-09-07 as the reference date. Finalize the list in 'ready' status, ensuring an audit of this state is conducted."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 203}),
    Action(name="GetUserById", kwargs={"user_id": 103}),
    Action(
      name="CreateEmptyGroceryList",
      kwargs={"household_id": 203, "source_meal_plan_id": None, "created_by_user_id": 103, "status_enum": "initialized"},
    ),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,412]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(
      name="FlagOverlapLastMonthOnList",
      kwargs={"list_id": 8003, "household_id": 203, "anchor_date": "2025-09-07"},
    ),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(
      name="LogAuditEvent",
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
            "Handle the preparation of a pantry-first Dinner grocery list for the Peterson Couple (household_id 206) utilizing recipes 408 and 405 (without a meal plan). Ensure the final list displays aggregated quantities per (ingredient_id, unit), fully detailed grocery sections, and both pantry-staple and last-30-days overlap flags calculated using 2025-09-07 as the reference. Leave it in 'ready' status along with an audit indicating this state."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 206}),
    Action(name="GetUserById", kwargs={"user_id": 106}),
    Action(
      name="CreateEmptyGroceryList",
      kwargs={"household_id": 206, "source_meal_plan_id": None, "created_by_user_id": 106, "status_enum": "initialized"},
    ),
    Action(
      name="LogAuditEvent",
      kwargs={
        "household_id": 206,
        "user_id": 106,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "created",
        "payload_json": {"status": "initialized", "list_id": 8003, "source_meal_plan_id": None},
      },
    ),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[408,405]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(
      name="FlagOverlapLastMonthOnList",
      kwargs={"list_id": 8003, "household_id": 206, "anchor_date": "2025-09-07"},
    ),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(
      name="LogAuditEvent",
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
            "Coordinate the planning of five peanut-optional Dinners for the Brown Large Family (household_id 207) for the week commencing 2025-09-15, aimed at adult dietary targets (≈2300 kcal, 125g protein) without repeating meals from the previous 14 days and with no more than two from each cuisine. Connect the resulting plan to a single grocery list that features categorized sections, pantry-staple flags, and last-30-days overlap flags, using 2025-09-21 as the basis. Ensure the list remains in 'ready' status, with all necessary audits documented. Acceptance criteria: a new meal plan containing five Dinner entries; one linked list with detailed sections, pantry, and overlap flags; list status marked 'ready'; audits include the meal plan creation and list lifecycle."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 207}),
    Action(name="BuildRecipeFilters", kwargs={"meal_type": "Dinner", "min_protein_g": 25, "peanut_free": False, "cuisines_exclude": []}),
    Action(name="ListRecipesByFilters", kwargs={"filter_token": "F:Dinner:P25:PF0:EX"}),
    Action(name="ListRecentMealHistory", kwargs={"household_id": 207, "days_back": 14, "anchor_date": "2025-09-21"}),
    Action(
      name="ExcludeRecipeIds",
      kwargs={"candidate_recipe_ids_json": "[402,404,407,423,425,427,428,429,430,434,435]", "exclude_recipe_ids": []},
    ),
    Action(
      name="ApplyCuisineCap",
      kwargs={"recipe_ids_json": "[402,404,407,423,425,427,428,429,430,434,435]", "max_per_cuisine": 2},
    ),
    Action(
      name="RankRecipesForTargets",
      kwargs={"recipe_ids_json": "[402,404,407,423,425,427,429,430,434]", "needed_count": 5, "target_calories": 2300, "target_protein": 125},
    ),
    Action(name="CreateMealPlan", kwargs={"household_id": 207, "week_start_date": "2025-09-15", "created_by_user_id": 107}),
    Action(
      name="LogAuditEvent",
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
      name="BulkAddMealPlanEntries",
      kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-15", "selected_recipe_ids_json": "[425,407,423,404,427]"},
    ),
    Action(
      name="CreateEmptyGroceryList",
      kwargs={"household_id": 207, "source_meal_plan_id": 6003, "created_by_user_id": 107, "status_enum": "initialized"},
    ),
    Action(
      name="LogAuditEvent",
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
      name="UpsertGroceryListItemsFromRecipes",
      kwargs={"list_id": 8003, "recipe_ids_json": "[425,407,423,404,427]"},
    ),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(
      name="FlagOverlapLastMonthOnList",
      kwargs={"list_id": 8003, "household_id": 207, "anchor_date": "2025-09-21"},
    ),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(
      name="LogAuditEvent",
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
            "Handle the creation of a peanut-free, no-heat school-lunch pack for the “Martinez Household” (household_id=202) by selecting exactly five lunch recipes with a prep time ≤10 minutes. Choose the five recipes with the lowest recipe_id values from the filtered options, organize a ready grocery list with applied categories; flag pantry staples and 30-day overlaps with anchor_date=2025-09-08, document audits for list creation and finalization, and return the created list_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":202}),
    Action(name="GetUserById", kwargs={"user_id":102}),
    Action(name="BuildRecipeFilters", kwargs={"meal_type":"Lunch","peanut_free":True,"no_heat":True,"max_prep_minutes":10}),
    Action(name="ListRecipesByFilters", kwargs={"filter_token":"F:Lunch:P0:PF1:EX"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":202,"created_by_user_id":102,"status_enum":"initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id":202,"user_id":102,"entity_type":"grocery_list","entity_id":8003,"action_enum":"grocery_list_created","payload_json":{"status":"initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[409,410,411,412,413]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id":8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id":8003,"household_id":202,"anchor_date":"2025-09-08"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id":8003,"status_enum":"ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id":202,"user_id":102,"entity_type":"grocery_list","entity_id":8003,"action_enum":"grocery_list_status_set","payload_json":{"status":"ready"}})
  ],
  outputs=["8003"]
),

Task(
  annotator="saaish2",
  user_id="task_044",
        instruction=(
            "Coordinate a breakfast starter list for the “Rodriguez Household” (household_id=208) using recipes 418 and 421. Produce a single ready grocery list with categorized sections, flag pantry staples, signal overlaps with anchor_date=2025-09-05, and log audit events for list creation and finalization."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":208}),
    Action(name="GetUserById", kwargs={"user_id":108}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":208,"created_by_user_id":108,"status_enum":"initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id":208,"user_id":108,"entity_type":"grocery_list","entity_id":8003,"action_enum":"grocery_list_created","payload_json":{"status":"initialized"}}),
    Action(name="GetRecipeById", kwargs={"recipe_id":418}),
    Action(name="GetRecipeById", kwargs={"recipe_id":421}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[418,421]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id":8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id":8003,"household_id":208,"anchor_date":"2025-09-05"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id":8003,"status_enum":"ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id":208,"user_id":108,"entity_type":"grocery_list","entity_id":8003,"action_enum":"grocery_list_status_set","payload_json":{"status":"ready"}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_045",
        instruction=(
            "Handle the creation of a light snack bundle for the “Davis Retirement” household (household_id=210) using precisely two snack recipes (recipe_id ∈ {449, 450}). Provide a single consolidated grocery list for household_id=210 with categorized sections, pantry staples marked, 30-day overlaps flagged with anchor_date=2025-09-05, and audit events for both list creation and finalization included."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":210}),
    Action(name="GetUserById", kwargs={"user_id":110}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":210,"created_by_user_id":110,"status_enum":"initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id":210,"user_id":110,"entity_type":"grocery_list","entity_id":8003,"action_enum":"grocery_list_created","payload_json":{"status":"initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[449,450]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id":8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id":8003,"household_id":210,"anchor_date":"2025-09-05"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id":8003,"status_enum":"ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id":210,"user_id":110,"entity_type":"grocery_list","entity_id":8003,"action_enum":"grocery_list_status_set","payload_json":{"status":"ready"}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_046",
        instruction=(
            "Coordinate the finalization of the Bennett Family’s current grocery list (ID 8001) by identifying pantry staples and overlapping items from the last 30 days using their meal history. Change the list status to “ready” and log an audit for this transition. Acceptance criteria: for list 8001, ensure pantry_staple_flag and overlap_last_month_flag are updated for all items; status_enum == 'ready'; and there is one audit recorded for this change."
        ),
  actions=[
    Action(name="GetGroceryListDetails", kwargs={"list_id": 8001}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8001}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8001, "household_id": 201}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8001, "status_enum": "ready"}),
    Action(
      name="LogAuditEvent",
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
            "Prepare a peanut-free school-lunch grocery list for the Rodriguez Household utilizing precisely these Lunch recipe IDs: 409, 410, 444. Organize items by store section, identify pantry staples, and maintain an audit of the list creation process. Set the list status to 'initialized'. Finally, provide the grocery_list_id that you established."
        ),
  actions=[
    Action(
      name="CreateEmptyGroceryList",
      kwargs={"household_id": 208, "created_by_user_id": 108, "status_enum": "initialized"}
    ),
    Action(
      name="UpsertGroceryListItemsFromRecipes",
      kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,444]"}
    ),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(
      name="LogAuditEvent",
      kwargs={
        "household_id": 208,
        "user_id": 108,
        "entity_type": "grocery_list",
        "entity_id": 8003,
        "action_enum": "created_from_lunches",
        "payload_json": {"list_id": 8003, "recipes": [409, 410, 444]}
      }
    ),
    Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),
  ],
  outputs=["8003"]
),

Task(
  annotator="saaish2",
  user_id="task_048",
        instruction=(
            "Formulate a seven-lunch meal plan for the Brown Large Family (household_id=207) for the week commencing on 2025-09-08 under user_id=107 using exactly these recipes in sequence: [409,410,411,412,441,442,447]. Success entails creating a single new meal_plans row with seven Lunch entries for those recipes starting 2025-09-08, along with one audit event documenting the plan creation. Return the stored week_start_date for the devised plan."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":207}),
    Action(name="GetUserById", kwargs={"user_id":107}),
    Action(name="CreateMealPlan", kwargs={"household_id":207,"week_start_date":"2025-09-08","created_by_user_id":107}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-08","selected_recipe_ids_json":"[409,410,411,412,441,442,447]"}),
    Action(name="LogAuditEvent", kwargs={"household_id":207,"user_id":107,"entity_type":"meal_plan","entity_id":6003,"action_enum":"plan_created","payload_json":{"week_start":"2025-09-08","entries":7}}),
  ],
  outputs=[
    "2025-09-08"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_049",
        instruction=(
            "Re-categorize the current Martinez Household grocery list (ID 8002), maintaining its status as 'initialized', verify stock at FoodExpress (store_id 9002), and document an audit of the inventory inspection. Acceptance: for list 8002, grocery sections are specified, status_enum == 'initialized', and one audit is documented for the inventory examination."
        ),
  actions=[
    Action(name="GetGroceryListDetails", kwargs={"list_id": 8002}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8002}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8002, "status_enum": "initialized"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8002, "store_id": 9002}),
    Action(
      name="LogAuditEvent",
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
            "Prepare a compact Dinner grocery list for the Brown-Brown Family using precisely these two Dinner recipe IDs: 431 and 432. Add items from these recipes, identify any last-30-day overlap with household meals, assign the list status to 'ready', and register an audit of the update. Acceptance: a new list containing items exclusively from 431 and 432 is present, overlap indicators set, status_enum == 'ready', and an audit registered."
        ),
  actions=[
    Action(
      name="CreateEmptyGroceryList",
      kwargs={"household_id": 204, "created_by_user_id": 104, "status_enum": "initialized"}
    ),
    Action(
      name="UpsertGroceryListItemsFromRecipes",
      kwargs={"list_id": 8003, "recipe_ids_json": "[431,432]"}
    ),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 204}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(
      name="LogAuditEvent",
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
            "Handle creating a peanut-free Lunch grocery list for the Lee-Anderson Family using precisely these Lunch recipe IDs: 441 and 445. Populate the items, verify their availability at Wellness Foods Hub (store_id 9006), and log an audit of this availability verification. Leave the list in 'initialized' status. Acceptance: a fresh list is created containing only the specified recipes, availability is checked at store 9006, and an audit is documented."
        ),
  actions=[
    Action(
      name="CreateEmptyGroceryList",
      kwargs={"household_id": 209, "created_by_user_id": 109, "status_enum": "initialized"}
    ),
    Action(
      name="UpsertGroceryListItemsFromRecipes",
      kwargs={"list_id": 8003, "recipe_ids_json": "[441,445]"}
    ),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9006}),
    Action(
      name="LogAuditEvent",
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
            "Coordinate the creation of a standalone grocery list for the household “Wang Solo” (household_id=203) under created_by_user_id=103, not associated with any meal plan, and gathered from exactly these recipes: [401, 402]. Successful completion requires a single new grocery_lists row for that household, with items collected from those recipes and status ‘initialized’; record one audit of the list creation. Return the new list_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":203}),
    Action(name="GetUserById", kwargs={"user_id":103}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":203,"source_meal_plan_id":None,"created_by_user_id":103,"status_enum":"initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[401,402]"}),
    Action(name="LogAuditEvent", kwargs={"household_id":203,"user_id":103,"entity_type":"grocery_lists","entity_id":8003,"action_enum":"list_created","payload_json":{"recipe_ids":[401,402]}})
  ],
  outputs=["8003"]
),

Task(
  annotator="saaish2",
  user_id="task_053",
        instruction=(
            "Ensure the finalization and refreshing of hygiene for the existing grocery list list_id=8002 for the “Martinez Household” (household_id=202). Success is achieved when the sections of the list are updated using ingredient metadata, the pantry_staple_flag remains consistent, and the list status is changed to ‘finalized’ with a recorded audit."
        ),
  actions=[
    Action(name="GetGroceryListDetails", kwargs={"list_id":8002}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8002}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id":8002}),
    Action(name="SetGroceryListStatus", kwargs={"list_id":8002,"status_enum":"finalized"}),
    Action(name="LogAuditEvent", kwargs={"household_id":202,"user_id":102,"entity_type":"grocery_lists","entity_id":8002,"action_enum":"list_finalized","payload_json":{"status_after":"finalized"}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_054",
        instruction=(
            "Apply 30-day overlap flags for the “Martinez Household” (household_id=202) on grocery list list_id=8002, using anchor_date=2025-08-31. Success is attained when each grocery_list_items row in that list has overlap_last_month_flag appropriately set according to the household’s meal history over the last 30 days, and an audit is logged."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":202}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id":8002,"household_id":202,"anchor_date":"2025-08-31"}),
    Action(name="LogAuditEvent", kwargs={"household_id":202,"user_id":102,"entity_type":"grocery_lists","entity_id":8002,"action_enum":"overlap_flags_updated","payload_json":{"anchor_date":"2025-08-31"}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_055",
        instruction=(
            "Prepare a concise two-dinner menu for the “Rodriguez Household” (household_id=208) for the week commencing 2025-09-01 under created_by_user_id=108, utilizing these dinner recipes in sequence: [406, 407]. Success involves generating a single new meal_plans row for that week linked to that household and ensuring exactly two Dinner entries are included. Provide the created meal_plan_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":208}),
    Action(name="CreateMealPlan", kwargs={"household_id":208,"week_start_date":"2025-09-01","created_by_user_id":108}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-01","selected_recipe_ids_json":"[406,407]"}),
    Action(name="LogAuditEvent", kwargs={"household_id":208,"user_id":108,"entity_type":"meal_plans","entity_id":6003,"action_enum":"meal_plan_created","payload_json":{"week_start_date":"2025-09-01","entry_count":2}})
  ],
  outputs=["6003"]
),

Task(
  annotator="saaish2",
  user_id="task_056",
        instruction=(
            "For the existing plan meal_plan_id=6002 of the “Martinez Household”, apply the standard child-friendly modification note to recipe_id=407 and save it to the corresponding Dinner entry. Success means that the entry’s notes match the fixed child-mods template, and an audit is duly recorded."
        ),
  actions=[
    Action(name="GetMealPlanDetails", kwargs={"meal_plan_id":6002}),
    Action(name="GenerateChildModifications", kwargs={"recipe_ids_json":"[407]"}),
    Action(name="UpdateMealPlanEntryNotes", kwargs={"meal_plan_id":6002,"notes_map":{"407":"Reduce spice for kids. Child-friendly: mild seasoning; cut to bite-size; soft textures."}}),
    Action(name="LogAuditEvent", kwargs={"household_id":202,"user_id":102,"entity_type":"meal_plans","entity_id":6002,"action_enum":"entry_notes_updated","payload_json":{"recipe_id":407}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_057",
        instruction=(
            "Arrange a quick grocery list for the “Brown Large Family” (household_id=207) using exactly these two dinner recipes: [401, 402]. Completing this task requires adding one new grocery_lists row for that household, compiling items from those recipes, updating grocery sections, and recording a creation audit."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":207}),
    Action(name="GetUserById", kwargs={"user_id":107}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":207,"source_meal_plan_id":None,"created_by_user_id":107,"status_enum":"initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[401,402]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
    Action(name="LogAuditEvent", kwargs={"household_id":207,"user_id":107,"entity_type":"grocery_lists","entity_id":8003,"action_enum":"list_created","payload_json":{"recipe_ids":[401,402]}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_058",
        instruction=(
            "Develop a 5-night Dinner mini-plan for the Wang Solo household (household_id 203) starting the week of 2025-09-08 using these recipes in precise order: 401, 402, 403, 404, 405. Generate one grocery list tied to that plan from those recipes, assess 30-day overlap flags using 2025-09-14 as the reference point, and ensure the list is in 'ready' status. Successful task means a meal plan with five Dinner entries from 2025-09-08 to 2025-09-12 in the specified order; one linked grocery list compiled from those recipes with overlap flags set; list status as 'ready'; precisely two audits recorded (plan created; list ready). Provide the meal_plan_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 203}),
    Action(name="GetUserById", kwargs={"user_id": 103}),
    Action(name="CreateMealPlan", kwargs={"household_id": 203, "week_start_date": "2025-09-08", "created_by_user_id": 103}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[401,402,403,404,405]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 203, "source_meal_plan_id": 6003, "created_by_user_id": 103, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,402,403,404,405]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 203, "anchor_date": "2025-09-14"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-08"}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"status": "ready"}})
  ],
  outputs=[
    "6003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_059",
        instruction=(
            "Manage the assembly of a peanut-free weekday Lunch list for the Brown-Brown Family (household_id 204) using precisely these Lunch recipes: 409, 410, 412, 445. Adhere to peanut-free constraints when verifying item availability at FoodExpress (store_id 9002). Arrange a delivery order for 2025-09-03T10:00:00Z–2025-09-03T12:00:00Z, include all available items at the best price, leave the order in 'placed' status, and assign the list to 'ordered'. Acceptance involves one list compiled from those recipes; checking inventory at store 9002; applying safe substitutions when deterministically available; creating one order filled only with available items; order 'placed'; list 'ordered'; audits encompassing order creation, order placed, and list ordered in sequence."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 204}),
    Action(name="GetUserById", kwargs={"user_id": 104}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 204, "source_meal_plan_id": None, "created_by_user_id": 104, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,412,445]"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(name="ProposeSubstituteProducts", kwargs={"store_id": 9002, "flagged_items": [{"ingredient_id": 1001}, {"ingredient_id": 1005}, {"ingredient_id": 1013}, {"ingredient_id": 1014}, {"ingredient_id": 1015}, {"ingredient_id": 1024}, {"ingredient_id": 1043}, {"ingredient_id": 1044}, {"ingredient_id": 1089}], "require_peanut_free": True}),
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id": 8003, "substitutions": []}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 204, "store_id": 9002, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-03T10:00:00Z", "scheduled_slot_end_ts": "2025-09-03T12:00:00Z"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"store_id": 9002, "slot_start": "2025-09-03T10:00:00Z", "slot_end": "2025-09-03T12:00:00Z"}}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9002}),
    Action(name="UpdateOrderStatus", kwargs={"order_id": 10003, "new_status": "placed"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ordered"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "order", "entity_id": 10003, "action_enum": "placed", "payload_json": {"store_id": 9002}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ordered", "payload_json": {"status": "ordered"}})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_060",
        instruction=(
            "Coordinate the delivery of a vegetarian Dinner plan for the Shah Extended Family (household_id 205) spanning 2025-09-15 to 2025-09-18, utilizing precisely these four recipes in this sequence: 405, 424, 426, 432. Acceptance includes four Dinner entries dated from 2025-09-15 through 2025-09-18 in the specified sequence; a singular linked grocery list consolidated from those recipes with 30-day overlap flags assessed using 2025-09-14 as the reference; list status 'ready'; exactly two audits recorded (plan created; list ready). Provide the grocery_list_id and the total number of items."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 205}),
    Action(name="GetUserById", kwargs={"user_id": 105}),
    Action(name="CreateMealPlan", kwargs={"household_id": 205, "week_start_date": "2025-09-15", "created_by_user_id": 105}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-15", "selected_recipe_ids_json": "[405,424,426,432]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 205, "source_meal_plan_id": 6003, "created_by_user_id": 105, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[405,424,426,432]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 205, "anchor_date": "2025-09-14"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-15"}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"status": "ready"}})
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
            "Handle the preparation of a peanut-free school-lunch list for the Lee-Anderson Family (household_id 209) utilizing precisely these Lunch recipes: 441, 442, 444. Establish 30-day overlap flags using 2025-09-07 as the reference point, assess availability at FoodExpress (store_id 9002) adhering to the peanut-safe substitution policy, apply secure in-store substitutions if feasible, and set the list status to 'ready'. Document audits for both the list creation and its readiness. Acceptance: a single grocery list compiled from those recipes; overlap flags activated; inventory verified at 9002 respecting peanut-free substitutions; status 'ready'; two audits. Return the grocery_list_id and the total item count."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 209}),
    Action(name="GetUserById", kwargs={"user_id": 109}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 209, "source_meal_plan_id": None, "created_by_user_id": 109, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[441,442,444]"}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2025-09-07"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(name="ProposeSubstituteProducts", kwargs={"store_id": 9002, "flagged_items": [{"ingredient_id": 1009}, {"ingredient_id": 1013}, {"ingredient_id": 1014}, {"ingredient_id": 1020}, {"ingredient_id": 1024}, {"ingredient_id": 1043}, {"ingredient_id": 1044}, {"ingredient_id": 1070}, {"ingredient_id": 1090}, {"ingredient_id": 1109}], "require_peanut_free": True}),
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id": 8003, "substitutions": []}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"status": "ready"}})
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
            "Coordinate the creation of a 4-night, low-prep Dinner plan for the Davis Retirement household (household_id 210) spanning from 2025-09-05 to 2025-09-08 using these recipes in the specified sequence: 435, 428, 423, 425. Generate one linked grocery list from those recipes, verify store availability at GreenGrocer Digital (store_id 9001) with deterministic in-store substitutions where available, and arrange delivery for 2025-09-05T17:00:00Z–2025-09-05T19:00:00Z. Ensure the order is marked 'placed' and the list 'ordered'. Acceptance: one plan with four Dinner entries dated 2025-09-05 through 2025-09-08; one linked list; availability checked with deterministic substitutions applied; one order created containing only available items; order 'placed'; list 'ordered'; audits captured for meal plan creation, grocery list formation, order generation, order placement, and list ordering."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 210}),
    Action(name="GetUserById", kwargs={"user_id": 110}),
    Action(name="CreateMealPlan", kwargs={"household_id": 210, "week_start_date": "2025-09-05", "created_by_user_id": 110}),
    Action(
      name="LogAuditEvent",
      kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-05"}}
    ),
    Action(
      name="BulkAddMealPlanEntries",
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
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 210, "source_meal_plan_id": 6003, "created_by_user_id": 110, "status_enum": "initialized"}),
    Action(
      name="LogAuditEvent",
      kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}
    ),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[435,428,423,425]"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9001}),
    Action(
      name="CreateOrderFromList",
      kwargs={"household_id": 210, "store_id": 9001, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-05T17:00:00Z", "scheduled_slot_end_ts": "2025-09-05T19:00:00Z"}
    ),
    Action(
      name="AddOrderItemsFromList",
      kwargs={
        "order_id": 10003,
        "store_id": 9001,
        "only_in_stock": True,
        "allow_instore_substitutions": True,
        "price_strategy": "lowest"
      }
    ),
    Action(
      name="UpdateOrderStatus",
      kwargs={"order_id": 10003, "new_status": "placed"}
    ),
    Action(
      name="SetGroceryListStatus",
      kwargs={"list_id": 8003, "status_enum": "ordered"}
    ),
    Action(
      name="LogAuditEvent",
      kwargs={"household_id": 210, "user_id": 110, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"store_id": 9001}}
    ),
    Action(
      name="LogAuditEvent",
      kwargs={"household_id": 210, "user_id": 110, "entity_type": "order", "entity_id": 10003, "action_enum": "placed", "payload_json": {"store_id": 9001}}
    ),
    Action(
      name="LogAuditEvent",
      kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ordered", "payload_json": {"status": "ordered"}}
    ),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_063",
        instruction=(
            "Coordinate the preparation of a singular, independent grocery order for the “Bennett Family” (household_id=201) under user_id=101 utilizing exactly recipes [401, 402]. Adhere to store 9001 availability, apply any in-store substitutions before proceeding to checkout, arrange the order for 2025-01-02T10:00:00Z–12:00:00Z, and conclude with the grocery list marked as “ordered.” Document audits for both the creation and ordering of the list, as well as the creation and placement of the order."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":201}),
    Action(name="GetUserById", kwargs={"user_id":101}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":201,"source_meal_plan_id":None,"created_by_user_id":101,"status_enum":"initialized"}),
    Action(name="LogAuditEvent", kwargs={
      "household_id":201,"user_id":101,"entity_type":"grocery_list","entity_id":8003,
      "action_enum":"created","payload_json":{"status":"initialized"}
    }),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[401,402]"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id":8003,"store_id":9001}),
    Action(name="ProposeSubstituteProducts", kwargs={
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
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id":8003,"substitutions":[]}),
    Action(name="CreateOrderFromList", kwargs={
      "household_id":201,"store_id":9001,"list_id":8003,
      "scheduled_slot_start_ts":"2025-01-02T10:00:00Z","scheduled_slot_end_ts":"2025-01-02T12:00:00Z"
    }),
    Action(name="LogAuditEvent", kwargs={
      "household_id":201,"user_id":101,"entity_type":"order","entity_id":10003,
      "action_enum":"created","payload_json":{"store_id":9001}
    }),
    Action(name="AddOrderItemsFromList", kwargs={"order_id":10003,"store_id":9001}),
    Action(name="UpdateOrderStatus", kwargs={"order_id":10003,"new_status":"placed"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id":8003,"status_enum":"ordered"}),
    Action(name="LogAuditEvent", kwargs={
      "household_id":201,"user_id":101,"entity_type":"order","entity_id":10003,
      "action_enum":"placed","payload_json":{"store_id":9001}
    }),
    Action(name="LogAuditEvent", kwargs={
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
            "Initiate a new order (order shell) for the Bennett Family (household_id=201) at GreenGrocer Digital (store_id=9001) using the existing grocery list 8001, planned for 2025-09-02T16:00:00Z–18:00:00Z, and fill order_items by selecting the lowest-price in-stock products according to policy. Log one audit event for order creation. Keep the order status unchanged."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":201}),
    Action(name="GetUserById", kwargs={"user_id":101}),
    Action(name="CreateOrderFromList", kwargs={"household_id":201,"store_id":9001,"list_id":8001,"scheduled_slot_start_ts":"2025-09-02T16:00:00Z","scheduled_slot_end_ts":"2025-09-02T18:00:00Z"}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id":10003,"store_id":9001}),
    Action(name="LogAuditEvent", kwargs={"household_id":201,"user_id":101,"entity_type":"order","entity_id":10003,"action_enum":"order_created","payload_json":"{\"source_list\":8001}"}),
  ],
  outputs=[
  ]
),

Task(
  annotator="saaish2",
  user_id="task_065",
        instruction=(
            "Handle a family grocery run for the “Brown Large Family” (household_id=207) under user_id=107 utilizing recipes [423, 425, 435] as a single cohesive list. Success indicates that store 9003 availability is adhered to, with in-store substitutions applied as necessary before placing a unified order for 2025-01-02T10:00:00Z–12:00:00Z using the lowest-priced available items; the grocery list achieves the status “ordered”; and audits document the order’s creation, placement, and the final ordering of the list."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":207}),
    Action(name="GetUserById", kwargs={"user_id":107}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":207,"source_meal_plan_id":None,"created_by_user_id":107,"status_enum":"initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[423,425,435]"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id":8003,"store_id":9003}),
    Action(name="ProposeSubstituteProducts", kwargs={
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
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id":8003,"substitutions":[]}),
    Action(name="CreateOrderFromList", kwargs={
      "household_id":207,"store_id":9003,"list_id":8003,
      "scheduled_slot_start_ts":"2025-01-02T10:00:00Z","scheduled_slot_end_ts":"2025-01-02T12:00:00Z"
    }),
    Action(name="LogAuditEvent", kwargs={
      "household_id":207,"user_id":107,"entity_type":"order","entity_id":10003,
      "action_enum":"created","payload_json":{"store_id":9003}
    }),
    Action(name="AddOrderItemsFromList", kwargs={"order_id":10003,"store_id":9003}),
    Action(name="UpdateOrderStatus", kwargs={"order_id":10003,"new_status":"placed"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id":8003,"status_enum":"ordered"}),
    Action(name="LogAuditEvent", kwargs={
      "household_id":207,"user_id":107,"entity_type":"order","entity_id":10003,
      "action_enum":"placed","payload_json":{"store_id":9003}
    }),
    Action(name="LogAuditEvent", kwargs={
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
            "Coordinate the delivery of a seven-night dinner plan for the “Martinez Household” (household_id=202) for the week starting 2025-09-15 under user_id=102, using recipes [441, 442, 444, 435, 428, 423, 425]. Develop one integrated grocery list, apply categorization and pantry-staples organization, set 30-day overlap flags at anchor_date=2025-08-31, finalize the list, and ensure audits are recorded for both the creation of the meal plan and the finalization of the grocery list exclusively."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":202}),
    Action(name="GetUserById", kwargs={"user_id":102}),
    Action(name="CreateMealPlan", kwargs={"household_id":202,"week_start_date":"2025-09-15","created_by_user_id":102}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-15","selected_recipe_ids_json":"[441,442,444,435,428,423,425]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":202,"source_meal_plan_id":6003,"created_by_user_id":102,"status_enum":"initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[441,442,444,435,428,423,425]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id":8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id":8003,"household_id":202,"anchor_date":"2025-08-31"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id":8003,"status_enum":"finalized"}),
    Action(name="LogAuditEvent", kwargs={
      "household_id":202,"user_id":102,"entity_type":"meal_plan","entity_id":6003,
      "action_enum":"created","payload_json":{"week_start_date":"2025-09-15"}
    }),
    Action(name="LogAuditEvent", kwargs={
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
            "Handle the task of compiling a peanut-free school-lunch grocery list for the Shah Extended Family (household_id 205) using exactly these seven Lunch recipe IDs: 409, 410, 412, 413, 441, 444, 445. Consolidate items, organize grocery sections, and set the list as ready while documenting an audit for the readiness status change. Acceptance: one grocery list for household 205 with items consolidated from exactly the seven recipes specified; grocery sections completed; list status = 'ready'; an audit is recorded marking the transition from 'initialized' to 'ready'. Return the list_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 205}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 205, "created_by_user_id": 105, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,412,413,441,444,445]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"from": "initialized", "to": "ready"}}),
  ],
  outputs=["8003"]
),

Task(
  annotator="saaish2",
  user_id="task_068",
        instruction=(
            "Coordinate the creation of a 7-night Dinner plan for the Rodriguez Household (household_id 208) for the week commencing 2025-09-08 using exactly these recipe IDs in sequence: 401, 402, 425, 427, 428, 431, 433. Associate a grocery list with that plan and consolidate items; ensure pantry-staple flags are marked. Acceptance: one meal plan with seven Dinner entries from 2025-09-08 through 2025-09-14 in the specified order; a linked grocery list with aggregated items and pantry flags; list status remains 'initialized'. Return the meal_plan_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 208}),
    Action(name="GetUserById", kwargs={"user_id": 108}),
    Action(name="CreateMealPlan", kwargs={"household_id": 208, "week_start_date": "2025-09-08", "created_by_user_id": 108}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[401,402,425,427,428,431,433]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 208, "source_meal_plan_id": 6003, "created_by_user_id": 108, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,402,425,427,428,431,433]"}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
  ],
  outputs=["6003"]
),

Task(
  annotator="saaish2",
  user_id="task_069",
        instruction=(
            "Handle the assembly of a 5-day peanut-free school-lunch list for the Brown Large Family (household_id 207) using specifically these Lunch recipe IDs: 409, 410, 411, 412, 413; subsequently verify availability at FoodExpress (store_id 9002), schedule an order for the time window 2025-09-03T10:00:00Z–2025-09-03T12:00:00Z, and fill it with the lowest-price items that are marked as 'in_stock' or 'low' at that store. Review the key stages: list assembly, inventory verification, order scheduling, and item selection. Leave the order in its initial status. Acceptance involves having one grocery list with items consolidated from those five recipes; confirmation of inventory at store 9002; one order initialized with only available items; necessary audit events present. Provide the order_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 207}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 207, "created_by_user_id": 107, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,411,412,413]"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "inventory_checked", "payload_json": {"store_id": 9002}}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 207, "store_id": 9002, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-03T10:00:00Z", "scheduled_slot_end_ts": "2025-09-03T12:00:00Z"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"store_id": 9002}}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9002}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "order", "entity_id": 10003, "action_enum": "items_added", "payload_json": {"source_list_id": 8003}}),
  ],
  outputs=["10003"]
),

Task(
  annotator="saaish2",
  user_id="task_070",
        instruction=(
            "Coordinate the creation of a standalone grocery list for the Martinez Household (household_id=202) under user_id=102, not associated with any meal plan, compiled from exactly these lunch recipes: [409,410,413]. Success entails one new entry in grocery_lists with items compiled from these recipes and status 'initialized', alongside an audit event capturing the list creation. Return the generated list_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":202}),
    Action(name="GetUserById", kwargs={"user_id":102}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":202,"source_meal_plan_id":None,"created_by_user_id":102,"status_enum":"initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[409,410,413]"}),
    Action(name="LogAuditEvent", kwargs={"household_id":202,"user_id":102,"entity_type":"grocery_list","entity_id":8003,"action_enum":"list_created","payload_json":{"source":"recipes","count":3}}),
  ],
  outputs=[
    "8003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_071",
        instruction=(
            "Handle the creation of a 3-night Dinner grocery list for the Peterson Couple (household_id 206) using exactly these recipe IDs: 404, 405, 431. Verify product availability at Value Groceries Direct (store_id 9004), assign pantry-staple flags and grocery sections, and mark the list as 'ready'. Oversee the auditing of list creation and readiness status change. Acceptance: a grocery list with combined items from the specified recipes; availability confirmed at store 9004; pantry flags and sections included; list status as 'ready'; necessary audit events documented. Provide the list_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 206}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 206, "created_by_user_id": 106, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[404,405,431]"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9004}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"from": "initialized", "to": "ready"}}),
  ],
  outputs=["8003"]
),

Task(
  annotator="saaish2",
  user_id="task_072",
        instruction=(
            "Coordinate the production of a single-store Dinner order for the Brown-Brown Family (household_id 204) based on exactly these seven recipes: 423, 424, 425, 426, 427, 428, 429. The output should be one draft order at GreenGrocer Digital (store_id 9001) for 2025-09-05T18:00:00Z–20:00:00Z, ensuring items are sourced only from the store's available stock at the lowest price. Log audits for both creation and item filling. Acceptance: a dedicated list is compiled for those seven recipes; an appropriate draft order is generated for store 9001 during the specified slot; the order comprises only available items selected at the lowest price; audits are recorded; provide the order_id and the final total_cents."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 204}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 204, "created_by_user_id": 104, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[423,424,425,426,427,428,429]"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9001}),
    Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "inventory_checked", "payload_json": {"store_id": 9001}}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 204, "store_id": 9001, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-05T18:00:00Z", "scheduled_slot_end_ts": "2025-09-05T20:00:00Z"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"store_id": 9001}}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9001}),
    Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "order", "entity_id": 10003, "action_enum": "items_added", "payload_json": {"source_list_id": 8003}}),
  ],
  outputs=["10003", "2746"]
),

Task(
  annotator="saaish2",
  user_id="task_073",
        instruction=(
            "Manage the delivery of a five-night Dinner plan for the Martinez Household (household_id 202) spanning 2025-09-08 through 2025-09-12 with exact recipes 401, 402, 404, 405, 431 in that sequence. Facilitate one linked grocery list encompassing aggregated items, accurate grocery sections, and pantry-staple flags, and ensure the list is marked as 'ready' with audits reflecting both the meal plan initiative and the list’s status change. Acceptance criteria: one plan featuring five Dinner entries on the specified dates in the prescribed order; one linked grocery list displaying sections and pantry flags; final list status is 'ready'; audits are logged for meal plan creation and for the list transformation from 'initialized' to 'ready'."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 202}),
    Action(name="GetUserById", kwargs={"user_id": 102}),
    Action(name="CreateMealPlan", kwargs={"household_id": 202, "week_start_date": "2025-09-08", "created_by_user_id": 102}),
    Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-08"}}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[401,402,404,405,431]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 202, "source_meal_plan_id": 6003, "created_by_user_id": 102, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,402,404,405,431]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"from": "initialized", "to": "ready"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_074",
        instruction=(
            "Coordinate the creation of a five-day, peanut-free school-lunch grocery list for the Brown Large Family (household_id 207) based on exactly Lunch recipes 409, 410, 411, 412, 413. The list must consolidate items, display appropriate grocery sections and pantry-staple flags, and show last-30-day overlap as of 2025-09-07. Maintain the list in 'initialized' and document audits for creation, sections populated, and overlap evaluation (include peanut_free: true in the overlap-evaluated audit payload). Acceptance: one list for household 207 utilizing those precise recipes; sections and pantry flags included; overlap flags reflect meals in the 30-day window up to 2025-09-07; status stays 'initialized'; audits are recorded for creation, sections populated, and overlap evaluation indicating peanut_free true."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 207}),
    Action(name="GetUserById", kwargs={"user_id": 107}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 207, "created_by_user_id": 107, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,411,412,413]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="ListRecentMealHistory", kwargs={"household_id": 207, "days_back": 30, "anchor_date": "2025-09-07"}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 207, "anchor_date": "2025-09-07"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "sections_populated", "payload_json": {"sections": True}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "overlap_evaluated", "payload_json": {"anchor_date": "2025-09-07", "peanut_free": True}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_075",
        instruction=(
            "Handle the development of a seven-night Dinner plan for the Rodriguez Household (household_id 208) from 2025-09-15 through 2025-09-21, strictly utilizing recipes 401, 402, 425, 427, 428, 431, 433 in the specified sequence, and include a linked grocery list. Check availability at Value Groceries Direct (store_id 9004), then coordinate a draft delivery order for 2025-09-16T18:00:00Z–20:00:00Z based on that list (populating the order with items is unnecessary at this stage). Ensure audits for the creation of the meal plan, the list, and the order. Acceptance: one plan with seven entries for the designated dates in the set sequence; one linked grocery list; availability confirmed at store 9004; a draft order is present for the given period; audits are in place for the meal plan, list, and order creation."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 208}),
    Action(name="GetUserById", kwargs={"user_id": 108}),
    Action(name="CreateMealPlan", kwargs={"household_id": 208, "week_start_date": "2025-09-15", "created_by_user_id": 108}),
    Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-15"}}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-15", "selected_recipe_ids_json": "[401,402,425,427,428,431,433]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 208, "source_meal_plan_id": 6003, "created_by_user_id": 108, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,402,425,427,428,431,433]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9004}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 208, "store_id": 9004, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-16T18:00:00Z", "scheduled_slot_end_ts": "2025-09-16T20:00:00Z"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"store_id": 9004}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_076",
        instruction=(
            "Coordinate the assembly of a combined Breakfast & Snacks grocery list for the Shah Extended Family (household_id 205) using precisely recipes 441, 444, 445. The list must consolidate items, classify them by grocery section, denote pantry-staple flags, and show a 30-day overlap as of 2025-09-07. Ensure the list is marked as 'ready' and document audits for creation, overlap analysis, and readiness. Acceptance: one list employing exactly those three recipes; clear section categorizations and pantry flags; overlap flags indicating the prior 30 days up to 2025-09-07; final status 'ready'; audits exist for creation, overlap assessment, and readiness."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 205}),
    Action(name="GetUserById", kwargs={"user_id": 105}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 205, "created_by_user_id": 105, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[441,444,445]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="ListRecentMealHistory", kwargs={"household_id": 205, "days_back": 30, "anchor_date": "2025-09-07"}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 205, "anchor_date": "2025-09-07"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "overlap_evaluated", "payload_json": {"anchor_date": "2025-09-07"}}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "ready", "payload_json": {"from": "initialized", "to": "ready"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_077",
        instruction=(
            "Coordinate a weekend brunch set for the Lee-Anderson Family (household_id 209) to align with 2025-09-13 using exactly recipes 432, 435, 408 in that sequence. Develop one linked grocery list with combined items, accurate grocery sections, pantry-staple indications, and last-30-day overlap up to 2025-09-07. Ensure the list stays 'initialized' and audit both creation and overlap assessment. Acceptance criteria: one plan anchored to 2025-09-13 with three entries in the specified order; one linked list featuring sections, pantry indications, and correct overlap indicators; status remains 'initialized'; audits are in place for both creation and overlap assessment."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 209}),
    Action(name="GetUserById", kwargs={"user_id": 109}),
    Action(name="CreateMealPlan", kwargs={"household_id": 209, "week_start_date": "2025-09-13", "created_by_user_id": 109}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-13", "selected_recipe_ids_json": "[432,435,408]"}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 209, "source_meal_plan_id": 6003, "created_by_user_id": 109, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[432,435,408]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="ListRecentMealHistory", kwargs={"household_id": 209, "days_back": 30, "anchor_date": "2025-09-07"}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2025-09-07"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "overlap_evaluated", "payload_json": {"anchor_date": "2025-09-07"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_078",
        instruction=(
            "Develop a single-store, peanut-safe school-lunch draft order for the Brown-Brown Family (household_id 204) using precisely Lunch recipes 409, 410, 411, 412, 413 at GreenGrocer Digital (store_id 9001). Create a specialized grocery list with consolidated items, accurate grocery sections, and pantry-staple indicators. Produce a draft delivery order for 2025-09-05T10:00:00Z–12:00:00Z linked to that list (populating items is not necessary). Conduct audits for both list creation and order creation, and include a peanut-free verification note. Acceptance requirements: one list comprising those five Lunch recipes; presence of sections and pantry indicators; one draft order set for the specified time at store 9001; audits are present for list creation, order creation, and a peanut-free verification note."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 204}),
    Action(name="GetUserById", kwargs={"user_id": 104}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 204, "created_by_user_id": 104, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"status": "initialized"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,411,412,413]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 204, "store_id": 9001, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-05T10:00:00Z", "scheduled_slot_end_ts": "2025-09-05T12:00:00Z"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"store_id": 9001}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "order", "entity_id": 10003, "action_enum": "policy_checked", "payload_json": {"peanut_free": True}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_079",
        instruction=(
            "Handle the task of creating a standalone grocery list for the household “Wang Solo” (household_id=203) with created_by_user_id=103, compiled from exactly these peanut-free lunch recipes: [409, 410, 444]. Success entails generating one new grocery_lists entry for that household with the items matching the aggregate of those recipes (ensuring no duplicate ingredient entries), grocery_section values completed, status set to “finalized,” and a single audit documenting the list creation. Provide the new list_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":203}),
    Action(name="GetUserById", kwargs={"user_id":103}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":203, "created_by_user_id":103}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003, "recipe_ids_json":"[409,410,444]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
    Action(name="SetGroceryListStatus", kwargs={"list_id":8003, "status_enum":"finalized"}),
    Action(name="LogAuditEvent", kwargs={"household_id":203, "user_id":103, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"created"})
  ],
  outputs=[
    "8003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_080",
        instruction=(
            "Coordinate the delivery of a dinner-only grocery outcome for the household “Brown Large Family” (household_id=207) using precisely these recipes: [401, 402, 405, 406], directed by created_by_user_id=107. The outcome must adhere to policy for store 9004 by substituting any unavailable items with authorized in-catalog alternatives, culminating in a finalized list. Success is a single grocery list for that household where items equal the aggregate of those recipes (avoiding duplicate ingredient/unit entries), sections aligned with the catalog, and any initially unavailable items addressed with valid substitutes when necessary, concluding with a finalized list. Do not proceed with order placement."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":207}),
    Action(name="GetUserById", kwargs={"user_id":107}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":207, "created_by_user_id":107}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003, "recipe_ids_json":"[401,402,405,406]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id":8003, "store_id":9004}),
    Action(name="ProposeSubstituteProducts", kwargs={
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
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id":8003, "substitutions":[]}),
    Action(name="SetGroceryListStatus", kwargs={"list_id":8003, "status_enum":"finalized"}),
    Action(name="LogAuditEvent", kwargs={"household_id":207, "user_id":107, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"created"}),
    Action(name="LogAuditEvent", kwargs={"household_id":207, "user_id":107, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"finalized"})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_081",
        instruction=(
            "Handle the creation of a pantry-first restock list for the “Shah Extended Family” (household_id=205) under created_by_user_id=105. Ensure that you keep only the recipes from [441, 444, 446, 447] containing ≤2 non-staple ingredients, aggregating the chosen recipes into one list. A successful task results in exactly one list for that household sourced from the selected recipes, with last-30-days overlap flags computed using anchor_date=2025-08-31, and the list marked as “finalized.” Refrain from evaluating store inventory or placing an order."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":205}),
    Action(name="GetUserById", kwargs={"user_id":105}),
    Action(name="MinimizeNewIngredients", kwargs={"recipe_ids_json":"[441,444,446,447]", "max_new_ingredients_per_recipe":2}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":205, "created_by_user_id":105}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003, "recipe_ids_json":"[447]"}),
    Action(name="LogAuditEvent", kwargs={"household_id":205, "user_id":105, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"created"}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id":8003, "household_id":205, "anchor_date":"2025-08-31"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id":8003, "status_enum":"finalized"}),
    Action(name="LogAuditEvent", kwargs={"household_id":205, "user_id":105, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"finalized"})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_082",
        instruction=(
            "Coordinate the creation of a Dinner grocery list specifically for the Lee-Anderson Family (household_id 209) using recipes [423, 424, 426]. Ensure it is left in 'ready' status, and thoroughly document an audit of the update. For successful acceptance: a single grocery list exists for household 209 with aggregated items from those recipes, the status set to 'ready', and an audit has been logged for the update. Provide the created list_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 209}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 209, "created_by_user_id": 109, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[423,424,426]"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(
      name="LogAuditEvent",
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
            "Handle the creation of a peanut-free school-lunch pack for the “Lee-Anderson Family” (household_id=209) under created_by_user_id=109 with precisely these five lunches: [409, 410, 411, 442, 444]. Success involves generating one new grocery list for that household, incorporating those lunches, with recent-overlap annotations on anchor_date=2025-08-31, sections sorted, and conducting an availability scan at store_id=9006 that provides peanut-free substitution suggestions (but do not implement them)."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":209}),
    Action(name="GetUserById", kwargs={"user_id":109}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":209, "created_by_user_id":109}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003, "recipe_ids_json":"[409,410,411,442,444]"}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id":8003, "household_id":209, "anchor_date":"2025-08-31"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id":8003, "store_id":9006}),
    Action(name="ProposeSubstituteProducts", kwargs={
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
            "Coordinate the assembly of a three-dinner grocery list for the “Peterson Couple” (household_id=206) under created_by_user_id=106 using precisely these recipes: [431, 433, 435]. Success is defined as creating one new list for that household consolidated from those dinners, with pantry staples identified and grocery sections filled, the list being marked “finalized,” and a single audit documenting the finalization."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id":206}),
    Action(name="GetUserById", kwargs={"user_id":106}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id":206, "created_by_user_id":106}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003, "recipe_ids_json":"[431,433,435]"}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id":8003}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
    Action(name="SetGroceryListStatus", kwargs={"list_id":8003, "status_enum":"finalized"}),
    Action(name="LogAuditEvent", kwargs={"household_id":206, "user_id":106, "entity_type":"grocery_list", "entity_id":8003, "action_enum":"finalized"})
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_085",
        instruction=(
            "Handle the creation of a set 3-night Dinner mini-plan for the Peterson Couple (household_id 206) covering the period from 2025-09-12 to 2025-09-14 using precisely these recipe IDs in sequence: 434, 432, 431. Acceptance: a meal plan with three Dinner entries exists on those dates in this order; an audit is available recording the meal plan's creation with week_start_date 2025-09-12."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 206}),
    Action(name="GetUserById", kwargs={"user_id": 106}),
    Action(name="CreateMealPlan", kwargs={"household_id": 206, "week_start_date": "2025-09-12", "created_by_user_id": 106}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-12", "selected_recipe_ids_json": "[434,432,431]"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-12"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_086",
        instruction=(
            "Coordinate the assembly of a specific grocery list for the Peterson Couple (household_id 206) derived exclusively from these two Dinner recipe IDs: 431 and 402. Maintain the list in 'initialized' status. Acceptance: a grocery list is present for household 206 with items strictly aggregated from the given recipes; grocery sections are filled; pantry-staple flags are applied; an audit is available documenting list creation with source 'recipes' and status 'initialized'."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 206}),
    Action(name="GetUserById", kwargs={"user_id": 106}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 206, "created_by_user_id": 106, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[431,402]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="LogAuditEvent", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"source": "recipes", "status": "initialized"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_087",
        instruction=(
            "Handle the preparation of a peanut-free school-lunch pack for the Rodriguez Household (household_id 208) using the specified Lunch recipe IDs: 409 and 413. Start by checking FoodExpress (store_id 9002) for item availability, then suggest peanut-free alternatives if items are unavailable; do not modify the original list with these suggestions. Acceptance criteria: a grocery list in 'initialized' status, purely based on those recipes, must be present; store availability must be confirmed at store_id 9002; a proposal for peanut-free alternatives must be generated; an audit noting the substitution proposal event must exist."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 208}),
    Action(name="GetUserById", kwargs={"user_id": 108}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 208, "created_by_user_id": 108, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,413]"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(
      name="ProposeSubstituteProducts",
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
      name="LogAuditEvent",
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
            "Coordinate the opening of a draft delivery order at FoodExpress (store_id 9002) for the Martinez Household using the existing weekday list (list_id 8002) for the time slot 2025-09-03T16:00:00Z to 2025-09-03T18:00:00Z. Include all available items from that store at the lowest price and ensure an audit of order creation is recorded. Leave the order in draft form. Acceptance criteria: a draft order is created for household_id 202 associated with list_id 8002 and items added; an audit is documented reflecting the creation of the order in 'draft'."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 202}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 202, "store_id": 9002, "list_id": 8002, "scheduled_slot_start_ts": "2025-09-03T16:00:00Z", "scheduled_slot_end_ts": "2025-09-03T18:00:00Z"}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9002}),
    Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "order", "entity_id": 10003, "action_enum": "created", "payload_json": {"status": "draft"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_089",
        instruction=(
            "Handle the creation of a 4-night Dinner plan for the Brown Large Family (household_id 207) from 2025-09-08 to 2025-09-11 using these exact recipes in order: 401, 402, 406, 425. Set each entry's note to exactly include: \"Child-friendly: mild seasoning; cut to bite-size; soft textures.\" Acceptance: a meal plan is available with four Dinner entries on those specific dates in the given sequence; each entry's note contains that precise child-friendly text; an audit is present documenting the meal plan's creation with week_start_date 2025-09-08."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 207}),
    Action(name="CreateMealPlan", kwargs={"household_id": 207, "week_start_date": "2025-09-08", "created_by_user_id": 107}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[401,402,406,425]"}),
    Action(name="UpdateMealPlanEntryNotes", kwargs={"meal_plan_id": 6003, "notes_map": {"401": "Child-friendly: mild seasoning; cut to bite-size; soft textures.", "402": "Child-friendly: mild seasoning; cut to bite-size; soft textures.", "406": "Child-friendly: mild seasoning; cut to bite-size; soft textures.", "425": "Child-friendly: mild seasoning; cut to bite-size; soft textures."}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-08"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_090",
        instruction=(
            "Coordinate the creation of a grocery list for the Martinez Household (household_id 202) using exactly these Dinner recipe IDs: 425 and 427. Keep the list in 'initialized' status (created_by_user_id 102); calculate 30-day overlap flags with 2025-09-07 as the reference point; and organize grocery sections. Acceptance: a grocery list exists with items strictly gathered from those recipes; overlap_last_month flags indicate anchor 2025-09-07; grocery sections are organized; an audit is available reflecting the list update with the specified anchor."
        ),
  actions=[
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 202, "created_by_user_id": 102, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[425,427]"}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 202, "anchor_date": "2025-09-07"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(
      name="LogAuditEvent",
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
            "Handle the delivery of a singular finalized grocery list for the household \"Wang Solo\" (household_id=203). This list should be created by user_id=103 and derived solely from recipes [401, 402]. Success is defined as having exactly one new, finalized list for the household that adheres to policy guidelines as outlined in rules.py hygiene by the anchor_date=2025-08-31. Ensure that no orders are generated."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 203}),
    Action(name="GetUserById", kwargs={"user_id": 103}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 203, "source_meal_plan_id": None, "created_by_user_id": 103, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "grocery_list_created", "created_at": "2025-08-31T00:00:00Z", "payload_json": {"source_recipes": [401, 402], "anchor_date": "2025-08-31"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,402]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 203, "anchor_date": "2025-08-31"}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "finalized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "grocery_list_finalized", "created_at": "2025-08-31T00:00:00Z", "payload_json": {"status": "finalized", "anchor_date": "2025-08-31"}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_092",
        instruction=(
            "Coordinate the compilation of a peanut-free school-lunch grocery list for the \"Brown Large Family\" (household_id=207), created by user_id=107, utilizing precisely the following lunch recipes: [409, 410, 411, 412, 413]. Success means crafting a new list for that household that is compliant with policy and peanut-free at an ingredient level (validated through the recipes' ingredient data), not associated with any meal plan (source_meal_plan_id=None), and starts with the status 'initialized'. Ensure a last-30-day overlap evaluation by anchor_date=2025-09-01, verify availability at store_id=9001, and do not create or update any orders."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 207}),
    Action(name="GetUserById", kwargs={"user_id": 107}),
    Action(name="ListRecipeIngredients", kwargs={"recipe_id": 409}),
    Action(name="ListRecipeIngredients", kwargs={"recipe_id": 410}),
    Action(name="ListRecipeIngredients", kwargs={"recipe_id": 411}),
    Action(name="ListRecipeIngredients", kwargs={"recipe_id": 412}),
    Action(name="ListRecipeIngredients", kwargs={"recipe_id": 413}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 207, "source_meal_plan_id": None, "created_by_user_id": 107, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "grocery_list_created", "created_at": "2025-09-01T00:00:00Z", "payload_json": {"source_recipes": [409, 410, 411, 412, 413], "peanut_free_validated": True, "anchor_date": "2025-09-01"}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,411,412,413]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 207, "anchor_date": "2025-09-01"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9001}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_093",
        instruction=(
            "Handle a budget-store pickup shell order preparation for the “Rodriguez Household” (household_id=208) using a new list designated by user_id=108 from recipes [401, 405]. The task is successful if a policy-compliant list exists for that household; stock is assessed at store_id=9004 with an in-store substitution review if the catalog items are missing; a draft order for 2025-09-02T10:00:00Z–12:00:00Z is established for that store; no order items are included; and audit logs capture the list creation and order creation. The order retains draft status."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 208}),
    Action(name="GetUserById", kwargs={"user_id": 108}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 208, "source_meal_plan_id": None, "created_by_user_id": 108, "status_enum": "initialized"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "grocery_list_created", "payload_json": {"source_recipes": [401, 405]}}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[401,405]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9004}),
    Action(name="ProposeSubstituteProducts", kwargs={"store_id": 9004, "flagged_items": [{"ingredient_id": 1003}, {"ingredient_id": 1006}, {"ingredient_id": 1009}, {"ingredient_id": 1010}, {"ingredient_id": 1011}, {"ingredient_id": 1012}, {"ingredient_id": 1015}, {"ingredient_id": 1016}, {"ingredient_id": 1017}, {"ingredient_id": 1021}], "require_peanut_free": False}),
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id": 8003, "substitutions": []}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 208, "store_id": 9004, "list_id": 8003, "scheduled_slot_start_ts": "2025-09-02T10:00:00Z", "scheduled_slot_end_ts": "2025-09-02T12:00:00Z"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "order", "entity_id": 10003, "action_enum": "order_created", "payload_json": {"store_id": 9004, "list_id": 8003, "slot": ["2025-09-02T10:00:00Z", "2025-09-02T12:00:00Z"]}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_094",
        instruction=(
            "Coordinate the delivery of a seven-night Dinner plan for the household “Brown Large Family” (household_id=207) for the week beginning 2025-09-08 under user_id=107, using precisely these recipes: [401, 402, 403, 404, 405, 406, 407]. Achieving success means exactly one meal_plan exists for that week with seven Dinner entries for those recipes, and each entry’s note matches exactly: “Child-note v1: mild seasoning; cut to bite-size; soft textures.” No grocery list or order is generated."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 207}),
    Action(name="GetUserById", kwargs={"user_id": 107}),
    Action(name="CreateMealPlan", kwargs={"household_id": 207, "week_start_date": "2025-09-08", "created_by_user_id": 107}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "meal_plan_created", "payload_json": {"week_start_date": "2025-09-08"}}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[401,402,403,404,405,406,407]"}),
    Action(name="UpdateMealPlanEntryNotes", kwargs={"meal_plan_id": 6003, "notes_map": {"401": "Child-note v1: mild seasoning; cut to bite-size; soft textures.", "402": "Child-note v1: mild seasoning; cut to bite-size; soft textures.", "403": "Child-note v1: mild seasoning; cut to bite-size; soft textures.", "404": "Child-note v1: mild seasoning; cut to bite-size; soft textures.", "405": "Child-note v1: mild seasoning; cut to bite-size; soft textures.", "406": "Child-note v1: mild seasoning; cut to bite-size; soft textures.", "407": "Child-note v1: mild seasoning; cut to bite-size; soft textures."}}),
    Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "meal_plan_entries_added", "payload_json": {"count": 7}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_095",
        instruction=(
            "Handle a new order for the “Martinez Household” (household_id=202) using the current grocery list list_id=8002 at store_id=9002 for the period 2025-09-03T16:00:00Z–18:00:00Z. To succeed, ensure the order is generated from that list, items are chosen according to policy, the order status is marked as placed, the source list status updates to ordered, and audit logs capture the order creation, item population, status change, and list update."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 202}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8002, "store_id": 9002}),
    Action(name="CreateOrderFromList", kwargs={"household_id": 202, "store_id": 9002, "list_id": 8002, "scheduled_slot_start_ts": "2025-09-03T16:00:00Z", "scheduled_slot_end_ts": "2025-09-03T18:00:00Z"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "order", "entity_id": 10003, "action_enum": "order_created", "payload_json": {"store_id": 9002, "list_id": 8002, "slot": ["2025-09-03T16:00:00Z", "2025-09-03T18:00:00Z"]}}),
    Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9002}),
    Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "order", "entity_id": 10003, "action_enum": "order_items_added", "payload_json": {"source_list_id": 8002}}),
    Action(name="UpdateOrderStatus", kwargs={"order_id": 10003, "new_status": "placed"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "order", "entity_id": 10003, "action_enum": "order_placed", "payload_json": {"status": "placed"}}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8002, "status_enum": "ordered"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list", "entity_id": 8002, "action_enum": "grocery_list_ordered", "payload_json": {"status": "ordered", "linked_order_id": 10003}}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_096",
        instruction=(
            "Coordinate a peanut-free school-lunch list with a substitution review for the “Martinez Household” (household_id=202) initiated by created_by_user_id=102 using precisely these recipes: [409, 413]. Success requires consolidating these recipes into one new list, checking store availability at store_id=9002, executing a substitution pass that adheres to peanut-free guidelines while maintaining items if no in-store substitutes are available; an order is not to be created, and the list should stay in its original state."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 202}),
    Action(name="GetUserById", kwargs={"user_id": 102}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 202, "source_meal_plan_id": None, "created_by_user_id": 102, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,413]"}),
    Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9002}),
    Action(
      name="ProposeSubstituteProducts",
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
    Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id": 8003, "substitutions": []}),
  ],
  outputs=[]
),

Task(
  annotator="saaish2",
  user_id="task_097",
        instruction=(
            "Handle a categorized Dinner grocery list for the Bennett Family (household_id 201) using specifically recipes [403, 405]. Do not generate a meal plan. Keep the list in its default status and log an audit for the creation of the grocery list. Acceptance: one fresh grocery list connected to household 201 with items compiled from those recipes, grocery sections completed, pantry-staple flags marked according to policy, and an audit indicating the list’s initialized state. Return the new grocery_list_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 201}),
    Action(name="GetUserById", kwargs={"user_id": 101}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 201, "created_by_user_id": 101, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[403,405]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
    Action(
      name="LogAuditEvent",
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
            "Coordinate a 7-day Dinner rotation for Wang Solo (household_id 203) for the week commencing 2025-09-08 using recipes [431, 432, 434] in sequence across the week’s seven days. Incorporate the specified child-friendly text \"Child-friendly: mild seasoning; cut to bite-size; soft textures.\" into those entries, and document an audit for the creation of the meal plan. Acceptance: one meal plan for household 203 is established for week_start_date 2025-09-08 with seven Dinner entries adhering to the rotation, and each entry includes the appended child-friendly note. Return the created meal_plan_id."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 203}),
    Action(name="CreateMealPlan", kwargs={"household_id": 203, "week_start_date": "2025-09-08", "created_by_user_id": 103}),
    Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-08", "selected_recipe_ids_json": "[431,432,434,431,432,434,431]"}),
    Action(name="UpdateMealPlanEntryNotes", kwargs={
      "meal_plan_id": 6003,
      "notes_map": {
        "431": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
        "432": "Child-friendly: mild seasoning; cut to bite-size; soft textures.",
        "434": "Child-friendly: mild seasoning; cut to bite-size; soft textures."
      }
    }),
    Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plan", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-08"}}),
  ],
  outputs=[
    "6003"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_099",
        instruction=(
            "Handle the creation of a Breakfast-centered grocery list for Davis Retirement (household_id 210) utilizing exactly recipes [418, 419]. Organize the list categorically, change the list status to \"ready,\" and log an audit indicating the list’s \"ready\" condition. Acceptance: a new grocery list for household 210 with aggregated items, sections filled, status \"ready,\" and an associated audit entry. Provide the final list status string."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 210}),
    Action(name="CreateEmptyGroceryList", kwargs={"household_id": 210, "created_by_user_id": 110, "status_enum": "initialized"}),
    Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[418,419]"}),
    Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
    Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
    Action(name="LogAuditEvent", kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "status_updated"}),
    Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),
  ],
  outputs=[
    "ready"
  ]
),

Task(
  annotator="saaish2",
  user_id="task_100",
        instruction=(
            "Coordinate using the existing grocery list 8001 (household_id 201) to draft a delivery order at GreenGrocer Digital (store_id 9001) scheduled for 2025-09-05T09:00:00Z–2025-09-05T11:00:00Z. Ensure items are populated at the lowest price available in that store and log an audit for the order's creation. Acceptance: a new draft order for list 8001 at store 9001 with items added at the lowest price and a creation audit. Provide the new order_id and the final total_cents."
        ),
  actions=[
    Action(name="GetHouseholdById", kwargs={"household_id": 201}),
    Action(
      name="CreateOrderFromList",
      kwargs={
        "household_id": 201,
        "store_id": 9001,
        "list_id": 8001,
        "scheduled_slot_start_ts": "2025-09-05T09:00:00Z",
        "scheduled_slot_end_ts": "2025-09-05T11:00:00Z",
      },
    ),
    Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9001}),
    Action(
      name="LogAuditEvent",
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
#     "You are planning a compact 3-dinner mini-plan for the Wang Solo household (household_id=203) for the week starting 2025-09-01. "
#     "Acceptance criteria (deterministic terminal state): "
#     "1) Exactly one new meal plan exists for that week and household. "
#     "2) The plan has three Dinner entries using protein-forward, peanut-free recipes [402, 404, 407]. "
#     "3) One grocery list exists for that plan; items are aggregated from those recipes, sections categorized, pantry flags set; list status is left as 'initialized' and readiness is noted via audit. "
#     "4) Log audits for the meal plan creation and the grocery list creation using deterministic payloads. "
#     "Return the new grocery_list_id."
#   ),
#   actions=[
#     Action(name="GetHouseholdById", kwargs={"household_id": 203}),
#     Action(name="CreateMealPlan", kwargs={"household_id": 203, "week_start_date": "2025-09-01", "created_by_user_id": 103}),
#     Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[402,404,407]"}),
#     Action(name="CreateEmptyGroceryList", kwargs={"household_id": 203, "created_by_user_id": 103, "source_meal_plan_id": 6003, "status_enum": "initialized"}),
#     Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,404,407]"}),
#     Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
#     Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
#     Action(
#       name="LogAuditEvent",
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
#       name="LogAuditEvent",
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
#     "You are producing a full 7-dinner, child-friendly plan for the Brown-Brown Family (household_id=204) for the week starting 2025-09-01 and placing a GreenGrocer Digital (store_id=9001) order. "
#     "Acceptance criteria: "
#     "1) One new meal plan exists for that week with Dinner entries using recipes [402, 404, 405, 407, 408, 423, 427]. "
#     "2) Child-friendly notes are applied to all new entries using the deterministic template. "
#     "3) A grocery list is created from those recipes; sections and pantry flags are set; 30-day overlap flags computed with anchor_date=2025-08-31; list status set to 'ready'. "
#     "4) In-store availability is checked at store_id=9001; suggested substitutes are applied where available; an order is created for 2025-09-03T18:00:00Z–20:00:00Z, items added at lowest price, order status set to 'placed', and the list status set to 'ordered'. "
#     "5) Audit the plan creation, list creation, order placement, and list status update. "
#     "Return the list of created meal_plan entry_ids in ascending order."
#   ),
#   actions=[
#     Action(name="GetHouseholdById", kwargs={"household_id": 204}),
#     Action(name="CreateMealPlan", kwargs={"household_id": 204, "week_start_date": "2025-09-01", "created_by_user_id": 104}),
#     Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[402,404,405,407,408,423,427]"}),
#     Action(name="GenerateChildModifications", kwargs={"recipe_ids_json": "[402,404,405,407,408,423,427]"}),
#     Action(
#       name="UpdateMealPlanEntryNotes",
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
#     Action(name="CreateEmptyGroceryList", kwargs={"household_id": 204, "created_by_user_id": 104, "source_meal_plan_id": 6003, "status_enum": "initialized"}),
#     Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[402,404,405,407,408,423,427]"}),
#     Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
#     Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
#     Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 204, "anchor_date": "2025-08-31"}),
#     Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
#     Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9001}),
#     # Flag only ingredients that were out_of_stock in the inventory check at 9001 (deterministic: [1002]).
#     Action(
#       name="ProposeSubstituteProducts",
#       kwargs={
#         "store_id": 9001,
#         "flagged_items": [{"ingredient_id": 1002}],
#         "require_peanut_free": False
#       },
#     ),
#     # No viable substitutions available at this store for the flagged item; apply none.
#     Action(
#       name="UpdateGroceryListWithSubstitutes",
#       kwargs={"list_id": 8003, "substitutions": []},
#     ),
#     Action(
#       name="CreateOrderFromList",
#       kwargs={
#         "household_id": 204,
#         "store_id": 9001,
#         "list_id": 8003,
#         "scheduled_slot_start_ts": "2025-09-03T18:00:00Z",
#         "scheduled_slot_end_ts": "2025-09-03T20:00:00Z",
#       },
#     ),
#     Action(name="AddOrderItemsFromList", kwargs={"order_id": 10003, "store_id": 9001}),
#     Action(name="UpdateOrderStatus", kwargs={"order_id": 10003, "new_status": "placed"}),
#     Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ordered"}),
#     Action(
#       name="LogAuditEvent",
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
#       name="LogAuditEvent",
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
#       name="LogAuditEvent",
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
#       name="LogAuditEvent",
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
#     "You will create a peanut-free 3-day school-lunch plan for the Lee-Anderson Family anchored to the week starting 2025-09-01. Use recipes with ≥20 g protein per serving and, when more than three qualify, pick the top three by protein; break any remaining ties by lower prep_minutes, then lower recipe_id. Build a dedicated grocery list from those three lunches, categorize by store section, flag pantry staples and 30-day overlaps using 2025-08-30 as the anchor, set the list status to 'ready', and record audits for meal plan creation and grocery list creation/finalization. Accept when the lunch plan exists, the list aggregates exactly those lunches, the status is 'ready', and the audits are recorded."
#   ),
#   actions=[
#     Action(name="GetHouseholdById", kwargs={"household_id": 209}),
#     Action(name="GetUserById", kwargs={"user_id": 109}),
#     Action(name="BuildRecipeFilters", kwargs={"meal_type": "Lunch", "min_protein_g": 20, "peanut_free": True, "cuisines_exclude": []}),
#     Action(name="ListRecipesByFilters", kwargs={"filter_token": "F:Lunch:P20:PF1:EX"}),
#     Action(name="CreateMealPlan", kwargs={"household_id": 209, "week_start_date": "2025-09-01", "created_by_user_id": 109}),
#     Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[445, 443, 409]"}),
#     Action(name="CreateEmptyGroceryList", kwargs={"household_id": 209, "source_meal_plan_id": 6003, "created_by_user_id": 109, "status_enum": "initialized"}),
#     Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[445, 443, 409]"}),
#     Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
#     Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
#     Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2025-08-30"}),
#     Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "ready"}),
#     Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "created", "payload_json": {"week_start_date": "2025-09-01"}}),
#     Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"source_meal_plan_id": 6003}}),
#     Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "finalized", "payload_json": {"status": "ready"}})
#   ],
#   outputs=[]
# ),

# Task(
#   annotator="saaish2",
#   user_id="task_000",
#   instruction=(
#     "You manage weekly dinners for the Bennett Family (household_id 201). Create a new meal plan for the week of 2025-09-01 with exactly three peanut-free Dinner entries on 2025-09-01 through 2025-09-03, each providing at least 22g protein and avoiding any dinners this household cooked from 2025-08-01 to 2025-08-20. Use targets 2200 kcal and 120g protein to choose recipes. Success means: one new meal_plan for that week tied to three Dinner entries dated 2025-09-01..2025-09-03, and one new grocery_list linked to the plan with items equal to the aggregated recipe ingredients, categorized by section, and status='finalized', plus one audit row for that list."
#   ),
#   actions=[
#     Action(name="GetHouseholdById", kwargs={"household_id": 201}),
#     Action(name="BuildRecipeFilters", kwargs={"meal_type": "Dinner", "min_protein_g": 22, "peanut_free": True, "cuisines_exclude": []}),
#     # Known deterministic token for this filter
#     Action(name="ListRecipesByFilters", kwargs={"filter_token": "F:Dinner:P22:PF1:EX"}),
#     # Deterministic 20-day window ending 2025-08-20
#     Action(name="ListRecentMealHistory", kwargs={"household_id": 201, "days_back": 20, "anchor_date": "2025-08-20"}),
#     # Exclude ALL recent recipe_ids intersecting the candidate list (404,405,407 were recent)
#     Action(name="ExcludeRecipeIds", kwargs={
#       "candidate_recipe_ids_json": "[402, 404, 405, 407, 423, 425, 427, 428, 429, 434, 435]",
#       "exclude_recipe_ids": [404, 405, 407]
#     }),
#     # Rank strictly over the exclude output; pick 3 by stated targets
#     Action(name="RankRecipesForTargets", kwargs={
#       "recipe_ids_json": "[402, 423, 425, 427, 428, 429, 434, 435]",
#       "needed_count": 3,
#       "target_calories": 2200,
#       "target_protein": 120
#     }),
#     Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2025-09-01", "created_by_user_id": 101}),
#     # Use exactly the three selected in the previous step
#     Action(name="BulkAddMealPlanEntries", kwargs={
#       "meal_plan_id": 6003,
#       "week_start_date": "2025-09-01",
#       "selected_recipe_ids_json": "[425, 423, 435]"
#     }),
#     Action(name="CreateEmptyGroceryList", kwargs={"household_id": 201, "source_meal_plan_id": 6003, "created_by_user_id": 101, "status_enum": "initialized"}),
#     Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[425, 423, 435]"}),
#     Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
#     Action(name="SetGroceryListStatus", kwargs={"list_id": 8003, "status_enum": "finalized"}),
#     Action(name="LogAuditEvent", kwargs={
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
#     "You will plan a full 7-night Dinner week for the Bennett Family for the exact week starting 2025-09-01 using exactly these seven Dinner recipe IDs: 402, 423, 425, 427, 428, 429, 430. Apply the single fixed child-note template to every entry. Keep servings at defaults. Acceptance: the week is populated for all seven days under one new meal plan; each entry has exactly the fixed child-note template (and nothing else); no store or ordering changes."
#   ),
#   actions=[
#     Action(name="GetHouseholdById", kwargs={"household_id": 201}),
#     Action(name="GetUserById", kwargs={"user_id": 101}),
#     Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2025-09-01", "created_by_user_id": 101}),
#     Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2025-09-01", "selected_recipe_ids_json": "[402,423,425,427,428,429,430]"}),
#     # Apply one deterministic, fixed template string to every entry (no extra prose):
#     Action(
#       name="UpdateMealPlanEntryNotes",
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
#       name="LogAuditEvent",
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
#     "You will prepare a peanut-free school-lunch pack for Wang Solo by building a dedicated grocery list from exactly these five peanut-free Lunch recipes: 409, 410, 412, 443, 445. Categorize by section and set both pantry-staple and 30-day overlap flags with 2025-09-07 as the anchor. Keep the list initialized. Acceptance: one new list exists with items aggregated from those five lunches; sections assigned; pantry and overlap flags set; no store checks or orders."
#   ),
#   actions=[
#     Action(name="GetHouseholdById", kwargs={"household_id": 203}),
#     Action(name="GetUserById", kwargs={"user_id": 103}),
#     Action(name="CreateEmptyGroceryList", kwargs={"household_id": 203, "source_meal_plan_id": None, "created_by_user_id": 103, "status_enum": "initialized"}),
#     Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[409,410,412,443,445]"}),
#     Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
#     Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
#     Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 203, "anchor_date": "2025-09-07"})
#   ],
#   outputs=[]
# ),

# Task(
#   annotator="saaish2",
#   user_id="task_000",
#   instruction=(
#     "You will prepare a peanut-free school-lunch pack for the Brown Large Family by creating a dedicated grocery list from exactly these five Lunch recipes: 443, 409, 447, 441, 445. Categorize items and set pantry-staple and 30-day overlap flags using 2025-09-14 as the anchor. Keep the list initialized. Acceptance: one list exists with items aggregated from those five lunches; sections assigned; pantry and overlap flags set; no store checks or orders."
#   ),
#   actions=[
#     Action(name="GetHouseholdById", kwargs={"household_id": 207}),
#     Action(name="GetUserById", kwargs={"user_id": 107}),
#     Action(name="ListHouseholdMembers", kwargs={"household_id": 207}),
#     Action(name="ListInventoryByHousehold", kwargs={"household_id": 207}),
#     Action(name="ListRecentMealHistory", kwargs={"household_id": 207, "days_back": 30, "anchor_date": "2025-09-14"}),
#     Action(name="CreateEmptyGroceryList", kwargs={"household_id": 207, "source_meal_plan_id": None, "created_by_user_id": 107, "status_enum": "initialized"}),
#     Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id": 8003, "recipe_ids_json": "[443,409,447,441,445]"}),
#     Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
#     Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
#     Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 207, "anchor_date": "2025-09-14"}),
#     Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),
#     Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list", "entity_id": 8003, "action_enum": "created", "payload_json": {"source":"peanut_free_lunch","selected_recipes":[443,409,447,441,445]}})
#   ],
#   outputs=[]
# ),

# Task(
#   annotator="saaish2",
#   user_id="task_000",
#   instruction=(
#     "You generate a grocery list for the household “Shah Extended Family” (household_id=205) from recipes 401 and 402, created by user_id=105. Build a new list (status initialized), aggregate items from those two recipes, set grocery sections from ingredient metadata, and flag pantry staples on the list. Log one audit event for list generation. Return the new grocery list_id."
#   ),
#   actions=[
#     Action(name="GetHouseholdById", kwargs={"household_id":205}),
#     Action(name="GetUserById", kwargs={"user_id":105}),
#     Action(name="CreateEmptyGroceryList", kwargs={"household_id":205,"source_meal_plan_id":None,"created_by_user_id":105,"status_enum":"initialized"}),
#     Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[401,402]"}),
#     Action(name="CategorizeGroceryListSections", kwargs={"list_id":8003}),
#     Action(name="FlagPantryStaplesOnList", kwargs={"list_id":8003}),
#     Action(name="LogAuditEvent", kwargs={"household_id":205,"user_id":105,"entity_type":"grocery_lists","entity_id":8003,"action_enum":"generate_list","payload_json":{"recipe_ids":[401,402]}}),
#   ],
#   outputs=[
#     "8003"
#   ]
# ),

# Task(
#   annotator="saaish2",
#   user_id="task_000",
#   instruction=(
#     "You run a pantry-first dinner restock for the household “Lee-Anderson Family” (household_id=209) for the week starting 2025-09-08. Success requires: one meal plan under user_id=109 containing up to two dinners chosen from {401,402,403,404} that each introduce no more than three non-staple ingredients and align best with the adult target (member_id=327); a single grocery list derived exactly from the selected dinners; availability and product choice at store_id=9001 using lowest-price in-stock/low items for the scheduled slot 2025-09-09T09:00:00Z–11:00:00Z; and one audit event recording order placement. Return the created order_id and final total_cents."
#   ),
#   actions=[
#     Action(name="GetHouseholdById", kwargs={"household_id":209}),
#     Action(name="GetUserById", kwargs={"user_id":109}),
#     Action(name="GetMemberTargets", kwargs={"member_id":327}),
#     Action(name="MinimizeNewIngredients", kwargs={"recipe_ids_json":"[401,402,403,404]","max_new_ingredients_per_recipe":3}),
#     Action(name="RankRecipesForTargets", kwargs={"recipe_ids_json":"[401,404]","needed_count":2,"target_calories":2600,"target_protein":120}),
#     Action(name="CreateMealPlan", kwargs={"household_id":209,"week_start_date":"2025-09-08","created_by_user_id":109}),
#     Action(name="LogAuditEvent", kwargs={"household_id":209,"user_id":109,"entity_type":"meal_plans","entity_id":6003,"action_enum":"create_meal_plan","payload_json":{"week_start_date":"2025-09-08"}}),
#     Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id":6003,"week_start_date":"2025-09-08","selected_recipe_ids_json":"[404, 401]"}),
#     Action(name="CreateEmptyGroceryList", kwargs={"household_id":209,"source_meal_plan_id":6003,"created_by_user_id":109,"status_enum":"initialized"}),
#     Action(name="LogAuditEvent", kwargs={"household_id":209,"user_id":109,"entity_type":"grocery_lists","entity_id":8003,"action_enum":"create_grocery_list","payload_json":{"source_meal_plan_id":6003}}),
#     Action(name="UpsertGroceryListItemsFromRecipes", kwargs={"list_id":8003,"recipe_ids_json":"[404,401]"}),
#     Action(name="CheckStoreInventoryForList", kwargs={"list_id":8003,"store_id":9001}),
#     Action(name="ProposeSubstituteProducts", kwargs={"list_id":8003,"store_id":9001}),
#     Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id":8003}),
#     Action(name="CreateOrderFromList", kwargs={"household_id":209,"store_id":9001,"list_id":8003,"scheduled_slot_start_ts":"2025-09-09T09:00:00Z","scheduled_slot_end_ts":"2025-09-09T11:00:00Z"}),
#     Action(name="AddOrderItemsFromList", kwargs={"order_id":10003,"store_id":9001}),
#     Action(name="LogAuditEvent", kwargs={"household_id":209,"user_id":109,"entity_type":"orders","entity_id":10003,"action_enum":"place_order","payload_json":{"list_id":8003,"store_id":9001}}),
#   ],
#   outputs=[
#     "10003",
#     "1597"
#   ]
# ),

]
