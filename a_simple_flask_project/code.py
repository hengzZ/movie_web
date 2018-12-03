# coding:utf8
import os
import numpy as np
import cv2
import random
import uuid


class Code:
    # 随机一个字母或者数字
    def random_chr(self):
        num = random.randint(1, 3)
        if num == 1:
            # 随机一个数字
            char = random.randint(48, 57)
        elif num == 2:
            # 随机一个大写字母
            char = random.randint(97, 122)
        else:
            # 随机一个小写字母
            char = random.randint(65, 90)
        return chr(char)

    # 随机一个干扰字符
    def random_dis(self):
        arr = ["^", "_", "-", ".", "~", "%"]
        idx = random.randint(0, len(arr) - 1)
        return arr[idx]

    # 定义干扰字符颜色
    def random_dis_color(self):
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    # 定义字符颜色
    def random_chr_color(self):
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

    # 生成验证码
    def create_code(self):
        width = 240  # 240px
        height = 60  # 60px
        # 创建一个画布
        img = np.zeros((height, width, 3), np.uint8)
        color = (192, 192, 192)
        img[:, :, 0] = color[0]  # B
        img[:, :, 1] = color[1]  # G
        img[:, :, 2] = color[2]  # R
        # 创建font对象，定义字体大小
        font_name = random.randint(0, 5)
        font_size = random.randint(10, 20) / 10.0
        # 创建像素点
        for x in range(0, width, 5):
            for y in range(0, height, 5):
                cv2.circle(img, (x, y), 1, self.random_dis_color(), -1)
        # 填充干扰字符
        for v in range(0, width, 30):
            dis_char = self.random_dis()
            xloc = 5 + v
            # 字符底部所在位置范围
            yloc = random.randint(height - 15, height)
            cv2.putText(img, dis_char, (xloc, yloc), font_name, font_size, self.random_dis_color(), 2)
        # 填充字符
        chars = ""
        for v in range(4):
            c = self.random_chr()
            chars += str(c)
            # 字符底部所在范围
            yloc = random.randint(height - 15, height)
            xloc = int(v * (width / 4)) + random.randint(0, 30)
            cv2.putText(img, c, (xloc, yloc), font_name, font_size, self.random_chr_color(), 2)
        # 图片保存
        image_name = "%s.jpg" % uuid.uuid4().hex
        save_dir = os.path.join(os.path.dirname(__file__), "static/code")
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        cv2.imwrite(save_dir + "/" + image_name, img)
        return dict(
            img_name=image_name,
            code=chars
        )


if __name__ == "__main__":
    code = Code()
    print(code.create_code())
