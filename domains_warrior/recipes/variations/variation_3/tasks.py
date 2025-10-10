from domains.dto import Action, Task

TASKS = [
    # Task 001: Simple meal history entry
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_001",
        instruction=(
            "You are Aiden Mercer from the Mercer Family. On 2025-09-01, you made 'Teriyaki Tofu Bowl' "
            "for dinner and it turned out great. Before logging, you want to verify you had the key ingredients: "
            "Firm Tofu, Teriyaki Sauce, and White Rice in your pantry. Then you want to log this to your meal history as prepared "
            "with a 5-star rating, and add an audit log with reason 'User reported preparation with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Teriyaki Tofu Bowl"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Firm Tofu"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1003},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Teriyaki Sauce"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1021},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "White Rice"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1006},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-09-01",
                    "recipe_id": 405,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-09-01",
                    "recipe_id": 405,
                    "reason": "User reported preparation with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 002: Simple with history check
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_002",
        instruction=(
            "You are Lina Alvarez from the Alvarez Household. On 2025-09-01, you want to make "
            "'Moroccan Tagine' for dinner. You haven't made this recipe in the last week, "
            "so you want to log it to your meal history as prepared with a 4-star rating, and add an audit log with reason 'user_selection'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Lina Alvarez"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 102}),
            Action(
                name="get_meal_history_for_household", kwargs={"household_id": 202, "days_ago": 7}
            ),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Moroccan Tagine"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 202,
                    "plan_date": "2025-09-01",
                    "recipe_id": 429,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 202,
                    "user_id": 102,
                    "plan_date": "2025-09-01",
                    "recipe_id": 429,
                    "reason": "user_selection",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 003: Simple dessert
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_003",
        instruction=(
            "You are Sarah Chen. On 2025-09-01, you made 'Fruit Sorbet' for dessert "
            "because you were low on eggs. You want to log this to your meal history as prepared "
            "with a 4-star rating, and add an audit log with reason 'Switched to egg-free dessert'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Fruit Sorbet"}
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 203,
                    "plan_date": "2025-09-01",
                    "recipe_id": 452,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 203,
                    "user_id": 103,
                    "plan_date": "2025-09-01",
                    "recipe_id": 452,
                    "reason": "Switched to egg-free dessert",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 004: Simple curry dinner
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_004",
        instruction=(
            "You are Aiden Mercer. On 2025-09-02, you made 'Chickpea Curry' for dinner. "
            "Before logging, you want to verify you have the main ingredients: Canned Chickpeas, Yellow Onion, and Garlic. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged meal with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Chickpea Curry"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Canned Chickpeas"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1004},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Yellow Onion"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1010},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Garlic"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1011},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-09-02",
                    "recipe_id": 403,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-09-02",
                    "recipe_id": 403,
                    "reason": "Logged meal with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 005: Already passing - keep as is
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_005",
        instruction=(
            "You are Lina Alvarez from the Alvarez Household. After preparing lunch on 2025-09-05, "
            "you used 80 grams of 'Turkey Deli Slices' from your pantry. You want to update the inventory "
            "to reflect this usage and log the consumption for your household records."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Lina Alvarez"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 102}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Turkey Deli Slices"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 202, "ingredient_id": 1039},
            ),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 202, "ingredient_id": 1039, "delta": -80},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 202, "user_id": 102, "ingredient_id": 1039, "delta": -80},
            ),
        ],
        outputs=[],
    ),
    # Task 006: Check history and log meal
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_006",
        instruction=(
            "You are Sarah Chen. You want to make 'Shrimp Pad Thai' for dinner on 2025-09-08. "
            "First check if you've made it in the last 7 days, then log it to your meal history as prepared."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(
                name="get_meal_history_for_household", kwargs={"household_id": 203, "days_ago": 7}
            ),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Pad Thai"}
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 203,
                    "plan_date": "2025-09-08",
                    "recipe_id": 430,
                    "was_prepared": True,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 203,
                    "user_id": 103,
                    "plan_date": "2025-09-08",
                    "recipe_id": 430,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 007: Simple inventory update
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_007",
        instruction=(
            "You are Marcus Williams from the Williams-Brown Family. You used 200 grams of 'Chicken Breast' "
            "on 2025-09-01. Update your inventory and log this consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Marcus Williams"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 104}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Chicken Breast"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 204, "ingredient_id": 1001, "delta": -200},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 204, "user_id": 104, "ingredient_id": 1001, "delta": -200},
            ),
        ],
        outputs=[],
    ),
    # Task 008: Recipe details check
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_008",
        instruction=(
            "You are Priya Patel. You want to make 'Gluten-Free Pasta Primavera' on 2025-09-01 and need to check "
            "the ingredients first, then log it to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Priya Patel"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 105}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Gluten-Free Pasta Primavera"},
            ),
            Action(name="get_recipe_details", kwargs={"recipe_id": 431}),
            Action(name="list_recipe_ingredients", kwargs={"recipe_id": 431}),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 205,
                    "plan_date": "2025-09-01",
                    "recipe_id": 431,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 205,
                    "user_id": 105,
                    "plan_date": "2025-09-01",
                    "recipe_id": 431,
                    "reason": "Prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 009: Simple breakfast log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_009",
        instruction=(
            "You are David Kowalski. On 2025-09-01, you made 'Avocado Toast' for breakfast. "
            "You want to log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged by user'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "David Kowalski"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 106}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Avocado Toast"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 206,
                    "plan_date": "2025-09-01",
                    "recipe_id": 420,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 206,
                    "user_id": 106,
                    "plan_date": "2025-09-01",
                    "recipe_id": 420,
                    "reason": "Logged by user",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 010: Lunch with rating
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_010",
        instruction=(
            "You are Emma Johnson from the Johnson Large Family. On 2025-09-01, you made "
            "'Turkey Sandwich' for lunch. Before logging, you want to verify you have the key ingredients: "
            "Whole Wheat Bread, Turkey Deli Slices, and Cheddar Cheese. Then you want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Emma Johnson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 107}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Turkey Sandwich"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Whole Wheat Bread"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 207, "ingredient_id": 1026},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Turkey Deli Slices"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 207, "ingredient_id": 1039},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Cheddar Cheese"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 207, "ingredient_id": 1024},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 207,
                    "plan_date": "2025-09-01",
                    "recipe_id": 409,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 207,
                    "user_id": 107,
                    "plan_date": "2025-09-01",
                    "recipe_id": 409,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 011: Simple lunch
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_011",
        instruction=(
            "You are Antonio Garcia. On 2025-09-02, you made 'Hummus Veggie Wrap' for lunch. "
            "Before logging, you want to verify you have the key ingredients: Hummus, Tortilla Wraps, and Cucumber. "
            "Then log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged prepared meal with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Antonio Garcia"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 108}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Hummus Veggie Wrap"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Hummus"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 208, "ingredient_id": 1038},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Tortilla Wraps"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 208, "ingredient_id": 1043},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Cucumber"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 208, "ingredient_id": 1014},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 208,
                    "plan_date": "2025-09-02",
                    "recipe_id": 410,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 208,
                    "user_id": 108,
                    "plan_date": "2025-09-02",
                    "recipe_id": 410,
                    "reason": "Logged prepared meal with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 012: Simple meal with inventory check
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_012",
        instruction=(
            "You are Rachel Kim. On 2025-09-01, you made 'Grilled Salmon' for dinner. "
            "Check your salmon inventory first, then you want to log the meal as prepared with a 5-star rating, and add an audit log with reason 'Logged meal as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Rachel Kim"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 109}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Salmon"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 209, "ingredient_id": 1002},
            ),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Grilled Salmon"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 209,
                    "plan_date": "2025-09-01",
                    "recipe_id": 404,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 209,
                    "user_id": 109,
                    "plan_date": "2025-09-01",
                    "recipe_id": 404,
                    "reason": "Logged meal as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 013: Consume inventory
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_013",
        instruction=(
            "You are James Thompson. You used 150 grams of 'Ground Beef' on 2025-09-01. "
            "You need to update your inventory and log the consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "James Thompson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 110}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Ground Beef"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 210, "ingredient_id": 1045, "delta": -150},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 210, "user_id": 110, "ingredient_id": 1045, "delta": -150},
            ),
        ],
        outputs=[],
    ),
    # Task 014: Meal with reason
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_014",
        instruction=(
            "You are Aiden Mercer. On 2025-09-08, you made 'Chicken Tacos' for dinner. "
            "You want to log this to your meal history as prepared, and add an audit log with reason 'Family favorite night'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Chicken Tacos"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-09-08",
                    "recipe_id": 402,
                    "was_prepared": True,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-09-08",
                    "recipe_id": 402,
                    "reason": "Family favorite night",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 015: Pizza night
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_015",
        instruction=(
            "You are Lina Alvarez. On 2025-09-08, you made 'Heart-Healthy Baked Salmon' for dinner. "
            "Before logging, you want to verify you have the key ingredients: Salmon Fillet, Lemon, and Broccoli. "
            "Then log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Lina Alvarez"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 102}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Heart-Healthy Baked Salmon"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Salmon Fillet"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 202, "ingredient_id": 1002},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Lemon"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 202, "ingredient_id": 1022},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Broccoli"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 202, "ingredient_id": 1066},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 202,
                    "plan_date": "2025-09-08",
                    "recipe_id": 435,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 202,
                    "user_id": 102,
                    "plan_date": "2025-09-08",
                    "recipe_id": 435,
                    "reason": "Logged with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 016: Stuffed peppers
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_016",
        instruction=(
            "You are Sarah Chen. On 2025-09-08, you made 'Stuffed Bell Peppers' for dinner and loved them. "
            "Before logging, you want to verify you have the key ingredients: Bell Pepper, Ground Beef, and White Rice. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'User reported preparing recipe with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Stuffed Bell Peppers"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Bell Pepper"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1009},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Ground Beef"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1045},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "White Rice"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1006},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 203,
                    "plan_date": "2025-09-08",
                    "recipe_id": 428,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 203,
                    "user_id": 103,
                    "plan_date": "2025-09-08",
                    "recipe_id": 428,
                    "reason": "User reported preparing recipe with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 017: Pasta with inventory
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_017",
        instruction=(
            "You are Marcus Williams. On 2025-09-08, you made 'Spaghetti with Tomato Sauce' for dinner. "
            "Check your pasta inventory, then you want to log the meal as prepared, and add an audit log with reason 'Prepared meal'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Marcus Williams"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 104}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Spaghetti"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 204, "ingredient_id": 1005},
            ),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Spaghetti"}
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 204,
                    "plan_date": "2025-09-08",
                    "recipe_id": 401,
                    "was_prepared": True,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 204,
                    "user_id": 104,
                    "plan_date": "2025-09-08",
                    "recipe_id": 401,
                    "reason": "Prepared meal",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 018: Stir fry
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_018",
        instruction=(
            "You are Priya Patel. On 2025-09-08, you made 'Beef Stir-Fry' for dinner. "
            "You want to log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged by user as prepared with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Priya Patel"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 105}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Beef Stir-Fry"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 205,
                    "plan_date": "2025-09-08",
                    "recipe_id": 423,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 205,
                    "user_id": 105,
                    "plan_date": "2025-09-08",
                    "recipe_id": 423,
                    "reason": "Logged by user as prepared with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 019: Quesadilla
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_019",
        instruction=(
            "You are David Kowalski. On 2025-09-08, you made 'Veggie Quesadilla' for lunch. "
            "Before logging, you want to verify you have the key ingredients: Tortilla Wraps, Bell Pepper, and Cheddar Cheese. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "David Kowalski"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 106}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Quesadilla"}
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Tortilla Wraps"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 206, "ingredient_id": 1043},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Bell Pepper"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 206, "ingredient_id": 1009},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Cheddar Cheese"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 206, "ingredient_id": 1024},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 206,
                    "plan_date": "2025-09-08",
                    "recipe_id": 444,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 206,
                    "user_id": 106,
                    "plan_date": "2025-09-08",
                    "recipe_id": 444,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 020: Consume pork
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_020",
        instruction=(
            "You are Emma Johnson. You used 250 grams of 'Pork Tenderloin' on 2025-09-08. "
            "You need to update your inventory and log the consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Emma Johnson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 107}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Pork Tenderloin"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 207, "ingredient_id": 1046, "delta": -250},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 207, "user_id": 107, "ingredient_id": 1046, "delta": -250},
            ),
        ],
        outputs=[],
    ),
    # Tasks 021-040 - ALL SIMPLE (max 8 actions each, variation_2 style)
    # Task 021: Simple breakfast log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_021",
        instruction=(
            "You are Aiden Mercer. On 2025-09-22, you made 'Avocado Toast' for breakfast. "
            "Before logging, you want to verify you have the key ingredients: Avocado, Whole Wheat Bread, and Salt. "
            "Then log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged breakfast preparation with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Avocado Toast"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Avocado"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1086},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Whole Wheat Bread"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1026},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Salt"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1016},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-09-22",
                    "recipe_id": 420,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-09-22",
                    "recipe_id": 420,
                    "reason": "Logged breakfast preparation with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 022: Dinner with history check and rating
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_022",
        instruction=(
            "You are Aiden Mercer. On 2025-09-12, you want to make 'Beef Stir-Fry' for dinner. "
            "Check if you've made it in the last 7 days, then log it as prepared with a 5-star rating, and add an audit log with reason 'Prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="get_meal_history_for_household", kwargs={"household_id": 201, "days_ago": 7}
            ),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Beef Stir-Fry"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-09-12",
                    "recipe_id": 423,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-09-12",
                    "recipe_id": 423,
                    "reason": "Prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 023: Simple dessert log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_023",
        instruction=(
            "You are Emma Johnson. On 2025-09-22, you made 'Vegan Chocolate Mousse' for dessert. "
            "Before logging, you want to verify you have the key ingredients: Tempeh, Cocoa Powder, and Agave Nectar. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged prepared dessert with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Emma Johnson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 107}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Chocolate Mousse"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Tempeh"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 207, "ingredient_id": 1054},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Cocoa Powder"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 207, "ingredient_id": 1036},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Agave Nectar"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 207, "ingredient_id": 1117},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 207,
                    "plan_date": "2025-09-22",
                    "recipe_id": 451,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 207,
                    "user_id": 107,
                    "plan_date": "2025-09-22",
                    "recipe_id": 451,
                    "reason": "Logged prepared dessert with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 024: Simple salad
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_024",
        instruction=(
            "You are Sarah Chen. On 2025-09-24, you made 'Mediterranean Quinoa Salad' for dinner. "
            "Before logging, you want to verify you have the key ingredients: Quinoa, Romaine Lettuce, and Cucumber. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'user_logged'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Mediterranean Quinoa Salad"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Quinoa"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1007},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Romaine Lettuce"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1013},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Cucumber"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1014},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 203,
                    "plan_date": "2025-09-24",
                    "recipe_id": 406,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 203,
                    "user_id": 103,
                    "plan_date": "2025-09-24",
                    "recipe_id": 406,
                    "reason": "user_logged",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 025: Simple inventory consumption
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_025",
        instruction=(
            "You are Aiden Mercer. On 2025-09-25, you used 100 grams of 'Pork Tenderloin' for dinner. "
            "You want to update your inventory and log the consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Pork Tenderloin"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 201, "ingredient_id": 1046, "delta": -100},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 201, "user_id": 101, "ingredient_id": 1046, "delta": -100},
            ),
        ],
        outputs=[],
    ),
    # Task 026: Simple lunch log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_026",
        instruction=(
            "You are Lina Alvarez. On 2025-09-29, you made 'Turkey Sandwich' for lunch. "
            "Before logging, you want to verify you have the key ingredients: Whole Wheat Bread, Turkey Deli Slices, and Cheddar Cheese. "
            "Then log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged by user as prepared with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Lina Alvarez"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 102}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Turkey Sandwich"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Whole Wheat Bread"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 202, "ingredient_id": 1026},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Turkey Deli Slices"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 202, "ingredient_id": 1039},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Cheddar Cheese"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 202, "ingredient_id": 1024},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 202,
                    "plan_date": "2025-09-29",
                    "recipe_id": 409,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 202,
                    "user_id": 102,
                    "plan_date": "2025-09-29",
                    "recipe_id": 409,
                    "reason": "Logged by user as prepared with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 027: Simple dinner log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_027",
        instruction=(
            "You are Sarah Chen. On 2025-09-29, you made 'Spaghetti with Tomato Sauce' for dinner. "
            "Before logging, you want to verify you have the key ingredients: Spaghetti Pasta, Tomato Sauce, and Yellow Onion. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Spaghetti"}
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Spaghetti Pasta"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1005},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Tomato Sauce"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1012},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Yellow Onion"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1010},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 203,
                    "plan_date": "2025-09-29",
                    "recipe_id": 401,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 203,
                    "user_id": 103,
                    "plan_date": "2025-09-29",
                    "recipe_id": 401,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 028: Simple tofu bowl
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_028",
        instruction=(
            "You are Sarah Chen. On 2025-10-01, you made 'Teriyaki Tofu Bowl' for dinner. "
            "Before logging, you want to verify you have the key ingredients: Firm Tofu, Teriyaki Sauce, and White Rice. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged prepared meal with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Teriyaki Tofu Bowl"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Firm Tofu"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1003},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Teriyaki Sauce"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1021},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "White Rice"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1006},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 203,
                    "plan_date": "2025-10-01",
                    "recipe_id": 405,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 203,
                    "user_id": 103,
                    "plan_date": "2025-10-01",
                    "recipe_id": 405,
                    "reason": "Logged prepared meal with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 029: Simple meal with peanut-free check
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_029",
        instruction=(
            "You are Aiden Mercer. On 2025-09-29, you want to make 'Gluten-Free Pasta Primavera' for dinner. "
            "Check the recipe details to ensure it's peanut-free, then log it as prepared."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Gluten-Free Pasta Primavera"},
            ),
            Action(name="get_recipe_details", kwargs={"recipe_id": 431}),
            Action(name="list_recipe_ingredients", kwargs={"recipe_id": 431}),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-09-29",
                    "recipe_id": 431,
                    "was_prepared": True,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-09-29",
                    "recipe_id": 431,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 030: Simple soup dinner
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_030",
        instruction=(
            "You are David Kowalski. On 2025-10-03, you made 'Lentil Soup' for dinner. "
            "Before logging, you want to verify you have the key ingredients: Yellow Onion, Garlic, and Salt. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged meal history for prepared recipe with rating.'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "David Kowalski"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 106}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Lentil Soup"}
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Yellow Onion"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 206, "ingredient_id": 1010},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Garlic"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 206, "ingredient_id": 1011},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Salt"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 206, "ingredient_id": 1016},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 206,
                    "plan_date": "2025-10-03",
                    "recipe_id": 408,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 206,
                    "user_id": 106,
                    "plan_date": "2025-10-03",
                    "recipe_id": 408,
                    "reason": "Logged meal history for prepared recipe with rating.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 031: Simple breakfast log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_031",
        instruction=(
            "You are Emma Johnson. On 2025-10-06, you made 'Overnight Oats with Berries' for breakfast. "
            "Before logging, you want to verify you have the key ingredients: Rolled Oats, Milk, and Plain Greek Yogurt. "
            "Then you want to log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged by user as prepared with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Emma Johnson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 107}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Overnight Oats"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Rolled Oats"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 207, "ingredient_id": 1035},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Milk"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 207, "ingredient_id": 1037},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Plain Greek Yogurt"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 207, "ingredient_id": 1023},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 207,
                    "plan_date": "2025-10-06",
                    "recipe_id": 418,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 207,
                    "user_id": 107,
                    "plan_date": "2025-10-06",
                    "recipe_id": 418,
                    "reason": "Logged by user as prepared with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 032: Simple wrap lunch
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_032",
        instruction=(
            "You are Antonio Garcia. On 2025-10-08, you made 'Asian Lettuce Wraps' for lunch. "
            "Before logging, you want to verify you have the key ingredients: Ground Beef, Romaine Lettuce, and Mushrooms. "
            "Then log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged meal history for Asian Lettuce Wraps with 4-star rating.'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Antonio Garcia"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 108}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Asian Lettuce Wraps"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Ground Beef"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 208, "ingredient_id": 1045},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Romaine Lettuce"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 208, "ingredient_id": 1013},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Mushrooms"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 208, "ingredient_id": 1075},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 208,
                    "plan_date": "2025-10-08",
                    "recipe_id": 441,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 208,
                    "user_id": 108,
                    "plan_date": "2025-10-08",
                    "recipe_id": 441,
                    "reason": "Logged meal history for Asian Lettuce Wraps with 4-star rating.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 033: Dinner with inventory check and rating
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_033",
        instruction=(
            "You are David Kowalski. On 2025-10-09, you want to make 'Grilled Salmon' for dinner. "
            "you should check your salmon inventory first, then you want to log the meal as prepared with a 5-star rating, and add an audit log with reason 'prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "David Kowalski"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 106}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Salmon"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 206, "ingredient_id": 1002},
            ),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Grilled Salmon"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 206,
                    "plan_date": "2025-10-09",
                    "recipe_id": 404,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 206,
                    "user_id": 106,
                    "plan_date": "2025-10-09",
                    "recipe_id": 404,
                    "reason": "prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 034: Simple dessert log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_034",
        instruction=(
            "You are Aiden Mercer. On 2025-10-13, you made 'Fruit Sorbet' for dessert. "
            "Before logging, you want to verify you have the key ingredients: Frozen Berries and Agave Nectar. "
            "Then log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged by user Aiden Mercer with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Fruit Sorbet"}
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Frozen Berries"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1143},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Agave Nectar"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1117},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-10-13",
                    "recipe_id": 452,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-10-13",
                    "recipe_id": 452,
                    "reason": "Logged by user Aiden Mercer with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 035: Simple vegan burgers
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_035",
        instruction=(
            "You are Aiden Mercer. On 2025-10-15, you made 'Vegan Black Bean Burgers' for dinner. "
            "Before logging, you want to verify you have the key ingredients: Black Beans, Yellow Onion, and Carrots. "
            "Then log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged meal preparation with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Vegan Black Bean Burgers"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Black Beans"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1051},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Yellow Onion"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1010},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Carrots"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1068},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-10-15",
                    "recipe_id": 432,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-10-15",
                    "recipe_id": 432,
                    "reason": "Logged meal preparation with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 036: Simple inventory consumption
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_036",
        instruction=(
            "You are Aiden Mercer. On 2025-10-16, you used 200 grams of 'Chicken Breast' for dinner. "
            "Update your inventory and log the consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Chicken Breast"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 201, "ingredient_id": 1001, "delta": -200},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 201, "user_id": 101, "ingredient_id": 1001, "delta": -200},
            ),
        ],
        outputs=[],
    ),
    # Task 037: Simple lunch log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_037",
        instruction=(
            "You are Sarah Chen. On 2025-10-13, you made 'Chicken Caesar Salad' for lunch. "
            "Before logging, you want to verify you have the key ingredients: Chicken Breast, Romaine Lettuce, and Parmesan Cheese. "
            "Then log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged prepared meal with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Caesar Salad"}
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Chicken Breast"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1001},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Romaine Lettuce"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1013},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Parmesan Cheese"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1089},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 203,
                    "plan_date": "2025-10-13",
                    "recipe_id": 445,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 203,
                    "user_id": 103,
                    "plan_date": "2025-10-13",
                    "recipe_id": 445,
                    "reason": "Logged prepared meal with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 038: Simple dairy-free dinner
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_038",
        instruction=(
            "You are Emma Johnson. On 2025-10-15, you made 'Dairy-Free Coconut Curry' for dinner. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Emma Johnson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 107}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Dairy-Free Coconut Curry"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 207,
                    "plan_date": "2025-10-15",
                    "recipe_id": 433,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 207,
                    "user_id": 107,
                    "plan_date": "2025-10-15",
                    "recipe_id": 433,
                    "reason": "Logged as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 039: Check recipe ingredients
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_039",
        instruction=(
            "You are David Kowalski. On 2025-10-13, you want to make 'Shrimp Pad Thai' for dinner. "
            "Check the recipe details and ingredients first, then log it as prepared with a 5-star rating, and add an audit log with reason 'Prepared Shrimp Pad Thai for dinner with 5-star rating.'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "David Kowalski"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 106}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Pad Thai"}
            ),
            Action(name="get_recipe_details", kwargs={"recipe_id": 430}),
            Action(name="list_recipe_ingredients", kwargs={"recipe_id": 430}),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 206,
                    "plan_date": "2025-10-13",
                    "recipe_id": 430,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 206,
                    "user_id": 106,
                    "plan_date": "2025-10-13",
                    "recipe_id": 430,
                    "reason": "Prepared Shrimp Pad Thai for dinner with 5-star rating.",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 040: Simple keto dinner
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_040",
        instruction=(
            "You are Rachel Kim. On 2025-10-18, you made 'Keto Zucchini Lasagna' for dinner. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user request'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Rachel Kim"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 109}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Keto Zucchini Lasagna"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 209,
                    "plan_date": "2025-10-18",
                    "recipe_id": 434,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 209,
                    "user_id": 109,
                    "plan_date": "2025-10-18",
                    "recipe_id": 434,
                    "reason": "Logged by user request",
                },
            ),
        ],
        outputs=[],
    ),
    # Tasks 041-060 - ALL SIMPLE (max 8 actions each, variation_2 style)
    # Task 041: Simple dinner log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_041",
        instruction=(
            "You are Aiden Mercer. On 2025-10-20, you made 'Korean Beef Bowl' for dinner. "
            "Before logging, you want to verify you have the key ingredients: Ground Beef, Soy Sauce, and Sesame Oil. "
            "Then you want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Korean Beef Bowl"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Ground Beef"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1045},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Soy Sauce"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1020},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Sesame Oil"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1109},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-10-20",
                    "recipe_id": 427,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-10-20",
                    "recipe_id": 427,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 042: Simple risotto
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_042",
        instruction=(
            "You are Aiden Mercer. On 2025-10-22, you made 'Mushroom Risotto' for dinner. "
            "Before logging, you want to verify you have the key ingredients: White Rice, Mushrooms, and Yellow Onion. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Mushroom Risotto"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "White Rice"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1006},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Mushrooms"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1075},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Yellow Onion"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1010},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-10-22",
                    "recipe_id": 426,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-10-22",
                    "recipe_id": 426,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 043: Simple inventory consumption
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_043",
        instruction=(
            "You are Aiden Mercer. On 2025-10-23, you used 150 grams of 'Ground Beef' for dinner. "
            "You want to update your inventory and log the consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Ground Beef"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 201, "ingredient_id": 1045, "delta": -150},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 201, "user_id": 101, "ingredient_id": 1045, "delta": -150},
            ),
        ],
        outputs=[],
    ),
    # Task 044: Simple egg-free dessert log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_044",
        instruction=(
            "You are Lina Alvarez. On 2025-10-24, you made 'Fruit Sorbet' for dessert. "
            "Before logging, you want to verify you have the key ingredients: Frozen Berries and Agave Nectar. "
            "Then log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged by user'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Lina Alvarez"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 102}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Fruit Sorbet"}
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Frozen Berries"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 202, "ingredient_id": 1143},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Agave Nectar"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 202, "ingredient_id": 1117},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 202,
                    "plan_date": "2025-10-24",
                    "recipe_id": 452,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 202,
                    "user_id": 102,
                    "plan_date": "2025-10-24",
                    "recipe_id": 452,
                    "reason": "Logged by user",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 045: Dinner with history check and rating
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_045",
        instruction=(
            "You are Lina Alvarez. On 2025-10-25, you want to make 'Mushroom Risotto' for dinner. "
            "Check if you've made it in the last 10 days, then log it as prepared with a 5-star rating, and add an audit log with reason 'User indicated meal was prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Lina Alvarez"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 102}),
            Action(
                name="get_meal_history_for_household", kwargs={"household_id": 202, "days_ago": 10}
            ),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Mushroom Risotto"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 202,
                    "plan_date": "2025-10-25",
                    "recipe_id": 426,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 202,
                    "user_id": 102,
                    "plan_date": "2025-10-25",
                    "recipe_id": 426,
                    "reason": "User indicated meal was prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 046: Simple lunch log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_046",
        instruction=(
            "You are Sarah Chen. On 2025-10-27, you made 'Cheese and Crackers Bento' for lunch. "
            "Before logging, you want to verify you have the key ingredients: Crackers and Cheddar Cheese. "
            "Then log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged prepared meal with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Cheese and Crackers"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Crackers"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1040},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Cheddar Cheese"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 203, "ingredient_id": 1024},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 203,
                    "plan_date": "2025-10-27",
                    "recipe_id": 411,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 203,
                    "user_id": 103,
                    "plan_date": "2025-10-27",
                    "recipe_id": 411,
                    "reason": "Logged prepared meal with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 047: Simple pasta salad
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_047",
        instruction=(
            "You are Sarah Chen. On 2025-10-29, you made 'Pasta Salad Lunch' for lunch. "
            "You want to log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged by user'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Pasta Salad"}
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 203,
                    "plan_date": "2025-10-29",
                    "recipe_id": 412,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 203,
                    "user_id": 103,
                    "plan_date": "2025-10-29",
                    "recipe_id": 412,
                    "reason": "Logged by user",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 048: Simple kid-friendly dinner log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_048",
        instruction=(
            "You are Marcus Williams. On 2025-10-27, you made 'Chicken Tacos' for dinner. "
            "Before logging, you want to verify you have the key ingredients: Chicken Breast, Corn Tortillas, and Chili Powder. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Marcus Williams"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 104}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Chicken Tacos"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Chicken Breast"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 204, "ingredient_id": 1001},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Corn Tortillas"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 204, "ingredient_id": 1008},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Chili Powder"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 204, "ingredient_id": 1019},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 204,
                    "plan_date": "2025-10-27",
                    "recipe_id": 402,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 204,
                    "user_id": 104,
                    "plan_date": "2025-10-27",
                    "recipe_id": 402,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 049: Simple chili dinner
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_049",
        instruction=(
            "You are Marcus Williams. On 2025-10-29, you made 'Vegetarian Chili' for dinner. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Marcus Williams"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 104}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Vegetarian Chili"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 204,
                    "plan_date": "2025-10-29",
                    "recipe_id": 424,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 204,
                    "user_id": 104,
                    "plan_date": "2025-10-29",
                    "recipe_id": 424,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 050: Simple breakfast log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_050",
        instruction=(
            "You are Priya Patel. On 2025-10-27, you made 'Greek Yogurt Bowl' for breakfast. "
            "Before logging, you want to verify you have the key ingredients: Plain Greek Yogurt, Berries (Mixed), and Honey. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged breakfast preparation with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Priya Patel"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 105}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Greek Yogurt Bowl"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Plain Greek Yogurt"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 205, "ingredient_id": 1023},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Berries (Mixed)"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 205, "ingredient_id": 1083},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Honey"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 205, "ingredient_id": 1115},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 205,
                    "plan_date": "2025-10-27",
                    "recipe_id": 421,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 205,
                    "user_id": 105,
                    "plan_date": "2025-10-27",
                    "recipe_id": 421,
                    "reason": "Logged breakfast preparation with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 051: Simple inventory consumption
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_051",
        instruction=(
            "You are Priya Patel. On 2025-10-30, you used 300 grams of 'Lentils' for a batch cook. "
            "Update your inventory and log the consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Priya Patel"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 105}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Lentils"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 205, "ingredient_id": 1053, "delta": -300},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 205, "user_id": 105, "ingredient_id": 1053, "delta": -300},
            ),
        ],
        outputs=[],
    ),
    # Task 052: Simple egg-free dessert log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_052",
        instruction=(
            "You are David Kowalski. On 2025-10-27, you made 'Butter Shortbread' for dessert. "
            "Before logging, you want to verify you have the key ingredients: Unsalted Butter, Granulated Sugar, and Flour (All-Purpose). "
            "Then log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged preparation of Butter Shortbread with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "David Kowalski"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 106}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Butter Shortbread"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Unsalted Butter"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 206, "ingredient_id": 1029},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Granulated Sugar"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 206, "ingredient_id": 1028},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Flour (All-Purpose)"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 206, "ingredient_id": 1027},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 206,
                    "plan_date": "2025-10-27",
                    "recipe_id": 416,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 206,
                    "user_id": 106,
                    "plan_date": "2025-10-27",
                    "recipe_id": 416,
                    "reason": "Logged preparation of Butter Shortbread with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 053: Check recipe for substitutions
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_053",
        instruction=(
            "You are David Kowalski. On 2025-10-27, you want to make 'Gluten-Free Pasta Primavera' for dinner. "
            "Check the recipe details and ingredients first, then you want to log it to your meal history as prepared."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "David Kowalski"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 106}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Gluten-Free Pasta Primavera"},
            ),
            Action(name="get_recipe_details", kwargs={"recipe_id": 431}),
            Action(name="list_recipe_ingredients", kwargs={"recipe_id": 431}),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 206,
                    "plan_date": "2025-10-27",
                    "recipe_id": 431,
                    "was_prepared": True,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 206,
                    "user_id": 106,
                    "plan_date": "2025-10-27",
                    "recipe_id": 431,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 054: Simple cod dinner
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_054",
        instruction=(
            "You are Emma Johnson. On 2025-10-30, you made 'Baked Cod with Herbs' for dinner. "
            "Before logging, you want to verify you have the key ingredients: Cod Fillet, Lemon, and Thyme. "
            "Then log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged by user as prepared with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Emma Johnson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 107}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Baked Cod"}
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Cod Fillet"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 207, "ingredient_id": 1049},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Lemon"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 207, "ingredient_id": 1022},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Thyme"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 207, "ingredient_id": 1106},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 207,
                    "plan_date": "2025-10-30",
                    "recipe_id": 425,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 207,
                    "user_id": 107,
                    "plan_date": "2025-10-30",
                    "recipe_id": 425,
                    "reason": "Logged by user as prepared with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 055: Simple inventory consumption
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_055",
        instruction=(
            "You are James Thompson. On 2025-10-31, you used 250 grams of 'Cod Fillet' for dinner. "
            "Update your inventory and log the consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "James Thompson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 110}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Cod Fillet"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 210, "ingredient_id": 1049, "delta": -250},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 210, "user_id": 110, "ingredient_id": 1049, "delta": -250},
            ),
        ],
        outputs=[],
    ),
    # Task 056: Check recipe ingredients for substitutions
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_056",
        instruction=(
            "You are Aiden Mercer. On 2025-10-20, you want to make 'Dairy-Free Coconut Curry' for dinner. "
            "Check the recipe details and ingredients to ensure no dairy, then log it as prepared with a 5-star rating, and add an audit log with reason 'Prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Dairy-Free Coconut Curry"},
            ),
            Action(name="get_recipe_details", kwargs={"recipe_id": 433}),
            Action(name="list_recipe_ingredients", kwargs={"recipe_id": 433}),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-10-20",
                    "recipe_id": 433,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-10-20",
                    "recipe_id": 433,
                    "reason": "Prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 057: Simple tagine dinner
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_057",
        instruction=(
            "You are Lina Alvarez. On 2025-11-01, you made 'Moroccan Tagine' for dinner. "
            "Before logging, you want to verify you have the key ingredients: Chicken Thighs, Yellow Onion, and Carrots. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Lina Alvarez"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 102}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Moroccan Tagine"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Chicken Thighs"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 202, "ingredient_id": 1047},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Yellow Onion"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 202, "ingredient_id": 1010},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Carrots"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 202, "ingredient_id": 1068},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 202,
                    "plan_date": "2025-11-01",
                    "recipe_id": 429,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 202,
                    "user_id": 102,
                    "plan_date": "2025-11-01",
                    "recipe_id": 429,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 058: Simple inventory consumption
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_058",
        instruction=(
            "You are Sarah Chen. On 2025-11-02, you used 120 grams of 'Quinoa' for lunch prep. "
            "Update your inventory and log the consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Quinoa"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 203, "ingredient_id": 1007, "delta": -120},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 203, "user_id": 103, "ingredient_id": 1007, "delta": -120},
            ),
        ],
        outputs=[],
    ),
    # Task 059: Simple kid-friendly breakfast log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_059",
        instruction=(
            "You are Marcus Williams. On 2025-11-03, you made 'Pancakes' for breakfast. "
            "Before logging, you want to verify you have the key ingredients: Flour (All-Purpose), Milk, and Eggs. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged breakfast meal with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Marcus Williams"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 104}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Pancakes"}
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Flour (All-Purpose)"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 204, "ingredient_id": 1027},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Milk"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 204, "ingredient_id": 1037},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Eggs"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 204, "ingredient_id": 1030},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 204,
                    "plan_date": "2025-11-03",
                    "recipe_id": 422,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 204,
                    "user_id": 104,
                    "plan_date": "2025-11-03",
                    "recipe_id": 422,
                    "reason": "Logged breakfast meal with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 060: Check recipe ingredients at aggregator
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_060",
        instruction=(
            "You are James Thompson. On 2025-11-03, you want to make 'Heart-Healthy Baked Salmon' for dinner. "
            "Check the recipe details and ingredients first, then log it as prepared with a 4-star rating, and add an audit log with reason 'user marked as prepared with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "James Thompson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 110}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Heart-Healthy Baked Salmon"},
            ),
            Action(name="get_recipe_details", kwargs={"recipe_id": 435}),
            Action(name="list_recipe_ingredients", kwargs={"recipe_id": 435}),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 210,
                    "plan_date": "2025-11-03",
                    "recipe_id": 435,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 210,
                    "user_id": 110,
                    "plan_date": "2025-11-03",
                    "recipe_id": 435,
                    "reason": "user marked as prepared with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Tasks 061-080 - ALL SIMPLE (max 8 actions each, variation_2 style)
    # Task 061: Simple dinner log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_061",
        instruction=(
            "You are Aiden Mercer. On 2025-11-03, you made 'Stuffed Bell Peppers' for dinner. "
            "Before logging, you want to verify you have the key ingredients: Bell Pepper, Ground Beef, and White Rice. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Stuffed Bell Peppers"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Bell Pepper"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1009},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Ground Beef"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1045},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "White Rice"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1006},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-11-03",
                    "recipe_id": 428,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-11-03",
                    "recipe_id": 428,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 062: Simple thai dinner
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_062",
        instruction=(
            "You are Aiden Mercer. On 2025-11-05, you made 'Thai Chicken Stir-Fry' for dinner. "
            "Before logging, you want to verify you have the key ingredients: Chicken Breast, Bell Pepper, and Yellow Onion. "
            "Then log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Thai Chicken Stir-Fry"},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Chicken Breast"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1001},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Bell Pepper"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1009},
            ),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Yellow Onion"}),
            Action(
                name="get_inventory_for_household_and_ingredient_id",
                kwargs={"household_id": 201, "ingredient_id": 1010},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-11-05",
                    "recipe_id": 407,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-11-05",
                    "recipe_id": 407,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 063: Simple inventory consumption
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_063",
        instruction=(
            "You are Aiden Mercer. On 2025-11-06, you used 200 grams of 'Salmon Fillet' for dinner. "
            "You want to update your inventory and log the consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Salmon Fillet"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 201, "ingredient_id": 1002, "delta": -200},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 201, "user_id": 101, "ingredient_id": 1002, "delta": -200},
            ),
        ],
        outputs=[],
    ),
    # Task 064: Simple dinner log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_064",
        instruction=(
            "You are Lina Alvarez. On 2025-11-03, you made 'Vegetarian Chili' for dinner. "
            "You want to log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged meal with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Lina Alvarez"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 102}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Vegetarian Chili"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 202,
                    "plan_date": "2025-11-03",
                    "recipe_id": 424,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 202,
                    "user_id": 102,
                    "plan_date": "2025-11-03",
                    "recipe_id": 424,
                    "reason": "Logged meal with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 065: Check recipe for substitutions
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_065",
        instruction=(
            "You are Lina Alvarez. On 2025-11-03, you want to make 'Vegan Black Bean Burgers' for dinner. "
            "Check the recipe details and ingredients to ensure they're suitable, then log it as prepared with a 5-star rating, and add an audit log with reason 'Prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Lina Alvarez"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 102}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Vegan Black Bean Burgers"},
            ),
            Action(name="get_recipe_details", kwargs={"recipe_id": 432}),
            Action(name="list_recipe_ingredients", kwargs={"recipe_id": 432}),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 202,
                    "plan_date": "2025-11-03",
                    "recipe_id": 432,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 202,
                    "user_id": 102,
                    "plan_date": "2025-11-03",
                    "recipe_id": 432,
                    "reason": "Prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 066: Dinner with history check and rating
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_066",
        instruction=(
            "You are Sarah Chen. On 2025-11-04, you want to make 'Mediterranean Bowl' for dinner. "
            "Check if you've made it in the last 14 days, then log it as prepared with a 5-star rating, and add an audit log with reason 'Prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(
                name="get_meal_history_for_household", kwargs={"household_id": 203, "days_ago": 14}
            ),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Mediterranean Bowl"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 203,
                    "plan_date": "2025-11-04",
                    "recipe_id": 442,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 203,
                    "user_id": 103,
                    "plan_date": "2025-11-04",
                    "recipe_id": 442,
                    "reason": "Prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 067: Simple mediterranean bowl
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_067",
        instruction=(
            "You are Sarah Chen. On 2025-11-06, you made 'Mediterranean Bowl' for lunch. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged prepared meal with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Mediterranean Bowl"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 203,
                    "plan_date": "2025-11-06",
                    "recipe_id": 442,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 203,
                    "user_id": 103,
                    "plan_date": "2025-11-06",
                    "recipe_id": 442,
                    "reason": "Logged prepared meal with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 068: Simple kid-friendly dinner log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_068",
        instruction=(
            "You are Marcus Williams. On 2025-11-05, you made 'Pancakes' for dinner. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged prepared meal with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Marcus Williams"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 104}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Pancakes"}
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 204,
                    "plan_date": "2025-11-05",
                    "recipe_id": 422,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 204,
                    "user_id": 104,
                    "plan_date": "2025-11-05",
                    "recipe_id": 422,
                    "reason": "Logged prepared meal with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 069: Simple buddha bowl
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_069",
        instruction=(
            "You are Marcus Williams. On 2025-11-07, you made 'Buddha Bowl' for lunch. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged prepared meal with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Marcus Williams"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 104}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Buddha Bowl"}
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 204,
                    "plan_date": "2025-11-07",
                    "recipe_id": 446,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 204,
                    "user_id": 104,
                    "plan_date": "2025-11-07",
                    "recipe_id": 446,
                    "reason": "Logged prepared meal with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 070: Simple lunch log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_070",
        instruction=(
            "You are Priya Patel. On 2025-11-10, you made 'Hummus Veggie Wrap' for lunch. "
            "You want to log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged prepared meal with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Priya Patel"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 105}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Hummus Veggie Wrap"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 205,
                    "plan_date": "2025-11-10",
                    "recipe_id": 410,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 205,
                    "user_id": 105,
                    "plan_date": "2025-11-10",
                    "recipe_id": 410,
                    "reason": "Logged prepared meal with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 071: Simple high-protein dinner log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_071",
        instruction=(
            "You are David Kowalski. On 2025-11-10, you made 'Vegetable Omelet' for dinner. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged Vegetable Omelet as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "David Kowalski"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 106}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Vegetable Omelet"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 206,
                    "plan_date": "2025-11-10",
                    "recipe_id": 438,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 206,
                    "user_id": 106,
                    "plan_date": "2025-11-10",
                    "recipe_id": 438,
                    "reason": "Logged Vegetable Omelet as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 072: Simple breakfast log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_072",
        instruction=(
            "You are Emma Johnson. On 2025-11-10, you made 'Scrambled Eggs with Toast' for breakfast. "
            "You want to log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged breakfast preparation with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Emma Johnson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 107}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Scrambled Eggs"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 207,
                    "plan_date": "2025-11-10",
                    "recipe_id": 419,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 207,
                    "user_id": 107,
                    "plan_date": "2025-11-10",
                    "recipe_id": 419,
                    "reason": "Logged breakfast preparation with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 073: Check recipe for substitutions
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_073",
        instruction=(
            "You are Antonio Garcia. On 2025-11-10, you want to make 'Keto Zucchini Lasagna' for dinner. "
            "Check the recipe details and ingredients first, then log it as prepared with a 5-star rating, and add an audit log with reason 'Prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Antonio Garcia"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 108}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Keto Zucchini Lasagna"},
            ),
            Action(name="get_recipe_details", kwargs={"recipe_id": 434}),
            Action(name="list_recipe_ingredients", kwargs={"recipe_id": 434}),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 208,
                    "plan_date": "2025-11-10",
                    "recipe_id": 434,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 208,
                    "user_id": 108,
                    "plan_date": "2025-11-10",
                    "recipe_id": 434,
                    "reason": "Prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 074: Simple tuna sandwich
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_074",
        instruction=(
            "You are Rachel Kim. On 2025-11-12, you made 'Tuna Salad Sandwich' for lunch. "
            "You want to log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged by user'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Rachel Kim"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 109}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Tuna Salad Sandwich"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 209,
                    "plan_date": "2025-11-12",
                    "recipe_id": 443,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 209,
                    "user_id": 109,
                    "plan_date": "2025-11-12",
                    "recipe_id": 443,
                    "reason": "Logged by user",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 075: Simple inventory consumption
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_075",
        instruction=(
            "You are James Thompson. On 2025-11-13, you used 250 grams of 'Chicken Breast' for dinner. "
            "Update your inventory and log the consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "James Thompson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 110}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Chicken Breast"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 210, "ingredient_id": 1001, "delta": -250},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 210, "user_id": 110, "ingredient_id": 1001, "delta": -250},
            ),
        ],
        outputs=[],
    ),
    # Task 076: Check recipe for substitutions
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_076",
        instruction=(
            "You are Aiden Mercer. On 2025-11-10, you want to make 'Lentil Soup' for dinner. "
            "Check the recipe details and ingredients first, then you want to log it to your meal history as prepared."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Lentil Soup"}
            ),
            Action(name="get_recipe_details", kwargs={"recipe_id": 408}),
            Action(name="list_recipe_ingredients", kwargs={"recipe_id": 408}),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-11-10",
                    "recipe_id": 408,
                    "was_prepared": True,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-11-10",
                    "recipe_id": 408,
                },
            ),
        ],
        outputs=[],
    ),
    # Task 077: Simple soup and sandwich
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_077",
        instruction=(
            "You are Lina Alvarez. On 2025-11-14, you made 'Soup and Sandwich Combo' for lunch. "
            "You want to log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged prepared meal with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Lina Alvarez"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 102}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Soup and Sandwich"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 202,
                    "plan_date": "2025-11-14",
                    "recipe_id": 447,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 202,
                    "user_id": 102,
                    "plan_date": "2025-11-14",
                    "recipe_id": 447,
                    "reason": "Logged prepared meal with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 078: Simple inventory consumption
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_078",
        instruction=(
            "You are Rachel Kim. On 2025-11-15, you used 140 grams of 'Firm Tofu' for lunch prep. "
            "You want to update your inventory and log the consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Rachel Kim"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 109}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Firm Tofu"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 209, "ingredient_id": 1003, "delta": -140},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 209, "user_id": 109, "ingredient_id": 1003, "delta": -140},
            ),
        ],
        outputs=[],
    ),
    # Task 079: Simple dinner log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_079",
        instruction=(
            "You are James Thompson. On 2025-11-17, you made 'Baked Cod with Herbs' for dinner. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "James Thompson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 110}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Baked Cod with Herbs"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 210,
                    "plan_date": "2025-11-17",
                    "recipe_id": 425,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 210,
                    "user_id": 110,
                    "plan_date": "2025-11-17",
                    "recipe_id": 425,
                    "reason": "Logged as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 080: Simple quinoa breakfast
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_080",
        instruction=(
            "You are James Thompson. On 2025-11-19, you made 'Quinoa Breakfast Bowl' for breakfast. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "James Thompson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 110}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Quinoa Breakfast Bowl"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 210,
                    "plan_date": "2025-11-19",
                    "recipe_id": 436,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 210,
                    "user_id": 110,
                    "plan_date": "2025-11-19",
                    "recipe_id": 436,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Tasks 081-100 - ALL SIMPLE (max 8 actions each, variation_2 style)
    # Task 081: Simple lunch log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_081",
        instruction=(
            "You are Sarah Chen. On 2025-11-24, you made 'Turkey Sandwich' for lunch. "
            "You want to log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged by user'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Turkey Sandwich"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 203,
                    "plan_date": "2025-11-24",
                    "recipe_id": 409,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 203,
                    "user_id": 103,
                    "plan_date": "2025-11-24",
                    "recipe_id": 409,
                    "reason": "Logged by user",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 082: Simple chia pudding
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_082",
        instruction=(
            "You are Sarah Chen. On 2025-11-26, you made 'Chia Pudding' for breakfast. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Chia Pudding"}
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 203,
                    "plan_date": "2025-11-26",
                    "recipe_id": 437,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 203,
                    "user_id": 103,
                    "plan_date": "2025-11-26",
                    "recipe_id": 437,
                    "reason": "Logged with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 083: Simple inventory consumption
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_083",
        instruction=(
            "You are Sarah Chen. On 2025-11-27, you used 180 grams of 'Spinach' for lunch. "
            "You want to update your inventory and log the consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Sarah Chen"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 103}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Spinach"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 203, "ingredient_id": 1070, "delta": -180},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 203, "user_id": 103, "ingredient_id": 1070, "delta": -180},
            ),
        ],
        outputs=[],
    ),
    # Task 084: Simple kid-friendly breakfast log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_084",
        instruction=(
            "You are Marcus Williams. On 2025-11-24, you made 'Gluten-Free Pancakes' for breakfast. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged breakfast preparation with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Marcus Williams"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 104}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Gluten-Free Pancakes"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 204,
                    "plan_date": "2025-11-24",
                    "recipe_id": 440,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 204,
                    "user_id": 104,
                    "plan_date": "2025-11-24",
                    "recipe_id": 440,
                    "reason": "Logged breakfast preparation with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 085: Simple yogurt parfait
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_085",
        instruction=(
            "You are Marcus Williams. On 2025-11-28, you made 'Yogurt Parfait Cup' for lunch. "
            "You want to log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged by user Marcus Williams with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Marcus Williams"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 104}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Yogurt Parfait"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 204,
                    "plan_date": "2025-11-28",
                    "recipe_id": 413,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 204,
                    "user_id": 104,
                    "plan_date": "2025-11-28",
                    "recipe_id": 413,
                    "reason": "Logged by user Marcus Williams with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 086: Simple egg-free dessert log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_086",
        instruction=(
            "You are Priya Patel. On 2025-11-24, you made 'Gluten-Free Brownies' for dessert. "
            "You want to log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged prepared dessert with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Priya Patel"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 105}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Gluten-Free Brownies"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 205,
                    "plan_date": "2025-11-24",
                    "recipe_id": 453,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 205,
                    "user_id": 105,
                    "plan_date": "2025-11-24",
                    "recipe_id": 453,
                    "reason": "Logged prepared dessert with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 087: Check recipe for substitutions
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_087",
        instruction=(
            "You are Priya Patel. On 2025-11-24, you want to make 'Buddha Bowl' for dinner. "
            "Check the recipe details and ingredients to ensure they're suitable, then log it as prepared with a 5-star rating, and add an audit log with reason 'Prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Priya Patel"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 105}),
            Action(
                name="search_recipes_by_title_substring", kwargs={"title_substring": "Buddha Bowl"}
            ),
            Action(name="get_recipe_details", kwargs={"recipe_id": 446}),
            Action(name="list_recipe_ingredients", kwargs={"recipe_id": 446}),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 205,
                    "plan_date": "2025-11-24",
                    "recipe_id": 446,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 205,
                    "user_id": 105,
                    "plan_date": "2025-11-24",
                    "recipe_id": 446,
                    "reason": "Prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 088: Simple high-protein dinner log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_088",
        instruction=(
            "You are Antonio Garcia. On 2025-11-24, you made 'Moroccan Tagine' for dinner. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Antonio Garcia"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 108}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Moroccan Tagine"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 208,
                    "plan_date": "2025-11-24",
                    "recipe_id": 429,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 208,
                    "user_id": 108,
                    "plan_date": "2025-11-24",
                    "recipe_id": 429,
                    "reason": "Logged with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 089: Simple smoothie bowl
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_089",
        instruction=(
            "You are Antonio Garcia. On 2025-11-26, you made 'Smoothie Bowl' for breakfast. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Antonio Garcia"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 108}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Smoothie Bowl"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 208,
                    "plan_date": "2025-11-26",
                    "recipe_id": 439,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 208,
                    "user_id": 108,
                    "plan_date": "2025-11-26",
                    "recipe_id": 439,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 090: Simple inventory consumption
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_090",
        instruction=(
            "You are Antonio Garcia. On 2025-11-27, you used 200 grams of 'Chicken Thighs' for dinner. "
            "Update your inventory and log the consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Antonio Garcia"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 108}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Chicken Thighs"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 208, "ingredient_id": 1047, "delta": -200},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 208, "user_id": 108, "ingredient_id": 1047, "delta": -200},
            ),
        ],
        outputs=[],
    ),
    # Task 091: Simple dinner log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_091",
        instruction=(
            "You are Emma Johnson. On 2025-12-01, you made 'Thai Chicken Stir-Fry' for dinner. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Emma Johnson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 107}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Thai Chicken Stir-Fry"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 207,
                    "plan_date": "2025-12-01",
                    "recipe_id": 407,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 207,
                    "user_id": 107,
                    "plan_date": "2025-12-01",
                    "recipe_id": 407,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 092: Check recipe for substitutions
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_092",
        instruction=(
            "You are Emma Johnson. On 2025-12-01, you want to make 'Spaghetti with Tomato Sauce' for dinner. "
            "Check the recipe details and ingredients first, then log it as prepared with a 4-star rating, and add an audit log with reason 'User marked as prepared with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Emma Johnson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 107}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Spaghetti with Tomato Sauce"},
            ),
            Action(name="get_recipe_details", kwargs={"recipe_id": 401}),
            Action(name="list_recipe_ingredients", kwargs={"recipe_id": 401}),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 207,
                    "plan_date": "2025-12-01",
                    "recipe_id": 401,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 207,
                    "user_id": 107,
                    "plan_date": "2025-12-01",
                    "recipe_id": 401,
                    "reason": "User marked as prepared with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 093: Simple yogurt bowl
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_093",
        instruction=(
            "You are Emma Johnson. On 2025-12-03, you made 'Smoothie Bowl' for breakfast. "
            "You want to log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged manually by user'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Emma Johnson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 107}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Smoothie Bowl"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 207,
                    "plan_date": "2025-12-03",
                    "recipe_id": 439,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 207,
                    "user_id": 107,
                    "plan_date": "2025-12-03",
                    "recipe_id": 439,
                    "reason": "Logged manually by user",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 094: Simple breakfast log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_094",
        instruction=(
            "You are Rachel Kim. On 2025-12-01, you made 'Overnight Oats with Berries' for breakfast. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Rachel Kim"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 109}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Overnight Oats"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 209,
                    "plan_date": "2025-12-01",
                    "recipe_id": 418,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 209,
                    "user_id": 109,
                    "plan_date": "2025-12-01",
                    "recipe_id": 418,
                    "reason": "Logged by user",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 095: Simple chocolate cookies
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_095",
        instruction=(
            "You are Rachel Kim. On 2025-12-03, you made 'No-Bake Oatmeal Cocoa Cookies' for dessert. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Rachel Kim"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 109}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "No-Bake Oatmeal Cocoa"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 209,
                    "plan_date": "2025-12-03",
                    "recipe_id": 415,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 209,
                    "user_id": 109,
                    "plan_date": "2025-12-03",
                    "recipe_id": 415,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 096: Simple inventory consumption
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_096",
        instruction=(
            "You are Rachel Kim. On 2025-12-04, you used 160 grams of 'Eggs' for breakfast. "
            "You want to update your inventory and log the consumption."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Rachel Kim"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 109}),
            Action(name="search_ingredients_by_name", kwargs={"name_query": "Eggs"}),
            Action(
                name="update_inventory_quantity",
                kwargs={"household_id": 209, "ingredient_id": 1030, "delta": -160},
            ),
            Action(
                name="log_inventory_consume_by_keys",
                kwargs={"household_id": 209, "user_id": 109, "ingredient_id": 1030, "delta": -160},
            ),
        ],
        outputs=[],
    ),
    # Task 097: Simple dessert log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_097",
        instruction=(
            "You are Aiden Mercer. On 2025-12-05, you made 'Vegan Chocolate Mousse' for dessert. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Logged by user as prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "Aiden Mercer"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 101}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Chocolate Mousse"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 201,
                    "plan_date": "2025-12-05",
                    "recipe_id": 451,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 201,
                    "user_id": 101,
                    "plan_date": "2025-12-05",
                    "recipe_id": 451,
                    "reason": "Logged by user as prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 098: Simple lunch log
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_098",
        instruction=(
            "You are James Thompson. On 2025-12-01, you made 'Cheese and Crackers Bento' for lunch. "
            "You want to log this to your meal history as prepared with a 4-star rating, and add an audit log with reason 'Logged meal with 4-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "James Thompson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 110}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Cheese and Crackers"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 210,
                    "plan_date": "2025-12-01",
                    "recipe_id": 411,
                    "was_prepared": True,
                    "rating_int": 4,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 210,
                    "user_id": 110,
                    "plan_date": "2025-12-01",
                    "recipe_id": 411,
                    "reason": "Logged meal with 4-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 099: Check recipe for substitutions
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_099",
        instruction=(
            "You are James Thompson. On 2025-12-01, you want to make 'Chickpea Curry' for dinner. "
            "Check the recipe details and ingredients to ensure you have everything, then log it as prepared with a 5-star rating, and add an audit log with reason 'Prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "James Thompson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 110}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Chickpea Curry"},
            ),
            Action(name="get_recipe_details", kwargs={"recipe_id": 403}),
            Action(name="list_recipe_ingredients", kwargs={"recipe_id": 403}),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 210,
                    "plan_date": "2025-12-01",
                    "recipe_id": 403,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 210,
                    "user_id": 110,
                    "plan_date": "2025-12-01",
                    "recipe_id": 403,
                    "reason": "Prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
    # Task 100: Simple nice cream dessert
    Task(
        annotator="v3_simple",
        user_id="recipes_v3_pilot_100",
        instruction=(
            "You are James Thompson. On 2025-12-05, you made 'Banana Nice Cream' for dessert. "
            "You want to log this to your meal history as prepared with a 5-star rating, and add an audit log with reason 'Prepared with 5-star rating'."
        ),
        actions=[
            Action(name="get_user_by_full_name", kwargs={"full_name": "James Thompson"}),
            Action(name="get_household_by_primary_user", kwargs={"user_id": 110}),
            Action(
                name="search_recipes_by_title_substring",
                kwargs={"title_substring": "Banana Nice Cream"},
            ),
            Action(
                name="append_meal_history",
                kwargs={
                    "household_id": 210,
                    "plan_date": "2025-12-05",
                    "recipe_id": 417,
                    "was_prepared": True,
                    "rating_int": 5,
                },
            ),
            Action(
                name="log_meal_history_create_by_keys",
                kwargs={
                    "household_id": 210,
                    "user_id": 110,
                    "plan_date": "2025-12-05",
                    "recipe_id": 417,
                    "reason": "Prepared with 5-star rating",
                },
            ),
        ],
        outputs=[],
    ),
]
