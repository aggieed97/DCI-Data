import requests
import json

from datetime import datetime
import datetime as dt
from bs4 import BeautifulSoup

import dict_digger

import pandas as pd


CURRENT_YEAR = 2023

today = dt.date.today()
yesterday = (today - dt.timedelta(days=1)).strftime("%Y-%m-%d")

urls = [
 'https://www.dci.org/scores/recap/2023-midwest-premiere',
 'https://www.dci.org/scores/recap/2023-dci-central-indiana',
 'https://www.dci.org/scores/recap/2023-corps-at-the-crest-san-diego',
 'https://www.dci.org/scores/recap/2023-drums-on-parade',
 'https://www.dci.org/scores/recap/2023-the-beanpot',
 'https://www.dci.org/scores/recap/2023-cavalcade-of-brass',
 'https://www.dci.org/scores/recap/2023-dci-east-coast-showcase-quincy',
 'https://www.dci.org/scores/recap/2023-western-corps-connection',
 'https://www.dci.org/scores/recap/2023-drums-across-the-desert',
 'https://www.dci.org/scores/recap/2023-rotary-music-festival',
 'https://www.dci.org/scores/recap/2023-summer-music-games-in-cincinnati',
 'https://www.dci.org/scores/recap/2023-midcal-champions-showcase',
 'https://www.dci.org/scores/recap/2023-midwest-classic',
 'https://www.dci.org/scores/recap/2023-crownbeat',
 'https://www.dci.org/scores/recap/2023-drum-corps-at-the-rose-bowl',
 'https://www.dci.org/scores/recap/2023-whitewater-classic',
 'https://www.dci.org/scores/recap/2023-dci-macon',
 'https://www.dci.org/scores/recap/2023-dci-west',
 'https://www.dci.org/scores/recap/2023-river-city-rhapsody-la-crosse',
 'https://www.dci.org/scores/recap/2023-dci-capital-classic',
 'https://www.dci.org/scores/recap/2023-drums-across-america',
 'https://www.dci.org/scores/recap/2023-resound',
 'https://www.dci.org/scores/recap/2023-the-kiwanis-thunder-of-drums',
    '2023-celebration-in-brass',
    '2023-corps-encore',
    '2023-drums-on-the-chippewa',
    '2023-dci-tupelo',
    '2023-drums-along-the-rockies-cheyenne-edition',
    '2023-music-on-the-march',
    '2023-riverside-open',
    '2023-dci-little-rock',
    '2023-drums-across-the-river-region',
    '2023-drums-along-the-rockies',
    '2023-gold-showcase',
    '2023-show-of-shows',
    '2023-so-cal-classic',
    '2023-brass-impact',
    '2023-west-texas-drums',
    '2023-dci-abilene',
    '2023-dci-broken-arrow',
    '2023-dci-austin',
    '2023-dci-denton',
    '2023-dci-houston',
    '2023-white-rose-classic',
    '2023-summer-thunder',
    '2023-dci-connecticut',
    '2023-dci-mesquite',
    '2023-dci-mckinney',
    '2023-dci-new-hampshire',
    '2023-brigadiers-pageant-of-drums',
    '2023-dci-monroe',
    '2023-dci-southern-mississippi',
    '2023-dci-birmingham',
    '2023-music-on-the-mountain',
    '2023-the-masters-of-the-summer-music-games',
    '2023-beats-in-the-brook',
    '2023-nightbeat',
    '2023-dci-huntington',
    '2023-drum-corps-an-american-tradition',
    '2023-drums-across-the-smokies',
    '2023-summer-music-games-of-southwest-virginia',
    '2023-dci-glassboro',
    '2023-march-on',
    '2023-soaring-sounds',
    '2023-dci-east-coast-showcase-lawrence',
    '2023-drums-in-the-heartland',
    '2023-tournament-of-drums',
    '2023-dci-eastern-illinois',
    '2023-shoremen-brass-classic',
    '2023-dci-pittsburgh',
    '2023-dci-cincinnati',
    '2023-innovations-in-brass',
    '2023-lake-erie-fanfare',
]

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

corps = [
        'Blue Devils', 'Blue Knights', 'Blue Stars', 'Bluecoats', 'Boston Crusaders', 'Carolina Crown', 'Colts', 'Crossmen', 'Genesis', 'Jersey Surf',
        'Madison Scouts', 'Mandarins', 'Music City', 'Pacific Crest', 'Phantom Regiment', 'Santa Clara Vanguard', 'Seattle Cascades', 'Spirit of Atlanta',
        'The Academy', 'The Cadets', 'The Cavaliers', 'Troopers'
        ]

if yesterday in performance_dates:
    score_recap_df = pd.DataFrame()

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        script = soup.find_all('script')[7].text.strip()[16:-1]
        data = json.loads(script)

        competition = dict_digger.dig(data, 'state', 'competitions', 'current')

        if competition:
            corp_list = []

            for item in competition:
                corp_name = item['groupName']

                if corp_name in corps:
                    total_score = item['totalScore']
                    competition_date = datetime.strptime(item['competition']['date'], "%Y-%m-%dT%H:%M:%S").date()
                    location = item['competition']['location']
                    event_name = item['competition']['eventName']

                    print(f"Processing {corp_name} in {location}")

                    general_effect_total_score = item['categories'][0]['Score']
                    visual_total_score = item['categories'][1]['Score']
                    music_total_score = item['categories'][2]['Score']

                    general_effect1_judge = item['categories'][0]['Captions'][0]['JudgeFirstName'] + ' ' + \
                                            item['categories'][0]['Captions'][0]['JudgeLastName']
                    general_effect2_judge = item['categories'][0]['Captions'][1]['JudgeFirstName'] + ' ' + \
                                            item['categories'][0]['Captions'][1]['JudgeLastName']
                    general_effect1_score = item['categories'][0]['Captions'][0]['Score']
                    general_effect2_score = item['categories'][0]['Captions'][1]['Score']

                    visual_proficiency_judge = item['categories'][1]['Captions'][0]['JudgeFirstName'] + ' ' + \
                                               item['categories'][1]['Captions'][0]['JudgeLastName']
                    visual_proficiency_score = item['categories'][1]['Captions'][0]['Score']

                    visual_analysis_judge = item['categories'][1]['Captions'][1]['JudgeFirstName'] + ' ' + \
                                            item['categories'][1]['Captions'][1]['JudgeLastName']
                    visual_analysis_score = item['categories'][1]['Captions'][1]['Score']

                    visual_color_guard_judge = item['categories'][1]['Captions'][2]['JudgeFirstName'] + ' ' + \
                                               item['categories'][1]['Captions'][2]['JudgeLastName']
                    visual_color_guard_score = item['categories'][1]['Captions'][2]['Score']

                    try:
                        music_brass_judge = item['categories'][2]['Captions'][0]['JudgeFirstName'] + ' ' + \
                                            item['categories'][2]['Captions'][0]['JudgeLastName']
                    except:
                        music_brass_judge = "Judge"

                    music_brass_score = item['categories'][2]['Captions'][0]['Score']

                    try:
                        music_analysis_judge = item['categories'][2]['Captions'][1]['JudgeFirstName'] + ' ' + \
                                               item['categories'][2]['Captions'][1]['JudgeLastName']
                    except:
                        music_analysis_judge = "Judge"

                    music_analysis_score = item['categories'][2]['Captions'][1]['Score']

                    music_percussion_judge = item['categories'][2]['Captions'][2]['JudgeFirstName'] + ' ' + \
                                             item['categories'][2]['Captions'][2]['JudgeLastName']
                    music_percussion_score = item['categories'][2]['Captions'][2]['Score']

                    scores = {
                        'date': competition_date,
                        'location': location,
                        'event_name': event_name,
                        'drum_corps': corp_name,
                        'general_effect1_judge': general_effect1_judge,
                        'general_effect2_judge': general_effect2_judge,
                        'visual_proficiency_judge': visual_proficiency_judge,
                        'visual_analysis_judge': visual_analysis_judge,
                        'visual_color_guard_judge': visual_color_guard_judge,
                        'music_brass_judge': music_brass_judge,
                        'music_analysis_judge': music_analysis_judge,
                        'music_percussion_judge': music_percussion_judge,
                        'general_effect1_score': general_effect1_score,
                        'general_effect2_score': general_effect2_score,
                        'general_effect_total_score': general_effect_total_score,
                        'visual_proficiency_score': visual_proficiency_score,
                        'visual_analysis_score': visual_analysis_score,
                        'visual_color_guard_score': visual_color_guard_score,
                        'visual_total_score': visual_total_score,
                        'music_brass_score': music_brass_score,
                        'music_analysis_score': music_analysis_score,
                        'music_percussion_score': music_percussion_score,
                        'music_total_score': music_total_score,
                        'total_score': total_score
                    }

                    corp_list.append(scores)

            temp_df = pd.DataFrame(corp_list)
            score_recap_df = pd.concat([score_recap_df, temp_df])
        else:
            pass

    score_recap_df.to_csv(f'./data/{CURRENT_YEAR}-DCI-Caption-Score-Recaps.csv', index=False)

else:
    print(f'No performances for {yesterday}')