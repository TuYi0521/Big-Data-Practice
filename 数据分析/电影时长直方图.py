from matplotlib import pyplot as plt
import pandas

df = pandas.read_csv("./IMDB-Movie-Data.csv")
print(df)
data_time = df["Runtime (Minutes)"].values
print(data_time,type(data_time))

plt.figure(figsize=(20,8),dpi=80)
max = max(data_time)
min = min(data_time)
print(min,max,max-min)
num_bin = (max-min)//5

plt.hist(data_time,num_bin)

plt.xticks(range(min,max+5,5))
plt.show()

