import pymysql


def get_conn():
    # 获取数据库连接
    conn = pymysql.connect('localhost', 'root', 'root', 'appium')
    return conn


def select():
    # 获取数据库连接
    conn = get_conn()

    # 创建游标对象
    cursor = conn.cursor()

    # 执行sql查询
    cursor.execute('SELECT * FROM student WHERE id=1')

    # 获取单条数据
    data = cursor.fetchone()
    print(data)

    # 获取所有记录
    cursor.execute('SELECT * FROM student')
    rows = cursor.fetchall()
    print(rows)
    for row in rows:
        id = row[0]
        name = row[1]
        age = row[2]
        print('id={} name={} age={}'.format(id, name, age))

    # 关闭数据库连接
    conn.close()


def insert():
    # 获取数据库连接
    conn = get_conn()

    try:
        # 创建游标对象
        cursor = conn.cursor()

        # 执行sql
        sql = 'insert into student(name,age) values("python", 10)'
        cursor.execute(sql)

        # 提交事务
        conn.commit()
    except:
        # 回滚事务
        conn.rollback()
    finally:
        # 关闭数据库连接
        conn.close()


def update():
    # 获取数据库连接
    conn = get_conn()

    try:
        # 创建游标对象
        cursor = conn.cursor()

        # 执行sql
        sql = 'update student set age=100 where id=1'
        cursor.execute(sql)

        # 提交事务
        conn.commit()
    except:
        # 回滚事务
        conn.rollback()
    finally:
        # 关闭数据库连接
        conn.close()


def delete():
    # 获取数据库连接
    conn = get_conn()

    try:
        # 创建游标对象
        cursor = conn.cursor()

        # 执行sql
        sql = 'delete from student where id=4'
        cursor.execute(sql)

        # 提交事务
        conn.commit()
    except:
        # 回滚事务
        conn.rollback()
    finally:
        # 关闭数据库连接
        conn.close()


# select()
# insert()
# update()
delete()
