from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
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
 '2023-08-04',
 '2023-08-05',
 '2023-08-06',
 '2023-08-07',
 '2023-08-08',
 '2023-08-10',
 '2023-08-11',
 '2023-08-12'
]

corps_url = ['Blue%20Devils', 'Blue%20Knights', 'Blue%20Stars', 'Bluecoats', 'Boston%20Crusaders', 'Carolina%20Crown',
             'Colts', 'Crossmen', 'Genesis', 'Jersey%20Surf', 'Madison%20Scouts', 'Mandarins', 'Music%20City',
             'Pacific%20Crest', 'Phantom%20Regiment', 'Santa%20Clara%20Vanguard',
             'Seattle%20Cascades', 'Spirit%20of%20Atlanta', 'The%20Academy', 'The%20Cadets', 'The%20Cavaliers',
             'Troopers']
#corps = [w.replace('%20', ' ') for w in corps_url]

if yesterday in performance_dates:

    df = pd.DataFrame()
    for corps in corps_url:
        
        newdf = pd.DataFrame()
        for i in range(CURRENT_YEAR, CURRENT_YEAR+1):
            url = 'https://www.dci.org/scores/corps-summary?season='+str(i)+'&corp='+corps

            uClient = uReq(url) # opening up connection, grabbing the page
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, "html.parser")

            table = page_soup.find_all("table")

            try:
                score_table = pd.read_html(str(table))[3]
                newdf = pd.concat([newdf, score_table])
            except:
                continue
            newdf['Corps'] = corps
        df = pd.concat([df, newdf])

    cols = ['Date', 'Location', 'Rank', 'Score', 'Corps']
    df.columns = cols

    df = df.query("Rank != '--'")
    df = df[df.Date != 'Not Scored']
    df = df.dropna()

    df.Score = pd.to_numeric(df.Score)

    df.Date = pd.to_datetime(df.Date)

    df.Corps = df.Corps.str.replace('%20', ' ')

    df = df.sort_values(['Date', 'Location', 'Score'], ascending = [True, True, False])
    df = df.reset_index(drop = True)

    df.to_csv(f'./data/{CURRENT_YEAR}-World-Class-DCI-scores.csv', index=False)
else:
    print(f'No performances for {yesterday}')