"""Helpers for numpy array inspection."""

from __future__ import annotations

from typing import Any


def ndarray_display_type(array: Any) -> str:
    """Return a compact one-line display label for a numpy ndarray."""
    return f"ndarray(shape={tuple(array.shape)}, dtype={getattr(array, 'dtype', 'unknown')})"


def summarize_ndarray(array: Any, *, max_items: int) -> dict[str, Any]:
    """Return summary metadata for a numpy ndarray."""
    return {
        "shape": list(array.shape),
        "dtype": str(array.dtype),
    }
