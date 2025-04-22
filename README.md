# Steam Reviews Visualization

## Overview  
This project leverages the **ELK Stack (Elasticsearch, Logstash, Kibana)** and **Docker** to analyze **1.6M+ gaming reviews** in real time. It demonstrates distributed system capabilities like **horizontal scaling, fault tolerance, and replication**, providing actionable insights into player sentiment and game popularity.  

## Key Features  
- **Real-time data processing**: Logstash pipelines ingest and transform gaming reviews into structured JSON.  
- **Distributed storage**: Elasticsearch shards and replicates data across 3 nodes for high availability.  
- **Interactive dashboards**: Kibana visualizes trends (e.g., 51.9% recommendation rate for PUBG).  
- **Containerized deployment**: Docker Compose simplifies setup and scaling.  
