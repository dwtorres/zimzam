"""Tiny transforms: one pure function (unit-tested), one Spark function (integration-tested)."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyspark.sql import DataFrame


def greet(name: str) -> str:
    return f"hello, {name}"


def add_watermark_column(df: "DataFrame", column: str = "_ingested_at") -> "DataFrame":
    from pyspark.sql import functions as F

    return df.withColumn(column, F.current_timestamp())
