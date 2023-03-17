oldi = ["1", "2", "3"]
newi = [] 
for item in oldi:
    newi.append(int(item))	
print(newi)
mixt = ["ab", "ac", "ad", "ab", "ab", "ac", "a"]
ft = list(filter(lambda x: x == "ab", mixt))
print(ft)	
a = list(filter(lambda x:x%2, [1,2,3,4,5,6,7,8]))
print(a)	
a = [-1,0,1,0,0,1,0,-1]
b = list(filter(None, a)) 
print(b)
from functools import reduce
def func(prev, curr):
    return prev + 2 * curr
a = reduce(func, [1, 2, 3, 4, 5]) 
print(a)
