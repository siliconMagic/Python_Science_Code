# coding:utf-8

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm


def get_image():
    img = plt.imread(r'./images/lena.jpg')
    print(img.shape)
    print(img.dtype)
    # 反转图像的θ轴,使图像反转
    # plt.imshow(img[::-1])
    # plt.imshow(img, origin = "lower")


    # plt.imshow(img * 1.0)
    # plt.imshow(img / 255.0)
    # 使图像变亮
    # plt.imshow(np.clip(img/200.0, 0, 1))
    '''
    plt.imshow(img[:,:,0])
    plt.colorbar()
    plt.show()
    '''
    plt.imshow(img, cmap = cm.copper)
    plt.show()


if __name__ == "__main__":
    get_image()