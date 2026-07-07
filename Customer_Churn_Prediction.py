import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

print("Project environment is ready.")
print(f"Workspace root: {ROOT}")
