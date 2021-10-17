#!/usr/bin/env python3

import json

from confluent_kafka import Consumer
import yaml

with open("config.yml", "r") as Y:
    config = yaml.safe_load(Y)

c = Consumer({"bootstrap.servers": config["kafka"]["server"], "group.id": "stockgroup"})
c.subscribe([config["kafka"]["topic"]])

while True:
    try:
        msg = c.poll(1.0)
        if msg is None or msg.error():
            continue
        data = json.loads(msg.value().decode(config["data"]["encoding"]))
        print(data)
    except KeyboardInterrupt:
        c.close()

