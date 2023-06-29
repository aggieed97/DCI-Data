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

larger_urls = [
        "https://www.dci.org/scores/recap/2023-dci-southwestern-championship",
        'https://www.dci.org/scores/recap/2023-dci-southeastern-championship',
        'https://www.dci.org/scores/recap/2023-dci-eastern-classic-2',
        'https://www.dci.org/scores/recap/2023-dci-eastern-classic',
        'https://www.dci.org/scores/recap/2023-dci-world-championship-prelims',
        'https://www.dci.org/scores/recap/2023-dci-world-championship-semifinals',
        'https://www.dci.org/scores/recap/2023-dci-world-championship-finals'
]

performance_dates = [
 '2023-07-22',
 '2023-07-29',
 '2023-08-04',
 '2023-08-05',
 '2023-08-10',
 '2023-08-11',
 '2023-08-12'
]

if yesterday in performance_dates:
    larger_comps_df = pd.DataFrame()

    for url in larger_urls:
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

                    general_effect1_judge = item['categories'][0]['Captions'][0]['JudgeLastName'] + '/' + \
                                            item['categories'][0]['Captions'][1]['JudgeLastName']
                    general_effect2_judge = item['categories'][0]['Captions'][2]['JudgeLastName'] + '/' + \
                                            item['categories'][0]['Captions'][3]['JudgeLastName']

                    general_effect1a_score = item['categories'][0]['Captions'][0]['Score']
                    general_effect1b_score = item['categories'][0]['Captions'][1]['Score']
                    general_effect2a_score = item['categories'][0]['Captions'][2]['Score']
                    general_effect2b_score = item['categories'][0]['Captions'][3]['Score']

                    visual_proficiency_judge = item['categories'][1]['Captions'][0]['JudgeFirstName'] + ' ' + \
                                               item['categories'][1]['Captions'][0]['JudgeLastName']
                    visual_proficiency_score = item['categories'][1]['Captions'][0]['Score']

                    visual_analysis_judge = item['categories'][1]['Captions'][1]['JudgeFirstName'] + ' ' + \
                                            item['categories'][1]['Captions'][1]['JudgeLastName']
                    visual_analysis_score = item['categories'][1]['Captions'][1]['Score']

                    visual_color_guard_judge = item['categories'][1]['Captions'][2]['JudgeFirstName'] + ' ' + \
                                               item['categories'][1]['Captions'][2]['JudgeLastName']
                    visual_color_guard_score = item['categories'][1]['Captions'][2]['Score']

                    music_brass_judge = item['categories'][2]['Captions'][0]['JudgeFirstName'] + ' ' + \
                                        item['categories'][2]['Captions'][0]['JudgeLastName']
                    music_brass_score = item['categories'][2]['Captions'][0]['Score']

                    if len(competition[-1]['categories'][2]['Captions']) == 4:
                        music_analysis_judge = item['categories'][2]['Captions'][1]['JudgeLastName'] + '/' + \
                                               item['categories'][2]['Captions'][2]['JudgeLastName']
                        # music_analysis2_judge = item['categories'][2]['Captions'][2]['JudgeFirstName'] + ' ' + item['categories'][2]['Captions'][2]['JudgeLastName']
                        music_analysis1_score = item['categories'][2]['Captions'][1]['Score']
                        music_analysis2_score = item['categories'][2]['Captions'][2]['Score']

                        music_percussion_judge = item['categories'][2]['Captions'][3]['JudgeFirstName'] + ' ' + \
                                                 item['categories'][2]['Captions'][3]['JudgeLastName']
                        music_percussion_score = item['categories'][2]['Captions'][3]['Score']
                    else:
                        music_analysis_judge = item['categories'][2]['Captions'][1]['JudgeFirstName'] + ' ' + \
                                               item['categories'][2]['Captions'][1]['JudgeLastName']
                        music_analysis1_score = item['categories'][2]['Captions'][1]['Score']
                        music_analysis2_score = 0

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
                        'general_effect1a_score': general_effect1a_score,
                        'general_effect1b_score': general_effect1b_score,
                        'general_effect2a_score': general_effect2a_score,
                        'general_effect2b_score': general_effect2b_score,
                        'general_effect_total_score': general_effect_total_score,
                        'visual_proficiency_score': visual_proficiency_score,
                        'visual_analysis_score': visual_analysis_score,
                        'visual_color_guard_score': visual_color_guard_score,
                        'visual_total_score': visual_total_score,
                        'music_brass_score': music_brass_score,
                        'music_analysis1_score': music_analysis1_score,
                        'music_analysis2_score': music_analysis2_score,
                        'music_percussion_score': music_percussion_score,
                        'music_total_score': music_total_score,
                        'total_score': total_score
                    }
                    corp_list.append(scores)

            temp_df = pd.DataFrame(corp_list)
            larger_comps_df = pd.concat([larger_comps_df, temp_df])
        else:
            pass

    larger_comps_df.to_csv(f'./data/{CURRENT_YEAR}-DCI-Caption-Score-Recaps-Large.csv', index=False)

else:
    print(f'No performances for {yesterday}')