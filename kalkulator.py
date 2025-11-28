import numpy as np
import matplotlib.pyplot as plt

# buat rentang nilai x (hindari titik yang menyebabkan tan tak terdefinisi)
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.tan(x)

plt.plot(x, y)
plt.ylim(-10, 10)  # batasi sumbu y biar grafik tidak terlalu ekstrem
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Grafik Fungsi tan(x)")
plt.xlabel("x")
plt.ylabel("tan(x)")
plt.grid(True)

plt.show()
