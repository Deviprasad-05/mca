import csv
# with open('mca.csv','w',newline='') as csvfile:
#    data=csv.writer(csvfile)
#    data.writerow(['id','name','mobile','email'])
#    data2=[
#          [1,'raju',9040990099,'raju12@gmail.com'],
#         [2,'ram',9809897986,'ramu456@gmail.com'],
#         [3,'raj',890989098,'raj45@gmail.com']
#    ]
#    data.writerows(data2)

# with open('mca.csv','r') as csvfile:
#     data = csv.reader(csvfile)
#     for i in data:
#         print(i)

# with=open('mca1.csv','w',newline='')as csvfile:
#     fieldnames = ['id','name','mobile','email']
#     data=csv.DictWriter(csvfile,fieldnames)
#     data.writeheader()
#     rows=[
#         {'id':1,'name':'licky','mobile':9080909080,'email':'licky123@gmail.com'},
#         {'name':'devi','id':2,'email':'devi23@gmail.com','mobile':8909087654},
#     ] 
#     data.writerows(rows)

with open('mca1.csv','r')as csvfile:
    data=csv.DictReader(csvfile)
    for row in data:
        print(row['name'])