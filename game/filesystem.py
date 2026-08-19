from pathlib import Path

ALLOWED_FILE_TYPES = {
    ".txt",
    ".log",
    ".csv",
    ".md",
}

class FakeFileSystem:
    def __init__(self, root_path):
        self.root_path = Path(root_path)

        if not self.root_path.exists():
            raise FileNotFoundError(f"Game files directory does not exist: {self.root_path}")

        self.files = self._load_directory(self.root_path)

        self.current_path = []

    def _load_directory(self, path) -> dict:
        # Recursively convert real game_files folder into a fake filesystem

        filesystem = {}

        for item in sorted(path.iterdir()):
            if item.name.startswith("."):
                continue

            if item.is_dir():
                filesystem[item.name] = self._load_directory(item)

            elif item.is_file():
                if item.suffix.lower() not in ALLOWED_FILE_TYPES:
                    continue

                try:
                    filesystem[item.name] = item.read_text(
                        encoding="utf-8",
                    )

                except UnicodeDecodeError:
                    raise ValueError(
                        f"{item} must be saved as UTF-8"
                    )

        return filesystem

    def get_current_directory(self) -> dict:
        directory = self.files

        for folder in self.current_path:
            directory = directory[folder]

        return directory

    def get_path(self):
        if not self.current_path:
            return "/"

        return "/" + "/".join(self.current_path)

    def ls(self):
        directory = self.get_current_directory()

        for name, item in directory.items():

            if isinstance(item, dict):
                print(f"[DIR] {name}")

            else:
                print(f"[FILE] {name}")

    def cd(self, location):
        location = location.strip()

        if location == "/":
            self.current_path = []
            return

        if location == "..":
            if self.current_path:
                self.current_path.pop()

            return

        directory = self.get_current_directory()

        if location not in directory:
            print(f"Directory not found: {location}")
            return

        if not isinstance(directory[location], dict):
            print(f"{location} is not a directory")
            return

        self.current_path.append(location)

    def view(self, filename):
        directory = self.get_current_directory()

        if filename not in directory:
            print(f"File not found: {filename}")
            return

        item = directory[filename]
        if isinstance(item, dict):
            print(f"{filename} is a directory")
            return

        print()
        print(item.strip())
        print()

    def reset(self):
        self.current_path = []

