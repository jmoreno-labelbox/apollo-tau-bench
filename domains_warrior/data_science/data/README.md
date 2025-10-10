# Rainforest Tau Bench - Data Science Domain

A comprehensive benchmark dataset for testing data science automation workflows, featuring a complete flood-risk analysis pipeline with 27 interconnected tables and perfect referential integrity.

## 📊 Dataset Overview

The `data_science_main` domain contains a realistic data science project for coastal flood risk prediction, with:

- **27 JSON tables** covering the entire data science lifecycle
- **Perfect referential integrity** across all foreign keys
- **5-10+ rows per table** for realistic testing scenarios
- **Complete file path consistency** in the central registry
- **Production-ready data structures** for automation testing

## 🎯 Task Guides

### Task 1: Data Intake and Preparation

**Objective**: Set up project structure, acquire environmental datasets, perform ETL, and capture literature references.

#### 📋 Required Tables

**Configuration & Setup:**
- `project_config.json` - Project parameters (target cities, forecast horizons)
- `file_directory.json` - Central file registry (updated as directories are created)

**Geographic & Weather Data:**
- `geocoding_results.json` - City coordinates and canonical names
- `weather_forecasts.json` - Hourly weather forecasts for target cities
- `noaa_station_searches.json` - Nearby NOAA tide stations
- `water_levels.json` - Observed water level data
- `tide_predictions.json` - Tide predictions for stations
- `coastal_meteorology.json` - Meteorological observations

**ETL & Processing:**
- `etl_runs.json` - ETL pipeline execution logs
- `processed_timeseries.json` - Merged and normalized timeseries data
- `qc_figures.json` - Quality control plots and visualizations

**Literature Research:**
- `zotero_searches.json` - Literature search queries and results
- `zotero_metadata.json` - Paper metadata and citations
- `zotero_fulltexts.json` - Available full-text papers

**System Logs:**
- `terminal_log.json` - Command execution and output logs

#### 🔄 Workflow Steps

1. **Project Setup**: Create directories and update `file_directory.json`
2. **Geocoding**: Use `geocoding_results.json` for city coordinates
3. **Weather Data**: Fetch forecasts using `weather_forecasts.json` structure
4. **NOAA Integration**: Discover stations via `noaa_station_searches.json`
5. **Tide Data**: Retrieve water levels and predictions from respective tables
6. **ETL Processing**: Run Python scripts, log to `etl_runs.json`
7. **Literature Search**: Query Zotero and store in literature tables
8. **Logging**: Record all operations in `terminal_log.json`

#### ✅ Verification Checklist

- [ ] All project directories exist in `file_directory.json`
- [ ] Geocoding returns valid lat/lon for target cities
- [ ] Weather forecasts cover configured horizon with required variables
- [ ] At least one NOAA station found within radius
- [ ] Water levels and tide predictions available for primary station
- [ ] ETL produces merged timeseries CSV and QC plots
- [ ] Zotero search returns results with metadata
- [ ] Terminal log contains success messages



---

### Task 2: Modeling and Evaluation

**Objective**: Engineer features, train baseline model, compute metrics, and prepare outputs.

#### 📋 Required Tables

**Environment & Dependencies:**
- `environment.json` - Python environment and package versions
- `file_store.json` - Code files and requirements.txt content

**Data Processing:**
- `processed_timeseries.json` - Input merged dataset
- `features.json` - Engineered features and definitions
- `model_config.json` - Model configuration parameters
- `dataset_split.json` - Train/test split information

**Modeling Pipeline:**
- `models.json` - Trained model metadata and paths
- `predictions.json` - Model predictions and outputs
- `metrics.json` - Model evaluation metrics

**Visualization:**
- `qc_figures.json` - Model performance plots

**Outputs:**
- `stakeholder_outputs.json` - Final deliverables for stakeholders

#### 🔄 Workflow Steps

1. **Environment Check**: Verify dependencies in `environment.json`
2. **Feature Engineering**: Load timeseries data, create features, save to `features.json`
3. **Target Definition**: Define risk thresholds in `model_config.json`
4. **Data Splitting**: Create time-based splits, log to `dataset_split.json`
5. **Model Training**: Train LogisticRegression, save to `models.json`
6. **Prediction**: Generate predictions, store in `predictions.json`
7. **Evaluation**: Compute AUC/accuracy, record in `metrics.json`
8. **Visualization**: Create summary plots, add to `qc_figures.json`
9. **Output Preparation**: Copy files to final locations, update `stakeholder_outputs.json`

#### ✅ Verification Checklist

- [ ] Requirements.txt exists with pandas, scikit-learn, matplotlib, seaborn, joblib
- [ ] Features CSV contains: timestamp, precip_24h_mm, tide_anomaly_6h_max_m, pressure_drop_6h_hpa
- [ ] Model config includes: classification_threshold_m, precip_24h_threshold_mm, test_split_fraction
- [ ] Split summary shows time-based method with non-zero train/test counts
- [ ] Model file (simple_model.joblib) exists and is non-zero size
- [ ] Predictions CSV has proba, pred columns matching test set size
- [ ] Metrics CSV contains numeric AUC and accuracy values
- [ ] Risk timeseries plot exists and is viewable
- [ ] Final outputs (predictions_final.csv, metrics_summary.csv) are available

---

### Task 3: Reporting and Communication

**Objective**: Create structured reports, insert metrics/figures, add references, and communicate results.

#### 📋 Required Tables

**Reporting Platform:**
- `notion_pages.json` - Notion page metadata and content structure
- `gmail_messages.json` - Email drafts and sent messages

**Content Sources:**
- `stakeholder_outputs.json` - Final predictions and metrics files
- `qc_figures.json` - Key visualizations for reports
- `zotero_metadata.json` - Literature references and citations

**Supporting Data:**
- `file_directory.json` - File paths for attachments and artifacts
- `terminal_log.json` - Operation confirmations

#### 🔄 Workflow Steps

1. **Notion Setup**: Create new page, record in `notion_pages.json`
2. **Page Retrieval**: Confirm page ID and prepare for updates
3. **Content Structure**: Add sections (Executive Summary, Data & Methods, Results, Limitations, Next Steps)
4. **Metrics Insertion**: Pull from `stakeholder_outputs.json`, insert into Results
5. **Figure Embedding**: Add key plots from `qc_figures.json`
6. **References**: Fetch citations from `zotero_metadata.json`, append References section
7. **Metadata Update**: Add file links to page properties
8. **Email Draft**: Create draft using Notion link and attachments
9. **Email Send**: Send to stakeholders, record in `gmail_messages.json`

#### ✅ Verification Checklist

- [ ] Notion page created with expected title and base properties
- [ ] Page can be retrieved and ID is stable
- [ ] Section blocks exist: Executive Summary, Data & Methods, Results, Limitations, Next Steps
- [ ] Metrics snippet from metrics_summary.csv inserted in Results
- [ ] Risk timeseries plot embedded/linked in Results section
- [ ] Zotero references fetched and References section appended
- [ ] Page properties include working links to predictions_final.csv, metrics_summary.csv, artifacts
- [ ] Email draft created with correct subject, Notion URL, recipients, attachments
- [ ] Email sent successfully with timestamp recorded

---

## 🗂️ Table Reference Guide

### Core Data Tables
| Table | Purpose | Key Fields | Related Tables |
|-------|---------|------------|----------------|
| `project_config.json` | Project parameters | target_city, forecast_horizon_days | geocoding_results, weather_forecasts |
| `geocoding_results.json` | City coordinates | query_city, latitude, longitude | weather_forecasts, noaa_station_searches |
| `weather_forecasts.json` | Weather data | city, timestamps, variables | coastal_meteorology |
| `noaa_station_searches.json` | Station discovery | station_ids, station_names | water_levels, tide_predictions |
| `water_levels.json` | Observed water levels | station_id, timestamps, water_level_m | tide_predictions, coastal_meteorology |
| `tide_predictions.json` | Tide predictions | station_id, timestamps, tide_pred_m | water_levels |
| `coastal_meteorology.json` | Meteorological data | station_id, timestamps, variables | weather_forecasts |

### ML Pipeline Tables
| Table | Purpose | Key Fields | Related Tables |
|-------|---------|------------|----------------|
| `processed_timeseries.json` | Merged dataset | csv_path, columns, row_count | features, models |
| `features.json` | Engineered features | csv_path, feature_names | processed_timeseries, models |
| `model_config.json` | Model parameters | classification_threshold_m, test_split_fraction | models, dataset_split |
| `dataset_split.json` | Train/test splits | method, train_index_count, test_index_count | models, predictions |
| `models.json` | Trained models | model_name, model_path, feature_names | predictions, metrics |
| `predictions.json` | Model outputs | model_name, predictions_csv_path, row_count | models, metrics |
| `metrics.json` | Model evaluation | model_name, auc_nullable, accuracy_nullable | models, predictions |

### Literature & Documentation
| Table | Purpose | Key Fields | Related Tables |
|-------|---------|------------|----------------|
| `zotero_searches.json` | Search queries | query, result_item_ids | zotero_metadata, zotero_fulltexts |
| `zotero_metadata.json` | Paper metadata | item_ids, titles, authors | zotero_searches |
| `zotero_fulltexts.json` | Full-text papers | item_ids, file_paths | zotero_metadata |
| `notion_pages.json` | Report pages | page_id, title, sections_present | stakeholder_outputs, qc_figures |
| `gmail_messages.json` | Email communications | subject, recipients, attachments_paths | stakeholder_outputs |

### System & Infrastructure
| Table | Purpose | Key Fields | Related Tables |
|-------|---------|------------|----------------|
| `file_directory.json` | File registry | paths, file_sizes_bytes, file_hashes_sha256 | All tables with file paths |
| `etl_runs.json` | ETL execution logs | run_id, input_paths, output_paths | processed_timeseries, qc_figures |
| `terminal_log.json` | Command logs | commands, exit_codes, printed_messages | All operations |
| `environment.json` | Python environment | packages_installed, requirements_path_nullable | file_store |
| `file_store.json` | File contents | paths, file_contents_text | environment, models |
| `mcp_tool_calls.json` | Tool execution | server_names, tool_names, params_json | All API calls |
| `qc_figures.json` | Visualizations | figure_paths, descriptions | etl_runs, models |
| `stakeholder_outputs.json` | Final deliverables | predictions_final_csv_path, metrics_summary_csv_path | predictions, metrics |

## 🔗 Foreign Key Relationships

### Station-based Relationships
- `noaa_station_searches.station_ids[]` → `water_levels.station_id`
- `noaa_station_searches.station_ids[]` → `tide_predictions.station_id`
- `noaa_station_searches.station_ids[]` → `coastal_meteorology.station_id`

### Model-based Relationships
- `models.model_name` → `predictions.model_name`
- `models.model_name` → `metrics.model_name`
- `models.model_path` → `file_directory.paths[]`

### File-based Relationships
- `models.model_path` → `file_directory.paths[]`
- `predictions.predictions_csv_path` → `file_directory.paths[]`
- `metrics.metrics_csv_path` → `file_directory.paths[]`
- `features.csv_path` → `file_directory.paths[]`
- `processed_timeseries.csv_path` → `file_directory.paths[]`

### Literature Relationships
- `zotero_searches.result_item_ids[]` → `zotero_metadata.item_ids[]`
- `zotero_searches.result_item_ids[]` → `zotero_fulltexts.item_ids[]`

### City-based Relationships
- `project_config.target_city` → `geocoding_results.query_city`
- `project_config.target_city` → `weather_forecasts.city`
- `project_config.target_city` → `noaa_station_searches.query_latitude/longitude`

## 🚀 Getting Started

1. **Clone the repository** and navigate to the data science domain
2. **Review the task guides** above for your specific automation needs
3. **Use the table reference guide** to understand data relationships
4. **Follow the verification checklists** to ensure complete workflows
5. **Leverage the foreign key relationships** for data validation

## 📝 Notes

- All file paths in the dataset use leading slashes (e.g., `/models/simple_model.joblib`)
- Timestamps are in ISO 8601 format (UTC)
- Nullable fields are properly handled throughout the dataset
- All tables maintain referential integrity for realistic testing scenarios
- The dataset supports both individual task testing and end-to-end workflow validation

---

*This dataset provides a comprehensive foundation for testing data science automation workflows with realistic, interconnected data structures.*
