import pymysql
"""
1、创建数据库的链接
2、建立游标
3、设计查询语句
4、提交相关语句
5、关闭游标
6、关闭数据库链接
"""
connect = pymysql.connect(
    host="192.168.100.16",
    user="kkb_vlc_test",
    password="AwcbA8tGIqmAOw5w",
    db="kkb_vlc_live_operation_test",
    charset="utf8"
)

cur = connect.cursor()
cur.execute(" select * from drama_live ")
connect.commit()
for i in range(100):
    res = cur.fetchone()
    print(res)
cur.close()
connect.close()

