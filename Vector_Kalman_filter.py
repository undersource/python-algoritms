import numpy as np
import matplotlib.pyplot as plt

N = 100
dNoise = 1
dSignal = 5
r = 0.99
en = 0.1

M = 3
R = np.array([[r, 0, 0], [0, r, 0], [0, 0, r]])
Vksi = np.eye(M) * en
V = np.eye(M) * dNoise

x = np.zeros(N * M).reshape(N, M)
x[:][0] = np.random.normal(0, dSignal, M)

for i in range(1, N):
    x[:][i] = np.dot(R, x[:][i - 1]) + np.random.normal(0, en, M)

z = x + np.random.normal(0, dNoise, size=(N, M))

xx = np.zeros(N * M).reshape(N, M)
P = np.zeros(M * M).reshape(M, M)
xx[:][0] = z[:][0]
P = V

Vinv = np.linalg.inv(V)

for i in range(1, N):
    Pe = np.dot(np.dot(R, P), R.T) + Vksi
    P = np.dot(Pe, V) * np.linalg.inv(Pe + V)
    xe = np.dot(R, xx[:][i - 1])

fig, (axX, axY, axZ) = plt.subplots(nrows=3, ncols=1, figsize=(10, 6))

res = xx.reshape(M * N)
resX = x.reshape(M * N)
resZ = z.reshape(M * N)


axX.plot(resX[0:N * M:M])
axX.plot(resZ[0:N * M:M])
axX.plot(res[0:N * M:M])

axY.plot(resX[1:N * M:M])
axY.plot(resZ[1:N * M:M])
axY.plot(res[1:N * M:M])

axZ.plot(resX[2:N * M:M])
axZ.plot(resZ[2:N * M:M])
axZ.plot(res[2:N * M:M])


axX.set_ylabel('Axis X')
axY.set_ylabel('Axis Y')
axZ.set_ylabel('Axis Z')

axX.grid(True)
axY.grid(True)
axZ.grid(True)

plt.show()
