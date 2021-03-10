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
# -「第1章 基礎知識」1.2 ベクトルと内積 の内容をPythonで再現

import numpy as np

# 縦ベクトル (column vector)
x = np.array([1, 3, -5, 2])

# 横ベクトル (row vector) 求め方その1
# 縦ベクトルをtransposeメソッドにより転置して横ベクトルにする
y = np.array([1, 3, -5, 2]).transpose()

# 横ベクトル (row vector) 求め方その1
# 縦ベクトルをtranspose関数により転置して横ベクトルにする
y = np.transpose(np.array([1, 3, -5, 2]))

# 内積 求め方その1 (arrayに付随したdotメソッド)
inner_product = x.dot(y)  # 39

# 内積 求め方その2 (Numpyのdot関数)
inner_product2 = np.dot(x, y)  # 39

# 内積 求め方その3 ( @ 演算子)
inner_product3 = x @ y  # 39
