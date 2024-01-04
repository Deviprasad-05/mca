import csv
with open('mca.csv','w',newline='') as csvfile:
    data=csv.writer(csvfile)
    data.writerow(['id','name','mobile','email'])
    data2=[
          [1,'raju',9040990099,'raju12@gmail.com'],
         [2,'ram',9809897986,'ramu456@gmail.com'],
         [3,'raj',890989098,'raj45@gmail.com']
    ]
    data.writerows(data2)