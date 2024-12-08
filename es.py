from elasticsearch import Elasticsearch, helpers
import json

# Connect to Elasticsearch with authentication
es = Elasticsearch(
    hosts=["http://localhost:9200/"],
)

NUM_PARTS = 100000


def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        docs = [json.loads(line) for line in f]
    helpers.bulk(es, docs, index="reviews")


load_data(f"dataset_part_0.json")
