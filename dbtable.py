import pymysql
con=pymysql.connect(user='root',password='root',port=3306,database='pythonmysql')
cursor=con.cursor()
def create_table():
   try:
    query='''
    create table customer(
    id int primary key,
    name varchar(100),
    mobile bigint unique,
    balance bigint
    );
    '''
    cursor.execute(query)
   except pymysql.err.OperationalError as e:
      print(f'{e}')
def insert_record():
  query= '''insert into customer(id,name,mobile,balance)
  values(1,'raju',9090909090,5000)'''
  cursor.execute(query)
  con.commit()

def get_records():
  query='select*from customer'
  cursor.execute(query)
  records = cursor.fetchall()
  for i in records:
    print(i)
 
def insert_dynamic(cid,name,mobile,bal):
  record=(cid,name,mobile,bal)
  query="insert into customer(id,name,mobile,balance) values(%s,%s,%s,%s)"
  cursor.execute(query,record)
  con.commit()

def drop_record(cid):
  query= f'delete from customer where id={cid}'
  cursor.execute(query)
  con.commit()
  print('record removed')

def update_record(name):
  query=f'update from customer where name={name}'
  con.commit(query)
  print('record update')
  
    
  
  