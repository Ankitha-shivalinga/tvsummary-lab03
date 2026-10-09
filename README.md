
# TVMaze Show Records

## Data source

This project uses the TVMaze API to download TV show records.

Source: https://api.tvmaze.com/shows?page=0

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Ankitha-shivalinga/week02-records.git
   ```

2. Create and activate a virtual environment.

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Run

Run the program using:

```bash
python records.py
```

The program downloads TV show records, calculates the aggregations and creates a `summary.json` file.

## Example output

The program downloaded 240 records in my test run.

The summary includes:

* Total number of records
* Number of shows in each genre
* Number of shows by premiere decade

Example:

```json
{
  "source_url": "https://api.tvmaze.com/shows?page=0",
  "total_records": 240,
  "shows_per_genre": {
    "Drama": 154,
    "Comedy": 66
  },
  "shows_per_decade": {
    "2010s": 179,
    "2000s": 51
  }
}
```

## Data quirks

* Some records may have missing genres.
* Some records may have missing or invalid premiere dates.
* Invalid records are skipped during aggregation.

## Design choices

* Lists store the downloaded records.
* Dictionaries store the aggregation counts.
* Sets remove duplicate genres within a record.
* A set comprehension filters valid genres.

## Known limitations

* The program uses a single TVMaze API page.
* The summary reflects the data available when the program is run.
