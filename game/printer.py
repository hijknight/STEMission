import subprocess
from pathlib import Path

def print_file(file_path):
    file = Path(file_path)

    if not file.exists():
        print(f"File not found: {file_path}")
        return False

    try:
        subprocess.run(
            ["lp", str(file_path)],
            check=True,
        )
    except subprocess.CalledProcessError:
        print(f"PRINT ERROR: Unable to submit print job.")
        return False