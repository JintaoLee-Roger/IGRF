import numpy as np

a = 6371.2    # 地球半径
ntheta = 100
nphi = 200
N1 = 195
N2 = 25
t = 180 / np.pi

theta = np.linspace(0, np.pi, ntheta)
phi = np.linspace(-np.pi, np.pi, nphi)
[Phi, Theta] = np.meshgrid(phi, theta)
shapex = list(Phi.shape)
shapex.append(N2)

def factorial(N):
    # 阶乘函数

    a = 1
    if N == 0:
        a == 1
    else:
        for i in range(1, N+1):
            a = a * i
    return a
