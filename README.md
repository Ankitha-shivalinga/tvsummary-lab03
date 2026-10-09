# TV Show Summary

## Data source

- **API:** TVMaze
- **URL:** https://api.tvmaze.com/shows?page=0
- **Records downloaded:** 240 in the checked run

## Setup

This project uses Python 3.11.

Create the Conda environment:

```bash
conda env create -f environment.yml
conda activate tvsummary
```

Install the package and its dependencies:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Run

From the project folder, run:

```bash
python main.py
```

The program downloads TV show records, calculates the summaries, and writes the result to `data/processed/summary.json`.

If the API request fails, the program displays an error message.

## Test

Run the unit tests with:

```bash
python -m unittest discover -s tests
```

The tests use handmade records and do not require a network connection.

## Layout

| File or folder | Purpose |
|---|---|
| `main.py` | Runs the summary program |
| `src/tvsummary/models.py` | Represents and cleans individual show records |
| `src/tvsummary/sources.py` | Downloads records from TVMaze |
| `src/tvsummary/aggregations.py` | Calculates genre and decade counts |
| `src/tvsummary/report.py` | Writes the summary JSON |
| `src/tvsummary/config.py` | Stores the URL, timeout, and output path |
| `src/tvsummary/__init__.py` | Exposes the package's public classes |
| `tests/` | Contains unit tests |
| `data/processed/summary.json` | Stores the generated summary |

## What moved where

The original single-file program was refactored into separate modules:

- Downloading moved to `sources.py`.
- Record cleaning moved to `models.py`.
- Genre and decade calculations moved to `aggregations.py`.
- JSON output moved to `report.py`.
- Configuration values moved to `config.py`.
- `main.py` coordinates the program.

## Design choices

A list holds the downloaded records. Each record is represented by a `ShowRecord` object, which cleans missing or malformed fields. Dictionaries store aggregation counts, and a set removes duplicate genres within an individual show.

The `Aggregation` base class defines the aggregation interface. `GenreAggregation` and `DecadeAggregation` override its aggregation method.

Only the source module imports `requests`. This keeps network access separate from data cleaning, aggregation, and report writing.

## Known limitations

The summary reflects the data returned by the selected TVMaze endpoint. Counts may change when the API data changes. The tests use handmade records rather than live API responses.