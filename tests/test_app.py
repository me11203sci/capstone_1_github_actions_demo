import sys
from pathlib import Path

root = Path(file).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add

def test_add():
    assert add(3, 4) == 7