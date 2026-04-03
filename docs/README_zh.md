# PyDataPeekr

PyDataPeekr 是一个用于探查嵌套数据文件和复杂 Python 对象结构的工具，支持清晰的树状输出和 Markdown 输出。

English README: [../README.md](../README.md)
完整 API 文档: [api_zh.md](api_zh.md)

## 1. 支持的文件后缀

`*.pkl` `*.pickle` `*.parquet` `*.json` `*.jsonl` `*.csv` `*.tsv` `*.yaml` `*.yml` `*.npy` `*.npz`

## 2. 安装方式

从 PyPI 安装稳定版：

```bash
pip install pydatapeekr
# 或者
uv pip install pydatapeekr
```

直接从仓库安装最新版（`beta`，可能不稳定）：

```bash
pip install "git+https://github.com/slkhms777/pydatapeekr.git"
# 或者
uv pip install "git+https://github.com/slkhms777/pydatapeekr.git"
```

## 3. CLI 用法

快速开始：

```bash
peek your_file_path
```

## 4. API 用法

```python
import pydatapeekr as peekr

print(peekr.inspect_file("data.json"))
```

更多 API 示例和完整说明请见 [api_zh.md](api_zh.md)。
