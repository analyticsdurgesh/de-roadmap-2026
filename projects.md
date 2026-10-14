# Data engineering project ideas

A project counts in an interview when the interviewer can open the repo, run it, read what broke, and see the number it produced. Interviewers grade three things: whether the project ran, whether you know why the number is right, and what you did when it was wrong.

## What every project needs

- A README that says what goes in and what comes out, the pipeline stages, the checks, and one measured result with the query that produced it.
- A way to run it from an empty folder: setup steps, sample data, one command.
- A quality gate, such as row counts, a reconciliation or a freshness check.
- A section called "what broke", with the fix.

Push each project to GitHub with an architecture diagram and a README that explains your design decisions. That is what off-campus recruiters open.

## Ideas by stage

| Stage | Project | What it proves |
|---|---|---|
| 1 | Clean CSV or API data, load it into relational tables, and write SQL checks for missing or duplicate records. | SQL, Python, basic data checks |
| 1 | A Python script that loads API data into Postgres on a cloud VM, with logging and error handling. | Python for data work, one cloud |
| 2 | A public dataset, such as e-commerce orders, modelled as a star schema in a warehouse free tier, with dbt models, tests and docs. | Data modelling, dbt |
| 3 | A batch ETL flow with staged, cleaned and analytics-ready tables, plus a small monitoring report. | Layered pipelines, monitoring |
| 3 | End to end: ingest from an API or files, transform with Spark or dbt, store as Delta or Iceberg, orchestrate with Airflow on your cloud, and put a dashboard on top. | The core 2026 stack |
| 4 | The stage 3 project with a Kafka feed through Spark Structured Streaming, data-quality tests, and cost notes in the README. | Streaming, data quality, cost awareness |

## Four builds with public repos

These four are on PrepNPlaced's [Data Engineering Projects](https://www.prepnplaced.com/data-engineering-projects) page, with what each one proves and the interview questions it draws.

### 1. The five-stage pipeline from the free book, broken on purpose

Chapter 13 of the [free book](https://www.prepnplaced.com/data-engineering-book) builds one pipeline in five stages from an empty folder, then breaks it four ways: a join that fans out, a load that runs twice, late-arriving rows, and a schema change. Stack: Python, SQL, Parquet and Airflow, with a mock API as the source. Repo: [data-engineering-book-field-kit](https://github.com/analyticsdurgesh/data-engineering-book-field-kit).

Do this one first. It teaches the shape the other three assume: ingest, validate, model, load, orchestrate, and check the final number against the source.

### 2. StreamCommerce Lakehouse 360

Orders and clickstream events stream through Kafka into a bronze, silver and gold medallion on Delta Lake, and a live revenue dashboard reads the gold layer. Stack: Kafka, Spark Structured Streaming, Delta Lake, Databricks. Repo: [StreamCommerce-Lakehouse-360](https://github.com/analyticsdurgesh/StreamCommerce-Lakehouse-360).

### 3. Retail Revenue Intelligence

Model retail data, compute revenue, cohort and retention metrics in SQL and Python, and ship a dashboard. It is the warehouse-and-BI shape most Indian analytics and data roles interview on, and the one of the four a data analyst can also claim. Stack: SQL, Python, pandas. Repo: [Retail-Revenue-Intelligence](https://github.com/analyticsdurgesh/Retail-Revenue-Intelligence).

### 4. Snowflake and dbt analytics engineering

Tested, documented dbt models and incremental pipelines into dimensional marts on Snowflake, with lineage. It answers the "have you used dbt for real" question. Stack: Snowflake, dbt, SQL. Repo: [Snowflake_DBT_Project](https://github.com/analyticsdurgesh/Snowflake_DBT_Project).

Projects 2 to 4 are built live in PrepNPlaced's Data Engineering cohort. The repos above are the instructor's reference versions.

## Putting a project on your resume

Write one line per project in the shape "built X that does Y, measured Z". For example: "Built a five-stage orders pipeline (Python, Airflow, Parquet) with a row-count quality gate; caught a join fan-out that overstated revenue by 44.9% in testing."

Then expect three questions on any project you list:

1. Walk me through the data flow.
2. What broke, and how did you know?
3. What would change at ten times the volume?

If you cannot answer the second one, the project is not ready for your resume. One project you can explain for fifteen minutes beats four you can explain for two.

Full guide: [Data Engineering Projects for Your Resume](https://www.prepnplaced.com/data-engineering-projects).
