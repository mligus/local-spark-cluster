import random
import json

from datetime import datetime

from kafka import KafkaProducer
from kafka.errors import KafkaError


producer = KafkaProducer(
    bootstrap_servers=["localhost:9093"],
    value_serializer=lambda m: json.dumps(m).encode("utf-8"),
)

for _ in range(100):
    future = producer.send("my-topic", {
        "sensor": random.choice(["foo", "bar", "baz"]),
        "temp": random.random() * 100,
        "created_at": datetime.utcnow().isoformat(),
    })
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        # log.exception()
        print("Error!")
        pass
    print (record_metadata.topic)
    print (record_metadata.partition)
    print (record_metadata.offset)

producer.flush()
producer.close()