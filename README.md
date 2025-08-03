# DirFuzZ
```
Developed by thush
```
# 🔍 Python Async Directory & File Fuzzer

A fast and recursive directory + file fuzzing tool for web applications, written in Python using `aiohttp` and `asyncio`.

---

## 🚀 Features

- ✅ Async fuzzing with `aiohttp` for high performance
- 🔁 Recursive directory discovery (optional)
- 📄 File fuzzing with extensions
- 🧪 Custom status code filtering

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/python-fuzzer.git
cd python-fuzzer
uv venv
uv sync
```


python fuzz.py --url http://example.com/ \
  --word-list wordlist.txt \
  --status-codes 200,301,403 \
  -e php,html,txt \
  -r 2 \
  -fname files.txt


