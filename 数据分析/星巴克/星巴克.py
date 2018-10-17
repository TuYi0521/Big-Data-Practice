import pandas as pd

df = pd.read_csv("starbucks_store_worldwide.csv")
ch_data = df[df["Country"]=="CN"]
# print(ch_data)

# grouped = ch_data.groupby(by="State/Province").count()["Brand"]
# print(grouped,type(grouped))

grouped1 = ch_data.groupby(by=[df["Country"],df["State/Province"]]).count()[["Brand"]]
grouped2 = ch_data[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
grouped3 = ch_data.groupby(by=[df["Country"],df["State/Province"]])[["Brand"]].count()
print(grouped1,type(grouped1))
print(grouped2,type(grouped2))
print(grouped3,type(grouped3))

