"""High-level inspection entry points."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from pydatapeekr.formatters import format_inspection
from pydatapeekr.inspectors.core import analyze_object
from pydatapeekr.loaders import load_file


def inspect_obj(
    obj: Any,
    *,
    max_depth: int = 4,
    max_dict_items: int = 8,
    max_list_items: int = 1,
    show_sample: bool = False,
    format: str = "tree",
    write_to_file: str | Path | bool | None = None,
) -> str:
    """Inspect an in-memory object and render the result."""
    inspection = analyze_object(
        obj,
        max_depth=max_depth,
        max_dict_items=max_dict_items,
        max_list_items=max_list_items,
        show_sample=show_sample,
    )
    output = format_inspection(inspection, format=format)
    if write_to_file is not None:
        target = resolve_output_path(
            inspection_name="root",
            requested_path=write_to_file,
        )
        target.write_text(output, encoding="utf-8")
    return output


def display_obj(
    obj: Any,
    *,
    max_depth: int = 4,
    max_dict_items: int = 8,
    max_list_items: int = 1,
    show_sample: bool = False,
    format: str = "tree",
    style: str = "rule",
    stream: Any | None = None,
) -> str:
    """Inspect an in-memory object and print it with a terminal-friendly wrapper."""
    output = inspect_obj(
        obj,
        max_depth=max_depth,
        max_dict_items=max_dict_items,
        max_list_items=max_list_items,
        show_sample=show_sample,
        format=format,
        write_to_file=None,
    )
    wrapped = wrap_output(output, style=style)
    print(wrapped, file=stream or sys.stdout)
    return wrapped


def inspect_file(
    path: str | Path,
    *,
    max_depth: int = 4,
    max_dict_items: int = 8,
    max_list_items: int = 1,
    show_sample: bool = False,
    format: str = "tree",
    write_to_file: str | Path | bool | None = None,
) -> str:
    """Load a file, inspect it, and render the result."""
    input_path = Path(path)
    loaded = load_file(input_path)
    inspection = analyze_object(
        loaded,
        name=input_path.name,
        max_depth=max_depth,
        max_dict_items=max_dict_items,
        max_list_items=max_list_items,
        show_sample=show_sample,
    )
    output = format_inspection(inspection, format=format)
    if write_to_file is not None:
        target = resolve_output_path(
            inspection_name=input_path.name,
            requested_path=write_to_file,
            base_dir=input_path.parent,
        )
        target.write_text(output, encoding="utf-8")
    return output


def display_file(
    path: str | Path,
    *,
    max_depth: int = 4,
    max_dict_items: int = 8,
    max_list_items: int = 1,
    show_sample: bool = False,
    format: str = "tree",
    style: str = "rule",
    stream: Any | None = None,
) -> str:
    """Inspect a file and print it with a terminal-friendly wrapper."""
    output = inspect_file(
        path,
        max_depth=max_depth,
        max_dict_items=max_dict_items,
        max_list_items=max_list_items,
        show_sample=show_sample,
        format=format,
        write_to_file=None,
    )
    wrapped = wrap_output(output, style=style)
    print(wrapped, file=stream or sys.stdout)
    return wrapped


def wrap_output(text: str, *, style: str = "rule") -> str:
    """Wrap inspection text for clearer terminal display."""
    normalized = style.lower()
    if normalized == "plain":
        return text
    if normalized == "blank":
        return f"\n{text}\n"
    if normalized == "rule":
        line = "-" * 40
        return f"{line}\n{text}\n{line}"
    raise ValueError(f"Unsupported display style: {style}")


def resolve_output_path(
    *,
    inspection_name: str,
    requested_path: str | Path | bool,
    base_dir: str | Path | None = None,
) -> Path:
    """Resolve a writable output path for persisted inspection results."""
    if requested_path is True:
        target = Path(base_dir or ".") / f"data_info_{inspection_name}.txt"
    else:
        target = Path(requested_path)
    if target.suffix.lower() not in {".txt", ".md", ".markdown"}:
        raise ValueError("Output file must use one of: .txt, .md, .markdown")
    return target
