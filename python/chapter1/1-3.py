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
# -「第1章 基礎知識」1.3 正弦波 の内容をPythonで再現

# 三角関数は音の信号解析で重要
# 正弦波 (sine wave, sinusoid) ：cosとsinの違いは位相差 (pi/2)

import numpy as np
from scipy.io import wavfile

OUT_WAVE_FILE = "1-3.wav"

n_framerate = 44100  # 標本化周波数 (Hz)
freq = 1000  # 正弦波の周波数 (Hz)
duration = 1  # 音の継続時間 (sec)
amplitude = 8000  # 正弦波の振幅 (amplitude)
period = 1.0 / n_framerate  # 標本化周期 (sec)

# 継続時間に等しい標本点の作成
# 0秒からduration秒までを、標本化周期periodで区切る
time = np.arange(0, duration, period)

# sin関数の引数はラジアンで与える必要あり
# 2πを掛けることで、1秒間の間に0から2π[rad]まで変化
sine_wave = amplitude * np.sin(2 * np.pi * freq * time)  # 正弦波を作成

# wavの書き込み (scipyモジュールを利用)
sine_wave = sine_wave.astype(np.int16)  # 16bit整数に変換
wavfile.write(OUT_WAVE_FILE, n_framerate, sine_wave)
