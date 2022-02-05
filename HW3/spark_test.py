from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("MDA_2021") \
    .master("local[*]") \
    .getOrCreate()
    # .config('spark.ui.port', '4050') \

sc=spark.sparkContext
# sc.setLogLevel('ALL')

a = sc.parallelize([1,2,4,5,5])

print(a.take(2))

print()
