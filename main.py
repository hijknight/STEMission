from pathlib import Path

from game.authentication import login
from game.display import login_success, opening
from game.filesystem import FakeFileSystem
from game.terminal import Terminal

def main():

    project_root = Path(__file__).parent

    science_files = project_root / "science_files" # cells4L password
    bridge_files = project_root / "bridge_files"
    battery_files = project_root / "battery_files"



    while True:
        opening()

        login_info = login()

        username = login_info[0]
        password = login_info[1]

        login_success()

        if password.lower() == "cells4l":
            filesystem = FakeFileSystem(science_files)
        elif password.lower() == "bridgesarecool":
            filesystem = FakeFileSystem(bridge_files)
        else:
            filesystem = FakeFileSystem(battery_files)

        terminal = Terminal(filesystem)

        terminal.run(username)


if __name__ == '__main__':
    main()