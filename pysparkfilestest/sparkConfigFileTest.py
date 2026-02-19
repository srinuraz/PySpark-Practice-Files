import os
import tempfile
import pyspark
from pyspark.sql import SparkSession

static_tmp = "C:/spark_temp"
os.makedirs(static_tmp, exist_ok=True)

spark = (SparkSession.builder
    .config("spark.local.dir", static_tmp)
    .getOrCreate()
)