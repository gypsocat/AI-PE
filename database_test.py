import os
import time
import student
import psycopg2

databaseLoading = 'loading_table'
databaseStudent = 'student_message'
databaseTeacher = 'teacher_message'
databaseSport1 = 'sport1'


def connect_database():  # 连接到数据库
    conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user='postgres',
        password='ztz991596',
        port='5432')

    cur = conn.cursor()
    return cur, conn


def get_time(cur):  # 获取数据库内当前时间戳
    cur.execute('SELECT TIMEOFDAY();')
    messages = cur.fetchall()
    return messages


def get_all_message(cur, dbname):
    cur.execute('SELECT * FROM ' + dbname)
    messages = cur.fetchall()
    return messages


def truncate_table(cur, dbname):
    cur.execute('truncate table '+dbname)


def find_message(id, code, cur):  # 检查输入的学号、工号和密码是否匹配
    string = 'select * from '+databaseLoading+' where StudentID='+str(id)+' and Code=\''+code+'\';'
    cur.execute(string)
    message = cur.fetchall()
    if not message:
        return False
    else:
        return True


def find_student_message(student_id, cur):  # 找到学生的存储地点
    string = 'select * from '+ databaseStudent + 'where studentID=' + str(student_id) + ';'
    cur.execute(string)


def insert_new_student(name, student_id, sex, class_number, term, pwd, cur):  # 插入新学生
    string1 = 'insert into ' + databaseLoading + ' VALUES(' + str(student_id) + ',\'' + str(pwd) + '\');'
    string2 = 'insert into ' + databaseStudent + ' VALUES(' + str(student_id) + ',\'' + name + '\',' + str(
        sex) + ',' + str(class_number) + ',' + str(term) + ');'
    cur.execute(string1+string2)


def insert_new_teacher(name, teacherid, class1, term1, class2, term2, class3, term3, pwd, cur):  # 插入新老师
    string1 = 'insert into ' + databaseLoading + ' VALUES(' + str(teacherid) + ',\'' + str(pwd) + '\');'
    string2 = 'insert into ' + databaseTeacher + ' VALUES(' + str(teacherid) + ',\'' + name + '\',' + str(class1) + \
              ',' + str(term1) + ',' + str(class2) + ',' + str(term2) + ',' + str(class3) + ',' + str(term3) + ');'
    cur.execute(string1+string2)


def insert_new_sport_message_in_sport1(studentid, standrednumber, error1, error2, sporttime, studentclass, grade, cur):
    # 插入运动信息
    totalNum = standrednumber + error1 + error2
    string1 = 'insert into ' + databaseSport1
    string2 = ' VALUES(' + str(studentid) + ',' + '(SELECT TIMEOFDAY()),' + str(totalNum) + ',' + str(standrednumber) + ',' + \
              str(error1) + ',' + str(error2) + ',' + str(sporttime) + ',' + str(studentclass) + ',' + str(grade) + ');'
    print(string1+string2)
    print(get_time(cur))
    cur.execute(string1+string2)


def delete_student(student_id, cur):  # 删除学生
    string1 = 'delete from ' + databaseLoading + ' where StudentID=' + str(student_id) + ';'
    string2 = 'delete from ' + databaseStudent + ' where studentID=' + str(student_id) + ';'
    string3 = 'delete from ' + databaseSport1 + ' where studentID=' + str(student_id) + ';'
    cur.execute(string1+string2+string3)


def delete_teacher(teacherid, cur):  # 删除老师
    string1 = 'delete from ' + databaseLoading + ' where StudentID=' + str(teacherid) + ';'
    string2 = 'delete from ' + databaseTeacher + ' where teacherID=' + str(teacherid) + ';'
    cur.execute(string1+string2)


def get_sport1_message_by_student(studentid, cur):  # 获取一个学生的所有运动记录，返回两个值：记录的条数，具体的记录（二维数组）
    string1 = 'select * from ' + databaseSport1 + ' where '
    string2 = 'studentID=' + str(studentid) + ';'
    string3 = 'select COUNT(*) from ' + databaseSport1 + ' where '
    print(string1 + string2)
    cur.execute(string1 + string2)
    messages = cur.fetchall()
    cur.execute(string3 + string2)
    count = cur.fetchall()
    return count[0][0], messages


def get_sport1_message_by_teacher(teacherid, cur, class_id):  # 获取老师带的一个班级的所有学生的所有运动记录
    string1 = ' '
    if class_id == 1:
        string1 += 'class1'
    elif class_id == 2:
        string1 += 'class2'
    elif class_id == 3:
        string1 += 'class3'
    else:
        string1 += 'class1'
    string0 = 'select' + string1 + ' from ' + databaseTeacher + ' where teacherID=' + str(teacherid) + ';'
    cur.execute(string0)
    messages = cur.fetchall()  # messages[0][0]是班级名称
    string1 = 'select studentid from ' + databaseStudent + ' where class=' + str(messages[0][0]) + ';'
    cur.execute(string1)
    messages1 = cur.fetchall()  # 学生的学号
    stu_arr = []
    for i in messages1:
        student_string = 'select * from ' + databaseStudent + ' where studentid=' + str(i[0]) + ';'
        cur.execute(student_string)
        messages_of_student = cur.fetchall()
        stu = student.student_class(messages_of_student[0][1], messages_of_student[0][0],   # stu是学生类
                                    messages_of_student[0][3], messages_of_student[0][2], messages_of_student[0][4])
        string_circle = 'select sportnumber, standrednumber, errornumber1, errornumber2, sporttime, grade from '\
                        + databaseSport1 + ' where studentid=' + str(i[0]) + ';'
        cur.execute(string_circle)
        messages_of_sport = cur.fetchall()
        for j in messages_of_sport:
            stu.append_message(j)
        stu.get_sport_message(0)
        stu1 = stu.copy()
        stu_arr.append(stu1)
        stu.delete_sport_message()
        print(messages_of_sport)
    return stu_arr


if __name__ == '__main__':
    cur, conn = connect_database()
    truncate_table(cur, databaseStudent)
    truncate_table(cur, databaseLoading)
    truncate_table(cur, databaseTeacher)
    truncate_table(cur, databaseSport1)
    timenow = get_time(cur)
    print(timenow)
    print(timenow[0][0])
    message = get_all_message(cur, databaseLoading)
    print(message)
    insert_new_student('王基荣', 1602008, 0, 1602, 4, 'wjr', cur)
    a = find_message(1602008, 'wjr', cur)
    print(a)
    insert_new_student('吴卓峻', 1601020, 0, 1601, 4, '123456a', cur)
    insert_new_student('胡翔越', 1601008, 0, 1601, 4, 'hxy', cur)
    insert_new_teacher('曾勇', 888, 1601, 1, 1602, 1, 1603, 1, '654321', cur)
    insert_new_teacher('高中喜', 889, 1604, 1, 1605, 1, 1606, 1, 'aaaaa', cur)
    insert_new_sport_message_in_sport1(1601020, 20, 5, 5, 30, 1601, 100, cur)
    time.sleep(5)
    insert_new_sport_message_in_sport1(1602008, 25, 5, 10, 30, 1602, 100, cur)
    time.sleep(5)
    insert_new_sport_message_in_sport1(1601020, 50, 2, 3, 60, 1601, 100, cur)
    time.sleep(5)
    insert_new_sport_message_in_sport1(1602008, 30, 10, 10, 30, 1602, 100, cur)
    time.sleep(5)
    insert_new_sport_message_in_sport1(1601008, 32, 5, 5, 40, 1601, 100, cur)
    count,a = get_sport1_message_by_student(1601020, cur)
    stu_arr = get_sport1_message_by_teacher(888, cur, 1)
    for i in stu_arr:
        i.speak()
    c = get_all_message(cur, databaseLoading)
    b = get_all_message(cur, databaseStudent)
    t = get_all_message(cur, databaseTeacher)
    d = get_all_message(cur, databaseSport1)

    print('loading message:')
    print(b)
    print('student message:')
    print(c)
    print('teacher message:')
    print(t)
    print('sport message')
    print(d)
    print('count of message:', count)
    print('some sport message')
    print(a)

    delete_student(1601020, cur)
    delete_teacher(888, cur)
    print('message after delete:')
    c = get_all_message(cur, databaseLoading)
    b = get_all_message(cur, databaseStudent)
    d = get_all_message(cur, databaseTeacher)
    a = get_all_message(cur, databaseSport1)
    print(b)
    print(c)
    print(d)
    print(a)

    truncate_table(cur, databaseStudent)
    truncate_table(cur, databaseLoading)
    truncate_table(cur, databaseTeacher)
    truncate_table(cur, databaseSport1)

    conn.commit()
    cur.close()
    conn.close()
