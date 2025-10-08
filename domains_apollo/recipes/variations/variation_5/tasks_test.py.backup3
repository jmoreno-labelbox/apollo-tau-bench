from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="recipes_v5_0001",
        instruction="Arrange a FreshMart‑ready Dinner week for household 201 starting on 2026-09-07 with these exact seven dinners in sequence: 401, 404, 406, 423, 424, 433, 434. Compile and sort the grocery list. Provide the list_id.",
        actions=[
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-09-07", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-09-07", "selected_recipe_ids_json": "[401,404,406,423,424,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
        ],
        outputs=["8003"]
    ),
    Task(
      annotator="0",
      user_id="recipes_v5_0002",
      instruction="The user '101' must confirm a packet for a 'Dinner' rotation for household '201': plan dinners '401', '404', '406', '423', '424', '433', '434' for '2026-09-28', produce the packet, document the creation, and supply the 'meal_plan_id' and the packet URI.",
      actions=[
          Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-09-28", "created_by_user_id": 101}),
          Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-09-28", "selected_recipe_ids_json": "[401,404,406,423,424,433,434]"}),
          Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
          Action(name="LogAuditEvent", kwargs={
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
        instruction="Identify repeat-risk ingredients for household 201: align dinners 401, 404, 406, 423, 424, 433, 434 for the date 2026-10-05, compile the list, then detect any overlaps using 2026-10-05 as the reference point and indicate pantry staples. Provide the list_id.",
        actions=[
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-10-05", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-05", "selected_recipe_ids_json": "[401,404,406,423,424,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 201, "anchor_date": "2026-10-05"}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0004",
        instruction=(
            "Design a seven-dinner meal plan for household '201' for the week commencing '2026-10-05', compile the grocery list, and ensure that no-change substitutions are executed (everything remains the same)."
        ),
        actions=[
        Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-10-05"}),
        Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-05"}),
        Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201}),
        Action(name="UpdateGroceryListWithSubstitutes", kwargs={"list_id": 8003, "substitutions": []})
        ],
        outputs=[]
    ),    

  Task(
    annotator="0",
    user_id="recipes_v5_0005",
        instruction=(
            "Handle the retrieval of a grocery 'list_id' for household '201' for the week commencing '2026-10-19'. Ensure it is categorized, flagged as pantry-staple, and appropriately re-categorized to reflect final sections."
        ),
    actions=[
      Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-10-19"}),
      Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-19"}),
      Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201}),
      Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
      Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
      Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003})
    ],
    outputs=["8003"]
  ),
Task(
    annotator="0",
    user_id="recipes_v5_0006",
        instruction=(
            "Coordinate the process to ensure the order for household '201' at store '901' during the time slot '2026-10-13T16:00:00Z'..'2026-10-13T18:00:00Z', generated from the weekly plan starting on '2026-10-12', concludes with the status 'canceled'. Provide the 'order_id'."
        ),
    actions=[
      Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-10-12"}),
      Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-12"}),
      Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201}),
      Action(
        name="CreateOrderFromList",
        kwargs={
          "household_id": 201,
          "store_id": 901,
          "list_id": 8003,
          "scheduled_slot_start_ts": "2026-10-13T16:00:00Z",
          "scheduled_slot_end_ts": "2026-10-13T18:00:00Z"
        }
      ),
      Action(name="UpdateOrderStatus", kwargs={"order_id": 10003, "new_status": "canceled"})
    ],
    outputs=["10003"]
  ),

    Task(
        annotator="0",
        user_id="recipes_v5_0007",
        instruction=(
            "Handle the scheduling of seven dinners for household '201' for the week commencing '2026-07-13' with user 'ryan.bennett@example.com' (user_id '101'), include recipes '[401,403,406,424,427,433,435]', construct the grocery list, organize sections, and return the generated 'list_id'."
        ),
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "ryan.bennett@example.com"}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-07-13", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-07-13", "selected_recipe_ids_json": "[401,403,406,424,427,433,435]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0008",
        instruction=(
            "Coordinate the creation of a seven-dinner schedule for household '201' for '2026-07-20' (user_id '101'), applying the recipes '[402,404,405,423,424,432,434]', subsequently produce the packet URI and provide both the 'meal_plan_id' and the packet."
        ),
        actions=[
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-07-20", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-07-20", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003})
        ],
        outputs=["6003", "packet://meal_plan/6003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0009",
        instruction=(
            "Construct a weekly dinner schedule for household '201' for '2026-07-27' (user 'ryan.bennett@example.com', user_id '101'), include recipes '[401,404,406,423,425,433,434]', then generate the grocery list and identify pantry staples; return 'list_id'."
        ),
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "ryan.bennett@example.com"}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-07-27", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-07-27", "selected_recipe_ids_json": "[401,404,406,423,425,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0010",
        instruction=(
            "Formulate a seven-dinner plan for household '201' for '2026-08-03' (user_id '101'), include recipes '[407,404,427,423,402,425,429]', create the grocery list, and mark last-30-day overlap with the anchor '2026-08-03'; return 'list_id'."
        ),
        actions=[
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-08-03", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-08-03", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 201, "anchor_date": "2026-08-03"})
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0011",
        instruction=(
            "Handle creating a seven-dinner plan for household '201' for '2026-08-17' (user 'ryan.bennett@example.com', user_id '101'), incorporate recipes '[402,404,405,423,424,432,434]', and generate the grocery list. Then, organize sections and provide 'list_id'."
        ),
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "ryan.bennett@example.com"}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-08-17", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-08-17", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0012",
        instruction=(
            "Coordinate a weekly dinner plan for household '201' for '2026-08-31' (user 'ryan.bennett@example.com', user_id '101') including recipes '[407,404,427,423,402,425,429]'. Subsequently, compile the grocery list and conduct an inventory check for store '901'. Return 'list_id'."
        ),
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "ryan.bennett@example.com"}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-08-31", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-08-31", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 901})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0013",
        instruction=(
            "Handle scheduling seven dinners for household '201' on '2026-09-07' (user_id '101') using recipes '[401,403,406,424,427,433,435]', compile the packet, and record plan creation; provide the 'meal_plan_id' and packet."
        ),
        actions=[
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-09-07", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-09-07", "selected_recipe_ids_json": "[401,403,406,424,427,433,435]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2026-09-07", "meal_plan_id": 6003}})
        ],
        outputs=["6003", "packet://meal_plan/6003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0014",
        instruction=(
            "Coordinate a seven-dinner plan for household '201' for '2026-09-14' (user 'ryan.bennett@example.com', user_id '101'), with recipes '[402,404,405,423,424,432,434]', then generate the grocery list and highlight pantry staples; provide 'list_id'."
        ),
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "ryan.bennett@example.com"}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-09-14", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-09-14", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0015",
        instruction=(
            "Handle the creation of a dinner plan for household '201' scheduled for '2026-09-28' (user 'ryan.bennett@example.com', user_id '101') utilizing recipes '[407,404,427,423,402,425,429]'. Assemble the grocery list and conduct an inventory check for store '901'. Return 'list_id'."
        ),
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "ryan.bennett@example.com"}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-09-28", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-09-28", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 901})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0016",
        instruction=(
            "Coordinate the building of a weekly dinner plan for household '201' planned for '2026-10-05' (user_id '101') using recipes '[401,403,406,424,427,433,435]'. Proceed to generate the grocery list and record a 'create' audit for the list. Return 'list_id'."
        ),
        actions=[
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-10-05", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-05", "selected_recipe_ids_json": "[401,403,406,424,427,433,435]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="LogAuditEvent", kwargs={"household_id": 201, "user_id": 101, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"list_id": 8003, "source_meal_plan_id": 6003}})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0017",
        instruction=(
            "Handle the creation of a seven-dinner plan for household '201' for '2026-10-12' (user 'ryan.bennett@example.com', user_id '101') with recipes '[402,404,405,423,424,432,434]'. Construct the grocery list, categorize sections, and return 'list_id'."
        ),
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "ryan.bennett@example.com"}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-10-12", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-12", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0018",
        instruction=(
            "Coordinate the building of a weekly dinner plan for household '201' for '2026-10-19' (user_id '101') utilizing recipes '[401,404,406,423,425,433,434]'. Subsequently, generate the packet and return the 'meal_plan_id' with packet."
        ),
        actions=[
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-10-19", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-19", "selected_recipe_ids_json": "[401,404,406,423,425,433,434]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003})
        ],
        outputs=["6003", "packet://meal_plan/6003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0019",
        instruction=(
            "Handle the creation of a seven-dinner plan for household '201' for '2026-10-26' (user 'ryan.bennett@example.com', user_id '101') using recipes '[407,404,427,423,402,425,429]', then proceed to generate the grocery list and identify pantry staples; provide 'list_id'."
        ),
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "ryan.bennett@example.com"}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-10-26", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-10-26", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0020",
        instruction=(
            "Coordinate the creation of a seven-dinner plan for household '201' for '2026-11-02' (user_id '101') with recipes '[401,403,406,424,427,433,435]', proceed to compile the grocery list, and execute an inventory check for store '901'; provide 'list_id'."
        ),
        actions=[
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-11-02", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-11-02", "selected_recipe_ids_json": "[401,403,406,424,427,433,435]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 901})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0021",
        instruction=(
            "Coordinate the planning of seven dinners for household '201' for '2026-11-09' (user 'ryan.bennett@example.com', user_id '101') by utilizing recipes '[402,404,405,423,424,432,434]', generate the packet, and document the creation of the plan. Return 'meal_plan_id' and packet."
        ),
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "ryan.bennett@example.com"}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-11-09", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-11-09", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2026-11-09", "meal_plan_id": 6003}})
        ],
        outputs=["6003", "packet://meal_plan/6003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0022",
        instruction=(
            "Organize a weekly dinner plan for household '201' for '2026-11-16' (user_id '101') incorporating recipes '[401,404,406,423,425,433,434]', then construct the grocery list and categorize sections; return 'list_id'."
        ),
        actions=[
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-11-16", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-11-16", "selected_recipe_ids_json": "[401,404,406,423,425,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0023",
        instruction=(
            "Coordinate a schedule for seven dinners for household '201' for '2026-11-23' (user 'ryan.bennett@example.com', user_id '101') using recipes '[407,404,427,423,402,425,429]', prepare the grocery list, and mark any last-30-day overlap with anchor '2026-11-23'. Provide 'list_id'."
        ),
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "ryan.bennett@example.com"}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-11-23", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-11-23", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 201, "anchor_date": "2026-11-23"})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0024",
        instruction=(
            "Arrange a seven-dinner plan for household '201' for '2026-11-30' (user_id '101') with recipes '[401,403,406,424,427,433,435]', assemble the packet, and return the 'meal_plan_id' and packet URI."
        ),
        actions=[
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-11-30", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-11-30", "selected_recipe_ids_json": "[401,403,406,424,427,433,435]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003})
        ],
        outputs=["6003", "packet://meal_plan/6003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0025",
        instruction=(
            "Ensure a weekly dinner plan is set for household '201' for '2026-12-07' (user 'ryan.bennett@example.com', user_id '101') using recipes '[402,404,405,423,424,432,434]', prepare the grocery list, and record a 'create' audit for the list; provide the 'list_id'."
        ),
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "ryan.bennett@example.com"}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-12-07", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-12-07", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="LogAuditEvent", kwargs={"household_id": 201, "user_id": 101, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"list_id": 8003, "source_meal_plan_id": 6003}})
        ],
        outputs=["8003"]
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0026",
        instruction=(
            "Organize seven dinners for household '201' for '2026-12-14' (user_id '101') with recipes '[401,404,406,423,425,433,434]', compile the grocery list, and sort sections; supply the 'list_id'."
        ),
        actions=[
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2026-12-14", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2026-12-14", "selected_recipe_ids_json": "[401,404,406,423,425,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003})
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0027",
        instruction="Coordinate the creation of the dinner recipe packet for household '201' associated with user '101' for the week starting '2027-02-22'. Schedule precisely these dinners '401,403,406,424,427,432,434', then provide the 'meal_plan_id' and the packet URI.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 101}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2027-02-22", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-02-22", "selected_recipe_ids_json": "[401,403,406,424,427,432,434]"}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "packet_generated", "payload_json": {"week_start_date": "2027-02-22", "meal_plan_id": 6003, "packet_uri": "packet://meal_plan/6003", "scheduled_recipes": [401,403,406,424,427,432,434]}})
        ],
        outputs=["6003", "packet://meal_plan/6003"]
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0028",
        instruction="Arrange Dinners for '2027-09-20' using recipes '[407,404,427,423,402,425,429]' for the household connected to user '103'. Generate the recipe packet, record a 'create' audit for the meal plan, compile the grocery list, and return the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 103}),
            Action(name="CreateMealPlan", kwargs={"household_id": 203, "week_start_date": "2027-09-20", "created_by_user_id": 103}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-09-20", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2027-09-20", "meal_plan_id": 6003}}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0029",
        instruction="Handle the scheduling of Dinners for '2027-10-11' utilizing recipes '[423,424,425,427,432,433,434]' for the household associated with user '106'. Generate the recipe packet, log an audit with the 'create' action for the meal plan, compile the grocery list, and provide the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 106}),
            Action(name="CreateMealPlan", kwargs={"household_id": 206, "week_start_date": "2027-10-11", "created_by_user_id": 106}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-10-11", "selected_recipe_ids_json": "[423,424,425,427,432,433,434]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2027-10-11", "meal_plan_id": 6003}}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0030",
        instruction="Coordinate a Dinner plan for '2027-10-25' using recipes '[401,404,405,423,424,433,435]' for the household linked to user '108'. Create the grocery list, mark pantry staples, sort sections, verify store '901' availability, and deliver the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 108}),
            Action(name="CreateMealPlan", kwargs={"household_id": 208, "week_start_date": "2027-10-25", "created_by_user_id": 108}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-10-25", "selected_recipe_ids_json": "[401,404,405,423,424,433,435]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 208, "created_by_user_id": 108}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 901}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0031",
        instruction="Handle creating Dinners for '2027-11-01' with recipes '[402,403,404,423,425,432,434]' for the household associated with user '109', produce the recipe packet, record a 'create' audit for the meal plan, compile the grocery list, and provide the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 109}),
            Action(name="CreateMealPlan", kwargs={"household_id": 209, "week_start_date": "2027-11-01", "created_by_user_id": 109}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-11-01", "selected_recipe_ids_json": "[402,403,404,423,425,432,434]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2027-11-01", "meal_plan_id": 6003}}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 209, "created_by_user_id": 109}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0032",
        instruction="Coordinate scheduling Dinners for '2027-11-22' utilizing recipes '[401,402,403,404,405,406,407]' for the household connected to user '102', create the recipe packet, log a 'create' audit for the meal plan, assemble the grocery list, and furnish the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 102}),
            Action(name="CreateMealPlan", kwargs={"household_id": 202, "week_start_date": "2027-11-22", "created_by_user_id": 102}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-11-22", "selected_recipe_ids_json": "[401,402,403,404,405,406,407]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2027-11-22", "meal_plan_id": 6003}}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0033",
        instruction="Handle creating a Dinner plan for '2027-12-27' using recipes '[401,403,406,424,427,433,435]' for the household associated with user '107'. Build the grocery list, flag pantry staples, categorize sections, verify availability at store '901', and return the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 107}),
            Action(name="CreateMealPlan", kwargs={"household_id": 207, "week_start_date": "2027-12-27", "created_by_user_id": 107}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-12-27", "selected_recipe_ids_json": "[401,403,406,424,427,433,435]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 901}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0034",
        instruction="Coordinate scheduling Dinners for '2028-01-03' using recipes '[402,404,405,423,424,432,434]' for the household associated with user '108'. Generate the recipe packet, log a 'create' audit for the meal plan, build the grocery list, and return the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 108}),
            Action(name="CreateMealPlan", kwargs={"household_id": 208, "week_start_date": "2028-01-03", "created_by_user_id": 108}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-03", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-01-03", "meal_plan_id": 6003}}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 208, "created_by_user_id": 108}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0035",
        instruction="Handle the creation of a Dinner plan for '2028-01-17' using recipes '[407,404,427,423,402,425,429]' for the household associated with user '110', assemble the grocery list, mark pantry staples, organize into sections, verify store '901' availability, and provide the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 110}),
            Action(name="CreateMealPlan", kwargs={"household_id": 210, "week_start_date": "2028-01-17", "created_by_user_id": 110}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-17", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 210, "created_by_user_id": 110}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 901}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0036",
        instruction="Coordinate scheduling Dinners for '2028-01-24' using recipes '[401,402,403,404,405,406,407]' for the household linked to user '101', compile the recipe packet, record a 'create' audit for the meal plan, prepare the grocery list, and furnish the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 101}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2028-01-24", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-24", "selected_recipe_ids_json": "[401,402,403,404,405,406,407]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-01-24", "meal_plan_id": 6003}}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0037",
        instruction="Handle creating a Dinner plan for '2028-02-07' with recipes '[401,402,404,423,427,432,434]' for the household associated with user '103', compile the grocery list, identify pantry staples, organize sections, verify store '901' availability, and provide the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 103}),
            Action(name="CreateMealPlan", kwargs={"household_id": 203, "week_start_date": "2028-02-07", "created_by_user_id": 103}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-02-07", "selected_recipe_ids_json": "[401,402,404,423,427,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 901}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0038",
        instruction="Coordinate scheduling of Dinners for '2028-02-14' using recipes '[401,403,404,423,427,433,434]' for the household linked to user '104', prepare the recipe packet, record a 'create' audit for the meal plan, assemble the grocery list, and furnish the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 104}),
            Action(name="CreateMealPlan", kwargs={"household_id": 204, "week_start_date": "2028-02-14", "created_by_user_id": 104}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-02-14", "selected_recipe_ids_json": "[401,403,404,423,427,433,434]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-02-14", "meal_plan_id": 6003}}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0039",
        instruction="Develop a Dinner plan for '2028-02-28' using recipes '[401,404,405,423,424,433,435]' for the household tied to user '106', compile the grocery list, mark pantry staples, organize into sections, verify store '901' availability, and provide the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 106}),
            Action(name="CreateMealPlan", kwargs={"household_id": 206, "week_start_date": "2028-02-28", "created_by_user_id": 106}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-02-28", "selected_recipe_ids_json": "[401,404,405,423,424,433,435]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 901}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0040",
        instruction="Arrange Dinners for '2028-03-06' using recipes '[402,403,404,423,425,432,434]' for the household associated with user '107', create the recipe packet, record a 'create' audit for the meal plan, compile the grocery list, and supply the 'meal_plan_id' and packet URI.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 107}),
            Action(name="CreateMealPlan", kwargs={"household_id": 207, "week_start_date": "2028-03-06", "created_by_user_id": 107}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-03-06", "selected_recipe_ids_json": "[402,403,404,423,425,432,434]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-03-06", "meal_plan_id": 6003}}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0041",
        instruction="Handle scheduling Dinners for '2028-03-27' with recipes '[407,404,427,423,402,425,429]' for the household associated with user '110', generate the recipe packet, record a 'create' audit for the meal plan, compile the grocery list, and provide the 'meal_plan_id' along with the packet URI.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 110}),
            Action(name="CreateMealPlan", kwargs={"household_id": 210, "week_start_date": "2028-03-27", "created_by_user_id": 110}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-03-27", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-03-27", "meal_plan_id": 6003}}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 210, "created_by_user_id": 110}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0042",
        instruction="Coordinate the creation of a Dinner plan for '2028-04-10' using recipes '[423,424,425,427,432,433,434]' for the household tied to user '102', prepare the grocery list, highlight pantry staples, categorize sections, verify store '901' availability, and return the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 102}),
            Action(name="CreateMealPlan", kwargs={"household_id": 202, "week_start_date": "2028-04-10", "created_by_user_id": 102}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-04-10", "selected_recipe_ids_json": "[423,424,425,427,432,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 901}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0043",
        instruction="Arrange Dinners for '2028-04-17' with recipes '[401,402,404,423,427,432,434]' for the household associated with user '103', produce the recipe packet, log a 'create' audit for the meal plan, compile the grocery list, and provide the 'meal_plan_id' along with the packet URI.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 103}),
            Action(name="CreateMealPlan", kwargs={"household_id": 203, "week_start_date": "2028-04-17", "created_by_user_id": 103}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-04-17", "selected_recipe_ids_json": "[401,402,404,423,427,432,434]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-04-17", "meal_plan_id": 6003}}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
        ],
        outputs=["6003", "packet://meal_plan/6003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0044",
        instruction=(
            "Formulate a household-compliant weekly Dinner plan for '2027-12-13' for the main user linked with the email 'ryan.bennett@example.com', ensuring the plan complies with household policy (exclude dinners from the past '28' days and limit to '2' recipes per cuisine). Provide a valid plan using recipes '[429,430,431,432,433,434,435]' consistent with policy, create the grocery list, verify availability at store '9007', and return the 'list_id'."
        ),
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "ryan.bennett@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 101}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 201, "days_back": 28, "anchor_date": "2027-12-13"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[429,430,431,432,433,434,435]", "max_per_cuisine": 2}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2027-12-13", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-12-13", "selected_recipe_ids_json": "[429,430,431,432,433,434,435]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9007}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0045",
        instruction="Handle email 'sofia.martinez@example.com' to devise a weekly Dinner plan for the week commencing '2027-12-20', steering clear of recipes from the previous '28' days and limiting to '2' recipes per cuisine from the candidate set '[401,402,403,404,405,406,407]'; choose precisely '7' dinners, compile the grocery list, ensure availability at store '9001', and return the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "sofia.martinez@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 102}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 202, "days_back": 28, "anchor_date": "2027-12-20"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[401,402,403,404,405,406,407]", "max_per_cuisine": 2}),
            Action(name="RankRecipesForTargets", kwargs={"recipe_ids_json": "[401,402,403,404,405,406,407]", "needed_count": 7}),
            Action(name="CreateMealPlan", kwargs={"household_id": 202, "week_start_date": "2027-12-20", "created_by_user_id": 102}),
            Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2027-12-20"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-12-20", "selected_recipe_ids_json": "[407,404,402,405,401,403,406]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9001}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0046",
        instruction="Coordinate with email 'emily.wang@example.com' to formulate a weekly Dinner plan for the week starting '2027-12-27', steering clear of recipes from the previous '28' days and restricting to a maximum of '2' recipes per cuisine from the candidate set '[408,409,410,411,412,413,414]'; select up to '7' dinners, assemble the grocery list, confirm availability at store '9002', and return the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "emily.wang@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 103}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 203, "days_back": 28, "anchor_date": "2027-12-27"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[408,409,410,411,412,413,414]", "max_per_cuisine": 2}),
            Action(name="CreateMealPlan", kwargs={"household_id": 203, "week_start_date": "2027-12-27", "created_by_user_id": 103}),
            Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2027-12-27"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-12-27", "selected_recipe_ids_json": "[408,409,410,411,412]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),
            Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9002}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0047",
        instruction="Utilize the email 'daniel.Brown@example.com' to develop a weekly Dinner plan for the week commencing '2028-01-03', excluding recipes from the preceding '28' days and limiting to '2' recipes per cuisine from the candidate set '[415,416,417,418,419,420,421]'; choose up to '7' dinners, compile the grocery list, confirm availability at store '9003', and provide the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "daniel.Brown@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 104}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 204, "days_back": 28, "anchor_date": "2028-01-03"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[415,416,417,418,419,420,421]", "max_per_cuisine": 2}),
            Action(name="CreateMealPlan", kwargs={"household_id": 204, "week_start_date": "2028-01-03", "created_by_user_id": 104}),
            Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-01-03"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-03", "selected_recipe_ids_json": "[415,416,417,420,421]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9003}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0048",
        instruction="Employ the email 'anjali.shah@example.com' to organize a weekly Dinner plan for the week starting '2028-01-10', bypassing recipes from the last '28' days and restricting to '2' recipes per cuisine from the candidate set '[422,423,424,425,426,427,428]'; pick up to '7' dinners, prepare the grocery list, verify availability at store '9004', and submit the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "anjali.shah@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 105}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 205, "days_back": 28, "anchor_date": "2028-01-10"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[422,423,424,425,426,427,428]", "max_per_cuisine": 2}),
            Action(name="CreateMealPlan", kwargs={"household_id": 205, "week_start_date": "2028-01-10", "created_by_user_id": 105}),
            Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-01-10"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-10", "selected_recipe_ids_json": "[422,423,424,425,426,427]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 205, "created_by_user_id": 105}),
            Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9004}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0049",
        instruction="Handle the creation of a weekly Dinner plan using email 'michael.peterson@example.com' for the week commencing on '2028-01-17'. Exclude any recipes from the last '28' days and ensure no more than '2' recipes per cuisine from the list '[401,402,403,404,405,406,407]'. Choose exactly '7' dinners, compile the grocery list, confirm availability at store '9005', and provide the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "michael.peterson@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 106}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 206, "days_back": 28, "anchor_date": "2028-01-17"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[401,402,403,404,405,406,407]", "max_per_cuisine": 2}),
            Action(name="RankRecipesForTargets", kwargs={"recipe_ids_json": "[401,402,403,404,405,406,407]", "needed_count": 7}),
            Action(name="CreateMealPlan", kwargs={"household_id": 206, "week_start_date": "2028-01-17", "created_by_user_id": 106}),
            Action(name="LogAuditEvent", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-01-17"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-17", "selected_recipe_ids_json": "[407,404,402,405,401,403,406]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="LogAuditEvent", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9005}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0050",
        instruction="Coordinate the creation of a weekly Dinner plan with the email 'olivia.brown@example.com' for the week starting '2028-01-24'. Avoid recipes from the past '28' days and limit to '2' recipes per cuisine within the candidate set '[408,409,410,411,412,413,414]'. Select up to '7' dinners, assemble the grocery list, check availability at store '9006', and supply the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "olivia.brown@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 107}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 207, "days_back": 28, "anchor_date": "2028-01-24"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[408,409,410,411,412,413,414]", "max_per_cuisine": 2}),
            Action(name="CreateMealPlan", kwargs={"household_id": 207, "week_start_date": "2028-01-24", "created_by_user_id": 107}),
            Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-01-24"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-24", "selected_recipe_ids_json": "[408,409,410,411,412]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9006}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0051",
        instruction="Utilize the email 'diego.rodriguez@example.com' to formulate a weekly Dinner plan commencing on '2028-01-31'. Eliminate any recipes used within the previous '28' days and limit selections to '2' recipes per cuisine from the candidate set '[415,416,417,418,419,420,421]'. Choose a maximum of '7' dinners, compile the grocery list, confirm stock at store '9007', and provide the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "diego.rodriguez@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 108}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 208, "days_back": 28, "anchor_date": "2028-01-31"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[415,416,417,418,419,420,421]", "max_per_cuisine": 2}),
            Action(name="CreateMealPlan", kwargs={"household_id": 208, "week_start_date": "2028-01-31", "created_by_user_id": 108}),
            Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-01-31"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-01-31", "selected_recipe_ids_json": "[415,416,417,420,421]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 208, "created_by_user_id": 108}),
            Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9007}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0052",
        instruction="Utilize the email 'grace.lee@example.com' to formulate a weekly Dinner plan commencing on '2028-02-07'. Eliminate any recipes used within the previous '28' days and limit selections to '2' recipes per cuisine from the candidate set '[422,423,424,425,426,427,428]'. Choose a maximum of '7' dinners, compile the grocery list, confirm stock at store '9008', and provide the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "grace.lee@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 109}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 209, "days_back": 28, "anchor_date": "2028-02-07"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[422,423,424,425,426,427,428]", "max_per_cuisine": 2}),
            Action(name="CreateMealPlan", kwargs={"household_id": 209, "week_start_date": "2028-02-07", "created_by_user_id": 109}),
            Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-02-07"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-02-07", "selected_recipe_ids_json": "[422,423,424,425,426,427]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 209, "created_by_user_id": 109}),
            Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9008}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0053",
        instruction="Handle creating a weekly Dinner plan for the week starting '2028-02-14' using email 'william.davis@example.com', ensuring to exclude recipes from the last '28' days and limiting to '2' recipes per cuisine from the candidate set '[401,403,406,424,427,433,435]'; choose exactly '7' dinners, assemble the grocery list, check availability at store '9009', and provide the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "william.davis@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 110}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 210, "days_back": 28, "anchor_date": "2028-02-14"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[401,403,406,424,427,433,435]", "max_per_cuisine": 2}),
            Action(name="RankRecipesForTargets", kwargs={"recipe_ids_json": "[401,403,406,424,427,433,435]", "needed_count": 7}),
            Action(name="CreateMealPlan", kwargs={"household_id": 210, "week_start_date": "2028-02-14", "created_by_user_id": 110}),
            Action(name="LogAuditEvent", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-02-14"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-02-14", "selected_recipe_ids_json": "[427,435,401,403,406,433,424]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 210, "created_by_user_id": 110}),
            Action(name="LogAuditEvent", kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9009}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0054",
        instruction="Coordinate creating a weekly Dinner plan for the week starting '2028-02-21' using email 'ryan.bennett@example.com', ensuring to exclude recipes from the last '28' days and limiting to '2' recipes per cuisine from the candidate set '[408,409,410,411,412,413,414]'; pick up to '7' dinners, prepare the grocery list, verify availability at store '9010', and provide the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "ryan.bennett@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 101}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 201, "days_back": 28, "anchor_date": "2028-02-21"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[408,409,410,411,412,413,414]", "max_per_cuisine": 2}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2028-02-21", "created_by_user_id": 101}),
            Action(name="LogAuditEvent", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-02-21"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-02-21", "selected_recipe_ids_json": "[408,409,410,411,412]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="LogAuditEvent", kwargs={"household_id": 201, "user_id": 101, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9010}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0055",
        instruction="Handle the creation of a weekly Dinner plan using the email 'sofia.martinez@example.com' for the week commencing '2028-02-28'. Ensure no recipes from the past '28' days are included and limit to '2' recipes per cuisine from the candidate set '[415,416,417,418,419,420,421]'. Choose up to '7' dinners, assemble the grocery list, check availability at store '9011', and provide the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "sofia.martinez@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 102}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 202, "days_back": 28, "anchor_date": "2028-02-28"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[415,416,417,418,419,420,421]", "max_per_cuisine": 2}),
            Action(name="CreateMealPlan", kwargs={"household_id": 202, "week_start_date": "2028-02-28", "created_by_user_id": 102}),
            Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-02-28"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-02-28", "selected_recipe_ids_json": "[415,416,417,420,421]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9011}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0056",
        instruction="Coordinate the creation of a weekly Dinner plan utilizing the email 'emily.wang@example.com' for the week starting '2028-03-06'. Exclude recipes from the previous '28' days and restrict to '2' recipes per cuisine from the candidate set '[422,423,424,425,426,427,428]'. Opt for up to '7' dinners, compile the grocery list, verify availability at store '9012', and return the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "emily.wang@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 103}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 203, "days_back": 28, "anchor_date": "2028-03-06"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[422,423,424,425,426,427,428]", "max_per_cuisine": 2}),
            Action(name="CreateMealPlan", kwargs={"household_id": 203, "week_start_date": "2028-03-06", "created_by_user_id": 103}),
            Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-03-06"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-03-06", "selected_recipe_ids_json": "[422,423,424,425,426,427]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),
            Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9012}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0057",
        instruction="Utilize the email 'daniel.Brown@example.com' to formulate a weekly Dinner plan for the week commencing '2028-03-13', ensuring not to include recipes from the previous '28' days and maintaining no more than '2' recipes per cuisine from the provided candidate set '[429,430,431,432,433,434,435]'; choose precisely '7' dinners, compile the grocery list, confirm availability at store '9013', and retrieve the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "daniel.Brown@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 104}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 204, "days_back": 28, "anchor_date": "2028-03-13"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[429,430,431,432,433,434,435]", "max_per_cuisine": 2}),
            Action(name="RankRecipesForTargets", kwargs={"recipe_ids_json": "[429,430,431,432,433,434,435]", "needed_count": 7}),
            Action(name="CreateMealPlan", kwargs={"household_id": 204, "week_start_date": "2028-03-13", "created_by_user_id": 104}),
            Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-03-13"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-03-13", "selected_recipe_ids_json": "[429,430,435,434,433,431,432]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9013}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0058",
        instruction="Leverage the email 'anjali.shah@example.com' to devise a weekly Dinner plan for the week beginning '2028-03-20', avoiding recipes used in the past '28' days and keeping a maximum of '2' recipes per cuisine from the candidate list '[401,402,403,404,405,406,407]'; select exactly '7' dinners, generate the grocery list, check availability at store '9014', and provide the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "anjali.shah@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 105}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 205, "days_back": 28, "anchor_date": "2028-03-20"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[401,402,403,404,405,406,407]", "max_per_cuisine": 2}),
            Action(name="RankRecipesForTargets", kwargs={"recipe_ids_json": "[401,402,403,404,405,406,407]", "needed_count": 7}),
            Action(name="CreateMealPlan", kwargs={"household_id": 205, "week_start_date": "2028-03-20", "created_by_user_id": 105}),
            Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-03-20"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-03-20", "selected_recipe_ids_json": "[407,404,402,405,401,403,406]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 205, "created_by_user_id": 105}),
            Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9014}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0059",
        instruction="Handle the creation of a weekly Dinner plan using the email 'michael.peterson@example.com' for the week commencing '2028-03-27'. Ensure to avoid recipes used in the last '28' days and limit to '2' recipes per cuisine from the options '[408,409,410,411,412,413,414]'. Select a maximum of '7' dinners, compile the grocery list, confirm its availability at the store '9015', and provide the 'list_id'.",
        actions=[
            Action(name="GetUserByEmail", kwargs={"email": "michael.peterson@example.com"}),
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 106}),
            Action(name="ListRecentMealHistory", kwargs={"household_id": 206, "days_back": 28, "anchor_date": "2028-03-27"}),
            Action(name="ApplyCuisineLimit", kwargs={"recipe_ids_json": "[408,409,410,411,412,413,414]", "max_per_cuisine": 2}),
            Action(name="CreateMealPlan", kwargs={"household_id": 206, "week_start_date": "2028-03-27", "created_by_user_id": 106}),
            Action(name="LogAuditEvent", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2028-03-27"}}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-03-27", "selected_recipe_ids_json": "[408,409,410,411,412]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="LogAuditEvent", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9015}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0060",
        instruction="Coordinate a Dinner week scheduling for the household associated with user '101' beginning on '2028-04-03', following these seven specific dinners in order: '401','404','406','423','424','433','434'. Organize and group the grocery list, verify stock at store '9001', and supply the 'list_id'. For internal checks, also enumerate the household members and retrieve a snapshot of the meal-plan details to confirm ownership and 'week_start_date', though these validations need not be included in the outputs.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 101}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2028-04-03", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-04-03", "selected_recipe_ids_json": "[401,404,406,423,424,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 201}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9001}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0061",
        instruction="Generate a Dinner plan for the household associated with user '102' for the week commencing '2028-04-10' using precisely these seven dinners in sequence: '402','404','405','423','424','432','434'. Prepare the grocery list, identify pantry staples, inspect store '9002', and provide the 'list_id'. Additionally, ensure internal consistency by enumerating household members and obtaining a meal-plan details snapshot to confirm correct ownership and dates (omit these from outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 102}),
            Action(name="CreateMealPlan", kwargs={"household_id": 202, "week_start_date": "2028-04-10", "created_by_user_id": 102}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-04-10", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 202}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9002}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0062",
        instruction="Arrange a Dinner week for the household linked to user '103' beginning '2028-04-17' with these specific dinners in order: '407','404','427','423','402','425','429'. Assemble the grocery list, highlight any last-30-day overlap using anchor '2028-04-17', and supply the 'list_id'. Moreover, create a concise internal validation trail by listing household members and gathering a meal-plan details snapshot to verify correct linkage (these should not be included in outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 103}),
            Action(name="CreateMealPlan", kwargs={"household_id": 203, "week_start_date": "2028-04-17", "created_by_user_id": 103}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-04-17", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),
            Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 203, "anchor_date": "2028-04-17"}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 203}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0063",
        instruction="Handle the construction of a Dinner plan for the household associated with user '104' for the week commencing '2028-04-24' using precisely '423','424','425','427','432','433','434'. Develop the grocery list, mark pantry staples, verify availability at store '9003', and provide the 'list_id'. Conduct an internal verification step by listing household members and acquiring a meal-plan details snapshot to confirm ownership and configuration (verification details are not necessary in outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 104}),
            Action(name="CreateMealPlan", kwargs={"household_id": 204, "week_start_date": "2028-04-24", "created_by_user_id": 104}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-04-24", "selected_recipe_ids_json": "[423,424,425,427,432,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 204}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9003}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0064",
        instruction="Coordinate the creation of a Dinner week for the household tied to user '105' starting from '2028-05-01' with the exact items: '401','403','404','423','427','433','434'. Construct and organize the grocery list, and supply the 'list_id'. For internal quality assurance, enumerate the household members, retrieve the meal-plan details, obtain the grocery-list details to verify ownership and sections, and capture a brief household inventory snapshot for reconciliation (these validations are not required in outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 105}),
            Action(name="CreateMealPlan", kwargs={"household_id": 205, "week_start_date": "2028-05-01", "created_by_user_id": 105}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-05-01", "selected_recipe_ids_json": "[401,403,404,423,427,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 205, "created_by_user_id": 105}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 205}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
            Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),
            Action(name="ListInventoryByHousehold", kwargs={"household_id": 205}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0065",
        instruction="Handle scheduling a Dinner week for the household associated with user '106' beginning on '2028-05-08', specifically utilizing '402','404','405','423','424','432','434'. Construct the grocery list, confirm store '9005', and return the 'list_id'. For internal verification, retrieve the grocery-list details, meal-plan specifics, and a brief snapshot of the household inventory for reconciliation purposes (ensure these verifications are not included in the outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 106}),
            Action(name="CreateMealPlan", kwargs={"household_id": 206, "week_start_date": "2028-05-08", "created_by_user_id": 106}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-05-08", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9005}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
            Action(name="ListInventoryByHousehold", kwargs={"household_id": 206}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0066",
        instruction="Coordinate Dinners planning for the household linked to user '107' for the week starting '2028-05-15' using specifically the items '401','404','406','423','425','433','435'. Create the grocery list, organize sections, mark pantry staples, and return the 'list_id'. As part of internal quality assurance, acquire the grocery-list details, meal-plan specifics, and a short household inventory snapshot to confirm list composition (additional information is not required in the outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 107}),
            Action(name="CreateMealPlan", kwargs={"household_id": 207, "week_start_date": "2028-05-15", "created_by_user_id": 107}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-05-15", "selected_recipe_ids_json": "[401,404,406,423,425,433,435]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
            Action(name="ListInventoryByHousehold", kwargs={"household_id": 207}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0067",
        instruction="Organize a Dinner plan for the household associated with user '108' for the week commencing '2028-05-22' using precisely '407','404','427','423','402','425','429'. Construct the grocery list, confirm its availability at store '9007', and provide the 'list_id'. Additionally, perform an internal audit by retrieving the grocery-list details and meal-plan specifics and capturing a succinct household inventory snapshot (there is no need to return extra data).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 108}),
            Action(name="CreateMealPlan", kwargs={"household_id": 208, "week_start_date": "2028-05-22", "created_by_user_id": 108}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-05-22", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 208, "created_by_user_id": 108}),
            Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9007}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
            Action(name="ListInventoryByHousehold", kwargs={"household_id": 208}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0068",
        instruction="Arrange Dinners for the household related to user '109' for the week beginning '2028-05-29', utilizing exactly '402','403','404','423','425','432','434'. Assemble the grocery list, identify any overlap from the last 30 days using the anchor '2028-05-29', and submit the 'list_id'. Also, execute an internal validation by acquiring grocery-list specifics, meal-plan particulars, and a brief household inventory snapshot for reconciliation (these checks are not required in the output).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 109}),
            Action(name="CreateMealPlan", kwargs={"household_id": 209, "week_start_date": "2028-05-29", "created_by_user_id": 109}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-05-29", "selected_recipe_ids_json": "[402,403,404,423,425,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 209, "created_by_user_id": 109}),
            Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),
            Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 209, "anchor_date": "2028-05-29"}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
            Action(name="ListInventoryByHousehold", kwargs={"household_id": 209}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0069",
        instruction="Handle the creation of a Dinner plan for the household associated with user '110' for the week commencing on '2028-06-05', ensuring to include '401','403','406','424','427','432','434'. Develop the grocery list, verify stock at store '9009', and provide the 'list_id'. For internal QA purposes, retrieve grocery-list specifics and meal-plan data while taking a brief household inventory snapshot (excluding the QA data from outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 110}),
            Action(name="CreateMealPlan", kwargs={"household_id": 210, "week_start_date": "2028-06-05", "created_by_user_id": 110}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-06-05", "selected_recipe_ids_json": "[401,403,406,424,427,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 210, "created_by_user_id": 110}),
            Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9009}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
            Action(name="ListInventoryByHousehold", kwargs={"household_id": 210}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0070",
        instruction="Coordinate a Dinner week for the household connected to user '102' beginning '2028-06-12' incorporating '402','404','405','423','424','432','434' in that order. Assemble the grocery list, organize sections, check stock at store '9002', and supply the 'list_id'. For internal QA, enumerate the household members and obtain a meal-plan details snapshot (omitting the QA from outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 102}),
            Action(name="CreateMealPlan", kwargs={"household_id": 202, "week_start_date": "2028-06-12", "created_by_user_id": 102}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-06-12", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9002}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 202}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0071",
        instruction="Handle the creation of a Dinner week for the household associated with user '103' beginning '2028-06-19' utilizing exactly '407','404','427','423','402','425','429'. Formulate the grocery list, organize the sections, identify pantry staples, verify availability at store '9003', and provide the 'list_id'. For internal QA, also procure the meal-plan details and grocery-list details to verify ownership and sections (QA does not need to be part of outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 103}),                                                          
            Action(name="CreateMealPlan", kwargs={"household_id": 203, "week_start_date": "2028-06-19", "created_by_user_id": 103}), 
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-06-19", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),  
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),                                         
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),                                                 
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),                                                     
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9003}),                                
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),                                                       
            Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),                                                        
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0072",
        instruction=(
            "Coordinate a Dinner week schedule for the household linked to user '104' that starts on '2028-06-26', using exactly '423','424','425','427','432','433','434'. Construct the grocery list, flag any last-30-day overlaps referencing anchor '2028-06-26', confirm availability at store '9004', and return the 'list_id'. For internal QA, also record a snapshot of meal-plan details and list the household members (avoid including QA in outputs)."
        ),
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 104}),
            Action(name="CreateMealPlan", kwargs={"household_id": 204, "week_start_date": "2028-06-26", "created_by_user_id": 104}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-06-26", "selected_recipe_ids_json": "[423,424,425,427,432,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 204, "anchor_date": "2028-06-26"}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9004}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 204}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0073",
        instruction=(
            "Coordinate a Dinner week for the household associated with user '106' commencing on '2028-07-10' by utilizing codes '402','404','405','423','424','432','434'. Compile the grocery list, confirm stock availability at store '9006', and provide the 'list_id'. For internal QA purposes, list household members and obtain details of both the meal plan and grocery list to verify ownership and sections (QA data is not necessary in outputs)."
        ),
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 106}),
            Action(name="CreateMealPlan", kwargs={"household_id": 206, "week_start_date": "2028-07-10", "created_by_user_id": 106}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-07-10", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9006}),
            Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 206}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0074",
        instruction="Arrange a Dinner week for the household associated with user '107' beginning '2028-07-17' using precisely '401','404','406','423','425','433','435'. Organize and categorize the grocery list, initiate an order at store '9007' for the time slot '2028-07-18T10:00:00Z'..'2028-07-18T12:00:00Z', update the order status to 'on_hold', and return the 'order_id'. For internal QA, capture a snapshot of meal plan details (QA data is not required in outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 107}),
            Action(name="CreateMealPlan", kwargs={"household_id": 207, "week_start_date": "2028-07-17"}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "selected_recipe_ids_json": "[401,404,406,423,425,433,435]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="CreateOrderFromList", kwargs={"household_id": 207, "store_id": 9007, "list_id": 8003, "scheduled_slot_start_ts": "2028-07-18T10:00:00Z", "scheduled_slot_end_ts": "2028-07-18T12:00:00Z"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": 10003, "new_status": "on_hold"}),
        ],
        outputs=["10003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0075",
        instruction="Organize Dinners for the household associated with user '110' for the week commencing on '2028-08-07' utilizing precisely '401','403','406','424','427','432','434'. Compile the recipe packet, create and classify the grocery list, verify availability at store '9010', record a 'packet_generated' audit event for the meal plan, and provide the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 110}),
            Action(name="CreateMealPlan", kwargs={"household_id": 210, "week_start_date": "2028-08-07"}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "selected_recipe_ids_json": "[401,403,406,424,427,432,434]"}),
            Action(name="GenerateRecipePacket", kwargs={"meal_plan_id": 6003}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9010}),
            Action(name="LogAuditEvent", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "packet_generated"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0076",
        instruction="Design a Dinner week for the household connected to user '104' beginning '2028-09-04' using specifically '423','424','425','427','432','433','434'. Prepare and organize the grocery list, confirm stock at store '9004', and return the 'list_id'. Add an internal QA snapshot by listing household members and retrieving meal-plan details (not required in outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 104}),
            Action(name="CreateMealPlan", kwargs={"household_id": 204, "week_start_date": "2028-09-04", "created_by_user_id": 104}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-09-04", "selected_recipe_ids_json": "[423,424,425,427,432,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9004}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 204}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0077",
        instruction="Initiate a Dinner week for the household associated with user '105' commencing from '2028-09-11' using precisely '401','403','404','423','427','433','434'. Organize and categorize the grocery list, identify pantry staples, verify store '9005', record a 'create' audit event for the grocery list, and provide the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 105}),                                                                                                    
            Action(name="CreateMealPlan", kwargs={"household_id": 205, "week_start_date": "2028-09-11", "created_by_user_id": 105}),                                           
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "selected_recipe_ids_json": "[401,403,404,423,427,433,434]"}),                               
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003}),                                                                                    
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),                                                                                           
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),                                                                                                
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9005}),                                                                           
            Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create"}),            
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="gen_v5",
        user_id="recipes_v5_0078",
        instruction="Arrange a Dinner week for household '209' beginning '2027-07-18' utilizing exactly '402','403','404','423','425','432','434'; compile the grocery list, confirm store '9010', document a 'create' audit for the list, and give back the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 109}),
            Action(name="CreateMealPlan", kwargs={"household_id": 209, "week_start_date": "2027-07-18", "created_by_user_id": 109}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-07-18", "selected_recipe_ids_json": "[402,403,404,423,425,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 209, "created_by_user_id": 109}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9010}),
            Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0079",
        instruction="Handle the creation of a Dinner week for the household associated with user '107' beginning '2028-09-25' utilizing precisely '401','404','406','423','425','433','435'. Organize and categorize the grocery list, confirm stock at store '9007', and provide the 'list_id'. Incorporate an internal meal-plan snapshot for QA (not necessary in outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 107}),
            Action(name="CreateMealPlan", kwargs={"household_id": 207, "week_start_date": "2028-09-25", "created_by_user_id": 107}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-09-25", "selected_recipe_ids_json": "[401,404,406,423,425,433,435]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9007}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
            Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0080",
        instruction=(
            "Coordinate the development of a Dinner week for the household linked to user '108' starting '2028-10-02' using exactly '407','404','427','423','402','425','429'. Create and organize the grocery list, indicate any overlaps in the last 30 days using the anchor '2028-10-02', check availability at store '9008', and return the 'list_id'."
        ),
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 108}),
            Action(name="CreateMealPlan", kwargs={"household_id": 208, "week_start_date": "2028-10-02", "created_by_user_id": 108}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-10-02", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 208, "created_by_user_id": 108}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 208, "anchor_date": "2028-10-02"}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9008}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0081",
        instruction="Construct a Dinner week for the household associated with user '110' commencing on '2028-10-16' using exactly '401','403','406','424','427','432','434'. Develop the grocery list, examine store '9011', categorize sections, flag pantry staples, and provide the 'list_id'. For internal QA, identify household members and obtain a meal-plan and grocery-list snapshot (no need to include QA in outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 110}),                                                                                                     
            Action(name="CreateMealPlan", kwargs={"household_id": 210, "week_start_date": "2028-10-16", "created_by_user_id": 110}),                                           
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "selected_recipe_ids_json": "[401,403,406,424,427,432,434]"}),                              
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 210, "created_by_user_id": 110}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9011}),                                                                       
            Action(name="ListHouseholdMembers", kwargs={"household_id": 210}),                                                                                               
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),                                                                                                
            Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),                                                                                                   
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),                                                                                           
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),                                                                                                
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0082",
        instruction="Arrange Dinners for the household tied to user '101' for the week beginning on '2028-10-23' utilizing exactly '407','404','427','423','402','425','429'. Create and categorize the grocery list, flag pantry staples, review store '9012', and supply the 'list_id'. For internal QA, identify household members and gather meal-plan and grocery-list specifics (no need to include QA in outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 101}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2028-10-23"}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9012}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 201}),
            Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0083",
        instruction="Handle the creation of a Dinner week for the household associated with user '102' beginning on '2028-10-30' utilizing precisely '402','404','405','423','424','432','434'. Develop the grocery list, mark any last-30-day overlap with the anchor date '2028-10-30', confirm availability at store '9013', and provide the 'list_id'. Capture an internal snapshot of meal-plan details for QA purposes (exclude QA from outputs).",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 102}),
            Action(name="CreateMealPlan", kwargs={"household_id": 202, "week_start_date": "2028-10-30", "created_by_user_id": 102}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2028-10-30", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="FlagOverlapLastMonthOnList", kwargs={"list_id": 8003, "household_id": 202, "anchor_date": "2028-10-30"}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9013}),
            Action(name="GetMealPlanDetails", kwargs={"meal_plan_id": 6003}),
            Action(name="GetGroceryListDetails", kwargs={"list_id": 8003}),
        ],
        outputs=["8003"],
    ),

    Task(
        annotator="0",
        user_id="recipes_v5_0084",
        instruction=(
            "Coordinate the scheduling of Dinners for the household connected to user '109' for the week commencing '2028-10-09' employing precisely '402','403','404','423','425','432','434'. Construct and categorize the grocery list, identify pantry staples, verify at store '9009', document a 'create' audit event for the grocery list, and deliver the 'list_id'."
        ),
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 109}),
            Action(name="CreateMealPlan", kwargs={"household_id": 209, "week_start_date": "2028-10-09", "created_by_user_id": 109}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "selected_recipe_ids_json": "[402,403,404,423,425,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003}),
            Action(name="CategorizeGroceryListSections", kwargs={"list_id": 8003}),
            Action(name="FlagPantryStaplesOnList", kwargs={"list_id": 8003}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9009}),
            Action(name="LogAuditEvent", kwargs={"household_id": 209, "user_id": 109, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0085",
        instruction="Arrange a Dinner week for household '201' beginning on '2027-01-03' utilizing exactly '401','404','406','423','424','433','434' in the specified sequence; compile the grocery list, confirm availability at store '9001', record a 'create' audit for the list, and provide the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 101}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2027-01-03", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-01-03", "selected_recipe_ids_json": "[401,404,406,423,424,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="LogAuditEvent", kwargs={"household_id": 201, "user_id": 101, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0086",
        instruction="Plan a Dinner week for household '207' to start on '2027-07-04' with the precise use of '401','404','406','423','425','433','435'; generate the grocery list, check the inventory at store '9008', document a 'create' audit for the list, and give back the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 107}),
            Action(name="CreateMealPlan", kwargs={"household_id": 207, "week_start_date": "2027-07-04", "created_by_user_id": 107}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-07-04", "selected_recipe_ids_json": "[401,404,406,423,425,433,435]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9008}),
            Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0087",
        instruction="Initiate scheduling for a Dinner week for household '204' beginning on '2027-01-24' using precisely '423','424','425','427','432','433','434'; assemble the grocery list, confirm availability at store '9004', record an audit for 'create' action on the list, and provide the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 104}),
            Action(name="CreateMealPlan", kwargs={"household_id": 204, "week_start_date": "2027-01-24", "created_by_user_id": 104}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-01-24", "selected_recipe_ids_json": "[423,424,425,427,432,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9004}),
            Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0088",
        instruction="Plan a Dinner week for household '205' starting on '2027-01-31' employing exactly '401','403','404','423','427','433','434'; construct the grocery list, ensure validation at store '9005', document the creation of the grocery-list, and supply the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 105}),
            Action(name="CreateMealPlan", kwargs={"household_id": 205, "week_start_date": "2027-01-31", "created_by_user_id": 105}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-01-31", "selected_recipe_ids_json": "[401,403,404,423,427,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 205, "created_by_user_id": 105}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9005}),
            Action(name="LogAuditEvent", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0089",
        instruction="Handle the scheduling of a Dinner week for household '206' beginning '2027-02-07' utilizing precisely '402','404','405','423','424','432','434'; compile the grocery list, confirm store '9006', record a 'create' audit for the list, and provide the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 106}),
            Action(name="CreateMealPlan", kwargs={"household_id": 206, "week_start_date": "2027-02-07", "created_by_user_id": 106}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-02-07", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9006}),
            Action(name="LogAuditEvent", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0090",
        instruction="Coordinate the scheduling of a Dinner week for household '207' commencing on '2027-02-14' employing exactly '401','404','406','423','425','433','435'; assemble the grocery list, ensure availability at store '9007', document a 'create' audit for the list, and furnish the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 107}),
            Action(name="CreateMealPlan", kwargs={"household_id": 207, "week_start_date": "2027-02-14", "created_by_user_id": 107}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-02-14", "selected_recipe_ids_json": "[401,404,406,423,425,433,435]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9007}),
            Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0091",
        instruction="Coordinate a Dinner week for household '201' commencing on '2027-03-14' utilizing specifically '401','404','406','423','424','433','434'; prepare the grocery list, verify store '9002', document the list creation process, and provide the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 101}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2027-03-14", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-03-14", "selected_recipe_ids_json": "[401,404,406,423,424,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9002}),
            Action(name="LogAuditEvent", kwargs={"household_id": 201, "user_id": 101, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0092",
        instruction="Organize a Dinner week for household '202' starting '2027-03-21' by incorporating exactly '402','404','405','423','424','432','434'; assemble the grocery list, confirm store '9003', record a 'create' audit for the list, and supply the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 102}),
            Action(name="CreateMealPlan", kwargs={"household_id": 202, "week_start_date": "2027-03-21", "created_by_user_id": 102}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-03-21", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0093",
        instruction="Ensure to arrange a Dinner week for household '203' commencing '2027-03-28' using precisely '407','404','427','423','402','425','429'; compile the grocery list, confirm store '9004', record the list creation, and provide the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 103}),
            Action(name="CreateMealPlan", kwargs={"household_id": 203, "week_start_date": "2027-03-28", "created_by_user_id": 103}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-03-28", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 203, "created_by_user_id": 103}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9004}),
            Action(name="LogAuditEvent", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0094",
        instruction="Ensure to arrange a Dinner week for household '204' starting '2027-04-04' using precisely '423','424','425','427','432','433','434'; compile the grocery list, confirm store '9005', record a 'create' audit for the list, and provide the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 104}),
            Action(name="CreateMealPlan", kwargs={"household_id": 204, "week_start_date": "2027-04-04", "created_by_user_id": 104}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-04-04", "selected_recipe_ids_json": "[423,424,425,427,432,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 204, "created_by_user_id": 104}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9005}),
            Action(name="LogAuditEvent", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0095",
        instruction="Coordinate a Dinner week for household '206' commencing '2027-04-18' utilizing precisely '402','404','405','423','424','432','434'; compile the grocery list, confirm store '9007', document the list creation, and provide the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 106}),
            Action(name="CreateMealPlan", kwargs={"household_id": 206, "week_start_date": "2027-04-18", "created_by_user_id": 106}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-04-18", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 206, "created_by_user_id": 106}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9007}),
            Action(name="LogAuditEvent", kwargs={"household_id": 206, "user_id": 106, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0096",
        instruction="Arrange a Dinner week for household '207' beginning '2027-04-25' with precisely '401','404','406','423','425','433','435'; create the grocery list, verify store '9008', register a 'create' audit for the list, and supply the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 107}),
            Action(name="CreateMealPlan", kwargs={"household_id": 207, "week_start_date": "2027-04-25", "created_by_user_id": 107}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-04-25", "selected_recipe_ids_json": "[401,404,406,423,425,433,435]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 207, "created_by_user_id": 107}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9008}),
            Action(name="LogAuditEvent", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0097",
        instruction="Handle the scheduling of a Dinner week for household '208' commencing '2027-05-02' by exclusively using '407','404','427','423','402','425','429'; create the grocery list, check store '9009', document the list creation, and provide the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 108}),
            Action(name="CreateMealPlan", kwargs={"household_id": 208, "week_start_date": "2027-05-02", "created_by_user_id": 108}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-05-02", "selected_recipe_ids_json": "[407,404,427,423,402,425,429]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 208, "created_by_user_id": 108}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9009}),
            Action(name="LogAuditEvent", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0098",
        instruction="Coordinate the scheduling of a Dinner week for household '210' associated with user '110' beginning '2027-05-16' utilizing solely '401','403','406','424','427','432','434'; generate the grocery list, confirm store '9001', record the list creation, and deliver the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 110}),
            Action(name="CreateMealPlan", kwargs={"household_id": 210, "week_start_date": "2027-05-16", "created_by_user_id": 110}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-05-16", "selected_recipe_ids_json": "[401,403,406,424,427,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 210, "created_by_user_id": 110}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="LogAuditEvent", kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0099",
        instruction="Organize a Dinner week for household '201' beginning '2027-05-23' utilizing precisely '401','404','406','423','424','433','434'; compile the grocery list, confirm store '9002', document a 'create' audit for the list, and provide the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 101}),
            Action(name="CreateMealPlan", kwargs={"household_id": 201, "week_start_date": "2027-05-23", "created_by_user_id": 101}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-05-23", "selected_recipe_ids_json": "[401,404,406,423,424,433,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 201, "created_by_user_id": 101}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9002}),
            Action(name="LogAuditEvent", kwargs={"household_id": 201, "user_id": 101, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
    Task(
        annotator="0",
        user_id="recipes_v5_0100",
        instruction="Plan a Dinner week for household '202' starting on '2027-05-30' using precisely '402','404','405','423','424','432','434'; prepare the grocery list, verify store '9003', record the list creation, and supply the 'list_id'.",
        actions=[
            Action(name="GetHouseholdByUserId", kwargs={"user_id": 102}),
            Action(name="CreateMealPlan", kwargs={"household_id": 202, "week_start_date": "2027-05-30", "created_by_user_id": 102}),
            Action(name="BulkAddMealPlanEntries", kwargs={"meal_plan_id": 6003, "week_start_date": "2027-05-30", "selected_recipe_ids_json": "[402,404,405,423,424,432,434]"}),
            Action(name="CreateGroceryListFromMealPlan", kwargs={"meal_plan_id": 6003, "household_id": 202, "created_by_user_id": 102}),
            Action(name="CheckStoreInventoryForList", kwargs={"list_id": 8003, "store_id": 9003}),
            Action(name="LogAuditEvent", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_lists", "action_enum": "create"}),
        ],
        outputs=["8003"],
    ),
]