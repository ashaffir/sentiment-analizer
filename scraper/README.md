# Scraper service
1. Access API of various social networks
2. Retrieve the posts/messages and any relevant information
2.1 Periodic runs to collect information that is related to fields of interest (e.g. NFTs, crypto) 
2.2 Collect information that from influencers in fields of interest
3. Store the information in documents/collections according to the social network

# Interfaces
## Connected to MongoDB
## Communicated with the rest of the system via API (FastAPI)

# Setup

# Running

./run_server.sh

or 

uvicorn main:app --reload --port 8222 --log-config ./log.ini

# Testing

<!-- Reference -->
https://github.com/janstrohschein/KOARCH/tree/master/Use_Cases/other/Social_Media_Emotion_Detection
