from collections import OrderedDict

dict = {"name":"zs","age":"18","city":"深圳"}
print(dict)

pk=sorted(dict.items(),key=lambda i:i[0])
print(pk)
dict2 = OrderedDict(pk)
print(dict2)