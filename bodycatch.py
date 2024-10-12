import re
import cv2
import matplotlib.pyplot as plt
import json
# import time
import numpy as np
import os
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

colorclass = plt.cm.ScalarMappable(cmap='jet')
colors = colorclass.to_rgba(np.linspace(0, 1, int(33)))
colormap = (colors[:, 0:3])
file_name1 = "sport_angle.txt"
file_name2 = "sport_error_angle.txt"
file_name3 = "error_kind.txt"
angleArrayBuffer = []
angle_print = [0, 0]
suggestion = []

def append_the_file(f_n):
    print(angleArrayBuffer)
    with open(f_n, 'a') as file_mid:
        file_mid.writelines(angleArrayBuffer)
        file_mid.write('\n')
        angleArrayBuffer.clear()
        file_mid.close()


def append_error_file(error_kind):
    with open(file_name3, 'a') as file_mid:
        file_mid.writelines(str(error_kind))
        file_mid.write(' ')
        file_mid.close()


def count_push_up(angle_array, sport_num, sport_state, sport_error_num, pointer):  # 俯卧撑
    p1 = 0
    p2 = 1
    if pointer[0] < 5:
        if np.array_equal(sport_state, [1, 2, 3, 2, 1]) or np.array_equal(sport_state, [1, 3, 1, 0, 0]) \
                or np.array_equal(sport_state, [1, 2, 3, 1, 0]) or np.array_equal(sport_state, [1, 3, 2, 1, 0]):
            sport_state *= 0
            print(sport_state)
            pointer[0] = -1
            sport_num[0] += 1

            append_the_file(file_name1)

        elif np.array_equal(sport_state, [1, 2, 1, 0, 0]):
            sport_state *= 0
            pointer[0] = -1
            sport_error_num[0] += 1
            
            append_the_file(file_name2)
            append_error_file(1)

        elif np.array_equal(sport_state, [1, 2, 3, 2, 3]) or np.array_equal(sport_state, [1,3,2,3,0]):
            sport_state *= 0
            pointer[0] = -1
            sport_num[0] += 1
            sport_error_num[1] += 1

            append_the_file(file_name2)
            append_error_file(2)

    else:
        sport_state *= 0
        pointer[0] = -1
        angleArrayBuffer.clear()

    if angle_array:
        angle_print = [angle_array[p1], angle_array[p2]]
        if angle_array[p1] < 80 or angle_array[p2] < 80:  # 3
            if pointer[0] == -1 or pointer[0] == 4:
                return pointer
            if sport_state[pointer[0]] != 3:
                pointer += 1
                sport_state[pointer[0]] = 3
        elif angle_array[p1] > 140 or angle_array[p2] > 140:  # 1
            if pointer[0] == 4:
                return pointer
            if pointer[0] == -1 or sport_state[pointer[0]] != 1:
                pointer[0] += 1
                sport_state[pointer[0]] = 1
        else:  # 2
            if pointer[0] == -1 or pointer[0] == 4:
                return pointer
            if sport_state[pointer[0]] != 2:
                pointer[0] += 1
                sport_state[pointer[0]] = 2
        angleArrayBuffer.append(str(int(angle_array[p1]))+' '+str(int(angle_array[p2]))+'\n')
    return pointer


def count_sit_up(angle_array, sport_num, sport_state, sport_error_num, pointer):  # 仰卧起坐
    p1 = 4
    p2 = 5
    if pointer[0] < 5:
        if np.array_equal(sport_state, [1, 2, 3, 2, 1]) or np.array_equal(sport_state, [1, 3, 1, 0, 0]) \
                or np.array_equal(sport_state, [1, 2, 3, 1, 0]) or np.array_equal(sport_state, [1, 3, 2, 1, 0]):
            sport_state *= 0
            print(sport_state)
            pointer[0] = -1
            sport_num[0] += 1

            append_the_file(file_name1)

        elif np.array_equal(sport_state, [1, 2, 1, 0, 0]):
            sport_state *= 0
            pointer[0] = -1
            sport_error_num[0] += 1

            append_the_file(file_name2)
            append_error_file(1)

        elif np.array_equal(sport_state, [1, 2, 3, 2, 3]) or np.array_equal(sport_state, [1,3,2,3,0]):
            sport_state *= 0
            pointer[0] = -1
            sport_num[0] += 1
            sport_error_num[1] += 1

            append_the_file(file_name2)
            append_error_file(2)

    else:
        sport_state *= 0
        pointer[0] = -1
        angleArrayBuffer.clear()

    if angle_array:
        angle_print = [angle_array[p1], angle_array[p2]]
        if angle_array[p1] < 40 or angle_array[p2] < 40:  # 3
            if pointer[0] == -1 or pointer[0] == 4:
                return pointer
            if sport_state[pointer[0]] != 3:
                pointer[0] += 1
                sport_state[pointer[0]] = 3
        elif angle_array[p1] > 70 or angle_array[p2] > 70:  # 1
            if pointer[0] == 4:
                return pointer
            if pointer[0] == -1 or sport_state[pointer[0]] != 1:
                pointer[0] += 1
                sport_state[pointer[0]] = 1
        else:                                           # 2
            if pointer[0] == -1 or pointer[0] == 4:
                return pointer
            if sport_state[pointer[0]] != 2:
                pointer[0] += 1
                sport_state[pointer[0]] = 2
        angleArrayBuffer.append(str(int(angle_array[p1])) + ' ' + str(int(angle_array[p2])) + '\n')
    return pointer


def count_up_down(angle_array, sport_num, sport_state, sport_error_num, pointer):  #引体向上
    print(sport_state)
    p1 = 0
    p2 = 1
    if pointer[0] < 5:
        if np.array_equal(sport_state, [1, 2, 3, 2, 1]) or np.array_equal(sport_state, [1, 3, 1, 0, 0]) \
                or np.array_equal(sport_state, [1, 2, 3, 1, 0]) or np.array_equal(sport_state, [1, 3, 2, 1, 0]):
            sport_state *= 0
            print('add'+str(sport_num[0]))
            pointer[0] = -1
            sport_num[0] += 1
            suggestion.clear()
            append_the_file(file_name1)
            suggestion.append("无")
        
        elif np.array_equal(sport_state, [1, 2, 1, 0, 0]):
            sport_state *= 0
            pointer[0] = -1
            sport_error_num[0] += 1
            suggestion.append("引起时头颈未超越杠杆杠面")
            append_the_file(file_name2)
            append_error_file(1)
        
        elif np.array_equal(sport_state, [1, 2, 3, 2, 3]) or np.array_equal(sport_state, [1,3,2,3,0]):
            sport_state *= 0
            pointer[0] = -1
            sport_num[0] += 1
            sport_error_num[1] += 1
            suggestion.append("手肘角度过小，还原时请呈直臂悬垂姿势")
            append_the_file(file_name2)
            append_error_file(2)

    else:
        sport_state *= 0
        pointer[0] = -1
        angleArrayBuffer.clear()
        suggestion.append("无")

    if angle_array:
        angle_print = [angle_array[p1], angle_array[p2]]
        if angle_array[p1] < 75 or angle_array[p2] < 75:  # 3
            if pointer[0] == -1 or pointer[0] == 4:
                return pointer
            if sport_state[pointer[0]] != 3:
                pointer[0] += 1
                sport_state[pointer[0]] = 3
        elif angle_array[p1] > 100 or angle_array[p2] > 100:  # 1
            if pointer[0] == 4:
                return pointer
            if pointer[0] == -1 or sport_state[pointer[0]] != 1:
                pointer[0] += 1
                sport_state[pointer[0]] = 1
        else:  # 2
            if pointer[0] == -1 or pointer[0] == 4:
                return pointer
            if sport_state[pointer[0]] != 2:
                pointer[0] += 1
                sport_state[pointer[0]] = 2
        angleArrayBuffer.append(str(int(angle_array[p1])) + ' ' + str(int(angle_array[p2])) + '\n')
    return pointer


def calculate_angle(a, b, c):  # 计算角度
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


# def draw3d(plt, ax, world_landmarks, connnection=mp_pose.POSE_CONNECTIONS):
#     ax.clear()
#     ax.set_xlim3d(-1, 1)
#     ax.set_ylim3d(-1, 1)
#     ax.set_zlim3d(-1, 1)
#
#     landmarks = []
#     for index, landmark in enumerate(world_landmarks.landmark):
#         landmarks.append([landmark.x, landmark.z, landmark.y * (-1)])
#     landmarks = np.array(landmarks)
#
#     ax.scatter(landmarks[:, 0], landmarks[:, 1], landmarks[:, 2], c=np.array(colormap), s=50)
#     for _c in connnection:
#         ax.plot([landmarks[_c[0], 0], landmarks[_c[1], 0]],
#                 [landmarks[_c[0], 1], landmarks[_c[1], 1]],
#                 [landmarks[_c[0], 2], landmarks[_c[1], 2]], 'k')
#     plt.pause(0.001)
#     # plt.savefig('image.png')


def main_circulate(image, sport_type, sport_num, sport_state, sport_error_num, ss_pointer, width, height):
    global ss_pointer1
    # # image.flags.writeable = False
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # results = pose.process(image)
    # # print(results)
    #
    # # Draw the pose annotation on the image.
    # image.flags.writeable = True
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # if if_draw_line == 1:
    #     mp_drawing.draw_landmarks(
    #         image,
    #         results.pose_landmarks,
    #         mp_pose.POSE_CONNECTIONS,  # 35个结点
    #         landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # """
    # results.pose_landmarks: MediaPipe返回的姿势关键点结果。它包含了检测到的人体姿势的关键点信息。
    # mp_pose.POSE_CONNECTIONS: 姿势关键点之间的连接。这是一个预定义的常量，表示要绘制的关键点连接。
    # """
    os.system('python ~/PaddleDetection/deploy/python/det_keypoint_unite_infer.py '
              '--det_model_dir=./PaddleDetection/output_inference/picodet_v2_s_320_pedestrian '
              '--keypoint_model_dir=./PaddleDetection/output_inference/tinypose_128x96 '
              '--image_file=./video_image/received_image.png '
              '--device=GPU '
              '--output_dir=./image_output '
              '--save_results=True')

    keypoint_names = [
        "Nose", "Left Eye", "Right Eye", "Left Ear", "Right Ear", "Left Shoulder",
        "Right Shoulder", "Left Elbow", "Right Elbow", "Left Wrist", "Right Wrist",
        "Left Hip", "Right Hip", "Left Knee", "Right Knee", "Left Ankle", "Right Ankle"
    ]

    # 读取JSON文件
    file_path = '/mnt/data/det_keypoint_unite_image_results.json'
    with open(file_path, 'r') as f:
        data = json.load(f)

    # 遍历数据，寻找第一个包含完整17个关键点的图片
    keypoints_dict = {}
    for entry in data:
        image_data = entry[2]
        for keypoints_data in image_data[0]:
            if len(keypoints_data) == 17:
                keypoints_dict = {keypoint_names[i]: (kp[0], kp[1]) for i, kp in enumerate(keypoints_data)}
                break

    angleArray = []
    try:
        # 根据读取的坐标进行赋值
        leye = [keypoints_dict["Left Eye"][0] * width, keypoints_dict["Left Eye"][1] * height]
        reye = [keypoints_dict["Right Eye"][0] * width, keypoints_dict["Right Eye"][1] * height]
        nose = [keypoints_dict["Nose"][0] * width, keypoints_dict["Nose"][1] * height]
        lshoulder = [keypoints_dict["Left Shoulder"][0] * width, keypoints_dict["Left Shoulder"][1] * height]
        rshoulder = [keypoints_dict["Right Shoulder"][0] * width, keypoints_dict["Right Shoulder"][1] * height]

        lshoulder = [keypoints_dict["Left Shoulder"][0] * width, keypoints_dict["Left Shoulder"][1] * height]
        lelbow = [keypoints_dict["Left Elbow"][0] * width, keypoints_dict["Left Elbow"][1] * height]
        lwrist = [keypoints_dict["Left Wrist"][0] * width, keypoints_dict["Left Wrist"][1] * height]
        lhip = [keypoints_dict["Left Hip"][0] * width, keypoints_dict["Left Hip"][1] * height]
        lankle = [keypoints_dict["Left Ankle"][0] * width, keypoints_dict["Left Ankle"][1] * height]
        lknee = [keypoints_dict["Left Knee"][0] * width, keypoints_dict["Left Knee"][1] * height]

        rshoulder = [keypoints_dict["Right Shoulder"][0] * width, keypoints_dict["Right Shoulder"][1] * height]
        relbow = [keypoints_dict["Right Elbow"][0] * width, keypoints_dict["Right Elbow"][1] * height]
        rwrist = [keypoints_dict["Right Wrist"][0] * width, keypoints_dict["Right Wrist"][1] * height]
        rhip = [keypoints_dict["Right Hip"][0] * width, keypoints_dict["Right Hip"][1] * height]
        rankle = [keypoints_dict["Right Ankle"][0] * width, keypoints_dict["Right Ankle"][1] * height]
        rknee = [keypoints_dict["Right Knee"][0] * width, keypoints_dict["Right Knee"][1] * height]

        langle = calculate_angle(lshoulder, lelbow, lwrist)  # 肩-肘-手
        rangle = calculate_angle(rshoulder, relbow, rwrist)
        lsangle = calculate_angle(lhip, lshoulder, lelbow)
        rsangle = calculate_angle(rhip, rshoulder, relbow)
        rhangle = calculate_angle(rshoulder, rhip, rknee)  # 肩-屁股-膝盖
        lhangle = calculate_angle(lshoulder, lhip, lknee)
        rkangle = calculate_angle(rankle, rknee, rhip)
        lkangle = calculate_angle(lankle, lknee, lhip)
        angleArray = [langle, rangle, lsangle, rsangle, rhangle, lhangle, rkangle, lkangle]
        #print(angleArray)
    except:
        pass
    # print(sport_type)
    if sport_type[0] == 0:
        ss_pointer1 = count_sit_up(angleArray, sport_num, sport_state, sport_error_num, ss_pointer)
    elif sport_type[0] == 1:
        ss_pointer1 = count_up_down(angleArray, sport_num, sport_state, sport_error_num, ss_pointer)
    elif sport_type[0] == 2:
        ss_pointer1 = count_push_up(angleArray, sport_num, sport_state, sport_error_num, ss_pointer)

    return image, ss_pointer1


def get_message_from_file(sport_type):  # 计算最大角度和最小角度
    dataNumOfLine = 0
    if sport_type == 0 or sport_type == 1 or sport_type == 2:
        dataNumOfLine = 2
    file = open(file_name1, 'r')
    numbers = []
    for line in file:
        if line == '\n':
            continue
        num = re.findall(r'\d+', line)
        numbers.extend(num)
    print(numbers)
    max_num = numbers[0]
    min_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    return max_num, min_num

# 性别 年龄 运动类型 运动个数 运动时间 正确个数 错误总数 1类错误 2类错误
def make_conclusion(sex, age, sport_type, total, sport_num, sport_error_num, time_of_sport, file_path):
    errorNum = sport_error_num[0]+sport_error_num[1]
    print(sex, age, sport_type, total, time_of_sport, sport_num[0], errorNum)
    string =( str(sex) + ' ' + str(age) + ' ' + str(sport_type) + ' ' + str(int(total)) + ' '
    + str(int(time_of_sport)) + ' ' +str(int(sport_num[0])) +  ' ' + str(int(errorNum)))
    string1 = ' '
    i = 0
    while i < sport_error_num[0] :
        i += 1
    string1 += i
    string1 += ' '
    i = 0
    while i < sport_error_num[1]:
        i += 1
    string1 += i
    string += string1
    f = open(file_path, 'w')
    f.writelines(string)
    f.close()
    print("generate conclusion")