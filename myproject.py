import os,cv2,subprocess,time,psycopg2,json,uuid
from reportlab.pdfgen import canvas
import numpy as np
# import mediapipe as mp
import matplotlib.pyplot as plt
from flask import Flask,render_template,request,jsonify,redirect,flash,Response,send_file
from werkzeug.utils import secure_filename
from bodycatch import main_circulate, make_conclusion,suggestion
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from psycopg2 import pool, sql
from psycopg2 import OperationalError
import logging
from test import *
import codecs
import markdown
import pdfkit



# # 需要的全局变量
# mp_pose = mp.solutions.pose
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# pose = mp_pose.Pose(
#             min_detection_confidence=0.5,
#             min_tracking_confidence=0.5,
#             model_complexity=1)
# """
# mp_pose：MediaPipe姿势估计解决方案的实例。
# mp_drawing：用于在图像上绘制姿势关键点的模块。
# mp_drawing_styles：用于定义绘制样式的模块
# pose:模型
# """
# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

time_start = [0]
ss_pointer = [-1]  # 移进规约队列指针
sportNum = np.zeros(5)  # 标准动作个数（只有第一个有效）
sportErrorNum = np.zeros(5)  # 错误动作个数（前两个分别表示前两种错误）
sportState = np.zeros(5)  # 移进规约队列
sportType = [1]

colorclass = plt.cm.ScalarMappable(cmap='jet')
colors = colorclass.to_rgba(np.linspace(0, 1, int(33)))
colormap = (colors[:, 0:3])
file_name1 = "sport_angle.txt"
file_name2 = "sport_error_angle.txt"
file_name3 = "error_kind.txt"
file_name4 = "sport_conclusion.txt"
angleArrayBuffer = []

user_id=None


#================================================================================================
app = Flask(__name__)

# 路径配置
PROMPT_FILE = "./prompt_t.txt"
DATA_FILE = "./user_input.txt"
OUTPUT_FILE = "./tmp_text/chatbox.txt"
INTERACTION_SCRIPT = "./chatbox.py"

# 创建数据库连接池
# connection_pool = psycopg2.pool.SimpleConnectionPool(
#     1,  # 最小连接数
#     10,  # 最大连接数
#     host="localhost",
#     database="project_test",
#     user='postgres',
#     password='xj041012',
#     port='5432'
# )
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123123@localhost/project_test'
#app.config['SQLALCHEMY_POOL_SIZE'] = 20
#db.init_app(app)

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

# 使用连接池
connection_pool = create_connection_pool()

@app.route('/')
def display():
    return render_template('display.html')

@app.route('/', methods=['POST'])
def login():
    # 这个是登录界面
    data = request.get_json()  # 获取JSON数据
    id_number = data.get('ID')  # 获取'id'字段的值
    password = data.get('password')  # 获取'password'字段的值
    identity = data.get('identity')
    print(id_number,password,identity)

    # 从连接池获取一个数据库连接
    conn = get_connection_from_pool()
    # 使用连接创建一个游标对象
    cur = conn.cursor()

    try:
        # 数据库操作
        result = find_message(id_number, password, identity, cur)
        print("check_message success!!!!")
        print("result:", result)

        # 假设find_message函数返回True表示验证成功，False表示验证失败
        if result:
            return jsonify({"result": True})  # 返回验证成功的JSON响应
        else:
            # 验证失败，显示错误信息
            return jsonify({"result": False})  # 返回错误信息的JSON响应

    except Exception as e:
        print("An error occurred:", e)
        # 发生错误时回滚事务
        conn.rollback()
        return jsonify({"error": "An error occurred. Please try again later."})  # 返回通用错误信息的JSON响应
    finally:
        # 关闭游标对象，释放相关资源
        cur.close()
        # 将连接放回连接池
        put_connection_to_pool(conn)

    #return result
#===============================================登录数据库交互====================================
@app.route('/database')
# 使用连接池进行数据库操作
def database_operation():
    # 从连接池获取一个数据库连接
    conn = get_connection_from_pool()
    # 使用连接创建一个游标对象
    cur = conn.cursor()
        
    try:
       #===========================
       #数据库操作
       #==========================
        #insert_new_student('小明', 1601020, 0, 1601, 4, '123456a', cur)
        #insert_new_student('小强', 1601008, 0, 1601, 4, 'hxy', cur)
        #insert_new_teacher('小勇', 888, 1601, 1, 1602, 1, 1603, 1, '654321', cur)
        #insert_new_teacher('小喜', 889, 1604, 1, 1605, 1, 1606, 1, 'aaaaa', cur)
        # 提交事务
        conn.commit()
    except Exception as e:
        print("An error occurred:", e)
        # 发生错误时回滚事务
        conn.rollback()
    finally:
        # 关闭游标对象，释放相关资源
        cur.close()
        # 将连接放回连接池
        put_connection_to_pool(conn)
    
    # 返回查询结果
    return "good"
#===============================================登录数据库交互=====================================
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'response': '未接收到有效的消息。'}), 400

    try:
        # 1. 写入用户消息到 sport_conclusion.txt
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            f.write(user_input)

        # 2. 确保 tmp_text 目录存在
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

        # 3. 执行 interaction.py
        result = subprocess.run(['python', INTERACTION_SCRIPT], capture_output=True, text=True, timeout=60)

        if result.returncode != 0:
            print(f"interaction.py 错误输出: {result.stderr}")
            return jsonify({'response': '对不起，出现了错误，请稍后再试。11111111111111111111111'}), 500

        # 4. 等待 interaction.py 完成并读取输出
        # 这里简单等待1秒，确保文件写入完成
        time.sleep(1)

        if not os.path.exists(OUTPUT_FILE):
            print("未找到 AI 响应文件。")
            return jsonify({'response': '对不起，未能获取到AI的响应，请稍后再试。'}), 500

        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            ai_response = f.read().strip()

        if not ai_response:
            ai_response = '对不起，未能获取到AI的响应，请稍后再试。'

        return jsonify({'response': ai_response})

    except subprocess.TimeoutExpired:
        print("interaction.py 执行超时。")
        return jsonify({'response': 'interaction.py 执行超时'}), 500
    except Exception as e:
        print(f"处理请求时发生异常: {e}")
        return jsonify({'response':'处理请求时发生异常: {e}'}), 500

@app.route('/admin_assign_message')
def admin_assign_message():
    return render_template('admin_assign_message.html')

@app.route('/admin_class_table')
def admin_class_table():
    return render_template('admin_class_table.html')

@app.route('/admin_msg_overview')
def admin_msg_overwiew():
    return render_template('admin_msg_overview.html')

@app.route('/admin_message_edit')
def admin_message_edit():
    return render_template('admin_message_edit.html')

@app.route('/admin_user_table')
def admin_user_table():
    return render_template('admin_user_table.html')

@app.route('/admin_edit_user')
def admin_edit_user():
    return render_template('admin_edit_user.html')


@app.route('/admin_add_user')
def admin_add_user():
    return render_template('admin_add_user.html')


@app.route('/student_edit_info')
def student_edit_info():
    return render_template('student_edit_info.html')

@app.route('/student_feedback')
def student_feedback():
    return render_template('student_feedback.html')

@app.route('/student_message_source')
def student_message_source():
    return render_template('student_message_source.html')

@app.route('/message_detail')
def message_detail():
    return render_template('message_detail.html')

@app.route('/student_profile_mobile')
def student_profile_mobile():
    return render_template('student_profile_mobile.html')

@app.route('/student_profile_show')
def student_profile_show():
    return render_template('student_profile_show.html')

@app.route('/student_search_result')
def student_search_result():
    return render_template('student_search_result.html')

@app.route('/student_sport_mobile')
def student_sport_mobile():
    return render_template('student_sport_mobile.html')

@app.route('/student_task_detail')
def student_task_detail():
    return render_template('student_task_detail.html')

@app.route('/student_video_web')
def student_video_web():
    return render_template('student_video_web.html')

@app.route('/student_video_mobile')
def student_video_mobile():
    return render_template('student_video_mobile.html')

@app.route('/student_video_mobile_fullscreen')
def student_video_mobile_fullscreen():
    return render_template('student_video_mobile_fullscreen.html')

@app.route('/student_task_overview')
def student_task_overview():
    return render_template('student_task_overview.html')

@app.route('/teacher_assign_task')
def teacher_assign_task():
    return render_template('teacher_assign_task.html')

@app.route('/teacher_class_profile')
def teacher_class_porfile():
    return render_template('teacher_class_profile.html')

@app.route('/teacher_class_profile_02006')
def teacher_class_profile_02006():
    return render_template('teacher_class_profile_02006.html')
@app.route('/teacher_class_profile_09007')
def teacher_class_profile_09007():
    return render_template('teacher_class_profile_09007.html')
@app.route('/teacher_class_profile_09016')
def teacher_class_profile_09016():
    return render_template('teacher_class_profile_09016.html')


@app.route('/teacher_evaluate_task_detail')
def teacher_evaluate_task_detail():
    return render_template('teacher_evaluate_task_detail.html')

@app.route('/teacher_evaluate_task_overview')
def teacher_evaluate_task_overview():
    return render_template('teacher_evaluate_task_overview.html')

@app.route('/teacher_profile')
def teacher_profile():
    return render_template('teacher_profile.html')

@app.route('/teacher_chat')
def teachr_chat():
    return render_template('teacher_chat.html')

@app.route('/teacher_visualization')
def teacher_visualization():
    return render_template('teacher_visualization.html')
#===============================================个人信息界面-填写数据=====================================
@app.route('/profile')
def profile():
    print("run html")
    return render_template('profile.html')

@app.route('/profile', methods=['POST'])
def receive_data():
    print("receive")
    # 检查请求是否包含 JSON 数据
    if request.is_json:
        data = request.get_json()
        # 检查是否包含 'name' 和 'ID' 键
        if 'name' in data and 'ID' in data:
            name = data.get('name')
            # 进行后续操作
            print(name)
            ID = data.get('ID')
            print(ID)
            return jsonify({'message': 'Data received successfully'})
        else:
            return jsonify({'error': 'Missing required fields'}), 400
    else:
        return jsonify({'error': 'Request must be in JSON format'}), 400
#================================================个人信息界面-填写数据=====================================
@app.route('/sport')
def sport():
    return render_template('sport.html')

@app.route('/video')
def video():
    return render_template('video.html')
#===============================================保存运动视频==============================================
@app.route('/run_learn1', methods=['GET'])
def run_learn1():
    try:
        f1 = open(file_name1, 'w')
        f2 = open(file_name2, 'w')
        f3 = open(file_name3, 'w')
        f4 = open(file_name4, 'w')
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        time_start[0] = time.time()
        return 'bodycatch.py executed successfully'
    except Exception as e:
        return str(e), 500
    
    
@app.route('/get_suggestion', methods=['GET'])
def get_suggestion():
    global suggestion, sportNum
    # 只传递 sportNum 的第一个数据
    sportNum_value = int(sportNum[0]) if isinstance(sportNum, np.ndarray) else sportNum
    # 将 suggestion 转换为普通列表
    suggestion_list = list(suggestion)
    return jsonify({"sportNum": sportNum_value, "suggestion": suggestion_list})



@app.route('/reset_data', methods=['POST'])
def reset_data():
    print("1111111111111111111111111111111111111")
    global suggestion, sportNum
    suggestion = ['无']
    sportNum = np.zeros(5)
    return jsonify({"message": "Data reset successfully"})


@app.route('/upload_video1', methods=['POST'])
def upload_video1():
    # 检查请求中是否包含文件
    if 'video' not in request.files:
        return jsonify({'error': '未找到文件'})

    video_file = request.files['video']
    
    # 检查文件名是否为空
    if video_file.filename == '':
        return jsonify({'error': '未选择文件'})

    # 生成另一个唯一的文件名
    recognition_filename = 'recognition.mp4'
    
    # 将视频文件保存到服务器上的 recognition 文件夹中
    video_file.save(os.path.join('./recognition', recognition_filename))

    return jsonify({'message': '视频上传成功'})

@app.route('/upload_video2', methods=['POST'])
def upload_video2():
    # 检查请求中是否包含文件
    if 'video' not in request.files:
        return jsonify({'error': '未找到文件'})

    video_file = request.files['video']
    
    # 检查文件名是否为空
    if video_file.filename == '':
        return jsonify({'error': '未选择文件'})

    # 生成唯一的文件名
    unique_filename = str(uuid.uuid4()) + '.mp4'
    
    # 将视频文件保存到服务器上的 vedio 文件夹中
    video_file.save(os.path.join('./video', unique_filename))

    return jsonify({'message': '视频上传成功'})

#================================================保存运动视频=========================================
 

#================================================实时上传视频=========================================
@app.route('/realtime_upload', methods=['POST'])
def realtime_upload():
    # 从POST请求中获取图像数据
    image_data = request.data
    # 将图像数据解码为像素数据
    pixel_data = np.frombuffer(image_data, dtype=np.uint8)

    # 重塑像素数据为图像形状
    width, height = 640, 480  # 假设图像大小为640x480
    if 'width' in request.args and 'height' in request.args:
        width = int(request.args['width'])
        height = int(request.args['height'])
        
    pixel_data = pixel_data.reshape((height, width, 4))  # 4通道(RGBA)

    # 创建一个空的图像，将像素数据写入其中
    image = cv2.cvtColor(pixel_data, cv2.COLOR_RGBA2BGRA)
    # 保存图像文件到指定路径
    save_path = './video_image'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    cv2.imwrite(os.path.join(save_path, 'received_image.png'), image)  # 保存图像文件
    fig = plt.figure()
    image1, ss_pointer1 = main_circulate(image, sportType, sportNum, sportState, sportErrorNum, ss_pointer, width, height)
    # image1是处理后的图片，ss_pointer1是当前的移进规约栈指针
    return 'Image received and saved successfully'  
#================================================实时上传视频========================================   


#================================================显示运动评价======================================== 
@app.route('/run_interaction',methods=['GET'])
def run_interaction():
    print('11111111111111111111111111111111111111111111111')
    try:
        # 使用 subprocess 启动一个 Python 子进程，并运行 interaction.py
        result = subprocess.run(['python', 'interaction.py'], capture_output=True, text=True)
        print(result.stdout)  # 打印子进程的标准输出
        print('interaction executed successfully')
        return 'interaction executed successfully'
    except Exception as e:
        print('Exception'+str(e))
        return str(e), 500


@app.route('/run_conclusion',methods=['GET'])
def run_conlusion():
    print("into run_conclusion！！！！！！！！！")
    total1 = sportNum[0] + sportErrorNum[0] + sportErrorNum[1]
   # data = request.get_json()
    #print("get json")
   # time = data.get('time')
   # print(type(time))
   # 处理 variable_value，可以将其存储到数据库中或进行其他操作
    time0 = time.time() - time_start[0]
    make_conclusion(1, 18, sportType[0], total1, sportNum, sportErrorNum, time0, file_name4)
    return jsonify({'message': 'time received successfully'})



@app.route('/get_file_content')
def get_file_content():
    #time.sleep(5)  # 延迟5秒
    file_path = './tmp_text/suggestion.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

@app.route('/get_file_content_comment')
def get_file_content_comment():
    #time.sleep(3)  # 延迟3秒
    file_path = './tmp_text/test.txt'
    with open(file_path, 'r') as file:
        content = file.read()
    return content


@app.route( '/reset_file_content')
def reset_file_content():
   # file_path = './tmp_text/test.txt'
   # with open(file_path, 'w') as file:
   #     file.write("加载中......")
    return 'File content reset to "加载中......"'




# 生成PDF文件
def generate_pdf(file_path, md_content):
    c = canvas.Canvas(file_path)
    c.drawString(100, 750, md_content)  # 在页面上写入Markdown内容11
    c.save()

@app.route('/generate_pdf')
def generate_pdf_route():
    # 读取 Markdown 文件
    file_path = './tmp_text/学生个人体育运动报告.md'
    with codecs.open(file_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # 将 Markdown 转换为 HTML
    html_content = markdown.markdown(md_content)

    # 将 HTML 写入临时文件
    with codecs.open("temp.html", "w", encoding="utf-8") as f:
        f.write('<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>')
        f.write(html_content)

    # 将 HTML 转换为 PDF
    pdfkit.from_file("temp.html", "temp.pdf")

    # 发送 PDF 文件给客户端
    return send_file("temp.pdf", as_attachment=True)



#================================================显示运动评价======================================== 
'''
@app.route('/login')
def login():
    return render_template('login.html')
'''

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html')

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/student_data')
def student_data():
    return render_template('student_data.html')
        
        
#目前for record in decoded_records可以打印，但是不能将数据渲染到html网页上
@app.route('/student', methods=['POST'])
def get_sport_record():
    print("start get_sport_record")
    data = request.get_json()  # 获取JSON数据
    user_id = int(data.get('user_id'))  # 获取'id'字段的值并转换为整数类型
    user_id = 1601020
    print('user_id:',user_id)
    return student(user_id)


@app.route('/get_details',methods=['POST'])
def get_details():
    print("start get_detail")
    data = request.get_json()
    print("data:",data)
    detail = data['data']['detail']
    sport_type = data['data']['sport_type']
    time = data['data']['time']
    
    
    conn = get_connection_from_pool()
    # 使用连接创建一个游标对象
    cur = conn.cursor()
    result_json = json.dumps(get_sport_details(sport_type, detail, time, cur))
    return result_json


@app.route('/personal')
def personal():
    return render_template('personal.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
#    app.run(host='0.0.0.0')
   app.run(host='0.0.0.0', port=8080)
    
