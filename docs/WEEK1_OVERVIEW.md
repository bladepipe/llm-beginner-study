# 📚 WEEK 1: Bigram Foundations

## 🧭 Learning Path (Text Diagram)

```
Shakespeare text
     ↓
Count pairs ('h'→'e')
     ↓
Normalize → P('e'|'h') = 0.6
     ↓
Sample → 'h' → 'e' → 'l' → ...
```

## 🗂️ Key Concept Cards

### 1. Bigram Model
- **EN**: Predicts next char *only* from previous one: `P(w_t | w_{t-1})`
- **中文**: 仅凭前一个字符预测下一个，如 `P('e'|'h')`

### 2. Counting Approach
- **EN**: No gradients. Just count & divide.
- **中文**: 无需梯度。只统计、再归一化。

### 3. Autoregressive Generation
- **EN**: Start → lookup → sample → repeat.
- **中文**: 起始 → 查表 → 采样 → 循环。

---
✅ Done. Next: Add `bigram_scratch.py`.