#!/usr/bin/env python3

import json

from confluent_kafka import Producer
import yaml
import yfinance as yf

with open("config.yml", "r") as Y:
    config = yaml.safe_load(Y)

p = Producer({"bootstrap.servers": config["kafka"]["server"]})

data = yf.download(
    config["stock"]["symbol"], start=config["stock"]["start_date"], end=config["stock"]["end_date"], period="1d"
)
data["json"] = data.apply(lambda x: x.to_json(), axis=1)
for index, row in data.iterrows():
    p.produce(config["kafka"]["topic"], row["json"].encode(config["data"]["encoding"]))
p.flush()
