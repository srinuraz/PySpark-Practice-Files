import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SCD2Test').getOrCreate()

# list of employee data
data = [["1001", "gaurav", "hyderabad","42000"],
["1002", "vijay", "hyderabad","45565"],
["1003", "akanksha","hyderabad", "52000"],
["1004", "niharika", "hyderabad","35000"]]

# specify column names
columns = ['id','name','location','salry']

# creating a dataframe from the lists of data
df_full = spark.createDataFrame(data, columns)

# list of employee data
data = [ ["1003", "akanksha","delhi", "65000"],
["1004", "niharika", "bihar",None],
["1005", "murali","vijaywada", "80000"],
["1002", "vijay", "hyderabad","45565"]
]

# specify column names
columns = ['id','name','location','salry']

# creating a dataframe from the lists of data
df_daily = spark.createDataFrame(data, columns)

from pyspark.sql.functions import *

df_full=df_full.withColumn("Active_Flag",lit("Y")).withColumn("From_date",\
to_date(current_date()))\
.withColumn("To_date",lit("Null"))
df_full.show()

df_daily=df_daily.withColumn("Active_Flage",lit("Y"))\
.withColumn("From_date",to_date(current_date()))\
.withColumn("To_date",lit("Null"))


update_ds = df_full.join(df_daily, ((df_full.id==df_daily.id) & (df_full.Active_Flag =='Y'
,"inner")))\
.filter(hash(df_full.name,df_full.location,df_full.salry) !=
hash(df_daily.name,df_daily.location,df_daily.salry))\
.select(df_full.id,
df_full.name,
df_full.location,
df_full.salry,
lit("N").alias("Active_Flag"),
df_full.From_date,
lit(to_date(current_date())).alias("To_Date"))
update_ds.show()

no_change = df_full.join(update_ds,((df_full.id==update_ds.id) & (df_full.Active_Flag =='Y'
,"left_anti")))
no_change.show()

insert_ds = df_daily.join(no_change,"id","left_anti")
insert_ds.show()

df_final=update_ds.union(insert_ds).union(no_change)
df_final.show()