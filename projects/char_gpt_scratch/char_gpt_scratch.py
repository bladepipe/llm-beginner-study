#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
极简字符级 GPT（从零实现，无 PyTorch/TensorFlow）
功能：训练一个单层线性模型预测下一个字符
输入：'hello world' → 输出：'h'→'e', 'e'→'l', ... → 学习 P(next|context)
"""

import numpy as np
import random

# 1. 数据准备：用莎士比亚片段（简化）
text = "To be, or not to be, that is the question:\nWhether 'tis nobler in the mind to suffer\nThe slings and arrows of outrageous fortune,\nOr to take arms against a sea of troubles\nAnd by opposing end them. To die—to sleep,".lower()
chars = sorted(list(set(text)))
vocab_size = len(chars)
print(f'字符集大小: {vocab_size}, 字符: {"".join(chars)}')

# 2. 构建字符→索引映射
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}

# 3. 将文本转为索引序列
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])

data = np.array(encode(text), dtype=np.int32)

# 4. 构建训练数据：每步取前 8 个字符预测第 9 个（context_len=8）
context_len = 8
X, Y = [], []
for i in range(len(data) - context_len):
    X.append(data[i:i+context_len])
    Y.append(data[i+context_len])
X = np.array(X, dtype=np.int32)
Y = np.array(Y, dtype=np.int32)
print(f'训练样本数: {len(X)}')

# 5. 初始化权重（随机小值）
W = np.random.randn(vocab_size, vocab_size) * 0.01  # (vocab, vocab)

# 6. 训练循环（仅 100 步，演示用）
for step in range(100):
    # 随机选一个样本
    ix = random.randint(0, len(X)-1)
    x = X[ix]
    y = Y[ix]
    
    # 前向传播：x 最后一个字符的 logits
    logits = W[x[-1]]  # 只用最后一个字符（简化版）
    probs = np.exp(logits) / np.sum(np.exp(logits))
    
    # 反向传播（梯度 = probs - one_hot）
    one_hot = np.zeros(vocab_size)
    one_hot[y] = 1
    grad = probs - one_hot
    W[x[-1]] -= 0.1 * grad  # 学习率 0.1
    
    if step % 20 == 0:
        loss = -np.log(probs[y])
        print(f'Step {step}, Loss: {loss:.4f}')

# 7. 生成文本（从 't' 开始）
start_char = 't'
context = [stoi[start_char]]
print(f'\n生成开始: "{start_char}"')
for _ in range(50):
    # 取 context 最后一个字符的 logits
    logits = W[context[-1]]
    probs = np.exp(logits) / np.sum(np.exp(logits))
    next_idx = np.random.choice(len(probs), p=probs)
    context.append(next_idx)
print('生成结果:', decode(context))

# ✅ 这就是全部：数据→映射→训练→生成。没有魔法，只有统计与线性代数。
