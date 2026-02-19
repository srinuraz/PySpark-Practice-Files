from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SCD-1Test').getOrCreate()

# list of employee data
data = [["1001", "gaurav", "hyderabad","42000"],
["1002", "vijay", "hyderabad","45565"],
["1003", "akanksha","hyderabad", "52000"],
["1004", "niharika", "hyderabad","35000"]]
# specify column names
columns = ['id','name','location','salry']
# creating a dataframe from the lists of data
df_full = spark.createDataFrame(data, columns)

print("Full data...")
df_full.show()

# list of employee data
data = [ ["1003", "akanksha","delhi", "65000"],
["1004", "niharika", "bihar","10000"],
["1005", "murali","vijaywada", "80000"],
["1002", "vijay", "hyderabad","45565"]
]
# specify column names
columns = ['id','name','location','salry']
# creating a dataframe from the lists of data
df_daily_update = spark.createDataFrame(data, columns)

print("daily data...")
df_daily_update.show()


from pyspark.sql.functions import coalesce
res=df_full.join(df_daily_update,"id","full_outer").\
select(coalesce(df_full.id,df_daily_update.id).alias("ID"),\
coalesce(df_daily_update.name,df_full.name).alias("Name"),\
coalesce(df_daily_update.location,df_full.location).alias("Location"),\
coalesce(df_daily_update.salry,df_full.salry).alias("Salary")
)
res.show()