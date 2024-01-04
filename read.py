import re
with open("C:\\Users\\administrator.MCA\\Desktop\\content.txt.txt",'r+') as file:
    data=file.read()
    data1=re.sub('a','@',data)
    file.write(data1)
