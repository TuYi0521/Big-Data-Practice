from collections import Counter
import os

list = [1,666,666,77,77,77]
res = Counter(list)
print(res,type(res))
print(os.linesep,res[77],os.linesep,res[66],os.linesep,res[1])