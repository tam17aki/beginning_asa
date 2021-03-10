#!/usr/bin/env python3

""" ひたすら楽して音響信号解析 Python version. """

# MIT License

# Copyright (C) 2021 by Akira TAMAMORI

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Commentary:
# -「第1章 基礎知識」1.4 複素数 の内容をPythonで再現
# - 図の再現も含める
# - 参考 https://python.atelierkobato.com/ellipse/

import matplotlib.pyplot as plt
import numpy as np

# 複素数のプロット →複素平面（2次元平面）上の点としてプロット

# 単位円上、等間隔にn_points個の点を取って分割する
# 1周を2πとして、各thetaが角度に対応する（弧度法）
n_points = 1000
theta = np.linspace(0, 2 * np.pi, n_points)

# 円の中心座標
center = np.array([0, 0])

# 円の半径
radius = 0.9

# 円周上の 実部と虚部 (x座標とy座標)
circ_x = center[0] + radius * np.cos(theta)
circ_y = center[1] + radius * np.sin(theta)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel("Real part", fontsize=12)
ax.set_ylabel("Imag part", fontsize=12)
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

# 円をプロット
ax.plot(circ_x, circ_y, linewidth=2)

# 円内に取った複素数の実部と虚部
real = 0.8 * radius * np.cos(2 * np.pi * 70 / 360)
imag = 0.8 * radius * np.sin(2 * np.pi * 70 / 360)

# 原点と単位円を結ぶ直線をプロット
ax.plot([0, real], [0, imag], "black")
ax.scatter(real, imag, c="black", marker="o", s=30)

# テキストを配置（実軸上）
angle = 260
text_angle = angle * np.pi / 180
loc_x = real + 0.08 * np.cos(text_angle)
loc_y = 0.0 + 0.08 * np.sin(text_angle)
ax.text(loc_x, loc_y, "a", fontsize=14, color="black")

# テキストを配置（虚軸上）
angle = 200
text_angle = angle * np.pi / 180
loc_x = 0.0 + 0.08 * np.cos(text_angle)
loc_y = imag + 0.08 * np.sin(text_angle)
ax.text(loc_x, loc_y, "b", fontsize=14, color="black")

# 複素数から実軸に下ろした垂線
ax.plot([real, real], [0, imag], color="black", linestyle="--", linewidth=0.5)

# 複素数から虚軸に下ろした垂線
ax.plot([0, real], [imag, imag], color="black", linestyle="--", linewidth=0.5)

# 実軸の描画
ax.plot([-1.0, 1.0], [0, 0], color="black", linestyle="-", linewidth=0.8)
# 虚軸の描画
ax.plot([0, 0], [-1.0, 1.0], color="black", linestyle="-", linewidth=0.8)

plt.show()


# 複素数の例題
x = 3 + 4 * 1j  # 虚数単位は1j
r = np.abs(x)  # 絶対値
theta = np.angle(x)  # 偏角
print(r)
print(theta)
print(np.real(x))  # 実部を取り出す
print(np.imag(x))  # 虚部を取り出す

# 図1.4は省略
