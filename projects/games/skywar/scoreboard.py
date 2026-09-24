#Add data of each game into data file in csv format



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
    default_first_row = ["Name","Score","Health","Time","Exp","Level","Distance","Map"]
    def __init__(self,data_LIST): #Write data into database
        self.data = data_LIST
        return self.update_data()

    def update_data(self): #Update data with algo e.g sorting,sum to re-rank all the data
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
            #time.sleep(1)

    def read(self,key) -> str:   #str key => str element
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
            #df = None  # pd.read_csv(f)

        if not df.empty:
            try:
                #return df.iloc[-1][key]
                return df.iloc[-1][key]
            except:
                return ""
        else:
            #print("Data is not updated.Please recall again to update.")
            return ""
    def readlines(self,number): #number of data   # int=> DF/NONE
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
            #df = None  # pd.read_csv(f)

        if not df.empty :
            #try:
            length = df.shape[0] #(24,7)
            print(length)
            if length>abs(number):
                length = number
            else:
                pass
            if number>=0:
                return df.iloc[0:length:]
            else:
                return df.iloc[df.shape[0]-1:df.shape[0]-4:-1]

            # except:
            #     return None
        else:
            # print("Data is not updated.Please recall again to update.")
            return df

    def read_key(self,key):   #str => None/DF
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
            #df = None  # pd.read_csv(f)
        return df
        # if df is not None:
        #     try:
        #         df = df[df["Name"]==key]
        #         print(df)
        #         if df.empty:
        #             return None
        #         else:
        #             return df
        #     except:
        #         return None
        # else:
        #     return None


    def write(self,values) -> None: #Write data into database again      LIST => None
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
                return df
            except:
                return ""
        else:
            # print("Data is not updated.Please recall again to update.")
            return ""



if __name__ == "__main__":
    #TEST ZONE
    # score = 10
    # username  = "Benny"
    # info = [username,score,23,41,4,1421,"dkaow","dwadwa","benny"]
    SCORE_SYSTEM = score_system([])
    # print(SCORE_SYSTEM.read("Name"))
    # SCORE_SYSTEM.write(["Mary",20])
    # print(SCORE_SYSTEM.readlines(-1))
    # print(SCORE_SYSTEM.read_key("Mary"))
    # print(SCORE_SYSTEM.read_key("Mary").iloc[-1]["Score"])
    # print(time.asctime(time.localtime(time.time())))

    # init_time = time.time()
    # while True:
    #     T = (time.time()-init_time)
    #     print(T)
    DATA = SCORE_SYSTEM.read_database()
    print(SCORE_SYSTEM.read_database()[DATA["Score"]==DATA["Score"].max()])
    print(SCORE_SYSTEM.read_database()[DATA["Score"]==DATA["Score"].max()]["Name"]) #1st
    print(SCORE_SYSTEM.read_database().nlargest(3,"Score"))
    # for i in SCORE_SYSTEM.read_database().nlargest(3,"Score")["Name"]:
    #     print(i)
    print(SCORE_SYSTEM.read_database().nlargest(3,"Score")[["Name","Score"]].values)
    for j in SCORE_SYSTEM.read_database().nlargest(3,"Score")[["Name","Score"]].values:
        print(j[0])
        print(j[1])