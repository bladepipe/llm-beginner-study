# WEEK 2: Tokenization & Embedding
> 💡 将字符序列转化为向量——Bigram 到 GPT 的关键跃迁。

---

| English | 中文 |
|---------|------|
| `encode()` / `decode()` | 把文本转为整数序列，再还原回来 |
| `nn.Embedding(vocab_size, n_embd)` | 把每个整数映射成一个稠密向量 |
| `shakespeare.txt` → `[1,27,3,...]` → `[[0.2,-0.8,...], ...]` | 数据流清晰可见 |

✅ 为什么是 WEEK 2？
• 它让模型“看见”语义，而不仅是统计共现；
• 它是 `minGPT-light/model.py` 中 `self.token_embedding_table` 的独立实现。

▶️ 立即实践：
```python
from projects.minGPT-light.tokenizer import Tokenizer
from projects.minGPT-light.embedding import Embedding

t = Tokenizer()
e = Embedding(vocab_size=65, n_embd=32)

ids = t.encode("hello world")
vecs = e(torch.tensor(ids))
print(vecs.shape)  # (11, 32)
```
