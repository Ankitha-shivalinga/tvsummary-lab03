import json
from pathlib import Path
import requests

SOURCE_URL = "https://api.tvmaze.com/shows?page=0"
OUTPUT = Path("summary.json")


def fetch_records(url):
    """Download the records and return them as Python objects."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def shows_per_genre(records):
    """Count the number of shows in each genre."""
    genre_counts = {}

    for record in records:
        if not isinstance(record, dict):
            continue

        genres = record.get("genres")

        if not isinstance(genres, list):
            continue

        valid_genres = {
            genre.strip()
            for genre in genres
            if isinstance(genre, str) and genre.strip()
        }

        for genre in sorted(valid_genres):
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts

def shows_per_decade(records):
    """Count the number of shows premiered in each decade."""
    decade_counts = {}

    for record in records:
        if not isinstance(record, dict):
            continue

        premiered = record.get("premiered")

        if not isinstance(premiered, str) or len(premiered) < 4:
            continue

        try:
            year = int(premiered[:4])
        except ValueError:
            continue

        decade = (year // 10) * 10
        decade_label = f"{decade}s"
        decade_counts[decade_label] = decade_counts.get(decade_label, 0) + 1

    return decade_counts

def build_summary(records):
    """Create a summary of the downloaded records."""
    summary = {
        "source_url": SOURCE_URL,
        "total_records": len(records),
        "shows_per_genre": shows_per_genre(records),
        "shows_per_decade": shows_per_decade(records)
    }

    return summary

def save_summary(summary, output):
    """Save the summary to a JSON file."""
    output.write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8"
    )

def main():
    """Run the program."""
    try:
        records = fetch_records(SOURCE_URL)
    except requests.RequestException as error:
        print(f"Error downloading data: {error}")
        return
    except ValueError as error:
        print(f"Error reading API response: {error}")
        return

    summary = build_summary(records)
    save_summary(summary, OUTPUT)
    print(f"Summary saved to {OUTPUT}")


if __name__ == "__main__":
    main()