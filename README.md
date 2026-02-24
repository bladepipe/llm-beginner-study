# 🔑 LLM 入门学习仓库（精简教学版）

> 从字符统计到 GPT 建模，三步走通原理 —— **不依赖 GPU，纯 Python，中文注释，开箱即学**。

## 📚 学习路径（推荐顺序）
1. **【入门】`bigram_scratch.py`**  
   → 仅 1901 字节，实现 `P('e'|'h')` 统计与文本生成；  
   → [查看源码](bigram_scratch.py)｜[配套教学](LEARNING_GUIDE.md)

2. **【进阶】`projects/minGPT-light/tokenizer.py` & `embedding.py`**  
   → `tokenizer.py`: 将文本转为整数序列（`encode()`/`decode()`）；  
   → `embedding.py`: 将整数序列转为稠密向量（`nn.Embedding`）；  
   → [WEEK 2 概览](docs/WEEK2_OVERVIEW.md)｜[源码目录](projects/minGPT-light/)

3. **【进阶】`projects/minGPT-light/model.py`**  
   → 5675 字节，带中文注释的 minGPT 核心；  
   → 对比说明：`【进阶对比】这是 Bigram 的‘升级版’：不再只看前1个字符，而是用 self-attention 看整个上文`；  
   → [查看源码](projects/minGPT-light/model.py)

4. **【数据】`data/shakespeare.txt`**  
   → 2700 字节精简莎士比亚文本，可直接用于训练；  
   → [下载数据](data/shakespeare.txt)

5. **【规划】`docs/WEEK1_OVERVIEW.md`**  
   → 首周学习地图 + 3 张关键概念卡片（Tokenization / Attention / Autoregression）；  
   → [打开概览](docs/WEEK1_OVERVIEW.md)

## 🚀 快速开始
```bash
# 1. 运行入门模型
python bigram_scratch.py

# 2. 运行 WEEK 2 向量化示例
python -c "from projects.minGPT-light.tokenizer import Tokenizer; from projects.minGPT-light.embedding import Embedding; t=Tokenizer(); e=Embedding(); print(e(torch.tensor(t.encode('hello world'))).shape)"

# 3. 查看进阶模型结构
cat projects/minGPT-light/model.py

# 4. 训练你的第一个 GPT（CPU 可行）
cd projects/minGPT-light && python train.py --data_dir=../../data/
```

> 💡 **提示**：所有文件均无外部依赖，`pip install torch` 后即可运行 `minGPT-light`。