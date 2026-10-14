# Contributing

Thanks for helping. This roadmap is condensed from free guides on prepnplaced.com, so changes follow the site.

**Good pull requests:** a broken link, a typo, a tool that has been renamed or retired, a sentence that is wrong. Keep each change small and say why in the description.

**Open an issue instead** to add a stage, a tool or a resource. Changes to the plan itself go into the guide on prepnplaced.com first and then here, so the two never disagree.

**House style:** plain words and short sentences. Facts a reader can check, with a link. No marketing language and no em dashes.

**Before you open a pull request,** run the link check. It needs Python 3.9 or later and no packages:

```bash
python3 scripts/check_links.py            # offline: files, hosts, house style
python3 scripts/check_links.py --online   # also fetches every linked page
```

By contributing, you agree that your text is licensed under CC BY 4.0 and your code under MIT, like the rest of the repo.
