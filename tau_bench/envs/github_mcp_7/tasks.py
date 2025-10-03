
tasks = [
    {
        "annotator": variation_7,
        "user_id": "task_700",
        "instruction": "Handle repository 'blog-lite' to ensure that a pull request is open from branch 'feature-home' to 'main', with the label 'docs' attached. Once this condition is fulfilled, list the open pull requests for 'blog-lite'.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "blog-lite"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "blog-lite",
                    "branch": "feature-home"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "blog-lite",
                    "branch": "feature-home",
                    "message": "setup index"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "blog-lite",
                    "head_branch": "feature-home",
                    "base_branch": "main",
                    "title": "Home section"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "blog-lite",
                    "number": 1,
                    "label": "docs"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "blog-lite",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"docs\"",
                "\"title\": \"Home section\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_701",
        "instruction": "Coordinate the repository 'support-bot' such that branch 'resize' contains a commit 'add resize', and a pull request titled 'Resize feature' is open from 'resize' to 'main' with the label 'feature'. Afterward, list the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "support-bot"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "support-bot",
                    "branch": "resize"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "support-bot",
                    "branch": "resize",
                    "message": "add resize"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "support-bot",
                    "head_branch": "resize",
                    "base_branch": "main",
                    "title": "Resize feature"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "support-bot",
                    "number": 1,
                    "label": "feature"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "support-bot",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"feature\"",
                "\"title\": \"Resize feature\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_702",
        "instruction": "Ensure the repository 'img-tool' comprises a branch 'readme' with a commit 'write readme'. There should be an open pull request titled 'README' from 'readme' to 'main' with the label 'api'. After confirming this, list all open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "img-tool"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "img-tool",
                    "branch": "readme"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "img-tool",
                    "branch": "readme",
                    "message": "write readme"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "img-tool",
                    "head_branch": "readme",
                    "base_branch": "main",
                    "title": "README"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "img-tool",
                    "number": 1,
                    "label": "api"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "img-tool",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"api\"",
                "\"title\": \"README\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_703",
        "instruction": "Verify that the repository 'calc-pro' features an open pull request from branch 'daily-cron' to 'main', marked with the label 'ops'. Once this condition is met, proceed to list the open pull requests for 'calc-pro'.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "calc-pro"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "calc-pro",
                    "branch": "daily-cron"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "calc-pro",
                    "branch": "daily-cron",
                    "message": "cron impl"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "calc-pro",
                    "head_branch": "daily-cron",
                    "base_branch": "main",
                    "title": "Cron jobs"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "calc-pro",
                    "number": 1,
                    "label": "ops"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "calc-pro",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ops\"",
                "\"title\": \"Cron jobs\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_704",
        "instruction": "Handle the maintenance of the repository 'docs-kit' with a branch 'badges' containing a commit 'README badges', ensuring there is a pull request titled 'README badges' from 'badges' to 'main' that is open with the label 'security'; provide a list of open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "docs-kit"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "docs-kit",
                    "branch": "badges"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "docs-kit",
                    "branch": "badges",
                    "message": "README badges"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "docs-kit",
                    "head_branch": "badges",
                    "base_branch": "main",
                    "title": "README badges"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "docs-kit",
                    "number": 1,
                    "label": "security"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "docs-kit",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"security\"",
                "\"title\": \"README badges\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_705",
        "instruction": "Coordinate the maintenance of the repository 'portal-ui' where the branch 'theme' includes a commit 'dark theme', and there is a pull request titled 'Dark theme' from 'theme' to 'main' open with the label 'infra'; supply a list of open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "portal-ui"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "portal-ui",
                    "branch": "theme"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "portal-ui",
                    "branch": "theme",
                    "message": "dark theme"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "portal-ui",
                    "head_branch": "theme",
                    "base_branch": "main",
                    "title": "Dark theme"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "portal-ui",
                    "number": 1,
                    "label": "infra"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "portal-ui",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"infra\"",
                "\"title\": \"Dark theme\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_706",
        "instruction": "Handle the repository 'backup-tool' where the branch 'index-v2' includes a commit labeled 'add indexer', and a pull request titled 'Indexer v2' from 'index-v2' to 'main' is currently open with the label 'seo'; enumerate the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "backup-tool"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "backup-tool",
                    "branch": "index-v2"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "backup-tool",
                    "branch": "index-v2",
                    "message": "add indexer"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "backup-tool",
                    "head_branch": "index-v2",
                    "base_branch": "main",
                    "title": "Indexer v2"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "backup-tool",
                    "number": 1,
                    "label": "seo"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "backup-tool",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"seo\"",
                "\"title\": \"Indexer v2\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_707",
        "instruction": "Manage the repository 'pkg-index' where the branch 'smtp' contains a commit called 'smtp auth', and a pull request titled 'SMTP auth' from 'smtp' to 'main' is presently open, marked with the label 'ui'; list the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "pkg-index"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "pkg-index",
                    "branch": "smtp"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "pkg-index",
                    "branch": "smtp",
                    "message": "smtp auth"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "pkg-index",
                    "head_branch": "smtp",
                    "base_branch": "main",
                    "title": "SMTP auth"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "pkg-index",
                    "number": 1,
                    "label": "ui"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "pkg-index",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ui\"",
                "\"title\": \"SMTP auth\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_708",
        "instruction": "Handle the repository 'core-lib' ensuring the branch 'landing' includes a commit 'hero copy', and the pull request named 'Landing page' from 'landing' to 'main' remains open with the label 'docs'; enumerate open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "core-lib"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "core-lib",
                    "branch": "landing"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "core-lib",
                    "branch": "landing",
                    "message": "hero copy"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "core-lib",
                    "head_branch": "landing",
                    "base_branch": "main",
                    "title": "Landing page"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "core-lib",
                    "number": 1,
                    "label": "docs"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "core-lib",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"docs\"",
                "\"title\": \"Landing page\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_709",
        "instruction": "Coordinate the maintenance of repository 'data-cleaner' where the branch 'tax' contains the commit 'add vat', and ensure that the pull request titled 'VAT support' from 'tax' to 'main' is open with the label 'feature'; enumerate open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "data-cleaner"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "data-cleaner",
                    "branch": "tax"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "data-cleaner",
                    "branch": "tax",
                    "message": "add vat"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "data-cleaner",
                    "head_branch": "tax",
                    "base_branch": "main",
                    "title": "VAT support"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "data-cleaner",
                    "number": 1,
                    "label": "feature"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "data-cleaner",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"feature\"",
                "\"title\": \"VAT support\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_710",
        "instruction": "Handle repository 'docs-kit-plus' to ensure it's in the following condition: branch 'sitemap' contains a commit 'gen sitemap'; an open pull request titled 'Sitemap' is present from 'sitemap' to 'main' with label 'api'. Then, provide the list of open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "docs-kit-plus"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "docs-kit-plus",
                    "branch": "sitemap"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "docs-kit-plus",
                    "branch": "sitemap",
                    "message": "gen sitemap"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "docs-kit-plus",
                    "head_branch": "sitemap",
                    "base_branch": "main",
                    "title": "Sitemap"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "docs-kit-plus",
                    "number": 1,
                    "label": "api"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "docs-kit-plus",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"api\"",
                "\"title\": \"Sitemap\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_711",
        "instruction": "Coordinate repository 'payments-svc' ensuring branch 'pd' holds a commit 'pagerduty hook', and that a pull request titled 'PagerDuty webhook' from 'pd' to 'main' is open and bears the label 'ops'; enumerate the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "payments-svc"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "payments-svc",
                    "branch": "pd"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "payments-svc",
                    "branch": "pd",
                    "message": "pagerduty hook"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "payments-svc",
                    "head_branch": "pd",
                    "base_branch": "main",
                    "title": "PagerDuty webhook"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "payments-svc",
                    "number": 1,
                    "label": "ops"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "payments-svc",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ops\"",
                "\"title\": \"PagerDuty webhook\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_712",
        "instruction": "Handle repository 'cli-tool' by ensuring branch 'embeddings' contains the commit 'add sbert', and there's a pull request with the title 'Embeddings' from 'embeddings' to 'main' labeled 'security'; enumerate open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "cli-tool"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "cli-tool",
                    "branch": "embeddings"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "cli-tool",
                    "branch": "embeddings",
                    "message": "add sbert"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "cli-tool",
                    "head_branch": "embeddings",
                    "base_branch": "main",
                    "title": "Embeddings"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "cli-tool",
                    "number": 1,
                    "label": "security"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "cli-tool",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"security\"",
                "\"title\": \"Embeddings\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_713",
        "instruction": "Handle repository 'scheduler' by ensuring branch 'sms' contains the commit 'twilio', and there's a pull request with the title 'SMS support' from 'sms' to 'main' labeled 'infra'; enumerate open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "scheduler"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "scheduler",
                    "branch": "sms"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "scheduler",
                    "branch": "sms",
                    "message": "twilio"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "scheduler",
                    "head_branch": "sms",
                    "base_branch": "main",
                    "title": "SMS support"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "scheduler",
                    "number": 1,
                    "label": "infra"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "scheduler",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"infra\"",
                "\"title\": \"SMS support\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_714",
        "instruction": "Handle the 'search-api' repository where the 'geojson' branch includes a commit named 'import geojson', and a pull request titled 'GeoJSON import' from 'geojson' to 'main' is active with the label 'seo'. Enumerate the open pull requests.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "search-api"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "search-api",
                    "branch": "geojson"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "search-api",
                    "branch": "geojson",
                    "message": "import geojson"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "search-api",
                    "head_branch": "geojson",
                    "base_branch": "main",
                    "title": "GeoJSON import"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "search-api",
                    "number": 1,
                    "label": "seo"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "search-api",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"seo\"",
                "\"title\": \"GeoJSON import\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_715",
        "instruction": "Handle the 'monitor' repository where the 'batch' branch contains a commit called 'batch process', and a pull request titled 'Batch process' from 'batch' to 'main' is open with the label 'ui'. Enumerate the open pull requests.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "monitor"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "monitor",
                    "branch": "batch"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "monitor",
                    "branch": "batch",
                    "message": "batch process"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "monitor",
                    "head_branch": "batch",
                    "base_branch": "main",
                    "title": "Batch process"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "monitor",
                    "number": 1,
                    "label": "ui"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "monitor",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ui\"",
                "\"title\": \"Batch process\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_716",
        "instruction": "Verify that repository 'mail-svc' is configured as follows: branch 'reply' should contain a commit named 'quick replies'; an open pull request titled 'Quick replies' should be present from 'reply' to 'main' with the label 'docs'. Afterward, provide the list of open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "mail-svc"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "mail-svc",
                    "branch": "reply"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "mail-svc",
                    "branch": "reply",
                    "message": "quick replies"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "mail-svc",
                    "head_branch": "reply",
                    "base_branch": "main",
                    "title": "Quick replies"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "mail-svc",
                    "number": 1,
                    "label": "docs"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "mail-svc",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"docs\"",
                "\"title\": \"Quick replies\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_717",
        "instruction": "Manage repository 'report-gen' to ensure branch 'nightly' has a commit 'cron spec', and an open pull request titled 'Nightly cron' should exist from 'nightly' to 'main' with the label 'feature'; then, display the list of open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "report-gen"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "report-gen",
                    "branch": "nightly"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "report-gen",
                    "branch": "nightly",
                    "message": "cron spec"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "report-gen",
                    "head_branch": "nightly",
                    "base_branch": "main",
                    "title": "Nightly cron"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "report-gen",
                    "number": 1,
                    "label": "feature"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "report-gen",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"feature\"",
                "\"title\": \"Nightly cron\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_718",
        "instruction": "Ensure the repository 'auth-svc' is maintained, where the branch 'android-ci' contains a commit 'gradle fix', and a pull request named 'Android CI' from 'android-ci' to 'main' is open with the label 'api'. List any open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "auth-svc"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "auth-svc",
                    "branch": "android-ci"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "auth-svc",
                    "branch": "android-ci",
                    "message": "gradle fix"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "auth-svc",
                    "head_branch": "android-ci",
                    "base_branch": "main",
                    "title": "Android CI"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "auth-svc",
                    "number": 1,
                    "label": "api"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "auth-svc",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"api\"",
                "\"title\": \"Android CI\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_719",
        "instruction": "Take care of the repository 'ui-lib', ensuring the branch 'dag' includes a commit 'add dag', and an open pull request titled 'Airflow DAG' from 'dag' to 'main' exists with label 'ops'. List the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "ui-lib"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "ui-lib",
                    "branch": "dag"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "ui-lib",
                    "branch": "dag",
                    "message": "add dag"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "ui-lib",
                    "head_branch": "dag",
                    "base_branch": "main",
                    "title": "Airflow DAG"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "ui-lib",
                    "number": 1,
                    "label": "ops"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "ui-lib",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ops\"",
                "\"title\": \"Airflow DAG\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_720",
        "instruction": "Ensure the 'db-migrator' repository is maintained, specifically where branch 'minimax' contains a commit labeled 'minimax', and there is an existing pull request named 'Add minimax' from 'minimax' to 'main' with a 'security' label. Compile a list of open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "db-migrator"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "db-migrator",
                    "branch": "minimax"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "db-migrator",
                    "branch": "minimax",
                    "message": "minimax"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "db-migrator",
                    "head_branch": "minimax",
                    "base_branch": "main",
                    "title": "Add minimax"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "db-migrator",
                    "number": 1,
                    "label": "security"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "db-migrator",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"security\"",
                "\"title\": \"Add minimax\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_721",
        "instruction": "Ensure the 'kafka-consumer' repository is maintained, particularly where the 'tiles' branch includes a commit titled 'tile cache', and an open pull request named 'Tile cache' exists from 'tiles' to 'main' with the label 'infra'. Compile a list of open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "kafka-consumer"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "kafka-consumer",
                    "branch": "tiles"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "kafka-consumer",
                    "branch": "tiles",
                    "message": "tile cache"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "kafka-consumer",
                    "head_branch": "tiles",
                    "base_branch": "main",
                    "title": "Tile cache"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "kafka-consumer",
                    "number": 1,
                    "label": "infra"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "kafka-consumer",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"infra\"",
                "\"title\": \"Tile cache\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_722",
        "instruction": "Manage the repository 'notifier' where the 'session' branch has a commit called 'session mgmt', and there's an open pull request titled 'Session init' from 'session' to 'main' with the label 'seo'; enumerate open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "notifier"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "notifier",
                    "branch": "session"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "notifier",
                    "branch": "session",
                    "message": "session mgmt"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "notifier",
                    "head_branch": "session",
                    "base_branch": "main",
                    "title": "Session init"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "notifier",
                    "number": 1,
                    "label": "seo"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "notifier",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"seo\"",
                "\"title\": \"Session init\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_723",
        "instruction": "Oversee the repository 'crawler' where the 'etl' branch includes a commit labeled 'etl script', and there's an open pull request titled 'ETL v1' from 'etl' to 'main' with the label 'ui'; enumerate open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "crawler"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "crawler",
                    "branch": "etl"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "crawler",
                    "branch": "etl",
                    "message": "etl script"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "crawler",
                    "head_branch": "etl",
                    "base_branch": "main",
                    "title": "ETL v1"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "crawler",
                    "number": 1,
                    "label": "ui"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "crawler",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ui\"",
                "\"title\": \"ETL v1\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_724",
        "instruction": "Ensure repository 'logger' is up-to-date, with branch 'vat' containing a commit 'vat rounding'. An open pull request titled 'VAT rounding' should exist from 'vat' to 'main', labeled 'docs'. Please list the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "logger"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "logger",
                    "branch": "vat"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "logger",
                    "branch": "vat",
                    "message": "vat rounding"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "logger",
                    "head_branch": "vat",
                    "base_branch": "main",
                    "title": "VAT rounding"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "logger",
                    "number": 1,
                    "label": "docs"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "logger",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"docs\"",
                "\"title\": \"VAT rounding\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_725",
        "instruction": "Ensure repository 'game-ai' is maintained, with branch 'cron' containing a commit 'cron jobs'. An open pull request titled 'Cron jobs v2' should exist from 'cron' to 'main', labeled 'feature'. Please list the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "game-ai"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "game-ai",
                    "branch": "cron"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "game-ai",
                    "branch": "cron",
                    "message": "cron jobs"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "game-ai",
                    "head_branch": "cron",
                    "base_branch": "main",
                    "title": "Cron jobs v2"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "game-ai",
                    "number": 1,
                    "label": "feature"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "game-ai",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"feature\"",
                "\"title\": \"Cron jobs v2\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_726",
        "instruction": "Ensure the management of the repository 'image-cdn' where the 'oauth' branch includes a commit 'oauth route', and there's an active pull request titled 'OAuth route' from 'oauth' to 'main' with the label 'api'; enumerate open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "image-cdn"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "image-cdn",
                    "branch": "oauth"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "image-cdn",
                    "branch": "oauth",
                    "message": "oauth route"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "image-cdn",
                    "head_branch": "oauth",
                    "base_branch": "main",
                    "title": "OAuth route"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "image-cdn",
                    "number": 1,
                    "label": "api"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "image-cdn",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"api\"",
                "\"title\": \"OAuth route\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_727",
        "instruction": "Oversee the repository 'analytics' where the 'graphql' branch contains a commit 'schema', and an existing pull request is titled 'GraphQL schema' from 'graphql' to 'main' with the label 'ops'; enumerate open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "analytics"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "analytics",
                    "branch": "graphql"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "analytics",
                    "branch": "graphql",
                    "message": "schema"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "analytics",
                    "head_branch": "graphql",
                    "base_branch": "main",
                    "title": "GraphQL schema"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "analytics",
                    "number": 1,
                    "label": "ops"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "analytics",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ops\"",
                "\"title\": \"GraphQL schema\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_728",
        "instruction": "Handle the repository 'seo-helper', ensuring the branch 'avatars' includes a commit 'avatar gen', and there is an open pull request titled 'Avatar generator' from 'avatars' to 'main' with the label 'security'; list open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "seo-helper"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "seo-helper",
                    "branch": "avatars"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "seo-helper",
                    "branch": "avatars",
                    "message": "avatar gen"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "seo-helper",
                    "head_branch": "avatars",
                    "base_branch": "main",
                    "title": "Avatar generator"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "seo-helper",
                    "number": 1,
                    "label": "security"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "seo-helper",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"security\"",
                "\"title\": \"Avatar generator\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_729",
        "instruction": "Coordinate the repository 'release-bot', ensuring the branch 'payments' contains a commit 'fee calc', and there is an open pull request titled 'Fee calc' from 'payments' to 'main' with the label 'infra'; list open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "release-bot"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "release-bot",
                    "branch": "payments"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "release-bot",
                    "branch": "payments",
                    "message": "fee calc"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "release-bot",
                    "head_branch": "payments",
                    "base_branch": "main",
                    "title": "Fee calc"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "release-bot",
                    "number": 1,
                    "label": "infra"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "release-bot",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"infra\"",
                "\"title\": \"Fee calc\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_730",
        "instruction": "Handle the repository 'docs-site' with the branch 'profiles' that contains a commit 'profile page', and ensure that there is an open pull request titled 'Profile page' from 'profiles' to 'main' with the label 'seo'; enumerate any open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "docs-site"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "docs-site",
                    "branch": "profiles"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "docs-site",
                    "branch": "profiles",
                    "message": "profile page"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "docs-site",
                    "head_branch": "profiles",
                    "base_branch": "main",
                    "title": "Profile page"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "docs-site",
                    "number": 1,
                    "label": "seo"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "docs-site",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"seo\"",
                "\"title\": \"Profile page\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_731",
        "instruction": "Coordinate the management of the repository 'billing-svc' with the branch 'events' containing a commit 'event bus', and verify that an open pull request titled 'Event bus' from 'events' to 'main' exists with the label 'ui'; enumerate the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "billing-svc"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "billing-svc",
                    "branch": "events"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "billing-svc",
                    "branch": "events",
                    "message": "event bus"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "billing-svc",
                    "head_branch": "events",
                    "base_branch": "main",
                    "title": "Event bus"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "billing-svc",
                    "number": 1,
                    "label": "ui"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "billing-svc",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ui\"",
                "\"title\": \"Event bus\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_732",
        "instruction": "Ensure the repository 'feature-flag' is maintained, where the branch 'comments' includes a commit 'comment form', and there's an open pull request titled 'Comments UI' from 'comments' to 'main' with the label 'docs'; show the open pull requests.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "feature-flag"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "feature-flag",
                    "branch": "comments"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "feature-flag",
                    "branch": "comments",
                    "message": "comment form"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "feature-flag",
                    "head_branch": "comments",
                    "base_branch": "main",
                    "title": "Comments UI"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "feature-flag",
                    "number": 1,
                    "label": "docs"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "feature-flag",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"docs\"",
                "\"title\": \"Comments UI\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_733",
        "instruction": "Ensure the repository 'cache-layer' is maintained, where the branch 'notify' includes a commit 'notify rules', and there's an open pull request titled 'Notify rules' from 'notify' to 'main' with the label 'feature'; show the open pull requests.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "cache-layer"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "cache-layer",
                    "branch": "notify"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "cache-layer",
                    "branch": "notify",
                    "message": "notify rules"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "cache-layer",
                    "head_branch": "notify",
                    "base_branch": "main",
                    "title": "Notify rules"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "cache-layer",
                    "number": 1,
                    "label": "feature"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "cache-layer",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"feature\"",
                "\"title\": \"Notify rules\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_734",
        "instruction": "Ensure the repository 'ml-pipeline' is kept up to date where the 'realtime' branch includes a commit 'socket hub', and there is a pull request titled 'Realtime hub' from 'realtime' to 'main' which is open with the label 'api'; enumerate the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "ml-pipeline"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "ml-pipeline",
                    "branch": "realtime"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "ml-pipeline",
                    "branch": "realtime",
                    "message": "socket hub"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "ml-pipeline",
                    "head_branch": "realtime",
                    "base_branch": "main",
                    "title": "Realtime hub"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "ml-pipeline",
                    "number": 1,
                    "label": "api"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "ml-pipeline",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"api\"",
                "\"title\": \"Realtime hub\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_735",
        "instruction": "Ensure the repository 'mobile-app' is kept up to date where the 'delta' branch includes a commit 'delta sync', and there is a pull request titled 'Delta sync' from 'delta' to 'main' which is open with the label 'ops'; enumerate the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "mobile-app"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "mobile-app",
                    "branch": "delta"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "mobile-app",
                    "branch": "delta",
                    "message": "delta sync"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "mobile-app",
                    "head_branch": "delta",
                    "base_branch": "main",
                    "title": "Delta sync"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "mobile-app",
                    "number": 1,
                    "label": "ops"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "mobile-app",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ops\"",
                "\"title\": \"Delta sync\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_736",
        "instruction": "Handle the 'web-auth' repository by ensuring the 'pdf' branch contains the commit 'pdf export', and verify that a pull request with the title 'PDF export' from 'pdf' to 'main' is open with the label 'security'; enumerate the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "web-auth"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "web-auth",
                    "branch": "pdf"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "web-auth",
                    "branch": "pdf",
                    "message": "pdf export"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "web-auth",
                    "head_branch": "pdf",
                    "base_branch": "main",
                    "title": "PDF export"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "web-auth",
                    "number": 1,
                    "label": "security"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "web-auth",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"security\"",
                "\"title\": \"PDF export\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_737",
        "instruction": "Manage the 'observability' repository where the 'thumb' branch includes a commit 'image thumbs', and check that a pull request titled 'Thumbnailer' from 'thumb' to 'main' is open with the label 'infra'; list the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "observability"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "observability",
                    "branch": "thumb"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "observability",
                    "branch": "thumb",
                    "message": "image thumbs"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "observability",
                    "head_branch": "thumb",
                    "base_branch": "main",
                    "title": "Thumbnailer"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "observability",
                    "number": 1,
                    "label": "infra"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "observability",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"infra\"",
                "\"title\": \"Thumbnailer\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_738",
        "instruction": "Handle the repository 'map-service' in which branch 'schedule' has a commit 'schedule lib', and ensure the pull request named 'Scheduler core' from 'schedule' to 'main' is open with the label 'seo'; enumerate open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "map-service"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "map-service",
                    "branch": "schedule"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "map-service",
                    "branch": "schedule",
                    "message": "schedule lib"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "map-service",
                    "head_branch": "schedule",
                    "base_branch": "main",
                    "title": "Scheduler core"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "map-service",
                    "number": 1,
                    "label": "seo"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "map-service",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"seo\"",
                "\"title\": \"Scheduler core\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_739",
        "instruction": "Coordinate the repository 'api-gateway' where branch 'bus' contains a commit 'bus impl', and verify that a pull request titled 'Event bus v2' from 'bus' to 'main' is open with the label 'ui'; list the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "api-gateway"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "api-gateway",
                    "branch": "bus"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "api-gateway",
                    "branch": "bus",
                    "message": "bus impl"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "api-gateway",
                    "head_branch": "bus",
                    "base_branch": "main",
                    "title": "Event bus v2"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "api-gateway",
                    "number": 1,
                    "label": "ui"
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "api-gateway",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ui\"",
                "\"title\": \"Event bus v2\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_740",
        "instruction": "Verify the existence of the 'data-lake' repository (and create it if it's not present). Make sure there is an open issue titled 'Reply delay' with the text 'Replies are slow in peak hours.', tagged with 'ops', and assigned to 'chris'. Once confirmed, provide only the 'label', 'assignees', and 'title' fields for that issue (avoid returning complete issue objects).",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "data-lake"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "data-lake",
                    "title": "Reply delay",
                    "body": "Replies are slow in peak hours."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "data-lake",
                    "number": 1,
                    "label": "ops"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "data-lake",
                    "number": 1,
                    "username": "chris"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "data-lake"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ops\"",
                "\"assignees\": [\"chris\"]",
                "\"title\": \"Reply delay\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_741",
        "instruction": "Verify the presence of the 'chat-bot' repository (and create it if it's absent). Make certain there is an open issue titled 'Rate limit' with the content 'Too strict rate limiting.', tagged as 'api', and assigned to 'chris'. Upon confirmation, supply only the 'label', 'assignees', and 'title' fields for that issue (do not return the entire issue objects).",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "chat-bot"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "chat-bot",
                    "title": "Rate limit",
                    "body": "Too strict rate limiting."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "chat-bot",
                    "number": 1,
                    "label": "api"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "chat-bot",
                    "number": 1,
                    "username": "chris"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "chat-bot"
                }
            }
        ],
        "outputs": [
                "\"label\": \"api\"",
                "\"assignees\": [\"chris\"]",
                "\"title\": \"Rate limit\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_742",
        "instruction": "Verify repository 'cron-runner' is present (establish it if absent). Confirm there is an ongoing issue titled 'Bad rounding' with content 'Rounding error in totals.', tagged 'priority', and allocated to 'elena'. Upon verification, return solely the 'label', 'assignees', and 'title' fields for that issue (do not include full issue objects).",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "cron-runner"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "cron-runner",
                    "title": "Bad rounding",
                    "body": "Rounding error in totals."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "cron-runner",
                    "number": 1,
                    "label": "priority"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "cron-runner",
                    "number": 1,
                    "username": "elena"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "cron-runner"
                }
            }
        ],
        "outputs": [
                "\"label\": \"priority\"",
                "\"assignees\": [\"elena\"]",
                "\"title\": \"Bad rounding\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_743",
        "instruction": "Verify repository 'oncall-bot' is present (create it if it isn't). Confirm there is a current issue titled 'Null handling' with content 'Handle None safely.', tagged 'bug', and allocated to 'jake'. After verification, return solely the 'label', 'assignees', and 'title' fields for that issue (do not include full issue objects).",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "oncall-bot"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "oncall-bot",
                    "title": "Null handling",
                    "body": "Handle None safely."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "oncall-bot",
                    "number": 1,
                    "label": "bug"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "oncall-bot",
                    "number": 1,
                    "username": "jake"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "oncall-bot"
                }
            }
        ],
        "outputs": [
                "\"label\": \"bug\"",
                "\"assignees\": [\"jake\"]",
                "\"title\": \"Null handling\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_744",
        "instruction": "Handle the existence of the 'linter' repository, creating it if it does not yet exist. Verify there is an issue open with the title 'S3 lifecycle', containing the body 'Configure S3 lifecycle policies.', tagged as 'infra', and assigned to 'olivia'. Once this is confirmed, provide only the 'label', 'assignees', and 'title' attributes for that specific issue (full issue objects should not be returned).",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "linter"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "linter",
                    "title": "S3 lifecycle",
                    "body": "Configure S3 lifecycle policies."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "linter",
                    "number": 1,
                    "label": "infra"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "linter",
                    "number": 1,
                    "username": "olivia"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "linter"
                }
            }
        ],
        "outputs": [
                "\"label\": \"infra\"",
                "\"assignees\": [\"olivia\"]",
                "\"title\": \"S3 lifecycle\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_745",
        "instruction": "Verify the repository 'ai-sdk' exists, creating it as necessary. Confirm there is an open issue titled 'Token expiry bug', with the body 'Expired tokens still validate.', labeled as 'security', and assigned to 'arjun'. Afterward, return just the 'label', 'assignees', and 'title' details for that issue (avoid returning complete issue objects).",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "ai-sdk"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "ai-sdk",
                    "title": "Token expiry bug",
                    "body": "Expired tokens still validate."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "ai-sdk",
                    "number": 1,
                    "label": "security"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "ai-sdk",
                    "number": 1,
                    "username": "arjun"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "ai-sdk"
                }
            }
        ],
        "outputs": [
                "\"label\": \"security\"",
                "\"assignees\": [\"arjun\"]",
                "\"title\": \"Token expiry bug\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_746",
        "instruction": "Verify the presence of the repository 'design-system' and create it if it does not exist. Confirm that there is an open issue with the title 'Eviction policy', containing the body 'Decide LFU vs LRU.', marked with the label 'planning', and assigned to 'nora'. Once verified, provide only the 'label', 'assignees', and 'title' fields for that specific issue (avoid returning complete issue objects).",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "design-system"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "design-system",
                    "title": "Eviction policy",
                    "body": "Decide LFU vs LRU."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "design-system",
                    "number": 1,
                    "label": "planning"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "design-system",
                    "number": 1,
                    "username": "nora"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "design-system"
                }
            }
        ],
        "outputs": [
                "\"label\": \"planning\"",
                "\"assignees\": [\"nora\"]",
                "\"title\": \"Eviction policy\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_747",
        "instruction": "Verify that the repository 'etl-runner' is present or create it if absent. Confirm there is an open issue with the title 'Add cron parser' and body 'Add a Cron expression parser.', labeled 'feature', and assigned to 'zayn'. Once confirmed, supply only the 'label', 'assignees', and 'title' fields for that issue (avoid providing full issue objects).",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "etl-runner"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "etl-runner",
                    "title": "Add cron parser",
                    "body": "Add a Cron expression parser."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "etl-runner",
                    "number": 1,
                    "label": "feature"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "etl-runner",
                    "number": 1,
                    "username": "zayn"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "etl-runner"
                }
            }
        ],
        "outputs": [
                "\"label\": \"feature\"",
                "\"assignees\": [\"zayn\"]",
                "\"title\": \"Add cron parser\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_748",
        "instruction": "Handle the management of the repository 'geo-index' by creating an issue with the title 'Healthcheck fails', including the body 'Probe endpoint fails on cold start.', labeled as 'bug' and assigned to 'amin'; proceed to list issues.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "geo-index"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "geo-index",
                    "title": "Healthcheck fails",
                    "body": "Probe endpoint fails on cold start."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "geo-index",
                    "number": 1,
                    "label": "bug"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "geo-index",
                    "number": 1,
                    "username": "amin"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "geo-index"
                }
            }
        ],
        "outputs": [
                "\"label\": \"bug\"",
                "\"assignees\": [\"amin\"]",
                "\"title\": \"Healthcheck fails\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_749",
        "instruction": "Verify the existence of the repository 'queue-svc' (initiate its creation if it's absent). Confirm there is an open issue titled 'Add migration plan', with the body 'Outline migration steps.', labeled 'planning', and assigned to 'emma'. Once confirmed, return solely the 'label', 'assignees', and 'title' fields for that issue (omit returning complete issue objects).",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "queue-svc"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "queue-svc",
                    "title": "Add migration plan",
                    "body": "Outline migration steps."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "queue-svc",
                    "number": 1,
                    "label": "planning"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "queue-svc",
                    "number": 1,
                    "username": "emma"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "queue-svc"
                }
            }
        ],
        "outputs": [
                "\"label\": \"planning\"",
                "\"assignees\": [\"emma\"]",
                "\"title\": \"Add migration plan\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_750",
        "instruction": "Handle the repository 'rate-limiter' to confirm its existence (create it if absent). Confirm there is an open issue titled 'CSV export' with the body 'Export CSV with delimiter option.', labeled 'feature', and assigned to 'emma'. Once confirmed, provide only the 'label', 'assignees', and 'title' fields for that particular issue (avoid returning full issue objects).",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "rate-limiter"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "rate-limiter",
                    "title": "CSV export",
                    "body": "Export CSV with delimiter option."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "rate-limiter",
                    "number": 1,
                    "label": "feature"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "rate-limiter",
                    "number": 1,
                    "username": "emma"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "rate-limiter"
                }
            }
        ],
        "outputs": [
                "\"label\": \"feature\"",
                "\"assignees\": [\"emma\"]",
                "\"title\": \"CSV export\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_751",
        "instruction": "Coordinate the management of the repository 'uploader' by initiating an issue with the title 'Respect robots.txt', including the body 'Crawler must respect robots.txt.', labeled 'compliance', and assigned to 'amin'; display the list of issues.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "uploader"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "uploader",
                    "title": "Respect robots.txt",
                    "body": "Crawler must respect robots.txt."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "uploader",
                    "number": 1,
                    "label": "compliance"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "uploader",
                    "number": 1,
                    "username": "amin"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "uploader"
                }
            }
        ],
        "outputs": [
                "\"label\": \"compliance\"",
                "\"assignees\": [\"amin\"]",
                "\"title\": \"Respect robots.txt\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_752",
        "instruction": "Handle the management of repository 'image-proc' by creating an issue titled 'Rule for imports' with body 'Enforce import ordering.' labeled 'enhancement' and assigned to 'olivia'; proceed to list issues.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "image-proc"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "image-proc",
                    "title": "Rule for imports",
                    "body": "Enforce import ordering."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "image-proc",
                    "number": 1,
                    "label": "enhancement"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "image-proc",
                    "number": 1,
                    "username": "olivia"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "image-proc"
                }
            }
        ],
        "outputs": [
                "\"label\": \"enhancement\"",
                "\"assignees\": [\"olivia\"]",
                "\"title\": \"Rule for imports\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_753",
        "instruction": "Coordinate the management of repository 'webhooks' by initiating an issue titled 'Toggle not saved' with body 'Toggles revert after refresh.' labeled 'bug' and assigned to 'karim'; then list issues.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "webhooks"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "webhooks",
                    "title": "Toggle not saved",
                    "body": "Toggles revert after refresh."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "webhooks",
                    "number": 1,
                    "label": "bug"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "webhooks",
                    "number": 1,
                    "username": "karim"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "webhooks"
                }
            }
        ],
        "outputs": [
                "\"label\": \"bug\"",
                "\"assignees\": [\"karim\"]",
                "\"title\": \"Toggle not saved\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_754",
        "instruction": "Handle the repository 'form-builder' by creating an issue with the title 'Rate limit header' and the body 'Expose X-RateLimit headers.', labeled as 'api', and assign it to 'olivia'; then list issues.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "form-builder"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "form-builder",
                    "title": "Rate limit header",
                    "body": "Expose X-RateLimit headers."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "form-builder",
                    "number": 1,
                    "label": "api"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "form-builder",
                    "number": 1,
                    "username": "olivia"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "form-builder"
                }
            }
        ],
        "outputs": [
                "\"label\": \"api\"",
                "\"assignees\": [\"olivia\"]",
                "\"title\": \"Rate limit header\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_755",
        "instruction": "Coordinate the repository 'markdown-viewer' by setting up an issue titled 'Add dashboard' with the body 'Create Grafana dashboards.', labeled 'observability', and assign to 'emma'; subsequently list issues.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "markdown-viewer"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "markdown-viewer",
                    "title": "Add dashboard",
                    "body": "Create Grafana dashboards."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "markdown-viewer",
                    "number": 1,
                    "label": "observability"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "markdown-viewer",
                    "number": 1,
                    "username": "emma"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "markdown-viewer"
                }
            }
        ],
        "outputs": [
                "\"label\": \"observability\"",
                "\"assignees\": [\"emma\"]",
                "\"title\": \"Add dashboard\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_756",
        "instruction": "Handle the repository 'audit-log' by creating an issue titled 'Cold start' with the body 'Function cold starts are high.' labeled as 'ops' and assign it to 'elena'; list the issues.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "audit-log"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "audit-log",
                    "title": "Cold start",
                    "body": "Function cold starts are high."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "audit-log",
                    "number": 1,
                    "label": "ops"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "audit-log",
                    "number": 1,
                    "username": "elena"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "audit-log"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ops\"",
                "\"assignees\": [\"elena\"]",
                "\"title\": \"Cold start\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_757",
        "instruction": "Handle the repository 'session-store' by creating an issue titled 'Webhook retry' with the body 'Implement exponential backoff.' labeled as 'api' and assign it to 'jake'; list the issues.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "session-store"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "session-store",
                    "title": "Webhook retry",
                    "body": "Implement exponential backoff."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "session-store",
                    "number": 1,
                    "label": "api"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "session-store",
                    "number": 1,
                    "username": "jake"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "session-store"
                }
            }
        ],
        "outputs": [
                "\"label\": \"api\"",
                "\"assignees\": [\"jake\"]",
                "\"title\": \"Webhook retry\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_758",
        "instruction": "Handle repository 'graphql-gw' by creating an issue titled 'Dark mode toggle' with the body 'Add a dark theme switcher.' labeled 'ui' and assigned to 'nora'; list issues.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "graphql-gw"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "graphql-gw",
                    "title": "Dark mode toggle",
                    "body": "Add a dark theme switcher."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "graphql-gw",
                    "number": 1,
                    "label": "ui"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "graphql-gw",
                    "number": 1,
                    "username": "nora"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "graphql-gw"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ui\"",
                "\"assignees\": [\"nora\"]",
                "\"title\": \"Dark mode toggle\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_759",
        "instruction": "Coordinate repository 'oauth-proxy' by creating an issue titled 'Timezone bug' with the body 'Datetime parsing incorrect.' labeled 'bug' and assigned to 'chris'; list issues.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "oauth-proxy"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "repo": "oauth-proxy",
                    "title": "Timezone bug",
                    "body": "Datetime parsing incorrect."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "repo": "oauth-proxy",
                    "number": 1,
                    "label": "bug"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "repo": "oauth-proxy",
                    "number": 1,
                    "username": "chris"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "repo": "oauth-proxy"
                }
            }
        ],
        "outputs": [
                "\"label\": \"bug\"",
                "\"assignees\": [\"chris\"]",
                "\"title\": \"Timezone bug\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_760",
        "instruction": "Handle the transfer of repository 'profile-svc' to 'core-team' as the new owner; create an issue titled 'Deprecate old API' with the body 'Plan removal of v1 API.' labeled 'deprecate' and assigned to 'nora'; subsequently, enumerate issues for owner 'core-team'.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "profile-svc"
                },
            },
            {
                "name": "TransferRepo",
                "arguments": {
                    "repo": "profile-svc",
                    "new_owner": "core-team"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "owner": "core-team",
                    "repo": "profile-svc",
                    "title": "Deprecate old API",
                    "body": "Plan removal of v1 API."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "owner": "core-team",
                    "repo": "profile-svc",
                    "number": 1,
                    "label": "deprecate"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "owner": "core-team",
                    "repo": "profile-svc",
                    "number": 1,
                    "username": "nora"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "owner": "core-team",
                    "repo": "profile-svc"
                }
            }
        ],
        "outputs": [
                "\"owner\": \"core-team\"",
                "\"title\": \"Deprecate old API\"",
                "\"label\": \"deprecate\"",
                "\"assignees\": [\"nora\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_761",
        "instruction": "Ensure the repository 'comments-api' is transferred to 'edge-team' as its new owner; under this new ownership, open an issue titled 'Purge endpoint' with the body 'Add purge endpoint for CDN.' labeled 'ops' and assign it to 'amin'; afterwards, list issues for owner 'edge-team'.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "comments-api"
                },
            },
            {
                "name": "TransferRepo",
                "arguments": {
                    "repo": "comments-api",
                    "new_owner": "edge-team"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "owner": "edge-team",
                    "repo": "comments-api",
                    "title": "Purge endpoint",
                    "body": "Add purge endpoint for CDN."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "owner": "edge-team",
                    "repo": "comments-api",
                    "number": 1,
                    "label": "ops"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "owner": "edge-team",
                    "repo": "comments-api",
                    "number": 1,
                    "username": "amin"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "owner": "edge-team",
                    "repo": "comments-api"
                }
            }
        ],
        "outputs": [
                "\"owner\": \"edge-team\"",
                "\"title\": \"Purge endpoint\"",
                "\"label\": \"ops\"",
                "\"assignees\": [\"amin\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_762",
        "instruction": "Handle the transfer of repository 'notifications' to 'security-group' as the new owner; once transferred, initiate an issue titled 'Rotate keys' with the content 'Rotate signing keys regularly.' with the label 'security', assigning it to 'arjun'; subsequently, enumerate issues for 'security-group'.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "notifications"
                },
            },
            {
                "name": "TransferRepo",
                "arguments": {
                    "repo": "notifications",
                    "new_owner": "security-group"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "owner": "security-group",
                    "repo": "notifications",
                    "title": "Rotate keys",
                    "body": "Rotate signing keys regularly."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "owner": "security-group",
                    "repo": "notifications",
                    "number": 1,
                    "label": "security"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "owner": "security-group",
                    "repo": "notifications",
                    "number": 1,
                    "username": "arjun"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "owner": "security-group",
                    "repo": "notifications"
                }
            }
        ],
        "outputs": [
                "\"owner\": \"security-group\"",
                "\"title\": \"Rotate keys\"",
                "\"label\": \"security\"",
                "\"assignees\": [\"arjun\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_763",
        "instruction": "Oversee the transfer of the repository 'realtime-hub' to 'data-team' for new ownership; under the new owner, create an issue titled 'Partition table' with the description 'Partition table by month.' marked with the label 'infra' and assigned to 'emma'; finally, compile a list of issues for 'data-team'.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "realtime-hub"
                },
            },
            {
                "name": "TransferRepo",
                "arguments": {
                    "repo": "realtime-hub",
                    "new_owner": "data-team"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "owner": "data-team",
                    "repo": "realtime-hub",
                    "title": "Partition table",
                    "body": "Partition table by month."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "owner": "data-team",
                    "repo": "realtime-hub",
                    "number": 1,
                    "label": "infra"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "owner": "data-team",
                    "repo": "realtime-hub",
                    "number": 1,
                    "username": "emma"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "owner": "data-team",
                    "repo": "realtime-hub"
                }
            }
        ],
        "outputs": [
                "\"owner\": \"data-team\"",
                "\"title\": \"Partition table\"",
                "\"label\": \"infra\"",
                "\"assignees\": [\"emma\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_764",
        "instruction": "Handle the transfer of the 'delta-sync' repository to the 'platform' owner; once ownership is established, initiate an issue titled 'Feature flags' with the body 'Rollout gradual flags.' and label it 'feature', assigning it to 'karim'. Finally, compile a list of issues related to the 'platform' owner.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "delta-sync"
                },
            },
            {
                "name": "TransferRepo",
                "arguments": {
                    "repo": "delta-sync",
                    "new_owner": "platform"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "owner": "platform",
                    "repo": "delta-sync",
                    "title": "Feature flags",
                    "body": "Rollout gradual flags."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "owner": "platform",
                    "repo": "delta-sync",
                    "number": 1,
                    "label": "feature"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "owner": "platform",
                    "repo": "delta-sync",
                    "number": 1,
                    "username": "karim"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "owner": "platform",
                    "repo": "delta-sync"
                }
            }
        ],
        "outputs": [
                "\"owner\": \"platform\"",
                "\"title\": \"Feature flags\"",
                "\"label\": \"feature\"",
                "\"assignees\": [\"karim\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_765",
        "instruction": "Coordinate the transfer of the 'pdf-tool' repository to the 'growth' owner. Under the new ownership, create an issue titled 'ETL ownership' with the content 'Move ETL jobs here.', label it 'analytics', and assign it to 'emma'. Subsequently, assemble a list of issues associated with the 'growth' owner.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "pdf-tool"
                },
            },
            {
                "name": "TransferRepo",
                "arguments": {
                    "repo": "pdf-tool",
                    "new_owner": "growth"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "owner": "growth",
                    "repo": "pdf-tool",
                    "title": "ETL ownership",
                    "body": "Move ETL jobs here."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "owner": "growth",
                    "repo": "pdf-tool",
                    "number": 1,
                    "label": "analytics"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "owner": "growth",
                    "repo": "pdf-tool",
                    "number": 1,
                    "username": "emma"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "owner": "growth",
                    "repo": "pdf-tool"
                }
            }
        ],
        "outputs": [
                "\"owner\": \"growth\"",
                "\"title\": \"ETL ownership\"",
                "\"label\": \"analytics\"",
                "\"assignees\": [\"emma\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_766",
        "instruction": "Make certain the 'thumbnailer' repository is transferred to be under the 'sre-team'; within the new ownership, initiate an issue titled 'Alert routing' with the description 'Route alerts to PagerDuty.' marked with label 'ops' and assign it to 'zayn'; subsequently, compile a list of issues for the 'sre-team' owner.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "thumbnailer"
                },
            },
            {
                "name": "TransferRepo",
                "arguments": {
                    "repo": "thumbnailer",
                    "new_owner": "sre-team"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "owner": "sre-team",
                    "repo": "thumbnailer",
                    "title": "Alert routing",
                    "body": "Route alerts to PagerDuty."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "owner": "sre-team",
                    "repo": "thumbnailer",
                    "number": 1,
                    "label": "ops"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "owner": "sre-team",
                    "repo": "thumbnailer",
                    "number": 1,
                    "username": "zayn"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "owner": "sre-team",
                    "repo": "thumbnailer"
                }
            }
        ],
        "outputs": [
                "\"owner\": \"sre-team\"",
                "\"title\": \"Alert routing\"",
                "\"label\": \"ops\"",
                "\"assignees\": [\"zayn\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_767",
        "instruction": "Verify that the repository 'scheduler-pro' is reassigned to the 'ml-team'; once transferred, create an issue titled 'Model registry' containing the text 'Registry for ML models.' with the label 'ml' assigned to 'nora'; afterward, catalog the issues for the 'ml-team' owner.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "scheduler-pro"
                },
            },
            {
                "name": "TransferRepo",
                "arguments": {
                    "repo": "scheduler-pro",
                    "new_owner": "ml-team"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "owner": "ml-team",
                    "repo": "scheduler-pro",
                    "title": "Model registry",
                    "body": "Registry for ML models."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "owner": "ml-team",
                    "repo": "scheduler-pro",
                    "number": 1,
                    "label": "ml"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "owner": "ml-team",
                    "repo": "scheduler-pro",
                    "number": 1,
                    "username": "nora"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "owner": "ml-team",
                    "repo": "scheduler-pro"
                }
            }
        ],
        "outputs": [
                "\"owner\": \"ml-team\"",
                "\"title\": \"Model registry\"",
                "\"label\": \"ml\"",
                "\"assignees\": [\"nora\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_768",
        "instruction": "Handle the transfer of the 'event-bus' repository to the ownership of 'infra-team'; once transferred, create an issue under the new owner called 'VPC peering' with the description 'Establish VPC peering.' carrying the label 'infra' and assign it to 'olivia'; subsequently, enumerate issues for the owner 'infra-team'.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "event-bus"
                },
            },
            {
                "name": "TransferRepo",
                "arguments": {
                    "repo": "event-bus",
                    "new_owner": "infra-team"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "owner": "infra-team",
                    "repo": "event-bus",
                    "title": "VPC peering",
                    "body": "Establish VPC peering."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "owner": "infra-team",
                    "repo": "event-bus",
                    "number": 1,
                    "label": "infra"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "owner": "infra-team",
                    "repo": "event-bus",
                    "number": 1,
                    "username": "olivia"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "owner": "infra-team",
                    "repo": "event-bus"
                }
            }
        ],
        "outputs": [
                "\"owner\": \"infra-team\"",
                "\"title\": \"VPC peering\"",
                "\"label\": \"infra\"",
                "\"assignees\": [\"olivia\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_769",
        "instruction": "Coordinate the transfer of the 'payment-ui' repository to 'design-team'; after this, under the new owner, initiate an issue titled 'Icon refresh' with the content 'Refresh icon set.' bearing the label 'ui' and assign it to 'elena'; following that, list issues for 'design-team'.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "payment-ui"
                },
            },
            {
                "name": "TransferRepo",
                "arguments": {
                    "repo": "payment-ui",
                    "new_owner": "design-team"
                },
            },
            {
                "name": "OpenIssue",
                "arguments": {
                    "owner": "design-team",
                    "repo": "payment-ui",
                    "title": "Icon refresh",
                    "body": "Refresh icon set."
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "issue",
                    "owner": "design-team",
                    "repo": "payment-ui",
                    "number": 1,
                    "label": "ui"
                },
            },
            {
                "name": "AssignUser",
                "arguments": {
                    "kind": "issue",
                    "owner": "design-team",
                    "repo": "payment-ui",
                    "number": 1,
                    "username": "elena"
                },
            },
            {
                "name": "ListIssues",
                "arguments": {
                    "owner": "design-team",
                    "repo": "payment-ui"
                }
            }
        ],
        "outputs": [
                "\"owner\": \"design-team\"",
                "\"title\": \"Icon refresh\"",
                "\"label\": \"ui\"",
                "\"assignees\": [\"elena\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_770",
        "instruction": "Handle the repository 'coupon-svc' ensuring branch 'feat-1' contains a commit 'feature 1', and ensure a pull request titled 'Feature 1' from 'feat-1' to 'main' is open with the label 'ops', after undergoing closure and reopening; enumerate open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "coupon-svc"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "coupon-svc",
                    "branch": "feat-1"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "coupon-svc",
                    "branch": "feat-1",
                    "message": "feature 1"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "coupon-svc",
                    "head_branch": "feat-1",
                    "base_branch": "main",
                    "title": "Feature 1"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "coupon-svc",
                    "number": 1,
                    "label": "ops"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "coupon-svc",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "coupon-svc",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "coupon-svc",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ops\"",
                "\"title\": \"Feature 1\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_771",
        "instruction": "Coordinate the repository 'shipping-svc' ensuring branch 'feat-2' contains a commit 'feature 2', and ensure a pull request titled 'Feature 2' from 'feat-2' to 'main' is open with the label 'security', after undergoing closure and reopening; enumerate open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "shipping-svc"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "shipping-svc",
                    "branch": "feat-2"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "shipping-svc",
                    "branch": "feat-2",
                    "message": "feature 2"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "shipping-svc",
                    "head_branch": "feat-2",
                    "base_branch": "main",
                    "title": "Feature 2"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "shipping-svc",
                    "number": 1,
                    "label": "security"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "shipping-svc",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "shipping-svc",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "shipping-svc",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"security\"",
                "\"title\": \"Feature 2\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_772",
        "instruction": "Handle the repository 'catalog-api' where the branch 'feat-3' includes a commit labeled 'feature 3', and there's an active pull request titled 'Feature 3' from 'feat-3' to 'main' with the label 'infra', following its closure and reopening; enumerate the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "catalog-api"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "catalog-api",
                    "branch": "feat-3"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "catalog-api",
                    "branch": "feat-3",
                    "message": "feature 3"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "catalog-api",
                    "head_branch": "feat-3",
                    "base_branch": "main",
                    "title": "Feature 3"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "catalog-api",
                    "number": 1,
                    "label": "infra"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "catalog-api",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "catalog-api",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "catalog-api",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"infra\"",
                "\"title\": \"Feature 3\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_773",
        "instruction": "Handle the repository 'inventory-svc' where the branch 'feat-4' includes a commit labeled 'feature 4', and there's an active pull request titled 'Feature 4' from 'feat-4' to 'main' with the label 'seo', following its closure and reopening; enumerate the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "inventory-svc"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "inventory-svc",
                    "branch": "feat-4"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "inventory-svc",
                    "branch": "feat-4",
                    "message": "feature 4"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "inventory-svc",
                    "head_branch": "feat-4",
                    "base_branch": "main",
                    "title": "Feature 4"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "inventory-svc",
                    "number": 1,
                    "label": "seo"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "inventory-svc",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "inventory-svc",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "inventory-svc",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"seo\"",
                "\"title\": \"Feature 4\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_774",
        "instruction": "Ensure the repository 'recommendation' is up to date, with branch 'feat-5' containing the commit 'feature 5'. There is a pull request titled 'Feature 5' from 'feat-5' to 'main' that must be reopened after closing and should have the 'ui' label; list the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "recommendation"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "recommendation",
                    "branch": "feat-5"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "recommendation",
                    "branch": "feat-5",
                    "message": "feature 5"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "recommendation",
                    "head_branch": "feat-5",
                    "base_branch": "main",
                    "title": "Feature 5"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "recommendation",
                    "number": 1,
                    "label": "ui"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "recommendation",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "recommendation",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "recommendation",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ui\"",
                "\"title\": \"Feature 5\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_775",
        "instruction": "Handle the repository 'ab-testing' so that branch 'feat-6' includes the commit 'feature 6'. A pull request titled 'Feature 6' from 'feat-6' to 'main' needs to be reopened after being closed and must be tagged with 'docs'; display the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "ab-testing"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "ab-testing",
                    "branch": "feat-6"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "ab-testing",
                    "branch": "feat-6",
                    "message": "feature 6"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "ab-testing",
                    "head_branch": "feat-6",
                    "base_branch": "main",
                    "title": "Feature 6"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "ab-testing",
                    "number": 1,
                    "label": "docs"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "ab-testing",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "ab-testing",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "ab-testing",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"docs\"",
                "\"title\": \"Feature 6\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_776",
        "instruction": "Handle the repository 'experiments' ensuring branch 'feat-7' includes a commit 'feature 7', and manage a pull request titled 'Feature 7' moving from 'feat-7' to 'main' that remains open with label 'feature', post closure and reopening; display open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "experiments"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "experiments",
                    "branch": "feat-7"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "experiments",
                    "branch": "feat-7",
                    "message": "feature 7"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "experiments",
                    "head_branch": "feat-7",
                    "base_branch": "main",
                    "title": "Feature 7"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "experiments",
                    "number": 1,
                    "label": "feature"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "experiments",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "experiments",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "experiments",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"feature\"",
                "\"title\": \"Feature 7\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_777",
        "instruction": "Coordinate the repository 'feature-gates' ensuring branch 'feat-8' includes a commit 'feature 8', and manage a pull request titled 'Feature 8' moving from 'feat-8' to 'main' that remains open with label 'api', post closure and reopening; display open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "feature-gates"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "feature-gates",
                    "branch": "feat-8"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "feature-gates",
                    "branch": "feat-8",
                    "message": "feature 8"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "feature-gates",
                    "head_branch": "feat-8",
                    "base_branch": "main",
                    "title": "Feature 8"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "feature-gates",
                    "number": 1,
                    "label": "api"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "feature-gates",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "feature-gates",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "feature-gates",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"api\"",
                "\"title\": \"Feature 8\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_778",
        "instruction": "Ensure that the repository 'content-api' is maintained, with branch 'feat-9' containing a commit 'feature 9'. There should be an open pull request titled 'Feature 9' from 'feat-9' to 'main', labeled 'ops', which has been closed and reopened; provide a list of open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "content-api"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "content-api",
                    "branch": "feat-9"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "content-api",
                    "branch": "feat-9",
                    "message": "feature 9"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "content-api",
                    "head_branch": "feat-9",
                    "base_branch": "main",
                    "title": "Feature 9"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "content-api",
                    "number": 1,
                    "label": "ops"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "content-api",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "content-api",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "content-api",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ops\"",
                "\"title\": \"Feature 9\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_779",
        "instruction": "Ensure the repository 'feed-svc' is maintained, where branch 'feat-10' has a commit 'feature 10'. An open pull request titled 'Feature 10' from 'feat-10' to 'main' should exist, labeled 'security', after being closed and reopened; provide a list of open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "feed-svc"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "feed-svc",
                    "branch": "feat-10"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "feed-svc",
                    "branch": "feat-10",
                    "message": "feature 10"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "feed-svc",
                    "head_branch": "feat-10",
                    "base_branch": "main",
                    "title": "Feature 10"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "feed-svc",
                    "number": 1,
                    "label": "security"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "feed-svc",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "feed-svc",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "feed-svc",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"security\"",
                "\"title\": \"Feature 10\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_780",
        "instruction": "Handle repository 'media-cdn', ensuring that the branch 'feat-11' includes a commit 'feature 11'. Make sure a pull request titled 'Feature 11' from 'feat-11' to 'main' is open, tagged with the label 'infra', after previously being closed and then reopened; list all open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "media-cdn"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "media-cdn",
                    "branch": "feat-11"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "media-cdn",
                    "branch": "feat-11",
                    "message": "feature 11"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "media-cdn",
                    "head_branch": "feat-11",
                    "base_branch": "main",
                    "title": "Feature 11"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "media-cdn",
                    "number": 1,
                    "label": "infra"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "media-cdn",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "media-cdn",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "media-cdn",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"infra\"",
                "\"title\": \"Feature 11\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_781",
        "instruction": "Manage repository 'avatar-gen', confirming the branch 'feat-12' contains a commit 'feature 12'. Ensure that a pull request named 'Feature 12' from 'feat-12' to 'main' is open and marked with the label 'seo', following its closure and reopening; list all open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "avatar-gen"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "avatar-gen",
                    "branch": "feat-12"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "avatar-gen",
                    "branch": "feat-12",
                    "message": "feature 12"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "avatar-gen",
                    "head_branch": "feat-12",
                    "base_branch": "main",
                    "title": "Feature 12"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "avatar-gen",
                    "number": 1,
                    "label": "seo"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "avatar-gen",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "avatar-gen",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "avatar-gen",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"seo\"",
                "\"title\": \"Feature 12\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_782",
        "instruction": "Ensure the upkeep of the repository 'geo-routing', in which branch 'feat-13' includes a commit 'feature 13'. There is also a pull request titled 'Feature 13', moving from 'feat-13' to 'main', which is labeled 'ui' and reopened after closure; detail the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "geo-routing"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "geo-routing",
                    "branch": "feat-13"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "geo-routing",
                    "branch": "feat-13",
                    "message": "feature 13"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "geo-routing",
                    "head_branch": "feat-13",
                    "base_branch": "main",
                    "title": "Feature 13"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "geo-routing",
                    "number": 1,
                    "label": "ui"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "geo-routing",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "geo-routing",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "geo-routing",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ui\"",
                "\"title\": \"Feature 13\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_783",
        "instruction": "Manage the repository 'fraud-detect', focusing on branch 'feat-14' with its commit 'feature 14'. A pull request named 'Feature 14' is in process from 'feat-14' to 'main', carrying the 'docs' label and has been reopened after closing; enumerate the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "fraud-detect"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "fraud-detect",
                    "branch": "feat-14"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "fraud-detect",
                    "branch": "feat-14",
                    "message": "feature 14"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "fraud-detect",
                    "head_branch": "feat-14",
                    "base_branch": "main",
                    "title": "Feature 14"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "fraud-detect",
                    "number": 1,
                    "label": "docs"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "fraud-detect",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "fraud-detect",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "fraud-detect",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"docs\"",
                "\"title\": \"Feature 14\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_784",
        "instruction": "Handle the maintenance of repository 'vector-search' where the branch 'feat-15' includes a commit 'feature 15', and ensure a pull request titled 'Feature 15' from 'feat-15' to 'main' remains open with the label 'feature', after having been closed and reopened; enumerate the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "vector-search"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "vector-search",
                    "branch": "feat-15"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "vector-search",
                    "branch": "feat-15",
                    "message": "feature 15"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "vector-search",
                    "head_branch": "feat-15",
                    "base_branch": "main",
                    "title": "Feature 15"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "vector-search",
                    "number": 1,
                    "label": "feature"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "vector-search",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "vector-search",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "vector-search",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"feature\"",
                "\"title\": \"Feature 15\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_785",
        "instruction": "Handle the maintenance of repository 'sso-portal' where the branch 'feat-16' contains a commit 'feature 16', and ensure a pull request titled 'Feature 16' from 'feat-16' to 'main' stays open with the label 'api', after being closed and reopened; enumerate the open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "sso-portal"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "sso-portal",
                    "branch": "feat-16"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "sso-portal",
                    "branch": "feat-16",
                    "message": "feature 16"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "sso-portal",
                    "head_branch": "feat-16",
                    "base_branch": "main",
                    "title": "Feature 16"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "sso-portal",
                    "number": 1,
                    "label": "api"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "sso-portal",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "sso-portal",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "sso-portal",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"api\"",
                "\"title\": \"Feature 16\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_786",
        "instruction": "Ensure the repository 'tenant-admin' is managed where branch 'feat-17' includes a commit 'feature 17', and a pull request called 'Feature 17' from 'feat-17' to 'main' remains open with label 'ops', especially after it was closed and reopened; enumerate open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "tenant-admin"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "tenant-admin",
                    "branch": "feat-17"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "tenant-admin",
                    "branch": "feat-17",
                    "message": "feature 17"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "tenant-admin",
                    "head_branch": "feat-17",
                    "base_branch": "main",
                    "title": "Feature 17"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "tenant-admin",
                    "number": 1,
                    "label": "ops"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "tenant-admin",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "tenant-admin",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "tenant-admin",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"ops\"",
                "\"title\": \"Feature 17\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_787",
        "instruction": "Ensure the repository 'workspace-api' is managed where branch 'feat-18' includes a commit 'feature 18', and a pull request titled 'Feature 18' from 'feat-18' to 'main' stays open with label 'security', especially after being shut and reinitiated; enumerate open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "workspace-api"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "workspace-api",
                    "branch": "feat-18"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "workspace-api",
                    "branch": "feat-18",
                    "message": "feature 18"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "workspace-api",
                    "head_branch": "feat-18",
                    "base_branch": "main",
                    "title": "Feature 18"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "workspace-api",
                    "number": 1,
                    "label": "security"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "workspace-api",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "workspace-api",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "workspace-api",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"security\"",
                "\"title\": \"Feature 18\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_788",
        "instruction": "Ensure the repository 'notes-app' is maintained. Branch 'feat-19' contains a commit 'feature 19', and there is a pull request labeled 'infra' titled 'Feature 19' from 'feat-19' to 'main' that has been closed and reopened; display any open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "notes-app"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "notes-app",
                    "branch": "feat-19"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "notes-app",
                    "branch": "feat-19",
                    "message": "feature 19"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "notes-app",
                    "head_branch": "feat-19",
                    "base_branch": "main",
                    "title": "Feature 19"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "notes-app",
                    "number": 1,
                    "label": "infra"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "notes-app",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "notes-app",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "notes-app",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"infra\"",
                "\"title\": \"Feature 19\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_789",
        "instruction": "Ensure the repository 'doc-editor' is maintained. Branch 'feat-20' includes a commit 'feature 20', and there is a pull request labeled 'seo' titled 'Feature 20' from 'feat-20' to 'main' that has been closed and reopened; display any open PRs.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "doc-editor"
                },
            },
            {
                "name": "CreateBranch",
                "arguments": {
                    "repo": "doc-editor",
                    "branch": "feat-20"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "doc-editor",
                    "branch": "feat-20",
                    "message": "feature 20"
                },
            },
            {
                "name": "OpenPr",
                "arguments": {
                    "repo": "doc-editor",
                    "head_branch": "feat-20",
                    "base_branch": "main",
                    "title": "Feature 20"
                },
            },
            {
                "name": "AddLabel",
                "arguments": {
                    "kind": "pr",
                    "repo": "doc-editor",
                    "number": 1,
                    "label": "seo"
                },
            },
            {
                "name": "ClosePr",
                "arguments": {
                    "repo": "doc-editor",
                    "number": 1
                },
            },
            {
                "name": "ReopenPr",
                "arguments": {
                    "repo": "doc-editor",
                    "number": 1
                },
            },
            {
                "name": "ListPrs",
                "arguments": {
                    "repo": "doc-editor",
                    "state": "open"
                }
            }
        ],
        "outputs": [
                "\"label\": \"seo\"",
                "\"title\": \"Feature 20\"",
                "\"state\": \"open\""
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_790",
        "instruction": "Establish a repository 'renderer' tagged with topics ['ui', 'components'], make the commits 'init topics' and 'readme', and verify branches to confirm 'main' exists.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "renderer"
                },
            },
            {
                "name": "RepoTopics",
                "arguments": {
                    "repo": "renderer",
                    "topics": [
                        "ui",
                        "components"
                    ]
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "renderer",
                    "message": "init topics"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "renderer",
                    "message": "readme"
                },
            },
            {
                "name": "ListBranches",
                "arguments": {
                    "repo": "renderer"
                }
            }
        ],
        "outputs": [
                "\"topics\": [\"ui\", \"components\"]",
                "\"branches\": [\"main\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_791",
        "instruction": "Set up a repository 'state-store' with the specified topics ['cli', 'tools'], execute the commits 'init topics' and 'readme', and check branches to ensure 'main' is present.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "state-store"
                },
            },
            {
                "name": "RepoTopics",
                "arguments": {
                    "repo": "state-store",
                    "topics": [
                        "cli",
                        "tools"
                    ]
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "state-store",
                    "message": "init topics"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "state-store",
                    "message": "readme"
                },
            },
            {
                "name": "ListBranches",
                "arguments": {
                    "repo": "state-store"
                }
            }
        ],
        "outputs": [
                "\"topics\": [\"cli\", \"tools\"]",
                "\"branches\": [\"main\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_792",
        "instruction": "Establish a repository named 'odata-gw' with the topics ['security', 'auth'], make the commit 'init topics' along with 'readme', and display branches to confirm 'main' is present.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "odata-gw"
                },
            },
            {
                "name": "RepoTopics",
                "arguments": {
                    "repo": "odata-gw",
                    "topics": [
                        "security",
                        "auth"
                    ]
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "odata-gw",
                    "message": "init topics"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "odata-gw",
                    "message": "readme"
                },
            },
            {
                "name": "ListBranches",
                "arguments": {
                    "repo": "odata-gw"
                }
            }
        ],
        "outputs": [
                "\"topics\": [\"security\", \"auth\"]",
                "\"branches\": [\"main\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_793",
        "instruction": "Set up a repository entitled 'image-filter' with the topics ['data', 'etl'], perform the commit 'init topics' as well as 'readme', and list branches to verify 'main' is present.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "image-filter"
                },
            },
            {
                "name": "RepoTopics",
                "arguments": {
                    "repo": "image-filter",
                    "topics": [
                        "data",
                        "etl"
                    ]
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "image-filter",
                    "message": "init topics"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "image-filter",
                    "message": "readme"
                },
            },
            {
                "name": "ListBranches",
                "arguments": {
                    "repo": "image-filter"
                }
            }
        ],
        "outputs": [
                "\"topics\": [\"data\", \"etl\"]",
                "\"branches\": [\"main\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_794",
        "instruction": "Handle the creation of a repository 'push-gw' with topics ['ops', 'cron'], incorporate commit 'init topics' and commit 'readme', and list branches to verify the presence of 'main'.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "push-gw"
                },
            },
            {
                "name": "RepoTopics",
                "arguments": {
                    "repo": "push-gw",
                    "topics": [
                        "ops",
                        "cron"
                    ]
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "push-gw",
                    "message": "init topics"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "push-gw",
                    "message": "readme"
                },
            },
            {
                "name": "ListBranches",
                "arguments": {
                    "repo": "push-gw"
                }
            }
        ],
        "outputs": [
                "\"topics\": [\"ops\", \"cron\"]",
                "\"branches\": [\"main\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_795",
        "instruction": "Coordinate the setup of a repository 'sync-agent' with topics ['api', 'gateway'], include commit 'init topics' and commit 'readme', and list branches to confirm 'main' is present.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "sync-agent"
                },
            },
            {
                "name": "RepoTopics",
                "arguments": {
                    "repo": "sync-agent",
                    "topics": [
                        "api",
                        "gateway"
                    ]
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "sync-agent",
                    "message": "init topics"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "sync-agent",
                    "message": "readme"
                },
            },
            {
                "name": "ListBranches",
                "arguments": {
                    "repo": "sync-agent"
                }
            }
        ],
        "outputs": [
                "\"topics\": [\"api\", \"gateway\"]",
                "\"branches\": [\"main\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_796",
        "instruction": "Handle the creation of a repository named 'idp-core' with topics ['ml', 'models'], add the commits 'init topics' and 'readme', then display the branches to confirm the existence of 'main'.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "idp-core"
                },
            },
            {
                "name": "RepoTopics",
                "arguments": {
                    "repo": "idp-core",
                    "topics": [
                        "ml",
                        "models"
                    ]
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "idp-core",
                    "message": "init topics"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "idp-core",
                    "message": "readme"
                },
            },
            {
                "name": "ListBranches",
                "arguments": {
                    "repo": "idp-core"
                }
            }
        ],
        "outputs": [
                "\"topics\": [\"ml\", \"models\"]",
                "\"branches\": [\"main\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_797",
        "instruction": "Coordinate the establishment of a repository called 'policy-svc' with topics ['search', 'index'], add the commits 'init topics' and 'readme', and then list the branches to verify that 'main' is present.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "policy-svc"
                },
            },
            {
                "name": "RepoTopics",
                "arguments": {
                    "repo": "policy-svc",
                    "topics": [
                        "search",
                        "index"
                    ]
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "policy-svc",
                    "message": "init topics"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "policy-svc",
                    "message": "readme"
                },
            },
            {
                "name": "ListBranches",
                "arguments": {
                    "repo": "policy-svc"
                }
            }
        ],
        "outputs": [
                "\"topics\": [\"search\", \"index\"]",
                "\"branches\": [\"main\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_798",
        "instruction": "Handle the creation of a repository named 'usage-collector' with the topics ['media', 'cdn'], commit 'init topics' followed by 'readme', and then list branches to confirm the presence of 'main'.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "usage-collector"
                },
            },
            {
                "name": "RepoTopics",
                "arguments": {
                    "repo": "usage-collector",
                    "topics": [
                        "media",
                        "cdn"
                    ]
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "usage-collector",
                    "message": "init topics"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "usage-collector",
                    "message": "readme"
                },
            },
            {
                "name": "ListBranches",
                "arguments": {
                    "repo": "usage-collector"
                }
            }
        ],
        "outputs": [
                "\"topics\": [\"media\", \"cdn\"]",
                "\"branches\": [\"main\"]"
        ]
    }
    ,
    {
        "annotator": variation_7,
        "user_id": "task_799",
        "instruction": "Handle the creation of a repository named 'query-planner' with the topics ['geo', 'routing'], commit 'init topics' followed by 'readme', and then list branches to confirm the presence of 'main'.",
        "actions": [
            {
                "name": "CreateRepo",
                "arguments": {
                    "name": "query-planner"
                },
            },
            {
                "name": "RepoTopics",
                "arguments": {
                    "repo": "query-planner",
                    "topics": [
                        "geo",
                        "routing"
                    ]
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "query-planner",
                    "message": "init topics"
                },
            },
            {
                "name": "AddCommit",
                "arguments": {
                    "repo": "query-planner",
                    "message": "readme"
                },
            },
            {
                "name": "ListBranches",
                "arguments": {
                    "repo": "query-planner"
                }
            }
        ],
        "outputs": [
                "\"topics\": [\"geo\", \"routing\"]",
                "\"branches\": [\"main\"]"
        ]
    }
]
