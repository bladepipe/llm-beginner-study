# 📘 学习指南（Learning Guide）

本指南按周组织，每章包含：
- ✅ **核心目标**（What）
- ✅ **为什么学**（Why）
- ✅ **立即实践**（How）

---

## WEEK 1: Bigram 基础

### ✅ What
构建字符级统计语言模型：给定前一个字符，预测下一个字符的概率。

### ✅ Why
- 是所有 LLM 的起点，理解 `P(next|prev)` 是建模本质；
- 无需神经网络，纯 Python 即可实现，适合零基础入门。

### ✅ How
```python
# bigram_scratch.py
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}
# ... 统计共现频次 → 构建 P('e'|'h')
```

---

## WEEK 2: 分词与嵌入（Tokenization & Embedding）

> ⚠️ 思考题：用 `bigram_scratch.py` 生成 ‘The quick brown fox jumps...’ —— 当生成到 ‘jumps’ 时，模型只看到 ‘s’，却要预测下一个词。它无法知道前面有 ‘fox’，更不知道 ‘quick’ 和 ‘brown’ 的修饰关系。这就是 Bigram 的‘短视’。而 `model.py` 中的 self-attention，正是为解决这个‘长程依赖’问题而生。

### ✅ What
将字符序列转换为整数序列（tokenization），再映射为稠密向量（embedding），为后续 self-attention 提供输入。

### ✅ Why
- Bigram 只能建模局部共现，无法捕捉语义；
- 向量表示使模型能学习 `"king" - "man" + "woman" ≈ "queen"` 这类关系；
- 是从统计模型迈向神经网络模型的唯一桥梁。

### ✅ How
```python
# projects/minGPT-light/tokenizer.py
from tokenizer import Tokenizer
t = Tokenizer()
ids = t.encode("hello world")  # → [36, 37, 38, 38, 39, 1, 56, 40, 41, 42, 43]

# projects/minGPT-light/embedding.py
from embedding import Embedding
e = Embedding(vocab_size=65, n_embd=32)
vecs = e(torch.tensor(ids))     # → (11, 32) 向量矩阵
```

> 💡 提示：`vocab_size=65` 来自 `tokenizer.chars` 长度，`n_embd=32` 是可调超参，值越小越轻量。