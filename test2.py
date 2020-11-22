# Based on sample code https://github.com/spnichol/youtube_tutorial/blob/master/youtube_videos.py
# Run this code to install: pip install --upgrade google-api-python-client oauth2client

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import csv
import json
from pandas import DataFrame as pd
from pandas import json_normalize

DEVELOPER_KEY = "XXX YOUTUBE API KEY XXX"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def main():

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        hl="pt-BR",
        maxResults=500,
        regionCode="BR"
    )
    response = request.execute()

    response_json = json.dumps(response)
    loaded_response = json.loads(response_json)
    df = json_normalize(loaded_response['items'])

#    print(df)
    print(df.columns)
    df.to_excel("response.xlsx")

if __name__ == "__main__":
    main()
