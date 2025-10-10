from domains.dto import Task, Action

TASKS = [
    # 700
    Task(
        annotator="variation_7",
        user_id="task_700",
        instruction=(
            "You must ensure repository 'blog-lite' is in a state where an open pull request exists from branch 'feature-home' to 'main' and that PR has the label 'docs'. After achieving this state, list the open pull requests for 'blog-lite'."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'blog-lite'}),
            Action(name="create_branch", kwargs={'repo': 'blog-lite', 'branch': 'feature-home'}),
            Action(name="add_commit", kwargs={'repo': 'blog-lite', 'branch': 'feature-home', 'message': 'setup index'}),
            Action(name="open_pr", kwargs={'repo': 'blog-lite', 'head_branch': 'feature-home', 'base_branch': 'main', 'title': 'Home section'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'blog-lite', 'number': 1, 'label': 'docs'}),
            Action(name="list_prs", kwargs={'repo': 'blog-lite', 'state': 'open'}),
        ],
        outputs=[
            '"label": "docs"',
            '"title": "Home section"',
            '"state": "open"',
        ],
    ),

    # 701
    Task(
        annotator="variation_7",
        user_id="task_701",
        instruction=(
            "You should maintain repository 'support-bot' where branch 'resize' has a commit 'add resize', and a pull request titled 'Resize feature' from 'resize' to 'main' is open with label 'feature'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'support-bot'}),
            Action(name="create_branch", kwargs={'repo': 'support-bot', 'branch': 'resize'}),
            Action(name="add_commit", kwargs={'repo': 'support-bot', 'branch': 'resize', 'message': 'add resize'}),
            Action(name="open_pr", kwargs={'repo': 'support-bot', 'head_branch': 'resize', 'base_branch': 'main', 'title': 'Resize feature'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'support-bot', 'number': 1, 'label': 'feature'}),
            Action(name="list_prs", kwargs={'repo': 'support-bot', 'state': 'open'}),
        ],
        outputs=[
            '"label": "feature"',
            '"title": "Resize feature"',
            '"state": "open"',
        ],
    ),

    # 702
    Task(
        annotator="variation_7",
        user_id="task_702",
        instruction=(
            "You should maintain repository 'img-tool' where branch 'readme' has a commit 'write readme', and a pull request titled 'README' from 'readme' to 'main' is open with label 'api'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'img-tool'}),
            Action(name="create_branch", kwargs={'repo': 'img-tool', 'branch': 'readme'}),
            Action(name="add_commit", kwargs={'repo': 'img-tool', 'branch': 'readme', 'message': 'write readme'}),
            Action(name="open_pr", kwargs={'repo': 'img-tool', 'head_branch': 'readme', 'base_branch': 'main', 'title': 'README'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'img-tool', 'number': 1, 'label': 'api'}),
            Action(name="list_prs", kwargs={'repo': 'img-tool', 'state': 'open'}),
        ],
        outputs=[
            '"label": "api"',
            '"title": "README"',
            '"state": "open"',
        ],
    ),

    # 703
    Task(
        annotator="variation_7",
        user_id="task_703",
        instruction=(
            "You must ensure repository 'calc-pro' has an open pull request from branch 'daily-cron' to 'main' with the label 'ops'. After achieving this state, list the open pull requests for 'calc-pro'."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'calc-pro'}),
            Action(name="create_branch", kwargs={'repo': 'calc-pro', 'branch': 'daily-cron'}),
            Action(name="add_commit", kwargs={'repo': 'calc-pro', 'branch': 'daily-cron', 'message': 'cron impl'}),
            Action(name="open_pr", kwargs={'repo': 'calc-pro', 'head_branch': 'daily-cron', 'base_branch': 'main', 'title': 'Cron jobs'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'calc-pro', 'number': 1, 'label': 'ops'}),
            Action(name="list_prs", kwargs={'repo': 'calc-pro', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ops"',
            '"title": "Cron jobs"',
            '"state": "open"',
        ],
    ),

    # 704
    Task(
        annotator="variation_7",
        user_id="task_704",
        instruction=(
            "You should maintain repository 'docs-kit' where branch 'badges' has a commit 'README badges', and a pull request titled 'README badges' from 'badges' to 'main' is open with label 'security'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'docs-kit'}),
            Action(name="create_branch", kwargs={'repo': 'docs-kit', 'branch': 'badges'}),
            Action(name="add_commit", kwargs={'repo': 'docs-kit', 'branch': 'badges', 'message': 'README badges'}),
            Action(name="open_pr", kwargs={'repo': 'docs-kit', 'head_branch': 'badges', 'base_branch': 'main', 'title': 'README badges'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'docs-kit', 'number': 1, 'label': 'security'}),
            Action(name="list_prs", kwargs={'repo': 'docs-kit', 'state': 'open'}),
        ],
        outputs=[
            '"label": "security"',
            '"title": "README badges"',
            '"state": "open"',
        ],
    ),

    # 705
    Task(
        annotator="variation_7",
        user_id="task_705",
        instruction=(
            "You should maintain repository 'portal-ui' where branch 'theme' has a commit 'dark theme', and a pull request titled 'Dark theme' from 'theme' to 'main' is open with label 'infra'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'portal-ui'}),
            Action(name="create_branch", kwargs={'repo': 'portal-ui', 'branch': 'theme'}),
            Action(name="add_commit", kwargs={'repo': 'portal-ui', 'branch': 'theme', 'message': 'dark theme'}),
            Action(name="open_pr", kwargs={'repo': 'portal-ui', 'head_branch': 'theme', 'base_branch': 'main', 'title': 'Dark theme'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'portal-ui', 'number': 1, 'label': 'infra'}),
            Action(name="list_prs", kwargs={'repo': 'portal-ui', 'state': 'open'}),
        ],
        outputs=[
            '"label": "infra"',
            '"title": "Dark theme"',
            '"state": "open"',
        ],
    ),

    # 706
    Task(
        annotator="variation_7",
        user_id="task_706",
        instruction=(
            "You should maintain repository 'backup-tool' where branch 'index-v2' has a commit 'add indexer', and a pull request titled 'Indexer v2' from 'index-v2' to 'main' is open with label 'seo'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'backup-tool'}),
            Action(name="create_branch", kwargs={'repo': 'backup-tool', 'branch': 'index-v2'}),
            Action(name="add_commit", kwargs={'repo': 'backup-tool', 'branch': 'index-v2', 'message': 'add indexer'}),
            Action(name="open_pr", kwargs={'repo': 'backup-tool', 'head_branch': 'index-v2', 'base_branch': 'main', 'title': 'Indexer v2'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'backup-tool', 'number': 1, 'label': 'seo'}),
            Action(name="list_prs", kwargs={'repo': 'backup-tool', 'state': 'open'}),
        ],
        outputs=[
            '"label": "seo"',
            '"title": "Indexer v2"',
            '"state": "open"',
        ],
    ),

    # 707
    Task(
        annotator="variation_7",
        user_id="task_707",
        instruction=(
            "You should maintain repository 'pkg-index' where branch 'smtp' has a commit 'smtp auth', and a pull request titled 'SMTP auth' from 'smtp' to 'main' is open with label 'ui'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'pkg-index'}),
            Action(name="create_branch", kwargs={'repo': 'pkg-index', 'branch': 'smtp'}),
            Action(name="add_commit", kwargs={'repo': 'pkg-index', 'branch': 'smtp', 'message': 'smtp auth'}),
            Action(name="open_pr", kwargs={'repo': 'pkg-index', 'head_branch': 'smtp', 'base_branch': 'main', 'title': 'SMTP auth'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'pkg-index', 'number': 1, 'label': 'ui'}),
            Action(name="list_prs", kwargs={'repo': 'pkg-index', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ui"',
            '"title": "SMTP auth"',
            '"state": "open"',
        ],
    ),

    # 708
    Task(
        annotator="variation_7",
        user_id="task_708",
        instruction=(
            "You should maintain repository 'core-lib' where branch 'landing' has a commit 'hero copy', and a pull request titled 'Landing page' from 'landing' to 'main' is open with label 'docs'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'core-lib'}),
            Action(name="create_branch", kwargs={'repo': 'core-lib', 'branch': 'landing'}),
            Action(name="add_commit", kwargs={'repo': 'core-lib', 'branch': 'landing', 'message': 'hero copy'}),
            Action(name="open_pr", kwargs={'repo': 'core-lib', 'head_branch': 'landing', 'base_branch': 'main', 'title': 'Landing page'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'core-lib', 'number': 1, 'label': 'docs'}),
            Action(name="list_prs", kwargs={'repo': 'core-lib', 'state': 'open'}),
        ],
        outputs=[
            '"label": "docs"',
            '"title": "Landing page"',
            '"state": "open"',
        ],
    ),

    # 709
    Task(
        annotator="variation_7",
        user_id="task_709",
        instruction=(
            "You should maintain repository 'data-cleaner' where branch 'tax' has a commit 'add vat', and a pull request titled 'VAT support' from 'tax' to 'main' is open with label 'feature'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'data-cleaner'}),
            Action(name="create_branch", kwargs={'repo': 'data-cleaner', 'branch': 'tax'}),
            Action(name="add_commit", kwargs={'repo': 'data-cleaner', 'branch': 'tax', 'message': 'add vat'}),
            Action(name="open_pr", kwargs={'repo': 'data-cleaner', 'head_branch': 'tax', 'base_branch': 'main', 'title': 'VAT support'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'data-cleaner', 'number': 1, 'label': 'feature'}),
            Action(name="list_prs", kwargs={'repo': 'data-cleaner', 'state': 'open'}),
        ],
        outputs=[
            '"label": "feature"',
            '"title": "VAT support"',
            '"state": "open"',
        ],
    ),

    # 710
    Task(
        annotator="variation_7",
        user_id="task_710",
        instruction=(
            "Ensure repository 'docs-kit-plus' is in the following state: branch 'sitemap' includes a commit 'gen sitemap'; an open pull request titled 'Sitemap' exists from 'sitemap' to 'main' and has label 'api'. Then return the list of open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'docs-kit-plus'}),
            Action(name="create_branch", kwargs={'repo': 'docs-kit-plus', 'branch': 'sitemap'}),
            Action(name="add_commit", kwargs={'repo': 'docs-kit-plus', 'branch': 'sitemap', 'message': 'gen sitemap'}),
            Action(name="open_pr", kwargs={'repo': 'docs-kit-plus', 'head_branch': 'sitemap', 'base_branch': 'main', 'title': 'Sitemap'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'docs-kit-plus', 'number': 1, 'label': 'api'}),
            Action(name="list_prs", kwargs={'repo': 'docs-kit-plus', 'state': 'open'}),
        ],
        outputs=[
            '"label": "api"',
            '"title": "Sitemap"',
            '"state": "open"',
        ],
    ),

    # 711
    Task(
        annotator="variation_7",
        user_id="task_711",
        instruction=(
            "You should maintain repository 'payments-svc' where branch 'pd' has a commit 'pagerduty hook', and a pull request titled 'PagerDuty webhook' from 'pd' to 'main' is open with label 'ops'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'payments-svc'}),
            Action(name="create_branch", kwargs={'repo': 'payments-svc', 'branch': 'pd'}),
            Action(name="add_commit", kwargs={'repo': 'payments-svc', 'branch': 'pd', 'message': 'pagerduty hook'}),
            Action(name="open_pr", kwargs={'repo': 'payments-svc', 'head_branch': 'pd', 'base_branch': 'main', 'title': 'PagerDuty webhook'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'payments-svc', 'number': 1, 'label': 'ops'}),
            Action(name="list_prs", kwargs={'repo': 'payments-svc', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ops"',
            '"title": "PagerDuty webhook"',
            '"state": "open"',
        ],
    ),

    # 712
    Task(
        annotator="variation_7",
        user_id="task_712",
        instruction=(
            "You should maintain repository 'cli-tool' where branch 'embeddings' has a commit 'add sbert', and a pull request titled 'Embeddings' from 'embeddings' to 'main' is open with label 'security'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'cli-tool'}),
            Action(name="create_branch", kwargs={'repo': 'cli-tool', 'branch': 'embeddings'}),
            Action(name="add_commit", kwargs={'repo': 'cli-tool', 'branch': 'embeddings', 'message': 'add sbert'}),
            Action(name="open_pr", kwargs={'repo': 'cli-tool', 'head_branch': 'embeddings', 'base_branch': 'main', 'title': 'Embeddings'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'cli-tool', 'number': 1, 'label': 'security'}),
            Action(name="list_prs", kwargs={'repo': 'cli-tool', 'state': 'open'}),
        ],
        outputs=[
            '"label": "security"',
            '"title": "Embeddings"',
            '"state": "open"',
        ],
    ),

    # 713
    Task(
        annotator="variation_7",
        user_id="task_713",
        instruction=(
            "You should maintain repository 'scheduler' where branch 'sms' has a commit 'twilio', and a pull request titled 'SMS support' from 'sms' to 'main' is open with label 'infra'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'scheduler'}),
            Action(name="create_branch", kwargs={'repo': 'scheduler', 'branch': 'sms'}),
            Action(name="add_commit", kwargs={'repo': 'scheduler', 'branch': 'sms', 'message': 'twilio'}),
            Action(name="open_pr", kwargs={'repo': 'scheduler', 'head_branch': 'sms', 'base_branch': 'main', 'title': 'SMS support'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'scheduler', 'number': 1, 'label': 'infra'}),
            Action(name="list_prs", kwargs={'repo': 'scheduler', 'state': 'open'}),
        ],
        outputs=[
            '"label": "infra"',
            '"title": "SMS support"',
            '"state": "open"',
        ],
    ),

    # 714
    Task(
        annotator="variation_7",
        user_id="task_714",
        instruction=(
            "You should maintain repository 'search-api' where branch 'geojson' has a commit 'import geojson', and a pull request titled 'GeoJSON import' from 'geojson' to 'main' is open with label 'seo'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'search-api'}),
            Action(name="create_branch", kwargs={'repo': 'search-api', 'branch': 'geojson'}),
            Action(name="add_commit", kwargs={'repo': 'search-api', 'branch': 'geojson', 'message': 'import geojson'}),
            Action(name="open_pr", kwargs={'repo': 'search-api', 'head_branch': 'geojson', 'base_branch': 'main', 'title': 'GeoJSON import'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'search-api', 'number': 1, 'label': 'seo'}),
            Action(name="list_prs", kwargs={'repo': 'search-api', 'state': 'open'}),
        ],
        outputs=[
            '"label": "seo"',
            '"title": "GeoJSON import"',
            '"state": "open"',
        ],
    ),

    # 715
    Task(
        annotator="variation_7",
        user_id="task_715",
        instruction=(
            "You should maintain repository 'monitor' where branch 'batch' has a commit 'batch process', and a pull request titled 'Batch process' from 'batch' to 'main' is open with label 'ui'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'monitor'}),
            Action(name="create_branch", kwargs={'repo': 'monitor', 'branch': 'batch'}),
            Action(name="add_commit", kwargs={'repo': 'monitor', 'branch': 'batch', 'message': 'batch process'}),
            Action(name="open_pr", kwargs={'repo': 'monitor', 'head_branch': 'batch', 'base_branch': 'main', 'title': 'Batch process'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'monitor', 'number': 1, 'label': 'ui'}),
            Action(name="list_prs", kwargs={'repo': 'monitor', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ui"',
            '"title": "Batch process"',
            '"state": "open"',
        ],
    ),

    # 716
    Task(
        annotator="variation_7",
        user_id="task_716",
        instruction=(
            "Ensure repository 'mail-svc' is in the following state: branch 'reply' includes a commit 'quick replies'; an open pull request titled 'Quick replies' exists from 'reply' to 'main' and has label 'docs'. Then return the list of open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'mail-svc'}),
            Action(name="create_branch", kwargs={'repo': 'mail-svc', 'branch': 'reply'}),
            Action(name="add_commit", kwargs={'repo': 'mail-svc', 'branch': 'reply', 'message': 'quick replies'}),
            Action(name="open_pr", kwargs={'repo': 'mail-svc', 'head_branch': 'reply', 'base_branch': 'main', 'title': 'Quick replies'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'mail-svc', 'number': 1, 'label': 'docs'}),
            Action(name="list_prs", kwargs={'repo': 'mail-svc', 'state': 'open'}),
        ],
        outputs=[
            '"label": "docs"',
            '"title": "Quick replies"',
            '"state": "open"',
        ],
    ),

    # 717
    Task(
        annotator="variation_7",
        user_id="task_717",
        instruction=(
            "You should maintain repository 'report-gen' where branch 'nightly' has a commit 'cron spec', and a pull request titled 'Nightly cron' from 'nightly' to 'main' is open with label 'feature'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'report-gen'}),
            Action(name="create_branch", kwargs={'repo': 'report-gen', 'branch': 'nightly'}),
            Action(name="add_commit", kwargs={'repo': 'report-gen', 'branch': 'nightly', 'message': 'cron spec'}),
            Action(name="open_pr", kwargs={'repo': 'report-gen', 'head_branch': 'nightly', 'base_branch': 'main', 'title': 'Nightly cron'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'report-gen', 'number': 1, 'label': 'feature'}),
            Action(name="list_prs", kwargs={'repo': 'report-gen', 'state': 'open'}),
        ],
        outputs=[
            '"label": "feature"',
            '"title": "Nightly cron"',
            '"state": "open"',
        ],
    ),

    # 718
    Task(
        annotator="variation_7",
        user_id="task_718",
        instruction=(
            "You should maintain repository 'auth-svc' where branch 'android-ci' has a commit 'gradle fix', and a pull request titled 'Android CI' from 'android-ci' to 'main' is open with label 'api'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'auth-svc'}),
            Action(name="create_branch", kwargs={'repo': 'auth-svc', 'branch': 'android-ci'}),
            Action(name="add_commit", kwargs={'repo': 'auth-svc', 'branch': 'android-ci', 'message': 'gradle fix'}),
            Action(name="open_pr", kwargs={'repo': 'auth-svc', 'head_branch': 'android-ci', 'base_branch': 'main', 'title': 'Android CI'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'auth-svc', 'number': 1, 'label': 'api'}),
            Action(name="list_prs", kwargs={'repo': 'auth-svc', 'state': 'open'}),
        ],
        outputs=[
            '"label": "api"',
            '"title": "Android CI"',
            '"state": "open"',
        ],
    ),

    # 719
    Task(
        annotator="variation_7",
        user_id="task_719",
        instruction=(
            "You should maintain repository 'ui-lib' where branch 'dag' has a commit 'add dag', and a pull request titled 'Airflow DAG' from 'dag' to 'main' is open with label 'ops'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'ui-lib'}),
            Action(name="create_branch", kwargs={'repo': 'ui-lib', 'branch': 'dag'}),
            Action(name="add_commit", kwargs={'repo': 'ui-lib', 'branch': 'dag', 'message': 'add dag'}),
            Action(name="open_pr", kwargs={'repo': 'ui-lib', 'head_branch': 'dag', 'base_branch': 'main', 'title': 'Airflow DAG'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'ui-lib', 'number': 1, 'label': 'ops'}),
            Action(name="list_prs", kwargs={'repo': 'ui-lib', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ops"',
            '"title": "Airflow DAG"',
            '"state": "open"',
        ],
    ),

    # 720
    Task(
        annotator="variation_7",
        user_id="task_720",
        instruction=(
            "You should maintain repository 'db-migrator' where branch 'minimax' has a commit 'minimax', and a pull request titled 'Add minimax' from 'minimax' to 'main' is open with label 'security'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'db-migrator'}),
            Action(name="create_branch", kwargs={'repo': 'db-migrator', 'branch': 'minimax'}),
            Action(name="add_commit", kwargs={'repo': 'db-migrator', 'branch': 'minimax', 'message': 'minimax'}),
            Action(name="open_pr", kwargs={'repo': 'db-migrator', 'head_branch': 'minimax', 'base_branch': 'main', 'title': 'Add minimax'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'db-migrator', 'number': 1, 'label': 'security'}),
            Action(name="list_prs", kwargs={'repo': 'db-migrator', 'state': 'open'}),
        ],
        outputs=[
            '"label": "security"',
            '"title": "Add minimax"',
            '"state": "open"',
        ],
    ),

    # 721
    Task(
        annotator="variation_7",
        user_id="task_721",
        instruction=(
            "You should maintain repository 'kafka-consumer' where branch 'tiles' has a commit 'tile cache', and a pull request titled 'Tile cache' from 'tiles' to 'main' is open with label 'infra'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'kafka-consumer'}),
            Action(name="create_branch", kwargs={'repo': 'kafka-consumer', 'branch': 'tiles'}),
            Action(name="add_commit", kwargs={'repo': 'kafka-consumer', 'branch': 'tiles', 'message': 'tile cache'}),
            Action(name="open_pr", kwargs={'repo': 'kafka-consumer', 'head_branch': 'tiles', 'base_branch': 'main', 'title': 'Tile cache'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'kafka-consumer', 'number': 1, 'label': 'infra'}),
            Action(name="list_prs", kwargs={'repo': 'kafka-consumer', 'state': 'open'}),
        ],
        outputs=[
            '"label": "infra"',
            '"title": "Tile cache"',
            '"state": "open"',
        ],
    ),

    # 722
    Task(
        annotator="variation_7",
        user_id="task_722",
        instruction=(
            "You should maintain repository 'notifier' where branch 'session' has a commit 'session mgmt', and a pull request titled 'Session init' from 'session' to 'main' is open with label 'seo'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'notifier'}),
            Action(name="create_branch", kwargs={'repo': 'notifier', 'branch': 'session'}),
            Action(name="add_commit", kwargs={'repo': 'notifier', 'branch': 'session', 'message': 'session mgmt'}),
            Action(name="open_pr", kwargs={'repo': 'notifier', 'head_branch': 'session', 'base_branch': 'main', 'title': 'Session init'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'notifier', 'number': 1, 'label': 'seo'}),
            Action(name="list_prs", kwargs={'repo': 'notifier', 'state': 'open'}),
        ],
        outputs=[
            '"label": "seo"',
            '"title": "Session init"',
            '"state": "open"',
        ],
    ),

    # 723
    Task(
        annotator="variation_7",
        user_id="task_723",
        instruction=(
            "You should maintain repository 'crawler' where branch 'etl' has a commit 'etl script', and a pull request titled 'ETL v1' from 'etl' to 'main' is open with label 'ui'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'crawler'}),
            Action(name="create_branch", kwargs={'repo': 'crawler', 'branch': 'etl'}),
            Action(name="add_commit", kwargs={'repo': 'crawler', 'branch': 'etl', 'message': 'etl script'}),
            Action(name="open_pr", kwargs={'repo': 'crawler', 'head_branch': 'etl', 'base_branch': 'main', 'title': 'ETL v1'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'crawler', 'number': 1, 'label': 'ui'}),
            Action(name="list_prs", kwargs={'repo': 'crawler', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ui"',
            '"title": "ETL v1"',
            '"state": "open"',
        ],
    ),

    # 724
    Task(
        annotator="variation_7",
        user_id="task_724",
        instruction=(
            "You should maintain repository 'logger' where branch 'vat' has a commit 'vat rounding', and a pull request titled 'VAT rounding' from 'vat' to 'main' is open with label 'docs'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'logger'}),
            Action(name="create_branch", kwargs={'repo': 'logger', 'branch': 'vat'}),
            Action(name="add_commit", kwargs={'repo': 'logger', 'branch': 'vat', 'message': 'vat rounding'}),
            Action(name="open_pr", kwargs={'repo': 'logger', 'head_branch': 'vat', 'base_branch': 'main', 'title': 'VAT rounding'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'logger', 'number': 1, 'label': 'docs'}),
            Action(name="list_prs", kwargs={'repo': 'logger', 'state': 'open'}),
        ],
        outputs=[
            '"label": "docs"',
            '"title": "VAT rounding"',
            '"state": "open"',
        ],
    ),

    # 725
    Task(
        annotator="variation_7",
        user_id="task_725",
        instruction=(
            "You should maintain repository 'game-ai' where branch 'cron' has a commit 'cron jobs', and a pull request titled 'Cron jobs v2' from 'cron' to 'main' is open with label 'feature'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'game-ai'}),
            Action(name="create_branch", kwargs={'repo': 'game-ai', 'branch': 'cron'}),
            Action(name="add_commit", kwargs={'repo': 'game-ai', 'branch': 'cron', 'message': 'cron jobs'}),
            Action(name="open_pr", kwargs={'repo': 'game-ai', 'head_branch': 'cron', 'base_branch': 'main', 'title': 'Cron jobs v2'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'game-ai', 'number': 1, 'label': 'feature'}),
            Action(name="list_prs", kwargs={'repo': 'game-ai', 'state': 'open'}),
        ],
        outputs=[
            '"label": "feature"',
            '"title": "Cron jobs v2"',
            '"state": "open"',
        ],
    ),

    # 726
    Task(
        annotator="variation_7",
        user_id="task_726",
        instruction=(
            "You should maintain repository 'image-cdn' where branch 'oauth' has a commit 'oauth route', and a pull request titled 'OAuth route' from 'oauth' to 'main' is open with label 'api'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'image-cdn'}),
            Action(name="create_branch", kwargs={'repo': 'image-cdn', 'branch': 'oauth'}),
            Action(name="add_commit", kwargs={'repo': 'image-cdn', 'branch': 'oauth', 'message': 'oauth route'}),
            Action(name="open_pr", kwargs={'repo': 'image-cdn', 'head_branch': 'oauth', 'base_branch': 'main', 'title': 'OAuth route'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'image-cdn', 'number': 1, 'label': 'api'}),
            Action(name="list_prs", kwargs={'repo': 'image-cdn', 'state': 'open'}),
        ],
        outputs=[
            '"label": "api"',
            '"title": "OAuth route"',
            '"state": "open"',
        ],
    ),

    # 727
    Task(
        annotator="variation_7",
        user_id="task_727",
        instruction=(
            "You should maintain repository 'analytics' where branch 'graphql' has a commit 'schema', and a pull request titled 'GraphQL schema' from 'graphql' to 'main' is open with label 'ops'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'analytics'}),
            Action(name="create_branch", kwargs={'repo': 'analytics', 'branch': 'graphql'}),
            Action(name="add_commit", kwargs={'repo': 'analytics', 'branch': 'graphql', 'message': 'schema'}),
            Action(name="open_pr", kwargs={'repo': 'analytics', 'head_branch': 'graphql', 'base_branch': 'main', 'title': 'GraphQL schema'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'analytics', 'number': 1, 'label': 'ops'}),
            Action(name="list_prs", kwargs={'repo': 'analytics', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ops"',
            '"title": "GraphQL schema"',
            '"state": "open"',
        ],
    ),

    # 728
    Task(
        annotator="variation_7",
        user_id="task_728",
        instruction=(
            "You should maintain repository 'seo-helper' where branch 'avatars' has a commit 'avatar gen', and a pull request titled 'Avatar generator' from 'avatars' to 'main' is open with label 'security'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'seo-helper'}),
            Action(name="create_branch", kwargs={'repo': 'seo-helper', 'branch': 'avatars'}),
            Action(name="add_commit", kwargs={'repo': 'seo-helper', 'branch': 'avatars', 'message': 'avatar gen'}),
            Action(name="open_pr", kwargs={'repo': 'seo-helper', 'head_branch': 'avatars', 'base_branch': 'main', 'title': 'Avatar generator'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'seo-helper', 'number': 1, 'label': 'security'}),
            Action(name="list_prs", kwargs={'repo': 'seo-helper', 'state': 'open'}),
        ],
        outputs=[
            '"label": "security"',
            '"title": "Avatar generator"',
            '"state": "open"',
        ],
    ),

    # 729
    Task(
        annotator="variation_7",
        user_id="task_729",
        instruction=(
            "You should maintain repository 'release-bot' where branch 'payments' has a commit 'fee calc', and a pull request titled 'Fee calc' from 'payments' to 'main' is open with label 'infra'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'release-bot'}),
            Action(name="create_branch", kwargs={'repo': 'release-bot', 'branch': 'payments'}),
            Action(name="add_commit", kwargs={'repo': 'release-bot', 'branch': 'payments', 'message': 'fee calc'}),
            Action(name="open_pr", kwargs={'repo': 'release-bot', 'head_branch': 'payments', 'base_branch': 'main', 'title': 'Fee calc'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'release-bot', 'number': 1, 'label': 'infra'}),
            Action(name="list_prs", kwargs={'repo': 'release-bot', 'state': 'open'}),
        ],
        outputs=[
            '"label": "infra"',
            '"title": "Fee calc"',
            '"state": "open"',
        ],
    ),

    # 730
    Task(
        annotator="variation_7",
        user_id="task_730",
        instruction=(
            "You should maintain repository 'docs-site' where branch 'profiles' has a commit 'profile page', and a pull request titled 'Profile page' from 'profiles' to 'main' is open with label 'seo'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'docs-site'}),
            Action(name="create_branch", kwargs={'repo': 'docs-site', 'branch': 'profiles'}),
            Action(name="add_commit", kwargs={'repo': 'docs-site', 'branch': 'profiles', 'message': 'profile page'}),
            Action(name="open_pr", kwargs={'repo': 'docs-site', 'head_branch': 'profiles', 'base_branch': 'main', 'title': 'Profile page'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'docs-site', 'number': 1, 'label': 'seo'}),
            Action(name="list_prs", kwargs={'repo': 'docs-site', 'state': 'open'}),
        ],
        outputs=[
            '"label": "seo"',
            '"title": "Profile page"',
            '"state": "open"',
        ],
    ),

    # 731
    Task(
        annotator="variation_7",
        user_id="task_731",
        instruction=(
            "You should maintain repository 'billing-svc' where branch 'events' has a commit 'event bus', and a pull request titled 'Event bus' from 'events' to 'main' is open with label 'ui'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'billing-svc'}),
            Action(name="create_branch", kwargs={'repo': 'billing-svc', 'branch': 'events'}),
            Action(name="add_commit", kwargs={'repo': 'billing-svc', 'branch': 'events', 'message': 'event bus'}),
            Action(name="open_pr", kwargs={'repo': 'billing-svc', 'head_branch': 'events', 'base_branch': 'main', 'title': 'Event bus'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'billing-svc', 'number': 1, 'label': 'ui'}),
            Action(name="list_prs", kwargs={'repo': 'billing-svc', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ui"',
            '"title": "Event bus"',
            '"state": "open"',
        ],
    ),

    # 732
    Task(
        annotator="variation_7",
        user_id="task_732",
        instruction=(
            "You should maintain repository 'feature-flag' where branch 'comments' has a commit 'comment form', and a pull request titled 'Comments UI' from 'comments' to 'main' is open with label 'docs'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'feature-flag'}),
            Action(name="create_branch", kwargs={'repo': 'feature-flag', 'branch': 'comments'}),
            Action(name="add_commit", kwargs={'repo': 'feature-flag', 'branch': 'comments', 'message': 'comment form'}),
            Action(name="open_pr", kwargs={'repo': 'feature-flag', 'head_branch': 'comments', 'base_branch': 'main', 'title': 'Comments UI'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'feature-flag', 'number': 1, 'label': 'docs'}),
            Action(name="list_prs", kwargs={'repo': 'feature-flag', 'state': 'open'}),
        ],
        outputs=[
            '"label": "docs"',
            '"title": "Comments UI"',
            '"state": "open"',
        ],
    ),

    # 733
    Task(
        annotator="variation_7",
        user_id="task_733",
        instruction=(
            "You should maintain repository 'cache-layer' where branch 'notify' has a commit 'notify rules', and a pull request titled 'Notify rules' from 'notify' to 'main' is open with label 'feature'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'cache-layer'}),
            Action(name="create_branch", kwargs={'repo': 'cache-layer', 'branch': 'notify'}),
            Action(name="add_commit", kwargs={'repo': 'cache-layer', 'branch': 'notify', 'message': 'notify rules'}),
            Action(name="open_pr", kwargs={'repo': 'cache-layer', 'head_branch': 'notify', 'base_branch': 'main', 'title': 'Notify rules'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'cache-layer', 'number': 1, 'label': 'feature'}),
            Action(name="list_prs", kwargs={'repo': 'cache-layer', 'state': 'open'}),
        ],
        outputs=[
            '"label": "feature"',
            '"title": "Notify rules"',
            '"state": "open"',
        ],
    ),

    # 734
    Task(
        annotator="variation_7",
        user_id="task_734",
        instruction=(
            "You should maintain repository 'ml-pipeline' where branch 'realtime' has a commit 'socket hub', and a pull request titled 'Realtime hub' from 'realtime' to 'main' is open with label 'api'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'ml-pipeline'}),
            Action(name="create_branch", kwargs={'repo': 'ml-pipeline', 'branch': 'realtime'}),
            Action(name="add_commit", kwargs={'repo': 'ml-pipeline', 'branch': 'realtime', 'message': 'socket hub'}),
            Action(name="open_pr", kwargs={'repo': 'ml-pipeline', 'head_branch': 'realtime', 'base_branch': 'main', 'title': 'Realtime hub'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'ml-pipeline', 'number': 1, 'label': 'api'}),
            Action(name="list_prs", kwargs={'repo': 'ml-pipeline', 'state': 'open'}),
        ],
        outputs=[
            '"label": "api"',
            '"title": "Realtime hub"',
            '"state": "open"',
        ],
    ),

    # 735
    Task(
        annotator="variation_7",
        user_id="task_735",
        instruction=(
            "You should maintain repository 'mobile-app' where branch 'delta' has a commit 'delta sync', and a pull request titled 'Delta sync' from 'delta' to 'main' is open with label 'ops'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'mobile-app'}),
            Action(name="create_branch", kwargs={'repo': 'mobile-app', 'branch': 'delta'}),
            Action(name="add_commit", kwargs={'repo': 'mobile-app', 'branch': 'delta', 'message': 'delta sync'}),
            Action(name="open_pr", kwargs={'repo': 'mobile-app', 'head_branch': 'delta', 'base_branch': 'main', 'title': 'Delta sync'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'mobile-app', 'number': 1, 'label': 'ops'}),
            Action(name="list_prs", kwargs={'repo': 'mobile-app', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ops"',
            '"title": "Delta sync"',
            '"state": "open"',
        ],
    ),

    # 736
    Task(
        annotator="variation_7",
        user_id="task_736",
        instruction=(
            "You should maintain repository 'web-auth' where branch 'pdf' has a commit 'pdf export', and a pull request titled 'PDF export' from 'pdf' to 'main' is open with label 'security'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'web-auth'}),
            Action(name="create_branch", kwargs={'repo': 'web-auth', 'branch': 'pdf'}),
            Action(name="add_commit", kwargs={'repo': 'web-auth', 'branch': 'pdf', 'message': 'pdf export'}),
            Action(name="open_pr", kwargs={'repo': 'web-auth', 'head_branch': 'pdf', 'base_branch': 'main', 'title': 'PDF export'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'web-auth', 'number': 1, 'label': 'security'}),
            Action(name="list_prs", kwargs={'repo': 'web-auth', 'state': 'open'}),
        ],
        outputs=[
            '"label": "security"',
            '"title": "PDF export"',
            '"state": "open"',
        ],
    ),

    # 737
    Task(
        annotator="variation_7",
        user_id="task_737",
        instruction=(
            "You should maintain repository 'observability' where branch 'thumb' has a commit 'image thumbs', and a pull request titled 'Thumbnailer' from 'thumb' to 'main' is open with label 'infra'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'observability'}),
            Action(name="create_branch", kwargs={'repo': 'observability', 'branch': 'thumb'}),
            Action(name="add_commit", kwargs={'repo': 'observability', 'branch': 'thumb', 'message': 'image thumbs'}),
            Action(name="open_pr", kwargs={'repo': 'observability', 'head_branch': 'thumb', 'base_branch': 'main', 'title': 'Thumbnailer'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'observability', 'number': 1, 'label': 'infra'}),
            Action(name="list_prs", kwargs={'repo': 'observability', 'state': 'open'}),
        ],
        outputs=[
            '"label": "infra"',
            '"title": "Thumbnailer"',
            '"state": "open"',
        ],
    ),

    # 738
    Task(
        annotator="variation_7",
        user_id="task_738",
        instruction=(
            "You should maintain repository 'map-service' where branch 'schedule' has a commit 'schedule lib', and a pull request titled 'Scheduler core' from 'schedule' to 'main' is open with label 'seo'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'map-service'}),
            Action(name="create_branch", kwargs={'repo': 'map-service', 'branch': 'schedule'}),
            Action(name="add_commit", kwargs={'repo': 'map-service', 'branch': 'schedule', 'message': 'schedule lib'}),
            Action(name="open_pr", kwargs={'repo': 'map-service', 'head_branch': 'schedule', 'base_branch': 'main', 'title': 'Scheduler core'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'map-service', 'number': 1, 'label': 'seo'}),
            Action(name="list_prs", kwargs={'repo': 'map-service', 'state': 'open'}),
        ],
        outputs=[
            '"label": "seo"',
            '"title": "Scheduler core"',
            '"state": "open"',
        ],
    ),

    # 739
    Task(
        annotator="variation_7",
        user_id="task_739",
        instruction=(
            "You should maintain repository 'api-gateway' where branch 'bus' has a commit 'bus impl', and a pull request titled 'Event bus v2' from 'bus' to 'main' is open with label 'ui'; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'api-gateway'}),
            Action(name="create_branch", kwargs={'repo': 'api-gateway', 'branch': 'bus'}),
            Action(name="add_commit", kwargs={'repo': 'api-gateway', 'branch': 'bus', 'message': 'bus impl'}),
            Action(name="open_pr", kwargs={'repo': 'api-gateway', 'head_branch': 'bus', 'base_branch': 'main', 'title': 'Event bus v2'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'api-gateway', 'number': 1, 'label': 'ui'}),
            Action(name="list_prs", kwargs={'repo': 'api-gateway', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ui"',
            '"title": "Event bus v2"',
            '"state": "open"',
        ],
    ),

    # 740
    Task(
        annotator="variation_7",
        user_id="task_740",
        instruction=(
            "Ensure repository 'data-lake' exists (create it if missing). Ensure there is an open issue titled 'Reply delay' with body 'Replies are slow in peak hours.', labeled 'ops', and assigned to 'sam'. After ensuring this, return only the 'label', 'assignees', and 'title' fields for that issue (do not return full issue objects)."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'data-lake'}),
            Action(name="open_issue", kwargs={'repo': 'data-lake', 'title': 'Reply delay', 'body': 'Replies are slow in peak hours.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'data-lake', 'number': 1, 'label': 'ops'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'data-lake', 'number': 1, 'username': 'sam'}),
            Action(name="list_issues", kwargs={'repo': 'data-lake'}),
        ],
        outputs=[
            '"label": "ops"',
            '"assignees": ["sam"]',
            '"title": "Reply delay"',
        ],
    ),

    # 741
    Task(
        annotator="variation_7",
        user_id="task_741",
        instruction=(
            "Ensure repository 'chat-bot' exists (create it if missing). Ensure there is an open issue titled 'Rate limit' with body 'Too strict rate limiting.', labeled 'api', and assigned to 'sam'. After ensuring this, return only the 'label', 'assignees', and 'title' fields for that issue (do not return full issue objects)."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'chat-bot'}),
            Action(name="open_issue", kwargs={'repo': 'chat-bot', 'title': 'Rate limit', 'body': 'Too strict rate limiting.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'chat-bot', 'number': 1, 'label': 'api'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'chat-bot', 'number': 1, 'username': 'sam'}),
            Action(name="list_issues", kwargs={'repo': 'chat-bot'}),
        ],
        outputs=[
            '"label": "api"',
            '"assignees": ["sam"]',
            '"title": "Rate limit"',
        ],
    ),

    # 742
    Task(
        annotator="variation_7",
        user_id="task_742",
        instruction=(
            "Ensure repository 'cron-runner' exists (create it if missing). Ensure there is an open issue titled 'Bad rounding' with body 'Rounding error in totals.', labeled 'priority', and assigned to 'lena'. After ensuring this, return only the 'label', 'assignees', and 'title' fields for that issue (do not return full issue objects)."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'cron-runner'}),
            Action(name="open_issue", kwargs={'repo': 'cron-runner', 'title': 'Bad rounding', 'body': 'Rounding error in totals.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'cron-runner', 'number': 1, 'label': 'priority'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'cron-runner', 'number': 1, 'username': 'lena'}),
            Action(name="list_issues", kwargs={'repo': 'cron-runner'}),
        ],
        outputs=[
            '"label": "priority"',
            '"assignees": ["lena"]',
            '"title": "Bad rounding"',
        ],
    ),

    # 743
    Task(
        annotator="variation_7",
        user_id="task_743",
        instruction=(
            "Ensure repository 'oncall-bot' exists (create it if missing). Ensure there is an open issue titled 'Null handling' with body 'Handle None safely.', labeled 'bug', and assigned to 'mike'. After ensuring this, return only the 'label', 'assignees', and 'title' fields for that issue (do not return full issue objects)."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'oncall-bot'}),
            Action(name="open_issue", kwargs={'repo': 'oncall-bot', 'title': 'Null handling', 'body': 'Handle None safely.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'oncall-bot', 'number': 1, 'label': 'bug'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'oncall-bot', 'number': 1, 'username': 'mike'}),
            Action(name="list_issues", kwargs={'repo': 'oncall-bot'}),
        ],
        outputs=[
            '"label": "bug"',
            '"assignees": ["mike"]',
            '"title": "Null handling"',
        ],
    ),

    # 744
    Task(
        annotator="variation_7",
        user_id="task_744",
        instruction=(
            "Ensure repository 'linter' exists (create it if missing). Ensure there is an open issue titled 'S3 lifecycle' with body 'Configure S3 lifecycle policies.', labeled 'infra', and assigned to 'jane'. After ensuring this, return only the 'label', 'assignees', and 'title' fields for that issue (do not return full issue objects)."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'linter'}),
            Action(name="open_issue", kwargs={'repo': 'linter', 'title': 'S3 lifecycle', 'body': 'Configure S3 lifecycle policies.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'linter', 'number': 1, 'label': 'infra'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'linter', 'number': 1, 'username': 'jane'}),
            Action(name="list_issues", kwargs={'repo': 'linter'}),
        ],
        outputs=[
            '"label": "infra"',
            '"assignees": ["jane"]',
            '"title": "S3 lifecycle"',
        ],
    ),

    # 745
    Task(
        annotator="variation_7",
        user_id="task_745",
        instruction=(
            "Ensure repository 'ai-sdk' exists (create it if missing). Ensure there is an open issue titled 'Token expiry bug' with body 'Expired tokens still validate.', labeled 'security', and assigned to 'ravi'. After ensuring this, return only the 'label', 'assignees', and 'title' fields for that issue (do not return full issue objects)."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'ai-sdk'}),
            Action(name="open_issue", kwargs={'repo': 'ai-sdk', 'title': 'Token expiry bug', 'body': 'Expired tokens still validate.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'ai-sdk', 'number': 1, 'label': 'security'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'ai-sdk', 'number': 1, 'username': 'ravi'}),
            Action(name="list_issues", kwargs={'repo': 'ai-sdk'}),
        ],
        outputs=[
            '"label": "security"',
            '"assignees": ["ravi"]',
            '"title": "Token expiry bug"',
        ],
    ),

    # 746
    Task(
        annotator="variation_7",
        user_id="task_746",
        instruction=(
            "Ensure repository 'design-system' exists (create it if missing). Ensure there is an open issue titled 'Eviction policy' with body 'Decide LFU vs LRU.', labeled 'planning', and assigned to 'nora'. After ensuring this, return only the 'label', 'assignees', and 'title' fields for that issue (do not return full issue objects)."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'design-system'}),
            Action(name="open_issue", kwargs={'repo': 'design-system', 'title': 'Eviction policy', 'body': 'Decide LFU vs LRU.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'design-system', 'number': 1, 'label': 'planning'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'design-system', 'number': 1, 'username': 'nora'}),
            Action(name="list_issues", kwargs={'repo': 'design-system'}),
        ],
        outputs=[
            '"label": "planning"',
            '"assignees": ["nora"]',
            '"title": "Eviction policy"',
        ],
    ),

    # 747
    Task(
        annotator="variation_7",
        user_id="task_747",
        instruction=(
            "Ensure repository 'etl-runner' exists (create it if missing). Ensure there is an open issue titled 'Add cron parser' with body 'Add a Cron expression parser.', labeled 'feature', and assigned to 'omar'. After ensuring this, return only the 'label', 'assignees', and 'title' fields for that issue (do not return full issue objects)."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'etl-runner'}),
            Action(name="open_issue", kwargs={'repo': 'etl-runner', 'title': 'Add cron parser', 'body': 'Add a Cron expression parser.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'etl-runner', 'number': 1, 'label': 'feature'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'etl-runner', 'number': 1, 'username': 'omar'}),
            Action(name="list_issues", kwargs={'repo': 'etl-runner'}),
        ],
        outputs=[
            '"label": "feature"',
            '"assignees": ["omar"]',
            '"title": "Add cron parser"',
        ],
    ),

    # 748
    Task(
        annotator="variation_7",
        user_id="task_748",
        instruction=(
            "You should manage repository 'geo-index' by opening an issue titled 'Healthcheck fails' with body 'Probe endpoint fails on cold start.' labeled 'bug' assigned to 'amin'; list issues."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'geo-index'}),
            Action(name="open_issue", kwargs={'repo': 'geo-index', 'title': 'Healthcheck fails', 'body': 'Probe endpoint fails on cold start.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'geo-index', 'number': 1, 'label': 'bug'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'geo-index', 'number': 1, 'username': 'amin'}),
            Action(name="list_issues", kwargs={'repo': 'geo-index'}),
        ],
        outputs=[
            '"label": "bug"',
            '"assignees": ["amin"]',
            '"title": "Healthcheck fails"',
        ],
    ),

    # 749
    Task(
        annotator="variation_7",
        user_id="task_749",
        instruction=(
            "Ensure repository 'queue-svc' exists (create it if missing). Ensure there is an open issue titled 'Add migration plan' with body 'Outline migration steps.', labeled 'planning', and assigned to 'sara'. After ensuring this, return only the 'label', 'assignees', and 'title' fields for that issue (do not return full issue objects)."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'queue-svc'}),
            Action(name="open_issue", kwargs={'repo': 'queue-svc', 'title': 'Add migration plan', 'body': 'Outline migration steps.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'queue-svc', 'number': 1, 'label': 'planning'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'queue-svc', 'number': 1, 'username': 'sara'}),
            Action(name="list_issues", kwargs={'repo': 'queue-svc'}),
        ],
        outputs=[
            '"label": "planning"',
            '"assignees": ["sara"]',
            '"title": "Add migration plan"',
        ],
    ),

    # 750
    Task(
        annotator="variation_7",
        user_id="task_750",
        instruction=(
            "Ensure repository 'rate-limiter' exists (create it if missing). Ensure there is an open issue titled 'CSV export' with body 'Export CSV with delimiter option.', labeled 'feature', and assigned to 'sara'. After ensuring this, return only the 'label', 'assignees', and 'title' fields for that issue (do not return full issue objects)."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'rate-limiter'}),
            Action(name="open_issue", kwargs={'repo': 'rate-limiter', 'title': 'CSV export', 'body': 'Export CSV with delimiter option.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'rate-limiter', 'number': 1, 'label': 'feature'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'rate-limiter', 'number': 1, 'username': 'sara'}),
            Action(name="list_issues", kwargs={'repo': 'rate-limiter'}),
        ],
        outputs=[
            '"label": "feature"',
            '"assignees": ["sara"]',
            '"title": "CSV export"',
        ],
    ),

    # 751
    Task(
        annotator="variation_7",
        user_id="task_751",
        instruction=(
            "You should manage repository 'uploader' by opening an issue titled 'Respect robots.txt' with body 'Crawler must respect robots.txt.' labeled 'compliance' assigned to 'amin'; list issues."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'uploader'}),
            Action(name="open_issue", kwargs={'repo': 'uploader', 'title': 'Respect robots.txt', 'body': 'Crawler must respect robots.txt.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'uploader', 'number': 1, 'label': 'compliance'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'uploader', 'number': 1, 'username': 'amin'}),
            Action(name="list_issues", kwargs={'repo': 'uploader'}),
        ],
        outputs=[
            '"label": "compliance"',
            '"assignees": ["amin"]',
            '"title": "Respect robots.txt"',
        ],
    ),

    # 752
    Task(
        annotator="variation_7",
        user_id="task_752",
        instruction=(
            "You should manage repository 'image-proc' by opening an issue titled 'Rule for imports' with body 'Enforce import ordering.' labeled 'enhancement' assigned to 'jane'; list issues."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'image-proc'}),
            Action(name="open_issue", kwargs={'repo': 'image-proc', 'title': 'Rule for imports', 'body': 'Enforce import ordering.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'image-proc', 'number': 1, 'label': 'enhancement'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'image-proc', 'number': 1, 'username': 'jane'}),
            Action(name="list_issues", kwargs={'repo': 'image-proc'}),
        ],
        outputs=[
            '"label": "enhancement"',
            '"assignees": ["jane"]',
            '"title": "Rule for imports"',
        ],
    ),

    # 753
    Task(
        annotator="variation_7",
        user_id="task_753",
        instruction=(
            "You should manage repository 'webhooks' by opening an issue titled 'Toggle not saved' with body 'Toggles revert after refresh.' labeled 'bug' assigned to 'karim'; list issues."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'webhooks'}),
            Action(name="open_issue", kwargs={'repo': 'webhooks', 'title': 'Toggle not saved', 'body': 'Toggles revert after refresh.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'webhooks', 'number': 1, 'label': 'bug'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'webhooks', 'number': 1, 'username': 'karim'}),
            Action(name="list_issues", kwargs={'repo': 'webhooks'}),
        ],
        outputs=[
            '"label": "bug"',
            '"assignees": ["karim"]',
            '"title": "Toggle not saved"',
        ],
    ),

    # 754
    Task(
        annotator="variation_7",
        user_id="task_754",
        instruction=(
            "You should manage repository 'form-builder' by opening an issue titled 'Rate limit header' with body 'Expose X-RateLimit headers.' labeled 'api' assigned to 'jane'; list issues."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'form-builder'}),
            Action(name="open_issue", kwargs={'repo': 'form-builder', 'title': 'Rate limit header', 'body': 'Expose X-RateLimit headers.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'form-builder', 'number': 1, 'label': 'api'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'form-builder', 'number': 1, 'username': 'jane'}),
            Action(name="list_issues", kwargs={'repo': 'form-builder'}),
        ],
        outputs=[
            '"label": "api"',
            '"assignees": ["jane"]',
            '"title": "Rate limit header"',
        ],
    ),

    # 755
    Task(
        annotator="variation_7",
        user_id="task_755",
        instruction=(
            "You should manage repository 'markdown-viewer' by opening an issue titled 'Add dashboard' with body 'Create Grafana dashboards.' labeled 'observability' assigned to 'sara'; list issues."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'markdown-viewer'}),
            Action(name="open_issue", kwargs={'repo': 'markdown-viewer', 'title': 'Add dashboard', 'body': 'Create Grafana dashboards.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'markdown-viewer', 'number': 1, 'label': 'observability'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'markdown-viewer', 'number': 1, 'username': 'sara'}),
            Action(name="list_issues", kwargs={'repo': 'markdown-viewer'}),
        ],
        outputs=[
            '"label": "observability"',
            '"assignees": ["sara"]',
            '"title": "Add dashboard"',
        ],
    ),

    # 756
    Task(
        annotator="variation_7",
        user_id="task_756",
        instruction=(
            "You should manage repository 'audit-log' by opening an issue titled 'Cold start' with body 'Function cold starts are high.' labeled 'ops' assigned to 'lena'; list issues."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'audit-log'}),
            Action(name="open_issue", kwargs={'repo': 'audit-log', 'title': 'Cold start', 'body': 'Function cold starts are high.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'audit-log', 'number': 1, 'label': 'ops'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'audit-log', 'number': 1, 'username': 'lena'}),
            Action(name="list_issues", kwargs={'repo': 'audit-log'}),
        ],
        outputs=[
            '"label": "ops"',
            '"assignees": ["lena"]',
            '"title": "Cold start"',
        ],
    ),

    # 757
    Task(
        annotator="variation_7",
        user_id="task_757",
        instruction=(
            "You should manage repository 'session-store' by opening an issue titled 'Webhook retry' with body 'Implement exponential backoff.' labeled 'api' assigned to 'mike'; list issues."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'session-store'}),
            Action(name="open_issue", kwargs={'repo': 'session-store', 'title': 'Webhook retry', 'body': 'Implement exponential backoff.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'session-store', 'number': 1, 'label': 'api'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'session-store', 'number': 1, 'username': 'mike'}),
            Action(name="list_issues", kwargs={'repo': 'session-store'}),
        ],
        outputs=[
            '"label": "api"',
            '"assignees": ["mike"]',
            '"title": "Webhook retry"',
        ],
    ),

    # 758
    Task(
        annotator="variation_7",
        user_id="task_758",
        instruction=(
            "You should manage repository 'graphql-gw' by opening an issue titled 'Dark mode toggle' with body 'Add a dark theme switcher.' labeled 'ui' assigned to 'nora'; list issues."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'graphql-gw'}),
            Action(name="open_issue", kwargs={'repo': 'graphql-gw', 'title': 'Dark mode toggle', 'body': 'Add a dark theme switcher.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'graphql-gw', 'number': 1, 'label': 'ui'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'graphql-gw', 'number': 1, 'username': 'nora'}),
            Action(name="list_issues", kwargs={'repo': 'graphql-gw'}),
        ],
        outputs=[
            '"label": "ui"',
            '"assignees": ["nora"]',
            '"title": "Dark mode toggle"',
        ],
    ),

    # 759
    Task(
        annotator="variation_7",
        user_id="task_759",
        instruction=(
            "You should manage repository 'oauth-proxy' by opening an issue titled 'Timezone bug' with body 'Datetime parsing incorrect.' labeled 'bug' assigned to 'sam'; list issues."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'oauth-proxy'}),
            Action(name="open_issue", kwargs={'repo': 'oauth-proxy', 'title': 'Timezone bug', 'body': 'Datetime parsing incorrect.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'repo': 'oauth-proxy', 'number': 1, 'label': 'bug'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'repo': 'oauth-proxy', 'number': 1, 'username': 'sam'}),
            Action(name="list_issues", kwargs={'repo': 'oauth-proxy'}),
        ],
        outputs=[
            '"label": "bug"',
            '"assignees": ["sam"]',
            '"title": "Timezone bug"',
        ],
    ),

    # 760
    Task(
        annotator="variation_7",
        user_id="task_760",
        instruction=(
            "You should ensure repository 'profile-svc' is owned by 'core-team' via transfer; under the new owner open an issue titled 'Deprecate old API' with body 'Plan removal of v1 API.' labeled 'deprecate' assigned to 'nora'; then list issues for owner 'core-team'."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'profile-svc'}),
            Action(name="transfer_repo", kwargs={'repo': 'profile-svc', 'new_owner': 'core-team'}),
            Action(name="open_issue", kwargs={'owner': 'core-team', 'repo': 'profile-svc', 'title': 'Deprecate old API', 'body': 'Plan removal of v1 API.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'owner': 'core-team', 'repo': 'profile-svc', 'number': 1, 'label': 'deprecate'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'owner': 'core-team', 'repo': 'profile-svc', 'number': 1, 'username': 'nora'}),
            Action(name="list_issues", kwargs={'owner': 'core-team', 'repo': 'profile-svc'}),
        ],
        outputs=[
            '"owner": "core-team"',
            '"title": "Deprecate old API"',
            '"label": "deprecate"',
            '"assignees": ["nora"]',
        ],
    ),

    # 761
    Task(
        annotator="variation_7",
        user_id="task_761",
        instruction=(
            "You should ensure repository 'comments-api' is owned by 'edge-team' via transfer; under the new owner open an issue titled 'Purge endpoint' with body 'Add purge endpoint for CDN.' labeled 'ops' assigned to 'amin'; then list issues for owner 'edge-team'."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'comments-api'}),
            Action(name="transfer_repo", kwargs={'repo': 'comments-api', 'new_owner': 'edge-team'}),
            Action(name="open_issue", kwargs={'owner': 'edge-team', 'repo': 'comments-api', 'title': 'Purge endpoint', 'body': 'Add purge endpoint for CDN.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'owner': 'edge-team', 'repo': 'comments-api', 'number': 1, 'label': 'ops'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'owner': 'edge-team', 'repo': 'comments-api', 'number': 1, 'username': 'amin'}),
            Action(name="list_issues", kwargs={'owner': 'edge-team', 'repo': 'comments-api'}),
        ],
        outputs=[
            '"owner": "edge-team"',
            '"title": "Purge endpoint"',
            '"label": "ops"',
            '"assignees": ["amin"]',
        ],
    ),

    # 762
    Task(
        annotator="variation_7",
        user_id="task_762",
        instruction=(
            "You should ensure repository 'notifications' is owned by 'security-team' via transfer; under the new owner open an issue titled 'Rotate keys' with body 'Rotate signing keys regularly.' labeled 'security' assigned to 'ravi'; then list issues for owner 'security-team'."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'notifications'}),
            Action(name="transfer_repo", kwargs={'repo': 'notifications', 'new_owner': 'security-team'}),
            Action(name="open_issue", kwargs={'owner': 'security-team', 'repo': 'notifications', 'title': 'Rotate keys', 'body': 'Rotate signing keys regularly.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'owner': 'security-team', 'repo': 'notifications', 'number': 1, 'label': 'security'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'owner': 'security-team', 'repo': 'notifications', 'number': 1, 'username': 'ravi'}),
            Action(name="list_issues", kwargs={'owner': 'security-team', 'repo': 'notifications'}),
        ],
        outputs=[
            '"owner": "security-team"',
            '"title": "Rotate keys"',
            '"label": "security"',
            '"assignees": ["ravi"]',
        ],
    ),

    # 763
    Task(
        annotator="variation_7",
        user_id="task_763",
        instruction=(
            "You should ensure repository 'realtime-hub' is owned by 'data-team' via transfer; under the new owner open an issue titled 'Partition table' with body 'Partition table by month.' labeled 'infra' assigned to 'sara'; then list issues for owner 'data-team'."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'realtime-hub'}),
            Action(name="transfer_repo", kwargs={'repo': 'realtime-hub', 'new_owner': 'data-team'}),
            Action(name="open_issue", kwargs={'owner': 'data-team', 'repo': 'realtime-hub', 'title': 'Partition table', 'body': 'Partition table by month.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'owner': 'data-team', 'repo': 'realtime-hub', 'number': 1, 'label': 'infra'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'owner': 'data-team', 'repo': 'realtime-hub', 'number': 1, 'username': 'sara'}),
            Action(name="list_issues", kwargs={'owner': 'data-team', 'repo': 'realtime-hub'}),
        ],
        outputs=[
            '"owner": "data-team"',
            '"title": "Partition table"',
            '"label": "infra"',
            '"assignees": ["sara"]',
        ],
    ),

    # 764
    Task(
        annotator="variation_7",
        user_id="task_764",
        instruction=(
            "You should ensure repository 'delta-sync' is owned by 'platform' via transfer; under the new owner open an issue titled 'Feature flags' with body 'Rollout gradual flags.' labeled 'feature' assigned to 'karim'; then list issues for owner 'platform'."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'delta-sync'}),
            Action(name="transfer_repo", kwargs={'repo': 'delta-sync', 'new_owner': 'platform'}),
            Action(name="open_issue", kwargs={'owner': 'platform', 'repo': 'delta-sync', 'title': 'Feature flags', 'body': 'Rollout gradual flags.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'owner': 'platform', 'repo': 'delta-sync', 'number': 1, 'label': 'feature'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'owner': 'platform', 'repo': 'delta-sync', 'number': 1, 'username': 'karim'}),
            Action(name="list_issues", kwargs={'owner': 'platform', 'repo': 'delta-sync'}),
        ],
        outputs=[
            '"owner": "platform"',
            '"title": "Feature flags"',
            '"label": "feature"',
            '"assignees": ["karim"]',
        ],
    ),

    # 765
    Task(
        annotator="variation_7",
        user_id="task_765",
        instruction=(
            "You should ensure repository 'pdf-tool' is owned by 'growth' via transfer; under the new owner open an issue titled 'ETL ownership' with body 'Move ETL jobs here.' labeled 'analytics' assigned to 'sara'; then list issues for owner 'growth'."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'pdf-tool'}),
            Action(name="transfer_repo", kwargs={'repo': 'pdf-tool', 'new_owner': 'growth'}),
            Action(name="open_issue", kwargs={'owner': 'growth', 'repo': 'pdf-tool', 'title': 'ETL ownership', 'body': 'Move ETL jobs here.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'owner': 'growth', 'repo': 'pdf-tool', 'number': 1, 'label': 'analytics'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'owner': 'growth', 'repo': 'pdf-tool', 'number': 1, 'username': 'sara'}),
            Action(name="list_issues", kwargs={'owner': 'growth', 'repo': 'pdf-tool'}),
        ],
        outputs=[
            '"owner": "growth"',
            '"title": "ETL ownership"',
            '"label": "analytics"',
            '"assignees": ["sara"]',
        ],
    ),

    # 766
    Task(
        annotator="variation_7",
        user_id="task_766",
        instruction=(
            "You should ensure repository 'thumbnailer' is owned by 'sre-team' via transfer; under the new owner open an issue titled 'Alert routing' with body 'Route alerts to PagerDuty.' labeled 'ops' assigned to 'omar'; then list issues for owner 'sre-team'."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'thumbnailer'}),
            Action(name="transfer_repo", kwargs={'repo': 'thumbnailer', 'new_owner': 'sre-team'}),
            Action(name="open_issue", kwargs={'owner': 'sre-team', 'repo': 'thumbnailer', 'title': 'Alert routing', 'body': 'Route alerts to PagerDuty.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'owner': 'sre-team', 'repo': 'thumbnailer', 'number': 1, 'label': 'ops'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'owner': 'sre-team', 'repo': 'thumbnailer', 'number': 1, 'username': 'omar'}),
            Action(name="list_issues", kwargs={'owner': 'sre-team', 'repo': 'thumbnailer'}),
        ],
        outputs=[
            '"owner": "sre-team"',
            '"title": "Alert routing"',
            '"label": "ops"',
            '"assignees": ["omar"]',
        ],
    ),

    # 767
    Task(
        annotator="variation_7",
        user_id="task_767",
        instruction=(
            "You should ensure repository 'scheduler-pro' is owned by 'ml-team' via transfer; under the new owner open an issue titled 'Model registry' with body 'Registry for ML models.' labeled 'ml' assigned to 'nora'; then list issues for owner 'ml-team'."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'scheduler-pro'}),
            Action(name="transfer_repo", kwargs={'repo': 'scheduler-pro', 'new_owner': 'ml-team'}),
            Action(name="open_issue", kwargs={'owner': 'ml-team', 'repo': 'scheduler-pro', 'title': 'Model registry', 'body': 'Registry for ML models.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'owner': 'ml-team', 'repo': 'scheduler-pro', 'number': 1, 'label': 'ml'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'owner': 'ml-team', 'repo': 'scheduler-pro', 'number': 1, 'username': 'nora'}),
            Action(name="list_issues", kwargs={'owner': 'ml-team', 'repo': 'scheduler-pro'}),
        ],
        outputs=[
            '"owner": "ml-team"',
            '"title": "Model registry"',
            '"label": "ml"',
            '"assignees": ["nora"]',
        ],
    ),

    # 768
    Task(
        annotator="variation_7",
        user_id="task_768",
        instruction=(
            "You should ensure repository 'event-bus' is owned by 'infra-team' via transfer; under the new owner open an issue titled 'VPC peering' with body 'Establish VPC peering.' labeled 'infra' assigned to 'jane'; then list issues for owner 'infra-team'."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'event-bus'}),
            Action(name="transfer_repo", kwargs={'repo': 'event-bus', 'new_owner': 'infra-team'}),
            Action(name="open_issue", kwargs={'owner': 'infra-team', 'repo': 'event-bus', 'title': 'VPC peering', 'body': 'Establish VPC peering.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'owner': 'infra-team', 'repo': 'event-bus', 'number': 1, 'label': 'infra'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'owner': 'infra-team', 'repo': 'event-bus', 'number': 1, 'username': 'jane'}),
            Action(name="list_issues", kwargs={'owner': 'infra-team', 'repo': 'event-bus'}),
        ],
        outputs=[
            '"owner": "infra-team"',
            '"title": "VPC peering"',
            '"label": "infra"',
            '"assignees": ["jane"]',
        ],
    ),

    # 769
    Task(
        annotator="variation_7",
        user_id="task_769",
        instruction=(
            "You should ensure repository 'payment-ui' is owned by 'ui-team' via transfer; under the new owner open an issue titled 'Icon refresh' with body 'Refresh icon set.' labeled 'ui' assigned to 'lena'; then list issues for owner 'ui-team'."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'payment-ui'}),
            Action(name="transfer_repo", kwargs={'repo': 'payment-ui', 'new_owner': 'ui-team'}),
            Action(name="open_issue", kwargs={'owner': 'ui-team', 'repo': 'payment-ui', 'title': 'Icon refresh', 'body': 'Refresh icon set.'}),
            Action(name="add_label", kwargs={'kind': 'issue', 'owner': 'ui-team', 'repo': 'payment-ui', 'number': 1, 'label': 'ui'}),
            Action(name="assign_user", kwargs={'kind': 'issue', 'owner': 'ui-team', 'repo': 'payment-ui', 'number': 1, 'username': 'lena'}),
            Action(name="list_issues", kwargs={'owner': 'ui-team', 'repo': 'payment-ui'}),
        ],
        outputs=[
            '"owner": "ui-team"',
            '"title": "Icon refresh"',
            '"label": "ui"',
            '"assignees": ["lena"]',
        ],
    ),

    # 770
    Task(
        annotator="variation_7",
        user_id="task_770",
        instruction=(
            "You should maintain repository 'coupon-svc' where branch 'feat-1' has a commit 'feature 1', and a pull request titled 'Feature 1' from 'feat-1' to 'main' is open with label 'ops', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'coupon-svc'}),
            Action(name="create_branch", kwargs={'repo': 'coupon-svc', 'branch': 'feat-1'}),
            Action(name="add_commit", kwargs={'repo': 'coupon-svc', 'branch': 'feat-1', 'message': 'feature 1'}),
            Action(name="open_pr", kwargs={'repo': 'coupon-svc', 'head_branch': 'feat-1', 'base_branch': 'main', 'title': 'Feature 1'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'coupon-svc', 'number': 1, 'label': 'ops'}),
            Action(name="close_pr", kwargs={'repo': 'coupon-svc', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'coupon-svc', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'coupon-svc', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ops"',
            '"title": "Feature 1"',
            '"state": "open"',
        ],
    ),

    # 771
    Task(
        annotator="variation_7",
        user_id="task_771",
        instruction=(
            "You should maintain repository 'shipping-svc' where branch 'feat-2' has a commit 'feature 2', and a pull request titled 'Feature 2' from 'feat-2' to 'main' is open with label 'security', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'shipping-svc'}),
            Action(name="create_branch", kwargs={'repo': 'shipping-svc', 'branch': 'feat-2'}),
            Action(name="add_commit", kwargs={'repo': 'shipping-svc', 'branch': 'feat-2', 'message': 'feature 2'}),
            Action(name="open_pr", kwargs={'repo': 'shipping-svc', 'head_branch': 'feat-2', 'base_branch': 'main', 'title': 'Feature 2'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'shipping-svc', 'number': 1, 'label': 'security'}),
            Action(name="close_pr", kwargs={'repo': 'shipping-svc', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'shipping-svc', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'shipping-svc', 'state': 'open'}),
        ],
        outputs=[
            '"label": "security"',
            '"title": "Feature 2"',
            '"state": "open"',
        ],
    ),

    # 772
    Task(
        annotator="variation_7",
        user_id="task_772",
        instruction=(
            "You should maintain repository 'catalog-api' where branch 'feat-3' has a commit 'feature 3', and a pull request titled 'Feature 3' from 'feat-3' to 'main' is open with label 'infra', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'catalog-api'}),
            Action(name="create_branch", kwargs={'repo': 'catalog-api', 'branch': 'feat-3'}),
            Action(name="add_commit", kwargs={'repo': 'catalog-api', 'branch': 'feat-3', 'message': 'feature 3'}),
            Action(name="open_pr", kwargs={'repo': 'catalog-api', 'head_branch': 'feat-3', 'base_branch': 'main', 'title': 'Feature 3'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'catalog-api', 'number': 1, 'label': 'infra'}),
            Action(name="close_pr", kwargs={'repo': 'catalog-api', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'catalog-api', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'catalog-api', 'state': 'open'}),
        ],
        outputs=[
            '"label": "infra"',
            '"title": "Feature 3"',
            '"state": "open"',
        ],
    ),

    # 773
    Task(
        annotator="variation_7",
        user_id="task_773",
        instruction=(
            "You should maintain repository 'inventory-svc' where branch 'feat-4' has a commit 'feature 4', and a pull request titled 'Feature 4' from 'feat-4' to 'main' is open with label 'seo', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'inventory-svc'}),
            Action(name="create_branch", kwargs={'repo': 'inventory-svc', 'branch': 'feat-4'}),
            Action(name="add_commit", kwargs={'repo': 'inventory-svc', 'branch': 'feat-4', 'message': 'feature 4'}),
            Action(name="open_pr", kwargs={'repo': 'inventory-svc', 'head_branch': 'feat-4', 'base_branch': 'main', 'title': 'Feature 4'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'inventory-svc', 'number': 1, 'label': 'seo'}),
            Action(name="close_pr", kwargs={'repo': 'inventory-svc', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'inventory-svc', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'inventory-svc', 'state': 'open'}),
        ],
        outputs=[
            '"label": "seo"',
            '"title": "Feature 4"',
            '"state": "open"',
        ],
    ),

    # 774
    Task(
        annotator="variation_7",
        user_id="task_774",
        instruction=(
            "You should maintain repository 'recommendation' where branch 'feat-5' has a commit 'feature 5', and a pull request titled 'Feature 5' from 'feat-5' to 'main' is open with label 'ui', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'recommendation'}),
            Action(name="create_branch", kwargs={'repo': 'recommendation', 'branch': 'feat-5'}),
            Action(name="add_commit", kwargs={'repo': 'recommendation', 'branch': 'feat-5', 'message': 'feature 5'}),
            Action(name="open_pr", kwargs={'repo': 'recommendation', 'head_branch': 'feat-5', 'base_branch': 'main', 'title': 'Feature 5'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'recommendation', 'number': 1, 'label': 'ui'}),
            Action(name="close_pr", kwargs={'repo': 'recommendation', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'recommendation', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'recommendation', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ui"',
            '"title": "Feature 5"',
            '"state": "open"',
        ],
    ),

    # 775
    Task(
        annotator="variation_7",
        user_id="task_775",
        instruction=(
            "You should maintain repository 'ab-testing' where branch 'feat-6' has a commit 'feature 6', and a pull request titled 'Feature 6' from 'feat-6' to 'main' is open with label 'docs', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'ab-testing'}),
            Action(name="create_branch", kwargs={'repo': 'ab-testing', 'branch': 'feat-6'}),
            Action(name="add_commit", kwargs={'repo': 'ab-testing', 'branch': 'feat-6', 'message': 'feature 6'}),
            Action(name="open_pr", kwargs={'repo': 'ab-testing', 'head_branch': 'feat-6', 'base_branch': 'main', 'title': 'Feature 6'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'ab-testing', 'number': 1, 'label': 'docs'}),
            Action(name="close_pr", kwargs={'repo': 'ab-testing', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'ab-testing', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'ab-testing', 'state': 'open'}),
        ],
        outputs=[
            '"label": "docs"',
            '"title": "Feature 6"',
            '"state": "open"',
        ],
    ),

    # 776
    Task(
        annotator="variation_7",
        user_id="task_776",
        instruction=(
            "You should maintain repository 'experiments' where branch 'feat-7' has a commit 'feature 7', and a pull request titled 'Feature 7' from 'feat-7' to 'main' is open with label 'feature', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'experiments'}),
            Action(name="create_branch", kwargs={'repo': 'experiments', 'branch': 'feat-7'}),
            Action(name="add_commit", kwargs={'repo': 'experiments', 'branch': 'feat-7', 'message': 'feature 7'}),
            Action(name="open_pr", kwargs={'repo': 'experiments', 'head_branch': 'feat-7', 'base_branch': 'main', 'title': 'Feature 7'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'experiments', 'number': 1, 'label': 'feature'}),
            Action(name="close_pr", kwargs={'repo': 'experiments', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'experiments', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'experiments', 'state': 'open'}),
        ],
        outputs=[
            '"label": "feature"',
            '"title": "Feature 7"',
            '"state": "open"',
        ],
    ),

    # 777
    Task(
        annotator="variation_7",
        user_id="task_777",
        instruction=(
            "You should maintain repository 'feature-gates' where branch 'feat-8' has a commit 'feature 8', and a pull request titled 'Feature 8' from 'feat-8' to 'main' is open with label 'api', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'feature-gates'}),
            Action(name="create_branch", kwargs={'repo': 'feature-gates', 'branch': 'feat-8'}),
            Action(name="add_commit", kwargs={'repo': 'feature-gates', 'branch': 'feat-8', 'message': 'feature 8'}),
            Action(name="open_pr", kwargs={'repo': 'feature-gates', 'head_branch': 'feat-8', 'base_branch': 'main', 'title': 'Feature 8'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'feature-gates', 'number': 1, 'label': 'api'}),
            Action(name="close_pr", kwargs={'repo': 'feature-gates', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'feature-gates', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'feature-gates', 'state': 'open'}),
        ],
        outputs=[
            '"label": "api"',
            '"title": "Feature 8"',
            '"state": "open"',
        ],
    ),

    # 778
    Task(
        annotator="variation_7",
        user_id="task_778",
        instruction=(
            "You should maintain repository 'content-api' where branch 'feat-9' has a commit 'feature 9', and a pull request titled 'Feature 9' from 'feat-9' to 'main' is open with label 'ops', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'content-api'}),
            Action(name="create_branch", kwargs={'repo': 'content-api', 'branch': 'feat-9'}),
            Action(name="add_commit", kwargs={'repo': 'content-api', 'branch': 'feat-9', 'message': 'feature 9'}),
            Action(name="open_pr", kwargs={'repo': 'content-api', 'head_branch': 'feat-9', 'base_branch': 'main', 'title': 'Feature 9'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'content-api', 'number': 1, 'label': 'ops'}),
            Action(name="close_pr", kwargs={'repo': 'content-api', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'content-api', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'content-api', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ops"',
            '"title": "Feature 9"',
            '"state": "open"',
        ],
    ),

    # 779
    Task(
        annotator="variation_7",
        user_id="task_779",
        instruction=(
            "You should maintain repository 'feed-svc' where branch 'feat-10' has a commit 'feature 10', and a pull request titled 'Feature 10' from 'feat-10' to 'main' is open with label 'security', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'feed-svc'}),
            Action(name="create_branch", kwargs={'repo': 'feed-svc', 'branch': 'feat-10'}),
            Action(name="add_commit", kwargs={'repo': 'feed-svc', 'branch': 'feat-10', 'message': 'feature 10'}),
            Action(name="open_pr", kwargs={'repo': 'feed-svc', 'head_branch': 'feat-10', 'base_branch': 'main', 'title': 'Feature 10'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'feed-svc', 'number': 1, 'label': 'security'}),
            Action(name="close_pr", kwargs={'repo': 'feed-svc', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'feed-svc', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'feed-svc', 'state': 'open'}),
        ],
        outputs=[
            '"label": "security"',
            '"title": "Feature 10"',
            '"state": "open"',
        ],
    ),

    # 780
    Task(
        annotator="variation_7",
        user_id="task_780",
        instruction=(
            "You should maintain repository 'media-cdn' where branch 'feat-11' has a commit 'feature 11', and a pull request titled 'Feature 11' from 'feat-11' to 'main' is open with label 'infra', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'media-cdn'}),
            Action(name="create_branch", kwargs={'repo': 'media-cdn', 'branch': 'feat-11'}),
            Action(name="add_commit", kwargs={'repo': 'media-cdn', 'branch': 'feat-11', 'message': 'feature 11'}),
            Action(name="open_pr", kwargs={'repo': 'media-cdn', 'head_branch': 'feat-11', 'base_branch': 'main', 'title': 'Feature 11'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'media-cdn', 'number': 1, 'label': 'infra'}),
            Action(name="close_pr", kwargs={'repo': 'media-cdn', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'media-cdn', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'media-cdn', 'state': 'open'}),
        ],
        outputs=[
            '"label": "infra"',
            '"title": "Feature 11"',
            '"state": "open"',
        ],
    ),

    # 781
    Task(
        annotator="variation_7",
        user_id="task_781",
        instruction=(
            "You should maintain repository 'avatar-gen' where branch 'feat-12' has a commit 'feature 12', and a pull request titled 'Feature 12' from 'feat-12' to 'main' is open with label 'seo', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'avatar-gen'}),
            Action(name="create_branch", kwargs={'repo': 'avatar-gen', 'branch': 'feat-12'}),
            Action(name="add_commit", kwargs={'repo': 'avatar-gen', 'branch': 'feat-12', 'message': 'feature 12'}),
            Action(name="open_pr", kwargs={'repo': 'avatar-gen', 'head_branch': 'feat-12', 'base_branch': 'main', 'title': 'Feature 12'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'avatar-gen', 'number': 1, 'label': 'seo'}),
            Action(name="close_pr", kwargs={'repo': 'avatar-gen', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'avatar-gen', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'avatar-gen', 'state': 'open'}),
        ],
        outputs=[
            '"label": "seo"',
            '"title": "Feature 12"',
            '"state": "open"',
        ],
    ),

    # 782
    Task(
        annotator="variation_7",
        user_id="task_782",
        instruction=(
            "You should maintain repository 'geo-routing' where branch 'feat-13' has a commit 'feature 13', and a pull request titled 'Feature 13' from 'feat-13' to 'main' is open with label 'ui', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'geo-routing'}),
            Action(name="create_branch", kwargs={'repo': 'geo-routing', 'branch': 'feat-13'}),
            Action(name="add_commit", kwargs={'repo': 'geo-routing', 'branch': 'feat-13', 'message': 'feature 13'}),
            Action(name="open_pr", kwargs={'repo': 'geo-routing', 'head_branch': 'feat-13', 'base_branch': 'main', 'title': 'Feature 13'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'geo-routing', 'number': 1, 'label': 'ui'}),
            Action(name="close_pr", kwargs={'repo': 'geo-routing', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'geo-routing', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'geo-routing', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ui"',
            '"title": "Feature 13"',
            '"state": "open"',
        ],
    ),

    # 783
    Task(
        annotator="variation_7",
        user_id="task_783",
        instruction=(
            "You should maintain repository 'fraud-detect' where branch 'feat-14' has a commit 'feature 14', and a pull request titled 'Feature 14' from 'feat-14' to 'main' is open with label 'docs', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'fraud-detect'}),
            Action(name="create_branch", kwargs={'repo': 'fraud-detect', 'branch': 'feat-14'}),
            Action(name="add_commit", kwargs={'repo': 'fraud-detect', 'branch': 'feat-14', 'message': 'feature 14'}),
            Action(name="open_pr", kwargs={'repo': 'fraud-detect', 'head_branch': 'feat-14', 'base_branch': 'main', 'title': 'Feature 14'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'fraud-detect', 'number': 1, 'label': 'docs'}),
            Action(name="close_pr", kwargs={'repo': 'fraud-detect', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'fraud-detect', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'fraud-detect', 'state': 'open'}),
        ],
        outputs=[
            '"label": "docs"',
            '"title": "Feature 14"',
            '"state": "open"',
        ],
    ),

    # 784
    Task(
        annotator="variation_7",
        user_id="task_784",
        instruction=(
            "You should maintain repository 'vector-search' where branch 'feat-15' has a commit 'feature 15', and a pull request titled 'Feature 15' from 'feat-15' to 'main' is open with label 'feature', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'vector-search'}),
            Action(name="create_branch", kwargs={'repo': 'vector-search', 'branch': 'feat-15'}),
            Action(name="add_commit", kwargs={'repo': 'vector-search', 'branch': 'feat-15', 'message': 'feature 15'}),
            Action(name="open_pr", kwargs={'repo': 'vector-search', 'head_branch': 'feat-15', 'base_branch': 'main', 'title': 'Feature 15'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'vector-search', 'number': 1, 'label': 'feature'}),
            Action(name="close_pr", kwargs={'repo': 'vector-search', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'vector-search', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'vector-search', 'state': 'open'}),
        ],
        outputs=[
            '"label": "feature"',
            '"title": "Feature 15"',
            '"state": "open"',
        ],
    ),

    # 785
    Task(
        annotator="variation_7",
        user_id="task_785",
        instruction=(
            "You should maintain repository 'sso-portal' where branch 'feat-16' has a commit 'feature 16', and a pull request titled 'Feature 16' from 'feat-16' to 'main' is open with label 'api', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'sso-portal'}),
            Action(name="create_branch", kwargs={'repo': 'sso-portal', 'branch': 'feat-16'}),
            Action(name="add_commit", kwargs={'repo': 'sso-portal', 'branch': 'feat-16', 'message': 'feature 16'}),
            Action(name="open_pr", kwargs={'repo': 'sso-portal', 'head_branch': 'feat-16', 'base_branch': 'main', 'title': 'Feature 16'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'sso-portal', 'number': 1, 'label': 'api'}),
            Action(name="close_pr", kwargs={'repo': 'sso-portal', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'sso-portal', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'sso-portal', 'state': 'open'}),
        ],
        outputs=[
            '"label": "api"',
            '"title": "Feature 16"',
            '"state": "open"',
        ],
    ),

    # 786
    Task(
        annotator="variation_7",
        user_id="task_786",
        instruction=(
            "You should maintain repository 'tenant-admin' where branch 'feat-17' has a commit 'feature 17', and a pull request titled 'Feature 17' from 'feat-17' to 'main' is open with label 'ops', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'tenant-admin'}),
            Action(name="create_branch", kwargs={'repo': 'tenant-admin', 'branch': 'feat-17'}),
            Action(name="add_commit", kwargs={'repo': 'tenant-admin', 'branch': 'feat-17', 'message': 'feature 17'}),
            Action(name="open_pr", kwargs={'repo': 'tenant-admin', 'head_branch': 'feat-17', 'base_branch': 'main', 'title': 'Feature 17'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'tenant-admin', 'number': 1, 'label': 'ops'}),
            Action(name="close_pr", kwargs={'repo': 'tenant-admin', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'tenant-admin', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'tenant-admin', 'state': 'open'}),
        ],
        outputs=[
            '"label": "ops"',
            '"title": "Feature 17"',
            '"state": "open"',
        ],
    ),

    # 787
    Task(
        annotator="variation_7",
        user_id="task_787",
        instruction=(
            "You should maintain repository 'workspace-api' where branch 'feat-18' has a commit 'feature 18', and a pull request titled 'Feature 18' from 'feat-18' to 'main' is open with label 'security', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'workspace-api'}),
            Action(name="create_branch", kwargs={'repo': 'workspace-api', 'branch': 'feat-18'}),
            Action(name="add_commit", kwargs={'repo': 'workspace-api', 'branch': 'feat-18', 'message': 'feature 18'}),
            Action(name="open_pr", kwargs={'repo': 'workspace-api', 'head_branch': 'feat-18', 'base_branch': 'main', 'title': 'Feature 18'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'workspace-api', 'number': 1, 'label': 'security'}),
            Action(name="close_pr", kwargs={'repo': 'workspace-api', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'workspace-api', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'workspace-api', 'state': 'open'}),
        ],
        outputs=[
            '"label": "security"',
            '"title": "Feature 18"',
            '"state": "open"',
        ],
    ),

    # 788
    Task(
        annotator="variation_7",
        user_id="task_788",
        instruction=(
            "You should maintain repository 'notes-app' where branch 'feat-19' has a commit 'feature 19', and a pull request titled 'Feature 19' from 'feat-19' to 'main' is open with label 'infra', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'notes-app'}),
            Action(name="create_branch", kwargs={'repo': 'notes-app', 'branch': 'feat-19'}),
            Action(name="add_commit", kwargs={'repo': 'notes-app', 'branch': 'feat-19', 'message': 'feature 19'}),
            Action(name="open_pr", kwargs={'repo': 'notes-app', 'head_branch': 'feat-19', 'base_branch': 'main', 'title': 'Feature 19'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'notes-app', 'number': 1, 'label': 'infra'}),
            Action(name="close_pr", kwargs={'repo': 'notes-app', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'notes-app', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'notes-app', 'state': 'open'}),
        ],
        outputs=[
            '"label": "infra"',
            '"title": "Feature 19"',
            '"state": "open"',
        ],
    ),

    # 789
    Task(
        annotator="variation_7",
        user_id="task_789",
        instruction=(
            "You should maintain repository 'doc-editor' where branch 'feat-20' has a commit 'feature 20', and a pull request titled 'Feature 20' from 'feat-20' to 'main' is open with label 'seo', after being closed and reopened; list open PRs."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'doc-editor'}),
            Action(name="create_branch", kwargs={'repo': 'doc-editor', 'branch': 'feat-20'}),
            Action(name="add_commit", kwargs={'repo': 'doc-editor', 'branch': 'feat-20', 'message': 'feature 20'}),
            Action(name="open_pr", kwargs={'repo': 'doc-editor', 'head_branch': 'feat-20', 'base_branch': 'main', 'title': 'Feature 20'}),
            Action(name="add_label", kwargs={'kind': 'pr', 'repo': 'doc-editor', 'number': 1, 'label': 'seo'}),
            Action(name="close_pr", kwargs={'repo': 'doc-editor', 'number': 1}),
            Action(name="reopen_pr", kwargs={'repo': 'doc-editor', 'number': 1}),
            Action(name="list_prs", kwargs={'repo': 'doc-editor', 'state': 'open'}),
        ],
        outputs=[
            '"label": "seo"',
            '"title": "Feature 20"',
            '"state": "open"',
        ],
    ),

    # 790
    Task(
        annotator="variation_7",
        user_id="task_790",
        instruction=(
            "You should create a repository 'renderer' with topics ['ui', 'components'], add commit 'init topics' and commit 'readme', and list branches to show 'main' exists."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'renderer'}),
            Action(name="repo_topics", kwargs={'repo': 'renderer', 'topics': ['ui', 'components']}),
            Action(name="add_commit", kwargs={'repo': 'renderer', 'message': 'init topics'}),
            Action(name="add_commit", kwargs={'repo': 'renderer', 'message': 'readme'}),
            Action(name="list_branches", kwargs={'repo': 'renderer'}),
        ],
        outputs=[
            '"topics": ["ui", "components"]',
            '"branches": ["main"]',
        ],
    ),

    # 791
    Task(
        annotator="variation_7",
        user_id="task_791",
        instruction=(
            "You should create a repository 'state-store' with topics ['cli', 'tools'], add commit 'init topics' and commit 'readme', and list branches to show 'main' exists."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'state-store'}),
            Action(name="repo_topics", kwargs={'repo': 'state-store', 'topics': ['cli', 'tools']}),
            Action(name="add_commit", kwargs={'repo': 'state-store', 'message': 'init topics'}),
            Action(name="add_commit", kwargs={'repo': 'state-store', 'message': 'readme'}),
            Action(name="list_branches", kwargs={'repo': 'state-store'}),
        ],
        outputs=[
            '"topics": ["cli", "tools"]',
            '"branches": ["main"]',
        ],
    ),

    # 792
    Task(
        annotator="variation_7",
        user_id="task_792",
        instruction=(
            "You should create a repository 'odata-gw' with topics ['security', 'auth'], add commit 'init topics' and commit 'readme', and list branches to show 'main' exists."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'odata-gw'}),
            Action(name="repo_topics", kwargs={'repo': 'odata-gw', 'topics': ['security', 'auth']}),
            Action(name="add_commit", kwargs={'repo': 'odata-gw', 'message': 'init topics'}),
            Action(name="add_commit", kwargs={'repo': 'odata-gw', 'message': 'readme'}),
            Action(name="list_branches", kwargs={'repo': 'odata-gw'}),
        ],
        outputs=[
            '"topics": ["security", "auth"]',
            '"branches": ["main"]',
        ],
    ),

    # 793
    Task(
        annotator="variation_7",
        user_id="task_793",
        instruction=(
            "You should create a repository 'image-filter' with topics ['data', 'etl'], add commit 'init topics' and commit 'readme', and list branches to show 'main' exists."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'image-filter'}),
            Action(name="repo_topics", kwargs={'repo': 'image-filter', 'topics': ['data', 'etl']}),
            Action(name="add_commit", kwargs={'repo': 'image-filter', 'message': 'init topics'}),
            Action(name="add_commit", kwargs={'repo': 'image-filter', 'message': 'readme'}),
            Action(name="list_branches", kwargs={'repo': 'image-filter'}),
        ],
        outputs=[
            '"topics": ["data", "etl"]',
            '"branches": ["main"]',
        ],
    ),

    # 794
    Task(
        annotator="variation_7",
        user_id="task_794",
        instruction=(
            "You should create a repository 'push-gw' with topics ['ops', 'cron'], add commit 'init topics' and commit 'readme', and list branches to show 'main' exists."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'push-gw'}),
            Action(name="repo_topics", kwargs={'repo': 'push-gw', 'topics': ['ops', 'cron']}),
            Action(name="add_commit", kwargs={'repo': 'push-gw', 'message': 'init topics'}),
            Action(name="add_commit", kwargs={'repo': 'push-gw', 'message': 'readme'}),
            Action(name="list_branches", kwargs={'repo': 'push-gw'}),
        ],
        outputs=[
            '"topics": ["ops", "cron"]',
            '"branches": ["main"]',
        ],
    ),

    # 795
    Task(
        annotator="variation_7",
        user_id="task_795",
        instruction=(
            "You should create a repository 'sync-agent' with topics ['api', 'gateway'], add commit 'init topics' and commit 'readme', and list branches to show 'main' exists."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'sync-agent'}),
            Action(name="repo_topics", kwargs={'repo': 'sync-agent', 'topics': ['api', 'gateway']}),
            Action(name="add_commit", kwargs={'repo': 'sync-agent', 'message': 'init topics'}),
            Action(name="add_commit", kwargs={'repo': 'sync-agent', 'message': 'readme'}),
            Action(name="list_branches", kwargs={'repo': 'sync-agent'}),
        ],
        outputs=[
            '"topics": ["api", "gateway"]',
            '"branches": ["main"]',
        ],
    ),

    # 796
    Task(
        annotator="variation_7",
        user_id="task_796",
        instruction=(
            "You should create a repository 'idp-core' with topics ['ml', 'models'], add commit 'init topics' and commit 'readme', and list branches to show 'main' exists."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'idp-core'}),
            Action(name="repo_topics", kwargs={'repo': 'idp-core', 'topics': ['ml', 'models']}),
            Action(name="add_commit", kwargs={'repo': 'idp-core', 'message': 'init topics'}),
            Action(name="add_commit", kwargs={'repo': 'idp-core', 'message': 'readme'}),
            Action(name="list_branches", kwargs={'repo': 'idp-core'}),
        ],
        outputs=[
            '"topics": ["ml", "models"]',
            '"branches": ["main"]',
        ],
    ),

    # 797
    Task(
        annotator="variation_7",
        user_id="task_797",
        instruction=(
            "You should create a repository 'policy-svc' with topics ['search', 'index'], add commit 'init topics' and commit 'readme', and list branches to show 'main' exists."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'policy-svc'}),
            Action(name="repo_topics", kwargs={'repo': 'policy-svc', 'topics': ['search', 'index']}),
            Action(name="add_commit", kwargs={'repo': 'policy-svc', 'message': 'init topics'}),
            Action(name="add_commit", kwargs={'repo': 'policy-svc', 'message': 'readme'}),
            Action(name="list_branches", kwargs={'repo': 'policy-svc'}),
        ],
        outputs=[
            '"topics": ["search", "index"]',
            '"branches": ["main"]',
        ],
    ),

    # 798
    Task(
        annotator="variation_7",
        user_id="task_798",
        instruction=(
            "You should create a repository 'usage-collector' with topics ['media', 'cdn'], add commit 'init topics' and commit 'readme', and list branches to show 'main' exists."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'usage-collector'}),
            Action(name="repo_topics", kwargs={'repo': 'usage-collector', 'topics': ['media', 'cdn']}),
            Action(name="add_commit", kwargs={'repo': 'usage-collector', 'message': 'init topics'}),
            Action(name="add_commit", kwargs={'repo': 'usage-collector', 'message': 'readme'}),
            Action(name="list_branches", kwargs={'repo': 'usage-collector'}),
        ],
        outputs=[
            '"topics": ["media", "cdn"]',
            '"branches": ["main"]',
        ],
    ),

    # 799
    Task(
        annotator="variation_7",
        user_id="task_799",
        instruction=(
            "You should create a repository 'query-planner' with topics ['geo', 'routing'], add commit 'init topics' and commit 'readme', and list branches to show 'main' exists."
        ),
        actions=[
            Action(name="create_repo", kwargs={'name': 'query-planner'}),
            Action(name="repo_topics", kwargs={'repo': 'query-planner', 'topics': ['geo', 'routing']}),
            Action(name="add_commit", kwargs={'repo': 'query-planner', 'message': 'init topics'}),
            Action(name="add_commit", kwargs={'repo': 'query-planner', 'message': 'readme'}),
            Action(name="list_branches", kwargs={'repo': 'query-planner'}),
        ],
        outputs=[
            '"topics": ["geo", "routing"]',
            '"branches": ["main"]',
        ],
    ),
]
