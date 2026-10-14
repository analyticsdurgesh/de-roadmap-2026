# Data Engineering Roadmap 2026 (India)

A free, ordered plan for becoming a data engineer in 2026, written for learners in India. Five stages, the skills in each, the proof to build, the free resources, and the chapter of the free book that covers it.

**The short answer:** learn SQL and Python first, then data modelling and one warehouse, then Spark, Airflow, dbt and one lakehouse format on a single cloud (AWS or Azure), then Kafka and data-quality checks. Build projects you can defend as you go. From scratch, at two to three hours a day, plan for 8 to 12 months to job-ready.

The full guide, with FAQs, certifications and salary bands, is the [Data Engineering Roadmap 2026 on PrepNPlaced](https://www.prepnplaced.com/data-engineering-roadmap-2026?utm_source=github&utm_medium=oss_repo&utm_campaign=de_roadmap_2026). The free book that goes with it is [Data Engineering: From Zero to Production & Interview Ready](https://www.prepnplaced.com/data-engineering-book?utm_source=github&utm_medium=oss_repo&utm_campaign=de_roadmap_2026).

## The five stages

| Stage | When | What you learn | What to show at the end | Free book |
|---|---|---|---|---|
| [1. Foundations](roadmap/01-foundations.md) | Months 1 to 3 | SQL to an advanced level, Python for data work, one cloud (AWS or Azure) | A Python script that loads API data into Postgres on a cloud VM | Lecture Zero, Chapters 1 to 4 |
| [2. Data modelling and the warehouse](roadmap/02-data-modelling.md) | Months 4 to 7 | Grain, star schemas, facts and dimensions, SCD Types 1 and 2, OLTP vs OLAP, columnar storage, dbt basics | A public dataset modelled as a star schema in a warehouse free tier, with dbt tests | Chapters 5 and 6 |
| [3. Spark, Airflow and the lakehouse](roadmap/03-spark-airflow-lakehouse.md) | Months 4 to 7 | PySpark, Airflow with dbt, Delta Lake or Iceberg, your cloud's data services | One end-to-end project: ingest, transform with dbt, orchestrate with Airflow, store as Delta or Iceberg | Chapters 7 to 10 |
| [4. Streaming, data quality and AI-assisted pipelines](roadmap/04-streaming-and-quality.md) | Months 8 to 10 | Kafka, Spark Structured Streaming, data-quality gates, reviewing AI-generated SQL and PySpark | The same project with a streaming feed, quality tests and cost notes | Chapters 11 and 12 |
| [5. Projects, resume and interviews](roadmap/05-projects-and-interviews.md) | From month 8 | Portfolio, resume lines, Naukri and LinkedIn, the interview loop | Two or three projects you can explain for fifteen minutes each | Chapters 13 and 14 |

Stages 2 and 3 overlap. The 2026 plan puts dbt, the warehouse, Spark, Airflow and a lakehouse format in the same block, months 4 to 7: you model the data while you learn the tools that move it.

## What changed for 2026

- Lakehouse is the default architecture. New job descriptions name Delta Lake or Apache Iceberg directly.
- dbt has moved from nice-to-have to expected for transformation work.
- Interviews now test whether you can review and debug AI-generated SQL and Spark code.
- Kafka and streaming appear in a growing share of GCC and product-company postings.
- Batch-only skill sets are getting filtered out at product companies.

## Learn now, skip for now

**Learn:** SQL, Python, PySpark, Airflow, dbt, Kafka, one cloud, Delta Lake or Iceberg, Docker basics, Git.

**Skip for now:** Hadoop MapReduce and Hive tuning (legacy maintenance only), Scala-first learning (Python covers Indian interviews), learning three clouds, and stacking certifications.

**Pick one cloud:** Azure is especially common at services companies and GCCs; AWS leads at product startups. Recruiters filter for depth in one stack.

**Match your target:** for services companies, add Azure Data Factory and Synapse or Fabric pipelines. For product companies, go deeper on Spark internals, data modelling and system design rounds.

**Certifications:** one at most, matched to your cloud: Databricks Data Engineer Associate, AWS Data Engineer Associate or Azure DP-700. No certificate substitutes for a deployed end-to-end project.

## How long it takes

From scratch, 8 to 12 months at two to three hours a day. If you already work with SQL, for example in support, testing or admin roles, 6 to 8 months. The end-to-end project in months 4 to 7 is the one part you cannot skip.

## In this repo

- [roadmap/](roadmap/): one file per stage, with skills, what to skip, the proof to build, book chapters and practice links.
- [projects.md](projects.md): project ideas for each stage, and four builds with public repos.
- [resources.md](resources.md): the free resources, in the order to use them.
- [checklist.md](checklist.md): the job-ready checklist, stage by stage.

When you reach stage 5, use the companion repo, [data engineering interview questions, round by round](https://github.com/analyticsdurgesh/data-engineering-interview-questions), or the [Data Engineer Interview Questions](https://www.prepnplaced.com/data-engineer-interview-questions) page.

## About

This roadmap is written and maintained by [Durgesh Yadav](https://www.prepnplaced.com/durgesh-yadav), founder of [PrepNPlaced](https://www.prepnplaced.com) and a Senior Data Engineer at 7-Eleven. He wrote the free book *Data Engineering: From Zero to Production & Interview Ready* and runs PrepNPlaced's 1:1 Data Engineering and Data Analytics [mentorships](https://www.prepnplaced.com/mentorship).

PrepNPlaced is a career platform for technical job seekers in India, started in June 2026 in Bengaluru by Durgesh Yadav and Pragya Rathi. Everything in this repo is condensed from its free guides, and each file links to the full page.

## How this is maintained

Maintained by Durgesh Yadav. Each stage follows the free guides on prepnplaced.com, and this repo is updated when those guides change, so the two do not disagree. Last checked against the site on 2 October 2026. If a link breaks or a tool name goes stale, open an issue.

## Contributing

Small fixes are welcome as pull requests: a broken link, a typo, a renamed tool. Ideas for new stages, tools or resources go in an issue first. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

The text in this repo is licensed under [CC BY 4.0](LICENSE-CC-BY-4.0). You can copy and adapt it, including commercially, if you give credit, for example: "Data Engineering Roadmap 2026 by Durgesh Yadav, PrepNPlaced (https://www.prepnplaced.com/data-engineering-roadmap-2026), CC BY 4.0".

The code in [scripts/](scripts/) is licensed under the [MIT License](LICENSE).
