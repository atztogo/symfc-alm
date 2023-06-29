"""Pytest conftest.py."""
from pathlib import Path

import numpy as np
from symfc_alm import read_dataset, DispForceDataset, CellDataset
import pytest


cwd = Path(__file__).parent


@pytest.fixture(scope="session")
def nacl_222_structure() -> CellDataset:
    """Return NaCl 2x2x2 supercell structure."""
    points = [
        [0.00, 0.00, 0.00],
        [0.50, 0.00, 0.00],
        [0.00, 0.50, 0.00],
        [0.50, 0.50, 0.00],
        [0.00, 0.00, 0.50],
        [0.50, 0.00, 0.50],
        [0.00, 0.50, 0.50],
        [0.50, 0.50, 0.50],
        [0.00, 0.25, 0.25],
        [0.50, 0.25, 0.25],
        [0.00, 0.75, 0.25],
        [0.50, 0.75, 0.25],
        [0.00, 0.25, 0.75],
        [0.50, 0.25, 0.75],
        [0.00, 0.75, 0.75],
        [0.50, 0.75, 0.75],
        [0.25, 0.00, 0.25],
        [0.75, 0.00, 0.25],
        [0.25, 0.50, 0.25],
        [0.75, 0.50, 0.25],
        [0.25, 0.00, 0.75],
        [0.75, 0.00, 0.75],
        [0.25, 0.50, 0.75],
        [0.75, 0.50, 0.75],
        [0.25, 0.25, 0.00],
        [0.75, 0.25, 0.00],
        [0.25, 0.75, 0.00],
        [0.75, 0.75, 0.00],
        [0.25, 0.25, 0.50],
        [0.75, 0.25, 0.50],
        [0.25, 0.75, 0.50],
        [0.75, 0.75, 0.50],
        [0.25, 0.25, 0.25],
        [0.75, 0.25, 0.25],
        [0.25, 0.75, 0.25],
        [0.75, 0.75, 0.25],
        [0.25, 0.25, 0.75],
        [0.75, 0.25, 0.75],
        [0.25, 0.75, 0.75],
        [0.75, 0.75, 0.75],
        [0.25, 0.00, 0.00],
        [0.75, 0.00, 0.00],
        [0.25, 0.50, 0.00],
        [0.75, 0.50, 0.00],
        [0.25, 0.00, 0.50],
        [0.75, 0.00, 0.50],
        [0.25, 0.50, 0.50],
        [0.75, 0.50, 0.50],
        [0.00, 0.25, 0.00],
        [0.50, 0.25, 0.00],
        [0.00, 0.75, 0.00],
        [0.50, 0.75, 0.00],
        [0.00, 0.25, 0.50],
        [0.50, 0.25, 0.50],
        [0.00, 0.75, 0.50],
        [0.50, 0.75, 0.50],
        [0.00, 0.00, 0.25],
        [0.50, 0.00, 0.25],
        [0.00, 0.50, 0.25],
        [0.50, 0.50, 0.25],
        [0.00, 0.00, 0.75],
        [0.50, 0.00, 0.75],
        [0.00, 0.50, 0.75],
        [0.50, 0.50, 0.75],
    ]
    lattice = np.eye(3) * 11.2811199999999996
    numbers = [11] * 32 + [17] * 32
    return CellDataset(lattice, points, numbers)


@pytest.fixture(scope="session")
def nacl_222_dataset() -> DispForceDataset:
    """Return NaCl 2x2x2 dataset."""
    return read_dataset(cwd / "FORCE_SETS_NaCl.xz")
