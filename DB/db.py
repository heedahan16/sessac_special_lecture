import pymysql

db = pymysql.connect(host='101.101.210.141', port=3306, user='study', password='study!@#$%', db='hdh7736', charset='utf8')

# 커서 생성
cursor = db.cursor()

## create문
# sql ="""
#     CREATE TABLE hdh (
#         name varchar(20) NOT NULL,
#         math INT NULL,
#         science INT NULL,
#         english INT NULL,
#         PRIMARY KEY (name)
#     )
# """

## insert문
# sql ="""
#     INSERT INTO hdh (name, math, science, english)
#         VALUES('한다희', 60, 40, 80)
# """
# cursor.execute(sql)
# db.commit()

# # update문
# sql = """
#     UPDATE hdh
#         SET math = 80,
#             science = 60,
#             english = 70
#         WHERE name = '한다희'
# """

# SELECT문
sql = """
    SELECT *
        FROM hdh
"""

# cusror 실행
cursor.execute(sql)

# fetch
rs = cursor.fetchall()
print(rs)

# # 커밋
# db.commit()

# cusror 종료
cursor.close()

# DB 종료
db.close()

