import tweepy
import config
import glob

## Authenticate Twitter API
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

## Get file list
path = "/home/aggieed97/Python-Projects/DCI-Data/images/*.png"
image_list = glob.glob(path)

for image in image_list:

    media_max_score = api.media_upload(
        filename=image
    )

    tweet_max_score = api.update_status(
        status="Testing Max Score Image",
        media_ids=[media_max_score.media_id_string]
    )