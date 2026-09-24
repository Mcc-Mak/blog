"""News sentiment scoring for stock headlines using VADER."""
import os
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen, Request  # open URL and send HTTP requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import ssl
nltk.download('vader_lexicon')
# --- ssl workaround (allow unverified https context) ---
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
class sentiments():
    def __init__(self):
        pass
    def get_news(self, tokens=["TSLA"]):
        # fetch news of each stock, e.g. finviz
        news_tables = {}
        for token in tokens:
            url = 'https://finviz.com/quote.ashx?t={}'.format(token)  # use stock website to get news of stock
            req = Request(url=url, headers={"User-Agent": "Chrome"})  # depends on the browser on the computer
            response = urlopen(req)
            html = BeautifulSoup(response, "html.parser")
            news_table = html.find(id="news-table")
            # data = []
            # date = ""
            # news_title = ""
            news_list = []
            for x, j in enumerate(news_table.findAll('tr')):  # j => html element with <tr> tag, x => element index
                text = j.a.get_text()
                date_scrape = j.td.text.split()
                if len(date_scrape) == 1:
                    time = date_scrape[0]
                else:
                    date = date_scrape[0]
                    time = date_scrape[1]
                news_list.append([token, date, time, text])
                """date = j.td.text
                news_title = j.a.text
                print(date+news_title)
                print("\n")
                data.append([date,news_title])
                """
            news_tables[token] = news_list
        return news_tables
    def get_sentiment_score(self, tokens=['TSLA']):
        # the sentiment score is between -1 to 1 (more negative to more positive)
        # input => tokens, output => df with sentiment score for news
        df_set = []
        try:
            vader = SentimentIntensityAnalyzer()
            columns = ['ticker', 'date', 'time', 'headline']
            for token in tokens:
                news_list = self.get_news([token])[token]
                news_df = pd.DataFrame(news_list, columns=columns)
                scores = news_df['headline'].apply(vader.polarity_scores).tolist()  # convert DataFrame to list
                scores_df = pd.DataFrame(scores)
                news_df = news_df.join(scores_df, rsuffix='_right')
                news_df['date'] = pd.to_datetime(news_df.date).dt.date
                df_set.append(news_df)
            return df_set
        except:
            return df_set
if __name__ == "__main__":
    s = sentiments()
    # news = s.get_news()
    sentiments = s.get_sentiment_score()  # input: [token1_code, token2_code ...]
    # print(news)
    print(sentiments[0])
# Reference: https://nickmccullum.com/stock-market-sentiment-analysis-python/