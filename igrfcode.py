from constant import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import scipy.special as scp
from pathlib import Path
import imageio
import os
import os.path

def readdata(filename):
    # 读取数据

    G = []
    n = []
    m = []
    data = np.zeros((195, 25))
    with open(filename) as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            lineData = line.strip().split()
            G.append(lineData[0])
            n.append(int(lineData[1]))
            m.append(int(lineData[2]))
            data[i,:] = lineData[3:]
            i = i + 1
    g = np.zeros(N1)
    for i in range(N1):
        g[i] = 0 if G[i] == 'g' else np.pi/2

    return g, n, m, data

def factorial(N):
    # 阶乘函数

    a = 1
    if N == 0:
        a == 1
    else:
        for i in range(1, N+1):
            a = a * i
    return a

def V(g, n, m, data):
    # 计算非偶极子场

    print('I have been run')
    ans = np.zeros(shapex)
    for i in range(N2):
        for j in range(N1):
            if n[j] == 1:
                # 去掉偶极子场
                continue
            e = 1 if m[j] == 0 else 2
            ans[:,:,i] = ans[:,:,i] - (-1)**(m[j])*(n[j]+1) * data[j,i]*np.cos(m[j]*Phi-g[j]) * \
                (e * factorial(n[j]-m[j]) / factorial(n[j]+m[j]))**0.5 * \
                    (scp.lpmv(m[j], n[j], np.cos(Theta)))
    
    ans.tofile('data.dat', sep = ' ', format = '%f')
    return ans
    

def drawpicture(path):
    # 画图

    plt.ion()
    # 读入生成的数据
    result = np.fromfile('data.dat', dtype = float, sep = ' ').reshape(shapex)
    # 画布大小
    fig = plt.figure(figsize=(10,7))
    ax1 = fig.add_axes([0.1,0.1,0.85,0.85])

    for index in range(N2):
        plt.cla()
        plt.title('IGRF--'+str(1900+index*5))
        # 绘制地图（世界地图）
        map = Basemap(ax = ax1)
        map.drawcoastlines()
        map.drawparallels(np.arange(-90,90,20),labels=[1,0,0,1])
        map.drawmeridians(np.arange(-180,180,30),labels=[1,0,0,1])
        # 绘制等值线
        X,Y = map(Phi, Theta)
        map.contour(X*t, 90 - Y*t, result[:,:,index], 15)

        # 将每年的非偶极子场的图保存
        plt.savefig(path+'IGRF--'+str(1900+index*5)+'.png')

        plt.pause(0.1)
    
    plt.ioff()
    plt.show()
    return


def creategif(path, gif_name):
    # 将png图片保存为gif动图

    frames = []
    
    pngFiles = os.listdir(path)
    image_list = [os.path.join(path, f) for f in pngFiles]
    for image_name in image_list:
        # 读取 png 图像文件
        frames.append(imageio.imread(image_name))
    # 保存为 gif 
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.3)

    return

def main():
    g, n, m, data = readdata('igrf12coeffs.txt')
    file = Path('data.dat')
    if not file.is_file():
        # 计算一次，避免重复计算
        V(g, n, m, data)

    path = 'D:/Learn/python/IGRF/pngfile'
    drawpicture(path)
    creategif(path, 'IGRF.gif')

main()

