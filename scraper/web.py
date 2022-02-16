"""Goolge search results

Google API Dashboard:
https://console.developers.google.com/apis/api/customsearch.googleapis.com/overview?authuser=1&project=moodalarm

Goolge Custom Search Console:
https://programmablesearchengine.google.com/cse/setup/basic?cx=b9434f8f13b9da3d5

Reference:
https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search

"""
import os
from platform import platform
from pydantic import confloat
from utils import blob_sentiment
from dotenv import dotenv_values

from googleapiclient.discovery import build

config = dotenv_values(".env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")


def google_search(search_term, api_key=GOOGLE_API_KEY, cse_id=GOOGLE_CSE_ID, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    items = res["items"]
    contents = [item["snippet"] for item in items]

    sia = blob_sentiment(contents)
    return sia


# results = google_search('"nft" "sculls" "skulls"', GOOGLE_API_KEY, GOOGLE_CSE_ID, num=10)
# results = google_search('"ukraine" "latest" "news"', GOOGLE_API_KEY, GOOGLE_CSE_ID, num=10)
# for result in results:
#     print(f"Title: {result['title']} >>>> {result['link']}")


# {'kind': 'customsearch#result',
#  'title': 'Blog — smART Advisory',
#  'htmlTitle': 'Blog — smART Advisory',
#  'link': 'https://nycgallerina.com/blog',
#  'displayLink': 'nycgallerina.com',
#  'snippet': "The recent Wikipedia editors' decision not to include NFT artists Beeple (known for ... The Sculls built their fortune through their taxi business and were\xa0...",
#  'htmlSnippet': 'The recent Wikipedia editors&#39; decision not to include <b>NFT</b> artists Beeple (known for ... The <b>Sculls</b> built their fortune through their taxi business and were&nbsp;...',
#  'cacheId': 'lb4fFzWslaUJ',
#  'formattedUrl': 'https://nycgallerina.com/blog',
#  'htmlFormattedUrl': 'https://nycgallerina.com/blog',
#  'pagemap':
#         {'metatags':
#          [
#              {'og:type': 'website',
#                 'twitter:title': 'Blog — smART Advisory',
#                 'twitter:card': 'summary',
#                 'og:site_name': 'smART Advisory',
#                 'viewport': 'width=device-width, initial-scale=1',
#                 'twitter:url': 'https://nycgallerina.com/blog',
#                 'twitter:description': 'Art History in a Nutshell with a Dash of Unconventional Wisdom',
#                 'og:title': 'Blog — smART Advisory',
#                 'og:url': 'https://nycgallerina.com/blog',
#                 'og:description': 'Art History in a Nutshell with a Dash of Unconventional Wisdom'
#            }]
#         }
# }
