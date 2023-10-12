from pyspark.sql import SparkSession

SparkSession.builder.master("spark://127.0.0.1:7077").getOrCreate().stop()