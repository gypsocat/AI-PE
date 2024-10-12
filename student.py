class student_class(object):  # 定义一个名为student_class的类，继承自object类

    # 类变量，用于存储学生的个人信息
    name = ' '
    studentID = 0
    classNum = 0
    sex = 0
    term = 0
    sport1_message = []  # 存储学生的运动信息

    # 初始化方法，用于初始化学生对象的个人信息
    def __init__(self, name, studentID, classNum, sex, term):
        self.name = name
        self.studentID = studentID
        self.classNum = classNum
        self.sex = sex
        self.term = term

    # 添加运动信息的方法
    def append_message(self, new_message, sport_type=1):
        self.sport1_message.append(new_message)

    # 获取指定类型的运动信息数量
    def get_sport_message_num(self, sport_type=1):
        return len(self.sport1_message)

    # 获取指定类型的运动信息
    def get_sport_message(self, num, sport_type=1):
        a = self.get_sport_message_num()
        if num > a or num < 1:
            return False
        return True, self.sport1_message[num-1]

    # 清空运动信息
    def delete_sport_message(self, sport_type=1):
        self.sport1_message.clear()

    # 获取学生姓名
    def get_name(self):
        return self.name

    # 获取学生性别
    def get_sex(self):
        return self.sex

    # 获取学生班级
    def get_class(self):
        return self.classNum

    # 获取学生学号
    def get_studentid(self):
        return self.get_studentid()

    # 获取学生学期
    def get_term(self):
        return self.term

    # 打印学生信息和运动信息
    def print_info(self):
        print('name:' + self.name + ' ID:', self.studentID, ' sex:', self.sex, ' class:', self.classNum, ' term:', self.term)
        num = 0
        for i in self.sport1_message:
            num += 1
            print('第', num, '条:', i)

    # 复制学生对象
    def copy(self):
        stu_mid = student_class(self.name, self.studentID, self.classNum, self.sex, self.term)
        stu_mid.sport1_message = self.sport1_message.copy()
        return stu_mid
