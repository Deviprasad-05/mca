import re
st = '9067579308'

data = re.findall('\+91-6789[0-9]\d{10}',st)
print(data)