import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType

# 1. Create a SparkSession instance
spark = SparkSession.builder.appName("MyApp").getOrCreate()

my_list = [1, 2, 3, 4]

# 2. Call createDataFrame on the 'spark' instance, not the class 'SparkSession'
my_df = spark.createDataFrame(my_list, IntegerType())

my_df.show()
