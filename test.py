import psycopg2
from psycopg2 import pool, sql
from psycopg2 import OperationalError
import logging
from myproject import connection_pool

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

databaseLoading = 'loading_table'
databaseStudent = 'student_message'
databaseTeacher = 'teacher_message'
databaseSport1 = 'sport1'


def create_connection_pool():
    try:
        # 尝试连接到目标数据库
        connection_pool = psycopg2.pool.SimpleConnectionPool(
            1, 10,
            host="localhost",
            database="project_test",
            user='postgres',
            password='xj041012',
            port='5432'
        )
        logger.info("成功连接到 'project_test' 数据库。")
        return connection_pool
    except OperationalError as e:
        logger.warning(f"无法连接到 'project_test' 数据库：{e}")
        try:
            # 连接到默认的 'postgres' 数据库
            default_pool = psycopg2.pool.SimpleConnectionPool(
                1, 10,
                host="localhost",
                database="postgres",
                user='postgres',
                password='xj041012',
                port='5432'
            )
            conn = default_pool.getconn()
            conn.autocommit = True
            with conn.cursor() as cur:
                # 检查目标数据库是否存在
                cur.execute("SELECT 1 FROM pg_database WHERE datname=%s", ("project_test",))
                exists = cur.fetchone()
                if not exists:
                    # 创建目标数据库
                    cur.execute(sql.SQL("CREATE DATABASE {}").format(
                        sql.Identifier("project_test")
                    ))
                    logger.info("已创建 'project_test' 数据库。")
                else:
                    logger.info("'project_test' 数据库已存在。")
            default_pool.putconn(conn)
            default_pool.closeall()

            # 重新尝试连接到目标数据库
            connection_pool = psycopg2.pool.SimpleConnectionPool(
                1, 10,
                host="localhost",
                database="project_test",
                user='postgres',
                password='xj041012',
                port='5432'
            )
            logger.info("成功连接到 'project_test' 数据库。")
            return connection_pool
        except Exception as e2:
            logger.error(f"创建或连接 'project_test' 数据库失败：{e2}")
            # 返回一个模拟的连接池，避免后续代码报错
            return MockConnectionPool()

# 定义模拟的连接池和连接
class MockConnectionPool:
    def __init__(self):
        logger.warning("使用模拟的连接池。所有数据库操作将被忽略。")

    def getconn(self):
        return MockConnection()

    def putconn(self, conn):
        pass

    def closeall(self):
        pass

class MockConnection:
    def cursor(self):
        return self

    def execute(self, query, params=None):
        logger.debug(f"Mock execute: {query} | params: {params}")

    def fetchone(self):
        return None

    def fetchall(self):
        return []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# 添加新的数据库操作函数到模拟连接池中
def get_connection_from_pool():
    return connection_pool.getconn()

def put_connection_to_pool(conn):
    connection_pool.putconn(conn)

def get_time(cur):
    cur.execute('SELECT TIMEOFDAY();')
    messages = cur.fetchall()
    return messages

def get_all_message(cur, dbname):
    cur.execute(f'SELECT * FROM {dbname}')
    return cur.fetchall()

def truncate_table(cur, dbname):
    cur.execute(f'TRUNCATE TABLE {dbname}')

def find_message(id, code, identity, cur):
    string = f"SELECT * FROM {databaseLoading} WHERE id={id} AND Code='{code}' AND user_identity='{identity}';"
    cur.execute(string)
    return cur.fetchall()

def get_sport_records_by_student(student_id, cur):
    string1 = f"SELECT * FROM sport_records WHERE detail = {student_id};"
    string2 = f"SELECT COUNT(*) FROM sport_records WHERE detail = {student_id};"
    cur.execute(string1)
    messages = cur.fetchall()
    cur.execute(string2)
    count = cur.fetchall()
    return count[0][0], messages

def find_student_message(student_id, cur):
    string = f'SELECT * FROM {databaseStudent} WHERE studentID={student_id};'
    cur.execute(string)

def insert_new_student(name, student_id, sex, class_number, term, pwd, cur):
    string1 = f"INSERT INTO {databaseLoading} VALUES({student_id},'{pwd}','student');"
    string2 = f"INSERT INTO {databaseStudent} VALUES({student_id},'{name}',{sex},{class_number},{term});"
    try:
        cur.execute(string1 + string2)
    except psycopg2.errors.UniqueViolation as e:
        print("UniqueViolation occurred:", e)
        raise e

def insert_new_teacher(name, teacher_id, class1, term1, class2, term2, class3, term3, pwd, cur):
    string1 = f"INSERT INTO {databaseLoading} VALUES({teacher_id},'{pwd}','teacher');"
    string2 = f"INSERT INTO {databaseTeacher} VALUES({teacher_id},'{name}',{class1},{term1},{class2},{term2},{class3},{term3});"
    try:
        cur.execute(string1)
        cur.execute(string2)
    except psycopg2.errors.UniqueViolation as e:
        print("UniqueViolation occurred:", e)
        raise e

def insert_new_sport_message_in_sport1(studentid, standrednumber, error1, error2, sporttime, studentclass, grade, cur):
    totalNum = standrednumber + error1 + error2
    string1 = f'INSERT INTO {databaseSport1}'
    string2 = f' VALUES({studentid}, (SELECT TIMEOFDAY()), {totalNum}, {standrednumber}, {error1}, {error2}, {sporttime}, {studentclass}, {grade});'
    try:
        cur.execute(string1 + string2)
    except psycopg2.errors.UniqueViolation as e:
        print("UniqueViolation occurred:", e)
        raise e

def delete_student(student_id, cur):
    string1 = f'DELETE FROM {databaseLoading} WHERE id={student_id};'
    string2 = f'DELETE FROM {databaseStudent} WHERE studentID={student_id};'
    string3 = f'DELETE FROM {databaseSport1} WHERE studentID={student_id};'
    cur.execute(string1 + string2 + string3)

def delete_teacher(teacherid, cur):
    string1 = f'DELETE FROM {databaseLoading} WHERE id={teacherid};'
    string2 = f'DELETE FROM {databaseTeacher} WHERE teacherID={teacherid};'
    cur.execute(string1 + string2)

def get_sport1_message_by_student(studentid, cur):
    string1 = f'SELECT * FROM {databaseSport1} WHERE studentID={studentid};'
    string2 = f'SELECT COUNT(*) FROM {databaseSport1} WHERE studentID={studentid};'
    cur.execute(string1)
    messages = cur.fetchall()
    cur.execute(string2)
    count = cur.fetchall()
    return count[0][0], messages

def get_sport1_message_by_teacher(teacherid, cur, class_id):
    class_str = ['class1', 'class2', 'class3'][class_id - 1]
    string0 = f'SELECT {class_str} FROM {databaseTeacher} WHERE teacherID={teacherid};'
    cur.execute(string0)
    messages = cur.fetchall()
    string1 = f'SELECT studentid FROM {databaseStudent} WHERE class={messages[0][0]};'
    cur.execute(string1)
    student_ids = cur.fetchall()
    return student_ids

def update_student_info(student_id, name, sex, class_number, term, pwd, cur):
    string = f"UPDATE {databaseStudent} SET name='{name}', sex={sex}, class={class_number}, term={term}, pwd='{pwd}' WHERE studentID={student_id};"
    cur.execute(string)

def update_teacher_info(teacher_id, name, class1, term1, class2, term2, class3, term3, pwd, cur):
    string = f"UPDATE {databaseTeacher} SET name='{name}', class1={class1}, term1={term1}, class2={class2}, term2={term2}, class3={class3}, term3={term3}, pwd='{pwd}' WHERE teacherID={teacher_id};"
    cur.execute(string)

def get_sport_details(sport_type, detail, time, cur):
    string = f"""
        SELECT t.table_name, s.studentid, s.time
        FROM information_schema.tables t 
        JOIN {sport_type} s ON t.table_name = '{sport_type}' 
        WHERE s.studentid = {detail} AND s.time = '{time}';
    """
    cur.execute(string)
    rows = cur.fetchall()
    return [{"table_name": row[0], "studentid": row[1], "time": row[2]} for row in rows]
