from tau_bench.types import Action, Task

TASKS = [
    # 700
    Task(
        annotator="variation_7",
        user_id="task_700",
    instruction=(
        "Handle repository 'blog-lite' to ensure that a pull request is open from branch 'feature-home' to 'main', with the label 'docs' attached. Once this condition is fulfilled, list the open pull requests for 'blog-lite'."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'blog-lite'}),
            Action(name="CreateBranch", kwargs={'repo': 'blog-lite', 'branch': 'feature-home'}),
            Action(name="AddCommit", kwargs={'repo': 'blog-lite', 'branch': 'feature-home', 'message': 'setup index'}),
            Action(name="OpenPr", kwargs={'repo': 'blog-lite', 'head_branch': 'feature-home', 'base_branch': 'main', 'title': 'Home section'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'blog-lite', 'number': 1, 'label': 'docs'}),
            Action(name="ListPrs", kwargs={'repo': 'blog-lite', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 701
    Task(
        annotator="variation_7",
        user_id="task_701",
    instruction=(
        "Coordinate the repository 'support-bot' such that branch 'resize' contains a commit 'add resize', and a pull request titled 'Resize feature' is open from 'resize' to 'main' with the label 'feature'. Afterward, list the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'support-bot'}),
            Action(name="CreateBranch", kwargs={'repo': 'support-bot', 'branch': 'resize'}),
            Action(name="AddCommit", kwargs={'repo': 'support-bot', 'branch': 'resize', 'message': 'add resize'}),
            Action(name="OpenPr", kwargs={'repo': 'support-bot', 'head_branch': 'resize', 'base_branch': 'main', 'title': 'Resize feature'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'support-bot', 'number': 1, 'label': 'feature'}),
            Action(name="ListPrs", kwargs={'repo': 'support-bot', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 702
    Task(
        annotator="variation_7",
        user_id="task_702",
    instruction=(
        "Ensure the repository 'img-tool' comprises a branch 'readme' with a commit 'write readme'. There should be an open pull request titled 'README' from 'readme' to 'main' with the label 'api'. After confirming this, list all open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'img-tool'}),
            Action(name="CreateBranch", kwargs={'repo': 'img-tool', 'branch': 'readme'}),
            Action(name="AddCommit", kwargs={'repo': 'img-tool', 'branch': 'readme', 'message': 'write readme'}),
            Action(name="OpenPr", kwargs={'repo': 'img-tool', 'head_branch': 'readme', 'base_branch': 'main', 'title': 'README'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'img-tool', 'number': 1, 'label': 'api'}),
            Action(name="ListPrs", kwargs={'repo': 'img-tool', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 703
    Task(
        annotator="variation_7",
        user_id="task_703",
    instruction=(
        "Verify that the repository 'calc-pro' features an open pull request from branch 'daily-cron' to 'main', marked with the label 'ops'. Once this condition is met, proceed to list the open pull requests for 'calc-pro'."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'calc-pro'}),
            Action(name="CreateBranch", kwargs={'repo': 'calc-pro', 'branch': 'daily-cron'}),
            Action(name="AddCommit", kwargs={'repo': 'calc-pro', 'branch': 'daily-cron', 'message': 'cron impl'}),
            Action(name="OpenPr", kwargs={'repo': 'calc-pro', 'head_branch': 'daily-cron', 'base_branch': 'main', 'title': 'Cron jobs'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'calc-pro', 'number': 1, 'label': 'ops'}),
            Action(name="ListPrs", kwargs={'repo': 'calc-pro', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 704
    Task(
        annotator="variation_7",
        user_id="task_704",
    instruction=(
        "Handle the maintenance of the repository 'docs-kit' with a branch 'badges' containing a commit 'README badges', ensuring there is a pull request titled 'README badges' from 'badges' to 'main' that is open with the label 'security'; provide a list of open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'docs-kit'}),
            Action(name="CreateBranch", kwargs={'repo': 'docs-kit', 'branch': 'badges'}),
            Action(name="AddCommit", kwargs={'repo': 'docs-kit', 'branch': 'badges', 'message': 'README badges'}),
            Action(name="OpenPr", kwargs={'repo': 'docs-kit', 'head_branch': 'badges', 'base_branch': 'main', 'title': 'README badges'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'docs-kit', 'number': 1, 'label': 'security'}),
            Action(name="ListPrs", kwargs={'repo': 'docs-kit', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 705
    Task(
        annotator="variation_7",
        user_id="task_705",
    instruction=(
        "Coordinate the maintenance of the repository 'portal-ui' where the branch 'theme' includes a commit 'dark theme', and there is a pull request titled 'Dark theme' from 'theme' to 'main' open with the label 'infra'; supply a list of open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'portal-ui'}),
            Action(name="CreateBranch", kwargs={'repo': 'portal-ui', 'branch': 'theme'}),
            Action(name="AddCommit", kwargs={'repo': 'portal-ui', 'branch': 'theme', 'message': 'dark theme'}),
            Action(name="OpenPr", kwargs={'repo': 'portal-ui', 'head_branch': 'theme', 'base_branch': 'main', 'title': 'Dark theme'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'portal-ui', 'number': 1, 'label': 'infra'}),
            Action(name="ListPrs", kwargs={'repo': 'portal-ui', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 706
    Task(
        annotator="variation_7",
        user_id="task_706",
    instruction=(
        "Handle the repository 'backup-tool' where the branch 'index-v2' includes a commit labeled 'add indexer', and a pull request titled 'Indexer v2' from 'index-v2' to 'main' is currently open with the label 'seo'; enumerate the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'backup-tool'}),
            Action(name="CreateBranch", kwargs={'repo': 'backup-tool', 'branch': 'index-v2'}),
            Action(name="AddCommit", kwargs={'repo': 'backup-tool', 'branch': 'index-v2', 'message': 'add indexer'}),
            Action(name="OpenPr", kwargs={'repo': 'backup-tool', 'head_branch': 'index-v2', 'base_branch': 'main', 'title': 'Indexer v2'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'backup-tool', 'number': 1, 'label': 'seo'}),
            Action(name="ListPrs", kwargs={'repo': 'backup-tool', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 707
    Task(
        annotator="variation_7",
        user_id="task_707",
    instruction=(
        "Manage the repository 'pkg-index' where the branch 'smtp' contains a commit called 'smtp auth', and a pull request titled 'SMTP auth' from 'smtp' to 'main' is presently open, marked with the label 'ui'; list the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'pkg-index'}),
            Action(name="CreateBranch", kwargs={'repo': 'pkg-index', 'branch': 'smtp'}),
            Action(name="AddCommit", kwargs={'repo': 'pkg-index', 'branch': 'smtp', 'message': 'smtp auth'}),
            Action(name="OpenPr", kwargs={'repo': 'pkg-index', 'head_branch': 'smtp', 'base_branch': 'main', 'title': 'SMTP auth'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'pkg-index', 'number': 1, 'label': 'ui'}),
            Action(name="ListPrs", kwargs={'repo': 'pkg-index', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 708
    Task(
        annotator="variation_7",
        user_id="task_708",
    instruction=(
        "Handle the repository 'core-lib' ensuring the branch 'landing' includes a commit 'hero copy', and the pull request named 'Landing page' from 'landing' to 'main' remains open with the label 'docs'; enumerate open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'core-lib'}),
            Action(name="CreateBranch", kwargs={'repo': 'core-lib', 'branch': 'landing'}),
            Action(name="AddCommit", kwargs={'repo': 'core-lib', 'branch': 'landing', 'message': 'hero copy'}),
            Action(name="OpenPr", kwargs={'repo': 'core-lib', 'head_branch': 'landing', 'base_branch': 'main', 'title': 'Landing page'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'core-lib', 'number': 1, 'label': 'docs'}),
            Action(name="ListPrs", kwargs={'repo': 'core-lib', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 709
    Task(
        annotator="variation_7",
        user_id="task_709",
    instruction=(
        "Coordinate the maintenance of repository 'data-cleaner' where the branch 'tax' contains the commit 'add vat', and ensure that the pull request titled 'VAT support' from 'tax' to 'main' is open with the label 'feature'; enumerate open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'data-cleaner'}),
            Action(name="CreateBranch", kwargs={'repo': 'data-cleaner', 'branch': 'tax'}),
            Action(name="AddCommit", kwargs={'repo': 'data-cleaner', 'branch': 'tax', 'message': 'add vat'}),
            Action(name="OpenPr", kwargs={'repo': 'data-cleaner', 'head_branch': 'tax', 'base_branch': 'main', 'title': 'VAT support'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'data-cleaner', 'number': 1, 'label': 'feature'}),
            Action(name="ListPrs", kwargs={'repo': 'data-cleaner', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 710
    Task(
        annotator="variation_7",
        user_id="task_710",
    instruction=(
        "Handle repository 'docs-kit-plus' to ensure it's in the following condition: branch 'sitemap' contains a commit 'gen sitemap'; an open pull request titled 'Sitemap' is present from 'sitemap' to 'main' with label 'api'. Then, provide the list of open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'docs-kit-plus'}),
            Action(name="CreateBranch", kwargs={'repo': 'docs-kit-plus', 'branch': 'sitemap'}),
            Action(name="AddCommit", kwargs={'repo': 'docs-kit-plus', 'branch': 'sitemap', 'message': 'gen sitemap'}),
            Action(name="OpenPr", kwargs={'repo': 'docs-kit-plus', 'head_branch': 'sitemap', 'base_branch': 'main', 'title': 'Sitemap'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'docs-kit-plus', 'number': 1, 'label': 'api'}),
            Action(name="ListPrs", kwargs={'repo': 'docs-kit-plus', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 711
    Task(
        annotator="variation_7",
        user_id="task_711",
    instruction=(
        "Coordinate repository 'payments-svc' ensuring branch 'pd' holds a commit 'pagerduty hook', and that a pull request titled 'PagerDuty webhook' from 'pd' to 'main' is open and bears the label 'ops'; enumerate the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'payments-svc'}),
            Action(name="CreateBranch", kwargs={'repo': 'payments-svc', 'branch': 'pd'}),
            Action(name="AddCommit", kwargs={'repo': 'payments-svc', 'branch': 'pd', 'message': 'pagerduty hook'}),
            Action(name="OpenPr", kwargs={'repo': 'payments-svc', 'head_branch': 'pd', 'base_branch': 'main', 'title': 'PagerDuty webhook'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'payments-svc', 'number': 1, 'label': 'ops'}),
            Action(name="ListPrs", kwargs={'repo': 'payments-svc', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 712
    Task(
        annotator="variation_7",
        user_id="task_712",
    instruction=(
        "Handle repository 'cli-tool' by ensuring branch 'embeddings' contains the commit 'add sbert', and there's a pull request with the title 'Embeddings' from 'embeddings' to 'main' labeled 'security'; enumerate open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'cli-tool'}),
            Action(name="CreateBranch", kwargs={'repo': 'cli-tool', 'branch': 'embeddings'}),
            Action(name="AddCommit", kwargs={'repo': 'cli-tool', 'branch': 'embeddings', 'message': 'add sbert'}),
            Action(name="OpenPr", kwargs={'repo': 'cli-tool', 'head_branch': 'embeddings', 'base_branch': 'main', 'title': 'Embeddings'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'cli-tool', 'number': 1, 'label': 'security'}),
            Action(name="ListPrs", kwargs={'repo': 'cli-tool', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 713
    Task(
        annotator="variation_7",
        user_id="task_713",
    instruction=(
        "Handle repository 'scheduler' by ensuring branch 'sms' contains the commit 'twilio', and there's a pull request with the title 'SMS support' from 'sms' to 'main' labeled 'infra'; enumerate open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'scheduler'}),
            Action(name="CreateBranch", kwargs={'repo': 'scheduler', 'branch': 'sms'}),
            Action(name="AddCommit", kwargs={'repo': 'scheduler', 'branch': 'sms', 'message': 'twilio'}),
            Action(name="OpenPr", kwargs={'repo': 'scheduler', 'head_branch': 'sms', 'base_branch': 'main', 'title': 'SMS support'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'scheduler', 'number': 1, 'label': 'infra'}),
            Action(name="ListPrs", kwargs={'repo': 'scheduler', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 714
    Task(
        annotator="variation_7",
        user_id="task_714",
    instruction=(
        "Handle the 'search-api' repository where the 'geojson' branch includes a commit named 'import geojson', and a pull request titled 'GeoJSON import' from 'geojson' to 'main' is active with the label 'seo'. Enumerate the open pull requests."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'search-api'}),
            Action(name="CreateBranch", kwargs={'repo': 'search-api', 'branch': 'geojson'}),
            Action(name="AddCommit", kwargs={'repo': 'search-api', 'branch': 'geojson', 'message': 'import geojson'}),
            Action(name="OpenPr", kwargs={'repo': 'search-api', 'head_branch': 'geojson', 'base_branch': 'main', 'title': 'GeoJSON import'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'search-api', 'number': 1, 'label': 'seo'}),
            Action(name="ListPrs", kwargs={'repo': 'search-api', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 715
    Task(
        annotator="variation_7",
        user_id="task_715",
    instruction=(
        "Handle the 'monitor' repository where the 'batch' branch contains a commit called 'batch process', and a pull request titled 'Batch process' from 'batch' to 'main' is open with the label 'ui'. Enumerate the open pull requests."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'monitor'}),
            Action(name="CreateBranch", kwargs={'repo': 'monitor', 'branch': 'batch'}),
            Action(name="AddCommit", kwargs={'repo': 'monitor', 'branch': 'batch', 'message': 'batch process'}),
            Action(name="OpenPr", kwargs={'repo': 'monitor', 'head_branch': 'batch', 'base_branch': 'main', 'title': 'Batch process'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'monitor', 'number': 1, 'label': 'ui'}),
            Action(name="ListPrs", kwargs={'repo': 'monitor', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 716
    Task(
        annotator="variation_7",
        user_id="task_716",
    instruction=(
        "Verify that repository 'mail-svc' is configured as follows: branch 'reply' should contain a commit named 'quick replies'; an open pull request titled 'Quick replies' should be present from 'reply' to 'main' with the label 'docs'. Afterward, provide the list of open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'mail-svc'}),
            Action(name="CreateBranch", kwargs={'repo': 'mail-svc', 'branch': 'reply'}),
            Action(name="AddCommit", kwargs={'repo': 'mail-svc', 'branch': 'reply', 'message': 'quick replies'}),
            Action(name="OpenPr", kwargs={'repo': 'mail-svc', 'head_branch': 'reply', 'base_branch': 'main', 'title': 'Quick replies'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'mail-svc', 'number': 1, 'label': 'docs'}),
            Action(name="ListPrs", kwargs={'repo': 'mail-svc', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 717
    Task(
        annotator="variation_7",
        user_id="task_717",
    instruction=(
        "Manage repository 'report-gen' to ensure branch 'nightly' has a commit 'cron spec', and an open pull request titled 'Nightly cron' should exist from 'nightly' to 'main' with the label 'feature'; then, display the list of open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'report-gen'}),
            Action(name="CreateBranch", kwargs={'repo': 'report-gen', 'branch': 'nightly'}),
            Action(name="AddCommit", kwargs={'repo': 'report-gen', 'branch': 'nightly', 'message': 'cron spec'}),
            Action(name="OpenPr", kwargs={'repo': 'report-gen', 'head_branch': 'nightly', 'base_branch': 'main', 'title': 'Nightly cron'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'report-gen', 'number': 1, 'label': 'feature'}),
            Action(name="ListPrs", kwargs={'repo': 'report-gen', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 718
    Task(
        annotator="variation_7",
        user_id="task_718",
    instruction=(
        "Ensure the repository 'auth-svc' is maintained, where the branch 'android-ci' contains a commit 'gradle fix', and a pull request named 'Android CI' from 'android-ci' to 'main' is open with the label 'api'. List any open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'auth-svc'}),
            Action(name="CreateBranch", kwargs={'repo': 'auth-svc', 'branch': 'android-ci'}),
            Action(name="AddCommit", kwargs={'repo': 'auth-svc', 'branch': 'android-ci', 'message': 'gradle fix'}),
            Action(name="OpenPr", kwargs={'repo': 'auth-svc', 'head_branch': 'android-ci', 'base_branch': 'main', 'title': 'Android CI'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'auth-svc', 'number': 1, 'label': 'api'}),
            Action(name="ListPrs", kwargs={'repo': 'auth-svc', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 719
    Task(
        annotator="variation_7",
        user_id="task_719",
    instruction=(
        "Take care of the repository 'ui-lib', ensuring the branch 'dag' includes a commit 'add dag', and an open pull request titled 'Airflow DAG' from 'dag' to 'main' exists with label 'ops'. List the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'ui-lib'}),
            Action(name="CreateBranch", kwargs={'repo': 'ui-lib', 'branch': 'dag'}),
            Action(name="AddCommit", kwargs={'repo': 'ui-lib', 'branch': 'dag', 'message': 'add dag'}),
            Action(name="OpenPr", kwargs={'repo': 'ui-lib', 'head_branch': 'dag', 'base_branch': 'main', 'title': 'Airflow DAG'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'ui-lib', 'number': 1, 'label': 'ops'}),
            Action(name="ListPrs", kwargs={'repo': 'ui-lib', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 720
    Task(
        annotator="variation_7",
        user_id="task_720",
    instruction=(
        "Ensure the 'db-migrator' repository is maintained, specifically where branch 'minimax' contains a commit labeled 'minimax', and there is an existing pull request named 'Add minimax' from 'minimax' to 'main' with a 'security' label. Compile a list of open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'db-migrator'}),
            Action(name="CreateBranch", kwargs={'repo': 'db-migrator', 'branch': 'minimax'}),
            Action(name="AddCommit", kwargs={'repo': 'db-migrator', 'branch': 'minimax', 'message': 'minimax'}),
            Action(name="OpenPr", kwargs={'repo': 'db-migrator', 'head_branch': 'minimax', 'base_branch': 'main', 'title': 'Add minimax'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'db-migrator', 'number': 1, 'label': 'security'}),
            Action(name="ListPrs", kwargs={'repo': 'db-migrator', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 721
    Task(
        annotator="variation_7",
        user_id="task_721",
    instruction=(
        "Ensure the 'kafka-consumer' repository is maintained, particularly where the 'tiles' branch includes a commit titled 'tile cache', and an open pull request named 'Tile cache' exists from 'tiles' to 'main' with the label 'infra'. Compile a list of open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'kafka-consumer'}),
            Action(name="CreateBranch", kwargs={'repo': 'kafka-consumer', 'branch': 'tiles'}),
            Action(name="AddCommit", kwargs={'repo': 'kafka-consumer', 'branch': 'tiles', 'message': 'tile cache'}),
            Action(name="OpenPr", kwargs={'repo': 'kafka-consumer', 'head_branch': 'tiles', 'base_branch': 'main', 'title': 'Tile cache'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'kafka-consumer', 'number': 1, 'label': 'infra'}),
            Action(name="ListPrs", kwargs={'repo': 'kafka-consumer', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 722
    Task(
        annotator="variation_7",
        user_id="task_722",
    instruction=(
        "Manage the repository 'notifier' where the 'session' branch has a commit called 'session mgmt', and there's an open pull request titled 'Session init' from 'session' to 'main' with the label 'seo'; enumerate open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'notifier'}),
            Action(name="CreateBranch", kwargs={'repo': 'notifier', 'branch': 'session'}),
            Action(name="AddCommit", kwargs={'repo': 'notifier', 'branch': 'session', 'message': 'session mgmt'}),
            Action(name="OpenPr", kwargs={'repo': 'notifier', 'head_branch': 'session', 'base_branch': 'main', 'title': 'Session init'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'notifier', 'number': 1, 'label': 'seo'}),
            Action(name="ListPrs", kwargs={'repo': 'notifier', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 723
    Task(
        annotator="variation_7",
        user_id="task_723",
    instruction=(
        "Oversee the repository 'crawler' where the 'etl' branch includes a commit labeled 'etl script', and there's an open pull request titled 'ETL v1' from 'etl' to 'main' with the label 'ui'; enumerate open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'crawler'}),
            Action(name="CreateBranch", kwargs={'repo': 'crawler', 'branch': 'etl'}),
            Action(name="AddCommit", kwargs={'repo': 'crawler', 'branch': 'etl', 'message': 'etl script'}),
            Action(name="OpenPr", kwargs={'repo': 'crawler', 'head_branch': 'etl', 'base_branch': 'main', 'title': 'ETL v1'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'crawler', 'number': 1, 'label': 'ui'}),
            Action(name="ListPrs", kwargs={'repo': 'crawler', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 724
    Task(
        annotator="variation_7",
        user_id="task_724",
    instruction=(
        "Ensure repository 'logger' is up-to-date, with branch 'vat' containing a commit 'vat rounding'. An open pull request titled 'VAT rounding' should exist from 'vat' to 'main', labeled 'docs'. Please list the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'logger'}),
            Action(name="CreateBranch", kwargs={'repo': 'logger', 'branch': 'vat'}),
            Action(name="AddCommit", kwargs={'repo': 'logger', 'branch': 'vat', 'message': 'vat rounding'}),
            Action(name="OpenPr", kwargs={'repo': 'logger', 'head_branch': 'vat', 'base_branch': 'main', 'title': 'VAT rounding'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'logger', 'number': 1, 'label': 'docs'}),
            Action(name="ListPrs", kwargs={'repo': 'logger', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 725
    Task(
        annotator="variation_7",
        user_id="task_725",
    instruction=(
        "Ensure repository 'game-ai' is maintained, with branch 'cron' containing a commit 'cron jobs'. An open pull request titled 'Cron jobs v2' should exist from 'cron' to 'main', labeled 'feature'. Please list the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'game-ai'}),
            Action(name="CreateBranch", kwargs={'repo': 'game-ai', 'branch': 'cron'}),
            Action(name="AddCommit", kwargs={'repo': 'game-ai', 'branch': 'cron', 'message': 'cron jobs'}),
            Action(name="OpenPr", kwargs={'repo': 'game-ai', 'head_branch': 'cron', 'base_branch': 'main', 'title': 'Cron jobs v2'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'game-ai', 'number': 1, 'label': 'feature'}),
            Action(name="ListPrs", kwargs={'repo': 'game-ai', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 726
    Task(
        annotator="variation_7",
        user_id="task_726",
    instruction=(
        "Ensure the management of the repository 'image-cdn' where the 'oauth' branch includes a commit 'oauth route', and there's an active pull request titled 'OAuth route' from 'oauth' to 'main' with the label 'api'; enumerate open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'image-cdn'}),
            Action(name="CreateBranch", kwargs={'repo': 'image-cdn', 'branch': 'oauth'}),
            Action(name="AddCommit", kwargs={'repo': 'image-cdn', 'branch': 'oauth', 'message': 'oauth route'}),
            Action(name="OpenPr", kwargs={'repo': 'image-cdn', 'head_branch': 'oauth', 'base_branch': 'main', 'title': 'OAuth route'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'image-cdn', 'number': 1, 'label': 'api'}),
            Action(name="ListPrs", kwargs={'repo': 'image-cdn', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 727
    Task(
        annotator="variation_7",
        user_id="task_727",
    instruction=(
        "Oversee the repository 'analytics' where the 'graphql' branch contains a commit 'schema', and an existing pull request is titled 'GraphQL schema' from 'graphql' to 'main' with the label 'ops'; enumerate open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'analytics'}),
            Action(name="CreateBranch", kwargs={'repo': 'analytics', 'branch': 'graphql'}),
            Action(name="AddCommit", kwargs={'repo': 'analytics', 'branch': 'graphql', 'message': 'schema'}),
            Action(name="OpenPr", kwargs={'repo': 'analytics', 'head_branch': 'graphql', 'base_branch': 'main', 'title': 'GraphQL schema'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'analytics', 'number': 1, 'label': 'ops'}),
            Action(name="ListPrs", kwargs={'repo': 'analytics', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 728
    Task(
        annotator="variation_7",
        user_id="task_728",
    instruction=(
        "Handle the repository 'seo-helper', ensuring the branch 'avatars' includes a commit 'avatar gen', and there is an open pull request titled 'Avatar generator' from 'avatars' to 'main' with the label 'security'; list open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'seo-helper'}),
            Action(name="CreateBranch", kwargs={'repo': 'seo-helper', 'branch': 'avatars'}),
            Action(name="AddCommit", kwargs={'repo': 'seo-helper', 'branch': 'avatars', 'message': 'avatar gen'}),
            Action(name="OpenPr", kwargs={'repo': 'seo-helper', 'head_branch': 'avatars', 'base_branch': 'main', 'title': 'Avatar generator'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'seo-helper', 'number': 1, 'label': 'security'}),
            Action(name="ListPrs", kwargs={'repo': 'seo-helper', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 729
    Task(
        annotator="variation_7",
        user_id="task_729",
    instruction=(
        "Coordinate the repository 'release-bot', ensuring the branch 'payments' contains a commit 'fee calc', and there is an open pull request titled 'Fee calc' from 'payments' to 'main' with the label 'infra'; list open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'release-bot'}),
            Action(name="CreateBranch", kwargs={'repo': 'release-bot', 'branch': 'payments'}),
            Action(name="AddCommit", kwargs={'repo': 'release-bot', 'branch': 'payments', 'message': 'fee calc'}),
            Action(name="OpenPr", kwargs={'repo': 'release-bot', 'head_branch': 'payments', 'base_branch': 'main', 'title': 'Fee calc'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'release-bot', 'number': 1, 'label': 'infra'}),
            Action(name="ListPrs", kwargs={'repo': 'release-bot', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 730
    Task(
        annotator="variation_7",
        user_id="task_730",
    instruction=(
        "Handle the repository 'docs-site' with the branch 'profiles' that contains a commit 'profile page', and ensure that there is an open pull request titled 'Profile page' from 'profiles' to 'main' with the label 'seo'; enumerate any open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'docs-site'}),
            Action(name="CreateBranch", kwargs={'repo': 'docs-site', 'branch': 'profiles'}),
            Action(name="AddCommit", kwargs={'repo': 'docs-site', 'branch': 'profiles', 'message': 'profile page'}),
            Action(name="OpenPr", kwargs={'repo': 'docs-site', 'head_branch': 'profiles', 'base_branch': 'main', 'title': 'Profile page'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'docs-site', 'number': 1, 'label': 'seo'}),
            Action(name="ListPrs", kwargs={'repo': 'docs-site', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 731
    Task(
        annotator="variation_7",
        user_id="task_731",
    instruction=(
        "Coordinate the management of the repository 'billing-svc' with the branch 'events' containing a commit 'event bus', and verify that an open pull request titled 'Event bus' from 'events' to 'main' exists with the label 'ui'; enumerate the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'billing-svc'}),
            Action(name="CreateBranch", kwargs={'repo': 'billing-svc', 'branch': 'events'}),
            Action(name="AddCommit", kwargs={'repo': 'billing-svc', 'branch': 'events', 'message': 'event bus'}),
            Action(name="OpenPr", kwargs={'repo': 'billing-svc', 'head_branch': 'events', 'base_branch': 'main', 'title': 'Event bus'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'billing-svc', 'number': 1, 'label': 'ui'}),
            Action(name="ListPrs", kwargs={'repo': 'billing-svc', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 732
    Task(
        annotator="variation_7",
        user_id="task_732",
    instruction=(
        "Ensure the repository 'feature-flag' is maintained, where the branch 'comments' includes a commit 'comment form', and there's an open pull request titled 'Comments UI' from 'comments' to 'main' with the label 'docs'; show the open pull requests."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'feature-flag'}),
            Action(name="CreateBranch", kwargs={'repo': 'feature-flag', 'branch': 'comments'}),
            Action(name="AddCommit", kwargs={'repo': 'feature-flag', 'branch': 'comments', 'message': 'comment form'}),
            Action(name="OpenPr", kwargs={'repo': 'feature-flag', 'head_branch': 'comments', 'base_branch': 'main', 'title': 'Comments UI'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'feature-flag', 'number': 1, 'label': 'docs'}),
            Action(name="ListPrs", kwargs={'repo': 'feature-flag', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 733
    Task(
        annotator="variation_7",
        user_id="task_733",
    instruction=(
        "Ensure the repository 'cache-layer' is maintained, where the branch 'notify' includes a commit 'notify rules', and there's an open pull request titled 'Notify rules' from 'notify' to 'main' with the label 'feature'; show the open pull requests."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'cache-layer'}),
            Action(name="CreateBranch", kwargs={'repo': 'cache-layer', 'branch': 'notify'}),
            Action(name="AddCommit", kwargs={'repo': 'cache-layer', 'branch': 'notify', 'message': 'notify rules'}),
            Action(name="OpenPr", kwargs={'repo': 'cache-layer', 'head_branch': 'notify', 'base_branch': 'main', 'title': 'Notify rules'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'cache-layer', 'number': 1, 'label': 'feature'}),
            Action(name="ListPrs", kwargs={'repo': 'cache-layer', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 734
    Task(
        annotator="variation_7",
        user_id="task_734",
    instruction=(
        "Ensure the repository 'ml-pipeline' is kept up to date where the 'realtime' branch includes a commit 'socket hub', and there is a pull request titled 'Realtime hub' from 'realtime' to 'main' which is open with the label 'api'; enumerate the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'ml-pipeline'}),
            Action(name="CreateBranch", kwargs={'repo': 'ml-pipeline', 'branch': 'realtime'}),
            Action(name="AddCommit", kwargs={'repo': 'ml-pipeline', 'branch': 'realtime', 'message': 'socket hub'}),
            Action(name="OpenPr", kwargs={'repo': 'ml-pipeline', 'head_branch': 'realtime', 'base_branch': 'main', 'title': 'Realtime hub'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'ml-pipeline', 'number': 1, 'label': 'api'}),
            Action(name="ListPrs", kwargs={'repo': 'ml-pipeline', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 735
    Task(
        annotator="variation_7",
        user_id="task_735",
    instruction=(
        "Ensure the repository 'mobile-app' is kept up to date where the 'delta' branch includes a commit 'delta sync', and there is a pull request titled 'Delta sync' from 'delta' to 'main' which is open with the label 'ops'; enumerate the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'mobile-app'}),
            Action(name="CreateBranch", kwargs={'repo': 'mobile-app', 'branch': 'delta'}),
            Action(name="AddCommit", kwargs={'repo': 'mobile-app', 'branch': 'delta', 'message': 'delta sync'}),
            Action(name="OpenPr", kwargs={'repo': 'mobile-app', 'head_branch': 'delta', 'base_branch': 'main', 'title': 'Delta sync'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'mobile-app', 'number': 1, 'label': 'ops'}),
            Action(name="ListPrs", kwargs={'repo': 'mobile-app', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 736
    Task(
        annotator="variation_7",
        user_id="task_736",
    instruction=(
        "Handle the 'web-auth' repository by ensuring the 'pdf' branch contains the commit 'pdf export', and verify that a pull request with the title 'PDF export' from 'pdf' to 'main' is open with the label 'security'; enumerate the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'web-auth'}),
            Action(name="CreateBranch", kwargs={'repo': 'web-auth', 'branch': 'pdf'}),
            Action(name="AddCommit", kwargs={'repo': 'web-auth', 'branch': 'pdf', 'message': 'pdf export'}),
            Action(name="OpenPr", kwargs={'repo': 'web-auth', 'head_branch': 'pdf', 'base_branch': 'main', 'title': 'PDF export'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'web-auth', 'number': 1, 'label': 'security'}),
            Action(name="ListPrs", kwargs={'repo': 'web-auth', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 737
    Task(
        annotator="variation_7",
        user_id="task_737",
    instruction=(
        "Manage the 'observability' repository where the 'thumb' branch includes a commit 'image thumbs', and check that a pull request titled 'Thumbnailer' from 'thumb' to 'main' is open with the label 'infra'; list the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'observability'}),
            Action(name="CreateBranch", kwargs={'repo': 'observability', 'branch': 'thumb'}),
            Action(name="AddCommit", kwargs={'repo': 'observability', 'branch': 'thumb', 'message': 'image thumbs'}),
            Action(name="OpenPr", kwargs={'repo': 'observability', 'head_branch': 'thumb', 'base_branch': 'main', 'title': 'Thumbnailer'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'observability', 'number': 1, 'label': 'infra'}),
            Action(name="ListPrs", kwargs={'repo': 'observability', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 738
    Task(
        annotator="variation_7",
        user_id="task_738",
    instruction=(
        "Handle the repository 'map-service' in which branch 'schedule' has a commit 'schedule lib', and ensure the pull request named 'Scheduler core' from 'schedule' to 'main' is open with the label 'seo'; enumerate open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'map-service'}),
            Action(name="CreateBranch", kwargs={'repo': 'map-service', 'branch': 'schedule'}),
            Action(name="AddCommit", kwargs={'repo': 'map-service', 'branch': 'schedule', 'message': 'schedule lib'}),
            Action(name="OpenPr", kwargs={'repo': 'map-service', 'head_branch': 'schedule', 'base_branch': 'main', 'title': 'Scheduler core'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'map-service', 'number': 1, 'label': 'seo'}),
            Action(name="ListPrs", kwargs={'repo': 'map-service', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 739
    Task(
        annotator="variation_7",
        user_id="task_739",
    instruction=(
        "Coordinate the repository 'api-gateway' where branch 'bus' contains a commit 'bus impl', and verify that a pull request titled 'Event bus v2' from 'bus' to 'main' is open with the label 'ui'; list the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'api-gateway'}),
            Action(name="CreateBranch", kwargs={'repo': 'api-gateway', 'branch': 'bus'}),
            Action(name="AddCommit", kwargs={'repo': 'api-gateway', 'branch': 'bus', 'message': 'bus impl'}),
            Action(name="OpenPr", kwargs={'repo': 'api-gateway', 'head_branch': 'bus', 'base_branch': 'main', 'title': 'Event bus v2'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'api-gateway', 'number': 1, 'label': 'ui'}),
            Action(name="ListPrs", kwargs={'repo': 'api-gateway', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 740
    Task(
        annotator="variation_7",
        user_id="task_740",
    instruction=(
        "Verify the existence of the 'data-lake' repository (and create it if it's not present). Make sure there is an open issue titled 'Reply delay' with the text 'Replies are slow in peak hours.', tagged with 'ops', and assigned to 'chris'. Once confirmed, provide only the 'label', 'assignees', and 'title' fields for that issue (avoid returning complete issue objects)."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'data-lake'}),
            Action(name="OpenIssue", kwargs={'repo': 'data-lake', 'title': 'Reply delay', 'body': 'Replies are slow in peak hours.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'data-lake', 'number': 1, 'label': 'ops'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'data-lake', 'number': 1, 'username': 'chris'}),
            Action(name="ListIssues", kwargs={'repo': 'data-lake'}),
        ],
        outputs=[]
    ),

    # 741
    Task(
        annotator="variation_7",
        user_id="task_741",
    instruction=(
        "Verify the presence of the 'chat-bot' repository (and create it if it's absent). Make certain there is an open issue titled 'Rate limit' with the content 'Too strict rate limiting.', tagged as 'api', and assigned to 'chris'. Upon confirmation, supply only the 'label', 'assignees', and 'title' fields for that issue (do not return the entire issue objects)."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'chat-bot'}),
            Action(name="OpenIssue", kwargs={'repo': 'chat-bot', 'title': 'Rate limit', 'body': 'Too strict rate limiting.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'chat-bot', 'number': 1, 'label': 'api'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'chat-bot', 'number': 1, 'username': 'chris'}),
            Action(name="ListIssues", kwargs={'repo': 'chat-bot'}),
        ],
        outputs=[]
    ),

    # 742
    Task(
        annotator="variation_7",
        user_id="task_742",
    instruction=(
        "Verify repository 'cron-runner' is present (establish it if absent). Confirm there is an ongoing issue titled 'Bad rounding' with content 'Rounding error in totals.', tagged 'priority', and allocated to 'elena'. Upon verification, return solely the 'label', 'assignees', and 'title' fields for that issue (do not include full issue objects)."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'cron-runner'}),
            Action(name="OpenIssue", kwargs={'repo': 'cron-runner', 'title': 'Bad rounding', 'body': 'Rounding error in totals.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'cron-runner', 'number': 1, 'label': 'priority'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'cron-runner', 'number': 1, 'username': 'elena'}),
            Action(name="ListIssues", kwargs={'repo': 'cron-runner'}),
        ],
        outputs=[]
    ),

    # 743
    Task(
        annotator="variation_7",
        user_id="task_743",
    instruction=(
        "Verify repository 'oncall-bot' is present (create it if it isn't). Confirm there is a current issue titled 'Null handling' with content 'Handle None safely.', tagged 'bug', and allocated to 'jake'. After verification, return solely the 'label', 'assignees', and 'title' fields for that issue (do not include full issue objects)."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'oncall-bot'}),
            Action(name="OpenIssue", kwargs={'repo': 'oncall-bot', 'title': 'Null handling', 'body': 'Handle None safely.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'oncall-bot', 'number': 1, 'label': 'bug'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'oncall-bot', 'number': 1, 'username': 'jake'}),
            Action(name="ListIssues", kwargs={'repo': 'oncall-bot'}),
        ],
        outputs=[]
    ),

    # 744
    Task(
        annotator="variation_7",
        user_id="task_744",
    instruction=(
        "Handle the existence of the 'linter' repository, creating it if it does not yet exist. Verify there is an issue open with the title 'S3 lifecycle', containing the body 'Configure S3 lifecycle policies.', tagged as 'infra', and assigned to 'olivia'. Once this is confirmed, provide only the 'label', 'assignees', and 'title' attributes for that specific issue (full issue objects should not be returned)."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'linter'}),
            Action(name="OpenIssue", kwargs={'repo': 'linter', 'title': 'S3 lifecycle', 'body': 'Configure S3 lifecycle policies.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'linter', 'number': 1, 'label': 'infra'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'linter', 'number': 1, 'username': 'olivia'}),
            Action(name="ListIssues", kwargs={'repo': 'linter'}),
        ],
        outputs=[]
    ),

    # 745
    Task(
        annotator="variation_7",
        user_id="task_745",
    instruction=(
        "Verify the repository 'ai-sdk' exists, creating it as necessary. Confirm there is an open issue titled 'Token expiry bug', with the body 'Expired tokens still validate.', labeled as 'security', and assigned to 'arjun'. Afterward, return just the 'label', 'assignees', and 'title' details for that issue (avoid returning complete issue objects)."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'ai-sdk'}),
            Action(name="OpenIssue", kwargs={'repo': 'ai-sdk', 'title': 'Token expiry bug', 'body': 'Expired tokens still validate.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'ai-sdk', 'number': 1, 'label': 'security'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'ai-sdk', 'number': 1, 'username': 'arjun'}),
            Action(name="ListIssues", kwargs={'repo': 'ai-sdk'}),
        ],
        outputs=[]
    ),

    # 746
    Task(
        annotator="variation_7",
        user_id="task_746",
    instruction=(
        "Verify the presence of the repository 'design-system' and create it if it does not exist. Confirm that there is an open issue with the title 'Eviction policy', containing the body 'Decide LFU vs LRU.', marked with the label 'planning', and assigned to 'nora'. Once verified, provide only the 'label', 'assignees', and 'title' fields for that specific issue (avoid returning complete issue objects)."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'design-system'}),
            Action(name="OpenIssue", kwargs={'repo': 'design-system', 'title': 'Eviction policy', 'body': 'Decide LFU vs LRU.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'design-system', 'number': 1, 'label': 'planning'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'design-system', 'number': 1, 'username': 'nora'}),
            Action(name="ListIssues", kwargs={'repo': 'design-system'}),
        ],
        outputs=[]
    ),

    # 747
    Task(
        annotator="variation_7",
        user_id="task_747",
    instruction=(
        "Verify that the repository 'etl-runner' is present or create it if absent. Confirm there is an open issue with the title 'Add cron parser' and body 'Add a Cron expression parser.', labeled 'feature', and assigned to 'zayn'. Once confirmed, supply only the 'label', 'assignees', and 'title' fields for that issue (avoid providing full issue objects)."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'etl-runner'}),
            Action(name="OpenIssue", kwargs={'repo': 'etl-runner', 'title': 'Add cron parser', 'body': 'Add a Cron expression parser.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'etl-runner', 'number': 1, 'label': 'feature'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'etl-runner', 'number': 1, 'username': 'zayn'}),
            Action(name="ListIssues", kwargs={'repo': 'etl-runner'}),
        ],
        outputs=[]
    ),

    # 748
    Task(
        annotator="variation_7",
        user_id="task_748",
    instruction=(
        "Handle the management of the repository 'geo-index' by creating an issue with the title 'Healthcheck fails', including the body 'Probe endpoint fails on cold start.', labeled as 'bug' and assigned to 'amin'; proceed to list issues."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'geo-index'}),
            Action(name="OpenIssue", kwargs={'repo': 'geo-index', 'title': 'Healthcheck fails', 'body': 'Probe endpoint fails on cold start.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'geo-index', 'number': 1, 'label': 'bug'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'geo-index', 'number': 1, 'username': 'amin'}),
            Action(name="ListIssues", kwargs={'repo': 'geo-index'}),
        ],
        outputs=[]
    ),

    # 749
    Task(
        annotator="variation_7",
        user_id="task_749",
    instruction=(
        "Verify the existence of the repository 'queue-svc' (initiate its creation if it's absent). Confirm there is an open issue titled 'Add migration plan', with the body 'Outline migration steps.', labeled 'planning', and assigned to 'emma'. Once confirmed, return solely the 'label', 'assignees', and 'title' fields for that issue (omit returning complete issue objects)."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'queue-svc'}),
            Action(name="OpenIssue", kwargs={'repo': 'queue-svc', 'title': 'Add migration plan', 'body': 'Outline migration steps.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'queue-svc', 'number': 1, 'label': 'planning'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'queue-svc', 'number': 1, 'username': 'emma'}),
            Action(name="ListIssues", kwargs={'repo': 'queue-svc'}),
        ],
        outputs=[]
    ),

    # 750
    Task(
        annotator="variation_7",
        user_id="task_750",
    instruction=(
        "Handle the repository 'rate-limiter' to confirm its existence (create it if absent). Confirm there is an open issue titled 'CSV export' with the body 'Export CSV with delimiter option.', labeled 'feature', and assigned to 'emma'. Once confirmed, provide only the 'label', 'assignees', and 'title' fields for that particular issue (avoid returning full issue objects)."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'rate-limiter'}),
            Action(name="OpenIssue", kwargs={'repo': 'rate-limiter', 'title': 'CSV export', 'body': 'Export CSV with delimiter option.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'rate-limiter', 'number': 1, 'label': 'feature'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'rate-limiter', 'number': 1, 'username': 'emma'}),
            Action(name="ListIssues", kwargs={'repo': 'rate-limiter'}),
        ],
        outputs=[]
    ),

    # 751
    Task(
        annotator="variation_7",
        user_id="task_751",
    instruction=(
        "Coordinate the management of the repository 'uploader' by initiating an issue with the title 'Respect robots.txt', including the body 'Crawler must respect robots.txt.', labeled 'compliance', and assigned to 'amin'; display the list of issues."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'uploader'}),
            Action(name="OpenIssue", kwargs={'repo': 'uploader', 'title': 'Respect robots.txt', 'body': 'Crawler must respect robots.txt.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'uploader', 'number': 1, 'label': 'compliance'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'uploader', 'number': 1, 'username': 'amin'}),
            Action(name="ListIssues", kwargs={'repo': 'uploader'}),
        ],
        outputs=[]
    ),

    # 752
    Task(
        annotator="variation_7",
        user_id="task_752",
    instruction=(
        "Handle the management of repository 'image-proc' by creating an issue titled 'Rule for imports' with body 'Enforce import ordering.' labeled 'enhancement' and assigned to 'olivia'; proceed to list issues."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'image-proc'}),
            Action(name="OpenIssue", kwargs={'repo': 'image-proc', 'title': 'Rule for imports', 'body': 'Enforce import ordering.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'image-proc', 'number': 1, 'label': 'enhancement'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'image-proc', 'number': 1, 'username': 'olivia'}),
            Action(name="ListIssues", kwargs={'repo': 'image-proc'}),
        ],
        outputs=[]
    ),

    # 753
    Task(
        annotator="variation_7",
        user_id="task_753",
    instruction=(
        "Coordinate the management of repository 'webhooks' by initiating an issue titled 'Toggle not saved' with body 'Toggles revert after refresh.' labeled 'bug' and assigned to 'karim'; then list issues."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'webhooks'}),
            Action(name="OpenIssue", kwargs={'repo': 'webhooks', 'title': 'Toggle not saved', 'body': 'Toggles revert after refresh.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'webhooks', 'number': 1, 'label': 'bug'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'webhooks', 'number': 1, 'username': 'karim'}),
            Action(name="ListIssues", kwargs={'repo': 'webhooks'}),
        ],
        outputs=[]
    ),

    # 754
    Task(
        annotator="variation_7",
        user_id="task_754",
    instruction=(
        "Handle the repository 'form-builder' by creating an issue with the title 'Rate limit header' and the body 'Expose X-RateLimit headers.', labeled as 'api', and assign it to 'olivia'; then list issues."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'form-builder'}),
            Action(name="OpenIssue", kwargs={'repo': 'form-builder', 'title': 'Rate limit header', 'body': 'Expose X-RateLimit headers.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'form-builder', 'number': 1, 'label': 'api'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'form-builder', 'number': 1, 'username': 'olivia'}),
            Action(name="ListIssues", kwargs={'repo': 'form-builder'}),
        ],
        outputs=[]
    ),

    # 755
    Task(
        annotator="variation_7",
        user_id="task_755",
    instruction=(
        "Coordinate the repository 'markdown-viewer' by setting up an issue titled 'Add dashboard' with the body 'Create Grafana dashboards.', labeled 'observability', and assign to 'emma'; subsequently list issues."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'markdown-viewer'}),
            Action(name="OpenIssue", kwargs={'repo': 'markdown-viewer', 'title': 'Add dashboard', 'body': 'Create Grafana dashboards.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'markdown-viewer', 'number': 1, 'label': 'observability'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'markdown-viewer', 'number': 1, 'username': 'emma'}),
            Action(name="ListIssues", kwargs={'repo': 'markdown-viewer'}),
        ],
        outputs=[]
    ),

    # 756
    Task(
        annotator="variation_7",
        user_id="task_756",
    instruction=(
        "Handle the repository 'audit-log' by creating an issue titled 'Cold start' with the body 'Function cold starts are high.' labeled as 'ops' and assign it to 'elena'; list the issues."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'audit-log'}),
            Action(name="OpenIssue", kwargs={'repo': 'audit-log', 'title': 'Cold start', 'body': 'Function cold starts are high.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'audit-log', 'number': 1, 'label': 'ops'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'audit-log', 'number': 1, 'username': 'elena'}),
            Action(name="ListIssues", kwargs={'repo': 'audit-log'}),
        ],
        outputs=[]
    ),

    # 757
    Task(
        annotator="variation_7",
        user_id="task_757",
    instruction=(
        "Handle the repository 'session-store' by creating an issue titled 'Webhook retry' with the body 'Implement exponential backoff.' labeled as 'api' and assign it to 'jake'; list the issues."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'session-store'}),
            Action(name="OpenIssue", kwargs={'repo': 'session-store', 'title': 'Webhook retry', 'body': 'Implement exponential backoff.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'session-store', 'number': 1, 'label': 'api'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'session-store', 'number': 1, 'username': 'jake'}),
            Action(name="ListIssues", kwargs={'repo': 'session-store'}),
        ],
        outputs=[]
    ),

    # 758
    Task(
        annotator="variation_7",
        user_id="task_758",
    instruction=(
        "Handle repository 'graphql-gw' by creating an issue titled 'Dark mode toggle' with the body 'Add a dark theme switcher.' labeled 'ui' and assigned to 'nora'; list issues."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'graphql-gw'}),
            Action(name="OpenIssue", kwargs={'repo': 'graphql-gw', 'title': 'Dark mode toggle', 'body': 'Add a dark theme switcher.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'graphql-gw', 'number': 1, 'label': 'ui'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'graphql-gw', 'number': 1, 'username': 'nora'}),
            Action(name="ListIssues", kwargs={'repo': 'graphql-gw'}),
        ],
        outputs=[]
    ),

    # 759
    Task(
        annotator="variation_7",
        user_id="task_759",
    instruction=(
        "Coordinate repository 'oauth-proxy' by creating an issue titled 'Timezone bug' with the body 'Datetime parsing incorrect.' labeled 'bug' and assigned to 'chris'; list issues."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'oauth-proxy'}),
            Action(name="OpenIssue", kwargs={'repo': 'oauth-proxy', 'title': 'Timezone bug', 'body': 'Datetime parsing incorrect.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'repo': 'oauth-proxy', 'number': 1, 'label': 'bug'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'repo': 'oauth-proxy', 'number': 1, 'username': 'chris'}),
            Action(name="ListIssues", kwargs={'repo': 'oauth-proxy'}),
        ],
        outputs=[]
    ),

    # 760
    Task(
        annotator="variation_7",
        user_id="task_760",
    instruction=(
        "Handle the transfer of repository 'profile-svc' to 'core-team' as the new owner; create an issue titled 'Deprecate old API' with the body 'Plan removal of v1 API.' labeled 'deprecate' and assigned to 'nora'; subsequently, enumerate issues for owner 'core-team'."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'profile-svc'}),
            Action(name="TransferRepo", kwargs={'repo': 'profile-svc', 'new_owner': 'core-team'}),
            Action(name="OpenIssue", kwargs={'owner': 'core-team', 'repo': 'profile-svc', 'title': 'Deprecate old API', 'body': 'Plan removal of v1 API.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'owner': 'core-team', 'repo': 'profile-svc', 'number': 1, 'label': 'deprecate'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'owner': 'core-team', 'repo': 'profile-svc', 'number': 1, 'username': 'nora'}),
            Action(name="ListIssues", kwargs={'owner': 'core-team', 'repo': 'profile-svc'}),
        ],
        outputs=[]
    ),

    # 761
    Task(
        annotator="variation_7",
        user_id="task_761",
    instruction=(
        "Ensure the repository 'comments-api' is transferred to 'edge-team' as its new owner; under this new ownership, open an issue titled 'Purge endpoint' with the body 'Add purge endpoint for CDN.' labeled 'ops' and assign it to 'amin'; afterwards, list issues for owner 'edge-team'."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'comments-api'}),
            Action(name="TransferRepo", kwargs={'repo': 'comments-api', 'new_owner': 'edge-team'}),
            Action(name="OpenIssue", kwargs={'owner': 'edge-team', 'repo': 'comments-api', 'title': 'Purge endpoint', 'body': 'Add purge endpoint for CDN.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'owner': 'edge-team', 'repo': 'comments-api', 'number': 1, 'label': 'ops'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'owner': 'edge-team', 'repo': 'comments-api', 'number': 1, 'username': 'amin'}),
            Action(name="ListIssues", kwargs={'owner': 'edge-team', 'repo': 'comments-api'}),
        ],
        outputs=[]
    ),

    # 762
    Task(
        annotator="variation_7",
        user_id="task_762",
    instruction=(
        "Handle the transfer of repository 'notifications' to 'security-group' as the new owner; once transferred, initiate an issue titled 'Rotate keys' with the content 'Rotate signing keys regularly.' with the label 'security', assigning it to 'arjun'; subsequently, enumerate issues for 'security-group'."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'notifications'}),
            Action(name="TransferRepo", kwargs={'repo': 'notifications', 'new_owner': 'security-group'}),
            Action(name="OpenIssue", kwargs={'owner': 'security-group', 'repo': 'notifications', 'title': 'Rotate keys', 'body': 'Rotate signing keys regularly.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'owner': 'security-group', 'repo': 'notifications', 'number': 1, 'label': 'security'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'owner': 'security-group', 'repo': 'notifications', 'number': 1, 'username': 'arjun'}),
            Action(name="ListIssues", kwargs={'owner': 'security-group', 'repo': 'notifications'}),
        ],
        outputs=[]
    ),

    # 763
    Task(
        annotator="variation_7",
        user_id="task_763",
    instruction=(
        "Oversee the transfer of the repository 'realtime-hub' to 'data-team' for new ownership; under the new owner, create an issue titled 'Partition table' with the description 'Partition table by month.' marked with the label 'infra' and assigned to 'emma'; finally, compile a list of issues for 'data-team'."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'realtime-hub'}),
            Action(name="TransferRepo", kwargs={'repo': 'realtime-hub', 'new_owner': 'data-team'}),
            Action(name="OpenIssue", kwargs={'owner': 'data-team', 'repo': 'realtime-hub', 'title': 'Partition table', 'body': 'Partition table by month.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'owner': 'data-team', 'repo': 'realtime-hub', 'number': 1, 'label': 'infra'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'owner': 'data-team', 'repo': 'realtime-hub', 'number': 1, 'username': 'emma'}),
            Action(name="ListIssues", kwargs={'owner': 'data-team', 'repo': 'realtime-hub'}),
        ],
        outputs=[]
    ),

    # 764
    Task(
        annotator="variation_7",
        user_id="task_764",
    instruction=(
        "Handle the transfer of the 'delta-sync' repository to the 'platform' owner; once ownership is established, initiate an issue titled 'Feature flags' with the body 'Rollout gradual flags.' and label it 'feature', assigning it to 'karim'. Finally, compile a list of issues related to the 'platform' owner."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'delta-sync'}),
            Action(name="TransferRepo", kwargs={'repo': 'delta-sync', 'new_owner': 'platform'}),
            Action(name="OpenIssue", kwargs={'owner': 'platform', 'repo': 'delta-sync', 'title': 'Feature flags', 'body': 'Rollout gradual flags.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'owner': 'platform', 'repo': 'delta-sync', 'number': 1, 'label': 'feature'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'owner': 'platform', 'repo': 'delta-sync', 'number': 1, 'username': 'karim'}),
            Action(name="ListIssues", kwargs={'owner': 'platform', 'repo': 'delta-sync'}),
        ],
        outputs=[]
    ),

    # 765
    Task(
        annotator="variation_7",
        user_id="task_765",
    instruction=(
        "Coordinate the transfer of the 'pdf-tool' repository to the 'growth' owner. Under the new ownership, create an issue titled 'ETL ownership' with the content 'Move ETL jobs here.', label it 'analytics', and assign it to 'emma'. Subsequently, assemble a list of issues associated with the 'growth' owner."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'pdf-tool'}),
            Action(name="TransferRepo", kwargs={'repo': 'pdf-tool', 'new_owner': 'growth'}),
            Action(name="OpenIssue", kwargs={'owner': 'growth', 'repo': 'pdf-tool', 'title': 'ETL ownership', 'body': 'Move ETL jobs here.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'owner': 'growth', 'repo': 'pdf-tool', 'number': 1, 'label': 'analytics'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'owner': 'growth', 'repo': 'pdf-tool', 'number': 1, 'username': 'emma'}),
            Action(name="ListIssues", kwargs={'owner': 'growth', 'repo': 'pdf-tool'}),
        ],
        outputs=[]
    ),

    # 766
    Task(
        annotator="variation_7",
        user_id="task_766",
    instruction=(
        "Make certain the 'thumbnailer' repository is transferred to be under the 'sre-team'; within the new ownership, initiate an issue titled 'Alert routing' with the description 'Route alerts to PagerDuty.' marked with label 'ops' and assign it to 'zayn'; subsequently, compile a list of issues for the 'sre-team' owner."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'thumbnailer'}),
            Action(name="TransferRepo", kwargs={'repo': 'thumbnailer', 'new_owner': 'sre-team'}),
            Action(name="OpenIssue", kwargs={'owner': 'sre-team', 'repo': 'thumbnailer', 'title': 'Alert routing', 'body': 'Route alerts to PagerDuty.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'owner': 'sre-team', 'repo': 'thumbnailer', 'number': 1, 'label': 'ops'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'owner': 'sre-team', 'repo': 'thumbnailer', 'number': 1, 'username': 'zayn'}),
            Action(name="ListIssues", kwargs={'owner': 'sre-team', 'repo': 'thumbnailer'}),
        ],
        outputs=[]
    ),

    # 767
    Task(
        annotator="variation_7",
        user_id="task_767",
    instruction=(
        "Verify that the repository 'scheduler-pro' is reassigned to the 'ml-team'; once transferred, create an issue titled 'Model registry' containing the text 'Registry for ML models.' with the label 'ml' assigned to 'nora'; afterward, catalog the issues for the 'ml-team' owner."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'scheduler-pro'}),
            Action(name="TransferRepo", kwargs={'repo': 'scheduler-pro', 'new_owner': 'ml-team'}),
            Action(name="OpenIssue", kwargs={'owner': 'ml-team', 'repo': 'scheduler-pro', 'title': 'Model registry', 'body': 'Registry for ML models.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'owner': 'ml-team', 'repo': 'scheduler-pro', 'number': 1, 'label': 'ml'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'owner': 'ml-team', 'repo': 'scheduler-pro', 'number': 1, 'username': 'nora'}),
            Action(name="ListIssues", kwargs={'owner': 'ml-team', 'repo': 'scheduler-pro'}),
        ],
        outputs=[]
    ),

    # 768
    Task(
        annotator="variation_7",
        user_id="task_768",
    instruction=(
        "Handle the transfer of the 'event-bus' repository to the ownership of 'infra-team'; once transferred, create an issue under the new owner called 'VPC peering' with the description 'Establish VPC peering.' carrying the label 'infra' and assign it to 'olivia'; subsequently, enumerate issues for the owner 'infra-team'."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'event-bus'}),
            Action(name="TransferRepo", kwargs={'repo': 'event-bus', 'new_owner': 'infra-team'}),
            Action(name="OpenIssue", kwargs={'owner': 'infra-team', 'repo': 'event-bus', 'title': 'VPC peering', 'body': 'Establish VPC peering.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'owner': 'infra-team', 'repo': 'event-bus', 'number': 1, 'label': 'infra'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'owner': 'infra-team', 'repo': 'event-bus', 'number': 1, 'username': 'olivia'}),
            Action(name="ListIssues", kwargs={'owner': 'infra-team', 'repo': 'event-bus'}),
        ],
        outputs=[]
    ),

    # 769
    Task(
        annotator="variation_7",
        user_id="task_769",
    instruction=(
        "Coordinate the transfer of the 'payment-ui' repository to 'design-team'; after this, under the new owner, initiate an issue titled 'Icon refresh' with the content 'Refresh icon set.' bearing the label 'ui' and assign it to 'elena'; following that, list issues for 'design-team'."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'payment-ui'}),
            Action(name="TransferRepo", kwargs={'repo': 'payment-ui', 'new_owner': 'design-team'}),
            Action(name="OpenIssue", kwargs={'owner': 'design-team', 'repo': 'payment-ui', 'title': 'Icon refresh', 'body': 'Refresh icon set.'}),
            Action(name="AddLabel", kwargs={'kind': 'issue', 'owner': 'design-team', 'repo': 'payment-ui', 'number': 1, 'label': 'ui'}),
            Action(name="AssignUser", kwargs={'kind': 'issue', 'owner': 'design-team', 'repo': 'payment-ui', 'number': 1, 'username': 'elena'}),
            Action(name="ListIssues", kwargs={'owner': 'design-team', 'repo': 'payment-ui'}),
        ],
        outputs=[]
    ),

    # 770
    Task(
        annotator="variation_7",
        user_id="task_770",
    instruction=(
        "Handle the repository 'coupon-svc' ensuring branch 'feat-1' contains a commit 'feature 1', and ensure a pull request titled 'Feature 1' from 'feat-1' to 'main' is open with the label 'ops', after undergoing closure and reopening; enumerate open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'coupon-svc'}),
            Action(name="CreateBranch", kwargs={'repo': 'coupon-svc', 'branch': 'feat-1'}),
            Action(name="AddCommit", kwargs={'repo': 'coupon-svc', 'branch': 'feat-1', 'message': 'feature 1'}),
            Action(name="OpenPr", kwargs={'repo': 'coupon-svc', 'head_branch': 'feat-1', 'base_branch': 'main', 'title': 'Feature 1'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'coupon-svc', 'number': 1, 'label': 'ops'}),
            Action(name="ClosePr", kwargs={'repo': 'coupon-svc', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'coupon-svc', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'coupon-svc', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 771
    Task(
        annotator="variation_7",
        user_id="task_771",
    instruction=(
        "Coordinate the repository 'shipping-svc' ensuring branch 'feat-2' contains a commit 'feature 2', and ensure a pull request titled 'Feature 2' from 'feat-2' to 'main' is open with the label 'security', after undergoing closure and reopening; enumerate open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'shipping-svc'}),
            Action(name="CreateBranch", kwargs={'repo': 'shipping-svc', 'branch': 'feat-2'}),
            Action(name="AddCommit", kwargs={'repo': 'shipping-svc', 'branch': 'feat-2', 'message': 'feature 2'}),
            Action(name="OpenPr", kwargs={'repo': 'shipping-svc', 'head_branch': 'feat-2', 'base_branch': 'main', 'title': 'Feature 2'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'shipping-svc', 'number': 1, 'label': 'security'}),
            Action(name="ClosePr", kwargs={'repo': 'shipping-svc', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'shipping-svc', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'shipping-svc', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 772
    Task(
        annotator="variation_7",
        user_id="task_772",
    instruction=(
        "Handle the repository 'catalog-api' where the branch 'feat-3' includes a commit labeled 'feature 3', and there's an active pull request titled 'Feature 3' from 'feat-3' to 'main' with the label 'infra', following its closure and reopening; enumerate the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'catalog-api'}),
            Action(name="CreateBranch", kwargs={'repo': 'catalog-api', 'branch': 'feat-3'}),
            Action(name="AddCommit", kwargs={'repo': 'catalog-api', 'branch': 'feat-3', 'message': 'feature 3'}),
            Action(name="OpenPr", kwargs={'repo': 'catalog-api', 'head_branch': 'feat-3', 'base_branch': 'main', 'title': 'Feature 3'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'catalog-api', 'number': 1, 'label': 'infra'}),
            Action(name="ClosePr", kwargs={'repo': 'catalog-api', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'catalog-api', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'catalog-api', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 773
    Task(
        annotator="variation_7",
        user_id="task_773",
    instruction=(
        "Handle the repository 'inventory-svc' where the branch 'feat-4' includes a commit labeled 'feature 4', and there's an active pull request titled 'Feature 4' from 'feat-4' to 'main' with the label 'seo', following its closure and reopening; enumerate the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'inventory-svc'}),
            Action(name="CreateBranch", kwargs={'repo': 'inventory-svc', 'branch': 'feat-4'}),
            Action(name="AddCommit", kwargs={'repo': 'inventory-svc', 'branch': 'feat-4', 'message': 'feature 4'}),
            Action(name="OpenPr", kwargs={'repo': 'inventory-svc', 'head_branch': 'feat-4', 'base_branch': 'main', 'title': 'Feature 4'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'inventory-svc', 'number': 1, 'label': 'seo'}),
            Action(name="ClosePr", kwargs={'repo': 'inventory-svc', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'inventory-svc', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'inventory-svc', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 774
    Task(
        annotator="variation_7",
        user_id="task_774",
    instruction=(
        "Ensure the repository 'recommendation' is up to date, with branch 'feat-5' containing the commit 'feature 5'. There is a pull request titled 'Feature 5' from 'feat-5' to 'main' that must be reopened after closing and should have the 'ui' label; list the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'recommendation'}),
            Action(name="CreateBranch", kwargs={'repo': 'recommendation', 'branch': 'feat-5'}),
            Action(name="AddCommit", kwargs={'repo': 'recommendation', 'branch': 'feat-5', 'message': 'feature 5'}),
            Action(name="OpenPr", kwargs={'repo': 'recommendation', 'head_branch': 'feat-5', 'base_branch': 'main', 'title': 'Feature 5'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'recommendation', 'number': 1, 'label': 'ui'}),
            Action(name="ClosePr", kwargs={'repo': 'recommendation', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'recommendation', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'recommendation', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 775
    Task(
        annotator="variation_7",
        user_id="task_775",
    instruction=(
        "Handle the repository 'ab-testing' so that branch 'feat-6' includes the commit 'feature 6'. A pull request titled 'Feature 6' from 'feat-6' to 'main' needs to be reopened after being closed and must be tagged with 'docs'; display the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'ab-testing'}),
            Action(name="CreateBranch", kwargs={'repo': 'ab-testing', 'branch': 'feat-6'}),
            Action(name="AddCommit", kwargs={'repo': 'ab-testing', 'branch': 'feat-6', 'message': 'feature 6'}),
            Action(name="OpenPr", kwargs={'repo': 'ab-testing', 'head_branch': 'feat-6', 'base_branch': 'main', 'title': 'Feature 6'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'ab-testing', 'number': 1, 'label': 'docs'}),
            Action(name="ClosePr", kwargs={'repo': 'ab-testing', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'ab-testing', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'ab-testing', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 776
    Task(
        annotator="variation_7",
        user_id="task_776",
    instruction=(
        "Handle the repository 'experiments' ensuring branch 'feat-7' includes a commit 'feature 7', and manage a pull request titled 'Feature 7' moving from 'feat-7' to 'main' that remains open with label 'feature', post closure and reopening; display open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'experiments'}),
            Action(name="CreateBranch", kwargs={'repo': 'experiments', 'branch': 'feat-7'}),
            Action(name="AddCommit", kwargs={'repo': 'experiments', 'branch': 'feat-7', 'message': 'feature 7'}),
            Action(name="OpenPr", kwargs={'repo': 'experiments', 'head_branch': 'feat-7', 'base_branch': 'main', 'title': 'Feature 7'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'experiments', 'number': 1, 'label': 'feature'}),
            Action(name="ClosePr", kwargs={'repo': 'experiments', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'experiments', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'experiments', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 777
    Task(
        annotator="variation_7",
        user_id="task_777",
    instruction=(
        "Coordinate the repository 'feature-gates' ensuring branch 'feat-8' includes a commit 'feature 8', and manage a pull request titled 'Feature 8' moving from 'feat-8' to 'main' that remains open with label 'api', post closure and reopening; display open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'feature-gates'}),
            Action(name="CreateBranch", kwargs={'repo': 'feature-gates', 'branch': 'feat-8'}),
            Action(name="AddCommit", kwargs={'repo': 'feature-gates', 'branch': 'feat-8', 'message': 'feature 8'}),
            Action(name="OpenPr", kwargs={'repo': 'feature-gates', 'head_branch': 'feat-8', 'base_branch': 'main', 'title': 'Feature 8'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'feature-gates', 'number': 1, 'label': 'api'}),
            Action(name="ClosePr", kwargs={'repo': 'feature-gates', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'feature-gates', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'feature-gates', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 778
    Task(
        annotator="variation_7",
        user_id="task_778",
    instruction=(
        "Ensure that the repository 'content-api' is maintained, with branch 'feat-9' containing a commit 'feature 9'. There should be an open pull request titled 'Feature 9' from 'feat-9' to 'main', labeled 'ops', which has been closed and reopened; provide a list of open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'content-api'}),
            Action(name="CreateBranch", kwargs={'repo': 'content-api', 'branch': 'feat-9'}),
            Action(name="AddCommit", kwargs={'repo': 'content-api', 'branch': 'feat-9', 'message': 'feature 9'}),
            Action(name="OpenPr", kwargs={'repo': 'content-api', 'head_branch': 'feat-9', 'base_branch': 'main', 'title': 'Feature 9'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'content-api', 'number': 1, 'label': 'ops'}),
            Action(name="ClosePr", kwargs={'repo': 'content-api', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'content-api', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'content-api', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 779
    Task(
        annotator="variation_7",
        user_id="task_779",
    instruction=(
        "Ensure the repository 'feed-svc' is maintained, where branch 'feat-10' has a commit 'feature 10'. An open pull request titled 'Feature 10' from 'feat-10' to 'main' should exist, labeled 'security', after being closed and reopened; provide a list of open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'feed-svc'}),
            Action(name="CreateBranch", kwargs={'repo': 'feed-svc', 'branch': 'feat-10'}),
            Action(name="AddCommit", kwargs={'repo': 'feed-svc', 'branch': 'feat-10', 'message': 'feature 10'}),
            Action(name="OpenPr", kwargs={'repo': 'feed-svc', 'head_branch': 'feat-10', 'base_branch': 'main', 'title': 'Feature 10'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'feed-svc', 'number': 1, 'label': 'security'}),
            Action(name="ClosePr", kwargs={'repo': 'feed-svc', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'feed-svc', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'feed-svc', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 780
    Task(
        annotator="variation_7",
        user_id="task_780",
    instruction=(
        "Handle repository 'media-cdn', ensuring that the branch 'feat-11' includes a commit 'feature 11'. Make sure a pull request titled 'Feature 11' from 'feat-11' to 'main' is open, tagged with the label 'infra', after previously being closed and then reopened; list all open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'media-cdn'}),
            Action(name="CreateBranch", kwargs={'repo': 'media-cdn', 'branch': 'feat-11'}),
            Action(name="AddCommit", kwargs={'repo': 'media-cdn', 'branch': 'feat-11', 'message': 'feature 11'}),
            Action(name="OpenPr", kwargs={'repo': 'media-cdn', 'head_branch': 'feat-11', 'base_branch': 'main', 'title': 'Feature 11'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'media-cdn', 'number': 1, 'label': 'infra'}),
            Action(name="ClosePr", kwargs={'repo': 'media-cdn', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'media-cdn', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'media-cdn', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 781
    Task(
        annotator="variation_7",
        user_id="task_781",
    instruction=(
        "Manage repository 'avatar-gen', confirming the branch 'feat-12' contains a commit 'feature 12'. Ensure that a pull request named 'Feature 12' from 'feat-12' to 'main' is open and marked with the label 'seo', following its closure and reopening; list all open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'avatar-gen'}),
            Action(name="CreateBranch", kwargs={'repo': 'avatar-gen', 'branch': 'feat-12'}),
            Action(name="AddCommit", kwargs={'repo': 'avatar-gen', 'branch': 'feat-12', 'message': 'feature 12'}),
            Action(name="OpenPr", kwargs={'repo': 'avatar-gen', 'head_branch': 'feat-12', 'base_branch': 'main', 'title': 'Feature 12'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'avatar-gen', 'number': 1, 'label': 'seo'}),
            Action(name="ClosePr", kwargs={'repo': 'avatar-gen', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'avatar-gen', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'avatar-gen', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 782
    Task(
        annotator="variation_7",
        user_id="task_782",
    instruction=(
        "Ensure the upkeep of the repository 'geo-routing', in which branch 'feat-13' includes a commit 'feature 13'. There is also a pull request titled 'Feature 13', moving from 'feat-13' to 'main', which is labeled 'ui' and reopened after closure; detail the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'geo-routing'}),
            Action(name="CreateBranch", kwargs={'repo': 'geo-routing', 'branch': 'feat-13'}),
            Action(name="AddCommit", kwargs={'repo': 'geo-routing', 'branch': 'feat-13', 'message': 'feature 13'}),
            Action(name="OpenPr", kwargs={'repo': 'geo-routing', 'head_branch': 'feat-13', 'base_branch': 'main', 'title': 'Feature 13'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'geo-routing', 'number': 1, 'label': 'ui'}),
            Action(name="ClosePr", kwargs={'repo': 'geo-routing', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'geo-routing', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'geo-routing', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 783
    Task(
        annotator="variation_7",
        user_id="task_783",
    instruction=(
        "Manage the repository 'fraud-detect', focusing on branch 'feat-14' with its commit 'feature 14'. A pull request named 'Feature 14' is in process from 'feat-14' to 'main', carrying the 'docs' label and has been reopened after closing; enumerate the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'fraud-detect'}),
            Action(name="CreateBranch", kwargs={'repo': 'fraud-detect', 'branch': 'feat-14'}),
            Action(name="AddCommit", kwargs={'repo': 'fraud-detect', 'branch': 'feat-14', 'message': 'feature 14'}),
            Action(name="OpenPr", kwargs={'repo': 'fraud-detect', 'head_branch': 'feat-14', 'base_branch': 'main', 'title': 'Feature 14'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'fraud-detect', 'number': 1, 'label': 'docs'}),
            Action(name="ClosePr", kwargs={'repo': 'fraud-detect', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'fraud-detect', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'fraud-detect', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 784
    Task(
        annotator="variation_7",
        user_id="task_784",
    instruction=(
        "Handle the maintenance of repository 'vector-search' where the branch 'feat-15' includes a commit 'feature 15', and ensure a pull request titled 'Feature 15' from 'feat-15' to 'main' remains open with the label 'feature', after having been closed and reopened; enumerate the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'vector-search'}),
            Action(name="CreateBranch", kwargs={'repo': 'vector-search', 'branch': 'feat-15'}),
            Action(name="AddCommit", kwargs={'repo': 'vector-search', 'branch': 'feat-15', 'message': 'feature 15'}),
            Action(name="OpenPr", kwargs={'repo': 'vector-search', 'head_branch': 'feat-15', 'base_branch': 'main', 'title': 'Feature 15'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'vector-search', 'number': 1, 'label': 'feature'}),
            Action(name="ClosePr", kwargs={'repo': 'vector-search', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'vector-search', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'vector-search', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 785
    Task(
        annotator="variation_7",
        user_id="task_785",
    instruction=(
        "Handle the maintenance of repository 'sso-portal' where the branch 'feat-16' contains a commit 'feature 16', and ensure a pull request titled 'Feature 16' from 'feat-16' to 'main' stays open with the label 'api', after being closed and reopened; enumerate the open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'sso-portal'}),
            Action(name="CreateBranch", kwargs={'repo': 'sso-portal', 'branch': 'feat-16'}),
            Action(name="AddCommit", kwargs={'repo': 'sso-portal', 'branch': 'feat-16', 'message': 'feature 16'}),
            Action(name="OpenPr", kwargs={'repo': 'sso-portal', 'head_branch': 'feat-16', 'base_branch': 'main', 'title': 'Feature 16'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'sso-portal', 'number': 1, 'label': 'api'}),
            Action(name="ClosePr", kwargs={'repo': 'sso-portal', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'sso-portal', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'sso-portal', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 786
    Task(
        annotator="variation_7",
        user_id="task_786",
    instruction=(
        "Ensure the repository 'tenant-admin' is managed where branch 'feat-17' includes a commit 'feature 17', and a pull request called 'Feature 17' from 'feat-17' to 'main' remains open with label 'ops', especially after it was closed and reopened; enumerate open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'tenant-admin'}),
            Action(name="CreateBranch", kwargs={'repo': 'tenant-admin', 'branch': 'feat-17'}),
            Action(name="AddCommit", kwargs={'repo': 'tenant-admin', 'branch': 'feat-17', 'message': 'feature 17'}),
            Action(name="OpenPr", kwargs={'repo': 'tenant-admin', 'head_branch': 'feat-17', 'base_branch': 'main', 'title': 'Feature 17'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'tenant-admin', 'number': 1, 'label': 'ops'}),
            Action(name="ClosePr", kwargs={'repo': 'tenant-admin', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'tenant-admin', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'tenant-admin', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 787
    Task(
        annotator="variation_7",
        user_id="task_787",
    instruction=(
        "Ensure the repository 'workspace-api' is managed where branch 'feat-18' includes a commit 'feature 18', and a pull request titled 'Feature 18' from 'feat-18' to 'main' stays open with label 'security', especially after being shut and reinitiated; enumerate open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'workspace-api'}),
            Action(name="CreateBranch", kwargs={'repo': 'workspace-api', 'branch': 'feat-18'}),
            Action(name="AddCommit", kwargs={'repo': 'workspace-api', 'branch': 'feat-18', 'message': 'feature 18'}),
            Action(name="OpenPr", kwargs={'repo': 'workspace-api', 'head_branch': 'feat-18', 'base_branch': 'main', 'title': 'Feature 18'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'workspace-api', 'number': 1, 'label': 'security'}),
            Action(name="ClosePr", kwargs={'repo': 'workspace-api', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'workspace-api', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'workspace-api', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 788
    Task(
        annotator="variation_7",
        user_id="task_788",
    instruction=(
        "Ensure the repository 'notes-app' is maintained. Branch 'feat-19' contains a commit 'feature 19', and there is a pull request labeled 'infra' titled 'Feature 19' from 'feat-19' to 'main' that has been closed and reopened; display any open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'notes-app'}),
            Action(name="CreateBranch", kwargs={'repo': 'notes-app', 'branch': 'feat-19'}),
            Action(name="AddCommit", kwargs={'repo': 'notes-app', 'branch': 'feat-19', 'message': 'feature 19'}),
            Action(name="OpenPr", kwargs={'repo': 'notes-app', 'head_branch': 'feat-19', 'base_branch': 'main', 'title': 'Feature 19'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'notes-app', 'number': 1, 'label': 'infra'}),
            Action(name="ClosePr", kwargs={'repo': 'notes-app', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'notes-app', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'notes-app', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 789
    Task(
        annotator="variation_7",
        user_id="task_789",
    instruction=(
        "Ensure the repository 'doc-editor' is maintained. Branch 'feat-20' includes a commit 'feature 20', and there is a pull request labeled 'seo' titled 'Feature 20' from 'feat-20' to 'main' that has been closed and reopened; display any open PRs."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'doc-editor'}),
            Action(name="CreateBranch", kwargs={'repo': 'doc-editor', 'branch': 'feat-20'}),
            Action(name="AddCommit", kwargs={'repo': 'doc-editor', 'branch': 'feat-20', 'message': 'feature 20'}),
            Action(name="OpenPr", kwargs={'repo': 'doc-editor', 'head_branch': 'feat-20', 'base_branch': 'main', 'title': 'Feature 20'}),
            Action(name="AddLabel", kwargs={'kind': 'pr', 'repo': 'doc-editor', 'number': 1, 'label': 'seo'}),
            Action(name="ClosePr", kwargs={'repo': 'doc-editor', 'number': 1}),
            Action(name="ReopenPr", kwargs={'repo': 'doc-editor', 'number': 1}),
            Action(name="ListPrs", kwargs={'repo': 'doc-editor', 'state': 'open'}),
        ],
        outputs=[]
    ),

    # 790
    Task(
        annotator="variation_7",
        user_id="task_790",
    instruction=(
        "Establish a repository 'renderer' tagged with topics ['ui', 'components'], make the commits 'init topics' and 'readme', and verify branches to confirm 'main' exists."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'renderer'}),
            Action(name="RepoTopics", kwargs={'repo': 'renderer', 'topics': ['ui', 'components']}),
            Action(name="AddCommit", kwargs={'repo': 'renderer', 'message': 'init topics'}),
            Action(name="AddCommit", kwargs={'repo': 'renderer', 'message': 'readme'}),
            Action(name="ListBranches", kwargs={'repo': 'renderer'}),
        ],
        outputs=[]
    ),

    # 791
    Task(
        annotator="variation_7",
        user_id="task_791",
    instruction=(
        "Set up a repository 'state-store' with the specified topics ['cli', 'tools'], execute the commits 'init topics' and 'readme', and check branches to ensure 'main' is present."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'state-store'}),
            Action(name="RepoTopics", kwargs={'repo': 'state-store', 'topics': ['cli', 'tools']}),
            Action(name="AddCommit", kwargs={'repo': 'state-store', 'message': 'init topics'}),
            Action(name="AddCommit", kwargs={'repo': 'state-store', 'message': 'readme'}),
            Action(name="ListBranches", kwargs={'repo': 'state-store'}),
        ],
        outputs=[]
    ),

    # 792
    Task(
        annotator="variation_7",
        user_id="task_792",
    instruction=(
        "Establish a repository named 'odata-gw' with the topics ['security', 'auth'], make the commit 'init topics' along with 'readme', and display branches to confirm 'main' is present."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'odata-gw'}),
            Action(name="RepoTopics", kwargs={'repo': 'odata-gw', 'topics': ['security', 'auth']}),
            Action(name="AddCommit", kwargs={'repo': 'odata-gw', 'message': 'init topics'}),
            Action(name="AddCommit", kwargs={'repo': 'odata-gw', 'message': 'readme'}),
            Action(name="ListBranches", kwargs={'repo': 'odata-gw'}),
        ],
        outputs=[]
    ),

    # 793
    Task(
        annotator="variation_7",
        user_id="task_793",
    instruction=(
        "Set up a repository entitled 'image-filter' with the topics ['data', 'etl'], perform the commit 'init topics' as well as 'readme', and list branches to verify 'main' is present."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'image-filter'}),
            Action(name="RepoTopics", kwargs={'repo': 'image-filter', 'topics': ['data', 'etl']}),
            Action(name="AddCommit", kwargs={'repo': 'image-filter', 'message': 'init topics'}),
            Action(name="AddCommit", kwargs={'repo': 'image-filter', 'message': 'readme'}),
            Action(name="ListBranches", kwargs={'repo': 'image-filter'}),
        ],
        outputs=[]
    ),

    # 794
    Task(
        annotator="variation_7",
        user_id="task_794",
    instruction=(
        "Handle the creation of a repository 'push-gw' with topics ['ops', 'cron'], incorporate commit 'init topics' and commit 'readme', and list branches to verify the presence of 'main'."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'push-gw'}),
            Action(name="RepoTopics", kwargs={'repo': 'push-gw', 'topics': ['ops', 'cron']}),
            Action(name="AddCommit", kwargs={'repo': 'push-gw', 'message': 'init topics'}),
            Action(name="AddCommit", kwargs={'repo': 'push-gw', 'message': 'readme'}),
            Action(name="ListBranches", kwargs={'repo': 'push-gw'}),
        ],
        outputs=[]
    ),

    # 795
    Task(
        annotator="variation_7",
        user_id="task_795",
    instruction=(
        "Coordinate the setup of a repository 'sync-agent' with topics ['api', 'gateway'], include commit 'init topics' and commit 'readme', and list branches to confirm 'main' is present."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'sync-agent'}),
            Action(name="RepoTopics", kwargs={'repo': 'sync-agent', 'topics': ['api', 'gateway']}),
            Action(name="AddCommit", kwargs={'repo': 'sync-agent', 'message': 'init topics'}),
            Action(name="AddCommit", kwargs={'repo': 'sync-agent', 'message': 'readme'}),
            Action(name="ListBranches", kwargs={'repo': 'sync-agent'}),
        ],
        outputs=[]
    ),

    # 796
    Task(
        annotator="variation_7",
        user_id="task_796",
    instruction=(
        "Handle the creation of a repository named 'idp-core' with topics ['ml', 'models'], add the commits 'init topics' and 'readme', then display the branches to confirm the existence of 'main'."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'idp-core'}),
            Action(name="RepoTopics", kwargs={'repo': 'idp-core', 'topics': ['ml', 'models']}),
            Action(name="AddCommit", kwargs={'repo': 'idp-core', 'message': 'init topics'}),
            Action(name="AddCommit", kwargs={'repo': 'idp-core', 'message': 'readme'}),
            Action(name="ListBranches", kwargs={'repo': 'idp-core'}),
        ],
        outputs=[]
    ),

    # 797
    Task(
        annotator="variation_7",
        user_id="task_797",
    instruction=(
        "Coordinate the establishment of a repository called 'policy-svc' with topics ['search', 'index'], add the commits 'init topics' and 'readme', and then list the branches to verify that 'main' is present."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'policy-svc'}),
            Action(name="RepoTopics", kwargs={'repo': 'policy-svc', 'topics': ['search', 'index']}),
            Action(name="AddCommit", kwargs={'repo': 'policy-svc', 'message': 'init topics'}),
            Action(name="AddCommit", kwargs={'repo': 'policy-svc', 'message': 'readme'}),
            Action(name="ListBranches", kwargs={'repo': 'policy-svc'}),
        ],
        outputs=[]
    ),

    # 798
    Task(
        annotator="variation_7",
        user_id="task_798",
    instruction=(
        "Handle the creation of a repository named 'usage-collector' with the topics ['media', 'cdn'], commit 'init topics' followed by 'readme', and then list branches to confirm the presence of 'main'."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'usage-collector'}),
            Action(name="RepoTopics", kwargs={'repo': 'usage-collector', 'topics': ['media', 'cdn']}),
            Action(name="AddCommit", kwargs={'repo': 'usage-collector', 'message': 'init topics'}),
            Action(name="AddCommit", kwargs={'repo': 'usage-collector', 'message': 'readme'}),
            Action(name="ListBranches", kwargs={'repo': 'usage-collector'}),
        ],
        outputs=[]
    ),

    # 799
    Task(
        annotator="variation_7",
        user_id="task_799",
    instruction=(
        "Handle the creation of a repository named 'query-planner' with the topics ['geo', 'routing'], commit 'init topics' followed by 'readme', and then list branches to confirm the presence of 'main'."
    ),
        actions=[
            Action(name="CreateRepo", kwargs={'name': 'query-planner'}),
            Action(name="RepoTopics", kwargs={'repo': 'query-planner', 'topics': ['geo', 'routing']}),
            Action(name="AddCommit", kwargs={'repo': 'query-planner', 'message': 'init topics'}),
            Action(name="AddCommit", kwargs={'repo': 'query-planner', 'message': 'readme'}),
            Action(name="ListBranches", kwargs={'repo': 'query-planner'}),
        ],
        outputs=[]
    ),
]
