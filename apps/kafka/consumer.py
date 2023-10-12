import json

from kafka import KafkaConsumer


consumer = KafkaConsumer(
    "my-topic",
    bootstrap_servers=["localhost:9093"],
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))