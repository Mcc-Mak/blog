"""Google Trends keyword search utility for stock sentiment."""
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import pytrends
# --- Google Trends client ---
class Trends:
    def __init__(self, hl="en-HK", tz=360):
        self.trends = TrendReq(hl=hl, tz=tz)  # 360 => Area code in US , 1=> Hong Kong timezone
    # def get_start_date(self,kw,date='today 24-m'):
    #     if isinstance(kw,str):
    #         self.trends.build_payload([kw],cat=0,timeframe=date)
    #     elif isinstance(kw,list):
    #         self.trends.build_payload(kw,cat=0,timeframe=date)
    #     data = self.trends.interest_over_time()
    #     data = data.reset_index()
    #     #print(data["date"])
    #     #return data["date"][0]
    # --- search interest over time for a keyword or a list ---
    def search(self, kw="NNDM", date='today 12-m', plot=False):  # date format: 'today 12-m' or '2020-04-01 2020-05-01'
        if isinstance(kw, str):
            self.trends.build_payload([kw], cat=0, timeframe=date)
        elif isinstance(kw, list):
            self.trends.build_payload(kw, cat=0, timeframe=date)
        data = self.trends.interest_over_time()
        data = data.reset_index()
        #data = self.trends.get_historical_interest([kw], year_start=2021, month_start=1, day_start=1, hour_start=0, year_end=2021, month_end=11, day_end=24, hour_end=0, cat=0, sleep=0)
        #Hourly data
        #print(data)
        if plot == True:
            # plot the trend for the first keyword
            #ax = plt.gca() #return the axis of current figure
            mdates = data["date"]
            # formatter = mdates.DateFormatter("%Y-%m-%d")
            # ax.xaxis.set_major_formatter(formatter)
            # locator = mdates.DayLocator()
            # ax.xaxis.set_major_locator(locator)
            plt.grid()
            if isinstance(kw, str):
                plt.plot(mdates, data[kw])
                plt.title("\"{}\" keyword trend".format(kw))
            elif isinstance(kw, list):
                plt.plot(mdates, data[kw[0]])
                plt.title("\"{}\" keyword trend".format(kw[0]))
            plt.show()
        return data
# --- demo run ---
if __name__ == "__main__":
    trend = Trends()
    #trend.search("TSLA stock",plot=True) #Only support one args search
    #trend.search("NNDM")
    sugs = trend.trends.suggestions("FB stcok")
    # print suggestions
    if len(sugs) >= 1:
        print(sugs[0]["title"])
        trend.search(sugs[0]["title"], plot=True)