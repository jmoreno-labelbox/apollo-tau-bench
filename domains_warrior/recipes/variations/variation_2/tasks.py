from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="001",
        instruction=(
            "You are a meal planning assistant for the Mercer Family, "
            "your task is to remove the 'Grilled Salmon with Lemon' "
            "from their current meal plan for the week from Aug 25, 2025 to Aug 31, 2025. "
            "The reason for removal is a note with 'temporary fish aversion'. "
            "Replace it with 'Chicken Tacos' for the same date (2025-08-27) "
            "and add a note to 'use mild seasoning'. "
            "Also, log these modifications in the audit trail, use 'replacement for salmon' as reason for adding the new recipe. "
            "You should make sure that you do this change only for them and not also for other customers."
        ),
        actions=[
        
            Action(name="search_households_by_name", kwargs={"name_query": 'Mercer Family'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Grilled Salmon with Lemon'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 404}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'salmon'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6103}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Chicken Tacos'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "plan_date": "2025-08-27", "recipe_id": 402, "notes": "use mild seasoning"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6103, "action_enum": "delete", "payload_json": {"reason": "temporary fish aversion"}}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "replacement for salmon"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="002",
        instruction=(
            "You are assisting Lina Alvarez (user 102) from the Alvarez Household (household 202). "
            "She is out of 'Turkey Deli Slices' (ingredient 1039, inventory item 7022) "
            "and needs to update her inventory to reflect a quantity of 0. "
            "She also wants to add 'Chicken Breast' (ingredient 1001) "
            "to her grocery list (list_id 8002) as she plans to make a different lunch. "
            "Add 500g of chicken breast to the list. "
            "Log the inventory update in the audit logs."
        ),
        actions=[
         
            Action(name="search_users_by_name", kwargs={"name_query": 'Lina Alvarez'}),
            Action(name="search_households_by_name", kwargs={"name_query": 'Alvarez Household'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Turkey Deli Slices'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Chicken Breast'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 202, 'ingredient_id': 1039}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 202, 'ingredient_id': 1001}),

            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7022, "new_quantity": 0}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8002, "ingredient_id": 1001, "quantity": 500, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "inventory_items", "entity_id": 7022, "action_enum": "update", "payload_json": {"field": "quantity", "new_value": 0}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="003",
        instruction=(
            "You are helping Sarah Chen create a new meal plan. "
            "Create a meal plan for the week starting '2025-09-01' for her household. "
            "Then, add the 'Teriyaki Tofu Bowl' for '2025-09-01' "
            "and the 'Mediterranean Quinoa Salad' for '2025-09-02'. "
            "Log the creation of the meal plan in the audit logs."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Sarah Chen'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),

            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Teriyaki Tofu Bowl'}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Mediterranean Quinoa Salad'}),

            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-01", "created_by_user_id": 103}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-01", "recipe_id": 405, "notes": ""}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-02", "recipe_id": 406, "notes": ""}),
            Action(name="add_audit_log", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="004",
        instruction=(
            "You are assisting the Williams-Brown Family (household 204). "
            "They need a new meal plan for the week starting '2025-09-01' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "Add 'Gluten-Free Pasta' (ingredient 1065, 400g) and 'Almond Milk' (ingredient 1092, 1000ml) to this new list. "
            "Finally, log the creation of the grocery list."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Williams-Brown Family'}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2025-09-01", "created_by_user_id": 104}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 204, "meal_plan_id": 6003, "user_id": 104}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Gluten-Free Pasta'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Almond Milk'}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1065, "quantity": 400, "unit": "g"}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1092, "quantity": 1000, "unit": "ml"}),
            Action(name="add_audit_log", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_lists", "entity_id": 8003, "action_enum": "create"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="005",
        instruction=(
            "You are creating a grocery order for the Patel Extended Family. "
            "They need a new meal plan for the week starting '2025-09-01' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "Create an order from this list at 'Specialty Ingredients Direct'. "
            "The subtotal is 3500 cents and the total is 3850 cents. "
            "Log the order placement in the audit logs."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Patel Extended Family'}),
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2025-09-01", "created_by_user_id": 105}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 205, "meal_plan_id": 6003, "user_id": 105}),
            Action(name="search_stores_by_name", kwargs={"name_query": 'Specialty Ingredients Direct'}),
            Action(name="create_order_from_grocery_list", kwargs={"household_id": 205, "store_id": 9005, "list_id": 8003, "subtotal_cents": 3500, "total_cents": 3850}),
            Action(name="add_audit_log", kwargs={"household_id": 205, "user_id": 105, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="006",
        instruction=(
            "You are a recipe assistant for the Johnson Large Family. "
            "They have chicken breast in their inventory and want a suggestion for dinner tonight, August 20, 2025. "
            "They do not want any recipes they have prepared in the last 7 days. "
            "You should find the 'Chicken Tacos' recipe, confirm it meets the criteria, "
            "and then log it to their meal history as 'prepared' with a 5-star rating. "
            "Also, add an audit log for this action with reason 'User cooked recipe suggestion'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Johnson Large Family"}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "chicken breast"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 207, "ingredient_id": 1001}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 207, "days_ago": 7}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Chicken Tacos"}),
            Action(name="add_meal_history", kwargs={"household_id": 207, "recipe_id": 402, "plan_date": "2025-08-20", "was_prepared": True, "rating_int": 5}),
            Action(name="add_audit_log", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User cooked recipe suggestion"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="007",
        instruction=(
            "You are assisting the Alvarez Household, which has a child with a peanut allergy. "
            "They are making 'Spaghetti with Tomato Sauce' but are out of regular spaghetti. "
            "Find a suitable, peanut-free pasta alternative. "
            "Add 500g of 'Gluten-Free Pasta' to their grocery list for their next shopping trip. "
            "Log this decision to substitute ingredients "
            "in the audit trail for future reference with reason 'Substitution for out-of-stock item, allergy consideration'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Alvarez Household"}),
            Action(name="get_members_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Spaghetti with Tomato Sauce"}),
            Action(name="get_recipe_ingredients", kwargs={"recipe_id": 401}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Spaghetti Pasta"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 202, "ingredient_id": 1005}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Gluten-Free Pasta"}),
            Action(name="get_grocery_lists_by_household_id", kwargs={"household_id": 202}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8002, "ingredient_id": 1065, "quantity": 500, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "grocery_list_items", "entity_id": 8114, "action_enum": "create", "payload_json": {"reason": "Substitution for out-of-stock item, allergy consideration"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="008",
        instruction=(
            "You are a grocery shopping assistant for the Kim-Smith Family. "
            "First, create a new meal plan for them for the week starting '2025-09-08'. "
            "Add two peanut-free lunch recipes: 'Hummus Veggie Wrap' for the 8th and 'Turkey Sandwich' for the 9th. "
            "Then, generate a grocery list from this new meal plan. "
            "Also, create an order from this list at 'GrocerDash', with a subtotal of 2500 cents and a total of 2750 cents. "
            # "Log both the meal plan creation and the order placement."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Kim-Smith Family"}),
            Action(name="search_recipes", kwargs={"meal_type": "Lunch", "is_peanut_free": True}),
            Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2025-09-08", "created_by_user_id": 109}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-08", "recipe_id": 410, 'meal_type': 'Lunch'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-09", "recipe_id": 409, 'meal_type': 'Lunch'}),
            # Action(name="add_audit_log", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create"}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 209, "meal_plan_id": 6003, "user_id": 109}),
            Action(name="search_stores_by_name", kwargs={"name_query": "GrocerDash"}),
            Action(name="create_order_from_grocery_list", kwargs={"household_id": 209, "store_id": 9002, "list_id": 8003, "subtotal_cents": 2500, "total_cents": 2750}),
            # Action(name="add_audit_log", kwargs={"household_id": 209, "user_id": 109, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="009",
        instruction=(
            "You are a meal plan manager for the Mercer Family. "
            "Find their meal plan for the week of August 25th. "
            "Locate the entry which has the note 'Cut pasta shorter'. "
            "Update the notes for this specific entry to say 'Cut pasta shorter and add extra cheese for Maya'. "
            "Log this note modification in the audit trail with reason 'User request to add detail'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Mercer Family"}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, "start_date": "2025-08-25", "end_date": "2025-08-31", "notes_substring": "Cut pasta shorter"}),
            Action(name="update_meal_plan_entry_notes", kwargs={"entry_id": 6102, "new_notes": "Cut pasta shorter and add extra cheese for Maya"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6102, "action_enum": "update", "payload_json": {"field": "notes", "reason": "User request to add detail"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="010",
        instruction=(
            "You are an assistant for the Johnson Large Family. "
            "They just made 'Stuffed Bell Peppers' from their meal history 2025-08-08. "
            "Update this meal to mark it as prepared and give it a 3-star rating because it was just okay. "

            "Also, find 'Bell Pepper' in 'Garcia Household' household inventory "
            "and decrease the quantity by 4, as they were used in a recent recipe. "
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Johnson Large Family"}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Stuffed Bell Peppers"}),
            Action(name="get_meal_history_by_household_and_date", kwargs={"household_id": 207, "plan_date": "2025-08-08"}),

            Action(name="update_meal_history", kwargs={"history_id": 6262, "was_prepared": True, "rating_int": 3}),

            Action(name="search_households_by_name", kwargs={"name_query": "Garcia Household"}),

            Action(name="search_ingredients_by_name", kwargs={"name_query": "Bell Pepper"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 208, "ingredient_id": 1009}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7076, "new_quantity": 0}),

        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="011",
        instruction=(
            "You are assisting David Kowalski of the Kowalski Couple. "
            "He needs to modify a grocery list for the Alvarez Household. "
            "Find the item for 'Turkey Deli Slices' on this list and remove it. "
            "Replace it by adding 2 'Avocados' to the list, as he wants to make fresh guacamole instead. "
            "Log this substitution with reason 'User substitution'."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": "David Kowalski"}),
            Action(name="search_households_by_name", kwargs={"name_query": "Alvarez Household"}),
            Action(name="get_grocery_lists_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Turkey Deli Slices"}),

            Action(name="get_grocery_list_items_by_list_id_and_ingredient_id", kwargs={"list_id": 8002, "ingredient_id": 1039}),

            Action(name="remove_item_from_grocery_list", kwargs={"item_id": 8112}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Avocado"}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8002, "ingredient_id": 1086, "quantity": 2, "unit": "pcs"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 106, "entity_type": "grocery_list_items", "entity_id": 8112, "action_enum": "delete", "payload_json": {"reason": "User substitution"}}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 106, "entity_type": "grocery_list_items", "entity_id": 8114, "action_enum": "create", "payload_json": {"reason": "User substitution"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="012",
        instruction=(
            "You are a meal planning assistant for Sarah Chen. "
            "She wants a Italian-themed dinner plan for three days. "
            "Create a new meal plan for her starting the week of '2025-09-15'. "
            "Find three different dinner recipes with the 'Italian' cuisine and "
            "add them to the plan for the 15th, 16th, and 17th. "
            "The recipes should be 'Spaghetti with Tomato Sauce', 'Mushroom Risotto', and 'Gluten-Free Pasta Primavera'. "
            "Finally, log the creation of this new meal plan with theme set to Italian ."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": "Sarah Chen"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="search_recipes", kwargs={"cuisine": "Italian", "meal_type": "Dinner"}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Spaghetti with Tomato Sauce"}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Mushroom Risotto"}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Gluten-Free Pasta Primavera"}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-15", "created_by_user_id": 103}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-15", "recipe_id": 401}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-16", "recipe_id": 426}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-17", "recipe_id": 431}),
            Action(name="add_audit_log", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"theme": "Italian"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="013",
        instruction=(
            "You are a meal planning assistant for Sarah Chen. "
            "She wants a custom themed dinner plan for three days. "
            "Create a new meal plan for her starting the week of '2025-09-15'. "
            "The recipes should be 'Mediterranean Quinoa Salad', 'Baked Cod with Herbs', and 'Mediterranean Bowl' "
            " and add them to the plan for the 15th, 16th, and 17th."
            "Finally, log the creation of this new meal plan with theme set to 'Mediterranean'."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": "Sarah Chen"}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Mediterranean Quinoa Salad"}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Baked Cod with Herbs"}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Mediterranean Bowl"}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-15", "created_by_user_id": 103}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-15", "recipe_id": 406}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-16", "recipe_id": 425}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-17", "recipe_id": 442}),
            Action(name="add_audit_log", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create", "payload_json": {"theme": "Mediterranean"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="014",
        instruction=(
            "You are a meal planning assistant for the Alvarez Household. "
            "Your task is to remove 'Lentil Soup' from their meal plan for the week of Aug 25, 2025. "
            "The reason for removal is a note saying it's 'too warm for soup this week'. "
            "Replace it with 'Mediterranean Quinoa Salad' for the same date (2025-08-25) and add a note to 'add extra feta cheese'. "
            "Log these modifications in the audit trail, using 'weather-appropriate replacement' as the reason for the addition."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Alvarez Household'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Lentil Soup'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 408}),
            # Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'smoother texture'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6111}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Mediterranean Quinoa Salad'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6002, "plan_date": "2025-08-25", "recipe_id": 406, "notes": "add extra feta cheese"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6111, "action_enum": "delete", "payload_json": {"reason": "weather-appropriate replacement"}}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "weather-appropriate replacement"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="015",
        instruction=(
            "You are a meal planning assistant for the Mercer Family. "
            "Remove 'Spaghetti with Tomato Sauce' from their meal plan dated 2025-08-26. "
            "The user noted they 'want a lower-carb option'. "
            "Replace it with 'Teriyaki Tofu Bowl' for the same date and add a note 'make tofu extra crispy'. "
            "Log these changes in the audit trail with reason 'replacement for dietary preference'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Mercer Family'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Spaghetti with Tomato Sauce'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 401}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'pasta shorter'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6102}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Teriyaki Tofu Bowl'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "plan_date": "2025-08-26", "recipe_id": 405, "notes": "make tofu extra crispy"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6102, "action_enum": "delete", "payload_json": {"reason": "replacement for dietary preference"}}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "replacement for dietary preference"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="016",
        instruction=(
            "You are a meal planning assistant for the Alvarez Household. "
            "Your task is to remove 'Grilled Salmon with Lemon' from their meal plan for 2025-08-28. "
            "The user is 'not in the mood for fish'. "
            "Replace it with 'Baked Cod with Herbs' for the same date and add a note 'serve with a side of asparagus'. "
            "Log the modifications in the audit trail with reason 'user preference change'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Alvarez Household'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Grilled Salmon with Lemon'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 404}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'Flake salmon'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6114}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Baked Cod with Herbs'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6002, "plan_date": "2025-08-28", "recipe_id": 425, "notes": "serve with a side of asparagus"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6114, "action_enum": "delete", "payload_json": {"reason": "user preference change"}}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "user preference change"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="017",
        instruction=(
            "You are a meal planning assistant for the Mercer Family. "
            "Please remove 'Chickpea Curry' from their plan for 2025-08-28. "
            "Reason: 'Child doesn't like chickpeas'. "
            "Replace it with the 'Beef Stir-Fry' recipe for the same date, noting to 'use low-sodium soy sauce'. "
            "Ensure both actions are logged in the audit trail with reason 'replacement for child preference'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Mercer Family'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Chickpea Curry'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 403}),
            # Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'Mild curry'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6104}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Beef Stir-Fry'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "plan_date": "2025-08-28", "recipe_id": 423, "notes": "use low-sodium soy sauce"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6104, "action_enum": "delete", "payload_json": {"reason": "replacement for child preference"}}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "replacement for child preference"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="018",
        instruction=(
            "You are a meal planning assistant for the Alvarez Household. "
            "The user wants to swap 'Spaghetti with Tomato Sauce' on 2025-08-26 because they want something 'less heavy'. "
            "Replace it with the 'Keto Zucchini Lasagna'. "
            "Add a note 'use extra mozzarella'. "
            "Log the removal and addition in the audit trail with reason 'dietary swap for lighter meal'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Alvarez Household'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Spaghetti with Tomato Sauce'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 401}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'pasta shorter'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6112}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Keto Zucchini Lasagna'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6002, "plan_date": "2025-08-26", "recipe_id": 434, "notes": "use extra mozzarella"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6112, "action_enum": "delete", "payload_json": {"reason": "dietary swap for lighter meal"}}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "dietary swap for lighter meal"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="019",
        instruction=(
            "You are a meal planning assistant for the Mercer Family. "
            "The user has guests coming over on 2025-08-29 and wants to swap out the 'Teriyaki Tofu Bowl'. "
            "The reason is 'need a more universally liked dish'. "
            "Replace it with 'Stuffed Bell Peppers' for the same date. "
            "Add a note 'make a vegetarian filling option'. "
            "Log both modifications in the audit trail with reason 'guest-friendly meal replacement'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Mercer Family'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Teriyaki Tofu Bowl'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 405}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'Crispy tofu'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6105}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Stuffed Bell Peppers'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "plan_date": "2025-08-29", "recipe_id": 428, "notes": "make a vegetarian filling option"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6105, "action_enum": "delete", "payload_json": {"reason": "guest-friendly meal replacement"}}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "guest-friendly meal replacement"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="020",
        instruction=(
            "You are a meal planning assistant for the Alvarez Household. "
            "On 2025-08-29, they have 'Teriyaki Tofu Bowl' planned but want to change it. "
            "The reason is 'craving Korean food'. "
            "Please replace it with 'Korean Beef Bowl' for the same day. "
            "Add a note 'use chicken instead of beef'. "
            "Log the change with reason 'cuisine preference change'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Alvarez Household'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Teriyaki Tofu Bowl'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 405}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'Tofu well-cooked'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6115}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Korean Beef Bowl'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6002, "plan_date": "2025-08-29", "recipe_id": 427, "notes": "use chicken instead of beef"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6115, "action_enum": "delete", "payload_json": {"reason": "cuisine preference change"}}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "cuisine preference change"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="021",
        instruction=(
            "You are an assistant for the Mercer Family. "
            "On 2025-08-30, they have 'Mediterranean Quinoa Salad' planned. "
            "The user wants to swap it because they 'want a warmer meal'. "
            "Replace it with 'Lentil Soup'. "
            "Add a note 'serve with crusty bread'. "
            "Log the changes with the reason 'comfort food replacement'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Mercer Family'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Mediterranean Quinoa Salad'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 406}),
            # Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'Less lemon for child'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6106}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Lentil Soup'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "plan_date": "2025-08-30", "recipe_id": 408, "notes": "serve with crusty bread"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6106, "action_enum": "delete", "payload_json": {"reason": "comfort food replacement"}}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "comfort food replacement"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="022",
        instruction=(
            "You are assisting the Alvarez Household. "
            "On 2025-08-30, they have a salad planned, but the 'weather is turning cold'. "
            "Please remove the 'Mediterranean Quinoa Salad' from their meal plan. "
            "Replace it with 'Vegetarian Chili'. "
            "Add a note 'top with sour cream and cheddar'. "
            "Log the swap in the audit trail with the reason 'replacement for cold weather'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Alvarez Household'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Mediterranean Quinoa Salad'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 406}),
            # Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'Add cheese for child'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6116}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Vegetarian Chili'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6002, "plan_date": "2025-08-30", "recipe_id": 424, "notes": "top with sour cream and cheddar"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6116, "action_enum": "delete", "payload_json": {"reason": "replacement for cold weather"}}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "replacement for cold weather"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="023",
        instruction=(
            "You are a meal planning assistant for the Mercer Family. "
            "They want to swap their 'Thai Chicken Stir-Fry' on 2025-08-31. "
            "The reason is 'ran out of soy sauce'. "
            "Replace it with 'Chicken Tacos', a recipe they have ingredients for. "
            "Add a note 'serve with guacamole'. "
            "Log the change with the reason 'ran out of soy sauce'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Mercer Family'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Thai Chicken Stir-Fry'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 407}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'Reduce spice'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6107}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Chicken Tacos'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "plan_date": "2025-08-31", "recipe_id": 402, "notes": "serve with guacamole"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6107, "action_enum": "delete", "payload_json": {"reason": "ran out of soy sauce"}}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "ran out of soy sauce"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="024",
        instruction=(
            "You are assisting the Alvarez Household. "
            "The user wants to remove 'Thai Chicken Stir-Fry' from their 2025-08-31 plan, because they 'prefer something with beef'. "
            "Replace it with 'Beef Stir-Fry'. "
            "Add the note 'add extra broccoli'. "
            "Log the change in the audit trail with reason 'prefer something with beef'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Alvarez Household'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Thai Chicken Stir-Fry'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 407}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'Low spice'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6117}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Beef Stir-Fry'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6002, "plan_date": "2025-08-31", "recipe_id": 423, "notes": "add extra broccoli"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6117, "action_enum": "delete", "payload_json": {"reason": "prefer something with beef"}}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6117, "action_enum": "create", "payload_json": {"reason": "prefer something with beef"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="025",
        instruction=(
            "You are assisting the Mercer Family. "
            "They need to change their meal for 2025-08-25 from 'Chicken Tacos' because they 'had Mexican food last night'. "
            "Replace it with 'Spaghetti with Tomato Sauce'. "
            "Add a note 'use garlic bread on the side'. "
            "Log the change and its reason as 'had Mexican food last night'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Mercer Family'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Chicken Tacos'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 402}),
            # Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'Reduce chili powder'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6101}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Spaghetti with Tomato Sauce'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "plan_date": "2025-08-25", "recipe_id": 401, "notes": "use garlic bread on the side"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6101, "action_enum": "delete", "payload_json": {"reason": "had Mexican food last night"}}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "had Mexican food last night"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="026",
        instruction=(
            "You are a meal planning assistant for the Alvarez Household. "
            "They have 'Chicken Tacos' on the plan for 2025-08-27. "
            "They want to switch to something vegetarian for that day. "
            "Replace the tacos with 'Chickpea Curry'. "
            "Add a note 'serve with naan bread'. "
            "Log the removal and addition, noting 'vegetarian day' as the reason."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Alvarez Household'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Chicken Tacos'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 402}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'Peanut-free confirmed'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6113}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Chickpea Curry'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6002, "plan_date": "2025-08-27", "recipe_id": 403, "notes": "serve with naan bread"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6113, "action_enum": "delete", "payload_json": {"reason": "vegetarian day"}}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "vegetarian day"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="027",
        instruction=(
            "You are a meal planning assistant for the Mercer Family. "
            "They want to replace 'Spaghetti with Tomato Sauce' on 2025-08-26 with something that 'feels healthier'. "
            "Replace it with 'Mediterranean Quinoa Salad'. "
            "Add the note 'add grilled chicken for extra protein'. "
            "Log the reason 'user wants a healthier option' for the swap in the audit trail."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Mercer Family'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Spaghetti with Tomato Sauce'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 401}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'pasta shorter'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6102}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Mediterranean Quinoa Salad'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "plan_date": "2025-08-26", "recipe_id": 406, "notes": "add grilled chicken for extra protein"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6102, "action_enum": "delete", "payload_json": {"reason": "user wants a healthier option"}}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "user wants a healthier option"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="028",
        instruction=(
            "You are assisting the Alvarez Household. "
            "The user finds 'Lentil Soup' boring and wants to remove it from their plan for 2025-08-25. "
            "Replace it with 'Chicken Tacos', noting 'use corn tortillas'. "
            "Log the change with the reason 'user preference for more exciting meal'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Alvarez Household'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Lentil Soup'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 408}),
            # Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'smoother texture'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6111}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Chicken Tacos'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6002, "plan_date": "2025-08-25", "recipe_id": 402, "notes": "use corn tortillas"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6111, "action_enum": "delete", "payload_json": {"reason": "user preference for more exciting meal"}}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "user preference for more exciting meal"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="029",
        instruction=(
            "You are a meal planning assistant for the Mercer Family. "
            "The user wants to replace 'Grilled Salmon with Lemon' on 2025-08-27 because 'salmon is too expensive this week'. "
            "Find a budget-friendly alternative, 'Baked Cod with Herbs', and add it for the same date. "
            "Add a note 'use frozen cod fillets'. "
            "Log the change, citing 'budgetary reasons' for the swap."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Mercer Family'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Grilled Salmon with Lemon'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 404}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'Flake salmon'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6103}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Baked Cod with Herbs'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "plan_date": "2025-08-27", "recipe_id": 425, "notes": "use frozen cod fillets"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6103, "action_enum": "delete", "payload_json": {"reason": "salmon is too expensive this week"}}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "budgetary reasons"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="030",
        instruction=(
            "You are assisting the Alvarez Household. "
            "They need to remove 'Spaghetti with Tomato Sauce' on 2025-08-26 because of a 'gluten-free guest'. "
            "Replace it with 'Gluten-Free Pasta Primavera'. "
            "Add a note 'ensure all vegetables are fresh'. "
            "Log the change, with reason 'gluten-free guest'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Alvarez Household'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Spaghetti with Tomato Sauce'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 401}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'pasta shorter'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6112}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Gluten-Free Pasta Primavera'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6002, "plan_date": "2025-08-26", "recipe_id": 431, "notes": "ensure all vegetables are fresh"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6112, "action_enum": "delete", "payload_json": {"reason": "gluten-free guest"}}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "gluten-free guest"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="031",
        instruction=(
            "You are assisting the Mercer Family. "
            "They are removing 'Chickpea Curry' from their plan for 2025-08-28. "
            "The reason is 'not enough time for prep'. "
            "Replace it with a quicker meal: 'Chicken Tacos'. "
            "Add a note 'use pre-cooked chicken to save time'. "
            "Log the swap."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Mercer Family'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Chickpea Curry'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 403}),
            # Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'Mild curry'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6104}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Chicken Tacos'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "plan_date": "2025-08-28", "recipe_id": 402, "notes": "use pre-cooked chicken to save time"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6104, "action_enum": "delete", "payload_json": {"reason": "not enough time for prep"}}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "not enough time for prep"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="032",
        instruction=(
            "You are assisting the Alvarez Household. "
            "They need to replace 'Teriyaki Tofu Bowl' on 2025-08-29. "
            "Reason: 'want to try a new recipe'. "
            "Replace it with 'Moroccan Tagine'. "
            "Add a note 'keep spices mild for the kids'. "
            "Log this change."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Alvarez Household'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Teriyaki Tofu Bowl'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 405}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'Tofu well-cooked'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6115}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Moroccan Tagine'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6002, "plan_date": "2025-08-29", "recipe_id": 429, "notes": "keep spices mild for the kids"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6115, "action_enum": "delete", "payload_json": {"reason": "want to try a new recipe"}}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "want to try a new recipe"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="033",
        instruction=(
            "You are assisting the Mercer Family. "
            "They are removing 'Chicken Tacos' from their plan for 2025-08-25. "
            "The reason is 'want to use up leftover chickpeas'. "
            "Replace it with 'Chickpea Curry'. "
            "Add a note 'use coconut milk for creaminess'. "
            "Log the swap with 'inventory management swap' reason for create and 'want to use up leftover chickpeas' for delete."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Mercer Family'}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Chicken Tacos'}),
            Action(name="get_meal_plan_entries_by_recipe_id", kwargs={"recipe_id": 402}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, 'start_date': '2025-08-25', 'end_date': '2025-08-31', 'notes_substring': 'Reduce chili powder'}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6101}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Chickpea Curry'}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "plan_date": "2025-08-25", "recipe_id": 403, "notes": "use coconut milk for creaminess"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6101, "action_enum": "delete", "payload_json": {"reason": "want to use up leftover chickpeas"}}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6118, "action_enum": "create", "payload_json": {"reason": "inventory management swap"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="034",
        instruction=(
            "You are assisting Aiden Mercer from the Mercer Family. "
            "He has just used the last of the 'Spaghetti Pasta' "
            "and needs to update his inventory to reflect a quantity of 0. "
            "He wants to buy a different type of pasta, so add 500g of 'Penne Pasta' "
            "to their grocery list. "
            "Log the inventory update in the audit logs."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Aiden Mercer'}),
            Action(name="search_households_by_name", kwargs={"name_query": 'Mercer Family'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Spaghetti Pasta'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Penne Pasta'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 201, 'ingredient_id': 1005}),
            # Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 201, 'ingredient_id': 1062}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7001, "new_quantity": 0}),
            Action(name="get_grocery_lists_by_household_id", kwargs={"household_id": 201}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8001, "ingredient_id": 1062, "quantity": 500, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "inventory_items", "entity_id": 7001, "action_enum": "update", "payload_json": {"field": "quantity", "new_value": 0}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="035",
        instruction=(
            "You are assisting Sarah Chen. "
            "She has finished her 'Firm Tofu' "
            "and needs to update her inventory to 0. "
            "They need a new meal plan for the week starting '2025-09-01' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "She wants to try something new, so add 250g of 'Tempeh' "
            "to her grocery list. "
            "Log the inventory update."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Sarah Chen'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Firm Tofu'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Tempeh'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 203, 'ingredient_id': 1003}),
            # Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 203, 'ingredient_id': 1054}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7031, "new_quantity": 0}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-01", "created_by_user_id": 103}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 203, "meal_plan_id": 6003, "user_id": 103}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1054, "quantity": 250, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 203, "user_id": 103, "entity_type": "inventory_items", "entity_id": 7031, "action_enum": "update", "payload_json": {"field": "quantity", "new_value": 0}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="036",
        instruction=(
            "You are assisting Emma Johnson of the Johnson Large Family. "
            "They've run out of 'Eggs'. "
            "Please update the inventory to show a quantity of 0. "
            "They need a new meal plan for the week starting '2025-09-02' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "Then, add a dozen (12 pcs) 'Eggs' to their grocery list to restock. "
            "Log this inventory adjustment."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Emma Johnson'}),
            Action(name="search_households_by_name", kwargs={"name_query": 'Johnson Large Family'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Eggs'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 207, 'ingredient_id': 1030}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7065, "new_quantity": 0}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2025-09-02", "created_by_user_id": 107}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 207, "meal_plan_id": 6003, "user_id": 107}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1030, "quantity": 12, "unit": "pcs"}),
            Action(name="add_audit_log", kwargs={"household_id": 207, "user_id": 107, "entity_type": "inventory_items", "entity_id": 7065, "action_enum": "update", "payload_json": {"field": "quantity", "new_value": 0}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="038",
        instruction=(
            "You are assisting David Kowalski. "
            "He just used his last 'Avocado'. "
            "Update his inventory quantity to 0. "
            "They need a new meal plan for the week starting '2025-09-03' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "He wants 'Hummus' for snacks instead, so add 200g of it "
            "to their grocery list. "
            "Log the change."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'David Kowalski'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 106}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Avocado'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Hummus'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 206, 'ingredient_id': 1086}),
            # Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 206, 'ingredient_id': 1038}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7061, "new_quantity": 0}),
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2025-09-03", "created_by_user_id": 106}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 206, "meal_plan_id": 6003, "user_id": 106}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1038, "quantity": 200, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 206, "user_id": 106, "entity_type": "inventory_items", "entity_id": 7061, "action_enum": "update", "payload_json": {"field": "quantity", "new_value": 0}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="039",
        instruction=(
            "You are assisting James Thompson from the Thompson Retirement household. "
            "He's used all the 'Broccoli'. "
            "Update the inventory to reflect 0 quantity. "
            "They need a new meal plan for the week starting '2025-09-04' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "For variety, add 1 head of 'Cauliflower' to their grocery list. "
            "Log the inventory change."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'James Thompson'}),
            Action(name="search_households_by_name", kwargs={"name_query": 'Thompson Retirement'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Broccoli'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Cauliflower'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 210, 'ingredient_id': 1066}),
            # Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 210, 'ingredient_id': 1067}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7088, "new_quantity": 0}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2025-09-04", "created_by_user_id": 110}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 210, "meal_plan_id": 6003, "user_id": 110}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1067, "quantity": 1, "unit": "pcs"}),
            Action(name="add_audit_log", kwargs={"household_id": 210, "user_id": 110, "entity_type": "inventory_items", "entity_id": 7088, "action_enum": "update", "payload_json": {"field": "quantity", "new_value": 0}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="040",
        instruction=(
            "You are assisting Aiden Mercer again. "
            "He has run out of 'Chicken Breast'. "
            "Update the inventory quantity to 0. "
            "He wants to make burgers, so add 500g of 'Ground Beef' "
            "to the Mercer Family's grocery list. "
            "Log the update."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Aiden Mercer'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 101}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Chicken Breast'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Ground Beef'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 201, 'ingredient_id': 1001}),
            # Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 201, 'ingredient_id': 1045}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7004, "new_quantity": 0}),
            Action(name="get_grocery_lists_by_household_id", kwargs={"household_id": 201}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8001, "ingredient_id": 1045, "quantity": 500, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "inventory_items", "entity_id": 7004, "action_enum": "update", "payload_json": {"field": "quantity", "new_value": 0}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="041",
        instruction=(
            "You are assisting Lina Alvarez. "
            "She's finished her 'Classic Hummus'. "
            "Update the inventory for her household to reflect a quantity of 0. "
            "She wants to make a sandwich, so add a 'loaf' of 'Whole Wheat Bread' "
            "to her grocery list. "
            "Log the inventory update."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Lina Alvarez'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 102}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Hummus'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Whole Wheat Bread'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 202, 'ingredient_id': 1038}),
            # Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 202, 'ingredient_id': 1026}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7023, "new_quantity": 0}),
            Action(name="get_grocery_lists_by_household_id", kwargs={"household_id": 202}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8002, "ingredient_id": 1026, "quantity": 1, "unit": "loaf"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "inventory_items", "entity_id": 7023, "action_enum": "update", "payload_json": {"field": "quantity", "new_value": 0}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="042",
        instruction=(
            "You are helping Priya Patel. "
            "She used all her 'Basmati Rice'. "
            "Please update the Patel Extended Family inventory quantity to 0. "
            "They need a new meal plan for the week starting '2025-09-05' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "She now wants to buy 'Jasmine Rice', so add 1kg of it "
            "to their grocery list. "
            "Log the inventory adjustment."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Priya Patel'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 105}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Basmati Rice'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Jasmine Rice'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 205, 'ingredient_id': 1058}),
            # Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 205, 'ingredient_id': 1059}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7054, "new_quantity": 0}),
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2025-09-05", "created_by_user_id": 105}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 205, "meal_plan_id": 6003, "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1059, "quantity": 1000, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 205, "user_id": 105, "entity_type": "inventory_items", "entity_id": 7054, "action_enum": "update", "payload_json": {"field": "quantity", "new_value": 0}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="043",
        instruction=(
            "You are assisting Antonio Garcia of the Garcia Household. "
            "They've used their last 'Bell Pepper'. "
            "Update the inventory to 0. "
            "They need a new meal plan for the week starting '2025-09-06' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "He needs to make a salad, so add a bag of 'Romaine Lettuce' (300g) "
            "to their grocery list. "
            "Log the update."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Antonio Garcia'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 108}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Bell Pepper'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Romaine Lettuce'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 208, 'ingredient_id': 1009}),
            # Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 208, 'ingredient_id': 1013}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7076, "new_quantity": 0}),
            Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2025-09-06", "created_by_user_id": 108}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 208, "meal_plan_id": 6003, "user_id": 108}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1013, "quantity": 300, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 208, "user_id": 108, "entity_type": "inventory_items", "entity_id": 7076, "action_enum": "update", "payload_json": {"field": "quantity", "new_value": 0}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="044",
        instruction=(
            "You are helping Rachel Kim of the Kim-Smith Family. "
            "They just finished their 'Almond Milk'. "
            "Update the inventory to 0. "
            "They need a new meal plan for the week starting '2025-09-07' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "They want to try 'Oat Milk' next, so add 1000ml of it "
            "to their grocery list. "
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Rachel Kim'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 109}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Almond Milk'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Oat Milk'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 209, 'ingredient_id': 1092}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7078, "new_quantity": 0}),
            Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2025-09-07", "created_by_user_id": 109}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 209, "meal_plan_id": 6003, "user_id": 109}),
            # Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 209, 'ingredient_id': 1093}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1093, "quantity": 1000, "unit": "ml"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="045",
        instruction=(
            "You are assisting the Mercer Family. "
            "They've used up their 'Cheddar Cheese'. "
            "Update the inventory quantity to 0. "
            "Add 200g of 'Mozzarella Cheese' to their grocery list for pizza night. "
            "Log the inventory adjustment."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Mercer Family'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Cheddar Cheese'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Mozzarella Cheese'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 201, 'ingredient_id': 1024}),
            # Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 201, 'ingredient_id': 1025}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7012, "new_quantity": 0}),
            Action(name="get_grocery_lists_by_household_id", kwargs={"household_id": 201}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8001, "ingredient_id": 1025, "quantity": 200, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "inventory_items", "entity_id": 7012, "action_enum": "update", "payload_json": {"field": "quantity", "new_value": 0}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="046",
        instruction=(
            "You are assisting Lina Alvarez. "
            "She's out of 'Plain Greek Yogurt'. "
            "Update her inventory to a quantity of 0. "
            "She wants to make parfaits, so add 500g of 'Yogurt (Vanilla)' "
            "to her grocery list. "
            "Log the update."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Lina Alvarez'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 102}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Plain Greek Yogurt'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Yogurt (Vanilla)'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 202, 'ingredient_id': 1023}),
            # Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 202, 'ingredient_id': 1042}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7027, "new_quantity": 0}),
            Action(name="get_grocery_lists_by_household_id", kwargs={"household_id": 202}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8002, "ingredient_id": 1042, "quantity": 500, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "inventory_items", "entity_id": 7027, "action_enum": "update", "payload_json": {"field": "quantity", "new_value": 0}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="047",
        instruction=(
            "You are assisting Sarah Chen. "
            "She just used her last bit of 'Spinach'. "
            "Update her inventory quantity to 0. "
            "They need a new meal plan for the week starting '2025-09-07' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "She needs more greens, so add 150g of 'Kale' "
            "to her grocery list. "
            "Log the inventory change."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Sarah Chen'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Spinach'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Kale'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 203, 'ingredient_id': 1070}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7036, "new_quantity": 0}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-07", "created_by_user_id": 103}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 203, "meal_plan_id": 6003, "user_id": 103}),
            # Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 203, 'ingredient_id': 1071}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1071, "quantity": 150, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 203, "user_id": 103, "entity_type": "inventory_items", "entity_id": 7036, "action_enum": "update", "payload_json": {"field": "quantity", "new_value": 0}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="048",
        instruction=(
            "You are helping James Thompson. "
            "He has finished the 'Plain Greek Yogurt'. "
            "Update the Thompson Retirement inventory to 0. "
            "They need a new meal plan for the week starting '2025-09-07' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "He needs more dairy, so add 1000ml of 'Milk' "
            "to their grocery list. "
            "Log the inventory adjustment."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'James Thompson'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 110}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Plain Greek Yogurt'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Milk'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 210, 'ingredient_id': 1023}),
            # Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 210, 'ingredient_id': 1037}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7090, "new_quantity": 0}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2025-09-07", "created_by_user_id": 110}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 210, "meal_plan_id": 6003, "user_id": 110}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1037, "quantity": 1000, "unit": "ml"}),
            Action(name="add_audit_log", kwargs={"household_id": 210, "user_id": 110, "entity_type": "inventory_items", "entity_id": 7090, "action_enum": "update", "payload_json": {"field": "quantity", "new_value": 0}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="049",
        instruction=(
            "You are assisting Emma Johnson of the Johnson Large Family. "
            "They've run out of 'Milk'. "
            "Update the inventory to show a quantity of 0. "
            "They need a new meal plan for the week starting '2025-09-07' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "They need a dairy-free option for a guest, so add 1000ml of 'Almond Milk' "
            "to their grocery list. "
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Emma Johnson'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 107}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Milk'}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": 'Almond Milk'}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 207, 'ingredient_id': 1037}),
            # Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 207, 'ingredient_id': 1092}),
            Action(name="update_inventory_item_quantity", kwargs={"inv_item_id": 7063, "new_quantity": 0}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2025-09-07", "created_by_user_id": 107}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 207, "meal_plan_id": 6003, "user_id": 107}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1092, "quantity": 1000, "unit": "ml"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="050",
        instruction=(
            "You are helping Marcus Williams create a new meal plan for the Williams-Brown Family. "
            "Create a plan for the week starting '2025-09-08'. "
            "Add 'Gluten-Free Pasta Primavera' for '2025-09-08' and 'Vegan Black Bean Burgers' for '2025-09-10'. "
            "Log the creation of the meal plan in the audit logs."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Marcus Williams'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 104}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Gluten-Free Pasta Primavera'}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Vegan Black Bean Burgers'}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2025-09-08", "created_by_user_id": 104}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-08", "recipe_id": 431, "notes": ""}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-10", "recipe_id": 432, "notes": ""}),
            Action(name="add_audit_log", kwargs={"household_id": 204, "user_id": 104, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="051",
        instruction=(
            "You are helping Priya Patel from the Patel Extended Family. "
            "Create a new vegetarian meal plan for the week starting '2025-09-15'. "
            "Add 'Vegetarian Chili' for '2025-09-15' and 'Chickpea Curry' for '2025-09-16'. "
            "Log the creation of the meal plan."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Priya Patel'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 105}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Vegetarian Chili'}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Chickpea Curry'}),
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2025-09-15", "created_by_user_id": 105}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-15", "recipe_id": 424, "notes": ""}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-16", "recipe_id": 403, "notes": ""}),
            Action(name="add_audit_log", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="052",
        instruction=(
            "You are assisting David Kowalski. "
            "Create a new low-carb meal plan for the Kowalski Couple for the week starting '2025-09-22'. "
            "Add 'Keto Zucchini Lasagna' for '2025-09-22' and 'Heart-Healthy Baked Salmon' for '2025-09-23'. "
            "Log the meal plan creation."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'David Kowalski'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 106}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Keto Zucchini Lasagna'}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Heart-Healthy Baked Salmon'}),
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2025-09-22", "created_by_user_id": 106}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-22", "recipe_id": 434, "notes": ""}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-23", "recipe_id": 435, "notes": ""}),
            Action(name="add_audit_log", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="053",
        instruction=(
            "You are helping Emma Johnson of the Johnson Large Family. "
            "Create a new meal plan for the week of '2025-10-06'. "
            "Add 'Pancakes' for dinner on '2025-10-06' and 'Stuffed Bell Peppers' on '2025-10-07'. "
            "Log the new plan in the audit trail."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Emma Johnson'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 107}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Pancakes'}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Stuffed Bell Peppers'}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2025-10-06", "created_by_user_id": 107}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-10-06", "recipe_id": 422, "notes": ""}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-10-07", "recipe_id": 428, "notes": ""}),
            Action(name="add_audit_log", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="054",
        instruction=(
            "You are assisting Antonio Garcia of the Garcia Household. "
            "Create a meal plan for the week of '2025-09-01'. "
            "Add 'Chicken Tacos' for '2025-09-01' and 'Korean Beef Bowl' for '2025-09-03'. "
            "Log the plan creation."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Antonio Garcia'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 108}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Chicken Tacos'}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Korean Beef Bowl'}),
            Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2025-09-01", "created_by_user_id": 108}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-01", "recipe_id": 402, "notes": ""}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-03", "recipe_id": 427, "notes": ""}),
            Action(name="add_audit_log", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="055",
        instruction=(
            "You are helping Rachel Kim from the Kim-Smith Family. "
            "Create a new meal plan for the week of '2025-09-08'. "
            "Add 'Dairy-Free Coconut Curry' for '2025-09-09' and 'Vegan Black Bean Burgers' for '2025-09-11'. "
            "Log the new meal plan."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Rachel Kim'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 109}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Dairy-Free Coconut Curry'}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Vegan Black Bean Burgers'}),
            Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2025-09-08", "created_by_user_id": 109}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-09", "recipe_id": 433, "notes": ""}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-11", "recipe_id": 432, "notes": ""}),
            Action(name="add_audit_log", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="056",
        instruction=(
            "You are assisting James Thompson of the Thompson Retirement household. "
            "Create a heart-healthy meal plan for the week of '2025-09-15'. "
            "Add 'Heart-Healthy Baked Salmon' for '2025-09-15' and 'Baked Cod with Herbs' for '2025-09-17'. "
            "Log the creation of this plan."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'James Thompson'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 110}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Heart-Healthy Baked Salmon'}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Baked Cod with Herbs'}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2025-09-15", "created_by_user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-15", "recipe_id": 435, "notes": ""}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-17", "recipe_id": 425, "notes": ""}),
            Action(name="add_audit_log", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="057",
        instruction=(
            "You are helping Sarah Chen with another meal plan. "
            "Create a new plan for the week of '2025-09-22'. "
            "Add 'Vegan Black Bean Burgers' for '2025-09-22' and 'Buddha Bowl' for '2025-09-24'. "
            "Log the new plan."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Sarah Chen'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Vegan Black Bean Burgers'}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Buddha Bowl'}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-22", "created_by_user_id": 103}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-22", "recipe_id": 432, "notes": ""}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-09-24", "recipe_id": 446, "notes": ""}),
            Action(name="add_audit_log", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="059",
        instruction=(
            "You are helping Priya Patel with a flavorful meal plan. "
            "Create a new plan for the Patel Extended Family for the week of '2025-10-06'. "
            "Add 'Moroccan Tagine' for '2025-10-06' and 'Chickpea Curry' for '2025-10-08'. "
            "Log this new meal plan."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Priya Patel'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 105}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Moroccan Tagine'}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": 'Chickpea Curry'}),
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2025-10-06", "created_by_user_id": 105}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-10-06", "recipe_id": 429, "notes": ""}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "plan_date": "2025-10-08", "recipe_id": 403, "notes": ""}),
            Action(name="add_audit_log", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_plans", "entity_id": 6003, "action_enum": "create"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="060",
        instruction=(
            "You are a recipe assistant for the Mercer Family. "
            "They have Salmon Fillet in their freezer and want a suggestion for dinner tonight, August 21, 2025. "
            "They do not want any meals they have eaten in the last two weeks. "
            "Find the 'Grilled Salmon with Lemon' recipe, confirm it's suitable, "
            "and then log it to their meal history as 'prepared' with a 4-star rating. "
            "Also, add an audit log for this action with the reason 'User prepared a healthy dinner'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Mercer Family"}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Salmon Fillet"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 201, "ingredient_id": 1002}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 201, "days_ago": 14}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Grilled Salmon with Lemon"}),
            Action(name="add_meal_history", kwargs={"household_id": 201, "recipe_id": 404, "plan_date": "2025-08-21", "was_prepared": True, "rating_int": 4}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User prepared a healthy dinner"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="061",
        instruction=(
            "You are a recipe assistant for Sarah Chen. "
            "She has tofu in her fridge and wants a suggestion for dinner tonight, August 22, 2025. "
            "She has not eaten this meal in the past 6 days. "
            "Find the 'Teriyaki Tofu Bowl' recipe, confirm it meets the criteria, "
            "and then log it to her meal history as 'prepared' with a 5-star rating. "
            "Also, add an audit log for this action with the reason 'User enjoyed a suggested vegetarian meal'."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Sarah Chen'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Tofu"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 203, "ingredient_id": 1003}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 203, "days_ago": 6}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Teriyaki Tofu Bowl"}),
            Action(name="add_meal_history", kwargs={"household_id": 203, "recipe_id": 405, "plan_date": "2025-08-22", "was_prepared": True, "rating_int": 5}),
            Action(name="add_audit_log", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User enjoyed a suggested vegetarian meal"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="062",
        instruction=(
            "You are assisting the Garcia Household. "
            "They have ground beef and want a dinner idea for tonight, August 20, 2025. "
            "They haven't had this meal in the past week. "
            "Find the 'Stuffed Bell Peppers' recipe, confirm it's a good fit, "
            "and log it to their meal history as 'prepared' with a 4-star rating. "
            "Also, add an audit log for this action with reason 'User logged a favorite meal'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Garcia Household"}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Ground Beef"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 208, "ingredient_id": 1045}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 208, "days_ago": 7}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Stuffed Bell Peppers"}),
            Action(name="add_meal_history", kwargs={"household_id": 208, "recipe_id": 428, "plan_date": "2025-08-20", "was_prepared": True, "rating_int": 4}),
            Action(name="add_audit_log", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User logged a favorite meal"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="063",
        instruction=(
            "You are assisting the Patel Extended Family. "
            "They have lentils and want a suggestion for dinner tonight, August 23, 2025. "
            "They have not eaten this meal in the last 10 days. "
            "Find the 'Lentil Soup' recipe, confirm it meets the criteria, "
            "and then log it to their meal history as 'prepared' with a 5-star rating. "
            "Also, add an audit log for this action with reason 'User logged a prepared family meal'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Patel Extended Family"}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Lentils"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 205, "ingredient_id": 1053}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 205, "days_ago": 10}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Lentil Soup"}),
            Action(name="add_meal_history", kwargs={"household_id": 205, "recipe_id": 408, "plan_date": "2025-08-23", "was_prepared": True, "rating_int": 5}),
            Action(name="add_audit_log", kwargs={"household_id": 205, "user_id": 105, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User logged a prepared family meal"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="064",
        instruction=(
            "You are a recipe assistant for the Kowalski Couple. "
            "They have salmon and want a keto-friendly dinner for tonight, August 24, 2025. "
            "They haven't eaten this meal in last 14 days. "
            "Find the 'Heart-Healthy Baked Salmon' recipe, confirm it's suitable, "
            "and then log it to their meal history as 'prepared' with a 5-star rating. "
            "Also, add an audit log for this action with reason 'User logged a keto-friendly recipe'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Kowalski Couple"}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Salmon"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 206, "ingredient_id": 1002}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 206, "days_ago": 14}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Heart-Healthy Baked Salmon"}),
            Action(name="add_meal_history", kwargs={"household_id": 206, "recipe_id": 435, "plan_date": "2025-08-24", "was_prepared": True, "rating_int": 5}),
            Action(name="add_audit_log", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User logged a keto-friendly recipe"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="065",
        instruction=(
            "You are assisting the Williams-Brown Family. "
            "They have black beans in their pantry and want a vegan dinner for tonight, August 21, 2025. "
            "They haven't had this meal in the last week. "
            "Find the 'Vegan Black Bean Burgers' recipe, confirm it works, "
            "and log it to their meal history as 'prepared' with a 4-star rating. "
            "Add an audit log for this action with reason 'User prepared a suggested vegan dinner'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Williams-Brown Family"}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Black Beans"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 204, "ingredient_id": 1051}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 204, "days_ago": 7}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Vegan Black Bean Burgers"}),
            Action(name="add_meal_history", kwargs={"household_id": 204, "recipe_id": 432, "plan_date": "2025-08-21", "was_prepared": True, "rating_int": 4}),
            Action(name="add_audit_log", kwargs={"household_id": 204, "user_id": 104, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User prepared a suggested vegan dinner"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="066",
        instruction=(
            "You are assisting the Thompson Retirement household. "
            "They have cod fillets and want a dinner idea for tonight, August 22, 2025. "
            "They did not make this in the last 14 days. "
            "Find the 'Baked Cod with Herbs' recipe, confirm it's a good fit, "
            "and log it to their meal history as 'prepared' with a 5-star rating. "
            "Add an audit log for this action with reason 'User cooked a recommended heart-healthy meal'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Thompson Retirement"}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Cod Fillet"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 210, "ingredient_id": 1049}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 210, "days_ago": 14}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Baked Cod with Herbs"}),
            Action(name="add_meal_history", kwargs={"household_id": 210, "recipe_id": 425, "plan_date": "2025-08-22", "was_prepared": True, "rating_int": 5}),
            Action(name="add_audit_log", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User cooked a recommended heart-healthy meal"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="067",
        instruction=(
            "You are a recipe assistant for the Mercer Family. "
            "They have chicken breast and want a new dinner idea for tonight, August 25, 2025. "
            "They have not eaten this meal in the last week. "
            "Find the 'Thai Chicken Stir-Fry' recipe, confirm it's suitable, "
            "and then log it to their meal history as 'prepared' with a 4-star rating. "
            "Also, add an audit log for this action with the reason 'User tried a new stir-fry recipe'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Mercer Family"}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Chicken Breast"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 201, "ingredient_id": 1001}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 201, "days_ago": 7}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Thai Chicken Stir-Fry"}),
            Action(name="add_meal_history", kwargs={"household_id": 201, "recipe_id": 407, "plan_date": "2025-08-25", "was_prepared": True, "rating_int": 4}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User tried a new stir-fry recipe"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="068",
        instruction=(
            "You are assisting the Alvarez Household. "
            "They have chickpeas in their pantry and want a vegetarian meal for tonight, August 26, 2025. "
            "They did not make this meal last week. "
            "Find the 'Chickpea Curry' recipe, confirm it meets the criteria, "
            "and log it to their meal history as 'prepared' with a 3-star rating. "
            "Add an audit log with reason 'User cooked a vegetarian meal, rating provided'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Alvarez Household"}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Chickpeas"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 202, "ingredient_id": 1004}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 202, "days_ago": 7}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Chickpea Curry"}),
            Action(name="add_meal_history", kwargs={"household_id": 202, "recipe_id": 403, "plan_date": "2025-08-26", "was_prepared": True, "rating_int": 3}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User cooked a vegetarian meal, rating provided"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="069",
        instruction=(
            "You are assisting Sarah Chen. "
            "She has quinoa in her pantry and wants a light dinner for tonight, August 27, 2025. "
            "She has not made this in the last 2 weeks. "
            "Find the 'Mediterranean Quinoa Salad' recipe, confirm it's suitable, "
            "and then log it to her meal history as 'prepared' with a 5-star rating. "
            "Add an audit log with reason 'User logged preparation of a favorite salad'."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Sarah Chen'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Quinoa"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 203, "ingredient_id": 1007}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 203, "days_ago": 14}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Mediterranean Quinoa Salad"}),
            Action(name="add_meal_history", kwargs={"household_id": 203, "recipe_id": 406, "plan_date": "2025-08-27", "was_prepared": True, "rating_int": 5}),
            Action(name="add_audit_log", kwargs={"household_id": 203, "user_id": 103, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User logged preparation of a favorite salad"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="070",
        instruction=(
            "You are assisting the Garcia Household. "
            "They have black beans in stock and want a dinner idea for tonight, August 21, 2025. "
            "They haven't had this meal in the last week. "
            "Find the 'Vegetarian Chili' recipe, confirm it's a good fit, "
            "and log it to their meal history as 'prepared' with a 5-star rating. "
            "Add an audit log for this action with reason 'User cooked a hearty chili'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Garcia Household"}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Black Beans"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 208, "ingredient_id": 1051}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 208, "days_ago": 7}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Vegetarian Chili"}),
            Action(name="add_meal_history", kwargs={"household_id": 208, "recipe_id": 424, "plan_date": "2025-08-21", "was_prepared": True, "rating_int": 5}),
            Action(name="add_audit_log", kwargs={"household_id": 208, "user_id": 108, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User cooked a hearty chili"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="071",
        instruction=(
            "You are a recipe assistant for the Johnson Large Family. "
            "They have ground beef and want a quick dinner for tonight, August 22, 2025. "
            "They did not eat this meal last week. "
            "Find the 'Korean Beef Bowl' recipe, confirm it's suitable, "
            "and then log it to their meal history as 'prepared' with a 4-star rating. "
            "Also, add an audit log for this action with the reason 'User cooked a quick weeknight meal'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Johnson Large Family"}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Ground Beef"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 207, "ingredient_id": 1045}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 207, "days_ago": 7}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Korean Beef Bowl"}),
            Action(name="add_meal_history", kwargs={"household_id": 207, "recipe_id": 427, "plan_date": "2025-08-22", "was_prepared": True, "rating_int": 4}),
            Action(name="add_audit_log", kwargs={"household_id": 207, "user_id": 107, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User cooked a quick weeknight meal"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="072",
        instruction=(
            "You are assisting the Kowalski Couple. "
            "They have zucchini and ground beef and want a low-carb dinner for tonight, August 25, 2025. "
            "They haven't made this in the last 4 days. "
            "Find the 'Keto Zucchini Lasagna' recipe, confirm it's a fit, "
            "and log it to their meal history as 'prepared' with a 5-star rating. "
            "Add an audit log for this action with reason 'User prepared a suggested low-carb dinner'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Kowalski Couple"}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Zucchini"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 206, "ingredient_id": 1073}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 206, "days_ago": 4}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Keto Zucchini Lasagna"}),
            Action(name="add_meal_history", kwargs={"household_id": 206, "recipe_id": 434, "plan_date": "2025-08-25", "was_prepared": True, "rating_int": 5}),
            Action(name="add_audit_log", kwargs={"household_id": 206, "user_id": 106, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User prepared a suggested low-carb dinner"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="073",
        instruction=(
            "You are a recipe assistant for the Thompson Retirement household. "
            "They have chicken thighs and want a comforting dinner for tonight, August 23, 2025. "
            "They did not make this meal last week. "
            "Find the 'Moroccan Tagine' recipe, confirm it's a good choice, "
            "and log it to their meal history as 'prepared' with a 4-star rating. "
            "Add an audit log with reason 'User logged a flavorful dinner'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Thompson Retirement"}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Chicken Thighs"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 210, "ingredient_id": 1047}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 210, "days_ago": 7}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Moroccan Tagine"}),
            Action(name="add_meal_history", kwargs={"household_id": 210, "recipe_id": 429, "plan_date": "2025-08-23", "was_prepared": True, "rating_int": 4}),
            Action(name="add_audit_log", kwargs={"household_id": 210, "user_id": 110, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User logged a flavorful dinner"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="074",
        instruction=(
            "You are assisting the Kim-Smith Family. "
            "They have quinoa and want a healthy breakfast idea for tomorrow, August 21, 2025. "
            "They have not eaten this meal in the last 2 weeks. "
            "Find the 'Quinoa Breakfast Bowl' recipe, confirm it's suitable, "
            "and then log it to their meal history as 'prepared' with a 5-star rating. "
            "Also, add an audit log with reason 'User planned a new breakfast'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Kim-Smith Family"}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Quinoa"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 209, "ingredient_id": 1007}),
            Action(name="get_meal_history_for_household", kwargs={"household_id": 209, "days_ago": 14}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Quinoa Breakfast Bowl"}),
            Action(name="add_meal_history", kwargs={"household_id": 209, "recipe_id": 436, "plan_date": "2025-08-21", "was_prepared": True, "rating_int": 5}),
            Action(name="add_audit_log", kwargs={"household_id": 209, "user_id": 109, "entity_type": "meal_history", "entity_id": 6301, "action_enum": "create", "payload_json": {"reason": "User planned a new breakfast"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="075",
        instruction=(
            "You are assisting the Mercer Family. They are making 'Chicken Tacos' but have run out of 'Cheddar Cheese'. "
            "Find a suitable cheese alternative. "
            "Add 200g of 'Mozzarella Cheese' to their grocery list for this recipe. "
            "Log this decision to substitute ingredients in the audit trail for future reference with the reason 'Out of stock, cheese substitution'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Mercer Family"}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Chicken Tacos"}),
            Action(name="get_recipe_ingredients", kwargs={"recipe_id": 402}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Cheddar Cheese"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 201, "ingredient_id": 1024}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Mozzarella Cheese"}),
            Action(name="get_grocery_lists_by_household_id", kwargs={"household_id": 201}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8001, "ingredient_id": 1025, "quantity": 200, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "grocery_list_items", "entity_id": 8114, "action_enum": "create", "payload_json": {"reason": "Out of stock, cheese substitution"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="076",
        instruction=(
            "You are assisting the Williams-Brown Family, who needs gluten-free options. "
            "They plan to make 'Gluten-Free Pancakes' but are out of 'Gluten-Free Flour'. "
            "Find another suitable flour. "
            "They need a new meal plan for the week starting '2025-09-01' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "Add 500g of 'Almond Flour' to their grocery list. "
            "Log this substitution, noting 'Out of stock, gluten-free flour alternative'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Williams-Brown Family"}),
            Action(name="get_members_by_household_id", kwargs={"household_id": 204}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Gluten-Free Pancakes"}),
            Action(name="get_recipe_ingredients", kwargs={"recipe_id": 440}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Gluten-Free Flour"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 204, "ingredient_id": 1119}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Almond Flour"}),
            Action(name="get_grocery_lists_by_household_id", kwargs={"household_id": 204}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2025-09-01", "created_by_user_id": 104}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 204, "meal_plan_id": 6003, "user_id": 104}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1120, "quantity": 500, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 204, "user_id": 104, "entity_type": "grocery_list_items", "entity_id": 8114, "action_enum": "create", "payload_json": {"reason": "Out of stock, gluten-free flour alternative"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="077",
        instruction=(
            "You are assisting the Johnson Large Family, who has a shellfish allergy. "
            "They want to make 'Beef Stir-Fry' but have no 'Ground Beef' in stock. "
            "Find a suitable, non-shellfish protein substitute. "
            "They need a new meal plan for the week starting '2025-09-01' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "Add 600g of 'Chicken Thighs' to their grocery list. "
            "Log this substitution with reason 'Out of beef, protein swap'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Johnson Large Family"}),
            Action(name="get_members_by_household_id", kwargs={"household_id": 207}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Beef Stir-Fry"}),
            Action(name="get_recipe_ingredients", kwargs={"recipe_id": 423}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Ground Beef"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 207, "ingredient_id": 1045}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Chicken Thighs"}),
            Action(name="get_grocery_lists_by_household_id", kwargs={"household_id": 207}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2025-09-01", "created_by_user_id": 107}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 207, "meal_plan_id": 6003, "user_id": 107}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1047, "quantity": 600, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 207, "user_id": 107, "entity_type": "grocery_list_items", "entity_id": 8114, "action_enum": "create", "payload_json": {"reason": "Out of beef, protein swap"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="078",
        instruction=(
            "You are assisting the Patel Extended Family, who are vegetarian. "
            "They are making 'Dairy-Free Coconut Curry' but lack 'Firm Tofu'. "
            "Find another vegetarian protein source for the curry. "
            "They need a new meal plan for the week starting '2025-09-01' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "Add a 400g can of 'Canned Chickpeas' to their grocery list. "
            "Log this substitution as 'Tofu out of stock, using chickpeas'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Patel Extended Family"}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Dairy-Free Coconut Curry"}),
            Action(name="get_recipe_ingredients", kwargs={"recipe_id": 433}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Firm Tofu"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 205, "ingredient_id": 1003}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Canned Chickpeas"}),
            Action(name="get_grocery_lists_by_household_id", kwargs={"household_id": 205}),
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2025-09-01", "created_by_user_id": 105}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 205, "meal_plan_id": 6003, "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1004, "quantity": 400, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 205, "user_id": 105, "entity_type": "grocery_list_items", "entity_id": 8114, "action_enum": "create", "payload_json": {"reason": "Tofu out of stock, using chickpeas"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="079",
        instruction=(
            "You are assisting the Thompson Retirement household. "
            "They are making 'Heart-Healthy Baked Salmon' but have no fresh 'Salmon Fillet'. "
            "Find another healthy fish option. "
            "They need a new meal plan for the week starting '2025-09-01' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "Add 500g of 'Cod Fillet' to their grocery list. "
            "Log this as a 'Substitution due to salmon availability'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Thompson Retirement"}),
            Action(name="get_members_by_household_id", kwargs={"household_id": 210}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Heart-Healthy Baked Salmon"}),
            Action(name="get_recipe_ingredients", kwargs={"recipe_id": 435}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Salmon Fillet"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 210, "ingredient_id": 1002}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Cod Fillet"}),
            Action(name="get_grocery_lists_by_household_id", kwargs={"household_id": 210}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2025-09-01", "created_by_user_id": 110}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 210, "meal_plan_id": 6003, "user_id": 110}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1049, "quantity": 500, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 210, "user_id": 110, "entity_type": "grocery_list_items", "entity_id": 8114, "action_enum": "create", "payload_json": {"reason": "Substitution due to salmon availability"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="083",
        instruction=(
            "You are assisting Sarah Chen. She wants to make 'Teriyaki Tofu Bowl' but is out of 'White Rice'. "
            "Find a substitute grain. "
            "They need a new meal plan for the week starting '2025-09-05' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "Add 300g of 'Quinoa' to her grocery list. "
            "Log this as 'Rice out of stock, substituting with quinoa'."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Sarah Chen'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Teriyaki Tofu Bowl"}),
            Action(name="get_recipe_ingredients", kwargs={"recipe_id": 405}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "White Rice"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 203, "ingredient_id": 1006}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Quinoa"}),
            Action(name="get_grocery_lists_by_household_id", kwargs={"household_id": 203}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-05", "created_by_user_id": 103}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 203, "meal_plan_id": 6003, "user_id": 103}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1007, "quantity": 300, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 203, "user_id": 103, "entity_type": "grocery_list_items", "entity_id": 8114, "action_enum": "create", "payload_json": {"reason": "Rice out of stock, substituting with quinoa"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="084",
        instruction=(
            "You are assisting the Garcia Household. They are making 'Chicken Tacos' but have no 'Romaine Lettuce'. "
            "Find a leafy green substitute. "
            "They need a new meal plan for the week starting '2025-09-05' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "Add 200g of 'Spinach' to their grocery list. "
            "Log this substitution as 'Lettuce unavailable, using spinach'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Garcia Household"}),
            Action(name="get_members_by_household_id", kwargs={"household_id": 208}),
            Action(name="search_recipes_by_title_substring", kwargs={"title_substring": "Chicken Tacos"}),
            Action(name="get_recipe_ingredients", kwargs={"recipe_id": 402}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Romaine Lettuce"}),
            Action(name="get_inventory_for_household_and_ingredient_id", kwargs={"household_id": 208, "ingredient_id": 1013}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Spinach"}),
            Action(name="get_grocery_lists_by_household_id", kwargs={"household_id": 208}),
            Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2025-09-05", "created_by_user_id": 108}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 208, "meal_plan_id": 6003, "user_id": 108}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1070, "quantity": 200, "unit": "g"}),
            Action(name="add_audit_log", kwargs={"household_id": 208, "user_id": 108, "entity_type": "grocery_list_items", "entity_id": 8114, "action_enum": "create", "payload_json": {"reason": "Lettuce unavailable, using spinach"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="085",
        instruction=(
            "You are creating a grocery order for the Mercer Family. "
            "They need a new meal plan for the week starting '2025-09-08' and a corresponding grocery list. "
            "Create the meal plan, then the list. "
            "Finally, create an order from this list at 'FreshMart Online'. "
            "The subtotal is 4200 cents and the total is 4550 cents. "
            "Log the order placement in the audit logs."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Mercer Family'}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2025-09-08", "created_by_user_id": 101}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 201, "meal_plan_id": 6003, "user_id": 101}),
            Action(name="search_stores_by_name", kwargs={"name_query": 'FreshMart Online'}),
            Action(name="create_order_from_grocery_list", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "subtotal_cents": 4200, "total_cents": 4550}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="086",
        instruction=(
            "You are creating a grocery order for the Alvarez Household. "
            "They need a new meal plan for the week starting '2025-09-08' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "Create an order from this list at 'GrocerDash'. "
            "The subtotal is 1800 cents and the total is 2000 cents. "
            "Log the order placement in the audit logs."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Alvarez Household'}),
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2025-09-08", "created_by_user_id": 102}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 202, "meal_plan_id": 6003, "user_id": 102}),
            Action(name="search_stores_by_name", kwargs={"name_query": 'GrocerDash'}),
            Action(name="create_order_from_grocery_list", kwargs={"household_id": 202, "store_id": 9002, "list_id": 8003, "subtotal_cents": 1800, "total_cents": 2000}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="087",
        instruction=(
            "You are creating a grocery order for Sarah Chen. "
            "She needs a new meal plan for the week starting '2025-09-15' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "Create an order from this list at 'Organic Valley Co-op'. "
            "The subtotal is 5500 cents and the total is 5950 cents. "
            "Log the order placement in the audit logs."
        ),
        actions=[
            Action(name="search_users_by_name", kwargs={"name_query": 'Sarah Chen'}),
            Action(name="get_household_by_user_id", kwargs={"user_id": 103}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-15", "created_by_user_id": 103}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 203, "meal_plan_id": 6003, "user_id": 103}),
            Action(name="search_stores_by_name", kwargs={"name_query": 'Organic Valley Co-op'}),
            Action(name="create_order_from_grocery_list", kwargs={"household_id": 203, "store_id": 9003, "list_id": 8003, "subtotal_cents": 5500, "total_cents": 5950}),
            Action(name="add_audit_log", kwargs={"household_id": 203, "user_id": 103, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="088",
        instruction=(
            "You are creating a grocery order for the Williams-Brown Family. "
            "They need a new meal plan for the week starting '2025-09-15' and a grocery list. "
            "Create a new grocery list linked to this new meal plan. "
            "Create an order from this list at 'Health First Market'. "
            "The subtotal is 6200 cents and the total is 6650 cents. "
            "Log the order placement in the audit logs."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Williams-Brown Family'}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2025-09-15", "created_by_user_id": 104}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 204, "meal_plan_id": 6003, "user_id": 104}),
            Action(name="search_stores_by_name", kwargs={"name_query": 'Health First Market'}),
            Action(name="create_order_from_grocery_list", kwargs={"household_id": 204, "store_id": 9006, "list_id": 8003, "subtotal_cents": 6200, "total_cents": 6650}),
            Action(name="add_audit_log", kwargs={"household_id": 204, "user_id": 104, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="089",
        instruction=(
            "You are creating a grocery order for the Kowalski Couple. "
            "They need a meal plan for the week starting '2025-09-22'. "
            "Create a new grocery list linked to the new plan. "
            "Create an order from this list at 'Budget Foods Express'. "
            "The subtotal is 2800 cents and the total is 3100 cents. "
            "Log the order placement."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Kowalski Couple'}),
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2025-09-22", "created_by_user_id": 106}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 206, "meal_plan_id": 6003, "user_id": 106}),
            Action(name="search_stores_by_name", kwargs={"name_query": 'Budget Foods Express'}),
            Action(name="create_order_from_grocery_list", kwargs={"household_id": 206, "store_id": 9004, "list_id": 8003, "subtotal_cents": 2800, "total_cents": 3100}),
            Action(name="add_audit_log", kwargs={"household_id": 206, "user_id": 106, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="090",
        instruction=(
            "You are creating a grocery order for the Johnson Large Family. "
            "They need a new meal plan for the week starting '2025-09-22'. "
            "Create a new grocery list for them. "
            "Create an order from this list using 'Farm Fresh Delivery'. "
            "The subtotal is 9500 cents and the total is 10150 cents. "
            "Log the order placement."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Johnson Large Family'}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2025-09-22", "created_by_user_id": 107}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 207, "meal_plan_id": 6003, "user_id": 107}),
            Action(name="search_stores_by_name", kwargs={"name_query": 'Farm Fresh Delivery'}),
            Action(name="create_order_from_grocery_list", kwargs={"household_id": 207, "store_id": 9007, "list_id": 8003, "subtotal_cents": 9500, "total_cents": 10150}),
            Action(name="add_audit_log", kwargs={"household_id": 207, "user_id": 107, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="091",
        instruction=(
            "You are creating a grocery order for the Garcia Household. "
            "They need a meal plan for the week starting '2025-09-29'. "
            "Create a new grocery list from that plan. "
            "Create an order from this list at 'QuickShop Express'. "
            "The subtotal is 4800 cents and the total is 5200 cents. "
            "Log the order placement."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Garcia Household'}),
            Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2025-09-29", "created_by_user_id": 108}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 208, "meal_plan_id": 6003, "user_id": 108}),
            Action(name="search_stores_by_name", kwargs={"name_query": 'QuickShop Express'}),
            Action(name="create_order_from_grocery_list", kwargs={"household_id": 208, "store_id": 9008, "list_id": 8003, "subtotal_cents": 4800, "total_cents": 5200}),
            Action(name="add_audit_log", kwargs={"household_id": 208, "user_id": 108, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="092",
        instruction=(
            "You are creating a grocery order for the Kim-Smith Family. "
            "They need a meal plan for the week starting '2025-09-29'. "
            "Create a grocery list from the plan. "
            "Create an order from this list at 'FreshMart Online'. "
            "The subtotal is 5100 cents and the total is 5500 cents. "
            "Log the order."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Kim-Smith Family'}),
            Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2025-09-29", "created_by_user_id": 109}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 209, "meal_plan_id": 6003, "user_id": 109}),
            Action(name="search_stores_by_name", kwargs={"name_query": 'FreshMart Online'}),
            Action(name="create_order_from_grocery_list", kwargs={"household_id": 209, "store_id": 9001, "list_id": 8003, "subtotal_cents": 5100, "total_cents": 5500}),
            Action(name="add_audit_log", kwargs={"household_id": 209, "user_id": 109, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="093",
        instruction=(
            "You are creating a grocery order for the Thompson Retirement household. "
            "They need a new meal plan for the week starting '2025-10-06'. "
            "Create a new grocery list from the new plan. "
            "Create an order from this list at 'GrocerDash'. "
            "The subtotal is 3200 cents and the total is 3500 cents. "
            "Log the order placement."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Thompson Retirement'}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2025-10-06", "created_by_user_id": 110}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 210, "meal_plan_id": 6003, "user_id": 110}),
            Action(name="search_stores_by_name", kwargs={"name_query": 'GrocerDash'}),
            Action(name="create_order_from_grocery_list", kwargs={"household_id": 210, "store_id": 9002, "list_id": 8003, "subtotal_cents": 3200, "total_cents": 3500}),
            Action(name="add_audit_log", kwargs={"household_id": 210, "user_id": 110, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="094",
        instruction=(
            "You are creating another grocery order for the Patel Extended Family. "
            "They need a plan for the week of '2025-10-06'. "
            "Create a grocery list from that plan. "
            "Then, create an order at 'Organic Valley Co-op'. "
            "The subtotal is 7500 cents and the total is 8100 cents. "
            "Log the placement of the order."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": 'Patel Extended Family'}),
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2025-10-06", "created_by_user_id": 105}),
            Action(name="create_grocery_list_from_meal_plan", kwargs={"household_id": 205, "meal_plan_id": 6003, "user_id": 105}),
            Action(name="search_stores_by_name", kwargs={"name_query": 'Organic Valley Co-op'}),
            Action(name="create_order_from_grocery_list", kwargs={"household_id": 205, "store_id": 9003, "list_id": 8003, "subtotal_cents": 7500, "total_cents": 8100}),
            Action(name="add_audit_log", kwargs={"household_id": 205, "user_id": 105, "entity_type": "orders", "entity_id": 10003, "action_enum": "place_order"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="095",
        instruction=(
            "You are a meal plan manager for the Alvarez Household. "
            "Find their meal plan for the week of August 25th. "
            "Locate the entry with the note 'Blend half for smoother texture'. "
            "Update the notes for this specific entry (ID 6111) to say 'Blend half for smoother texture and add a dollop of yogurt before serving'. "
            "Log this note modification in the audit trail with the reason 'User added a serving suggestion'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Alvarez Household"}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, "start_date": "2025-08-25", "end_date": "2025-08-31", "notes_substring": "Blend half"}),
            Action(name="update_meal_plan_entry_notes", kwargs={"entry_id": 6111, "new_notes": "Blend half for smoother texture and add a dollop of yogurt before serving"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6111, "action_enum": "update", "payload_json": {"field": "notes", "reason": "User added a serving suggestion"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="096",
        instruction=(
            "You are a meal plan manager for the Mercer Family. "
            "Find their meal plan for the week of August 25th. "
            "Locate the entry with the note 'Reduce chili powder for child'. "
            "Update the notes for this entry to say 'Reduce chili powder for child and serve with a side of mild salsa'. "
            "Log this modification with the reason 'User added a side dish suggestion'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Mercer Family"}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, "start_date": "2025-08-25", "end_date": "2025-08-31", "notes_substring": "Reduce chili powder"}),
            Action(name="update_meal_plan_entry_notes", kwargs={"entry_id": 6101, "new_notes": "Reduce chili powder for child and serve with a side of mild salsa"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6101, "action_enum": "update", "payload_json": {"field": "notes", "reason": "User added a side dish suggestion"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="097",
        instruction=(
            "You are a meal plan manager for the Alvarez Household. "
            "Find their meal plan for the week of August 25th. "
            "Locate the entry with the note 'Peanut-free confirmed'. "
            "Update the notes for this entry to say 'Peanut-free confirmed. Serve with avocado slices.'. "
            "Log this modification with the reason 'User requested a serving addition'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Alvarez Household"}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, "start_date": "2025-08-25", "end_date": "2025-08-31", "notes_substring": "Peanut-free confirmed"}),
            Action(name="update_meal_plan_entry_notes", kwargs={"entry_id": 6113, "new_notes": "Peanut-free confirmed. Serve with avocado slices."}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6113, "action_enum": "update", "payload_json": {"field": "notes", "reason": "User requested a serving addition"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="098",
        instruction=(
            "You are a meal plan manager for the Mercer Family. "
            "Find their meal plan for the week of August 25th. "
            "Locate the entry with the note 'Flake salmon'. "
            "Update the notes for this entry to say 'Flake salmon carefully to remove all bones for Maya'. "
            "Log this clarification with the reason 'User added specific instruction for child'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Mercer Family"}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, "start_date": "2025-08-25", "end_date": "2025-08-31", "notes_substring": "Flake salmon"}),
            Action(name="update_meal_plan_entry_notes", kwargs={"entry_id": 6103, "new_notes": "Flake salmon carefully to remove all bones for Maya"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6103, "action_enum": "update", "payload_json": {"field": "notes", "reason": "User added specific instruction for child"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="099",
        instruction=(
            "You are a meal plan manager for the Alvarez Household. "
            "Find their meal plan for the week of August 25th. "
            "Locate the entry with the note 'Flake salmon'. "
            "Update the notes for this entry to say 'Flake salmon and serve with a lemon wedge for the adults'. "
            "Log this update with the reason 'User added a serving note'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Alvarez Household"}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, "start_date": "2025-08-25", "end_date": "2025-08-31", "notes_substring": "Flake salmon"}),
            Action(name="update_meal_plan_entry_notes", kwargs={"entry_id": 6114, "new_notes": "Flake salmon and serve with a lemon wedge for the adults"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6114, "action_enum": "update", "payload_json": {"field": "notes", "reason": "User added a serving note"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="100",
        instruction=(
            "You are a meal plan manager for the Mercer Family. "
            "Find their meal plan for the week of August 25th. "
            "Locate the entry with the note 'Mild curry'. "
            "Update the notes for this entry to say 'Mild curry, and serve with rice instead of naan'. "
            "Log this change with the reason 'User specified a side dish'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Mercer Family"}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, "start_date": "2025-08-25", "end_date": "2025-08-31", "notes_substring": "Mild curry"}),
            Action(name="update_meal_plan_entry_notes", kwargs={"entry_id": 6104, "new_notes": "Mild curry, and serve with rice instead of naan"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6104, "action_enum": "update", "payload_json": {"field": "notes", "reason": "User specified a side dish"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="101",
        instruction=(
            "You are a meal plan manager for the Alvarez Household. "
            "Find their meal plan for the week of August 25th. "
            "Locate the entry with the note 'Tofu well-cooked'. "
            "Update the notes for this entry to say 'Tofu well-cooked and garnish with sesame seeds'. "
            "Log this change with the reason 'User added garnish instruction'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Alvarez Household"}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, "start_date": "2025-08-25", "end_date": "2025-08-31", "notes_substring": "Tofu well-cooked"}),
            Action(name="update_meal_plan_entry_notes", kwargs={"entry_id": 6115, "new_notes": "Tofu well-cooked and garnish with sesame seeds"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6115, "action_enum": "update", "payload_json": {"field": "notes", "reason": "User added garnish instruction"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="102",
        instruction=(
            "You are a meal plan manager for the Mercer Family. "
            "Find their meal plan for the week of August 25th. "
            "Locate the entry with the note 'Less lemon for child'. "
            "Update the notes for this entry to say 'Less lemon for child, and add some crumbled feta'. "
            "Log this change with the reason 'User added an ingredient'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Mercer Family"}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, "start_date": "2025-08-25", "end_date": "2025-08-31", "notes_substring": "Less lemon"}),
            Action(name="update_meal_plan_entry_notes", kwargs={"entry_id": 6106, "new_notes": "Less lemon for child, and add some crumbled feta"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6106, "action_enum": "update", "payload_json": {"field": "notes", "reason": "User added an ingredient"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="103",
        instruction=(
            "You are a meal plan manager for the Alvarez Household. "
            "Find their meal plan for the week of August 25th. "
            "Locate the entry with the note 'Add cheese for child'. "
            "Update the notes for this entry to say 'Add cheese for child and also some chopped cucumbers'. "
            "Log this change with the reason 'User added another ingredient for child'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Alvarez Household"}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, "start_date": "2025-08-25", "end_date": "2025-08-31", "notes_substring": "Add cheese"}),
            Action(name="update_meal_plan_entry_notes", kwargs={"entry_id": 6116, "new_notes": "Add cheese for child and also some chopped cucumbers"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6116, "action_enum": "update", "payload_json": {"field": "notes", "reason": "User added another ingredient for child"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="104",
        instruction=(
            "You are a meal plan manager for the Mercer Family. "
            "Find their meal plan for the week of August 25th. "
            "Locate the entry with the note 'Reduce spice'. "
            "Update the notes for this entry to say 'Reduce spice and add more bell peppers'. "
            "Log this update with the reason 'User requested vegetable addition'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Mercer Family"}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 201}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6001, "start_date": "2025-08-25", "end_date": "2025-08-31", "notes_substring": "Reduce spice"}),
            Action(name="update_meal_plan_entry_notes", kwargs={"entry_id": 6107, "new_notes": "Reduce spice and add more bell peppers"}),
            Action(name="add_audit_log", kwargs={"household_id": 201, "user_id": 101, "entity_type": "meal_plan_entries", "entity_id": 6107, "action_enum": "update", "payload_json": {"field": "notes", "reason": "User requested vegetable addition"}}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="105",
        instruction=(
            "You are a meal plan manager for the Alvarez Household. "
            "Find their meal plan for the week of August 25th. "
            "Locate the entry with the note 'Low spice'. "
            "Update the notes for this entry to say 'Low spice and add a lime wedge for serving'. "
            "Log this modification with the reason 'User added a garnish idea'."
        ),
        actions=[
            Action(name="search_households_by_name", kwargs={"name_query": "Alvarez Household"}),
            Action(name="get_meal_plans_by_household_id", kwargs={"household_id": 202}),
            Action(name="search_meal_plan_entries", kwargs={"meal_plan_id": 6002, "start_date": "2025-08-25", "end_date": "2025-08-31", "notes_substring": "Low spice"}),
            Action(name="update_meal_plan_entry_notes", kwargs={"entry_id": 6117, "new_notes": "Low spice and add a lime wedge for serving"}),
            Action(name="add_audit_log", kwargs={"household_id": 202, "user_id": 102, "entity_type": "meal_plan_entries", "entity_id": 6117, "action_enum": "update", "payload_json": {"field": "notes", "reason": "User added a garnish idea"}}),
        ],
        outputs=[]
    ),
]
