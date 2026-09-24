"""Persistent SkyWar scoreboard stored in a CSV database (scoredata.csv).

Reads, ranks and appends player records, and creates the CSV with a header
row the first time it runs. Each method derives the CSV path from the main
script (argv[0]) so the file lands next to py_game_full.py.
"""

import pandas as pd
import csv
import os
import sys
import numpy as np
import time

# print(os.getcwd())
# print(sys.path)
#
# print(sys.argv)
# print(__file__)

class score_system:
    default_first_row = ["Name", "Score", "Health", "Time", "Exp", "Level", "Distance", "Map"]

    def __init__(self, data_LIST):
        """Load the existing database (creating it on first run)."""
        self.data = data_LIST
        return self.update_data()

    def update_data(self):
        """Make sure the CSV exists and has its header row."""
        file_path = sys.argv[0][::-1]
        for i in sys.argv[0][::-1]:
            if i == "/":
                break
            file_path = file_path.replace(i, "", 1)
        file_path = "".join(file_path[::-1])

        try:
            f = open(file_path + "scoredata.csv", encoding="utf-8")
            df = pd.read_csv(f)
        except:
            csv_file = open(file_path + "scoredata.csv", "a+")
            csv_reader = csv.reader(csv_file, delimiter=",")
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow(self.default_first_row)
            # csv_reader = csv.reader(csv_file,delimiter=",")
            csv_file.close()
            # time.sleep(1)

    def read(self, key) -> str:  # str key => str element
        """Return the value stored in the newest record of a column."""
        file_path = sys.argv[0][::-1]
        for i in sys.argv[0][::-1]:
            if i == "/":
                break
            file_path = file_path.replace(i, "", 1)
        file_path = "".join(file_path[::-1])

        try:
            f = open(file_path + "scoredata.csv", encoding="utf-8")
            df = pd.read_csv(f)
        except:
            csv_file = open(file_path + "scoredata.csv", "a+")
            csv_reader = csv.reader(csv_file, delimiter=",")
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow(self.default_first_row)
            # csv_reader = csv.reader(csv_file,delimiter=",")
            csv_file.close()
            time.sleep(1)
            csv_file = open(csv_file.name, csv_file.mode)
            f = csv_file
            # df = None  # pd.read_csv(f)

        if not df.empty:
            try:
                # return df.iloc[-1][key]
                return df.iloc[-1][key]
            except:
                return ""
        else:
            # print("Data is not updated.Please recall again to update.")
            return ""

    def readlines(self, number):  # number of rows to return => DataFrame
        """Return the first ``number`` rows, or the last few if negative."""
        file_path = sys.argv[0][::-1]
        for i in sys.argv[0][::-1]:
            if i == "/":
                break
            file_path = file_path.replace(i, "", 1)
        file_path = "".join(file_path[::-1])

        try:
            f = open(file_path + "scoredata.csv", encoding="utf-8")
            df = pd.read_csv(f)
        except:
            csv_file = open(file_path + "scoredata.csv", "a+")
            csv_reader = csv.reader(csv_file, delimiter=",")
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow(self.default_first_row)
            # csv_reader = csv.reader(csv_file,delimiter=",")
            csv_file.close()
            time.sleep(1)
            csv_file = open(csv_file.name, csv_file.mode)
            f = csv_file
            # df = None  # pd.read_csv(f)

        if not df.empty:
            length = df.shape[0]  # (rows, columns)
            print(length)
            if length > abs(number):
                length = number
            else:
                pass
            if number >= 0:
                return df.iloc[0:length:]
            else:
                return df.iloc[df.shape[0]-1:df.shape[0]-4:-1]
        else:
            # print("Data is not updated.Please recall again to update.")
            return df

    def read_key(self, key):  # str => DataFrame/None
        """Return the whole database so callers can filter by player name."""
        file_path = sys.argv[0][::-1]
        for i in sys.argv[0][::-1]:
            if i == "/":
                break
            file_path = file_path.replace(i, "", 1)
        file_path = "".join(file_path[::-1])

        try:
            f = open(file_path + "scoredata.csv", encoding="utf-8")
            df = pd.read_csv(f)
        except:
            csv_file = open(file_path + "scoredata.csv", "a+")
            csv_reader = csv.reader(csv_file, delimiter=",")
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow(self.default_first_row)
            # csv_reader = csv.reader(csv_file,delimiter=",")
            csv_file.close()
            time.sleep(1)
            csv_file = open(csv_file.name, csv_file.mode)
            f = csv_file
            # df = None  # pd.read_csv(f)
        return df

    def write(self, values) -> None:  # list => None
        """Append one new player record, column-aligned, to the CSV."""
        file_path = sys.argv[0][::-1]
        for i in sys.argv[0][::-1]:
            if i == "/":
                break
            file_path = file_path.replace(i, "", 1)
        file_path = "".join(file_path[::-1])

        try:
            f = open(file_path + "scoredata.csv", encoding="utf-8")
            df = pd.read_csv(f)
        except:
            csv_file = open(file_path + "scoredata.csv", "a+")
            csv_reader = csv.reader(csv_file, delimiter=",")
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow(self.default_first_row)
            # csv_reader = csv.reader(csv_file,delimiter=",")
            csv_file.close()
            time.sleep(1)
            csv_file = open(csv_file.name, csv_file.mode)
            f = csv_file
            df = None  # pd.read_csv(f)
        if df is not None:
            Data = values
            input_keys = [i for i in df.keys()]
            INPUT = {}
            for i in range(len(input_keys)):
                # Pad missing trailing columns with NaN instead of shifting
                if i > len(Data) - 1:
                    INPUT.update({input_keys[i]: [np.nan]})
                else:
                    INPUT.update({input_keys[i]: [Data[i]]})
            new_df = pd.DataFrame(INPUT)
            # new_df = pd.concat([df,new_df],axis=0)
            new_df = df.append(new_df)
            new_df.to_csv(file_path + 'scoredata.csv', index=False)
        else:
            print("Data is not updated.Please recall again to update.")

    def read_database(self) -> pd.DataFrame:  # str key => str element
        """Return the whole scoreboard database as a DataFrame."""
        file_path = sys.argv[0][::-1]
        for i in sys.argv[0][::-1]:
            if i == "/":
                break
            file_path = file_path.replace(i, "", 1)
        file_path = "".join(file_path[::-1])

        try:
            f = open(file_path + "scoredata.csv", encoding="utf-8")
            df = pd.read_csv(f)
        except:
            csv_file = open(file_path + "scoredata.csv", "a+")
            csv_reader = csv.reader(csv_file, delimiter=",")
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow(self.default_first_row)
            # csv_reader = csv.reader(csv_file,delimiter=",")
            csv_file.close()
            time.sleep(1)
            csv_file = open(csv_file.name, csv_file.mode)
            f = csv_file
            # df = None  # pd.read_csv(f)

        if not df.empty:
            return df
        else:
            # print("Data is not updated.Please recall again to update.")
            return ""


if __name__ == "__main__":
    # --- Test zone ---
    SCORE_SYSTEM = score_system([])
    DATA = SCORE_SYSTEM.read_database()
    print(SCORE_SYSTEM.read_database()[DATA["Score"]==DATA["Score"].max()])
    print(SCORE_SYSTEM.read_database()[DATA["Score"]==DATA["Score"].max()]["Name"])  # 1st
    print(SCORE_SYSTEM.read_database().nlargest(3, "Score"))
    print(SCORE_SYSTEM.read_database().nlargest(3, "Score")[["Name", "Score"]].values)
    for j in SCORE_SYSTEM.read_database().nlargest(3, "Score")[["Name", "Score"]].values:
        print(j[0])
        print(j[1])