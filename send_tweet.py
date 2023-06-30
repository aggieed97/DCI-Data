import tweepy
import config
import glob

# Authenticate Twitter API
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Get file list
path = "/home/aggieed97/Python-Projects/DCI-Data/images/*.png"
image_list = glob.glob(path)

visual_images = []
music_images = []
ge_images = []
score_image = []
for image in image_list:
    if "visual" in image:
        visual_images.append(image)
    elif "music" in image:
        music_images.append(image)
    elif "general" in image:
        ge_images.append(image)
    else:
        score_image.append(image)

# Overall Maximum Score
media_max_score = api.media_upload(
    filename=score_image[0]
)

tweet_max_score = api.update_status(
    status="Here is the Current Ranking of #DCI2023 Drum Corps by Highest Score.\n\n#DCI #DrumCorpsInternational",
    media_ids=[media_max_score.media_id_string]
)

# Overall General Effect Score
media_max_ge_score = api.media_upload(
    filename=ge_images[0]
)

tweet_max_ge_score = api.update_status(
    status="Here is the Current Ranking of #DCI2023 Drum Corps by Highest GE Score.\n\n#DCI #DrumCorpsInternational",
    media_ids=[media_max_ge_score.media_id_string]
)

# Overall Visual Scores

visual_media_ids = []
for image in visual_images:
     res = api.media_upload(image)
     visual_media_ids.append(res.media_id)

tweet_visual_score = api.update_status(
    status="Here is the Current Ranking of #DCI2023 Drum Corps by Highest Visual Caption Scores and Visual Total Scores.\n\n#DCI #DrumCorpsInternational",
    media_ids=visual_media_ids
)

# Overall Music Scores
music_media_ids = []
for image in music_images:
     res = api.media_upload(image)
     music_media_ids.append(res.media_id)

tweet_music_score = api.update_status(
    status="Here is the Current Ranking of #DCI2023 Drum Corps by Highest Music Caption Scores and Music Total Scores.\n\n#DCI #DrumCorpsInternational",
    media_ids=music_media_ids
)
