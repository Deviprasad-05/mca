import re
st = '1 6 567 the 92 date 54 is 04/01/2024'

data = re.findall('\d+',st)
print(data)