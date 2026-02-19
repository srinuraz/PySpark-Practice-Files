from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("SparkDemo")
    .config("spark.python.worker.faulthandler.enabled", "true")
    .config("spark.sql.execution.pyspark.udf.faulthandler.enabled", "true")
    .config("spark.python.worker.timeout", "300")
    .getOrCreate()
)

data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
df = spark.createDataFrame(data, ["name", "value"])

df.show()

#spark.stop()
