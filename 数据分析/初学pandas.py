import pandas as pd
import string

index=list() #指定索引
res = pd.Series([1,2,31,12,3,4])    # res = pd.Series([1,2,31,12,3,4],index=list("abcdef"))
res2 = res.where(res>10)
print(res,res2)
# print(res.dtype)
# t4=res.astype(float)
# print(t4)
# t5=t4.astype(int)
# print(t5)

# 字典创建Series
# dict={"name":"zs","age":"18","city":"深圳"}
# t1 = pd.Series(dict)
# print(t1,t1.dtype)
#
# print(t1[0],t1[1],t1[2])                   # 根据索引取和根据键取一样
# print(t1["age"],t1["city"],t1["name"])
# print(t1[:2])                              # 取连续的前2行
# print(2222222222,t1[[0,2]])                # 取不连续的2行
# print(t1[["name","city"]])
# print(t1.index,type(t1.index),len(t1.index))
# for i in t1.index:
#     print(i)
# print(t1.values,type(t1.values),len(t1.values))
# for j in t1.values:
#     print(j)


# # 使用字典推式创建字典
# a = {string.ascii_uppercase[i]:i for i in range(10)}
# print(a)
# t2=pd.Series(a)
# print(t2.dtype)


# # 如果修改了索引，则
# t3 = pd.Series(a,index=list(string.ascii_uppercase[5:15]))
# print(t3,t3.dtype)

