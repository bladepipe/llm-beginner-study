# WEEK 1: Bigram Foundations
> 💡 这是所有语言模型的起点：从统计共现（`bigram_scratch.py`）出发，走向 GPT 的自注意力。

---

| English | 中文 |
|---------|------|
| Predicts next char *only* from previous one: `(e|h)` | 仅由前一个字符预测下一个：`(e|h)` |
| no gradients. Just count & divide. | 无梯度。仅计数与除法。 |
| start — lookup — sample — repeat. | 开始 — 查表 — 采样 — 重复。 |

✅ 为什么从 Bigram 学起？
• 它暴露了语言建模最本质问题：如何定义“上下文”？
• 它让你亲手写出概率表，理解 `P('e'|'h')` 而非调用黑箱 API。

▶️ 立即实践：
`python bigram_scratch.py`
（无需安装任何包，直接运行）