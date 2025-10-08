from tau_bench.types import Action, Task


TASKS = [
    Task(
        annotator="v3",
        user_id="recipes_v3_task_001",
        instruction=(
            "You are Ryan Bennett (primary user). Design a weekly Dinner plan for household 201 for the week commencing 2025-09-01. Implement a 14-day exclusion window (2025-08-18 to 2025-09-01) and restrict cuisines to no more than two. Use servings_adult=2 and servings_child=1. Include child-friendly notes on each entry and subsequently create a grocery list associated with the plan. Return the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Ryan Bennett"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 101}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 201}),
            Action(name="ComputeNutritionTargets", kwargs={"member_ids": [301, 302, 303]}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 201, "week_start_date": "2025-09-01", "created_by_user_id": 101, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 101}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-01"}}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create", "payload_json": {"source_meal_plan_id": 6003}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_002",
        instruction=(
            "You are Sofia Martinez (primary user). Prepare a weekly Dinner plan for household 202 for the week beginning 2025-09-01. Enforce a 14-day exclusion window (2025-08-18 to 2025-09-01) and limit cuisines to at most two. Use servings_adult=2 and servings_child=1. Incorporate child-friendly notes and generate a linked grocery list. Return the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Sofia Martinez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 102}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 202}),
            Action(name="ComputeNutritionTargets", kwargs={"member_ids": [304, 305]}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 202, "week_start_date": "2025-09-01", "created_by_user_id": 102, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 102}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_003",
        instruction=(
            "Assume the identity of Emily Wang. Develop a weekly Dinner plan for household 203 beginning on 2025-09-01. Enforce a 14-day exclusion period (2025-08-18 to 2025-09-01) with a maximum of two cuisines. Use servings_adult=1 and servings_child=0. Include notes suitable for children on each entry and generate a connected grocery list. Provide the meal_plan_id and grocery_list_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Emily Wang"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 103}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 203}),
            Action(name="ComputeNutritionTargets", kwargs={"member_ids": [306]}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 203, "week_start_date": "2025-09-01", "created_by_user_id": 103, "servings_adult": 1, "servings_child": 0, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 103}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_004",
        instruction=(
            "As Daniel Brown, formulate a weekly Dinner plan for household 204 commencing on 2025-09-08. Implement a 14-day exclusion period (2025-08-25 to 2025-09-08) and restrict cuisines to two at most. Utilize servings_adult=2 and servings_child=2. Incorporate child-friendly notes and produce a linked grocery list. Return the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Daniel Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 104}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 204}),
            Action(name="ComputeNutritionTargets", kwargs={"member_ids": [307, 308, 309, 310]}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 204, "week_start_date": "2025-09-08", "created_by_user_id": 104, "servings_adult": 2, "servings_child": 2, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 104}),
            Action(name="RecordAuditLog", kwargs={"household_id": 204, "user_id": 104, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-08"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_005",
        instruction=(
            "You are Anjali Shah. Develop a weekly Dinner plan for household 205 beginning the week of 2025-09-01. Implement a 14-day exclusion period (2025-08-18 to 2025-09-01) and restrict cuisines to a maximum of two. Utilize servings_adult=2 and servings_child=3. Include child-friendly notes and generate an associated grocery list. Provide IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Anjali Shah"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 105}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 205}),
            Action(name="ComputeNutritionTargets", kwargs={"member_ids": [311, 312, 313, 314, 315]}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 205, "week_start_date": "2025-09-01", "created_by_user_id": 105, "servings_adult": 2, "servings_child": 3, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 105}),
            Action(name="RecordAuditLog", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-01"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_006",
        instruction=(
            "You are Michael Peterson. Construct a weekly Dinner plan for household 206 for the week commencing on 2025-09-01. Enforce a 14-day exclusion window (2025-08-18 to 2025-09-01) and limit cuisines to no more than two. Apply servings_adult=2 and servings_child=0. Incorporate child-friendly notes and create a connected grocery list. Submit IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Michael Peterson"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 106}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 206}),
            Action(name="ComputeNutritionTargets", kwargs={"member_ids": [316, 317]}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 206, "week_start_date": "2025-09-01", "created_by_user_id": 106, "servings_adult": 2, "servings_child": 0, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 106}),
            Action(name="RecordAuditLog", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-01"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_007",
        instruction=(
            "Identify yourself as Olivia Brown. Develop a weekly Dinner plan for household 207 for the week starting on 2025-09-01. Implement a 14-day exclusion window (2025-08-18 to 2025-09-01) and restrict cuisines to a maximum of two. Utilize servings_adult=2 and servings_child=3. Incorporate child-friendly notes and generate a connected grocery list. Provide the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Olivia Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 107}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 207}),
            Action(name="ComputeNutritionTargets", kwargs={"member_ids": [318, 319, 320, 321, 322, 323]}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 207, "week_start_date": "2025-09-01", "created_by_user_id": 107, "servings_adult": 2, "servings_child": 3, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 107}),
            Action(name="RecordAuditLog", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-01"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_008",
        instruction=(
            "Identify yourself as Diego Rodriguez. Develop a weekly Dinner plan for household 208 for the week starting on 2025-09-01. Implement a 14-day exclusion window (2025-08-18 to 2025-09-01) and restrict cuisines to a maximum of two. Utilize servings_adult=2 and servings_child=1. Incorporate child-friendly notes and generate a connected grocery list. Provide the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Diego Rodriguez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 108}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 208}),
            Action(name="ComputeNutritionTargets", kwargs={"member_ids": [324, 325, 326]}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 208, "week_start_date": "2025-09-01", "created_by_user_id": 108, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 108}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_009",
        instruction=(
            "You are Grace Lee. Develop a weekly Dinner plan for household 209 for the week commencing 2025-09-01. Implement a 14-day exclusion window (2025-08-18 to 2025-09-01) and limit cuisines to a maximum of two. Use servings_adult=2 and servings_child=1. Include child-friendly notes and generate a linked grocery list. Return IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Grace Lee"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 109}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 209}),
            Action(name="ComputeNutritionTargets", kwargs={"member_ids": [327, 328, 329]}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 209, "week_start_date": "2025-09-01", "created_by_user_id": 109, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 109}),
            Action(name="RecordAuditLog", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-01"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_010",
        instruction=(
            "You are William Davis. Formulate a weekly Dinner plan for household 210 for the week initiating 2025-09-01. Enforce a 14-day exclusion window (2025-08-18 to 2025-09-01) and restrict cuisines to a maximum of two. Use servings_adult=2 and servings_child=0. Incorporate child-friendly notes and produce a linked grocery list. Return IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "William Davis"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 110}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 210}),
            Action(name="ComputeNutritionTargets", kwargs={"member_ids": [330, 331]}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 210, "week_start_date": "2025-09-01", "created_by_user_id": 110, "servings_adult": 2, "servings_child": 0, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 110}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v3",
        user_id="recipes_v3_task_011",
        instruction=(
            "You are Ryan Bennett. Ensure tonight's Dinner (2025-09-01) for household 201 is chosen using inventory items and pantry staples only (permit at most one missing non-staple ingredient). It must have at least 10g of protein and avoid recipes from the last 7 days. If several options are possible, choose the one with higher protein per serving, then fewer calories, followed by the lowest recipe_id. Document the preparation with a rating of 5, log an audit entry stating 'inventory dinner selection', and provide the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Ryan Bennett"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 101}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 201, "start_date": "2025-08-25", "end_date": "2025-09-01"}),
            Action(name="SelectInventoryDinnerAndLog", kwargs={"household_id": 201, "date_today": "2025-09-01", "min_protein_g": 10, "exclude_days_back": 7, "rating_int": 5, "allow_pantry_staples": True, "max_missing_ingredients": 1}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "inventory dinner selection", "date": "2025-09-01"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_012",
        instruction=(
            "You are Sofia Martinez. Handle tonight's Dinner (2025-09-01) for household 202 by selecting from inventory and pantry staples only (allowing at most one missing non-staple), making sure it includes at least 10g protein and disregarding recipes made in the previous 7 days. Favor options with higher protein first, then fewer calories, then the lowest recipe_id if several qualify. Note the preparation with a rating of 4, log an audit entry marking 'inventory dinner selection', and return the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Sofia Martinez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 102}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 202, "start_date": "2025-08-25", "end_date": "2025-09-01"}),
            Action(name="SelectInventoryDinnerAndLog", kwargs={"household_id": 202, "date_today": "2025-09-01", "min_protein_g": 10, "exclude_days_back": 7, "rating_int": 4, "allow_pantry_staples": True, "max_missing_ingredients": 1}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "inventory dinner selection", "date": "2025-09-01"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_013",
        instruction=(
            "Your name is Emily Wang. For household 203, select tonight's Dinner (2025-09-01) from inventory and pantry staples only, allowing at most one non-staple to be missing. Ensure it contains at least 10g of protein and doesn't repeat recipes from the past 7 days; resolve ties by selecting options with higher protein, then lower calories, and finally the smallest recipe_id. Document the preparation with a rating of 5, log an audit entry with 'inventory dinner selection', and return the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Emily Wang"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 103}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 203, "start_date": "2025-08-25", "end_date": "2025-09-01"}),
            Action(name="SelectInventoryDinnerAndLog", kwargs={"household_id": 203, "date_today": "2025-09-01", "min_protein_g": 10, "exclude_days_back": 7, "rating_int": 5, "allow_pantry_staples": True, "max_missing_ingredients": 1}),
            Action(name="RecordAuditLog", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "inventory dinner selection", "date": "2025-09-01"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_014",
        instruction=(
            "Assume the identity of Daniel Brown. For household 204, choose tonight's Dinner (2025-09-08) using inventory and pantry staples exclusively, permitting up to two missing non-staples, with a required protein content of at least 10g. Exclude recipes used in the prior 7 days; break ties by prioritizing higher protein, then lower calories, followed by the lowest recipe_id. Record the preparation with a 5-star rating, log an audit entry labeled 'inventory dinner selection', and provide the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Daniel Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 104}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 204, "start_date": "2025-09-01", "end_date": "2025-09-08"}),
            Action(name="SelectInventoryDinnerAndLog", kwargs={"household_id": 204, "date_today": "2025-09-08", "min_protein_g": 10, "exclude_days_back": 7, "rating_int": 5, "allow_pantry_staples": True, "max_missing_ingredients": 2}),
            Action(name="RecordAuditLog", kwargs={"household_id": 204, "user_id": 104, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "inventory dinner selection", "date": "2025-09-08"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_015",
        instruction=(
            "You are Anjali Shah. Make sure tonight's Dinner (2025-09-01) for household 205 is selected using inventory and pantry staples only (allow at most two missing non-staples), ensuring at least 10g protein and skipping recipes used in the past 7 days; break ties by prioritizing higher protein, then fewer calories, followed by the lowest recipe_id. Log preparation with a rating of 4, document an audit entry marked 'inventory dinner selection', and provide the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Anjali Shah"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 105}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 205, "start_date": "2025-08-25", "end_date": "2025-09-01"}),
            Action(name="SelectInventoryDinnerAndLog", kwargs={"household_id": 205, "date_today": "2025-09-01", "min_protein_g": 10, "exclude_days_back": 7, "rating_int": 4, "allow_pantry_staples": True, "max_missing_ingredients": 2}),
            Action(name="RecordAuditLog", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "inventory dinner selection", "date": "2025-09-01"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_016",
        instruction=(
            "You are Michael Peterson. Ensure that tonight's Dinner (2025-09-01) for household 206 is chosen using only inventory and pantry staples (allow at most one non-staple missing), containing at least 10g protein and excluding recipes from the previous 7 days; resolve ties by preferring higher protein, followed by lower calories, then the smallest recipe_id. Record preparation with a rating of 5, make an audit log with the note 'inventory dinner selection', and return the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Michael Peterson"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 106}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 206, "start_date": "2025-08-25", "end_date": "2025-09-01"}),
            Action(name="SelectInventoryDinnerAndLog", kwargs={"household_id": 206, "date_today": "2025-09-01", "min_protein_g": 10, "exclude_days_back": 7, "rating_int": 5, "allow_pantry_staples": True, "max_missing_ingredients": 1}),
            Action(name="RecordAuditLog", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "inventory dinner selection", "date": "2025-09-01"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_017",
        instruction=(
            "As Olivia Brown, you need to select tonight's Dinner (2025-09-01) for household 207 using only inventory and pantry staples (permit at most one non-staple absence), ensuring a minimum of 10g protein and excluding any recipe used within the last 7 days; resolve ties by preferring higher protein content, followed by lower calories, then the smallest recipe_id. Document the preparation with a rating of 4, record an audit entry labeled 'inventory dinner selection', and return the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Olivia Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 107}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 207, "start_date": "2025-08-25", "end_date": "2025-09-01"}),
            Action(name="SelectInventoryDinnerAndLog", kwargs={"household_id": 207, "date_today": "2025-09-01", "min_protein_g": 10, "exclude_days_back": 7, "rating_int": 4, "allow_pantry_staples": True, "max_missing_ingredients": 1}),
            Action(name="RecordAuditLog", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "inventory dinner selection", "date": "2025-09-01"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_018",
        instruction=(
            "As Diego Rodriguez, you need to choose tonight's Dinner (2025-09-01) for household 208 from only inventory and pantry staples (permit up to two non-staples to be missing), ensuring a minimum of 10g of protein and excluding any recipes from the previous 7 days; in case of a tie, prefer those with higher protein content, then lower calories, and finally the smallest recipe_id. Document the preparation with a rating of 5, record an audit entry marked 'inventory dinner selection', and return the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Diego Rodriguez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 108}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 208, "start_date": "2025-08-25", "end_date": "2025-09-01"}),
            Action(name="SelectInventoryDinnerAndLog", kwargs={"household_id": 208, "date_today": "2025-09-01", "min_protein_g": 10, "exclude_days_back": 7, "rating_int": 5, "allow_pantry_staples": True, "max_missing_ingredients": 2}),
            Action(name="RecordAuditLog", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "inventory dinner selection", "date": "2025-09-01"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_019",
        instruction=(
            "Assume the role of Grace Lee. Plan tonight's Dinner (2025-09-01) for household 209 using only inventory and pantry staples (permit at most one missing non-staple). Ensure the meal provides at least 10g of protein and omit any recipe used in the previous 7 days; in the event of ties, prioritize by greater protein content, then lower calorie count, then the smallest recipe_id. Document preparation with a rating of 5, log an audit entry stating 'inventory dinner selection', and retrieve the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Grace Lee"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 109}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 209, "start_date": "2025-08-25", "end_date": "2025-09-01"}),
            Action(name="SelectInventoryDinnerAndLog", kwargs={"household_id": 209, "date_today": "2025-09-01", "min_protein_g": 10, "exclude_days_back": 7, "rating_int": 5, "allow_pantry_staples": True, "max_missing_ingredients": 1}),
            Action(name="RecordAuditLog", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "inventory dinner selection", "date": "2025-09-01"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_020",
        instruction=(
            "Take on the persona of William Davis. Arrange tonight's Dinner (2025-09-01) for household 210 using inventory and pantry staples solely (permit at most one missing non-staple). The dinner must contain at least 10g of protein and exclude recipes used over the past 7 days; resolve ties by opting for higher protein, then lesser calories, followed by the lowest recipe_id. Record preparation with a system rating of 4, note an audit entry saying 'inventory dinner selection', and retrieve the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "William Davis"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 110}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 210, "start_date": "2025-08-25", "end_date": "2025-09-01"}),
            Action(name="SelectInventoryDinnerAndLog", kwargs={"household_id": 210, "date_today": "2025-09-01", "min_protein_g": 10, "exclude_days_back": 7, "rating_int": 4, "allow_pantry_staples": True, "max_missing_ingredients": 1}),
            Action(name="RecordAuditLog", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "inventory dinner selection", "date": "2025-09-01"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v3",
        user_id="recipes_v3_task_021",
        instruction=(
            "Assume the role of Ryan Bennett. Coordinate a grocery order placement at store_id 9002 for the Bennett Family by using existing grocery list_id 8001, scheduled on 2025-09-02 from 14:00 to 16:00 with a subtotal of 1647 cents and a total of 1747 cents, ensuring an order placement audit is logged."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Ryan Bennett"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 101}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 201, "list_id": 8001, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-02T14:00:00Z", "slot_end_ts": "2025-09-02T16:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9002, "list_id": 8001}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_022",
        instruction=(
            "Take on the identity of Sofia Martinez. Arrange for a grocery order at store_id 9002 for the Martinez Household utilizing the existing grocery list_id 8002, planned for 2025-09-02 from 10:00 to 12:00 with a subtotal of 1647 cents and a total of 1747 cents, and ensure an order placement audit is documented."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Sofia Martinez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 102}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 202, "list_id": 8002, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-02T10:00:00Z", "slot_end_ts": "2025-09-02T12:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9002, "list_id": 8002}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_023",
        instruction=(
            "Your name is Ryan Bennett. Arrange a placed grocery order at store_id 9002 using your existing grocery list_id 8001, for the date 2025-09-03 between 14:00 and 16:00, with a subtotal of 1647 cents and a total of 1747 cents, ensuring that an order placement audit is documented."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Ryan Bennett"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 101}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 201, "list_id": 8001, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-03T14:00:00Z", "slot_end_ts": "2025-09-03T16:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9002, "list_id": 8001}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_024",
        instruction=(
            "Your name is Sofia Martinez. Schedule a grocery order at store_id 9002 using the existing grocery list_id 8002, planned for 2025-09-03 from 10:00 to 12:00, maintaining a subtotal of 1647 cents and a total of 1747 cents, with an order placement audit preserved."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Sofia Martinez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 102}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 202, "list_id": 8002, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-03T10:00:00Z", "slot_end_ts": "2025-09-03T12:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9002, "list_id": 8002}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_025",
        instruction=(
            "As Ryan Bennett, you need to arrange a grocery order at store_id 9002 using the existing grocery list_id 8001, set for 2025-09-04 between 14:00 and 16:00, with a subtotal of 1647 cents and a total of 1747 cents, ensuring an audit of the order placement is recorded."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Ryan Bennett"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 101}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 201, "list_id": 8001, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-04T14:00:00Z", "slot_end_ts": "2025-09-04T16:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9002, "list_id": 8001}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_026",
        instruction=(
            "As Sofia Martinez, you should coordinate a grocery order at store_id 9002 using the existing grocery list_id 8002, planned for 2025-09-04 from 10:00 to 12:00, with a subtotal of 1647 cents and a total of 1747 cents, making sure to record an audit of the order placement."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Sofia Martinez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 102}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 202, "list_id": 8002, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-04T10:00:00Z", "slot_end_ts": "2025-09-04T12:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9002, "list_id": 8002}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_027",
        instruction=(
            "You are Ryan Bennett. You intend to place a grocery order at store_id 9002 using your current grocery list_id 8001, planned for 2025-09-05 from 14:00 to 16:00, with a subtotal of 1647 cents and a total of 1747 cents, and ensure that an order placement audit is recorded."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Ryan Bennett"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 101}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 201, "list_id": 8001, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-05T14:00:00Z", "slot_end_ts": "2025-09-05T16:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9002, "list_id": 8001}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_028",
        instruction=(
            "You are Sofia Martinez. You aim to place a grocery order at store_id 9002 using your available grocery list_id 8002, scheduled for 2025-09-05 from 10:00 to 12:00, with a subtotal of 1647 cents and a total of 1747 cents, and ensure that an order placement audit is recorded."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Sofia Martinez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 102}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 202, "list_id": 8002, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-05T10:00:00Z", "slot_end_ts": "2025-09-05T12:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9002, "list_id": 8002}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_029",
        instruction=(
            "Act as Ryan Bennett. Coordinate a grocery order at store_id 9002 using the existing grocery list_id 8001. Schedule it for 2025-09-06 between 14:00 and 16:00 with a subtotal of 1647 cents and a total of 1747 cents. Ensure an order placement audit is recorded."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Ryan Bennett"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 101}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 201, "list_id": 8001, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-06T14:00:00Z", "slot_end_ts": "2025-09-06T16:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9002, "list_id": 8001}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_030",
        instruction=(
            "Play the role of Sofia Martinez. Organize a grocery order at store_id 9002 using the existing grocery list_id 8002. Plan it for 2025-09-06 from 10:00 to 12:00 with a subtotal of 1647 cents and a total of 1747 cents. Make sure an order placement audit is recorded."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Sofia Martinez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 102}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 202, "list_id": 8002, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-06T10:00:00Z", "slot_end_ts": "2025-09-06T12:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9002, "list_id": 8002}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v3",
        user_id="recipes_v3_task_031",
        instruction=(
            "Your name is Ryan Bennett. On 2025-09-01, there are no eggs available for 'Chocolate Chip Cookies' (414). Coordinate a selection of the egg-free alternative that has the shortest cook time among 415, 416, 417; if tied, choose the one with the lowest recipe_id. Make sure records indicate preparation occurred on 2025-09-01, include a rating of 5, and an audit reason as 'cookie recovery - egg missing'."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Ryan Bennett"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 101}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 415}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 416}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 417}),
            Action(name="AppendMealHistory", kwargs={"household_id": 201, "plan_date": "2025-09-01", "recipe_id": 417, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "cookie recovery - egg missing", "original_recipe_id": 414, "chosen_alternative": 417}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_032",
        instruction=(
            "Assume the identity of Sofia Martinez. On the date 2025-09-01, eggs are not available for 'Chocolate Chip Cookies' (414). Organize for the dessert recovery to pick an egg-free alternative with the shortest cook time within recipes 415, 416, 417; if there's a tie, opt for the one with the smallest recipe_id. Ensure the database shows preparation on 2025-09-01 at a rating of 4, and logs an audit entry stating 'cookie recovery - egg missing'."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Sofia Martinez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 102}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 415}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 416}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 417}),
            Action(name="AppendMealHistory", kwargs={"household_id": 202, "plan_date": "2025-09-01", "recipe_id": 417, "was_prepared": True, "rating_int": 4}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "cookie recovery - egg missing", "original_recipe_id": 414, "chosen_alternative": 417}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_033",
        instruction=(
            "You are Emily Wang. On 2025-09-01, 'Chocolate Chip Cookies' (414) lack eggs. Choose the egg-free option with the least cooking time among 415, 416, 417 (use the lowest recipe_id to break ties). Document the preparation on 2025-09-01 with a rating of 5 and register an audit as 'cookie recovery - egg missing'."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Emily Wang"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 103}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 415}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 416}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 417}),
            Action(name="AppendMealHistory", kwargs={"household_id": 203, "plan_date": "2025-09-01", "recipe_id": 417, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "cookie recovery - egg missing", "original_recipe_id": 414, "chosen_alternative": 417}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_034",
        instruction=(
            "You are Daniel Brown. On 2025-09-08, eggs are absent for 'Chocolate Chip Cookies' (414). Opt for the egg-free alternative having the minimal cook time among 415, 416, 417 (resolve ties with the lowest recipe_id). Record the preparation on 2025-09-08 with a rating of 5 and create an audit entry for 'cookie recovery - egg missing'."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Daniel Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 104}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 415}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 416}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 417}),
            Action(name="AppendMealHistory", kwargs={"household_id": 204, "plan_date": "2025-09-08", "recipe_id": 417, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 204, "user_id": 104, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "cookie recovery - egg missing", "original_recipe_id": 414, "chosen_alternative": 417}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_035",
        instruction=(
            "Assume the role of Anjali Shah. Note that eggs are absent for 'Chocolate Chip Cookies' (414) on 2025-09-01. Aim for a dessert recovery outcome where you select the egg-free option with the briefest cook time among 415, 416, 417 (use the lowest recipe_id as a tie-breaker). Confirm the database reflects preparation on 2025-09-01 with a rating of 4 and includes an audit entry stating 'cookie recovery - egg missing'."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Anjali Shah"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 105}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 415}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 416}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 417}),
            Action(name="AppendMealHistory", kwargs={"household_id": 205, "plan_date": "2025-09-01", "recipe_id": 417, "was_prepared": True, "rating_int": 4}),
            Action(name="RecordAuditLog", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "cookie recovery - egg missing", "original_recipe_id": 414, "chosen_alternative": 417}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_036",
        instruction=(
            "Assume you are Michael Peterson. Please be aware that eggs are unavailable for 'Chocolate Chip Cookies' (414) on 2025-09-01. Select the egg-free alternative with the minimum cook time among 415, 416, 417 (opt for the lowest recipe_id if tied). Ensure preparation is recorded on 2025-09-01 with a rating of 5 and annotate with 'cookie recovery - egg missing'."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Michael Peterson"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 106}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 415}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 416}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 417}),
            Action(name="AppendMealHistory", kwargs={"household_id": 206, "plan_date": "2025-09-01", "recipe_id": 417, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "cookie recovery - egg missing", "original_recipe_id": 414, "chosen_alternative": 417}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_037",
        instruction=(
            "You are Olivia Brown. For 'Chocolate Chip Cookies' (414), eggs are absent on 2025-09-01. Select an egg-free dessert substitute based on minimal cook time among 415, 416, 417, defaulting to the lowest recipe_id in case of a tie. It is crucial that records reflect preparation on 2025-09-01 with a rating of 4 and note the audit reason as 'cookie recovery - egg missing'."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Olivia Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 107}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 415}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 416}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 417}),
            Action(name="AppendMealHistory", kwargs={"household_id": 207, "plan_date": "2025-09-01", "recipe_id": 417, "was_prepared": True, "rating_int": 4}),
            Action(name="RecordAuditLog", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "cookie recovery - egg missing", "original_recipe_id": 414, "chosen_alternative": 417}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_038",
        instruction=(
            "You are Diego Rodriguez. On 2025-09-06, eggs are unavailable for 'Chocolate Chip Cookies' (414). Ensure that the dessert contingency chooses the egg-free option with the least cook time from 415, 416, 417, resolving ties with the lowest recipe_id. Make certain the records display preparation on 2025-09-06 with a 5-star rating and the audit reason 'cookie recovery - egg missing'."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Diego Rodriguez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 108}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 415}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 416}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 417}),
            Action(name="AppendMealHistory", kwargs={"household_id": 208, "plan_date": "2025-09-06", "recipe_id": 417, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "cookie recovery - egg missing", "original_recipe_id": 414, "chosen_alternative": 417}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_039",
        instruction=(
            "Act as Grace Lee. Eggs are absent for 'Chocolate Chip Cookies' (414) on 2025-09-01. Choose the egg-free option with the least cooking duration from 415, 416, 417 (use the smallest recipe_id as a tiebreaker). Document this preparation on 2025-09-01 with a rating of 5 and note 'cookie recovery - egg missing'."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Grace Lee"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 109}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 415}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 416}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 417}),
            Action(name="AppendMealHistory", kwargs={"household_id": 209, "plan_date": "2025-09-01", "recipe_id": 417, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "cookie recovery - egg missing", "original_recipe_id": 414, "chosen_alternative": 417}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_040",
        instruction=(
            "Take on the role of William Davis. Eggs are unavailable for 'Chocolate Chip Cookies' (414) on 2025-09-01. Opt for the egg-free substitute with the minimum cook time among 415, 416, 417 (select the lowest recipe_id if tied) as the dessert of choice. Make sure meal_history captures preparation on 2025-09-01 with a rating of 4 and includes an audit entry specifying 'cookie recovery - egg missing'."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "William Davis"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 110}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 415}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 416}),
            Action(name="GetRecipeDetails", kwargs={"recipe_id": 417}),
            Action(name="AppendMealHistory", kwargs={"household_id": 210, "plan_date": "2025-09-01", "recipe_id": 417, "was_prepared": True, "rating_int": 4}),
            Action(name="RecordAuditLog", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "cookie recovery - egg missing", "original_recipe_id": 414, "chosen_alternative": 417}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v3",
        user_id="recipes_v3_task_041",
        instruction=(
            "You take on the role of Emily Wang (user_id 103). Organize a Dinner plan for household 203 starting the week of 2025-09-08, including a 14-day exclusion and a maximum of 2 dinners per cuisine. Determine servings based on the number of adults vs children. Make sure child-friendly notes are included and compile a comprehensive grocery list associated with the plan. Provide the IDs in return."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Emily Wang"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 103}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 203}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 203, "week_start_date": "2025-09-08", "created_by_user_id": 103, "servings_adult": 1, "servings_child": 0, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 103}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_042",
        instruction=(
            "Act as Daniel Brown (user_id 104). Formulate a Dinner plan for household 204 with a start date of 2025-09-08, incorporating a 14-day exclusion period and allowing no more than 2 recipes per cuisine. Calculate servings from the count of adults and children. Include notes that are suitable for children and prepare a complete grocery list. Return the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Daniel Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 104}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 204}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 204, "week_start_date": "2025-09-08", "created_by_user_id": 104, "servings_adult": 2, "servings_child": 2, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 104}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_043",
        instruction=(
            "As Anjali Shah (user_id 105), develop a Dinner menu for household 205 starting the week of 2025-09-08 with an exclusion period of 14 days and a limit of 2 cuisines. Determine servings based on the count of adults and children. Add notes suitable for children and compile a unified grocery list. Provide the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Anjali Shah"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 105}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 205}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 205, "week_start_date": "2025-09-08", "created_by_user_id": 105, "servings_adult": 3, "servings_child": 2, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 105}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_044",
        instruction=(
            "As Michael Peterson (user_id 106), design a Dinner plan for household 206 commencing the week of 2025-09-08 with a 14-day exclusion period and maximum of 2 cuisines per week. Base servings on adult versus child counts. Include child-friendly notes and prepare a consolidated grocery list. Submit the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Michael Peterson"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 106}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 206}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 206, "week_start_date": "2025-09-08", "created_by_user_id": 106, "servings_adult": 2, "servings_child": 0, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 106}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_045",
        instruction=(
            "Assume the role of Olivia Brown (user_id 107). Formulate a Dinner plan for household 207 for the week starting on 2025-09-08, incorporating a 14-day exclusion with a maximum of 2 per cuisine type. Base servings on member counts (adults versus children). Confirm child-friendly notes are included and compile a unified grocery list. Provide the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Olivia Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 107}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 207}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 207, "week_start_date": "2025-09-08", "created_by_user_id": 107, "servings_adult": 2, "servings_child": 4, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 107}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_046",
        instruction=(
            "Assume the identity of Diego Rodriguez (user_id 108). Form a Dinner plan for household 208 for the week commencing 2025-09-08, adhering to a 14-day exclusion policy with max_per_cuisine=2. Calculate servings based on member counts (distinguishing adults from children). Make sure to include child-friendly notes and prepare an integrated grocery list. Submit the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Diego Rodriguez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 108}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 208}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 208, "week_start_date": "2025-09-08", "created_by_user_id": 108, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 108}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_047",
        instruction=(
            "Being Grace Lee (user_id 109), devise a Dinner strategy for household 209 beginning the week of 2025-09-08, adhering to a 14-day exclusion and limiting max_per_cuisine to 2. Calculate servings based on member numbers (adults versus children). Guarantee that notes suitable for children are included and generate a comprehensive grocery list. Provide the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Grace Lee"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 109}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 209}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 209, "week_start_date": "2025-09-08", "created_by_user_id": 109, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 109}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_048",
        instruction=(
            "As William Davis (user_id 110), formulate a Dinner plan for household 210 starting the week of 2025-09-08, including a 14-day exclusion and capping max_per_cuisine at 2. Use member counts (adults versus children) to determine servings. Make sure child-friendly annotations are incorporated and assemble a unified grocery list. Return the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "William Davis"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 110}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 210}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 210, "week_start_date": "2025-09-08", "created_by_user_id": 110, "servings_adult": 2, "servings_child": 0, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 110}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_049",
        instruction=(
            "As Emily Wang (user_id 103), organize a Dinner plan for household 203 beginning on week_start_date 2025-09-15 with a 14-day exclusion period and max_per_cuisine=2. Calculate servings based on the number of household members (adults vs children). Make sure to include child-friendly notes and compile a comprehensive grocery list. Provide the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Emily Wang"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 103}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 203}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 203, "week_start_date": "2025-09-15", "created_by_user_id": 103, "servings_adult": 1, "servings_child": 0, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 103}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_050",
        instruction=(
            "Assume the role of Daniel Brown (user_id 104) and arrange a Dinner plan for household 204 for the week starting on 2025-09-15 with a 14-day exclusion and max_per_cuisine=2. Determine the servings using the member counts (adults vs children). Ensure that child-friendly notes are incorporated and assemble a unified grocery list. Submit the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Daniel Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 104}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 204}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 204, "week_start_date": "2025-09-15", "created_by_user_id": 104, "servings_adult": 2, "servings_child": 2, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 104}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v3",
        user_id="recipes_v3_task_051",
        instruction=(
            "You are identified as Emily Wang (user_id 103) for household 203. Seek a 7-Dinner plan starting from week_start_date 2025-09-15 that adheres to max_per_cuisine=2, excludes recipes made in the past 14 days (window 2025-09-01 to 2025-09-15), and manages ingredient overlap, with servings_adult=2 and servings_child=1; subsequently generate a merged grocery list from the plan and provide the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Emily Wang"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 103}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 203, "start_date": "2025-09-01", "end_date": "2025-09-15"}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 203, "week_start_date": "2025-09-15", "created_by_user_id": 103, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 103}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_052",
        instruction=(
            "Identified as Daniel Brown (user_id 104) for household 204. Automatically create a 7-Dinner plan for week_start_date 2025-09-15, maintaining max_per_cuisine=2, a 14-day restriction period (2025-09-01 to 2025-09-15), and controlling overlap, with servings_adult=2 and servings_child=1; afterward, compile a combined grocery list and supply plan and list IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Daniel Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 104}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 204, "start_date": "2025-09-01", "end_date": "2025-09-15"}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 204, "week_start_date": "2025-09-15", "created_by_user_id": 104, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 104}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_053",
        instruction=(
            "Assume the identity of Anjali Shah (user_id 105) associated with household 205. Generate a 7-Dinner plan (2025-09-15) with a cap of 2 on cuisines and applying a 14-day exclusion period (window 2025-09-01 to 2025-09-15); set servings_adult=2 and servings_child=1; compile a unified grocery list and provide IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Anjali Shah"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 105}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 205, "start_date": "2025-09-01", "end_date": "2025-09-15"}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 205, "week_start_date": "2025-09-15", "created_by_user_id": 105, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 105}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_054",
        instruction=(
            "Act as Michael Peterson (user_id 106) linked to household 206. Develop a weekly Dinner plan (2025-09-15) limiting to 2 cuisines and excluding a 14-day period (window 2025-09-01 to 2025-09-15); allocate servings_adult=2 and servings_child=1; assemble a consolidated grocery list and supply IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Michael Peterson"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 106}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 206, "start_date": "2025-09-01", "end_date": "2025-09-15"}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 206, "week_start_date": "2025-09-15", "created_by_user_id": 106, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 106}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_055",
        instruction=(
            "Act as Olivia Brown (user_id 107) for household 207. Automatically generate a 7-Dinner plan (2025-09-15) considering a cuisine cap of 2 and adhering to a 14-day exclusion (from 2025-09-01 to 2025-09-15), with servings_adult=2 and servings_child=1. Compile a consolidated grocery list and provide the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Olivia Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 107}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 207, "start_date": "2025-09-01", "end_date": "2025-09-15"}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 207, "week_start_date": "2025-09-15", "created_by_user_id": 107, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 107}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_056",
        instruction=(
            "Operate as Diego Rodriguez (user_id 108) for household 208. Automatically generate a 7-Dinner plan (2025-09-15) having a cuisine cap of 2 while observing a 14-day exclusion, ensuring servings_adult=2 and servings_child=1. Assemble a consolidated grocery list and return the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Diego Rodriguez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 108}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 208, "week_start_date": "2025-09-15", "created_by_user_id": 108, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 108}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_057",
        instruction=(
            "Assuming the role of Grace Lee (user_id 109) for household 209, schedule an automatic creation of a 7-Dinner plan (2025-09-15) with a cuisine cap of 2 and a 14-day exclusion, ensuring servings_adult=2 and servings_child=1; compile a unified grocery list and provide the IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Grace Lee"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 109}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 209, "week_start_date": "2025-09-15", "created_by_user_id": 109, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 109}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_058",
        instruction=(
            "Act as William Davis (user_id 110) for household 210, and arrange for an automatic generation of a 7-Dinner plan (2025-09-15) with a cuisine cap of 2 and a 14-day exclusion period, maintaining servings_adult=2 and servings_child=1; assemble a consolidated grocery list and return the corresponding IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "William Davis"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 110}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 210, "week_start_date": "2025-09-15", "created_by_user_id": 110, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 110}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_059",
        instruction=(
            "Act as Emily Wang (user_id 103) for household 203. Formulate an additional weekly Dinner plan starting on the date 2025-09-22 with a cuisine limit of 2 and a 14-day exclusion period, ensuring servings_adult=2 and servings_child=1; compile an integrated grocery list and provide IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Emily Wang"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 103}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 203, "week_start_date": "2025-09-22", "created_by_user_id": 103, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateAndPopulateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 103}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_060",
        instruction=(
            "Assume the role of Daniel Brown (user_id 104) for household 204. Devise another weekly Dinner plan with the week commencing on 2025-09-22, incorporating a cuisine cap of 2 and a 14-day exclusion; compile the grocery list; supply IDs."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Daniel Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 104}),
            Action(name="ListHouseholdMembers", kwargs={"household_id": 204}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 204, "week_start_date": "2025-09-22", "created_by_user_id": 104, "servings_adult": 2, "servings_child": 2, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="CreateGroceryListFromPlan", kwargs={"meal_plan_id": 6003, "created_by_user_id": 104}),
            Action(name="RecordAuditLog", kwargs={"household_id": 204, "user_id": 104, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-22", "cuisine_cap": 2, "exclude_days_back": 14}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_061",
        instruction=(
            "Assume the role of Ryan Bennett (user_id 101) for household 201. With grocery list_id 8001, prioritize store_id 9001 in accordance with the policy. Relate only items that are not pantry staples to available products (omit items where pantry_staple_flag=true) and establish a placed order with a subtotal of 2596 cents and a total of 2796 cents, scheduled in the delivery slot 2025-09-02T18:00:00Z–20:00:00Z. Provide the new order_id."
        ),
        actions=[
            Action(name="GetGroceryList", kwargs={"list_id": 8001}),
            Action(name="ListStoreProductsByIngredientIds", kwargs={"store_id": 9001, "ingredient_ids": [1005, 1012, 1001, 1002, 1015, 1011]}),
            Action(name="CreateOrder", kwargs={"store_id": 9001, "household_id": 201, "list_id": 8001, "status_enum": "placed", "subtotal_cents": 2596, "total_cents": 2796, "slot_start_ts": "2025-09-02T18:00:00Z", "slot_end_ts": "2025-09-02T20:00:00Z"}),
            Action(name="AddOrderItems", kwargs={"order_id": 10003, "items": [{"product_id": 9101, "requested_qty": 1}, {"product_id": 9102, "requested_qty": 1}, {"product_id": 9103, "requested_qty": 1}, {"product_id": 9104, "requested_qty": 1}]}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9001, "list_id": 8001}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_062",
        instruction=(
            "Act as Sofia Martinez (user_id 102) for household 202. Utilize grocery list_id 8002 to decisively choose store_id 9002 (aggregator) and match the list items to the store's products. Construct a placed order having a subtotal of 1647 cents and a total of 1747 cents, with a slot of 2025-09-02T10:00:00Z–12:00:00Z. Supply the new order_id."
        ),
        actions=[
            Action(name="GetGroceryList", kwargs={"list_id": 8002}),
            Action(name="ListStoreProductsByIngredientIds", kwargs={"store_id": 9002, "ingredient_ids": [1026, 1039, 1038]}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 202, "list_id": 8002, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-02T10:00:00Z", "slot_end_ts": "2025-09-02T12:00:00Z"}),
            Action(name="AddOrderItems", kwargs={"order_id": 10003, "items": [{"product_id": 9111, "requested_qty": 1}, {"product_id": 9112, "requested_qty": 1}, {"product_id": 9113, "requested_qty": 1}]}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9002, "list_id": 8002}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_063",
        instruction=(
            "Assume the identity of Ryan Bennett (user_id 101). For household 201 and list_id 8001, handle the selection of store_id 9001 deterministically. Formulate a placed order with a subtotal of 2596 cents and a total of 2796 cents for the time slot 2025-09-03T18:00:00Z–20:00:00Z. Provide back the order_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Ryan Bennett"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 101}),
            Action(name="GetGroceryList", kwargs={"list_id": 8001}),
            Action(name="CreateOrder", kwargs={"store_id": 9001, "household_id": 201, "list_id": 8001, "status_enum": "placed", "subtotal_cents": 2596, "total_cents": 2796, "slot_start_ts": "2025-09-03T18:00:00Z", "slot_end_ts": "2025-09-03T20:00:00Z"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_064",
        instruction=(
            "Assume the role of Sofia Martinez (user_id 102). For household 202 and list_id 8002, utilize a strategy aggregator to deterministically pick store_id 9002 and coordinate the creation of a placed order with a subtotal of 1647 cents and a total of 1747 cents for the time slot 2025-09-03T10:00:00Z–12:00:00Z. Return the order_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Sofia Martinez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 102}),
            Action(name="GetGroceryList", kwargs={"list_id": 8002}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 202, "list_id": 8002, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-03T10:00:00Z", "slot_end_ts": "2025-09-03T12:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"strategy": "aggregator_selected", "list_id": 8002}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_065",
        instruction=(
            "Assume the role of Ryan Bennett (user_id 101). For household 201 (list_id 8001), choose store_id 9001 deterministically and generate a placed order with a subtotal of 2596 cents and a total of 2796 cents for the time slot 2025-09-04T18:00:00Z–20:00:00Z. Provide the order_id."
        ),
        actions=[
            Action(name="GetGroceryList", kwargs={"list_id": 8001}),
            Action(name="CreateOrder", kwargs={"store_id": 9001, "household_id": 201, "list_id": 8001, "status_enum": "placed", "subtotal_cents": 2596, "total_cents": 2796, "slot_start_ts": "2025-09-04T18:00:00Z", "slot_end_ts": "2025-09-04T20:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9001, "list_id": 8001}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_066",
        instruction=(
            "Assume the identity of Sofia Martinez (user_id 102). For household 202 (list_id 8002), choose store_id 9002 deterministically and execute the order with a subtotal of 1647 cents and a total of 1747 cents for the time window 2025-09-04T10:00:00Z–12:00:00Z. Provide the order_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Sofia Martinez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 102}),
            Action(name="GetGroceryList", kwargs={"list_id": 8002}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 202, "list_id": 8002, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-04T10:00:00Z", "slot_end_ts": "2025-09-04T12:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9002, "list_id": 8002}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_067",
        instruction=(
            "Assume the role of Ryan Bennett (user_id 101). For household 201 (list_id 8001), consistently select store_id 9001 and initiate a placed order with a subtotal of 2596 cents and a total of 2796 cents for the time slot 2025-09-05T18:00:00Z–20:00:00Z. Provide the order_id after completion."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Ryan Bennett"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 101}),
            Action(name="GetGroceryList", kwargs={"list_id": 8001}),
            Action(name="CreateOrder", kwargs={"store_id": 9001, "household_id": 201, "list_id": 8001, "status_enum": "placed", "subtotal_cents": 2596, "total_cents": 2796, "slot_start_ts": "2025-09-05T18:00:00Z", "slot_end_ts": "2025-09-05T20:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9001, "list_id": 8001}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_068",
        instruction=(
            "Act as Sofia Martinez (user_id 102). For household 202 (list_id 8002), consistently choose store_id 9002 and execute the order placement with a subtotal of 1647 cents and a total of 1747 cents for the time slot 2025-09-05T10:00:00Z–12:00:00Z. Deliver the order_id once done."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Sofia Martinez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 102}),
            Action(name="GetGroceryList", kwargs={"list_id": 8002}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 202, "list_id": 8002, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-05T10:00:00Z", "slot_end_ts": "2025-09-05T12:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9002, "list_id": 8002}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_069",
        instruction=(
            "Assume the role of Ryan Bennett (user_id 101). For household 201 (list_id 8001), deterministically choose store_id 9001 and proceed to place the order with a subtotal of 2596 cents and a total of 2796 cents for the time slot 2025-09-06T18:00:00Z–20:00:00Z. Provide the order_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Ryan Bennett"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 101}),
            Action(name="GetGroceryList", kwargs={"list_id": 8001}),
            Action(name="CreateOrder", kwargs={"store_id": 9001, "household_id": 201, "list_id": 8001, "status_enum": "placed", "subtotal_cents": 2596, "total_cents": 2796, "slot_start_ts": "2025-09-06T18:00:00Z", "slot_end_ts": "2025-09-06T20:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9001, "list_id": 8001}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_070",
        instruction=(
            "Take on the identity of Sofia Martinez (user_id 102). For household 202 (list_id 8002), deterministically select store_id 9002 and execute the order with a subtotal of 1647 cents and a total of 1747 cents for the time slot 2025-09-06T10:00:00Z–12:00:00Z. Supply the order_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Sofia Martinez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 102}),
            Action(name="GetGroceryList", kwargs={"list_id": 8002}),
            Action(name="CreateOrder", kwargs={"store_id": 9002, "household_id": 202, "list_id": 8002, "status_enum": "placed", "subtotal_cents": 1647, "total_cents": 1747, "slot_start_ts": "2025-09-06T10:00:00Z", "slot_end_ts": "2025-09-06T12:00:00Z"}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order", "payload_json": {"store_id": 9002, "list_id": 8002}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v3",
        user_id="recipes_v3_task_071",
        instruction=(
            "Assume the role of Ryan Bennett (user_id 101) for household 201. On 2025-09-07, for Dinner, handle the preparation of recipe_id 401 using inventory with substitutions that preserve grocery_section, are peanut‑free, and favor pantry staples. Check these substitutions against the household inventory; if they are valid, make a record of the preparation (rating 5) and ensure an audit entry documents the substitutions validation with action_enum 'validate_substitutions' referring to the created meal_history. Return the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Ryan Bennett"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 101}),
            Action(name="ProposeAndValidateSubstitutions", kwargs={"recipe_id": 401, "household_id": 201, "preserve_section": True, "require_peanut_free": True, "prefer_pantry_staples": True}),
            Action(name="AppendMealHistory", kwargs={"household_id": 201, "plan_date": "2025-09-07", "recipe_id": 401, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "validate_substitutions", "payload_json": {"recipe_id": 401}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_072",
        instruction=(
            "Act as Sofia Martinez (user_id 102) for household 202. On 2025-09-07, for Dinner, arrange the preparation of recipe_id 402 by using inventory with substitutions that maintain grocery_section, are peanut‑free, and prioritize pantry staples. Verify these substitutions against the household inventory; once validated, log the preparation (rating 4) and ensure an audit entry logs the substitutions validation with action_enum 'validate_substitutions' pointing to the created meal_history. Return the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Sofia Martinez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 102}),
            Action(name="ProposeAndValidateSubstitutions", kwargs={"recipe_id": 402, "household_id": 202, "preserve_section": True, "require_peanut_free": True, "prefer_pantry_staples": True}),
            Action(name="AppendMealHistory", kwargs={"household_id": 202, "plan_date": "2025-09-07", "recipe_id": 402, "was_prepared": True, "rating_int": 4}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "validate_substitutions", "payload_json": {"recipe_id": 402}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_073",
        instruction=(
            "Act as Emily Wang (user_id 103) for household 203. On 2025-09-07 for Dinner, create meal using recipe_id 403 with substitutions maintaining grocery_section, being peanut-free, and favoring pantry staples. Confirm substitutions align with household inventory; once aligned, document the preparation with a rating of 5 and ensure an audit logs the substitutions validation using action_enum 'validate_substitutions' linked to the generated meal_history. Provide the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Emily Wang"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 103}),
            Action(name="ProposeAndValidateSubstitutions", kwargs={"recipe_id": 403, "household_id": 203, "preserve_section": True, "require_peanut_free": True, "prefer_pantry_staples": True}),
            Action(name="AppendMealHistory", kwargs={"household_id": 203, "plan_date": "2025-09-07", "recipe_id": 403, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "validate_substitutions", "payload_json": {"recipe_id": 403}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_074",
        instruction=(
            "Operate as Daniel Brown (user_id 104) for household 204. On 2025-09-08 for Dinner, assemble the dish using recipe_id 404 with substitutions keeping grocery_section, ensuring peanut-free options, and prioritizing pantry staples. Verify substitutions against household inventory; upon verification, log the preparation with a rating of 5 and guarantee an audit records the substitutions validation using action_enum 'validate_substitutions' associated with the created meal_history. Yield the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Daniel Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 104}),
            Action(name="ProposeAndValidateSubstitutions", kwargs={"recipe_id": 404, "household_id": 204, "preserve_section": True, "require_peanut_free": True, "prefer_pantry_staples": True}),
            Action(name="AppendMealHistory", kwargs={"household_id": 204, "plan_date": "2025-09-08", "recipe_id": 404, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 204, "user_id": 104, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "validate_substitutions", "payload_json": {"recipe_id": 404}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_075",
        instruction=(
            "Assume the role of Anjali Shah (user_id 105) for household 205. For Dinner on 2025-09-07, coordinate preparation of recipe_id 405 using substitutions that maintain grocery_section, remain peanut-free, and prioritize pantry staples. Verify substitutions against the household inventory; if validated, document the preparation (rating 4) and ensure an audit entry logs the validation of substitutions with action_enum 'validate_substitutions' linking to the created meal_history. Provide the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Anjali Shah"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 105}),
            Action(name="ProposeAndValidateSubstitutions", kwargs={"recipe_id": 405, "household_id": 205, "preserve_section": True, "require_peanut_free": True, "prefer_pantry_staples": True}),
            Action(name="AppendMealHistory", kwargs={"household_id": 205, "plan_date": "2025-09-07", "recipe_id": 405, "was_prepared": True, "rating_int": 4}),
            Action(name="RecordAuditLog", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "validate_substitutions", "payload_json": {"recipe_id": 405}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_076",
        instruction=(
            "Act as Michael Peterson (user_id 106) for household 206. For Dinner on 2025-09-07, manage preparation of recipe_id 406 utilizing substitutions that keep grocery_section intact, are peanut-free, and favor pantry staples. Confirm substitutions against household inventory; upon validation, record the preparation (rating 5) and ensure an audit entry logs the validation of substitutions with action_enum 'validate_substitutions' associated with the created meal_history. Offer the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Michael Peterson"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 106}),
            Action(name="ProposeAndValidateSubstitutions", kwargs={"recipe_id": 406, "household_id": 206, "preserve_section": True, "require_peanut_free": True, "prefer_pantry_staples": True}),
            Action(name="AppendMealHistory", kwargs={"household_id": 206, "plan_date": "2025-09-07", "recipe_id": 406, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "validate_substitutions", "payload_json": {"recipe_id": 406}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_077",
        instruction=(
            "Act as Olivia Brown (user_id 107) for household 207. For Dinner on 2025-09-07, assemble recipe_id 407 utilizing substitutions that maintain grocery_section, are peanut-free, and favor pantry staples. Confirm substitutions with household inventory; once confirmed, document the preparation (rating 4) and make certain an audit record logs the substitutions verification with action_enum 'validate_substitutions' linked to the generated meal_history. Provide the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Olivia Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 107}),
            Action(name="ProposeAndValidateSubstitutions", kwargs={"recipe_id": 407, "household_id": 207, "preserve_section": True, "require_peanut_free": True, "prefer_pantry_staples": True}),
            Action(name="AppendMealHistory", kwargs={"household_id": 207, "plan_date": "2025-09-07", "recipe_id": 407, "was_prepared": True, "rating_int": 4}),
            Action(name="RecordAuditLog", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "validate_substitutions", "payload_json": {"recipe_id": 407}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_078",
        instruction=(
            "Assume the role of Diego Rodriguez (user_id 108) for household 208. For Dinner on 2025-09-07, create recipe_id 408 using substitutions that retain grocery_section, are peanut-free, and prioritize pantry staples. Authenticate substitutions against household inventory; upon authentication, record the preparation (rating 5) and ensure an audit record logs the substitutions confirmation with action_enum 'validate_substitutions' associated with the created meal_history. Return the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Diego Rodriguez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 108}),
            Action(name="ProposeAndValidateSubstitutions", kwargs={"recipe_id": 408, "household_id": 208, "preserve_section": True, "require_peanut_free": True, "prefer_pantry_staples": True}),
            Action(name="AppendMealHistory", kwargs={"household_id": 208, "plan_date": "2025-09-07", "recipe_id": 408, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "validate_substitutions", "payload_json": {"recipe_id": 408}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_079",
        instruction=(
            "Assume the role of Grace Lee (user_id 109) for household 209. On 2025-09-07, handle the preparation of recipe_id 409 for Dinner, utilizing substitutions that maintain grocery_section, are peanut‑free, and favor pantry staples. Confirm substitutions against household inventory; if valid, log the preparation (rating 5) and make sure an audit entry documents the substitutions validation with action_enum 'validate_substitutions' in relation to the generated meal_history. Return the history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Grace Lee"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 109}),
            Action(name="ProposeAndValidateSubstitutions", kwargs={"recipe_id": 409, "household_id": 209, "preserve_section": True, "require_peanut_free": True, "prefer_pantry_staples": True}),
            Action(name="AppendMealHistory", kwargs={"household_id": 209, "plan_date": "2025-09-07", "recipe_id": 409, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "validate_substitutions", "payload_json": {"recipe_id": 409}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_080",
        instruction=(
            "Take on the identity of William Davis (user_id 110) for household 210. You intend to coordinate the serving of recipe_id 410 for Dinner on 2025-09-07. Employ only substitutions that keep grocery_section, are peanut‑free, and prioritize pantry staples. The preparation must be open to audit: include an audit entry linked with the resulting meal_history using action_enum 'validate_substitutions'. If substitutions don't align with your household inventory, refrain from recording the preparation. Return the created meal_history_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "William Davis"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 110}),
            Action(name="ProposeAndValidateSubstitutions", kwargs={"recipe_id": 410, "household_id": 210, "preserve_section": True, "require_peanut_free": True, "prefer_pantry_staples": True}),
            Action(name="AppendMealHistory", kwargs={"household_id": 210, "plan_date": "2025-09-07", "recipe_id": 410, "was_prepared": True, "rating_int": 4}),
            Action(name="RecordAuditLog", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "validate_substitutions", "payload_json": {"recipe_id": 410}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_081",
        instruction=(
            "You are Ryan Bennett (user_id 101) for household 201. Design a Dinner meal plan for the week commencing on 2025-09-08, ensuring no recipes from the previous 14 days are included and that no cuisine type is represented more than twice. Utilize servings that correspond to the number of adults and children in the household. Upon completion, your household will evaluate recipe_id 401 on 2025-09-09, giving it a rating of 5. Guarantee the plan's auditability by linking an audit entry to the created plan. Provide the meal_plan_id."
        ),
        actions=[
            Action(name="ListHouseholdMembers", kwargs={"household_id": 201}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 201, "week_start_date": "2025-09-08", "created_by_user_id": 101, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="AppendMealHistory", kwargs={"household_id": 201, "plan_date": "2025-09-09", "recipe_id": 401, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-08"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_082",
        instruction=(
            "You are Sofia Martinez (user_id 102) for household 202. Prepare a Dinner meal plan for the week starting on 2025-09-08, excluding recipes from the last 14 days and restricting each cuisine to a maximum of two instances. Servings should correspond to the number of adults and children in the household. Following planning, the household will rate recipe_id 402 on 2025-09-09, awarding it a rating of 4. Ensure the plan is auditable by including a reference entry to the plan created. Return the meal_plan_id."
        ),
        actions=[
            Action(name="ListHouseholdMembers", kwargs={"household_id": 202}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 202, "week_start_date": "2025-09-08", "created_by_user_id": 102, "servings_adult": 1, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="AppendMealHistory", kwargs={"household_id": 202, "plan_date": "2025-09-09", "recipe_id": 402, "was_prepared": True, "rating_int": 4}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-08"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_083",
        instruction=(
            "Your role is Emily Wang (user_id 103) for household 203. Construct a Dinner meal plan for the week commencing 2025-09-08, ensuring no meals are repeated from the preceding 14 days and restricting each cuisine type to a maximum of two instances. The number of servings must account for both household adults and children. Once the plan is finalized, register a household rating for recipe_id 403 on 2025-09-09 with a rating of 5. Guarantee an audit entry is linked to the appointed plan. Provide the meal_plan_id as feedback."
        ),
        actions=[
            Action(name="ListHouseholdMembers", kwargs={"household_id": 203}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 203, "week_start_date": "2025-09-08", "created_by_user_id": 103, "servings_adult": 1, "servings_child": 0, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="AppendMealHistory", kwargs={"household_id": 203, "plan_date": "2025-09-09", "recipe_id": 403, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-08"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_084",
        instruction=(
            "You are assigned as Daniel Brown (user_id 104) for household 204. Develop a Dinner meal plan for the week beginning 2025-09-08, observing a recency exclusion of 14 days and a maximum of two appearances per cuisine. Ensure the number of servings accommodates both household adults and children. After completing the plan, the household will provide a rating for recipe_id 404 on 2025-09-09 with a score of 5. Ensure the plan is auditable with an entry connected to the created plan. Deliver the meal_plan_id."
        ),
        actions=[
            Action(name="ListHouseholdMembers", kwargs={"household_id": 204}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 204, "week_start_date": "2025-09-08", "created_by_user_id": 104, "servings_adult": 2, "servings_child": 2, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="AppendMealHistory", kwargs={"household_id": 204, "plan_date": "2025-09-09", "recipe_id": 404, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 204, "user_id": 104, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-08"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_085",
        instruction=(
            "Handle the role of Anjali Shah (user_id 105) for household 205. Coordinate a Dinner meal plan for the week commencing on 2025-09-08, ensuring no recipes used in the past 14 days are repeated and limiting cuisines to a maximum of two. Use the servings based on the number of adults and children. Following the planning, log a rating for recipe_id 405 on 2025-09-09 with a rating of 4. Ensure an audit entry reflects the created plan. Return the meal_plan_id."
        ),
        actions=[
            Action(name="ListHouseholdMembers", kwargs={"household_id": 205}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 205, "week_start_date": "2025-09-08", "created_by_user_id": 105, "servings_adult": 3, "servings_child": 2, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="AppendMealHistory", kwargs={"household_id": 205, "plan_date": "2025-09-09", "recipe_id": 405, "was_prepared": True, "rating_int": 4}),
            Action(name="RecordAuditLog", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-08"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_086",
        instruction=(
            "Assume the identity of Michael Peterson (user_id 106) for household 206. Coordinate a Dinner meal plan for the week of 2025-09-08, adhering to a strict 14-day exclusion policy and capping each cuisine type to two. The servings must align with household composition. After planning, record a rating for recipe_id 406 on 2025-09-09 with a rating of 5. Ensure that the plan is auditable by associating an entry with the created plan. Return the meal_plan_id."
        ),
        actions=[
            Action(name="ListHouseholdMembers", kwargs={"household_id": 206}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 206, "week_start_date": "2025-09-08", "created_by_user_id": 106, "servings_adult": 2, "servings_child": 0, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="AppendMealHistory", kwargs={"household_id": 206, "plan_date": "2025-09-09", "recipe_id": 406, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-08"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_087",
        instruction=(
            "Act as Olivia Brown (user_id 107) for household 207. Construct a Dinner meal plan for the week commencing 2025-09-08, ensuring a 14-day recency exclusion and no more than two instances per cuisine. Number of servings must match the number of adults and children. Once the plan is created, evaluate recipe_id 407 on 2025-09-09 with a rating of 4. Make the plan auditable by associating it with an entry. Provide the meal_plan_id afterward."
        ),
        actions=[
            Action(name="ListHouseholdMembers", kwargs={"household_id": 207}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 207, "week_start_date": "2025-09-08", "created_by_user_id": 107, "servings_adult": 2, "servings_child": 4, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="AppendMealHistory", kwargs={"household_id": 207, "plan_date": "2025-09-09", "recipe_id": 407, "was_prepared": True, "rating_int": 4}),
            Action(name="RecordAuditLog", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-08"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_088",
        instruction=(
            "Act as Diego Rodriguez (user_id 108) for household 208. Design a Dinner meal plan for the week beginning 2025-09-08, imposing a two-per-cuisine limit and excluding recipes from the past 14 days. The quantity of servings must correspond to the number of adults and children. Upon completion, submit a rating for recipe_id 408 on 2025-09-09 with a score of 5. Ensure the plan's audibility by linking it back to the created plan. Provide the meal_plan_id afterward."
        ),
        actions=[
            Action(name="ListHouseholdMembers", kwargs={"household_id": 208}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 208, "week_start_date": "2025-09-08", "created_by_user_id": 108, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="AppendMealHistory", kwargs={"household_id": 208, "plan_date": "2025-09-09", "recipe_id": 408, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-08"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_089",
        instruction=(
            "Assume the role of Grace Lee (user_id 109) for household 209. Formulate a Dinner meal plan for the week commencing on 2025-09-08, omitting any recipes used during the previous 14 days and limiting each cuisine to a maximum of two. Ensure servings match the number of adults and children. Following the planning, assign a rating of 5 to recipe_id 409 on 2025-09-09. Make certain the plan is auditable by linking it with an audit entry. Return the meal_plan_id."
        ),
        actions=[
            Action(name="ListHouseholdMembers", kwargs={"household_id": 209}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 209, "week_start_date": "2025-09-08", "created_by_user_id": 109, "servings_adult": 2, "servings_child": 1, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="AppendMealHistory", kwargs={"household_id": 209, "plan_date": "2025-09-09", "recipe_id": 409, "was_prepared": True, "rating_int": 5}),
            Action(name="RecordAuditLog", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-08"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_090",
        instruction=(
            "Act as William Davis (user_id 110) for household 210. Develop a Dinner meal plan for the week starting on 2025-09-08, applying a 14-day exclusion rule and limiting each cuisine to two entries. Servings must accurately represent the counts of adults and children. Following the planning, provide a rating for recipe_id 410 on 2025-09-09 with a score of 4. Ensure the created plan is linked to an audit entry. Return the meal_plan_id."
        ),
        actions=[
            Action(name="ListHouseholdMembers", kwargs={"household_id": 210}),
            Action(name="CreateMealPlanWithAutoEntries", kwargs={"household_id": 210, "week_start_date": "2025-09-08", "created_by_user_id": 110, "servings_adult": 2, "servings_child": 0, "max_per_cuisine": 2, "exclude_days_back": 14}),
            Action(name="AppendMealHistory", kwargs={"household_id": 210, "plan_date": "2025-09-09", "recipe_id": 410, "was_prepared": True, "rating_int": 4}),
            Action(name="RecordAuditLog", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"week_start_date": "2025-09-08"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="v3",
        user_id="recipes_v3_task_091",
        instruction=(
            "As Ryan Bennett (user_id 101) for household 201, handle the order lifecycle by updating order_id 10001 to a delivered status, then examine the order details and the linked grocery list. After cooking, decrement household inventory for ingredient_id 1006 by 100 units to account for usage. Make an audit entry for this order update. Return the order_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Ryan Bennett"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 101}),
            Action(name="SetOrderStatus", kwargs={"order_id": 10001, "status_enum": "delivered"}),
            Action(name="GetOrderDetails", kwargs={"order_id": 10001}),
            Action(name="GetGroceryList", kwargs={"list_id": 8001}),
            Action(name="UpdateInventoryQuantity", kwargs={"household_id": 201, "ingredient_id": 1006, "delta": -100}),
            Action(name="RecordAuditLog", kwargs={"household_id": 201, "user_id": 101, "entity_type": "orders", "entity_id": 10001, "action_enum": "delivered", "payload_json": {"list_id": 8001, "store_id": 9001, "total_cents": 2796, "slot_end": "2025-08-22T20:00:00Z"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_092",
        instruction=(
            "Acting as Sofia Martinez (user_id 102) for household 202, set order_id 10002 to delivered, inspect the associated grocery list to review the order, and update inventory by reducing ingredient_id 1039 by 80 units following cooking. Document an audit entry related to this order update. Return the order_id."
        ),
        actions=[
            Action(name="SetOrderStatus", kwargs={"order_id": 10002, "status_enum": "delivered"}),
            Action(name="GetOrderDetails", kwargs={"order_id": 10002}),
            Action(name="GetGroceryList", kwargs={"list_id": 8002}),
            Action(name="GetInventoryItems", kwargs={"household_id": 202}),
            Action(name="UpdateInventoryQuantity", kwargs={"household_id": 202, "ingredient_id": 1039, "delta": -80}),
            Action(name="RecordAuditLog", kwargs={"household_id": 202, "user_id": 102, "entity_type": "orders", "entity_id": 10002, "action_enum": "delivered", "payload_json": {"list_id": 8002, "store_id": 9002, "total_cents": 1747, "slot_end": "2025-08-21T16:00:00Z"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_093",
        instruction=(
            "As Emily Wang (user_id 103) for household 203, examine the orders made so far and the recent meal history from 2025-08-02 to 2025-08-15. Then, adjust the inventory to account for cooking activities by reducing ingredient_id 1003 by 100 units. Create an audit entry that details the inventory modification. Provide the ingredient_id used."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Emily Wang"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 103}),
            Action(name="GetOrdersForHousehold", kwargs={"household_id": 203}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 203, "start_date": "2025-08-02", "end_date": "2025-08-15"}),
            Action(name="GetInventoryItems", kwargs={"household_id": 203}),
            Action(name="UpdateInventoryQuantity", kwargs={"household_id": 203, "ingredient_id": 1003, "delta": -100}),
            Action(name="RecordAuditLog", kwargs={"household_id": 203, "user_id": 103, "entity_type": "inventory_items", "entity_id": 7031, "action_enum": "consume", "payload_json": {"ingredient_id": 1003, "delta": -100}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_094",
        instruction=(
            "As Daniel Brown (user_id 104) for household 204, analyze the household orders along with the recent meal history between 2025-08-01 and 2025-08-14. Subsequently, reduce the inventory for ingredient_id 1073 by 1 to reflect its usage. Create an audit log entry that references the inventory update record (inv_item_id). Provide the ingredient_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Daniel Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 104}),
            Action(name="GetOrdersForHousehold", kwargs={"household_id": 204}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 204, "start_date": "2025-08-01", "end_date": "2025-08-14"}),
            Action(name="GetInventoryItems", kwargs={"household_id": 204}),
            Action(name="UpdateInventoryQuantity", kwargs={"household_id": 204, "ingredient_id": 1073, "delta": -1}),
            Action(name="RecordAuditLog", kwargs={"household_id": 204, "user_id": 104, "entity_type": "inventory_items", "entity_id": 7047, "action_enum": "consume", "payload_json": {"ingredient_id": 1073, "delta": -1}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_095",
        instruction=(
            "As Anjali Shah (user_id 105) for household 205, examine the household's orders and recent meal history from 2025-07-31 to 2025-08-13. Then, lower the inventory of ingredient_id 1058 by 200 units to match cooking usage. Log an audit entry associated with this inventory adjustment using inv_item_id. Provide the ingredient_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Anjali Shah"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 105}),
            Action(name="GetOrdersForHousehold", kwargs={"household_id": 205}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 205, "start_date": "2025-07-31", "end_date": "2025-08-13"}),
            Action(name="GetInventoryItems", kwargs={"household_id": 205}),
            Action(name="UpdateInventoryQuantity", kwargs={"household_id": 205, "ingredient_id": 1058, "delta": -200}),
            Action(name="RecordAuditLog", kwargs={"household_id": 205, "user_id": 105, "entity_type": "inventory_items", "entity_id": 7054, "action_enum": "consume", "payload_json": {"ingredient_id": 1058, "delta": -200}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_096",
        instruction=(
            "Acting as Michael Peterson (user_id 106) for household 206, assess the household's orders and recent meal history from 2025-07-30 to 2025-08-12. Following meals, decrease the inventory for ingredient_id 1002 by 200 units. Document an audit entry for this modification using inv_item_id. Provide the ingredient_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Michael Peterson"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 106}),
            Action(name="GetOrdersForHousehold", kwargs={"household_id": 206}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 206, "start_date": "2025-07-30", "end_date": "2025-08-12"}),
            Action(name="GetInventoryItems", kwargs={"household_id": 206}),
            Action(name="UpdateInventoryQuantity", kwargs={"household_id": 206, "ingredient_id": 1002, "delta": -200}),
            Action(name="RecordAuditLog", kwargs={"household_id": 206, "user_id": 106, "entity_type": "inventory_items", "entity_id": 7060, "action_enum": "consume", "payload_json": {"ingredient_id": 1002, "delta": -200, "recent_history_ids": [6254, 6255, 6256, 6257, 6258]}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_097",
        instruction=(
            "Assume the role of Olivia Brown (user_id 107) for household 207. Examine orders and meal history from 2025-07-29 to 2025-08-11, then adjust the inventory by reducing ingredient_id 1024 by 100 units to account for usage. Log an audit entry associated with the inventory adjustment (utilize inv_item_id). Return the ingredient_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Olivia Brown"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 107}),
            Action(name="GetOrdersForHousehold", kwargs={"household_id": 207}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 207, "start_date": "2025-07-29", "end_date": "2025-08-11"}),
            Action(name="GetInventoryItems", kwargs={"household_id": 207}),
            Action(name="UpdateInventoryQuantity", kwargs={"household_id": 207, "ingredient_id": 1024, "delta": -100}),
            Action(name="RecordAuditLog", kwargs={"household_id": 207, "user_id": 107, "entity_type": "inventory_items", "entity_id": 7066, "action_enum": "consume", "payload_json": {"ingredient_id": 1024, "delta": -100, "recent_history_ids": [6261, 6262, 6263, 6264, 6265]}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_098",
        instruction=(
            "Act as Diego Rodriguez (user_id 108) for household 208. Assess household orders and meal history from 2025-08-01 to 2025-08-14, then decrease inventory for ingredient_id 1009 by 2 units to represent post-cooking consumption. Record an audit entry for this usage referencing the inv_item_id. Return the ingredient_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Diego Rodriguez"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 108}),
            Action(name="GetOrdersForHousehold", kwargs={"household_id": 208}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 208, "start_date": "2025-08-01", "end_date": "2025-08-14"}),
            Action(name="GetInventoryItems", kwargs={"household_id": 208}),
            Action(name="UpdateInventoryQuantity", kwargs={"household_id": 208, "ingredient_id": 1009, "delta": -2}),
            Action(name="RecordAuditLog", kwargs={"household_id": 208, "user_id": 108, "entity_type": "inventory_items", "entity_id": 7076, "action_enum": "consume", "payload_json": {"ingredient_id": 1009, "delta": -2, "recent_history_ids": [6268, 6269, 6270, 6271, 6272]}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_099",
        instruction=(
            "Assume the role of Grace Lee (user_id 109) for household 209. Examine household orders and meal history from 2025-07-31 to 2025-08-13, then decrease inventory for ingredient_id 1092 by 250 units to reflect usage. Document an audit entry linked to this modification referencing inv_item_id. Provide the ingredient_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "Grace Lee"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 109}),
            Action(name="GetOrdersForHousehold", kwargs={"household_id": 209}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 209, "start_date": "2025-07-31", "end_date": "2025-08-13"}),
            Action(name="GetInventoryItems", kwargs={"household_id": 209}),
            Action(name="UpdateInventoryQuantity", kwargs={"household_id": 209, "ingredient_id": 1092, "delta": -250}),
            Action(name="RecordAuditLog", kwargs={"household_id": 209, "user_id": 109, "entity_type": "inventory_items", "entity_id": 7078, "action_enum": "consume", "payload_json": {"ingredient_id": 1092, "delta": -250, "recent_history_ids": [6275, 6276, 6277, 6278, 6279]}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="v3",
        user_id="recipes_v3_task_100",
        instruction=(
            "Act as William Davis (user_id 110) for household 210. Evaluate household orders and meal history between 2025-07-31 and 2025-08-12, then lower inventory for ingredient_id 1056 by 200 units due to post-cooking consumption. Log an audit entry for this inventory adjustment. Provide the ingredient_id."
        ),
        actions=[
            Action(name="GetUserByFullName", kwargs={"full_name": "William Davis"}),
            Action(name="GetHouseholdByPrimaryUser", kwargs={"user_id": 110}),
            Action(name="GetOrdersForHousehold", kwargs={"household_id": 210}),
            Action(name="GetMealHistoryRange", kwargs={"household_id": 210, "start_date": "2025-07-31", "end_date": "2025-08-12"}),
            Action(name="GetInventoryItems", kwargs={"household_id": 210}),
            Action(name="UpdateInventoryQuantity", kwargs={"household_id": 210, "ingredient_id": 1056, "delta": -200}),
            Action(name="RecordAuditLog", kwargs={"household_id": 210, "user_id": 110, "entity_type": "inventory_items", "entity_id": 7087, "action_enum": "consume", "payload_json": {"ingredient_id": 1056, "pre_qty": 500, "post_qty": 300, "delta": -200}}),
        ],
        outputs=[]
    ),
]
