from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .master("spark://127.0.0.1:7077") \
    .appName("Sample Kafka app") \
    .getOrCreate()
    # .config("spark.some.config.option", "some-value") \

people = [
    {"name":"Michael"},
    {"name":"Andy", "age":30},
    {"name":"Justin", "age":19},
]
df = spark.createDataFrame(data=people)
# Displays the content of the DataFrame to stdout
df.show()