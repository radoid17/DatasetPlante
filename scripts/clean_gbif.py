# Curata datele, elimina duplicatele si pastreaza doar coloanele utile (am sters: country, latitude, longitude, observation_date, record_license si collection_date)
# Sterge sufixul "L." din numele stiintifice; pastreaza numele comune daca exista.
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_DIR / "data" / "sample.csv"
OUTPUT_FILE = PROJECT_DIR / "data" / "sample_clean.csv"

REQUIRED_COLUMNS = (
    "record_id",
    "scientific_name",
    "image_url",
    "source_url",
    "image_license",
)
OUTPUT_COLUMNS = [
    "record_id",
    "scientific_name",
    "common_name",
    "image_url",
    "source_url",
    "image_license",
]


def is_http_url(value: str) -> bool:
    """Return whether a non-empty value is an absolute HTTP(S) URL."""
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> None:
    df = pd.read_csv(INPUT_FILE, dtype=str, keep_default_na=False)
    df.columns = df.columns.str.strip()

    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing:
        raise ValueError(
            "Input CSV is missing required column(s): " + ", ".join(missing)
        )

    common_name_column = next(
        (name for name in ("common_name", "vernacularName") if name in df.columns),
        None,
    )
    if common_name_column:
        df["common_name"] = df[common_name_column]
    else:
        df["common_name"] = ""

    for column in (*REQUIRED_COLUMNS, "common_name"):
        df[column] = df[column].astype(str).str.strip()

    required_values = [
        "record_id",
        "scientific_name",
        "image_url",
        "source_url",
        "image_license",
    ]
    valid = df[required_values].ne("").all(axis=1)
    valid &= df["image_url"].map(is_http_url)
    valid &= df["source_url"].map(is_http_url)
    df = df.loc[valid].copy()

    df["scientific_name"] = df["scientific_name"].str.replace(
        r"^(\S+\s+\S+)\s+L\.$", r"\1", regex=True
    )

    df = df.drop_duplicates(subset="record_id", keep="first")

    columns = [column for column in OUTPUT_COLUMNS if column != "common_name"]
    if common_name_column:
        columns.insert(2, "common_name")
    df.loc[:, columns].to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

    print(f"Records after cleaning: {len(df)}")
    print(f"Saved cleaned file: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
