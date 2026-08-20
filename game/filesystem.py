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
                    fake_name, locked, password = self._parse_filename(
                        item.name
                    )

                    filesystem[fake_name] = {
                        "__file__": True,
                        "content": item.read_text(
                            encoding="utf-8",
                        ),
                        "locked": locked,
                        "password": password,
                        "real_path": item,
                    }

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

            if self._is_directory(item):
                print(f"[FOLDER] {name}")

            elif self._is_file(item):

                if item["locked"]:
                    print(f"[LOCKED] {name}")
                else:
                    print(f"[FILE]   {name}")

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

        if not self._is_directory(directory[location]):
            print(f"{location} is not a directory")
            return

        self.current_path.append(location)

    def view(self, filename):
        directory = self.get_current_directory()

        if filename not in directory:
            print(f"File not found: {filename}")
            return

        item = directory[filename]

        if self._is_directory(item):
            print(f"{filename} is a directory")
            return

        if item["locked"]:
            print()
            print("ACCESS DENIED")
            print("This file is password protected.")
            print(f"Use: unlock {filename}")
            print()
            return

        print()
        print("Item Content")
        print("===============")
        print()
        print(item["content"].strip())
        print()
        print("===============")
        print("End of Item Content")
        print()

    def reset(self):
        self.current_path = []

    def get_real_file_path(self, filename):
        directory = self.get_current_directory()

        if filename not in directory:
            return None

        item = directory[filename]

        if not self._is_file(item):
            return None

        if item["locked"]:
            return None

        return item["real_path"]

    def _is_file(self, item):
        return (
                isinstance(item, dict)
                and item.get("__file__") is True
        )


    def _is_directory(self, item):
        return (
                isinstance(item, dict)
                and not self._is_file(item)
        )

    def _parse_filename(self, filename):
        """
        Convert a real filename into the fake filename
        and determine whether it is password protected.

        Example:
            protocol_V5.lock-4821.txt

        becomes:
            protocol_V5.txt
            locked = True
            password = 4821
        """

        if ".lock-" not in filename:
            return filename, False, None

        name_before_lock, lock_data = filename.split(".lock-", 1)

        if "." not in lock_data:
            raise ValueError(
                f"Invalid locked filename: {filename}"
            )

        password, extension = lock_data.split(".", 1)

        fake_filename = f"{name_before_lock}.{extension}"

        return fake_filename, True, password.lower()

    def unlock(self, filename, password):
        directory = self.get_current_directory()

        if filename not in directory:
            print(f"File not found: {filename}")
            return False

        item = directory[filename]

        if self._is_directory(item):
            print(f"{filename} is a directory")
            return False

        if not item["locked"]:
            print(f"{filename} is already unlocked.")
            return True

        if password != item["password"]:
            print()
            print("ACCESS DENIED")
            print("Incorrect password.")
            print()
            return False

        item["locked"] = False

        print()
        print("ACCESS GRANTED")
        print(f"{filename} unlocked.")
        print()

        return True

