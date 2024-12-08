import pandas as pd

# Load the CSV
df = pd.read_csv("steam_reviews.csv", chunksize=1000000)

# Write each chunk to JSON
for i, chunk in enumerate(df):
    chunk.to_json(f"json_data/dataset_part_{i}.json", orient="records", lines=True)
