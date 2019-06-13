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