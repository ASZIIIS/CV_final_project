import cv2


def getFaceFrame(img_path):
    img = None
    vc = cv2.VideoCapture(img_path)
    # n = 1  # 计数
    if vc.isOpened():  # ToDo:这里先只写了读视频的第一帧
        rval, frame = vc.read()
        img = frame
    # else:
    #     rval = False
    # timeF = 10  # 视频帧计数间隔频率
    # i = 0
    # while rval:  # 循环读取视频帧
    #     rval, frame = vc.read()
    #     if (n % timeF == 0):  # 每隔timeF帧进行存储操作
    #         i += 1
    #         print(i)
    #         cv2.imwrite('images/{}.jpg'.format(i), frame)  # 存储为图像
    #     n = n + 1
    #     cv2.waitKey(1)
    vc.release()
    return img