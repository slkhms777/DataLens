# PyDataPeekr

PyDataPeekr is a Python tool for inspecting nested data files and complex in-memory objects with readable tree and Markdown output.

Chinese README: [docs/README_zh.md](docs/README_zh.md)
Full API guide: [docs/api.md](docs/api.md)

## Supported File Extensions

`*.pkl` `*.pickle` `*.parquet` `*.json` `*.jsonl` `*.csv` `*.tsv` `*.yaml` `*.yml` `*.npy` `*.npz`

## Installation

Stable release from PyPI:

```bash
pip install pydatapeekr
# or
uv pip install pydatapeekr
```

Latest version from the repository (`beta`, may be unstable):

```bash
pip install "git+https://github.com/slkhms777/pydatapeekr.git"
# or
uv pip install "git+https://github.com/slkhms777/pydatapeekr.git"
```

## CLI Usage

Quick Start:

```bash
peek your_file_path
```

## API Usage

```python
import pydatapeekr as peekr

print(peekr.inspect_file("data.json"))
```

For the full API reference and more examples, see [docs/api.md](docs/api.md).
