file = open('mca.txt','av ')
data =[
    'murali\n',
    'chandra\n',
    'damodhar\n',
    'hasya\n'
]
file.writelines(data)
file.close()

file = open('mca.txt','r')
data = file.read()
print(data)
file.close()