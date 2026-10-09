# TV Show Summary

## Data source

- **API:** TVMaze
- **URL:** https://api.tvmaze.com/shows?page=0
- **Records downloaded:** 240 in the current run

## Setup

This project uses Python 3.11.

Create the Conda environment:

```bash
conda env create -f environment.yml
conda activate tvsummary
```

Install the package in editable mode:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Run

Run the program from the project root:

```bash
python main.py
```

The program downloads TV show records, calculates summaries by genre and premiere decade, and saves the results to `data/processed/summary.json`.

## Test

Run the unit tests:

```bash
python -m unittest discover -s tests
```

The tests use handmade records and do not require a network connection.

## Layout

```text
tvsummary-lab03/
├── main.py
├── pyproject.toml
├── environment.yml
├── requirements.txt
├── README.md
├── data/
│   ├── raw/
│   └── processed/
│       └── summary.json
├── src/
│   └── tvsummary/
│       ├── __init__.py
│       ├── config.py
│       ├── models.py
│       ├── sources.py
│       ├── aggregations.py
│       └── report.py
└── tests/
    └── test_models.py
```

## What moved where

| Original responsibility | New location |
|---|---|
| Download TVMaze records | `src/tvsummary/sources.py` |
| Clean and represent show records | `src/tvsummary/models.py` |
| Count shows by genre and decade | `src/tvsummary/aggregations.py` |
| Configure the URL, timeout, and output path | `src/tvsummary/config.py` |
| Write the summary JSON | `src/tvsummary/report.py` |
| Coordinate the program | `main.py` |
| Test record handling | `tests/test_models.py` |

## Design choices

- A `ShowRecord` class cleans missing or malformed show data when each record is initialized.
- `Aggregation` is the base class for `GenreAggregation` and `DecadeAggregation`. Both subclasses implement their own aggregation behavior.
- Polymorphism allows the main program to process the aggregation objects through their shared interface.
- Dictionaries store the summary counts, and JSON provides a readable output format.
- Configuration values are kept separate from the program logic.
- The package uses a `src` layout and can be installed in editable mode.

## Known limitations

- The summary may change when the TVMaze API data changes.
- Downloading records requires a network connection.
- The tests use handmade records and test record handling without calling the live API.