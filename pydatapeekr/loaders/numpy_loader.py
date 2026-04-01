"""NumPy file loaders."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from pydatapeekr.loaders.core import register_loader


def _require_numpy() -> Any:
    try:
        import numpy as np  # type: ignore
    except ImportError as exc:
        raise ImportError("numpy file loading requires numpy to be installed") from exc
    return np


def _unwrap_object_array(value: Any) -> Any:
    """Return the underlying Python object for 0-d object arrays."""
    dtype = getattr(value, "dtype", None)
    shape = getattr(value, "shape", None)
    if dtype == object and shape == ():
        return value.item()
    return value


def _load_numpy_file(np: Any, path: Path) -> Any:
    """Prefer safe loading and fall back to pickle-backed object arrays when needed."""
    try:
        return np.load(path, allow_pickle=False)
    except ValueError as exc:
        if "Object arrays cannot be loaded when allow_pickle=False" not in str(exc):
            raise
        return np.load(path, allow_pickle=True)


@register_loader(".npy")
def load_npy(path: Path) -> Any:
    """Load a NumPy array file."""
    np = _require_numpy()
    return _unwrap_object_array(_load_numpy_file(np, path))


@register_loader(".npz")
def load_npz(path: Path) -> dict[str, Any]:
    """Load a NumPy archive file into a plain mapping."""
    np = _require_numpy()
    with _load_numpy_file(np, path) as archive:
        return {key: _unwrap_object_array(archive[key]) for key in archive.files}
