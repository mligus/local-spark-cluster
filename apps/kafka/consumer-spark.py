import sys
from uuid import uuid1

# from pyspark import SparkContext, SparkConf
# from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StringType, StructField, StructType, DoubleType


if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .master("spark://127.0.0.1:7077") \
        .appName("Sample Kafka app") \
        .config("spark.streaming.stopGracefullyOnShutdown", True) \
        .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0') \
        .config("spark.sql.shuffle.partitions", 4) \
        .getOrCreate()

    sc = spark.sparkContext

    print(f"Application name: {sc.appName}")
    print(f"Master: {sc.master}")

    streaming_df = spark.readStream\
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9093") \
        .option("subscribe", "my-topic") \
        .load()
        # .option("startingOffsets", "earliest") \
    
    json_schema = StructType([
        StructField("sensor", StringType(), True),
        StructField("temp", DoubleType(), True),
        StructField("created_dt", StringType(), True),
    ])

    json_df = streaming_df.selectExpr("cast(value as string) as value")
    
    # writing_df = json_df.writeStream \
    #     .format("console") \
    #     .option("checkpointLocation","checkpoint_dir") \
    #     .start()

    # writing_df.awaitTermination()

    json_expanded_df = json_df.withColumn("value", from_json(json_df["value"], json_schema)).select("value.*") 

    print(json_expanded_df.schema)

    writing_df = json_expanded_df.writeStream \
        .format("console") \
        .start()
        # .option("checkpointLocation","checkpoint_dir") \
        # .outputMode("complete") \

    writing_df.awaitTermination()

    # json_expanded_df.show()

    # streaming_df.show()

    # sc = SparkContext(appName=”PythonStreamingRecieverKafkaWordCount”)
    # ssc = StreamingContext(sc, 2) # 2 second window    broker, topic = sys.argv[1:]
    # kvs = KafkaUtils.createStream(ssc, \
    #                               broker, \
    #                               “raw-event-streaming-consumer”,\{topic:1})     lines = kvs.map(lambda x: x[1])
    # counts = lines.flatMap(lambda line: line.split(“ “)) 
    #               .map(lambda word: (word, 1)) \
    #               .reduceByKey(lambda a, b: a+b)    counts.pprint()
    # ssc.start()
    # ssc.awaitTermination()