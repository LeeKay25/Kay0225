import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root',
password='125125',
charset='utf8',db='iot01')
cursor = conn.cursor()

def register():
    user = input('input your username:')
    password = input('input your password:')
    sql = "insert into user(username,password) values(%s,%s)"
    values =(user,password)
    cursor.execute(sql,values)
    conn.commit()
    cursor.close()
    conn.close()
    print(f'sucess,user:{user}')
def login():
    print('user login')
    user = input('input username:')
    password = input('input password:')
    sql = "select * from user where username = %s and password = %s"
    values = (user,password)
    cursor.execute(sql,values)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
       print('login sucess',result)
    else:
       print('failed')

def run():
    choice = input('*'*30+'\n'+'please input 1 or 2')
    if choice == '1':
        register()
    elif choice == '2':
        login()
    else:
        prijt('wrong input')

if __name__=='__main__':
    run()

