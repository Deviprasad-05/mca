b=([1,2,3,8],(1,2),{4,5,6},{2:2,3:3},'efgh')
a=[i for i in b if len(i)>2]
print(list(a))