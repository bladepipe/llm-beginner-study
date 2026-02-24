# WEEK 1: Bigram Foundations
> 💡 这是所有语言模型的起点：从统计共现（`bigram_scratch.py`）出发，走向 GPT 的自注意力。

---

| English | 中文 |
|---------|------|
| Predicts next char *only* from previous one: `(e|h)` | 仅由前一个字符预测下一个：`(e|h)` |
| no gradients. Just count & divide. | 无梯度。仅计数与除法。 |
| start — lookup — sample — repeat. | 开始 — 查表 — 采样 — 重复。 |