import tweepy
import config
import glob
import datetime as dt

CURRENT_YEAR = 2023

today = dt.date.today()
yesterday = (today - dt.timedelta(days=1)).strftime("%Y-%m-%d")

performance_dates = [
 '2023-06-28',
 '2023-06-30',
 '2023-07-01',
 '2023-07-02',
 '2023-07-03',
 '2023-07-05',
 '2023-07-07',
 '2023-07-08',
 '2023-07-09',
 '2023-07-10',
 '2023-07-11',
 '2023-07-12',
 '2023-07-13',
 '2023-07-14',
 '2023-07-15',
 '2023-07-16',
 '2023-07-17',
 '2023-07-18',
 '2023-07-19',
 '2023-07-20',
 '2023-07-21',
 '2023-07-22',
 '2023-07-23',
 '2023-07-24',
 '2023-07-25',
 '2023-07-25',
 '2023-07-26',
 '2023-07-28',
 '2023-07-29',
 '2023-07-30',
 '2023-07-31',
 '2023-08-01',
 '2023-08-02',
 '2023-08-03',
 '2023-08-04',
 '2023-08-05',
 '2023-08-06',
 '2023-08-07',
 '2023-08-08',
 '2023-08-10',
 '2023-08-11',
 '2023-08-12'
]

if yesterday in performance_dates:
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
else:
    print("No perforamces yesterday.")