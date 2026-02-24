# 🔑 新手三问（精简版）

1. 什么是 Bigram 模型？  
P('e'|'h') —— 仅凭前一个字符预测下一个。如 `'h'→'e'` 在训练中占 60%，模型即学得 0.6。

2. 它如何“学习”？  
① 扫文本；② 统计 `'h'→'e'` 等频次；③ 归一化为概率（例：`'h'` 出现 20 次，`'e'` 跟 12 次 → 0.6）。

3. 如何生成文本？  
给 `'t'` → 查表得 `'h':0.62`, `'e':0.12` → 加权随机选 `'h'` → 再查 `'h'` 行 → 循环。  
→ 这就是 GPT 的自回归生成（autoregressive generation）。

---

### 💡 一看就懂的核心代码（Python）
```python
# Step 1: 统计所有相邻字符对
for i in range(len(text) - 1):
    current = text[i]      # 当前字符（上下文）
    next_ch = text[i + 1]  # 下一个字符（目标）
    counts[current][next_ch] += 1  # 计数 +1

# Step 2: 将计数转为概率（每个上下文独立归一化）
for current_char, next_dict in counts.items():
    total = sum(next_dict.values())
    probs[current_char] = {
        ch: cnt / total for ch, cnt in next_dict.items()
    }
```
*这就是全部：扫描 → 计数 → 除法 → 生成。没有魔法，只有统计。*