# LEARNING_GUIDE.md — Bigram 模型逐行教学（中英双语 · 带行号）

## 🔑 新手最应掌握的三个核心问题

### 1. 什么是 Bigram 模型？
A Bigram model is a language model that predicts the next character based *only* on the previous one. Formally, it models: `P('e' | 'h')`
For example, if after the letter `'h'` the letter `'e'` appears 60% of the time in training text, the model captures exactly that probability.

Bigram 模型是一种语言模型，它仅根据前一个字符预测下一个字符。形式上，它建模的是：
  `P('e' | 'h')`（即“在 `'h'` 之后出现 `'e'` 的概率”）
例如，若在训练文本中，字母 `'h'` 后面出现 `'e'` 的频率为 60%，该模型就精确捕获这一概率。

### 2. 它如何“学习”？
It doesn’t use gradients or neural networks. It simply:
- Scans the training text (e.g., Shakespeare)
- Counts how often each pair (`'h'→'e'`, `'e'→'l'`, etc.) appears
- Converts those counts into probabilities (e.g., `'h'→'e'`: 12 times out of 20 total `'h'` appearances = 0.6)

它不使用梯度或神经网络。它只做三件事：
- 扫描训练文本（如莎士比亚戏剧）
- 统计每一对字符（如 `'h'→'e'`、`'e'→'l'` 等）出现的次数
- 将这些计数转化为概率（例如：`'h'` 共出现 20 次，其中 12 次后面是 `'e'` → `P('e'|'h') = 12/20 = 0.6`）

### 3. 它如何生成文本？
Given a starting character (e.g., `'t'`), it:
- Looks up the probability table for `'t'` → e.g., `'h':0.62`, `'e':0.12`, `' ':0.09`
- Randomly picks the next character *weighted by those probabilities*
- Repeats: now `'h'` becomes the context, looks up its row, samples again…

给定一个起始字符（如 `'t'`），它会：
- 查询 `'t'` 对应的概率表 → 例如 `'h':0.62`、`'e':0.12`、`' ':0.09`
- 按这些概率加权随机选取下一个字符
- 重复该过程：此时 `'h'` 成为新上下文，查询其对应行，再次采样……

→ This is **autoregressive generation**, the core idea behind GPT.
→ 这就是**自回归生成**，也是 GPT 的核心思想。