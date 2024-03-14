'''
Spark with PySpark:
Apache Spark is a distributed processing system used to
perform big data and machine learning tasks on large datasets.
'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct

spark = SparkSession.builder.appName("Datacamp Pyspark Tutorial")\
            .config("spark.memory.offHeap.enabled","true")\
                .config("spark.memory.offHeap.size","10g").getOrCreate()
df = spark.read.csv('online_retail.csv',header=True,escape="\"")
# a = df.head(5)
# a = df.count()
# print(a)


df.groupBy('Country').agg(countDistinct('CustomerID').alias('country_count')).show()
