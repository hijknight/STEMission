from pathlib import Path

from game.authentication import login
from game.display import login_success, opening
from game.filesystem import FakeFileSystem
from game.terminal import Terminal

def main():

    project_root = Path(__file__).parent

    science_files = project_root / "science_files" # cell
    engineering_files = project_root / "engineering_files" # bridge
    technology_files = project_root / "technology_files" # battery

    while True:
        opening()

        login_info = login()

        username = login_info[0]
        password = login_info[1]

        login_success()

        if password.lower() == "cell":
            filesystem = FakeFileSystem(science_files)
        elif password.lower() == "bridge":
            filesystem = FakeFileSystem(engineering_files)
        else:
            filesystem = FakeFileSystem(technology_files)

        terminal = Terminal(filesystem)

        terminal.run(username)

if __name__ == '__main__':
    main()