# LLM Beginner Study

A gentle, hands-on path from Bigram to minGPT.

## 🔧 Quick Start
```bash
pip install -e .
python bigram_scratch.py
```

## 🐞 Common Issues & Fixes
- **`ModuleNotFoundError: No module named 'projects'`** → Run `pip install -e .` first (not `python setup.py install`).
- **`UnicodeDecodeError` on Windows** → Save `input.txt` as UTF-8 without BOM, or add `encoding='utf-8'` to `open()` calls.
- **`P(*|'x')` shows empty or zeros** → Check `input.txt` has at least 2 lines and contains repeated character pairs (e.g., `hello\nhello`).

---

[Full learning guide → LEARNING_GUIDE.md](LEARNING_GUIDE.md)