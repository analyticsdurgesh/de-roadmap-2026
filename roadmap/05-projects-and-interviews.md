# Stage 5: Projects, resume and interviews (from month 8)

Start applying from month 8, while you are still learning. Your projects are the proof, your resume points to them, and the interview loop tests whether you can defend them.

## Projects

Two or three projects you can defend for fifteen minutes each beat a long list of tutorials. If you can, cover the three shapes interviews ask about: a batch pipeline with orchestration, a streaming or lakehouse build, and a tested warehouse. See [projects.md](../projects.md) for ideas and four builds with public repos.

Every project should have:

- A README that says what goes in, what comes out, the checks, and one measured result.
- A way to run it from a clean clone.
- At least one check that would have caught a wrong result.
- A "what broke" section with the fix, because that is the interview question.

## Resume

- One line per project: what you built, the stack in brackets, and one measured result. The number is what the interviewer underlines.
- Link the repo.
- List only the tools you can back with a project, a work example or a clear explanation. Unsupported keywords create interview risk.

## Applying in India

- **Naukri:** use the exact keywords from your target job descriptions (PySpark, Airflow, AWS or Azure, SQL, dbt), because recruiters search for literal strings. Refresh the profile weekly.
- **LinkedIn:** for GCC and startup roles.
- **Referrals first:** they convert far better than cold applications.
- **Campus:** mass recruiters such as TCS, Infosys, Wipro and Accenture hire generic engineers and allocate them later. Take the offer and ask for data projects from day one.
- **Switching from testing, support or BI:** pivot internally first. A move to a data team inside your own company costs nothing and builds the data experience external recruiters look for.
- **Notice periods:** expect 60 to 90 days at services companies, and plan your interviews around it.

## Preparing for the interview, step by step

1. Find out the loop: product companies and GCCs usually run four to six rounds, services companies two or three.
2. Practise SQL every day: joins, window functions, CTEs and deduplication, explaining each query as you write it.
3. Practise Python for data work: reading files and APIs, dictionaries, and pandas-style transformations.
4. Learn what happens inside a Spark job: stages, shuffles, partitions, skew and broadcast joins.
5. Pick one cloud and draw a pipeline on it from ingestion to the warehouse, including what happens when a step fails.
6. Prepare one project you can explain end to end: the data, your design choices, what broke and what you changed.
7. Run two or three mock interviews, then spend your remaining days on the round you did worst in.

## Read in the free book

[Data Engineering: From Zero to Production & Interview Ready](https://www.prepnplaced.com/data-engineering-book) (free PDF):

- Chapter 13, *The Portfolio Project*: five stages from an empty folder, then broken on purpose four ways.
- Chapter 14, *The Interview Loop*: a system design framework, three designs worked end to end, the loop round by round, and thirty days of revision.

## Practise on PrepNPlaced

- [Data Engineer Interview Questions](https://www.prepnplaced.com/data-engineer-interview-questions): the loop, round by round.
- The companion repo: [data engineering interview questions, round by round](https://github.com/analyticsdurgesh/data-engineering-interview-questions), with every question linked to its worked answer.
- [AI Mock Interview](https://www.prepnplaced.com/ai-mock-interview): two free rounds, no card.
- [Resume Score](https://www.prepnplaced.com/ats-resume-checker): a free score for your resume.
- [Data Engineer Resume](https://www.prepnplaced.com/data-engineer-resume): format and bullet examples.

Full guides: [Data Engineer Roadmap](https://www.prepnplaced.com/data-engineer-roadmap) and [How to Become a Data Engineer in India](https://www.prepnplaced.com/how-to-become-data-engineer-india), Step 5.

---

Previous: [Stage 4: Streaming, data quality and AI-assisted pipelines](04-streaming-and-quality.md) · Back to the [roadmap overview](../README.md)
