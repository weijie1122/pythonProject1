from conf.config import sql
import pymysql
def connect_sql():
    host=sql['host']
    port=sql['port']
    user=sql['user']
    passwd=sql['passwd']
    db=sql['db']
    charset=sql['charset']
    conn = pymysql.connect(host=host, user=user, passwd=passwd, charset=charset, cursorclass=pymysql.cursors.DictCursor)
    conn.select_db(db)
    return conn
def select_conn(conn,sql):
    cur=conn.cursor()
    cur.execute(sql)
    result=cur.fetchall()
    cur.close()
    conn.commit()
    return result

cur=connect_sql()
sql1='select * from ad_rules where id=1'
a=select_conn(cur,sql1)
print(a)







