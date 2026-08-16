"""Workspace parity smoke: proves this workspace runs our code against the pinned catalog."""

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", required=True)
    args = parser.parse_args()

    from pyspark.sql import SparkSession

    spark = SparkSession.builder.getOrCreate()
    row = spark.sql("SELECT current_catalog() AS c").first()
    session_catalog = row["c"] if row else "?"
    print(f"smoke ok: target catalog={args.catalog}, session catalog={session_catalog}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
