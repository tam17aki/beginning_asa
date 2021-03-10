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
# -「第1章 基礎知識」1.1 離散信号と波形の表示 の内容をPythonで再現

import matplotlib.pyplot as plt
import numpy as np

# A-D変換（連続信号→離散信号）

# 記録された数字が1, 3, -5, 2の場合
signal = np.array([1, 3, -5, 2])
time = np.arange(len(signal)) + 1  # 1を足すのはサンプル番号

# A-D変換における時間間隔 → 標本化周期
# 標本化周期の逆数 → 標本化周波数

# 波形を表示するときは matplotlib.pyplot のplot関数を使う
plt.plot(time, signal)
plt.grid()  # グリッド表示
plt.xlabel("Time (sample)")
plt.ylabel("Amplitude")
plt.show()

# 標本化周波数を10Hzとし, 横軸の単位を秒にする
samplerate = 10  # 標本化周波数 (Hz)
period = 1.0 / samplerate  # 標本化周期 (sec)
time = np.arange(len(signal)) * period
plt.plot(time, signal)
plt.grid()  # グリッド表示
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")
plt.show()
