# Time    : 11/27/2018 9:07 PM
# Author  : virualv
import pymysql
conn = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'joy',passwd = 'hzy122925',db = 'sqltest',charset = 'utf8')
cursor = conn.cursor()
# inp = input('inp >>>')
# raw = cursor.execute('insert into teacher (tname) value (%s)',inp)
# conn.commit()

# raw = cursor.execute('insert into score (student_id,course_id,num) value (%s,%s,%s)',(14,2,65))
# conn.commit()

# ls = (
#     ('男',1,'康健'),
#     ('女',2,'梁军'),
#     ('男',2,'凯云')
# )
# raw = cursor.executemany('insert into student (gender,class_id,sname)value (%s,%s,%s)',ls)  # 注意本次使用的是executemany(),而不是execute()
# conn.commit()

# raw = cursor.execute('SELECT score.student_id AS stu_id,\
#                         student.sname AS stu_name,\
#                         course.cname AS course,\
#                         score.num AS num\
#                         from score LEFT JOIN student ON student.sid=score.student_id\
#                          LEFT JOIN course ON course.cid = score.course_id')
# print('row:',raw)
# row1 = cursor.fetchone()  # 拿到的是一条数据本身
# row2 = cursor.fetchmany(2)
# row3 = cursor.fetchall()  # 拿到的是多条数据，一个元组（如果是一条数据，则在这条数据外面套一个括号）
# print(row1)
# print(row2)
# # print(row3)
# for i in row3:
#     # for t in i:
#     #     print(t)
#     print('%s %s %s %s'%i)
#     # print('\n')


# raw = cursor.execute('SELECT score.student_id AS stu_id,\
#                         student.sname AS stu_name,\
#                         course.cname AS course,\
#                         score.num AS num\
#                         from score LEFT JOIN student ON student.sid=score.student_id\
#                          LEFT JOIN course ON course.cid = score.course_id')
# print('row:',raw)
# print(cursor.fetchone())
# print(cursor.fetchone())
# # cursor.scroll(0,'absolute')       # 绝对位置（类似于相对路径）
# cursor.scroll(-1,'relative')        # 相对当前位置（类似于相对路径）
# print(cursor.fetchone())


#### FBI Warning
sql = "select * from student where sname = '%s' and sid = '%s'"
sql = sql % ('张二" or 1=1 -- ',56)
cursor.execute(sql)
print(cursor.fetchone())
cursor.close()
conn.close()